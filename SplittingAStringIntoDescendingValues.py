class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(known_comb, passed_string):
            if passed_string=="" and len(known_comb) > 1:
                return True


            for i in range(len(passed_string)):
                num = int(passed_string[:i+1])
                is_candidate = len(known_comb) == 0 or  num == known_comb[-1]-1

                if is_candidate:
                    known_comb.append(num)

                    remaining_string = passed_string[i+1:]
                    found_combo = backtrack(known_comb, remaining_string)
                    
                    if found_combo:
                        return True

                    known_comb.pop()
            return False

        return backtrack([], s)
