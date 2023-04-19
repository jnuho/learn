package main

import (
    _ "github.com/lib/pq"
    "database/sql"
    "fmt"
)

func MakeRedshiftConnection(username, password, host, port, dbName string) (*sql.DB, error) {

    url := fmt.Sprintf("sslmode=require user=%v password=%v host=%v port=%v dbname=%v",
        username,
        password,
        host,
        port,
        dbName)

    var err error
    var db *sql.DB
    if db, err = sql.Open("postgres", url); err != nil {
        return nil, fmt.Errorf("redshift connect error : (%v)", err)
    }

    if err = db.Ping(); err != nil {
        return nil, fmt.Errorf("redshift ping error : (%v)", err)
    }
    return db, nil
}

func main() {
  db, err := MakeRedshiftConnection(
    "krms",
    "Kaon.1234",
    "redshift-cluster-1.cifidpdz4c7t.ap-northeast-2.redshift.amazonaws.com",
    "5439",
    "dev")
  
  if err != nil {
    fmt.Println("Error-1")
    panic(err)
  }

  err = db.Ping()
  if err != nil {
    fmt.Println("Error-2")
    panic(err)
  }

  fmt.Println(db)
  fmt.Println(err)

  rows, err := db.Query("SELECT * FROM dev.public.category;")
  if err != nil {
    fmt.Println(err)
  }
  defer rows.Close()

  fmt.Println(rows)
}
