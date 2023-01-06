class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        result_in_k_and_f = []
        result_in_k_and_f.append(celsius + 273.15)
        result_in_k_and_f.append(celsius * 1.80 + 32.00)
        return result_in_k_and_f
