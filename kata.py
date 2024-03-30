#Flashed --> first try

                                #Level 8
def digitize(n):
    return [int(x) for x in str(n)[::-1]]


def find_needle(haystack):
    position = haystack.index("needle")
    str = f'found needle at position ' + position
    return str

def remove_char(s):
    str1 = s[1:-1]
    return str1


def positive_sum(arr):
    #Flashed
    sum = 0
    for i in arr:
        if i >= 0:
            sum = sum + i
    return sum

def bool_to_word(boolean):
    #Flashed
    if boolean:
        response = "Yes"
    else:
        response = "No"
    return response

def rps(p1, p2):
    result = ''
    if p1 == 'rock' and p2 == 'rock':
        result = f'Draw!'
    elif p1 == 'rock' and p2 == 'paper':
        result = f'Player 2 won!'
    elif p1 == 'rock' and p2 == 'scissors':
        result = f'Player 1 won!'
    elif p1 == 'paper' and p2 == 'paper':
        result = f'Draw!'
    elif p1 == 'paper' and p2 == 'rock':
        result = f'Player 1 won!!'
    elif p1 == 'paper' and p2 == 'scissors':
        result = f'Player 2 won!'
    elif p1 == 'scissors' and p2 == 'paper':
        result = f'Player 1 won!'    
    elif p1 == 'scissors' and p2 == 'scissors':
        result = f'Draw!'
    elif p1 == 'scissors' and p2 == 'rock':
        result = 'Player 2 won!'
    return result   

def past(h, m, s):
    #Flashed
    hours = h * 3600000
    minutes = m * 60000
    seconds = s * 1000
    return hours + minutes + seconds

def make_upper_case(s):
    #flashed
    return s.upper()

def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'
    

                                # Level 7
def mispelled(word1, word2):
    #ChatGPT'd
    if word1 == word2:
        return True
    
    if abs(len(word1) - len(word2)) > 1:
        return False
    
    i, j, edits = 0, 0, 0
    
    while i < len(word1) and j < len(word2):
        if word1[i] != word2[j]:
            edits += 1
            if edits > 1:
                return False
            if len(word1) > len(word2):
                i += 1
            elif len(word2) > len(word1):
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1
            
    if i < len(word1) or j < len(word2):
        edits += 1
        
    return edits == 1

def get_age(age):
    y = age.split()
    x = y[0]
    return int(x)
from math import trunc
def cockroach_speed(s):
    return trunc(s * 27.778)

def find_average(numbers):
    total = 0 
    amount = 0
    for i in numbers:
        total = total + i
        amount = len(numbers)
        
    return total/amount

def maps(a):
    li = []
    for i in a:
        li.append(i * 2)
    return li

def get_volume_of_cuboid(length, width, height):
    #Flashed
    return length * width * height

def to_jaden_case(string):
    # GPT'd
    words = string.split()
    words = [word.capitalize() for word in words]
    jaden_case_string = " ".join(words)
    return jaden_case_string

def square_digits(num):
    squares[] = num.split()
    for i in squares:
        li = i ** 2
    return li


def maskify(cc):
    # GPT'd
    return "#"*(len(cc)-4) + cc[-4:]

def square_sum(numbers):
    total = 0
    for i in numbers:
        total += i**2
    return total

def sum_array(arr):
    # half GPT'd
    highest = float('-inf')
    lowest = float('inf')
    total = 0
    if not isinstance(arr, list):
        return 0
    if len(arr) == 0:
        return 0
    for i in arr:
        if i < lowest:
            lowest = i
        if i > highest:
            highest = i
    if len(arr) <= 2:
        return 0
    total = sum(arr) - highest - lowest
    return total

def count_by(x, n):
    # GPT'd
    return [x * i for i in range(1, n+1)]

def xo(s):
    x = 0
    o = 0
    for i in s:
        if i == 'x' or i == 'X':
            x += 1
        elif i == 'o' or i == 'O':
            o += 1
    if x == o:
        return True
    elif x != o:
        return False

def smash(words):
    return " ".join(words)
def double_char(s):
    word = ""
    for i in s:
        word += i + i
    return word
def stray(arr):
    result = 0
    for i in arr:
        result ^= i
    return result
def find_dup(arr):
    for i in arr:
        arr.count(i) == 2

def duplicate_count(text):

    case_normalized = text.lower()

    char_count = {}

    for i in case_normalized:
        char_count