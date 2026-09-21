// https://coolshell.cn/articles/21214.html

// IoC – Inversion of Control

package main

import (
	"fmt"
)

type Widget struct {
	X, Y int
}
type Label struct {
	Widget        // Embedding (delegation)
	Text   string // Aggregation
}

type Button struct {
	Label // Embedding (delegation)
}

func NewButton(x, y int, text string) Button {
	return Button{Label{Widget{x, y}, text}}
}

type ListBox struct {
	Widget          // Embedding (delegation)
	Texts  []string // Aggregation
	Index  int      // Aggregation
}

type Painter interface {
	Paint()
}

type Clicker interface {
	Click()
}

func (label Label) Paint() {
	fmt.Printf("%p:Label.Paint(%q)\n", &label, label.Text)
}

// 因为这个接口可以通过 Label 的嵌入带到新的结构体，
// 所以，可以在 Button 中可以重载这个接口方法以
func (button Button) Paint() { // Override
	fmt.Printf("Button.Paint(%s)\n", button.Text)
}
func (button Button) Click() {
	fmt.Printf("Button.Click(%s)\n", button.Text)
}

func (listBox ListBox) Paint() {
	fmt.Printf("ListBox.Paint(%q)\n", listBox.Texts)
}
func (listBox ListBox) Click() {
	fmt.Printf("ListBox.Click(%q)\n", listBox.Texts)
}

func t1() {
	label := Label{Widget{20, 70}, "label"}
	button1 := Button{Label{Widget{10, 70}, "OK"}}
	button2 := NewButton(50, 70, "Cancel")
	listBox := ListBox{Widget{10, 40},
		[]string{"AL", "AK", "AZ", "AR"}, 0}

	for _, painter := range []Painter{label, listBox, button1, button2} {
		painter.Paint()
	}

	for _, widget := range []interface{}{label, listBox, button1, button2} {
		widget.(Painter).Paint()
		if clicker, ok := widget.(Clicker); ok {
			clicker.Click()
		}
		fmt.Println() // print a empty line
	}
}

// ================================================================
// 反转控制

type IntSet struct {
	data map[int]bool
}

func NewIntSet() IntSet {
	return IntSet{make(map[int]bool)}
}
func (set *IntSet) Add(x int) {
	set.data[x] = true
}
func (set *IntSet) Delete(x int) {
	delete(set.data, x)
}
func (set *IntSet) Contains(x int) bool {
	return set.data[x]
}

func main() {
	// t1()

}
