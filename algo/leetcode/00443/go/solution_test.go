package main

import (
	"strings"
	"testing"
)

func TestCompress(t *testing.T) {
	tests := []struct {
		name  string
		chars []byte
		want  string
	}{
		{name: "示例 1", chars: []byte("aabbccc"), want: "a2b2c3"},
		{name: "示例 2", chars: []byte("a"), want: "a"},
		{name: "示例 3", chars: []byte("a" + strings.Repeat("b", 12)), want: "ab12"},
		{name: "最紧的情况 run=2", chars: []byte("aa"), want: "a2"},
		{name: "无重复", chars: []byte("abc"), want: "abc"},
		{name: "两位数长度", chars: []byte(strings.Repeat("a", 11)), want: "a11"},
		{name: "三位数长度", chars: []byte(strings.Repeat("a", 100)), want: "a100"},
		{name: "最大长度", chars: []byte(strings.Repeat("a", 2000)), want: "a2000"},
		{name: "输入本身含数字字符", chars: []byte("112233"), want: "122232"},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			chars := append([]byte(nil), test.chars...)
			n := compress(chars)
			if got := string(chars[:n]); got != test.want {
				t.Errorf("compress(%q) -> %q, want %q", test.chars, got, test.want)
			}
		})
	}
}
