reverse_name = ""
stack = []
limit = 100
def push(a):
    if len(stack)>=limit:
        print("Overflow")
    else:
        stack.append(a)
def pull():
    global reverse_name
    if len(stack)==0:
        print("Underflow")
    else:
        x = stack.pop()
        reverse_name = reverse_name + x
name = "ROOHAS GNUT GNUT GNUT GNUT"
for i in name:
    push(i)
for i in name:
    pull()
print(reverse_name)