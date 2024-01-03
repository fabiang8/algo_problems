class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int l = 0; // vector start
        int r = nums.size() - 1; // vector end
        int m = r / 2; // mid point
        
        while ( l <= r)
        {
            if (nums[m] < target) // if target is greater than midpoint
            {
                l = m + 1; // left point is now midpoint + 1
                m = (l + r) / 2; // calculate new midpoint 
            }
            else if ( nums[m] > target)
            {
                r = m - 1;
                m = (l + r) / 2;
            }
            else
            {
                return m;
            }
        }
        return -1;
        
    }
};