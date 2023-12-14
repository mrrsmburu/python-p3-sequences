#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = [0, 1]  
    if length == 1:
        print(fib_list[0])
    elif length == 2:
        print(fib_list[0], fib_list[1])
    else:
        print(fib_list[0], fib_list[1], end=" ")
        for i in range(2, length):
            next_num = fib_list[i - 1] + fib_list[i - 2]
            fib_list.append(next_num)
            print(next_num, end=" ")
    print()
    pass