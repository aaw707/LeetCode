class Solution {
    public int maxProfit(int[] prices) {
        // record the current max profit
        int max_profit = 0;
        // record the current lowest buying price
        int buying_price = prices[0];
        
        // go over each day
        for (int price : prices) {
            // if the price of this day is lower than current lowest price recorded, update the lowest price
            if (price < buying_price) {
                buying_price = price;
            }    
            // calculate the profit by subtract lowest price from price of today
            int profit = price - buying_price;
            // if profit is larger than the max profit recorded, update max profit
            if (profit > max_profit) {
                max_profit = profit;
            }
        }
        return max_profit;
    }
}