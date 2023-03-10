class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def backtrack(potential_num, passed_str):
            if not passed_str and len(potential_num) > 2:
                return True

            for i in range(len(passed_str)):
                number = passed_str[:i+1]
                hasZeros = len(number) > 1 and number[0] == "0"

                if hasZeros:
                    return
                valid = len(potential_num) < 2 or potential_num[-2] + potential_num[-1] == int(number)
                potential_num.append(int(number))
                if valid:
                    found_comb = backtrack(potential_num, passed_str[i+1:])
                    if found_comb:
                        return True
                potential_num.pop()  

        return backtrack([], num)
