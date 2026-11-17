import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class SortBenchmark {

    static final int RUNS = 10;
    static final int WARMUP = 2;       // bỏ qua 2 lần đầu để JVM ổn định

    static final int[] CUTOFFS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
    static final int[] SIZES   = {1000, 5000, 10000, 50000, 100000, 500000, 1000000};
    static final String[] TYPES = {"random", "sorted", "reverse", "nearly_sorted"};

    public static void main(String[] args) throws IOException {
        PrintWriter pw = new PrintWriter(new FileWriter("results/raw_results.csv"));
        pw.println("cutoff,array_type,array_size,run,time_ms");

        for (int cutoff : CUTOFFS) {
            MergeSort.setCutoff(cutoff);
            System.out.println("Testing CUTOFF = " + cutoff + "...");

            for (String type : TYPES) {
                for (int n : SIZES) {
                    // warmup
                    for (int w = 0; w < WARMUP; w++) {
                        Integer[] arr = DataGenerator.generate(type, n);
                        MergeSort.sort(arr);
                    }

                    // actual runs
                    for (int run = 1; run <= RUNS; run++) {
                        Integer[] arr = DataGenerator.generate(type, n);
                        long start = System.nanoTime();
                        MergeSort.sort(arr);
                        long end = System.nanoTime();
                        double ms = (end - start) / 1_000_000.0;
                        pw.printf("%d,%s,%d,%d,%.4f%n", cutoff, type, n, run, ms);
                    }
                }
            }
        }

        pw.close();
        System.out.println("Done! Results saved to results/raw_results.csv");
    }
}
