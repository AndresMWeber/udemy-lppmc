



age = 24

print("my age is " + str(age) +" years ")

print("my age is {0} years".format(age))

print("""January {0}
February {1}
March {2}
april {0}
may {1}
june {1}
july {1}
august {1}
September {1}
Oktober {1}
November {1}
December {1}
""" .format( 28, 30, 31))


for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

print("""

""")


for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))


