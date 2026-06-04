class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> m=new HashMap<>();
        int l=nums.length;
        for(int i=0;i<l;i++){
            int c=target-nums[i];
            if(m.containsKey(c)){
                return new int[]{m.get(c),i};
            }
            m.put(nums[i],i);
        }
        return new int[]{};
    }
        
        
}

