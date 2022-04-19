class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        // find the idx of the list by the rule key
        int idx;
        if (ruleKey.equals("type")) {
            idx = 0;
        } else if (ruleKey.equals("color")) {
            idx = 1;
        } else {
            idx = 2;
        }
        // keep count of matching items
        int count = 0;
        // loop over items
        for (List<String> item : items) {
            // if value == rule value, count+1
            if (item.get(idx).equals(ruleValue)) {
                count++;
            }
        }
        return count;
    }
}