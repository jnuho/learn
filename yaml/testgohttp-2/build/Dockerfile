FROM golang:1.17-alpine as builder

WORKDIR /app

COPY . .

RUN go build -o main .

EXPOSE 8081

CMD ["./main"]
