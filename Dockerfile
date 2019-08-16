FROM golang:alpine 

RUN mkdir -p $GOPATH/src/github.com/ctreminiom/h-mandiola-api/

WORKDIR $GOPATH/src/github.com/ctreminiom/h-mandiola-api/

COPY . .

RUN CGO_ENABLED=0 go build -a -v

EXPOSE 8000

ENTRYPOINT ["./h-mandiola-api"]
