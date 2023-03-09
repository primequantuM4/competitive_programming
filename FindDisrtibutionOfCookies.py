class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.min_possible = float('inf')
        self.k = k
        children = [0] * k
        cookies.sort(reverse=True)
        def backtrack(children, bag_index):

            #base case
            if bag_index == len(cookies):
                self.min_possible = min(self.min_possible, max(children))
                return

            #middle case
            if max(children) >= self.min_possible:
                return

            for i in range(len(children)):
                bag = cookies[bag_index]
                children[i] += bag

                backtrack(children, bag_index+1)

                children[i]-=bag

        backtrack(children, 0)
        return self.min_possible
