from collections import deque
# Double ended queue.

people = ["Nag", "div", "pankaj", "shek"]

dq = deque(people)
print(dq)
dq.rotate()
print(dq)
dq.rotate()
print(dq)
# dq.rotate(-1)
# print(dq)
# dq.rotate(-2)
# print(dq)
# dq.rotate(0)
# print(dq)
# dq.rotate()
# print(dq)
# dq.rotate(1)
# print(dq)
# dq.rotate(2)
# print(dq)

# dq.extend(["kk", "Ang"])
# dq.rotate()
# dq.remove()
# dq.appendleft()
# dq.append()
# dq.popleft()
# print(dq)
# print(dq.popleft())
# print(dq.append(999))
# print(dq)
# dq.clear()

# s = [4,5,2,1]
# print(sorted(s))

# dq = deque([i for i in range(7)])
# print(dq.popleft())
# print(dq.popleft())
# print(dq.popleft())
# print(dq.popleft())
