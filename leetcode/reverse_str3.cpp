class Solution {
public:
    
    string reverseword(string s, int l, int r)
    {
        //int l = 0;  // first index
        //int r = s.size() - 1;  // last index 
        while( l <= r)
        {
            char holder = s[l];  // set variable to variable to hold
            s[l] = s[r]; // left value replaced with right
            s[r] = holder; // right value replaced with left
            l++; // increment left val
            r--; // decrement right val
        }
        return s;
    }
    
    string reverseWords(string s) {
        int start = 0;
        int end = 0;
        for ( int i = 0; i <= s.size() - 1; i++)
        {
            if( isspace(s[i]) ) // end = i
            {
                end = i - 1; // set end to i , last value in word
                s = reverseword(s,start,end); // reverse only start end segment of string
                i++;
                start = i; // start and end reset
                end = i;
               // return;
            }
            else if( i == s.size() - 1)
            {
                end = i;
                s = reverseword(s,start,end);
            }
        }
    return s;
    }
};