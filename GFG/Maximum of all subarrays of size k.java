//User function template for JAVA

class Solution
{
    //Function to find maximum of each subarray of size k.
    static ArrayList <Integer> max_of_subarrays(int arr[], int n, int k)
    {
        // Your code here
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0;i<=n-k;i++)
        {
            int max = 0;
            for(int j=i;j<k+i;j+=1)
            {
                if(arr[j]>max)
                max = arr[j];
            }
            list.add(max);
        }
        return list;
        
        
    }
}
