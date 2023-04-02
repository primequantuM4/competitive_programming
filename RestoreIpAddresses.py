class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #handle edge case
        if len(s) > 12:
            return []
        
        restoredIpAddresses = []
        availableIp = [9, 6, 3, 0]
        
        def backtrack(levels, cur_index, possible_ip):
            if len(possible_ip) == 4:
                restoredIpAddresses.append(".".join(possible_ip[:]))
                
            ip_arr = []
            for i in range(cur_index, len(s)):
                ip_arr.append(s[i])
                available_ip = len(s) - i - 1
                
                can_partition = availableIp[levels] >= available_ip
                not_leading_zero = ip_arr[0] != "0" or len(ip_arr) == 1
                less = int("".join(ip_arr)) <= 255
                
                if can_partition and not_leading_zero and less:
                    possible_ip.append("".join(ip_arr))
                    
                    backtrack(levels+1, i+1, possible_ip)
                    
                    possible_ip.pop()

        backtrack(0, 0, [])
        return restoredIpAddresses
