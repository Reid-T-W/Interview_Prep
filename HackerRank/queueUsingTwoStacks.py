#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
stack1 = []
stack2 = []
def execute_command(command):
    # Approach 1 (deque more expensive than enque)
    # but better than approach 1
    if command[0] == '1':
        stack1.append(command[1])
    elif command[0] == '2':
        # If stack 2 is not empty pop the element from stack2
        if stack2:
            stack2.pop()
        # If stack 2 is empty and stack 1 is not move all elements
        # in stack 1 to stack 2 and pop the last element
        else:
            if (stack1):
                while stack1:
                    element = stack1.pop()
                    stack2.append(element)
                element = stack2.pop()
            else:
                print("Queue is empty")
    elif command[0] == '3':
        # If stack 2 is not empty pop the element from stack2
        if stack2:
            print(stack2[-1])
        # If stack 2 is empty and stack 1 is not move all elements
        # in stack 1 to stack 2 and pop the last element
        else:
            if (stack1):
                while stack1:
                    element = stack1.pop()
                    stack2.append(element)
                print(stack2[-1])
            else:
                print("Queue is empty")

    # Approach 2 (Very Expensive deque operation)
    # if command[0] == '1':
    #     stack1.append(command[1])
    # elif command[0] == '2':
    #     # Turn by turn remove all elements from stack1
    #     # and add them to stack2, so that the first element of 
    #     # stack1 will be at the top of stack2
    #     while stack1:
    #         element = stack1.pop()
    #         stack2.append(element)
    #     # Remove the top element in stack2, this means that
    #     # the first element is removed
    #     element = stack2.pop()
    #     # Return the elements back to stack1
    #     while stack2:
    #         element = stack2.pop()
    #         stack1.append(element)
    # elif command[0] == '3':
    #     while stack1:
    #         element = stack1.pop()
    #         stack2.append(element)
    #     print(stack2[-1])
    #     while stack2:
    #         element = stack2.pop()
    #         stack1.append(element)   

    # Approach 3 (Very Expensive enque operation)
    # if command[0] == '1':
    #     # If the stack1 if not empty remove all items
    #     # turn by turn and move them over to stack 2
    #     # then add the new element to stack1
    #     # Then return all elements in stack2 back to stack 1
    #     if stack1:
    #         while stack1:
    #             element = stack1.pop()
    #             stack2.append(element)
    #         stack1.append(command[1])
    #         while stack2:
    #             element = stack2.pop()
    #             stack1.append(element)
    #     # If stack1 is empty just add the new element
    #     else:
    #         stack1.append(command[1])
    # elif command[0] == '2':
    #     element = stack1.pop()
    # elif command[0] == '3':
    #     print(stack1[-1])

if __name__ == '__main__':
    queries = int(input())
    for i in range(queries):
        query = input()
        command = query.split()
        execute_command(command);