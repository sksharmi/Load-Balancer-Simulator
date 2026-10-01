class LoadBalancer:

    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def round_robin(self):
        server = self.servers[self.current_index]

        self.current_index = (
            self.current_index + 1
        ) % len(self.servers)

        return server

    def least_connections(self):
        return min(
            self.servers,
            key=lambda server: server.active_connections
        )

    def weighted(self):
        return max(
            self.servers,
            key=lambda server:
                server.weight / (server.active_connections + 1)
        )
    def reset(self):
      self.current_index = 0

      for server in self.servers:
        server.reset_statistics()