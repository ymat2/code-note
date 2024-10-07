package main

import (
    "fmt"
    "flag"  // package to parse command-line arguments
)

func main() {
    // use flag.Type("Flag name", "Default value", "Help message")
    var name = flag.String("name", "Yuki", "Your name")

    var age int
    // or bind to variable using flag.TypeVar(%var, "Flag name", "Default value", "Help message")
    flag.IntVar(&age, "age", 25, "Your age")

    flag.Parse()

    // use pointer (*) in flagType, value in TypeVar
    fmt.Println(*name, age)
}
