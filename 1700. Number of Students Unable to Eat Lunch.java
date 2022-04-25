class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        
        // put students in a queue. students[0] at the beginning of queue
        Queue<Integer> q = new LinkedList<>();
        for (int s : students) {
            q.add(s);
        }
        // put sandwiches in a stack. sandwiches[0] at the top of stack
        Stack<Integer> st = new Stack<>();
        for (int i = sandwiches.length - 1; i >= 0; i--) {
            st.push(sandwiches[i]);
        }
        // keep track of whether all students in the queue can't eat
        int count;
        int len;
        
        while (st.size() != 0) {
            len = st.size();
            count = 0;
            int available_sandwich = st.peek();
            
            // if the student at beginning of queue doesn't want the available sandwich
            // they leave it and go to the queue's end
            while (q.peek() != available_sandwich) {
                int s = q.remove();
                q.add(s);
                count++;
                
                // all students in the queue can't eat
                if (count == len) {
                    // return num of students in the queue. aka num of students can't eat
                    return len; 
                }
            }
            
            // student at the beginning of queue wants the available sandwich
            q.remove();
            st.pop();
        }
        // all sandwiches are sold
        return 0;
    }
}

/*
sandwiches: stack
students: queue

int count;

while sandwiches is not empty:
    int len = sandwiches.length;
    count = 0;
    
    available_sandwich = sandwiches.peek()
    
    while students.peek() != available_sandwich:
        s = students.pop(0)
        students.push(s);
        count++;
        
        if count == len:
            return len // num of students can't eat
    
    // student takes the sandwich
    students.pop(0);
    sandwiches.pop();
    
// all sandwiches are sold
return 0;

*/
