# count = 0

# for i in range(5):
#     for j in range(8):
#         count += 1

# print(count)


# count = 0
# for i in range(5):
#     count += 1
#     for j in range(3):
#         count -= 1

# print(count)


funList = []
for i in range(1,5):
    row = []
    for j in range(i):
        row.append(j)
    funList.append(row)

print(funList)

myString = ""
for i in range(1,8):
    myString += str(i)
    print(myString)
    