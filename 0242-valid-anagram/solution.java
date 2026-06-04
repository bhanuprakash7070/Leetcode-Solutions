class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> m=new HashMap<>();
        if (s.length()!=t.length()){
            return false;
        }
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            m.put(ch,m.getOrDefault(ch,0)+1);
        }
        for(int i=0;i<t.length();i++){
            char ch=t.charAt(i);
            if(!m.containsKey(ch) || m.get(ch)==0){
                return false;
            }
            m.put(ch,m.get(ch)-1);
        }
        return true;
    }
}
