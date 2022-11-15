class Solution {
  public:
    int longestPerfectPiece(int arr[], int N) {
        // code here
        multiset<int> ms;
        int k=0, ans = 0;
        for(int i=0; i<N; i++)
        {
            ms.insert(arr[i]);
            while(k<N and !ms.empty() and *ms.rbegin() - *ms.begin() > 1)
            ms.erase(arr[k++]);
            ans = max(ans, i-k+1);
        }
         while(k < N and !ms.empty() and *ms.rbegin() - *ms.begin() > 1)
        ms.erase(arr[k++]);
        ans=max(ans, N-k);
        return ans;
    }
};
