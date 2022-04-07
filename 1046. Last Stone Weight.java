class Solution {
    public int lastStoneWeight(int[] stones) {
        // create a priority queue
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>(Collections.reverseOrder());
        // add each stone in the queue (sorted from max to min)
        int size = stones.length;
        for (int i = 0; i < size; i++) {
            queue.add(stones[i]);
        }
        // loop until there's at most 1 stone left
        while (queue.size() > 1) {
            int stone1 = queue.poll();
            int stone2 = queue.poll();
            // if 2 stones have the same weight, both are crashed
            // 2 stones have different weight, one remains with the weight difference
            if (stone1 != stone2) {
                queue.add(stone1 - stone2);
            }
        }
        
        // 1 stone left, return the weight of it
        if (queue.size() == 1) {
            return queue.poll();
        
        // 0 stone left
        } else {
            return 0;    
        }
    }
}