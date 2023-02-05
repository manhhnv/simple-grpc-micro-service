package main

import (
	"context"
	"flag"
	"log"
	"time"

	pb "client/proto"

	"google.golang.org/grpc"
	// "google.golang.org/grpc/credentials/insecure"
)

const (
	defaultName = "world"
)

var (
	addr = flag.String("addr", "localhost:50051", "the address to connect to")
	name = flag.String("name", defaultName, "Name to greet")
)

func main() {
	flag.Parse()
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewNlpServerClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	r, err := c.CorrectGrammar(ctx, &pb.CorrectGrammarRequest{
		Transcript: "She no went to the market.",
	})
	if err != nil {
		log.Fatalf("could not greet: %v", err.Error())
	}
	log.Printf("Greeting: %s - %s - %s", r.Type, r.CorrectTranscript, r.Message.Value)
}
