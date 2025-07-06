# Method 1:Quick way just multiply
def multiply_one_step(n, m):
    result = n * m
    print("\nUsing one step(n * m):", result)
    # Ask the user for two numbers
n = int(input("Enter the first number (n):"))
m = int(input("Enter the second number (m):"))
multiply_one_step(n, m) 



#Method 2:Slow way(add b again and again, a times)
def multiply_many_steps(n, m):
    result = 0
    for i in range(n):
        result += m
    print("Using many steps (adding m, n times):",result)

# Ask the user for two numbers
a = int(input("Enter the first number (n):"))
b = int(input("Enter the second number (m):"))

# Show results using both ways
multiply_one_step(n, m)
multiply_many_steps(n, m)



thing = input("Type something fun (like * or & or $): ")

count = int(input("How many times? "))


print("\nHere we go!\n")
for i in range(count):
    print(thing)