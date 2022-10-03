a = input()
b = input()
c = input()

value = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9,
}

GOP = {
    'black' : 1,
    'brown' : 10,
    'red' : 100,
    'orange' : 10**3,
    'yellow' : 10**4,
    'green' : 10**5,
    'blue' : 10**6,
    'violet' : 10**7,
    'grey' : 10**8,
    'white' : 10**9,
}

print((10*value[a]+value[b])*GOP[c])