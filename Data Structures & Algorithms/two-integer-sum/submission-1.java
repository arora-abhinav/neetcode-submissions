class Solution {
    public int[] twoSum(int[] nums, int target) {
        int indOne = 0;
        int indTwo = 0;
        int[] arr = new int[2];
        HashMap<Integer, Integer> ints = new HashMap<>();
        for(int i = 0; i < nums.length; i ++){
            ints.put(nums[i], i);
        }
        for(int i = 0; i < nums.length; i++){
            Integer diff = target - nums[i];
            if(ints.containsKey(diff) && i != ints.get(diff)){
                indOne = i;
                indTwo = ints.get(diff);
            }
        }
        if(indTwo > indOne){
            arr[0] = indOne;
            arr[1] = indTwo;
        }
        else{
            arr[1] = indOne;
            arr[0] = indTwo;
        }
        return arr;
    }
}
