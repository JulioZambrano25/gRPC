import grpc
from concurrent import futures
import time

import user_pb2
import user_pb2_grpc

# Implementación del servicio
class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        # Aquí podrías consultar una base de datos; usamos datos simulados
        users = {
            1: {"name": "Alice", "email": "alice@example.com"},
            2: {"name": "Bob", "email": "bob@example.com"}
        }
        user = users.get(request.id, {"name": "Desconocido", "email": "N/A"})
        return user_pb2.UserResponse(id=request.id, name=user["name"], email=user["email"])

# Crear servidor
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC corriendo en el puerto 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
