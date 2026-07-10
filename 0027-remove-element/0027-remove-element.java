class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length;
        int left = 0;
        int count = 0;
        for (int right = 0; right < n; right++) {

            if (nums[right] != val) {

                int temp = nums[right];
                nums[right] = nums[left];
                nums[left] = temp;

                left++;
                count++;

            }
        }
        return count;

    }
}