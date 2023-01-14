class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            if representitives[x] == x:
                return x

            representitives[x] = find(representitives[x])

            return representitives[x]

        def union(x, y):
            x = find(x)
            y = find(y)

            if x == y:
                return

            if x < y:
                representitives[y] = x
            else:
                representitives[x] = y

        representitives = [i for i in range(26)]

        for i in range(len(s1)):
            union(ord(s1[i]) - ord("a"), ord(s2[i]) - ord("a"))

        ans = ""

        for char in baseStr:
            ans += chr(find(ord(char) - ord("a")) + ord("a"))

        return ans
