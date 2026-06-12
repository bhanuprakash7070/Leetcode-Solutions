class Solution {
public:
    bool isPalindrome(string s) {
        string s_new="";
        for(char ch:s){
            if(isalnum(ch)){
                s_new+=tolower(ch);
            }
        }
        string temp=s_new;
        int l=0;
        int r=s_new.size()-1;
        while(l<r){
            swap(s_new[l],s_new[r]);
            l++;
            r--;
        }
        if(temp==s_new){
            return true;
        }
        else{
            return false;
        }
    }
};
