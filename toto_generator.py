import random

CONSTANT_THING=2

def generate_toto(num, lucky_num=0):
    l = []
    for i in range(num):
        l.append(random.randint(0,10))

    if lucky_num:
        l.append(lucky_num)
    return l

def igenerate_toto(num, lucky_num=0):
    for i in range(num):
        yield random.randint(0,10)

def square(n):
    return n * n

def main():
    print(generate_toto(6))
    for i in igenerate_toto(6):
        print(i)

    s = map(square, range(10))
    print(list(s))
    t = filter(lambda x: x % 2, range(10))


if __name__ == "__main__":
    main()
