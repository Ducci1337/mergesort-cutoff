import java.util.Random;

public class DataGenerator {

    private static final Random rand = new Random(42);

    public static Integer[] generate(String type, int n) {
        switch (type) {
            case "random":        return random(n);
            case "sorted":        return sorted(n);
            case "reverse":       return reverse(n);
            case "nearly_sorted": return nearlySorted(n);
            default: throw new IllegalArgumentException("Unknown type: " + type);
        }
    }

    // mảng ngẫu nhiên
    private static Integer[] random(int n) {
        Integer[] a = new Integer[n];
        for (int i = 0; i < n; i++)
            a[i] = rand.nextInt(n * 10);
        return a;
    }

    // mảng đã sắp xếp tăng dần
    private static Integer[] sorted(int n) {
        Integer[] a = new Integer[n];
        for (int i = 0; i < n; i++)
            a[i] = i;
        return a;
    }

    // mảng đã sắp xếp ngược (giảm dần)
    private static Integer[] reverse(int n) {
        Integer[] a = new Integer[n];
        for (int i = 0; i < n; i++)
            a[i] = n - i;
        return a;
    }

    // mảng gần như đã sắp xếp (đảo ngẫu nhiên 1% cặp)
    private static Integer[] nearlySorted(int n) {
        Integer[] a = sorted(n);
        int swaps = Math.max(1, n / 100);
        for (int i = 0; i < swaps; i++) {
            int x = rand.nextInt(n);
            int y = rand.nextInt(n);
            Integer tmp = a[x];
            a[x] = a[y];
            a[y] = tmp;
        }
        return a;
    }
}
