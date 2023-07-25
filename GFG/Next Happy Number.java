

//User function Template for Java

class Solution{

    static int isHappy(int N){
        // code here
        if (N == 1 || N == 7)
        return 1;
        int sum = N, a = N;
        
        while(sum>9)
        {
            sum = 0;
            while (a > 0) {
                int b = a%10;
                sum += b*b;
                a/=10;
            }
            if (sum == 1)
            return 1;
            a = sum;
        }
        if (sum == 7)
        return 1;
        return 0;
    }
    static int nextHappy(int N)
    {
        int a=N+1;
        int res=a;
        
        while(true)
        {
            if(isHappy(a)==1)
            return a;
            
            a++;
            res=a;
        }
    }
}
