from server import Server
from load_balancer import LoadBalancer
from simulator import Simulator
import random
from request import Request


servers = [
    Server("S1", weight=1),
    Server("S2", weight=2),
    Server("S3", weight=3)
]

load_balancer = LoadBalancer(servers)
def calculate_average_time(results):
    total_time = 0
    total_requests = 0

    for result in results:
        total_time += (
            result["average_time"]
            * result["requests_handled"]
        )

        total_requests += result["requests_handled"]

    if total_requests == 0:
        return 0

    return total_time / total_requests
def calculate_distribution(results):
    total_requests = sum(
        result["requests_handled"] for result in results
    )

    distribution = []

    for result in results:
        if total_requests == 0:
            percentage = 0
        else:
            percentage = (
                result["requests_handled"]
                / total_requests
            ) * 100

        distribution.append({
            "server_id": result["server_id"],
            "percentage": percentage
        })

    return distribution

simulator = Simulator(load_balancer)
requests = []

for i in range(10):
    processing_time = random.uniform(0.5, 2)
    request = Request(i + 1, processing_time)
    requests.append(request)

# Round Robin
print("\n\n===== ROUND ROBIN =====")

simulator.run(
    "round_robin",
    requests
)

round_robin_results = simulator.display_results()


# Reset before next experiment
load_balancer.reset()


# Least Connections
print("\n\n===== LEAST CONNECTIONS =====")

simulator.run(
    "least_connections",
     requests
)

least_connections_results = simulator.display_results()


# Reset before next experiment
load_balancer.reset()


# Weighted
print("\n\n===== WEIGHTED =====")

simulator.run(
    "weighted",
    requests
)

weighted_results = simulator.display_results()
print("\n\n================ COMPARISON ================")

print(
    f"{'Strategy':<25}"
    f"{'S1':<10}"
    f"{'S2':<10}"
    f"{'S3':<10}"
)

print("-" * 55)

print(
    f"{'Round Robin':<25}"
    f"{round_robin_results[0]['requests_handled']:<10}"
    f"{round_robin_results[1]['requests_handled']:<10}"
    f"{round_robin_results[2]['requests_handled']:<10}"
)

print(
    f"{'Least Connections':<25}"
    f"{least_connections_results[0]['requests_handled']:<10}"
    f"{least_connections_results[1]['requests_handled']:<10}"
    f"{least_connections_results[2]['requests_handled']:<10}"
)

print(
    f"{'Weighted':<25}"
    f"{weighted_results[0]['requests_handled']:<10}"
    f"{weighted_results[1]['requests_handled']:<10}"
    f"{weighted_results[2]['requests_handled']:<10}"
)
round_robin_distribution = calculate_distribution(
    round_robin_results
)

least_connections_distribution = calculate_distribution(
    least_connections_results
)

weighted_distribution = calculate_distribution(
    weighted_results
)
round_robin_average = calculate_average_time(
    round_robin_results
)

least_connections_average = calculate_average_time(
    least_connections_results
)

weighted_average = calculate_average_time(
    weighted_results
)


print("\n\n========== PERFORMANCE ==========")

print(
    f"Round Robin average time: "
    f"{round_robin_average:.2f} seconds"
)

print(
    f"Least Connections average time: "
    f"{least_connections_average:.2f} seconds"
)

print(
    f"Weighted average time: "
    f"{weighted_average:.2f} seconds"
)
print("\n\n========== LOAD DISTRIBUTION (%) ==========")

print(
    f"{'Strategy':<25}"
    f"{'S1':<10}"
    f"{'S2':<10}"
    f"{'S3':<10}"
)

print("-" * 55)

print(
    f"{'Round Robin':<25}"
    f"{round_robin_distribution[0]['percentage']:<10.1f}"
    f"{round_robin_distribution[1]['percentage']:<10.1f}"
    f"{round_robin_distribution[2]['percentage']:<10.1f}"
)

print(
    f"{'Least Connections':<25}"
    f"{least_connections_distribution[0]['percentage']:<10.1f}"
    f"{least_connections_distribution[1]['percentage']:<10.1f}"
    f"{least_connections_distribution[2]['percentage']:<10.1f}"
)

print(
    f"{'Weighted':<25}"
    f"{weighted_distribution[0]['percentage']:<10.1f}"
    f"{weighted_distribution[1]['percentage']:<10.1f}"
    f"{weighted_distribution[2]['percentage']:<10.1f}"
)