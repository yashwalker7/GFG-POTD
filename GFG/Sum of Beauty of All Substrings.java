class Solution {
    public static int beautySum(String str){
        // code here
        int sum=0;
        for(int i=0; i < str.length(); i++)
        {
            int [] a = new int[26];
            for(int j=i; j<str.length(); j++)
            {
                a[str.charAt(j)-'a']++;
                int max=-1;
                int min=501;
                
                for(int k=0; k<26;k++)
                {
                    max=Math.max(a[k], max);
                    if(a[k]!=0) min = Math.min(a[k],min);
                }
                sum+=max-min;
            }
        }
        return sum;
    }
}
     
