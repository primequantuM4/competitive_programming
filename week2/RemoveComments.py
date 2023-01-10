class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        codeWithoutComment = []
        validCode = []
        multiLineFlag = False
        for lines in source:
            words = 0
            while words < len(lines):
                if multiLineFlag:
                    if lines[words] == "*" and words < len(lines)-1 and lines[words + 1] == "/":
                        multiLineFlag = False
                        words += 1
                    words += 1
                else:
                    if lines[words] == "/" and words < len(lines)-1 and lines[words + 1] == "/":
                        #single line comment break
                        break
                    elif lines[words] == "/" and words < len(lines)-1 and lines[words + 1] == "*":
                        multiLineFlag = True
                        words += 2
                    else:
                        print(words)
                        validCode.append(lines[words])
                        words += 1
            if not multiLineFlag and len(validCode) > 0:
                codeWithoutComment.append("".join(validCode))
                validCode = []
            
        return codeWithoutComment
