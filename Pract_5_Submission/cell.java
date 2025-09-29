import java.util.*;

public class cell {

    int value;
    char dir;

    public static cell[][] LCS(String A, String B) {
        int m = A.length(), n = B.length();
        cell[][] cost = new cell[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                cost[i][j] = new cell();
            }
        }

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0) {
                    cost[i][j].value = 0;
                    cost[i][j].dir = 'H';
                } else if (A.charAt(i - 1) == B.charAt(j - 1)) {
                    cost[i][j].value = cost[i - 1][j - 1].value + 1;
                    cost[i][j].dir = 'D';
                } else if (cost[i - 1][j].value >= cost[i][j - 1].value) {
                    cost[i][j].value = cost[i - 1][j].value;
                    cost[i][j].dir = 'U';
                } else {
                    cost[i][j].value = cost[i][j - 1].value;
                    cost[i][j].dir = 'S';
                }
            }
        }

        return cost;
    }

    public static cell[][] LRS(String A) {
        int m = A.length(), n = A.length();
        cell[][] cost = new cell[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                cost[i][j] = new cell();
            }
        }

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0) {
                    cost[i][j].value = 0;
                    cost[i][j].dir = 'H';
                } else if (A.charAt(i - 1) == A.charAt(j - 1) && i != j) {
                    cost[i][j].value = cost[i - 1][j - 1].value + 1;
                    cost[i][j].dir = 'D';
                } else if (cost[i - 1][j].value >= cost[i][j - 1].value) {
                    cost[i][j].value = cost[i - 1][j].value;
                    cost[i][j].dir = 'U';
                } else {
                    cost[i][j].value = cost[i][j - 1].value;
                    cost[i][j].dir = 'S';
                }
            }
        }

        return cost;
    }

    public static void print(String A, int i, int j, cell[][] cost) {
        if (i == 0 || j == 0)
            return;

        if (cost[i][j].dir == 'D') {
            print(A, i - 1, j - 1, cost);
            System.out.print(A.charAt(i - 1));
        } else if (cost[i][j].dir == 'U') {
            print(A, i - 1, j, cost);
        } else {
            print(A, i, j - 1, cost);
        }
    }

    public static void main(String[] args) {
        String X = "AGCCCTAAGGGCTACCTAGCTT";
        String Y = "GACAGCCTACAAGCGTTAGCTTG";

        cell[][] costLCS = LCS(X, Y);

        System.out.print("The longest common sequence : ");
        print(X, X.length(), Y.length(), costLCS);
        System.out.println();
        System.out.println("The length of longest common subsequence : " + costLCS[X.length()][Y.length()].value);

        System.out.println("\n------------------------------------\n");

        String Z = "AABCBDC";

        cell[][] costLRS = LRS(Z);

        System.out.print("The longest repetitive sequence : ");
        print(Z, Z.length(), Z.length(), costLRS);
        System.out.println();
        System.out.println("The length of longest repetitive subsequence : " + costLRS[Z.length()][Z.length()].value);
    }
}
