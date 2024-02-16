import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
  public int findLeastNumOfUniqueInts(int[] arr, int k) {
    Map<Integer, Integer> counter = new HashMap<>();
    for (int num : arr) {
      counter.put(num, counter.getOrDefault(num, 0) + 1);
    }

    List<Integer> frequencies = new ArrayList<>(counter.values());
    Collections.sort(frequencies);

    int removedCount = 0;
    for (int freq : frequencies) {
      if (k < freq) {
        break;
      }

      k -= freq;
      removedCount += 1;
    }

    return frequencies.size() - removedCount;
  }
}
