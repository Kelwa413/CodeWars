def divisors(n):
    num = 0
    for i in range (1, n+1):
        if n % i == 0:
            num += 1
    return num


def between(a,b):
    list = []
    for i in range (a,b):
        list.append(i)
    return list

def paperwork(m,n):
    papers = 0
    if n|m < 0:
        return 0
    else:
        papers = m * n

    return papers

def solution(a,b):
    num = len(b)

    arr = a [-num:]
    if arr == a:
        return True
    else:
        return False

def descending_order(num):
    arr = [int(x) for x in str(num)]
    arr.sort(reverse=True)
    return int(''.join(map(str, arr)))


def is_palindrome(s):
    num = len(s)
    half = num // 2

    if num % 2 == 0:
        first = s[0:half]
        end = s[half:]
    else:
        first = s[0:half]
        end = s[half +1:]

    revEnd = end[::-1]

    return revEnd == first

