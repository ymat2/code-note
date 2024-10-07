package main

import (
    "bufio"
    "fmt"
    "math/rand"
    "os"
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
    word_list := get_file_contents("words.list")
    rand.Seed(time.Now().UnixNano())
    randomWord := word_list[rand.Intn(len(word_list))]
    return randomWord
}

func get_file_contents(file_name string) []string {
    var file_contents []string
    file, err := os.Open(file_name)
    if err != nil {
        fmt.Println("Error opening file:", err)
        os.Exit(1)
    }
    defer file.Close()
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        word := scanner.Text()
        file_contents = append(file_contents, word)
    }
    if err := scanner.Err(); err != nil {
        fmt.Println("Error reading file:", err)
    }
    return file_contents
}
