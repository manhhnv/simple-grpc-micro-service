from config import load
from concurrent import futures
from service.gpt import GPTService
from proto import server_pb2_grpc
from time import sleep
import grpc


config = load()
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
server_pb2_grpc.add_NlpServerServicer_to_server(GPTService(), server)
server.add_insecure_port(f"[::]:{config.PORT}")
server.start()
print(f"Server started [::]:{config.PORT}")

try:
    while True:
        sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
