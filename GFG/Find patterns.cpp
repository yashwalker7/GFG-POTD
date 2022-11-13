//User function template for C++

class Solution{   
public:
    int numberOfSubsequences(string S, string W){
        // code here 
        int a = 0;
        for(int i=0; i<S.size(); i++)
        {
            if(S[i] == W[a])
            {
                a++;
                S[i] = ' ';
            }
            if(a == W.size()) break;
        }
        if(a == W.size())
        return 1 + numberOfSubsequences(S, W);
        return 0;
    }
};
