package main

import "fmt"

func main() {
	/*Standard out*/
	fmt.Println("Hello, world")

	/*Declaring variables*/
	var name string = "John"
	var i = 3
	j := 4
	fmt.Println("My name is" + name)
	fmt.Println(i*j)

	/*AND-OR*/
	if (true && false) {fmt.Println("true and false")}
	if (true || false) {fmt.Println("true or false")}
	if (true && !true) {fmt.Println("true and not true")}
	if (true || !true) {fmt.Println("true or not true")}

	k := 8
	fmt.Println(ifelse(k))

	n := 3
	fmt.Println(swtch(n))
	fmt.Println(even_or_odd(n))

	/*Looping*/
	for i:=0; i<5; i++ {
		fmt.Println(i, "Hello, world")
	}

}

func ifelse(i int) string {
	if i>10 {
		state := "var>10"
		return state
	} else if i>8 {
		state :="var>8"
		return state
	} else {
		state := "var<=8"
		return state
	}
}

func swtch(n int) string {
	switch n {
		case 1:
			return "n is 1"
		case 2,3 :
			return "n is 2 or 3"
		default :
			return "n is not 1,2,3"
	}
}

func even_or_odd(i int) string {
	var state string
	if i%2 == 0 {
		state = "Number is even."
	} else {
		state = "Number is odd."
	}
	return state
}
