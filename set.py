
numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
numbers.add(16)
numbers.update([17,18,19,20])
numbers.remove(2)
numbers.discard(87)
numbers.pop()
setNumber = numbers.copy()
print(setNumber)
print(numbers)

setOne = {1,2,3,4,5}
setTwo = {5,6,7,8,9}
setThree = setOne.union(setTwo)
print(setThree)

set1 = {1,2,3}
set2 = {4,2,6}
set3 = set1.difference(set2)
print(set3)

set1 = {1,2,3}
set2 = {4,2,6}
set3 = set1.intersection(set2)
print(set3)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
set3 = set1.symmetric_difference(set2)
print(set3)

set1.isdisjoint(set2)
print(set1.issubset(set2))

set1.issubset(set2)
print(set1.issubset(set2))

set1.issuperset(set2)
print(set1.issuperset(set2))

set1 = list(set1)
print(set1)
set1 = tuple(set1)
print(set1)













