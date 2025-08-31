def sumofno(number):
    sum=0
    for i in str(number)[::]:
        sum = sum + int(i)

    return sum

n = sumofno(789)
print(n)

def sumof(number):
    sum=0
    ld=0
    while number>0:
        ld=number%10
        number = number // 10
        sum=sum+ld
    return sum

n = sumof(100023)
print(n)