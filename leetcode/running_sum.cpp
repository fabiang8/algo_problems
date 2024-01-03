// running sum of 1d array

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) 
    {
        int sum = 0;
        vector<int> newnums;
        for(int i = 0; i < nums.size(); i++)
        {
            sum += nums[i];
            newnums.push_back(sum); 
        }
        return newnums;
    }
};