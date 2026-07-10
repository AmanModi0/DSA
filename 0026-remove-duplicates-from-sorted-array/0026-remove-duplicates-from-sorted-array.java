class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        int left = 0;
        int unique = 1;
        Arrays.sort(nums);
        for (int right = 1; right < n; right++) {

            int num = nums[left];
            if (nums[right] != num) {
                left++;
                int temp = nums[right];
                nums[right] = nums[left];
                nums[left] = temp;
                unique++;
            }
        }
        return unique;
    }
}