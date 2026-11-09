"""The Python implementation of gRPC helloworld.Greeter client."""

import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    # Note (gRPC Python team): .close() is possible on a channel and should be
    # used in circunstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
        print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()