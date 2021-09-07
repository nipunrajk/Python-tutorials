greeting = 'Hello'
def change_greeting(input):
    global greeting
    greeting = input


def greeting_world():
    world = 'world'
    print(greeting, world)

change_greeting('hi')
greeting_world()
