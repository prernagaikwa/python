MAXSIZE = 8
stack = [0] * MAXSIZE
top = -1
def isfull():
    if(top == MAXSIZE):
        return 1
    else:
        return 0
def push(data):
    global top
    if(isfull() != 1):
        top = top + 1
        stack[top] = data
    else:
        print("Could not insert data, Stack is full")

def isfull():
    if (top == MAXSIZE):
    return 1
    else:
    return 0
def peek():
    return stack[top]
def push (data)
def isempty():
    if(top == -1):
        return 1
    else:
        return 0
    
    def isfull()

    