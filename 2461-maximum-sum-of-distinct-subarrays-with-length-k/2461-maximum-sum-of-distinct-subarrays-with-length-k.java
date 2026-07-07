class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        int n = nums.length;
        long maxSum = 0, winSum = 0;
        int left = 0;

        Map<Integer, Integer> map = new HashMap<>();

        for (int right = 0; right < n; right++) {

            map.put(nums[right], map.getOrDefault(nums[right], 0) + 1);

            if (right == left + k) {
                winSum -= nums[left];
                map.put(nums[left], map.get(nums[left]) - 1);
                if (map.get(nums[left]) == 0) {
                    map.remove(nums[left]);
                }
                left++;
            }
            winSum += nums[right];
            if (map.get(nums[right]) >= 2) {

                while (left <= right) {
                    winSum -= nums[left];
                    map.put(nums[left], map.get(nums[left]) - 1);
                    left++;
                    if (map.get(nums[right]) == 1) {
                        break;
                    }
                }
            }
            if (right - left + 1 != k) {
                continue;
            }

            maxSum = Math.max(winSum, maxSum);
            if (map.size() < k) {
                maxSum = 0;
            }

        }
        return maxSum;
    }
}