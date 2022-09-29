    void increment(vector<vector<int>> &matrix, int a1, int a2, int b1, int b2)
{
        for(int i=a1;i<=a2;i++)
        {
            for(int j=b1;j<=b2;j++)
            matrix[i][j]++;
        }
    }
    public:
    vector<vector<int>> solveQueries(int n, vector<vector<int>> Queries) {
        // Code here
              vector<vector<int>> mat(n, vector<int> (n, 0));

        for(int i=0;i<Queries.size();i++)
        {
            int a1= Queries[i][0];
            int b1= Queries[i][1];
            int a2= Queries[i][2];
            int b2= Queries[i][3];

            increment(mat, a1, a2, b1, b2);
        }
        return mat;
    }
};