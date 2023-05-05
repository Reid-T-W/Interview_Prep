#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
stack1 = []
stack2 = []
def execute_command(command):
    if command[0] == '1':
        # If the stack1 if not empty remove all items
        # turn by turn and move them over to stack 2
        # then add the new element to stack1
        # Then return all elements in stack2 back to stack 1
        if stack1:
            while stack1:
                element = stack1.pop()
                stack2.append(element)
            stack1.append(command[1])
            while stack2:
                element = stack2.pop()
                stack1.append(element)
        # If stack1 is empty just add the new element
        else:
            stack1.append(command[1])
    elif command[0] == '2':
        element = stack1.pop()
    elif command[0] == '3':
        print(stack1[-1])

if __name__ == '__main__':
    queries = int(input())
    for i in range(queries):
        query = input()
        command = query.split()
        execute_command(command);