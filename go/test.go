package main

import "fmt"

func main() {
	var a = [5]string{"a", "b", "c", "d", "e"}
    for i,v := range a {
        fmt.Printf("%d th Alphabet is %s\n", i+1, v)
    }
}
