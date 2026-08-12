#!/usr/bin/env bash

set -euo pipefail

readonly SCRIPT_NAME=${0##*/}

LOG_FILE=
ALERT_THRESHOLD=10
WEBHOOK_URL=

die() {
  printf '[FATAL] %s\n' "$*" >&2
  exit 1
}

warn() {
  printf '[WARN] %s\n' "$*" >&2
}

info() {
  printf '[INFO] %s\n' "$*"
}

usage() {
  printf 'Usage: %s LOG_FILE [--alert-threshold N] [--webhook URL]\n' "$SCRIPT_NAME"
}

require_option_value() {
  local option=$1
  local count=$2
  ((count >= 2)) || die "$option requires a value"
}

parse_args() {
  (($# >= 1)) || {
    usage >&2
    exit 2
  }
  LOG_FILE=$1
  shift

  while (($# > 0)); do
    case $1 in
    --alert-threshold)
      require_option_value "$1" "$#"
      ALERT_THRESHOLD=$2
      shift 2
      ;;
    --webhook)
      require_option_value "$1" "$#"
      WEBHOOK_URL=$2
      shift 2
      ;;
    --help)
      usage
      exit 0
      ;;
    *)
      die "unknown argument: $1"
      ;;
    esac
  done

  [[ $ALERT_THRESHOLD =~ ^[0-9]+$ ]] ||
    die "--alert-threshold must be a non-negative integer"
  [[ -f $LOG_FILE && -r $LOG_FILE ]] || die "log file is not readable: $LOG_FILE"
}

line_count() {
  awk 'END { print NR + 0 }' "$LOG_FILE"
}

count_level() {
  local level=$1
  awk -v expected="[$level]" '$3 == expected { count++ } END { print count + 0 }' "$LOG_FILE"
}

print_level_distribution() {
  awk '
		$3 ~ /^\[(INFO|WARN|ERROR|FATAL)\]$/ {
			level = $3
			gsub(/^\[|\]$/, "", level)
			count[level]++
		}
		END {
			for (level in count) {
				printf "%d %s\n", count[level], level
			}
		}
	' "$LOG_FILE" | sort -rn
}

print_top_error_messages() {
  awk '
		$3 == "[ERROR]" || $3 == "[FATAL]" {
			$1 = $2 = $3 = ""
			sub(/^ +/, "")
			print
		}
	' "$LOG_FILE" | sort | uniq -c | sort -rn | head -5
}

is_second_half_denser() {
  local level=$1
  local total midpoint
  total=$(line_count)
  ((total >= 2)) || return 1
  midpoint=$((total / 2))

  awk -v expected="[$level]" -v midpoint="$midpoint" '
		NR <= midpoint && $3 == expected { first++ }
		NR > midpoint && $3 == expected { second++ }
		END {
			first_lines = midpoint
			second_lines = NR - midpoint
			if (first_lines == 0 || second_lines == 0) {
				exit 1
			}
			exit !((second + 0) * first_lines > (first + 0) * second_lines)
		}
	' "$LOG_FILE"
}

send_alert() {
  local message=$1
  [[ -n $WEBHOOK_URL ]] || return 0
  command -v jq >/dev/null || {
    warn "jq is unavailable; alert was not sent"
    return 0
  }
  command -v curl >/dev/null || {
    warn "curl is unavailable; alert was not sent"
    return 0
  }

  local payload
  payload=$(jq -n --arg text "[log alert] $message" '{text: $text}') || {
    warn "failed to build alert payload"
    return 0
  }
  curl -fsS --connect-timeout 3 --max-time 10 \
    -H 'Content-Type: application/json' --data "$payload" "$WEBHOOK_URL" >/dev/null ||
    warn "alert request failed"
}

main() {
  parse_args "$@"

  local total errors warns fatals severe
  total=$(line_count)
  errors=$(count_level ERROR)
  warns=$(count_level WARN)
  fatals=$(count_level FATAL)
  severe=$((errors + fatals))

  info "analyzing: ${LOG_FILE##*/}"
  printf '%s\n' \
    '========================================' \
    "lines:  $total" \
    "ERROR:  $errors" \
    "WARN:   $warns" \
    "FATAL:  $fatals" \
    "severe: $((severe * 100 / (total > 0 ? total : 1)))%" \
    '========================================'

  printf '\n%s\n' '--- level distribution ---'
  print_level_distribution

  printf '\n%s\n' '--- top severe messages ---'
  print_top_error_messages

  local level
  for level in ERROR WARN FATAL; do
    if is_second_half_denser "$level"; then
      printf '[NOTICE] %s density is higher in the second half of the file\n' "$level"
    fi
  done

  if ((severe >= ALERT_THRESHOLD)); then
    warn "severe count $severe reached threshold $ALERT_THRESHOLD"
    send_alert "severe count $severe reached threshold $ALERT_THRESHOLD (${LOG_FILE##*/})"
  fi
}

main "$@"
