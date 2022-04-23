class Solution {
    public int[] finalPrices(int[] prices) {
        // stack to store current min price (backwards)
        Stack<Integer> stack = new Stack<>();
        // length of prices
        int len = prices.length;
        // discounts list
        int[] discounts = new int[len];
        
        // loop over each price backwards
        for (int i = len - 1; i >= 0; i--) {
            // if stack is empty: no prices[j] for j > i and prices[j] <= prices[i]
            if (stack.empty()) {
                // no discount
                discounts[i] = prices[i];        
                
            // stack is not empty
            } else {
                // remove the top of stack that's larger than prices[i]
                // until the stack is empty, or the top of stack <= prices[i]
                while (!stack.empty() && stack.peek() > prices[i]) {
                    stack.pop();
                }
                // the stack is empty, no discount
                if (stack.empty()) {
                    discounts[i] = prices[i];
                // stack is not empty, discount applies
                } else {
                    discounts[i] = prices[i] - stack.peek();
                }
            }
            // push the current price to the top of stack
            stack.push(prices[i]);
        }
        return discounts;
        
    }
}

