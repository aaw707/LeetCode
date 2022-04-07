class KthLargest {

    PriorityQueue<Integer> queue = new PriorityQueue<>();
    int k;
    
    public KthLargest(int k, int[] nums) {
        this.k = k;
        // add nums to queue
        for (int n : nums) {
            queue.add(n);
        }
    }
    
    public int add(int val) {
        // add val to queue
        queue.add(val);
        // only save the largest k values
        while (queue.size() > k) {
            queue.poll();
        }
        // return the kth largest
        return queue.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */