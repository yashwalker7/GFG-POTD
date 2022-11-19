class Solution {
    public:
    
    long long lcmTriplets(long long N) {
        // code here
        if(N==1 || N==2)
        return N;
        if(N&1==1)
        return (N)*(N-1)*(N-2);
        else if(__gcd(N,N-3)!=1)
        {
            return (N-1)*(N-2)*(N-3);
        }
        else
        return N*(N-1)*(N-3);
    }
};
