import time
import threading


class Server:
    def __init__(self, server_id, weight=1):
        self.server_id = server_id
        self.weight = weight
        self.active_connections = 0
        self.requests_handled = 0
        self.total_processing_time = 0

        self.lock = threading.Lock()

    def process_request(self, request_id, processing_time):
        with self.lock:
            self.active_connections += 1

        print(
            f"Request {request_id} -> Server {self.server_id}"
        )

        start_time = time.time()

        time.sleep(processing_time)

        end_time = time.time()

        with self.lock:
            self.active_connections -= 1
            self.requests_handled += 1
            self.total_processing_time += end_time - start_time

        print(
            f"Request {request_id} completed by Server {self.server_id}"
        )
    def get_statistics(self):
        with self.lock:
            if self.requests_handled == 0:
                average_time = 0
            else:
                average_time = (
                    self.total_processing_time
                    / self.requests_handled
                )

            return {
                "server_id": self.server_id,
                "requests_handled": self.requests_handled,
                "average_time": average_time,
                "active_connections": self.active_connections
            }
    def reset_statistics(self):
        with self.lock:
         self.active_connections = 0
         self.requests_handled = 0
         self.total_processing_time = 0    