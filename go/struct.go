package main

import "fmt"


func main() {
	var neko Cat
	neko.name = "Draemon"
	neko.age = 10

	fmt.Println(neko.intro("Nobita"))

	neko2 := Cat{age: 5, name: "Cat"}
	neko2.meow()
}


type Cat struct {
	name string
	age int
}


func (c Cat) intro(partner string) string {
	return "Hey, " + partner + ", I am " + c.name + "."
}


func (c Cat) meow() {
	for i:=0; i<c.age; i++ {
		fmt.Println("Meow~~")
	}
}
