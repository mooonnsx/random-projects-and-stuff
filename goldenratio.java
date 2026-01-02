// calculates golden ratio using fibonacci sequence
import java.util.Scanner;
public class goldenratio {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("How many iterations to estimate from?");
        int iterations = input.nextInt();
        long num1 = 1; // long for more accuracy
        long num2 = 1;
        long num3;
        for (int i = 0; i < iterations; i++) {
            num3 = num1;
            num1 += num2; // fibonacci sequence
            num2 = num3;
            System.out.println(num1);
        }
        System.out.println((float)(num1)/(float)(num2)); // calculates ratio (golden ratio - 1.618)
    }
}