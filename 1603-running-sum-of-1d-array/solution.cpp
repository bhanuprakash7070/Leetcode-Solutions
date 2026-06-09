class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int>ans;
        int rs=0;
        for(int i=0;i<nums.size();i++){
            
            rs+=nums[i];
            ans.push_back(rs);
        }
        return ans;
    }
};
