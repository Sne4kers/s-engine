# Example solution for GCD of two numbers problem

times = int(input())
for i in range(times):
    input_str = input()
    a, b = input_str.split()
    a = int(a)
    b = int(b)
    while a != 0 and b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    print(b + a)