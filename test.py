

l = [1,2,3,4,'a','True']

i = 0

size = len(l)

while i < size:
    a = l[i]
    print(a)
    i =  i + 1

print("-------------")
# for element loop
for i in l:
    print(i)
print("-------------")


# for index loop
# [0,1,2,3,4,5]
for i in range(len(l)):
    a = l[i]
    print(a)

print("------------- print(l[i])")

l = [1,2,3,4,5,6,7,8,9,10]
i = -1
while i > -len(l)-1:
    print(l[i])
    i = i - 1
print("-------------")

for i in range(len(l)):
    print(l[i])

print("-------------")

for i in l:
    print(i)


a = 'Hello'

def reverse(s):
    temp = []

    i = 0
    while i < len(s):
        temp.append(s[i])
        i =  i + 1
    # temp = ['H','e','l','l','o']
    j = 0
    k = -1
    while j < len(s):
        print(s[k])
        # i used for control condition
        j = j+1
        k = k-1




reverse(a)




