package main

import (
  "fmt"
  "os"
  "time"
  "os/exec"
)

func main() {
  ch := make(chan string)
  go func(ch chan string) {
    // disable input buffering
    exec.Command("stty", "-F", "/dev/tty", "cbreak", "min", "1").Run()
    // do not display entered characters on the screen
    exec.Command("stty", "-F", "/dev/tty", "-echo").Run()
    var b []byte = make([]byte, 1)
    for {
      os.Stdin.Read(b)
      ch <- string(b)
    }
  }(ch)

  for {
    select {
      case stdin, _ := <-ch:
        fmt.Println("Keys pressed:", stdin)
      default:
        fmt.Println("Working..")
    }
    time.Sleep(time.Millisecond * 100)
  }
}

