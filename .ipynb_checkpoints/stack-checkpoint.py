class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

# User input example
if __name__ == "__main__":
    stack = Stack()
    while True:
        print("\nOptions: push <item>, pop, peek, size, is_empty, quit")
        command = input("Enter command: ").strip().lower()
        if command.startswith("push"):
            _, item = command.split(maxsplit=1)
            stack.push(item)
            print(f"Pushed {item}")
        elif command == "pop":
            try:
                print("Popped:", stack.pop())
            except IndexError as e:
                print(e)
        elif command == "peek":
            try:
                print("Top element:", stack.peek())
            except IndexError as e:
                print(e)
        elif command == "size":
            print("Stack size:", stack.size())
        elif command == "is_empty":
            print("Stack is empty?", stack.is_empty())
        elif command == "quit":
            break
        else:
            print("Invalid command.")