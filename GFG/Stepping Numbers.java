class Solution{
    static int c = 0;
    int steppingNumbers(int n, int m){
        c=0;
        for(int i=1;i<10;i++)
        {
            solve(i,n,m);
        }
        if(n==0)
        return c+1;
        else
        return c;
    }
    void solve(int i,int n,int m)
    {
        if(i<=m && i>=n)c++;
        else if (i>m)return ;
        int last = i%10;
        int num1 = i*10+last+1;
        int num2 = i*10+last-1;
        if(last==0)solve(num1,n,m);
        else if(last==9)solve(num2,n,m);
        else
        {solve(num1,n,m);
        solve(num2,n,m);}
    }
}
