/*You are required to complete this method */

class Solution
{
    static int val=0;
    public boolean isKPartitionPossible(int a[], int n, int k)
    {
	// Your code here	
	int sum=0;
	val=0;
	for(int i:a)
	{
	    sum+=i;
	}
	if(sum%k!=0) return false;
	int vis[]=new int[n];
	return isPossible(a,sum/k,0,n,k,vis);
    }
    static boolean isPossible(int[] a,int target,int currSum, int n,int k, int vis[])
    {
        if (k==0) return true;
        if(target==currSum)
        {
            currSum = 0;
            return (isPossible(a, target, currSum,n,k-1,vis));
        }
        if (currSum>target) return false;
        for(int i=0;i<n;i++)
        {
            if(vis[i]==0)
            {
                vis[i]=1;
                if(isPossible(a,target,currSum+a[i],n,k,vis)) return true;
                vis[i] = 0;
            }
        } return false;
    }
}
