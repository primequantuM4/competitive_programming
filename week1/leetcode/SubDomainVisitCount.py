class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        numberOfVisits = collections.defaultdict(int)
        result = []
        for visits in cpdomains:
            timesVisited, domainName = visits.split()
            timesVisited = int(timesVisited)
            domainName = collections.deque(domainName.split("."))

            while domainName:
                site = ".".join(domainName)
                numberOfVisits[site] += timesVisited
                domainName.popleft()

        for domain in numberOfVisits:
            result.append(f"{numberOfVisits[domain]} {domain}")
        
        return result
        
