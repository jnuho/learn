package main

import (
  //"fmt"
  //"net/http"
  //"os"
  echo "github.com/labstack/echo/v4"
)


func main() {
  // create a new echo instance
  e := echo.New()
  //QueryParam along with PathVariable Get API
  //e.GET("/cats/:data",GetCats)
  e.GET("/:data",nil)
  //Post Request
  //e.POST("/cats", AddCat)
  e.Logger.Fatal(e.Start(":8080"))
}
