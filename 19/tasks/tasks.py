# 1 task


def fib_generator(n):
    fib_seka = []
    a, b = 0, 1
    for _ in range(n):
        fib_seka.append(a)
        a, b = b, a + b
    return fib_seka


seka = fib_generator(10)

print(f'Fib seka: {seka}')

def filtruoti_lyginius(seka):
    lyginiai = []
    for skaicius in seka:
        if skaicius % 2 == 0:
            lyginiai.append(skaicius)
    return lyginiai

lyginiu_seka = filtruoti_lyginius(seka)

print(f'Lyginiu seka: {lyginiu_seka}')

print('==================================================================================')


