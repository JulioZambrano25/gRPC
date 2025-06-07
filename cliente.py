import grpc
import user_pb2
import user_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        response = stub.GetUser(user_pb2.UserRequest(id=1))
        print(f"ID: {response.id}, Nombre: {response.name}, Email: {response.email}")

if __name__ == '__main__':
    run()
