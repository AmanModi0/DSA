class Solution {
    public int longestOnes(int[] nums, int k) {
        int n = nums.length;
        int countZero = 0;
        int l = 0;
        for (int r = 0; r < n; r++) {

            if (nums[r] == 0) {
                countZero++;
            }

            if (countZero > k) {
                if (nums[l] == 0) {
                    countZero--;
                }
                l++;
            }
        }
        return n - l;
    }
}
