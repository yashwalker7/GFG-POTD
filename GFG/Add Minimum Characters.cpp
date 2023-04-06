//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
//User function Template for C++

class Solution{   
public:
    int addMinChar(string str){    
        //code here
            int n=str.length();
            int i=0, j=n-1;
            int count=0;
            while(i<j)
            {
                if(str[i]==str[j])
                {
                    i++;
                    j--;
                }
                else
                {
                    count++;
                    i=0;
                    j=n-1-count;
                }
            }
            return count;
        }
        
    };

//{ Driver Code Starts.


int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string str;
        cin >> str;
        
        Solution ob;
        cout << ob.addMinChar(str) << endl;
    }
    return 0; 
} 
// } Driver Code Ends
