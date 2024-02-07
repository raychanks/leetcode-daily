import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
  public String frequencySort(String s) {
    Map<Character, Integer> counter = new HashMap<>();

    for (Character c : s.toCharArray()) {
      counter.put(c, counter.getOrDefault(c, 0) + 1);
    }

    List<Character> chars = new ArrayList<>(counter.keySet());
    Collections.sort(chars, (a, b) -> counter.get(b) - counter.get(a));

    StringBuilder sb = new StringBuilder();
    for (Character c : chars) {
      for (int i = 0; i < counter.get(c); i++) {
        sb.append(c);
      }
    }

    return sb.toString();
  }
}
