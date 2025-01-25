import inspect

# (10 * 4)

print(10 * 4)

# some some x (x * 4)

xx = (lambda x: x*4)(10)

# x = x(10)

print(xx)

# for some x and y (x * y)

gange = (lambda y: (lambda x: x*y))

print (gange)

plus = (lambda y: (lambda x: x+y))

print(plus)

result = plus(3)(6)
print(result)


test = (lambda x: plus(x)(2))(2)
test2 = (lambda y: (lambda x: plus(x)(y)))(3)(3)
test3 = (lambda op: (lambda y: (lambda x: op(x)(y))))(lambda y: (lambda x: x*y))(4)(5)

print(test3)


plus2 = (lambda y: (lambda x: x+y))(4)(3)

test4 = (lambda p: (lambda y: (lambda x: x+y))(p)(3))(5)

test5 = (lambda q: (lambda p: (lambda y: (lambda x: x+y))(p)(q)))(6)(9)

test6 = (lambda r: (lambda q: (lambda p: r(p)(q))))(lambda y: (lambda x: x+y))(8)(9)

print(test6)


x = 1

f = lambda x: x+1


re = f(x)
print(re)

f1 = 2+3

print(f1)

f2 = lambda x: 2+x

print(f2(4))

f3 = lambda y: lambda x: y+x

print(inspect.getsource(f3(5)), end="")

f4 = f3(2)

print(f4(3))