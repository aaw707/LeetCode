class MinStack {
    int min;
    Node head;
    Node tail;
    
    public MinStack() {
        min = Integer.MIN_VALUE;
        head = null;
        tail = null;
    }
    
    public void push(int val) {
        // node to be pushed
        Node n = new Node(val);
        // if no node in stack, n becomes head & tail, min = n.val
        if (head == null) {
            min = val;
            head = n;
            tail = n;
            n.next = n;
            n.prev = n;            
        // if already nodes in stack, append n to the end
        } else {
            tail.next = n;
            n.prev = tail;
            n.next = head;
            head.prev = n;
            tail = n;
            // if n.val < min, n.val is the new min
            if (val < min) {
                min = val;
            }
        }
    }
    
    public void pop() {
        // if only one node in stack, the stack is empty after the pop
        if (head == tail) {
            min = Integer.MIN_VALUE;
            head = null;
            tail = null;
        // if more than one node in stack
        } else {
            // remove the tail node
            Node n = tail;
            n.prev.next = n.next;
            n.next.prev = n.prev;
            tail = n.prev;
            // if the removed node was the min, find the new min
            if (n.val == min) {
                min = head.val;
                Node c = head.next;
                // go over the stack to find the min
                while (c != head) {
                    if (c.val < min) {
                        min = c.val;
                    }
                    c = c.next;
                }
            }
        }
    }
    
    public int top() {
        return tail.val;
    }
    
    public int getMin() {
        return min;
    }
    
    // use node to represent each val in min stack
    class Node {
        
        int val;
        Node next;
        Node prev;
        
        Node(int val) {
            this.val = val;
            prev = null;
            next = null;
        }
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */