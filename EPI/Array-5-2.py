# 5.2 Increment an arbitrary-precision integer

def increment(A):
    A[-1] += 1

    for i in reversed(range(1, len(A))):
        if A[i] == 10:
            A[i] = 0
            A[i-1] += 1
        else:
            break

    if A[0] == 10:
        A[0] = 1
        A.append(0)
    
    return A

def main():
    x = [1, 2, 3]
    y = [9, 9, 9]
    z = [1, 9, 9]
    print(increment(x))
    print(increment(y))
    print(increment(z))

if __name__ == '__main__':
    main()
