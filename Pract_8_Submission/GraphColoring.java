import java.util.*;

public class GraphColoring {

    static int V;

    static boolean isSafe(int v, int[][] graph, int[] color, int c) {
        for (int i = 0; i < V; i++) {
            if (graph[v][i] == 1 && color[i] == c)
                return false;
        }
        return true;
    }

    static boolean solve(int[][] graph, int m, int[] color, int v) {
        if (v == V)
            return true;

        for (int c = 1; c <= m; c++) {
            if (isSafe(v, graph, color, c)) {
                color[v] = c;
                if (solve(graph, m, color, v + 1))
                    return true;
                color[v] = 0;
            }
        }
        return false;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of vertices: ");
        V = sc.nextInt();

        int[][] graph = new int[V][V];
        System.out.println("Enter adjacency matrix:");
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                graph[i][j] = sc.nextInt();

        System.out.print("Enter number of frequencies (colors): ");
        int m = sc.nextInt();

        int[] color = new int[V];

        if (!solve(graph, m, color, 0))
            System.out.println("No valid coloring possible.");
        else {
            System.out.println("\nColor assigned to each cell:");
            for (int i = 0; i < V; i++)
                System.out.println("Cell " + (i+1) + " → Frequency " + color[i]);
        }
    }
}
