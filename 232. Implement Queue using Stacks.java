class MyQueue {

    Stack<Integer> input = new Stack<Integer>();
    Stack<Integer> output = new Stack<Integer>();
        
    public MyQueue() {
        
    }
    
    public void push(int x) {
        input.push(x);
        
    }
    
    public int pop() {
        if (!output.empty()) {
            return output.pop();
        } else {
            while (!input.empty()) {
                int item = input.pop();
                output.push(item);                
            }
            return output.pop();
        }
        
    }
    
    public int peek() {
        if (!output.empty()) {
            return output.peek();
        } else {
            while (!input.empty()) {
                int item = input.pop();
                output.push(item);                     
            }
            return output.peek();
        }
        
    }
    
    public boolean empty() {
        return (input.empty() && output.empty());
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */