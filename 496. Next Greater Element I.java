class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        // create a stack to store the next greater element
        Stack<Integer> st = new Stack<>();
        // length of inputs
        int len1 = nums1.length;
        int len2 = nums2.length;
        // list to store the next greater element for each num in nums2
        int[] greaters = new int[len2];
        
        // find and store the next greater element for each num in nums2
        for (int i = len2 - 1; i >= 0; i--) {
            // if stack is empty, there's no greater element for this num
            if (st.empty()) {
                greaters[i] = -1;
            } else {
                // pop the stack until the top element is greater than num or stack is empty
                while (!st.empty() && st.peek() < nums2[i]) {
                    st.pop();
                }
                // if stack is empty, there's no greater element for this num
                if (st.empty()) {
                    greaters[i] = -1;
                // if stack is not empty, the top element on the stack is the next greater element
                } else {
                    greaters[i] = st.peek();
                }
            }
            // put num onto stack
            st.push(nums2[i]);
        }
        
        // a list to store results
        int[] res = new int[len1];
        // for each num in nums1
        for (int i = 0; i < len1; i++) {
            // for each num in nums2
            for (int j = 0; j < len2; j++) {
                // find the num in nums2 equals to num in nums1
                if (nums1[i] == nums2[j]) {
                    // take the next greater element from greaters and put it into res
                    res[i] = greaters[j];
                    // check the next num in nums1
                    break;
                }
            }
        }
        return res;
    }
}

/*
st = new stack 
greaters = int[nums2.length]

for num in nums2 (backwards):
    if st is empty:
        greaters[i] = -1        
    else:
        while st.peek < num: # all nums are unique. no equals condition
            st.pop()
        if st is empty:
            greaters[i] = -1
        else:
            greaters[i] = st.peek
    
    put num onto stack
    
res = int[nums1.length]
for i in nums1:
    for j in nums2:
        if nums1[i] == nums2[j]:
            res[i] = greaters[j]

return res

*/      