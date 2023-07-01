
package main

import (
  "fmt"

  "github.com/eiannone/keyboard"
)

func main() {
  //tty, err := tty.Open()
  //if err != nil {
    //log.Fatal(err)
  //}
  //defer tty.Close()
//
  //for {
    //r, err := tty.ReadRune()
    //if err != nil {
      //log.Fatal(err)
    //}
    //fmt.Println("Key press => " + string(r))
  //}
  char, _, err := keyboard.GetSingleKey()
  if (err != nil) {
    panic(err)
  }
  fmt.Printf("You pressed: %q\r\n", char)
}
