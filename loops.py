for i in range(1,10):
    print(i)

languages = ["Python", "Java", "C++", "JavaScript"]
for lang in languages:
    print(lang)
 
j=1
while j<=5:
    print(j)
    j = j+1

for x in range(1,11):
    if x==5:
        break
    print(x)

for y in range(1,6):
    if y==3:
        continue
    print(y)    

num=int(input("enter the number"))
if num<5:
    print("small")    
elif num==5:
    print("same")    
else:
    print("big")    

age =50
if age>=50:
    if age<100:
        print("old generation")
else:
    print("young generation ")        

num1=80
if num1>50 and num1<40:
    print("not eligible to work")
else:
    print("eligible")        

k=2
print("even") if k%2==0 else print("odd")