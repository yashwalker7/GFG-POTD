//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.io.*;


// } Driver Code Ends
//User function Template for Java

class Solution {
    public String removeBrackets(String Exp) {
        char[] a = Exp.toCharArray();
        int b = Exp.length();

        int[] answer = new int[b + 1];
        Arrays.fill(answer, 1);

        int[] last = new int[b + 1];
        int[] nxt = new int[b + 1];

        Arrays.fill(last, -1);
        Arrays.fill(nxt, -1);

        int l = -1;
        for (int i = 0; i < b; i++) {
            last[i] = l;
            if (a[i] == '*' || a[i] == '+' || a[i] == '-' || a[i] == '/')
                l = a[i];
        }

        l = -1;
        for (int i = b - 1; i >= 0; i--) {
            nxt[i] = l;
            if (a[i] == '*' || a[i] == '+' || a[i] == '-' || a[i] == '/')
                l = a[i];
        }

        Stack<Integer> st = new Stack<Integer>();
        int[] sign = new int[256];
        int[] mp = new int[256];

        Arrays.fill(sign, -1);
        char[] operand = {'*', '+', '-', '/'};

        for (int p = 0; p < b; p++) {
            for (char z : operand) {
                mp[z] = 0;
                if (z == a[p])
                    sign[z] = p;
            }
            if (a[p] == '(')
                st.push(p);
            else if (a[p] == ')') {
                int i = st.pop();
                int j = p;

                int nxta = nxt[j];
                int lasta = last[i];

                for (char z : operand) {
                    if (sign[z] >= i) {
                        mp[z] = 1;
                    }
                }
                int k = 0;

                if (i > 0 && j + 1 < b && a[i - 1] == '(' && a[j + 1] == ')')
                    k = 1;
                if (mp['+'] == 0 && mp['*'] == 0 && mp['-'] == 0 && mp['/'] == 0)
                    k = 1;

                if (lasta == -1 && nxta == -1)
                    k = 1;
                if (lasta == '/' ) {

                }
                else if (lasta == '-' && (mp['+'] == 1 || mp['-'] == 1)) {

                }
                else if (mp['-'] == 0 && mp['+'] == 0) {
                    k = 1;
                }
                else {
                    if ((lasta == -1 || lasta == '+' || lasta == '-') && (nxta == -1 || nxta == '+' || nxta == '-'))
                        k = 1;
                }
                if (k == 1) {
                    answer[i] = 0;
                    answer[j] = 0;
                }
            }
        }

        StringBuilder res = new StringBuilder();
        for (int i = 0; i < b; i++) {
            if (answer[i] > 0) {
                res.append(a[i]);
            }
        }
        return res.toString();
    }
}

//{ Driver Code Starts.

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
        	String Exp = read.readLine();
            Solution ob = new Solution();
            System.out.println(ob.removeBrackets(Exp));
        }
        
    }
}
// } Driver Code Ends
