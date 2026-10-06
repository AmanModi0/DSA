class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        count = 0
        while True:
            if (
                c["b"] - 1 >= 0
                and c["a"] - 1 >= 0
                and c["l"] - 2 >= 0
                and c["o"] - 2 >= 0
                and c["n"] - 1 >= 0
            ):
                c["b"] -= 1
                c["a"] -= 1
                c["l"] -= 2
                c["o"] -= 2
                c["n"] -= 1
                count += 1
            else:
                return count
