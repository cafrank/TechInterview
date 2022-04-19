import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * My implementation of CoderPro34.  The idea is to lay out the meeting intervals on a timeline.  
 * Meeting start = +1, meeting end = -1. Walk the timeline from begining to end keeping a running
 * total and the max running total.  
 * Implement timeline with HashMap<Integer, List<Integer>>
 * Key is the time, valuye is a list of meeting starts and/or stops
 */
public class CoderPro34 {

    static class MD extends HashMap<Integer, List<Integer>> {
        public void append(int key, int value) {
            if (!this.containsKey(key)) {
                this.put(key, new LinkedList<Integer> ());
            }
            this.get(key).add(value);
        }

        public int getSum(int key) {
            return (!this.containsKey(key)) ? 0 : this.get(key).stream().reduce(0, Integer::sum);
        }

        public int[] getSortedKeys() {
            int[] arr = this.keySet().stream().mapToInt(Integer::intValue).toArray();
            Arrays.sort(arr);
            return arr;
        }

        public List<Integer>flatValues() {
            return this.values()
                .stream()
                .flatMap(Collection::stream)
                .collect(Collectors.toList());
        }

    };

    // Funny.  No typles or pairs in java.  Use int[]
    public static int meetingRooms(List<int[]> meetings) {
       MD md = new CoderPro34.MD();
        
        for(int[] m: meetings) {
            md.append(m[0], 1);
            md.append(m[1], -1);
        }

        int sum = 0, max = 0;
        for(Integer i: md.getSortedKeys()) {
            sum += md.getSum(i);
            max = sum>max ? sum : max;
        }
        return max;
    }

    public static void main(String[] args) {
        List<int[]> meetings = Arrays.asList(new int[]{1,2}, new int[]{3,4});
        meetings = Arrays.asList(new int[]{10,40}, new int[]{20,30}, new int[]{25,35}, new int[]{38,45}, new int[]{40,50});
        System.out.println(meetingRooms(meetings));
    }
}