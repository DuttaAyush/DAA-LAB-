import java.util.Scanner;

public class OBST {

    public static double OBST(int[] keys, double[] p, double[] q, int n) {
        double[][] e = new double[n + 1][n + 1];
        double[][] w = new double[n + 1][n + 1];
        int[][] root = new int[n][n];

        for (int i = 0; i <= n; i++) {
            e[i][i] = q[i];
            w[i][i] = q[i];
        }

        for (int l = 1; l <= n; l++) {
            for (int i = 0; i <= n - l; i++) {
                int j = i + l; 
                e[i][j] = Double.MAX_VALUE;
                w[i][j] = w[i][j - 1] + p[j - 1] + q[j];

                for (int r = i; r < j; r++) {
                    double cost = e[i][r] + e[r + 1][j] + w[i][j];
                    if (cost < e[i][j]) {
                        e[i][j] = cost;
                        root[i][j - 1] = r; 
                    }
                }
            }
        }

        return e[0][n]; 
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of keys: ");
        int n = sc.nextInt();

        int[] keys = new int[n];
        System.out.print("Enter keys: ");
        for (int i = 0; i < n; i++) {
            keys[i] = sc.nextInt();
        }

        double[] p = new double[n];
        System.out.print("Enter p[i] : ");
        for (int i = 0; i < n; i++) {
            p[i] = sc.nextDouble();
        }

        double[] q = new double[n + 1];
        System.out.print("Enter q[i] : ");
        for (int i = 0; i <= n; i++) {
            q[i] = sc.nextDouble();
        }

        double minCost = OBST(keys, p, q, n);
        System.out.printf("OBST Cost: %.4f\n", minCost);

        sc.close();
    }
}