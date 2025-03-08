import sys

class agent:
    def __init__(self,name,score):
        self.name = name
        self.score = score

agents = []
for _ in range(5):
    name, score = tuple(sys.stdin.readline().split())
    score = int(score)
    agents.append(agent(name,score))

min_idx = 0
for i in range(1,5):
    if agents[min_idx].score > agents[i].score:
        min_idx = i

print(agents[min_idx].name,agents[min_idx].score)