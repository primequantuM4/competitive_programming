class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left_ptr = 0
        right_ptr = len(skill) - 1
        powerSkill = skill[left_ptr] + skill[right_ptr]
        teamDivision = []

        while left_ptr < right_ptr:
            if skill[left_ptr] + skill[right_ptr] != powerSkill:
                return -1
            
            teamDivision.append((skill[left_ptr], skill[right_ptr]))
            left_ptr += 1
            right_ptr -= 1

        result = 0
        for prod, number in teamDivision:
            result += (prod * number)
        
        return result
