



# string = "1234567890"

# for char in string:
#     print(char)
#
# myItrerator = iter(string)
# print(myItrerator)

# print(next(myItrerator))
# print(next(myItrerator))
# print(next(myItrerator))
# print(next(myItrerator))
# print(next(myItrerator))
# print(next(myItrerator))
# print(next(myItrerator))
# print(next(myItrerator))
# print(next(myItrerator))
# print(next(myItrerator))



fordon = ["bil", "båt", "cykel", "flygplan"]

myIterator = iter(fordon)
for n in range(0, len(fordon)):

    nextItem = next(myIterator)
    print(nextItem)

