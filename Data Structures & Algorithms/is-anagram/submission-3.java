class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap <Character, Integer> sMap = new HashMap<>();
        HashMap <Character, Integer> tMap = new HashMap<>();
        for(Character c : s.toCharArray()){
            if(sMap.containsKey(c)){
                sMap.put(c, sMap.get(c) + 1);
            }
            else{
                sMap.put(c, 1);
            }
        }
        for(Character c : t.toCharArray()){
            if(tMap.containsKey(c)){
                tMap.put(c, tMap.get(c) + 1);
            }
            else{
                tMap.put(c, 1);
            }
        }
        for(Character c: sMap.keySet()){
            if(!tMap.containsKey(c) || !tMap.get(c).equals(sMap.get(c))){
                return false;
            }
        }
        for(Character c: tMap.keySet()){
            if(!sMap.containsKey(c) || !sMap.get(c).equals(tMap.get(c))){
                return false;
            }
        }
        return true;
     }
}
