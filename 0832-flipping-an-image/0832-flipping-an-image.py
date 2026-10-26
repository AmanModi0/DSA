class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in image:
            i.reverse()
            for j in range(len(i)):
                i[j] = int(not i[j])
        return image
