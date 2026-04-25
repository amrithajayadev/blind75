class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs: 
            encoded.append(f"{len(s)}#")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        words = []
        while i < n:
            j = i
            
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            i = j+1
            j = i + num
            words.append(s[i:j])
            i = j
        return words



