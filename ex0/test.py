def func(n):
    i = 0
    while i < n:
        yield i
        i += 1

r = func(5)
print(r)
print()

try:
    while True:
        print(next(r))
except StopIteration:
    pass

#for i in range(5):
#   continue

print("End")


#s = f"hello {n}"
#s = "hello {}".format(n)

#s = "hello {num}".format(num=n)

#s = "hello %d, %d, %d" % (n, n, n)
#s = (
#    f"hello{n}"
#    f"world{n}"
#)

#s = "helloworld"


#a = 99
#print(id(a))
#b = -1024
#print(id(b))
#b = a
#print(id(b))
#print(b)
#a = 42
#print(b)
#print(id(a))
#
#print([1, 2, 3])
#print(iter([1, 2, 3]))
#
#for i in [1, 2, 3]:
#    print(i)
