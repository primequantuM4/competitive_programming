class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = defaultdict(int)
        kFrequencies, heapified_words = [], []
        for i in words:
            words_count[i] -= 1
        
        for word, frequency in words_count.items():
            heappush(heapified_words, (frequency, word))

        for _ in range(k):
            _, word = heappop(heapified_words)
            kFrequencies.append(word)

        return kFrequencies
