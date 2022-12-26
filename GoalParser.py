class Solution:
    def interpret(self, command: str) -> str:
        translated = ""
        i = 0
        print(len(command))
        while i < len(command):
            if command[i] == "(":
                if command[i + 1] == "a":
                    translated += "al"
                    i += 4
                else:
                    translated += "o"
                    i += 2
            else:
                translated += "G"
                i += 1
            
        return translated
