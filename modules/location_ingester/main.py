import grpc
import location_pb2
import location_pb2_grpc

from concurrent import futures

from helper import publish_location


class LocationProducerServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        payload = {
            "person_id": int(request.person_id),
            "latitude": request.latitude,
            "longitude": request.longitude
        }

        print("Payload - %s", payload)

        publish_location(payload)
        return location_pb2.LocationMessage(**payload)


# Initialise gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationProducerServicer(), server)

print("Starting gRPC server on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

# Keep thread alive
server.wait_for_termination()
# try:
#     while True:
#         time.sleep(86400)
# except KeyboardInterrupt:
#     server.stop(0)