package main

import (
    "database/sql"
    "fmt"
    "log"

    "context"

    "github.com/aws/aws-lambda-go/events"
    "github.com/aws/aws-lambda-go/lambda"

    _ "github.com/lib/pq"
)

func handler(ctx context.Context, request events.APIGatewayProxyRequest) error {
    log.Println("Using the postgres approach to query Redshift")

    // The postgres apporach
    // connStr := "postgres://krms user:pass@your-cluster:5439/dev"
    connStr := "redshift-cluster-1.cifidpdz4c7t.ap-northeast-2.redshift.amazonaws.com:5439/dev"
    log.Print(connStr)
    db, err := sql.Open("postgres", connStr)
    if err != nil {
        log.Fatal(err)
    } var (
        tablename string
    )

    // Query the database
    //q := "SELECT DISTINCT tablename FROM PG_TABLE_DEF WHERE schemaname = 'public';"
    q := "SELECT DISTINCT tablename FROM PG_TABLE_DEF WHERE 1=1;"
    rows, err := db.Query(q)
    if err != nil {
        log.Fatal(err)
    }
    log.Print(rows)
    defer rows.Close()

    // Print data to logs
    for rows.Next() {
        err := rows.Scan(&tablename)
        if err != nil {
            log.Fatal(err)
        }
        log.Println(tablename)
    }

    // Handle errors
    err = rows.Err()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(rows)

    return nil
}

func main() {
    lambda.Start(handler)
}
