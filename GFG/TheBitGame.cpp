public:
    int swapBitGame(long long N){
        // code here 
        long long a=0;
        long long b=0;
        while(N) {
            if(N%2 && b>0)
            {
                a^=b;
            }
            if(N%2==0)
            {
                b++;
            }
            N/=2;
        }
        if(a)
        return 1;
        else
        return 2;
    }
};