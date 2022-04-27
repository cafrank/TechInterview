import java.util.Arrays;
import java.util.List;

public class Grab {
   
    
    int sumListElements() {
        List<Integer> integers = Arrays.asList(1, 2, 3, 4, 5);
        return integers.stream().reduce(0, Integer::sum);
    }
}
