#!/usr/bin/env bash

set -euo pipefail

readonly SCRIPT_NAME=${0##*/}

LOG_FILE=
ALERT_THRESHOLD=10
WEBHOOK_URL=
TOP=5

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
  printf 'Usage: %s LOG_FILE [--alert-threshold N] [--webhook URL] [--top N]\n' "$SCRIPT_NAME"
}

require_option_value() {
  local option=$1
  local count=$2
  ((count >= 2)) || die "$option requires a value"
}

parse_args() {
  while (($# > 0)); do
    case $1 in
    --help | -h)
      usage
      exit 0
      ;;
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
    --top)
      require_option_value "$1" "$#"
      TOP=$2
      shift 2
      ;;
    --*)
      die "unknown argument: $1"
      ;;
    *)
      [[ -z $LOG_FILE ]] || die "unexpected positional argument: $1"
      LOG_FILE=$1
      shift
      ;;
    esac
  done

  [[ -n $LOG_FILE ]] || {
    usage >&2
    exit 2
  }
  [[ $ALERT_THRESHOLD =~ ^0*([0-9]{1,9})$ ]] ||
    die "--alert-threshold must be an integer from 0 to 999999999"
  ALERT_THRESHOLD=$((10#${BASH_REMATCH[1]}))
  [[ $TOP =~ ^0*([0-9]{1,3})$ ]] ||
    die "--top must be an integer from 1 to 100"
  TOP=$((10#${BASH_REMATCH[1]}))
  ((TOP >= 1 && TOP <= 100)) || die "--top must be an integer from 1 to 100"
  if [[ -n $WEBHOOK_URL ]]; then
    case $WEBHOOK_URL in
    http://* | https://*) ;;
    *) die "--webhook must use http:// or https://" ;;
    esac
  fi
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
	' "$LOG_FILE" | LC_ALL=C sort -k1,1nr -k2,2
}

print_top_error_messages() {
  awk '
		$3 == "[ERROR]" || $3 == "[FATAL]" {
			$1 = $2 = $3 = ""
			sub(/^ +/, "")
			print
		}
	' "$LOG_FILE" |
    LC_ALL=C sort |
    uniq -c |
    LC_ALL=C sort -k1,1nr -k2,2 |
    awk -v limit="$TOP" 'NR <= limit'
}

is_second_half_denser() {
  local level=$1
  local total midpoint
  total=$(line_count) || return 2
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
  if ! curl -fsS --connect-timeout 3 --max-time 10 \
    --proto '=http,https' --header 'Content-Type: application/json' \
    --data-binary "$payload" --url "$WEBHOOK_URL" >/dev/null; then
    warn "alert request failed" || true
  fi
  return 0
}

main() {
  parse_args "$@"

  local total errors warns fatals severe
  total=$(line_count) || die "failed to count log lines"
  errors=$(count_level ERROR) || die "failed to count ERROR lines"
  warns=$(count_level WARN) || die "failed to count WARN lines"
  fatals=$(count_level FATAL) || die "failed to count FATAL lines"
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

  local level status
  for level in ERROR WARN FATAL; do
    if is_second_half_denser "$level"; then
      printf '[NOTICE] %s density is higher in the second half of the file\n' "$level"
    else
      status=$?
      ((status == 1)) || die "failed to compare $level density"
    fi
  done

  if ((severe >= ALERT_THRESHOLD)); then
    warn "severe count $severe reached threshold $ALERT_THRESHOLD"
    send_alert "severe count $severe reached threshold $ALERT_THRESHOLD (${LOG_FILE##*/})"
  fi
}

main "$@"
