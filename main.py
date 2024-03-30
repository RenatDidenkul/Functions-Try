l = [65, 785, 34, 765, 3]
#print(25 / 0)
#l[6] += l[1]
#print(l[6])

print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")
try:
    print(25 / 0)
except ZeroDivisionError:
    print("ZeroDivisionError")
except NameError:
    print("NameError")

print(l)

a = 0
while a < 10:
    a += 1
    if a == 5:
        break
    print(a)
else:
    print("END")