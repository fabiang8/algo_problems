class Solution {
public:
    void reverseString(vector<char>& s) {
        
        int l = 0;  // first index
        int r = s.size() - 1;  // last index 
        while( l <= r)
        {
            char holder = s[l];  // set variable to variable to hold
            s[l] = s[r]; // left value replaced with right
            s[r] = holder; // right value replaced with left
            l++; // increment left val
            r--; // decrement right val
        }
        
    }
};