import random
import threading

from request import Request


class Simulator:

    def __init__(self, load_balancer):
        self.load_balancer = load_balancer

    def run(self, strategy, requests):
       threads = []

       for request in requests:

           if strategy == "round_robin":
              server = self.load_balancer.round_robin()

           elif strategy == "least_connections":
            server = self.load_balancer.least_connections()

           elif strategy == "weighted":
            server = self.load_balancer.weighted()

           else:
            print("Invalid strategy")
            return

           thread = threading.Thread(
            target=server.process_request,
            args=(request.request_id, request.processing_time)
           )

           thread.start()
           threads.append(thread)

       for thread in threads:
        thread.join()
    def display_results(self):
        print("\n========== RESULTS ==========")

        results = []

        for server in self.load_balancer.servers:

            stats = server.get_statistics()

            print(f"\nServer: {stats['server_id']}")

            print(
               f"Requests handled: "
               f"{stats['requests_handled']}"
            )

            print(
                f"Average processing time: "
                f"{stats['average_time']:.2f} seconds"
            )

            print(
                f"Active connections: "
                f"{stats['active_connections']}"
            )

            results.append(stats)

        return results