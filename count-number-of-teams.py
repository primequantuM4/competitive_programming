class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0 
        for i, v in enumerate(rating[1:-1]):
            left_less, left_great = 0, 0
            right_less, right_great = 0, 0

            for left in range(i + 1):
                if rating[left] < v:
                    left_less += 1
                elif rating[left] > v:
                    left_great += 1
                
            for right in range(i + 2, len(rating)): 
                if rating[right] > v:
                    right_great += 1
                
                elif rating[right] < v:
                    right_less += 1
            
            count += (left_less * right_great + left_great * right_less)
        
        return count
            