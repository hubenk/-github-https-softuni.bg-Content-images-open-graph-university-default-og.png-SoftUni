n_line, m_line = input().split()

n = set()
m = set()

for _ in range(int(n_line)):
    n.add(input())

for _ in range(int(m_line)):
    m.add(input())

result = n.intersection(m)

print('\n'.join(result))
