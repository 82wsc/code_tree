import sys

class user:
    def __init__(self, user_id='codetree', level=10):
        self.user_id = user_id
        self.level = level

user1 = user()

id2, level2 = sys.stdin.readline().split()
level2 = int(level2)
user2 = user(id2, level2)

print(f"user {user1.user_id} lv {user1.level}")
print(f"user {user2.user_id} lv {user2.level}")

        