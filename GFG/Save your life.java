class Solution{
    static String maxSum(String w,char x[],int b[], int n){
        //code here
        int maxI=Integer.MIN_VALUE;
        int sum=0;
        String ans="";
        for(int i=0, j=0;j<w.length();j++){
            sum=sum+decode(w.charAt(j),x,b);
            if (maxI<sum){
                maxI=sum;
                ans=w.substring(i,j+1);
                }
                if(sum<0){
                i=j+1;sum=0;
            }
        }
        return ans;
    }
    public static int decode(char c,char[] x,int[] b){
        for(int i=0;i<x.length;i++){
            if(x[i]==c){
                return b[i];
            }
        }
        return c;
    }
}
