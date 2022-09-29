
class Solution{
public:
    int minLength(string s, int n) {
        // code here
        stack<char> a;
       for(int i=0;i<n;i++){
           if(a.empty()){
               a.push(s[i]);
           }else{
             int k=a.top()-'0';
             int h=s[i]-'0';
             if((k==4&&h==5)||(k==5&&h==4)||(k==6&&h==7)||(k==7&&h==6)||(k==0&&h==1)||(k==1&&h==0)||(k==2&&h==3)||(k==3&&h==2)||(k==8&&h==9)||(k==9&&h==8)){
                 a.push(s[i]);
             }
            else if((k+1==h)||(k==h+1)||(k==0&&h==9)||(k==9&&h==0)){
                 a.pop();
             }else{
                 a.push(s[i]);
             }
           }
       }
       return a.size();
    } 
};
