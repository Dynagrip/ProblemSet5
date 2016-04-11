
list1 = ['b','c','d']
list2 = [1,2,3]
list3 = [4,5,6]
testdict = {}
nestdict = {}

for item in list1:
    for element in list2:
        testdict[item] = nestdict[list3]

