package main
import(
  "fmt"
  "strings"
)

func main() {
  fmt.Println(strings.Count("Cheese", "e"))
	fmt.Println(strings.Count("Cheese", "ee"))
  fmt.Println(strings.Count("Cheeese", "ee"))
}
