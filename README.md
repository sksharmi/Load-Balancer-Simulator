** Load Balancer Simulator**

**Project Overview**

The Load Balancer Simulator is a Python-based project that simulates how incoming requests are distributed among multiple servers.

The project implements three load balancing strategies:

1. Round Robin
  
2. Least Connections
 
3. Weighted Load Balancing

The simulator uses Object-Oriented Programming (OOP) and Python threading to simulate concurrent request processing.

---

** Objectives**

The main objectives of this project are:

- Simulate multiple servers handling client requests.
  
- Implement different load balancing strategies.
  
- Compare how requests are distributed among servers.

- Use multithreading for concurrent request processing.
  
- Collect server performance statistics.
  
- Display load distribution percentages.

---

**Technologies Used**

- Python
  
- Object-Oriented Programming (OOP)
  
- Multithreading
  
- Greedy Scheduling Concepts

---

** Project Structure**

load-balancer-simulator

├── server.py

├── request.py

├── load_balancer.py

├── simulator.py

├── main.py

└── README.md

**File Description**

**server.py**

Contains the Server class.

Each server stores:

Server ID

Weight

Active connections

Number of requests handled

Total processing time

It also processes requests using threading.

**request.py**

Contains the Request class.

Each request has:

Request ID

Processing time

**load_balancer.py**

Contains the LoadBalancer class.

It implements:

1.Round Robin

2.Least Connections

3.Weighted Load Balancing

**simulator.py**

Contains the Simulator class.

It:

.Sends requests to selected servers.

.Creates threads for concurrent processing.

.Waits for all requests to complete.

.Displays server statistics.

**main.py**

This is the main program.

It:

.Creates servers

.Generates requests

.Runs all three load balancing strategies.

.Collects results.

.Compares request distribution.

.Calculates average processing time.

.Displays load distribution percentages.

**"Load Balancing Strategies":**

*1. Round Robin*

Round Robin distributes requests sequentially among the servers.

Example:

Request 1 → S1

Request 2 → S2

Request 3 → S3

Request 4 → S1

Request 5 → S2

This provides a simple and cyclic distribution of requests.

*2. Least Connections*

Least Connections selects the server that currently has the fewest active connections.

Example:

S1 → 2 active connections

S2 → 1 active connections

S3 → 3 active connections

Next request → S2

This strategy considers the current workload of each server.

*3. Weighted Load Balancing*

Each server is assigned a weight.

In this project:

S1 → Weight 1

S2 → Weight 2

S3 → Weight 3

The implementation uses the server weight together with its active connections to calculate a selection score.

Higher-weight servers can receive more requests.

**Multithreading**

.Python's threading module is used to simulate multiple requests being processed concurrently.

.For each request, the simulator creates a thread:

thread = threading.Thread(

    target=server.process_request,
    
    args=(request.request_id, request.processing_time)
)

The thread starts the request processing:

thread.start()

After all threads are created, the simulator waits for them:

thread.join()

This allows the project to simulate concurrent request handling.

**Fair Comparison**

.The same set of 10 requests is used for all three strategies.

.Each request is created once with a random processing time:

.processing_time = random.uniform(0.5, 2)

The same requests are then passed to:

1.Round Robin

2.Least Connections

3.Weighted

This makes the comparison more consistent because every strategy receives the same workload.

Performance Metrics

The simulator collects the following statistics:

Requests Handled

Number of requests processed by each server.

Average Processing Time

Average processing time of requests handled by each server.

Active Connections

Number of requests currently being processed.

Load Distribution

The percentage of total requests handled by each server.

The distribution is calculated using:

Request Distribution =

(Server Requests / Total Requests) × 100

**Sample Output**

Example:

================ COMPARISON ================

Strategy                 S1        S2        S3

-------------------------------------------------------

Round Robin              4         3         3

Least Connections        4         3         3

Weighted                 2         3         5

Load distribution:

========== LOAD DISTRIBUTION (%) ==========

Strategy                 S1        S2        S3

-------------------------------------------------------

Round Robin              40.0      30.0      30.0

Least Connections        40.0      30.0      30.0

Weighted                 20.0      30.0      50.0

The exact values may change between executions because request processing times and concurrent scheduling can vary.

**OOP Concepts Used:**

The project uses Object-Oriented Programming concepts through classes.

.Classes

.Server

.Request

.LoadBalancer

.Simulator

.Objects

!!Objects are created from these classes to represent:

.Servers

.Requests

.Load balancer

.Simulator

.Encapsulation

Server statistics and server state are maintained inside the Server class.

**Greedy Scheduling Concept**

.The Least Connections strategy follows a greedy approach.

.For each incoming request, the simulator selects the server with the lowest current number of active connections.

.Instead of planning all future requests, it makes a decision based on the current server state.

**How to Run:**

1.Make sure Python is installed.

2.Open the project folder in a terminal.

Run:

python main.py

No external Python packages are required.

**Conclusion**

The Load Balancer Simulator demonstrates how different load balancing strategies distribute incoming requests among multiple servers.

The project combines:

1.Load balancing algorithms

2.Greedy scheduling

3.Object-Oriented Programming

4.Multithreading

5.Performance measurement

6.Load distribution analysis

The simulator provides a simple way to understand how different server selection strategies affect request distribution in a multi-server environment.

























