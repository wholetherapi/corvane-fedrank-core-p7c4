"""FedRank replicator."""

class Replicator:
    def __init__(self, shards):
        self.shards = shards

    def replicate(self, batch):
        return [s.score(batch) for s in self.shards]
