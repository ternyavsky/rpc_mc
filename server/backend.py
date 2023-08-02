import rec_pb2_grpc
from rec_pb2 import HelloResponse
import grpc 
from concurrent import futures

class Greeter(rec_pb2_grpc.ServiceServicer):
    def SayHello(self, request, context):
        return HelloResponse(message=f"Microservis top! {request.name}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rec_pb2_grpc.add_ServiceServicer_to_server(
        Greeter(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()