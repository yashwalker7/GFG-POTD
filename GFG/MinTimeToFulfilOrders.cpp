

class Solution{
    public:
    int findMinTime(int n, vector<int>&a, int m){
        //write your code here
        int l = 0, hi = 1e9, ans = 0;
        while(l<=hi){
            int mid = (l+hi)/2;
            if(check(mid, a, n, m)){
                ans = mid;
                hi = mid-1;
            }
            else l = mid+1;
        }
        return ans;
    }
    bool check(int mid, vector<int>&a, int n, int m){
        int cnt = 0;
        for(int i= 0; i<m; i++){
            int sum = 0, curr = 0;
            while(sum < mid){
                sum+=(curr+1)*a[i];
                if(sum <= mid)curr++;
            }
            cnt+=curr;
        }
        return cnt>=n;
    }
    
};