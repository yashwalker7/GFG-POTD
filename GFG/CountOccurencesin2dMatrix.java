public 

//User function Template for Java

class Solution
{
    public int findOccurrence(char mat[][], String target)
    {
        // Write your code here
        
        int m = mat.length;
        int n = mat[0].length;
        int ans = 0;
        for(int i=0;i<m;++i) {
            for(int j=0;j<n;++j) {
                if(mat[i][j] == target.charAt(0)) {
                    ans += dfs(mat, i, j, target, 0);
                }
            }
        }
        return ans;
    }
    
    public int dfs(char[][] mat, int i, int j, String target, int index) {
        int m = mat.length;
        int n = mat[0].length;
        
        int found = 0;
        
        if(i >=0 && i < m && j >= 0 && j < n && target.charAt(index) == mat[i][j]) {
            char temp = mat[i][j];
            mat[i][j] = 0;
            ++index;
            if(index == target.length()) {
                found = 1;
            } else {
                found += dfs(mat, i+1, j, target, index);
                found += dfs(mat, i, j+1, target, index);
                found += dfs(mat, i, j-1, target, index);
                found += dfs(mat, i-1, j, target, index);
            }
            mat[i][j] = temp;
        }
        return found;
    }
} {
    
}
