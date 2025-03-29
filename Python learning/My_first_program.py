s="1234566"
sum=0
for i in s:
    sum=sum+int(i)
print(sum)


s=[1,2,3,4]
d={1:0,2:1,3:2,4:3}
d={}
for i in s:
    d[i]=s.index(i)
print(d)

s=["s","b","c","d","b"]
d={"s":0,"b":4,"c":2,"d":3}
g={}
for i in s:
    g[i]=s.index(i)
    print(g)

s="sailaja"
print(s.replace("a","@",1))



s="sailaja"
l=["s","i","l","j"]
list=[]
for i in s:
    if i!="a":
        list.append(i)
        print(list)


s="sailaja"
l=["j","l","i","s"]
lst=[]
for i in s:
    if i!="a":
        lst.insert(0,i)
        print(lst)

l = ['apple', 'banana', 'cherry', ['mango', 'pineapple', 'papaya']]
l1 = []

for i in l:
    if type(i) == list:
        l1.extend(i)  # Extends the list by adding each element of the nested list
    else:
        l1.append(i)  # Appends the individual element to the result list
    print(l1)  # Print the state of l1 after each iteration

print("Final list:", l1)  # Output the final flattened list









