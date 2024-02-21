class Solution {
  public int rangeBitwiseAnd(int left, int right) {
    while (right > left) {
      right &= right - 1;
    }

    while (left > right) {
      left &= left - 1;
    }

    return left;
  }
}
