class RecentCounter:

    def __init__(self):
        self.ping_history = list()

    def ping(self, t: int) -> int:
        idx = 0
        breaked = False
        for idx in range(len(self.ping_history)):
            if self.ping_history[idx] >= t - 3000:
                breaked = True
                break
        if breaked:
            self.ping_history = self.ping_history[idx:]
        else:
            self.ping_history = list()
        self.ping_history.append(t)
        return len(self.ping_history)
