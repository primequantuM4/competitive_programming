if __name__ == '__main__':
    N = int(input())
    
    listReturned = []
    for i in range(N):
        commands = input().split()
        command = commands[0]
        arguments = ",".join(commands[1:])
        if command == 'print':
            print(listReturned)
        else:
            result = f"listReturned.{command}({arguments})"
            exec(result)
