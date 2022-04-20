import java.util.*;
class Solution {
    public int countPoints(String rings) {
        // num of rings
        int n = rings.length() / 2;
        // a list of rings
        String[] rings_list = new String[n];
        // get rings from string and put into the list
        for (int i = 0; i < n; i++) {
            rings_list[i] = rings.substring(i * 2, i * 2 + 2);
        }
        // num of rod with 3 colors
        int count = 0;
        // use hash table to record colors on rods
        Hashtable<String, String> t = new Hashtable<>();
        // put each ring into hash map. key: rod num, val: colors
        for (String ring : rings_list) {
            String color = ring.substring(0, 1);
            String rod = ring.substring(1, 2);
            if (t.containsKey(rod)) {
                if (!t.get(rod).contains(color)) {
                    t.put(rod, t.get(rod) + color);
                }
            } else {
                t.put(rod, color);
            }
        }
        // count the rods with 3 colors
        for (String rod : t.keySet()) {
            if (t.get(rod).length() == 3) {
                count++;
            }
        }
        return count;
    }
}