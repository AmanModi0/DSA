class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int n = nums.length;
        int countOnes = 0;
        int maxOnes = 0;
        int i=0;
        while (i < n) {
            if (nums[i] == 1) {
                countOnes++;
            } else {
                countOnes = 0;
            }
            maxOnes = Math.max(countOnes, maxOnes);
            i++;
        }
        return maxOnes;
    }
}