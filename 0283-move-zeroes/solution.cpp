class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int sp=0;
        for(int fp=0;fp<nums.size();fp++){
            if(nums[fp]!=0){
                swap(nums[sp],nums[fp]);
                sp++;
            }
        }
    }
};
