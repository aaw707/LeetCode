import java.util.LinkedList;
import java.util.Queue;

class MyStack {

    // q1: stack
    // q2: helper queue
    Queue<Integer> q1 = new LinkedList<Integer>();
    Queue<Integer> q2 = new LinkedList<Integer>();
    
    public MyStack() {
        
    }
    
    public void push(int x) {
        // no item in stack. just add x in q1
        if (q1.isEmpty()) {
            q1.add(x);
            
        // there's already items in stack. use q2 to add item so that x is on "top"
        } else {
            while (!q1.isEmpty()) {
                q2.add(q1.remove());
            }
            q1.add(x);
            while (!q2.isEmpty()) {
                q1.add(q2.remove());
            }
        }
    }
    
    public int pop() {
        return q1.remove();
    }
    
    public int top() {
        return q1.peek();
    }
    
    public boolean empty() {
        return q1.isEmpty();
        // q2 is always empty outside .push()
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */