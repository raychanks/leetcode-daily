class Solution {
  public int missingNumber(int[] nums) {
    int missing = 0;

    for (int i = 1; i <= nums.length; i++) {
      missing ^= i ^ nums[i - 1];
    }

    return missing;
  }
}
