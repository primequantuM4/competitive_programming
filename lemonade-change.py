class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bills, ten_bills = 0, 0
        for bill in bills:
            if bill == 5:
                five_bills += 1
            
            elif bill == 10:
                if not five_bills:
                    return False
                
                five_bills -= 1
                ten_bills += 1

            elif bill == 20:
                if ten_bills and five_bills:
                    ten_bills -= 1
                    five_bills -= 1

                elif five_bills >= 3:
                    five_bills -= 3

                else:
                    return False

        return True
