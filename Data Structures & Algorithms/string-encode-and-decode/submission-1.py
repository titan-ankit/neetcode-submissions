class Solution:

    def encode(self, strs: List[str]) -> str:
        final = []
        for s in strs:
            final.append(f"{len(s)}#{s}")
        return "".join(final)

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while (i<(len(s))):
            j = i
            while (s[j]!='#'):
                j += 1
            
            length = int(s[i:j])
            
            i = j+1

            string = s[i:i+length]

            final.append(string)

            i += length
        return final
