class MyHashSet {
    ListNode head;
    
    public MyHashSet() {   
        head = null;
    }
    
    public void add(int key) {
        ListNode newNode = new ListNode(key);
        if (head == null) {
            head = newNode;
        } 
        if (!contains(key)) {
            newNode.next = head.next;
            head.next = newNode;            
        }
    }
    
    public void remove(int key) {
        if (head == null) {
            return;
        }
        if (head.val == key) {
            head = head.next;
        }
        ListNode node = head;
        while (node.next != null) {
            if (node.next.val == key) {
                node.next = node.next.next;
                return;
            } else {
                node = node.next;                
            }
        }
    }
    
    public boolean contains(int key) {
        ListNode node = head;
        while (node != null) {
            if (node.val == key) {
                return true;
            } else {
                node = node.next;
            }
        }
        return false;
    }
}

class ListNode {
    int val;
    ListNode next;
    public ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}



/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */