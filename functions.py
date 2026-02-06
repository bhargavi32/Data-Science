# def sample(username,password):
#     print("login successful") if username=="bhargavi" and password=="admin" else print("fail")

# username=input("ENTER THE NAME")
# password=input("pass")
# sample(username,password)

def db_call():
    return "db connection soon"
res = db_call()
print(res)

res = lambda num:num*num
print(res(10))

ress = lambda a,b:a+b
print(ress(100,200))