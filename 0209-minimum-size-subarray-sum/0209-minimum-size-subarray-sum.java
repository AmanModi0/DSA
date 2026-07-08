class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int len = nums.length + 1;
        int left = 0;
        int win = 0;

        for (int right = 0; right < nums.length; right++) {

            win += nums[right];

            while (win >= target && left <= right) {
                len = Math.min(len, right - left + 1);
                win -= nums[left];
                left++;
            }
        }
        if (len == nums.length + 1) {
            return 0;
        } else {
            return len;
        }
    }
}