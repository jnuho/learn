package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter,  r *http.Request) {
		fmt.Fprintf(w, "Hello World-3")
	})

	http.ListenAndServe(":8081", nil)
}

