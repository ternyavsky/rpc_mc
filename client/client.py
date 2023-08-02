import rec_pb2, rec_pb2_grpc
import grpc

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = rec_pb2_grpc.ServiceStub(channel)
        res = stub.SayHello(rec_pb2.HelloRequest(name="python"))
        print(res.message)


if __name__ == "__main__":
    main()