#!/usr/bin/env python3

def print_fibonacci(length):
    fibaonacci = []
    if length > 0 :
        fibaonacci.append(0)
        if length > 1:
            fibaonacci.append(1)
            if length > 2:
                for n in range(2,length):
                    fibaonacci.append(fibaonacci[n-2] + fibaonacci[n-1])

    print(fibaonacci)


print_fibonacci(15)
