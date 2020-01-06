list1 = [1,2,3,4]
list2 = [4,5,6,7,8]

zipped = list(zip(list1, list2))
print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)