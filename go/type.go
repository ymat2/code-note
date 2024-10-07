package main

import (
    "fmt"
    "math/rand"
    "time"
)

func main() {
    var a string
    var score, total int64 = 0, 0
    const (
        Reset  = "\033[0m"
        Red    = "\033[31m"
        Green  = "\033[32m"
        Yellow = "\033[33m"
        Blue   = "\033[34m"
        Purple = "\033[35m"
        Cyan   = "\033[36m"
        White  = "\033[37m"
    )

    for true {
        var answer string = generate_random_word()
        fmt.Print(answer, ": ")
        fmt.Scan(&a)

        if a == "q" {
            fmt.Println("\nYour score:", score, "/", total, "\n")
            break
        } else {
            if a == answer {
                fmt.Println(Green, "Correct! +1", Reset)
                score = score + 1
                total = total + 1
            } else {
                fmt.Println(Red, "Wrong!", Reset)
                total = total + 1
            }
        }
    }
}

func generate_random_word() string {
    word_list := []string {
        "function", "variable", "constant", "loop", "condition",
        "array", "object", "class", "method", "inheritance",
        "polymorphism", "encapsulation", "constructor", "destructor",
        "recursion", "pointer", "reference", "argument", "parameter",
        "return", "value", "error", "exception", "try", "catch",
        "throw", "finally", "initialize", "iterate", "compile",
        "execute", "syntax", "semantic", "statement", "expression",
        "operator", "operand", "module", "package", "import", "export",
        "interface", "abstract", "override", "overload", "static",
        "dynamic", "null", "boolean", "integer", "float", "string",
        "char", "double", "byte", "enum", "struct", "union", "typedef",
        "library", "framework", "dependency", "thread", "process",
        "queue", "stack", "heap", "tree", "graph", "hash", "map",
        "set", "key", "value", "algorithm", "search", "sort", "filter",
        "merge", "split", "concat", "shift", "pop", "push", "insert",
        "delete", "update", "query", "index", "lock", "unlock",
        "synchronize", "allocate", "free", "bind", "connect",
        "disconnect", "read", "write", "input", "output", "encode",
        "decode", "python", "apptainer", "{", "}", "(", ")", "&", "$",
    }

    rand.Seed(time.Now().UnixNano())
    randomWord := word_list[rand.Intn(len(word_list))]

    return randomWord
}
