stack = []
limit = 5
def push(a):
    if len(stack)>=limit:
        print("Overflow")
    else:
        stack.append(a)
        print(stack)
def pull():
    if len(stack)==0:
        print("Underflow")
    else:
        stack.pop()
        print(stack)
push(6)
push(7)
push(9)
push(1)
push(1)
pull()