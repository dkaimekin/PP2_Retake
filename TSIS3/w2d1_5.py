vector = []

command = "size"
while command != "end":
    command = input()
    if "push" in command:
        command = command.split(" ")
        vector.append(int(command[1]))
        print("OK")
        pass
    elif command == "size":
        print(len(vector))
        pass
    elif command == "pop":
        vector.pop()
        print("OK")
        pass
    elif command == "clear":
        vector.clear()
        print("OK")
        pass
    elif command == "front":
        print(vector[0])
        pass
    elif command == "back":
        print(vector[-1])
        pass
    elif command == "end":
        print("Black Devil")
        break