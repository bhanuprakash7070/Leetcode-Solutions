class Solution {
    public int[] limitOccurrences(int[] nums, int k) {
        Map<Integer,Integer> m=new HashMap<>();
        ArrayList<Integer> l=new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            int f=m.getOrDefault(nums[i],0);
            if(f<k){
                l.add(nums[i]);
                m.put(nums[i],f+1);
            }
        }
        int[] ans=new int [l.size()];
        for(int i=0;i<ans.length;i++){
            ans[i]=l.get(i);
        }
        return ans;

        }
    }

