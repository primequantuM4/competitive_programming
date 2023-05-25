class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #get a running sum
        #return true if the sum is positive? and false if it's negative...
        bill_count = defaultdict(int)
        print(len(bills))
        for idx,bill in enumerate(bills):
            if bill == 5:
                bill_count[5] += 1
            
            elif bill == 10:
                if bill_count[5] == 0:
                    return False
                
                bill_count[5] -= 1
                bill_count[10] += 1

            elif bill == 20:
                if bill_count[10] >= 1 and bill_count[5] >= 1:
                    bill_count[10] -= 1
                    bill_count[5] -= 1

                elif bill_count[5] >= 3:
                    bill_count[5] -= 3

                else:
                    return False

        return True