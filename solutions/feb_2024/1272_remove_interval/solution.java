import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
  public List<List<Integer>> removeInterval(int[][] intervals, int[] toBeRemoved) {
    List<List<Integer>> result = new ArrayList<>();
    int s1 = toBeRemoved[0];
    int e1 = toBeRemoved[1];

    for (int[] interval : intervals) {
      int s2 = interval[0];
      int e2 = interval[1];

      if (e2 <= s1 || e1 <= s2) {
        result.add(Arrays.asList(s2, e2));
        continue;
      }

      if (s2 < s1) {
        result.add(Arrays.asList(s2, s1));
      }
      if (e1 < e2) {
        result.add(Arrays.asList(e1, e2));
      }
    }

    return result;
  }
}
