package main

import (
    "fmt"
    "github.com/ymat2/mygo"
)

func main() {
    var my_name string = "Taro"
    msg := mygo.Hello(my_name)
    fmt.Println(msg)
}
