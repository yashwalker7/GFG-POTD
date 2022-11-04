class Solution {
    static int maxGroupSize(int[] arr, int N, int K) {
        // code here
        int[] temp = new int[K];
        for(int i: arr) temp[i % K]++;
        int ans = 0, i=1, j= K-1;
        while(i<j) {
            ans += Math.max(temp[i++], temp[j--]);
            
        }
        if(i==j && temp[i] > 0) ans++;
        if(temp[0] > 0) ans++;
        return ans;
    }
};
