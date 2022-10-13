
class Solution{
    public:
    int maximizeSum(int a[], int n) 
    {
        // Complete the function
        int F[100001]{};
        for (int i=0; i<n; i++)
            F[a[i]]++;
        int res = 0;
        for (int i=100000; i>=0; i--) {
            int x = F[i];
            if (x) {
                res += x*i;
                if (i) {
                    F[i-1] = max(F[i-1]-x, 0);
                }
            }
        }
        return res;
    }
};
