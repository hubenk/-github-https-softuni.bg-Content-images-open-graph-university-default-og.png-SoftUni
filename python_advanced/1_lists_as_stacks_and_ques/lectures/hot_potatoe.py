from collections import deque

children = deque(input().split())
toss = int(input())

while len(children) > 1:
    children.rotate(-toss)
    print(f"Removed {children.pop()}")

print(f"Last is {''.join(children)}")
