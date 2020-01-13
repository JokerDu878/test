''''#求质因数
num=int(input())
i=2
while num!=1:
    if num%i==0:
        print(i)
        num//=i
    else:
        i+=1
'''

str=input()
str1=str.strip()
i=0
count=0
while i<len(str1):
    while str1[i]!=" ":
        i+=1
        if i==len(str1):
            break
    count+=1
    if i == len(str1):
        break
    while str1[i]==" ":
        i+=1
print(count)
