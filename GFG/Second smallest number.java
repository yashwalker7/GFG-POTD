class Solution{
    static String secondSmallest(int S, int D){
        // code here
        int[] num = new int[D];
        for (int i = D - 1; i>0; i--) {
            int d = Math.min(S-1,9);
            num[i] = d;
            S -= d;
        }
        if (S>9){
            return "-1";
        }
        num[0] = S;
        for (int i = D -1; i>0;i--) {
            if(num[i] != 0 && num[i-1] !=9){
                num[i] -= 1;
                num[i-1] += 1;
                StringBuilder sb = new StringBuilder();
                for (int j=0; j<D; j++) {
                    sb.append(num[j]);
                }
                return sb.toString();
            }
        }
        return "-1";
