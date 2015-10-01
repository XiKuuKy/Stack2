"""
By Simon Harms.

Copyright 2015 Simon Harms, MIT LICENSE

Name: Stack2

Summary: Stack Version 2
"""
class Stack:
    """
    Python Stack V2 with view and change.
    """
    def __init__(self):
        """
        Initialize the Stack.
        """
        self.__storage = []

    def is_empty(self):
        """
        Returns if the Stack is empty.
        """
        return len(self.__storage) == 0

    def push(self, pushed):
        """
        Add to the Stack.
        """
        self.__storage.append(pushed)

    def pop(self):
        """
        Delete the top element.
        """
        return self.__storage.pop()

    def view(self):
        """
        Return the Topmost item in the Stack.
        """
        return self.__storage[-1]

    def change(self, new):
        """
        Make edits to the Topmost item in the Stack.
        """
        self.__storage[-1] = new

    def get_len(self):
        """
        Return the length of the stack.
        """
        return len(self.__storage)

    def get_stack(self):
        """
        Return the stack. (Can't edit it though. It is just a getter.)
        """
        return self.__storage

    def set_stack(self, new_stack):
        """
        Set the stack as the stack pased in. (use the newStacks getStack function.)
        """
        self.__storage = new_stack

    def get_string(self):
        """
        Get a string of the stack.
        """
        return "".join(self.__storage)
