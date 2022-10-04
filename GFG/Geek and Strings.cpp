class Solution{
public:
    vector<int> prefixCount(int N, int Q, string li[], string query[])
    {
        unordered_map<string,int>m;
        for (int i=0;i<N;i++)
        {
            string s="";
            int l=li[i].length();
            for(int j=0;j<l;j++)
            {
                s+=li[i][j];
                m[s]++;
            }
        }
        vector<int> ans(Q,0);
        for(int i=0;i<Q;i++)
        ans[i]=m[query[i]];
        
        return ans;
    }
};