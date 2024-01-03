class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0; // first index
        int r = nums.size() - 1; // last index
        int m = (l + r) / 2; // middle index
        
        while(l <= r) // continue while left and right dont meet
        {
            
           
            if(nums[m] == target) // if midpoint is target
            {
                return m;
            }
            if(target > nums[m]) // targe is greater than mid index
            {
                l = m + 1; // left index become m + 1
                m = (l + r) / 2; // recalculate midpoint
                
            }
            else if( target < nums[m]) // target less than mid
            {
                r = m - 1;
                m = (l + r) / 2;
            }
            
        }
        return l;
    }
};