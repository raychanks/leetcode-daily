class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_idx = 0

    def visit(self, url: str) -> None:
        while len(self.history) - 1 > self.current_idx:
            self.history.pop()

        self.history.append(url)
        self.current_idx += 1

    def back(self, steps: int) -> str:
        self.current_idx = max(self.current_idx - steps, 0)
        return self.history[self.current_idx]

    def forward(self, steps: int) -> str:
        self.current_idx = min(self.current_idx + steps, len(self.history) - 1)
        return self.history[self.current_idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
