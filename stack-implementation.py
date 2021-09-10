#list based stack implementation

def create_stack():
    stack = []
    return stack

# check whether the stack is empty or not
def check_empty(stack):
    return len(stack) == 0

# pushing item into the stack
def push(stack, item):
    stack.append(item)
    print('Pushed item', item)

# removing item from the stack
def pop(stack):
    if check_empty(stack):
        print('The stack is empty')
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print('Popped item: ', pop(stack) )
print('stack after popping an element: ', str(stack))


