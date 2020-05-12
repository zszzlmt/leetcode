class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = bin(N)
        result = str()
        for idx in range(2, len(binary)):
            result += "0" if binary[idx] == "1" else "1"
        print(binary, result)
        return int(result, 2)
