


#Lab Insights:
    #Lab 5
'''
        1. dict.copy(), list.copy(), set.copy() all copy without aliasing
        2. dictionary comprehensions-
            dict = {1:2, 3:4}
            dict2 = {x: dict[x] for x in dict.keys()}
        3. How to retrieve an element from a set:
            a = set([1,2,3])
            x = 0
            for e in a:
                x=e
                break
        4. break statements in ifs within loops break the loop, in nested loops break only innermost loop
        5. you can cast a set into a sorted list/tuple
'''
    #Lab 6
'''
x,y = [1,2] works
x = {1,2} makes a set
'''
#6.006
'''
1. You can loop backwards in python- for i in range(3,0,-1): goes through i = 3,2, 1
'''
'''
Problem Insights:
1. sum(collection) returns the sum
2. b, a = a+b, b works as intended for fibonacci
3. Make sure that when using recursion, return in the recursive call whenever you're planning to make the call return a value.  Else, just modify the list and have the parent function return the list.
4. dict.copy(), list.copy9), set.copy() all copy without aliasing
5. dictionary comprehensions- 
    dict={1:2, 3:4}
    dict2={x:dict[x] for x in dict.keys()}
6. How to retrieve an element from a set:
    a = {1,2,3}
    x = 0
    for e in a:
        x=e
        break
7. break statements in life within loops break the loop, in nested loops break only innermost loop
8. you can cast a set into a sorted list/tuple
9. x,y = [1,2] works
10. {1,2} makes a aset
11. you can loop backwards in python- for i in range(3,0,-1): goes through i =3,2,1
12. You can modify a list in a loop when looping through the objects and appending through the end and it'll loop through the list + the appended object
13. You can modify a list and insert in the beginning, but it might create an infinite loop.  
'''
b = [0]*5
b[1] = 3
print(b)
for i in range(3, 0, -1):
    print(i)

a=  [(1,2), (2,5), (4,3)]

a  = 1
b =3
print(a)
for l in 'fat':
    print(l)

def gen():
    for x in range(5):
        yield x

print(list(gen()))

d= dict()
d[1]= 2
d[2] = 3
d[3] =4
d = {}
for e in d:
    if d[e] is not None:
        print(e)

for e in {}:
    print(e)
x= [2,1,3]
x.sort()
print(x)

a = set('cat')
print(a)

s = 'abcd'
print(s.startswith('ab'))