x,y,z=1,2,3
print("priview x",x)
print("priview y",y)
print("priview z",z)
x,y,z=z,x,y
print(x)
print(y)
print(z)

#Splitting a string
data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(fruits[1])
print(data[1])
print(type(data))
print(type(fruits))

name = "Alice"
name2 = "Di"
age = 25
age2 = 23
message = "Hello, %s. You are %d years old." % (name2, age2)
message1 = "Hello, {}. u r {}.". format(name,age)
print(message)  # Output: Hello, Alice. You are 25 years old.
print(message1)

billion = 1_000_000_000
print(billion)

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    #print(count)

number=[10,20,30]
#print(type(number))

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)  # This line is part of the for loop
    print(f"{fruit} is delicious!")  # This line is also part of the for loop

