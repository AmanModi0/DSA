class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        if bills[0] == 10 or bills[0] == 20:
            return False
        change = {5: 0, 10: 0, 20: 0}
        for i in bills:
            change[i] += 1
            if i == 10:
                if change.get(5) < 1:
                    return False
                else:
                    change[5] -= 1
            elif i == 20:
                if change.get(10) < 1:
                    if change.get(5) < 3:
                        return False
                    else:
                        change[5] -= 3
                elif change.get(5) < 1:
                    return False
                else:
                    change[10] -= 1
                    change[5] -= 1
        return True
