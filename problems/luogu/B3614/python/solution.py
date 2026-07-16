i = """2
5
push 2
query
size
pop
query
3
pop
query
size"""

o = """2
1
Anguei!
Empty
Anguei!
0"""

t = int(input())
stk = []

for _ in range(t):
    m = int(input())
    for _ in range(m):
        s = input()
        if s[0:2] == 'pu':
            stk.append(int(s.split()[1]))
        elif s[0] == 'q':
            if stk:
                print(stk[-1])
            else:
                print('Anguei!')
        elif s[0:2] == 'po':
            if stk:
                print(stk[-1])
                stk.pop()
            else:
                print('Empty')
        elif s[0] == 's':
            print(len(stk))
