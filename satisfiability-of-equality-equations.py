class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        #union them both
        #check if they have the same representative 
        #if != and find returns true return false
        representative = {chr(i):chr(i) for i in range(97, 123)}
        def find(x):
            if x != representative[x]:
                representative[x] = find(representative[x])
            
            return representative[x]
        
        def union(x, y):
            rep_x = find(x)
            rep_y = find(y)

            representative[rep_x] = representative[rep_y]

        for equation in equations:
            a, operator, b = equation[0], equation[1:3], equation[-1]
            if operator == "==":
                union(a, b)
        for equation in equations:
            a, operator, b = equation[0], equation[1:3], equation[-1]
            if operator == "!=" and find(a) == find(b):
                return False

        return True

            