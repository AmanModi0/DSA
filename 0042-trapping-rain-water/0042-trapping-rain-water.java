class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int left = 0;
        int right = n - 1;
        int water = 0;
        int lmax = 0;
        int rmax = 0;

        while (left < right) {

            lmax=Math.max(height[left],lmax);
            rmax=Math.max(height[right],rmax);

            if (lmax < rmax) {
                water+= lmax -height[left];
                left++;
            }
            else{
                water+=rmax-height[right];
                right--;
            }
        }
        return water;
    }
}