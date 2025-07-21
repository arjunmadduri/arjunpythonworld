#create a program for reversing strings using stack
reverse_name = ""
stack = []
limit = 12
def push(a):
    if len(stack)>=limit:
        print("Overflow")
    else:
        stack.append(a)
        print(stack)
def pull():
    global reverse_name
    if len(stack)==0:
        print("Underflow")
    else:
        x = stack.pop()
        reverse_name = reverse_name+x
push("A")
push("R")
push("J")
push("U")
push("N")
push("H")
push("A")
push("S")
push("R")
push("I")
push("Z")
push("Z")
for i in range(12):
    pull()
print(reverse_name)