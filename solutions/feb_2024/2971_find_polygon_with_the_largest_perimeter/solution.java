import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
  public long largestPerimeter(int[] nums) {
    Arrays.sort(nums);

    List<Long> prefixSum = new ArrayList<>();
    long curSum = 0;
    for (int num : nums) {
      curSum += num;
      prefixSum.add(curSum);
    }

    for (int i = nums.length - 1; i >= 1; i--) {
      if (prefixSum.get(i) < prefixSum.get(i - 1) * 2) {
        return prefixSum.get(i);
      }
    }

    return -1;
  }
}
