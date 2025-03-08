import sys

class agent:
    def __init__(self,name,score):
        self.name = name
        self.score = score

agents = []
for _ in range(5):
    name, score = tuple(sys.stdin.readline().split())
    agents.append(agent(name,score))

print(agents[0].name, agents[0].score)