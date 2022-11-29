row = 5
a = '*'
b = 4

for i in range(row):
    for k in range(b):
        print(end=" ")
    
    b -= 1

    for j in range(i + 1):
        print(a, end=" ")
    print("\r")
