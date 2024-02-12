class Solution {
  public int majorityElement(int[] nums) {
    int curNum = nums[0];
    int count = 1;

    for (int i = 1; i < nums.length; i++) {
      if (nums[i] == curNum) {
        count++;
        continue;
      }

      if (count == 0) {
        curNum = nums[i];
        count = 1;
      } else {
        count--;
      }
    }

    return curNum;
  }
}
