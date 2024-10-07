package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
	file, err := os.Open("words.list")
	// Check error. Show error message and exit when cannot open file.
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	// defer: delay excusion of file.Close() until main() ends.
	defer file.Close()

    scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		charCount := len(line)
		fmt.Printf("Line: %s (Length: %d characters)\n", line, charCount)
	}

    // Check error while file scanning
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}
}
