class Solution {
    public List<String> cellsInRange(String s) {
        // find rows and columns
        char col1 = s.charAt(0);
        char row1 = s.charAt(1);
        char col2 = s.charAt(3);
        char row2 = s.charAt(4);
        // construct list of cells
        List<String> res = new ArrayList<>();
        int i = 0;
        // add each cell to res
        for (char col = col1; col <= col2; col++) {
            for (char row = row1; row <= row2; row++) {
                res.add(String.valueOf(col) + String.valueOf(row));
                i++;
            }
        }
        return res;
    }
}