# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('nCr 출력')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
y = input().split()

# 중복제거
x = list(set(y))

#출력
c = len(x)  #원소 개수

# 1개씩 출력
for i in range(c) :
     print(x[i], end=' / ')

# 2개씩 출력
"""for i in range(c-1):
    print(x[0], x[i+1], end=' / ')
for i in reversed(range(c-1,1,-1)):
    print(x[1], x[i], end=' / ')
for i in reversed(range(c-1,2,-1)):
    print(x[2], x[i], end=' / ')"""

for i in range(c):
    for m in reversed(range(c-1,i,-1)):
        print(x[i], x[m], end=' / ')  #2개
#3개
for i in range(c):
    for m in reversed(range(c-1,i,-1)):
        if x[i+1] != x[m] and x[i] != x[m]:
            print(x[i],x[i+1],x[m], end=' / ')

#4개
for i in range(c):
    for m in reversed(range(c-1,i,-1)):
        if x[i+1] != x[m] and x[i] != x[m] and x[i+2] != x[m]:
            print(x[i],x[i+1],x[i+2],x[m], end=' / ')