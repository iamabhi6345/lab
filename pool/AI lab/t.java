import java.util.Arrays;

public class t {
    public boolean isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int[][][] memo = new int[101][101][101]; // Memoization table (adjust size as needed)
        for (int i = 0; i <= 100; i++) {
            for (int j = 0; j <= 100; j++) {
                Arrays.fill(memo[i][j], -1);
            }
        }
        return dfs(sx, sy, fx, fy, t, memo);
    }

    static boolean dfs(int sx, int sy, int fx, int fy, int t, int[][][] memo) {
        if (sx == fx && sy == fy) {
            return true;
        }
        if (sx <= 0 || sy <= 0 || fx <= 0 || fy <= 0 || t <= 0) {
            return false;
        }
        if (memo[sx][sy][t] != -1) {
            return memo[sx][sy][t] == 1;
        }
        boolean result = false;
        for (int i = t - 1; i >= 0; i--) {
            if (dfs(sx + 1, sy, fx, fy, i, memo) || dfs(sx - 1, sy, fx, fy, i, memo) ||
                dfs(sx, sy + 1, fx, fy, i, memo) || dfs(sx, sy - 1, fx, fy, i, memo) ||
                dfs(sx + 1, sy + 1, fx, fy, i, memo) || dfs(sx + 1, sy - 1, fx, fy, i, memo) ||
                dfs(sx - 1, sy + 1, fx, fy, i, memo) || dfs(sx - 1, sy - 1, fx, fy, i, memo)) {
                result = true;
                break;
            }
        }
        memo[sx][sy][t] = result ? 1 : 0;
        return result;
    }

    public static void main(String[] args) {
        t solution = new t();
        int sx = 1, sy = 1, fx = 1, fy = 3, t = 2;
        boolean result = solution.isReachableAtTime(sx, sy, fx, fy, t);
        System.out.println(result); // Output: true
    }
}
