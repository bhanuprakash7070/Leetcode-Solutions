class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int sp=0;
        for(int fp=0;fp<nums.size();fp++){
            if(nums[fp]!=val){
                nums[sp]=nums[fp];
                sp++;
            }
        }
        return sp;
    }
};
