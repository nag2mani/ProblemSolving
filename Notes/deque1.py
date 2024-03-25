from collections import deque
# Double ended queue.

people = ["Nag", "div", "pankaj", "shek"]

dq = deque(people)
print(dq)
dq.rotate(-1)
print(dq)
dq.rotate(-2)
print(dq)
dq.rotate(0)
print(dq)
dq.rotate()
print(dq)
dq.rotate(1)
print(dq)
dq.rotate(2)
print(dq)

dq.extend(["kk", "Ang"])
# dq.rotate()
# dq.remove()
# dq.appendleft()
# dq.append()
# dq.popleft()
# dq.pop()
# dq.clear()

print(dq)