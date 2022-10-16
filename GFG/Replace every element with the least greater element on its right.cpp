class Solution{
    public:
    vector<int> findLeastGreater(vector<int>& arr, int n) {
        vector<int>ris(n);
        set<int>lista;
        int i;
        ris[n-1] = -1;
        for (i=n-2; i>=0; i--)
        {
            lista.emplace(arr[i+1]);
            auto it = lista.upper_bound(arr[i]);
            if (it == lista.end())
            ris[i] = -1;
            else
            ris[i] = *it;
        }
        return ris;
    }
};
