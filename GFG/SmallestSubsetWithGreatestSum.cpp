
class Solution{
    public:
    int minSubset(vector<int> &arr,int n){

        if(n==1) return 1;

        sort(arr.begin(),arr.end());

        long long int ans=1,temp=0,a=0;

        for(int i=0;i<n;i++) a+=arr[i];

        for(int i=n-1;i>0;i--){

            temp+=arr[i];

            if(a-temp < temp)

                return ans;

            else

                ans++;

        }

    }
};