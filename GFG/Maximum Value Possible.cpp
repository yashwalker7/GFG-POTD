//{ Driver Code Starts
//Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution {
public:
    long long maxPossibleValue(int N,vector<int> A, vector<int> B) {
        long long ans = 0, t = 0, z = 0, n = A.size();
        for(int i = 0; i < N; i++) B[i] /= 2;
        int x = INT_MAX;
        for(int i = 0; i < N; i++) {
            if(B[i]) x = min(A[i], x);
            t += B[i] * A[i];
            z += B[i];
        }
        if(z % 2) t -= x;
        return t * 2;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin>>N;
        vector<int> A(N), B(N);
        for(int i=0;i<N;i++){
            cin>>A[i];
        }
        for(int i=0;i<N;i++){
          cin>>B[i];
        }
        Solution obj;
        auto ans = obj.maxPossibleValue(N,A,B);
        cout<<ans<<endl;
    }
} 
// } Driver Code Ends
