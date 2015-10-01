from Stack2 import Stack

x = Stack()

x.push(34)
print(x.view())

x.change(x.view() + 40)

print(x.view())

x.pop()

x.push("Hello, Stacks!")

print(x.view())

x.push("\n")
x.push("h")
x.push("e")
x.push("l")
x.push("l")
x.push("o")
x.push("!")

z = ""

for i in x.get_stack():
    z = z + i

print(z.capitalize())

# These are really just examples. For usage look at the Docstrings.

print(x.get_string())
