class Solution {
  public int maxSumAfterPartitioning(int[] arr, int k) {
    int[] dp = new int[arr.length + 1];

    for (int i = arr.length - 1; i >= 0; i--) {
      for (int j = 1; j <= k; j++) {
        if (i + j > arr.length) {
          break;
        }

        int localMax = 0;
        for (int m = i; m < i + j; m++) {
          localMax = Math.max(localMax, arr[m]);
        }

        int localSum = localMax * j;
        dp[i] = Math.max(dp[i], localSum + dp[i + j]);
      }
    }

    return dp[0];
  }
}
