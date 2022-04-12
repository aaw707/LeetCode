class MyHashMap {
    private static final int BUCKET_SIZE = 1000;
    private ListNode[] buckets;
        
    public MyHashMap() {
        buckets = new ListNode[BUCKET_SIZE];
    }
    
    public void put(int key, int value) {
        // remove existing key, if applicable
        remove(key);
        // get the index
        int index = hash(key);
        // construct new node
        ListNode newNode = new ListNode(new Entry(key, value), buckets[index]);
        // insert
        buckets[index] = newNode;
    }
    
    public int get(int key) {
        // get the index
        int index = hash(key);
        // get the head
        ListNode head = buckets[index];
        // go over the nodes in this bucket
        while (head != null) {
            // return the value if key found
            if (head.entry.key == key) {
                return head.entry.val;
            } else {
                head = head.next;
            }
        }
        // return -1 if key not found
        return -1;
    }
    
    public void remove(int key) {
        // get the index
        int index = hash(key);
        // get the head
        ListNode head = buckets[index];
        // key doesn't exist
        if (head == null) {
            return;
        }
        // key at head
        if (head.entry.key == key) {
            buckets[index] = head.next;
            return;
        }
        // go over the nodes in this bucket
        while (head.next != null) {
            if (head.next.entry.key == key) {
                // if key found, remove node
                head.next = head.next.next;
                return;
            } else {
                head = head.next;
            }
        }
        // key doesn't exist
        return;        
    }
    
    public int hash(int key) {
        Integer _key = Integer.valueOf(key);
        // calculate the hash code
        int hash = _key.hashCode();
        // calculate the index
        int index = hash % BUCKET_SIZE;
        return index;
    }
}

class ListNode {
    Entry entry;
    ListNode next;
    
    ListNode(Entry e) {
        this.entry = e;
        this.next = null;
    } 
    ListNode(Entry e, ListNode next) {
        this.entry = e;
        this.next = next;
    }
}

class Entry {
    int key;
    int val;
    
    Entry(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */