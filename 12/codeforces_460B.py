# Little Dima and Equation

def sum_digits(x):
    return sum(map(int, str(x)))

def find_x():
    a, b, c = map(int, input().split())
    lst = [x for sum_x in range(1, 82) if 
           0 < (x := b * (sum_x**a) + c) < 10**9 and sum_digits(x) == sum_x]
    print(len(lst))
    if lst:
        print(*lst)

if __name__ == '__main__':
    find_x()
