import java.io.IOException;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

/**
 * Hack To The Future 2018
 *
 * @see https://qiita.com/tsukammo/items/7041a00e429f9f5ac4ae
 * @version open jdk 1.8
 */
public class Main {

    private static final int SEED = 20180217;
    private final Scanner sc = new Scanner(System.in);
    // 制約
    private final static int N = 100, row = 100, col = 100, pnum = 1000;
    // 山の外周に沿って斜め移動
    private static final int dx[] = new int[] { 1, -1, -1, 1 };
    private static final int dy[] = new int[] { 1, 1, -1, -1 };
    // 時間制限 : 6sec / メモリ制限 : 1024MB
    private static final long timeLimit = 5500;
    private final int[][] ans = new int[1000][3];
    private final int[][] map = new int[row][col];
    private final Random rnd;

    public Main() {
        this(SEED);
    }

    public Main(int seed) {
        rnd = new Random(seed);
    }

    public static void main(String[] args) throws IOException {
        new Main().solveChangeSubjectToUpdate();
    }

    /**
     * 変更対象の限定
     * 
     * https://atcoder.jp/contests/future-contest-2018-qual/submissions/2201789
     */
    public void solveChangeSubjectToUpdate() {
        input();
        init();
        simulateChangeSubjectToUpdate();
        outputPositiveH();
    }

    /**
     * スコアの持ち方を変更 abs to se: my -> 9706897948, 間違っている？
     * 
     * https://atcoder.jp/contests/future-contest-2018-qual/submissions/2199659
     */
    public void solveError() {
        input();
        init();
        simulateErrorAbs2Square();
        output();
    }

    /**
     * 焼きなまし法
     * 
     * https://atcoder.jp/contests/future-contest-2018-qual/submissions/2199385
     */
    public void solveSA() {
        input();
        init();
        simulateSimulatedAnnealing();
        output();
    }

    /**
     * 近傍探索範囲の限定
     * 
     * 前回最大スコアのx,y,h の近傍探索 各[-1, 1] に限定
     * 
     * https://atcoder.jp/contests/future-contest-2018-qual/submissions/2199174
     */
    public void solveNeighborhood() {
        input();
        init();
        simulateNeighborhood();
        output();
    }

    /**
     * 高速化 スコア計算（シミュレータ）
     * 
     * スコアを一から全て計算しているため、無駄が多い。変えた部分だけ、差分計算するように改修
     * 
     * https://atcoder.jp/contests/future-contest-2018-qual/submissions/2106800
     */
    public void solveFastSimulator() {
        input();
        init();
        simulateFast();
        output();
    }

    /**
     * 山登り法: 9,943,487,628 -> my: 9,957,631,640
     * 
     * 「ある状態からちょっとだけ変えて、より良くなったら採用する。」
     * 
     * from wiki: 評価関数の極値を探索する探索アルゴリズム。最も代表的な局所探索法として知られている。
     * 最良優先探索は過去の解を管理するが、探索対象を現在の解だけに制限したものである
     * 
     * https://atcoder.jp/contests/future-contest-2018-qual/submissions/2106613
     */
    public void solveHillClimbing() {
        input();
        init();
        simulateHC();
        output();
    }

    /**
     * シミュレーション: 9,769,240,193: my -> 9,766,036,442
     * 
     * ちゃんとシミュレータ作ってスコア計算し、 制限時間いっぱい1,000個のランダムな山を生成して、 一番良かったものを出力
     * https://atcoder.jp/contests/future-contest-2018-qual/submissions/2106523
     */
    public void solveSimulate() {
        input();
        init();
        simulate();
        output();
    }

    /**
     * テストケース作成と同様の方法で乱択 乱択した山を出力する 9,686,819,273点
     * https://atcoder.jp/contests/future-contest-2018-qual/submissions/2106371
     */
    public void solveRand() {
        input();
        init();
        output();
    }

    /**
     * ACを取る 4,625,945,259点 output 0:
     * https://atcoder.jp/contests/future-contest-2018-qual/submissions/2106302
     */
    public void solve0() {
        input();
        init();
        output0();
    }

    private void input() {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                map[j][i] = sc.nextInt();
            }
        }
    }

    private void init() {
        for (int i = 0; i < pnum; i++) {
            int x = rnd.nextInt(100);
            int y = rnd.nextInt(100);
            int h = rnd.nextInt(100) + 1;
            ans[i][0] = x;
            ans[i][1] = y;
            ans[i][2] = h;
        }
    }

    private void output() {
        System.out.println(ans.length);
        for (int i = 0; i < ans.length; i++) {
            System.out.println(ans[i][0] + " " + ans[i][1] + " " + ans[i][2]);
        }
    }

    private void outputPositiveH() {
        System.out.println(ans.length);
        for (int i = 0; i < ans.length; i++) {
            if (ans[i][2] > 0) {
                System.out.println(ans[i][0] + " " + ans[i][1] + " " + ans[i][2]);
            }
        }
    }

    private void output0() {
        System.out.println(0);
    }

    private void simulate() {
        // TLE 対策
        long st = System.currentTimeMillis();
        long et = st + timeLimit;

        // いったん評価
        int bestScore = eval(ans);
        int[][] bestOutput = new int[1000][3];
        for (int i = 0; i < bestOutput.length; i++) {
            bestOutput[i] = Arrays.copyOf(ans[i], ans[i].length);
        }

        while (System.currentTimeMillis() < et) {
            // 乱数生成して評価用データ作成
            int[][] tmpOutput = new int[1000][3];
            for (int i = 0; i < pnum; i++) {
                int x = rnd.nextInt(100);
                int y = rnd.nextInt(100);
                int h = rnd.nextInt(100) + 1;
                tmpOutput[i][0] = x;
                tmpOutput[i][1] = y;
                tmpOutput[i][2] = h;
            }

            // 再度評価して更新
            int tmpScore = eval(tmpOutput);
            if (bestScore > tmpScore) {
                bestOutput = tmpOutput;
                for (int i = 0; i < bestOutput.length; i++) {
                    bestOutput[i] = Arrays.copyOf(tmpOutput[i], tmpOutput[i].length);
                }
            }
        }

        // 反映
        for (int i = 0; i < bestOutput.length; i++) {
            ans[i] = Arrays.copyOf(bestOutput[i], bestOutput[i].length);
        }
    }

    void simulateHC() {
        long st = System.currentTimeMillis();
        long et = st + timeLimit;

        int bestScore = eval(ans);
        int[][] bestOutput = new int[1000][3];
        for (int i = 0; i < bestOutput.length; i++) {
            bestOutput[i] = Arrays.copyOf(ans[i], ans[i].length);
        }
        // ここまで同じ

        int loopCount = 0;
        while (System.currentTimeMillis() < et) {
            loopCount++;
            int[] tmpOutput = new int[3];
            int[] beforeOutput = new int[3];

            // ひとつだけ変えるために選択
            // 復元用にその山の状態を保持
            int n = rnd.nextInt(1000);
            beforeOutput[0] = bestOutput[n][0];
            beforeOutput[1] = bestOutput[n][1];
            beforeOutput[2] = bestOutput[n][2];
            tmpOutput[0] = rnd.nextInt(100);
            tmpOutput[1] = rnd.nextInt(100);
            tmpOutput[2] = rnd.nextInt(100) + 1;
            bestOutput[n] = tmpOutput;

            int tmpScore = eval(bestOutput);
            if (bestScore > tmpScore) {
                bestScore = tmpScore;
            } else {
                // rollback
                bestOutput[n] = beforeOutput;
            }
        }
        System.err.println("loop:" + loopCount);
        for (int i = 0; i < bestOutput.length; i++) {
            ans[i] = Arrays.copyOf(bestOutput[i], bestOutput[i].length);
        }
    }

    /**
     * 焼きなまし法:SA
     * 
     * <pre>
     * 条件を満たす場合はスコアが悪くなる方向にも更新を許す.
     * 山登り法の局所解に陥りやすいという欠点を考慮している
     * 条件設定の仕方や温度管理と呼ばれるパラメータ調整等の要素がある
     * </pre>
     */
    void simulateSimulatedAnnealing() {
        long st = System.currentTimeMillis();
        long et = st + timeLimit;

        int[][] bestOutput = new int[1000][3];
        for (int i = 0; i < bestOutput.length; i++) {
            bestOutput[i] = Arrays.copyOf(ans[i], ans[i].length);
        }

        int[][] diff = makeDiff(bestOutput);
        int bestScore = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                bestScore += Math.abs(diff[i][j]);
            }
        }

        int loopCount = 0;
        long currentTime = System.currentTimeMillis();
        double forceLine; // 許容ライン。時間経過によりラインを厳しくしていく。
        // パラメータ
        double C = timeLimit * 100; // 許容する確率定数。適当に弄る。
        while (currentTime < et) {
            loopCount++;
            int[] tmpOutput = new int[3];
            int[] beforeOutput = new int[3];
            int n = rnd.nextInt(1000);
            beforeOutput[0] = bestOutput[n][0];
            beforeOutput[1] = bestOutput[n][1];
            beforeOutput[2] = bestOutput[n][2];

            // 近傍探索: 3 - 1 = 0 to 2 - 1 = [-1, 1]
            int x = Math.max(0, beforeOutput[0] + rnd.nextInt(3) - 1);
            int y = Math.max(0, beforeOutput[1] + rnd.nextInt(3) - 1);
            int h = Math.max(1, beforeOutput[2] + rnd.nextInt(3) - 1);
            tmpOutput[0] = Math.min(99, x);
            tmpOutput[1] = Math.min(99, y);
            tmpOutput[2] = Math.min(100, h);

            updateDiff(diff, beforeOutput, tmpOutput);
            int tmpScore = 0;
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    tmpScore += Math.abs(diff[i][j]);
                }
            }

            // 時間経過すると forceLine の分子が小さくなる
            // forceLine 全体が小さくなり、nextDouble [0.0, 1.0] より大きくなりにくい
            currentTime = System.currentTimeMillis();
            forceLine = (et - currentTime) / C;
            if (bestScore > tmpScore || forceLine > rnd.nextDouble()) {
                bestScore = tmpScore;
                bestOutput[n] = tmpOutput;
            } else {
                // rollback
                updateDiff(diff, tmpOutput, beforeOutput);
            }
        }

        System.err.println("loop:" + loopCount);
        for (int i = 0; i < bestOutput.length; i++) {
            ans[i] = Arrays.copyOf(bestOutput[i], bestOutput[i].length);
        }
    }

    /**
     * スコアの持ち方を変えてみる(2乗誤差): 9,997,889,498点. my ->
     * 
     * <pre>
     * 今回の問題では、inputとの差がスコアとなっています。これを別の評価とすることで、より繊細な状態遷移を可能にできます。
     * スコアの持ち方のアイディアとして、下記のようなものが浮かびました。
     * 
     * - マス毎の差分の大小に応じてスコアに重みを付ける。 (今回はこれ)
     * - 中央と端とでスコアに重みを付ける。
     *  - 中間のほうが、周りに影響を与えやすい
     *  - 角は影響を与えにくい
     * - 差分のあるマス同士の距離で重みを付ける。
     *  - ?
     * - …etc.
     * </pre>
     */
    void simulateErrorAbs2Square() {
        long st = System.currentTimeMillis();
        long et = st + timeLimit;

        int[][] bestOutput = new int[1000][3];
        for (int i = 0; i < bestOutput.length; i++) {
            bestOutput[i] = Arrays.copyOf(ans[i], ans[i].length);
        }

        int[][] diff = makeDiff(bestOutput);
        int bestScore = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                bestScore += Math.pow(diff[i][j], 2);
            }
        }

        int loopCount = 0;
        long currentTime = System.currentTimeMillis();
        double forceLine; // 許容ライン。時間経過によりラインを厳しくしていく。
        // パラメータ
        double C = timeLimit * 100; // 許容する確率定数。適当に弄る。
        while (currentTime < et) {
            loopCount++;
            int[] tmpOutput = new int[3];
            int[] beforeOutput = new int[3];
            int n = rnd.nextInt(1000);
            beforeOutput[0] = bestOutput[n][0];
            beforeOutput[1] = bestOutput[n][1];
            beforeOutput[2] = bestOutput[n][2];

            // 近傍探索: 3 - 1 = 0 to 2 - 1 = [-1, 1]
            int x = Math.max(0, beforeOutput[0] + rnd.nextInt(3) - 1);
            int y = Math.max(0, beforeOutput[1] + rnd.nextInt(3) - 1);
            int h = Math.max(1, beforeOutput[2] + rnd.nextInt(3) - 1);
            tmpOutput[0] = Math.min(99, x);
            tmpOutput[1] = Math.min(99, y);
            tmpOutput[2] = Math.min(100, h);

            updateDiff(diff, beforeOutput, tmpOutput);
            int tmpScore = 0;
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    tmpScore += Math.pow(diff[i][j], 2);
                }
            }

            // 時間経過すると forceLine の分子が小さくなる
            // forceLine 全体が小さくなり、nextDouble [0.0, 1.0] より大きくなりにくい
            currentTime = System.currentTimeMillis();
            forceLine = (et - currentTime) / C;
            if (bestScore > tmpScore || forceLine > rnd.nextDouble()) {
                bestScore = tmpScore;
                bestOutput[n] = tmpOutput;
            } else {
                // rollback
                updateDiff(diff, tmpOutput, beforeOutput);
            }
        }

        // 本当のスコア
        bestScore = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                bestScore += Math.abs(diff[i][j]);
            }
        }

        System.err.println("loop:" + loopCount + " " + bestScore);
        for (int i = 0; i < bestOutput.length; i++) {
            ans[i] = Arrays.copyOf(bestOutput[i], bestOutput[i].length);
        }
    }

    /**
     * 初めは大きく後半になるにつれ小さく変化させる
     * 
     * 時間経過に応じて、変化対象に選ぶ山を制限するロジックを加えての結果 9,998,129,683点
     * 
     * <pre>
     * 開始直後は差分が大きく、大きな変化が求められる
     * しかし、広範囲移るにつれ差分はどんどん小さくなる
     * 大きな変化ではなく、小さい変化で詰めていく機会が増えていく
     * 後半、変化対象を小さな山に限定されるためスコア計算も軽くなり、試行回数の増加
     * </pre>
     */
    void simulateChangeSubjectToUpdate() {
        long st = System.currentTimeMillis();
        long et = st + timeLimit;

        int[][] bestOutput = new int[1000][3];
        for (int i = 0; i < bestOutput.length; i++) {
            bestOutput[i] = Arrays.copyOf(ans[i], ans[i].length);
        }

        int[][] diff = makeDiff(bestOutput);
        int bestScore = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                bestScore += Math.pow(diff[i][j], 2);
            }
        }

        // 残り時間の事前計算
        long restTime = et - System.currentTimeMillis();
        // 宣言を一回のみにして効率UP?
        int x, y, h;
        int loopCount = 0;
        double forceLine; // 許容ライン。時間経過によりラインを厳しくしていく。
        // パラメータ
        double C = timeLimit * 100; // 許容する確率定数。適当に弄る。
        while (restTime > 0) {
            loopCount++;
            int[] tmpOutput = new int[3];
            int[] beforeOutput = new int[3];

            // 時間に応じて変化対象の高さ限定
            int n = rnd.nextInt(1000);
            long limitHigh = 10 + 110 * (restTime) / timeLimit;
            while (bestOutput[n][2] > limitHigh) {
                n = rnd.nextInt(1000);
            }
            beforeOutput[0] = bestOutput[n][0];
            beforeOutput[1] = bestOutput[n][1];
            beforeOutput[2] = bestOutput[n][2];

            // 近傍探索: 3 - 1 = 0 to 2 - 1 = [-1, 1]
            x = Math.max(0, beforeOutput[0] + rnd.nextInt(3) - 1);
            y = Math.max(0, beforeOutput[1] + rnd.nextInt(3) - 1);
            h = Math.max(1, beforeOutput[2] + rnd.nextInt(3) - 1);
            tmpOutput[0] = Math.min(99, x);
            tmpOutput[1] = Math.min(99, y);
            tmpOutput[2] = Math.min(100, h);

            updateDiff(diff, beforeOutput, tmpOutput);
            int tmpScore = 0;
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    tmpScore += Math.pow(diff[i][j], 2);
                }
            }

            // 時間経過すると forceLine の分子が小さくなる
            // forceLine 全体が小さくなり、nextDouble [0.0, 1.0] より大きくなりにくい
            restTime = et - System.currentTimeMillis();
            forceLine = restTime / C;
            if (bestScore > tmpScore || forceLine > rnd.nextDouble()) {
                bestScore = tmpScore;
                bestOutput[n] = tmpOutput;
            } else {
                // rollback
                updateDiff(diff, tmpOutput, beforeOutput);
            }
        }

        // 本当のスコア
        bestScore = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                bestScore += Math.abs(diff[i][j]);
            }
        }

        System.err.println("loop:" + loopCount + " " + bestScore);
        for (int i = 0; i < bestOutput.length; i++) {
            ans[i] = Arrays.copyOf(bestOutput[i], bestOutput[i].length);
        }
    }

    /**
     * 近傍探索範囲の限定: my -> 9,997,735,564
     * 
     * <pre>
     * 乱択アプローチにおいて、次に取り得る状態「近傍」
     * ある山をひとつ選んでそれを作り直すという動きに対して、山の変化をもっと小さくする
     * 
     * 近傍は、できるだけスコアがよくなる可能性が高いものを選びたい
     * 多くの問題において、
     * 現在の状態から少しだけ変えた状態がスコア更新の可能性が高いことが知られている
     * 近傍の範囲を狭めることで点数の向上が見込める
     *
     * 近傍を少しだけ変えたものに限定、近傍の選択肢を狭めることになるが、期待値の高いものに集中投資すると考える
     * 例：確率1%で10点取れるもの（期待値：0.1）より、確率20%で1点取れるもの（期待値：0.2）を選ぶ。
     * 
     * 山登り法は、必ずスコアが良くなる方向にしか更新されず、局所解に陥りやすいという欠点がある
     * </pre>
     */
    void simulateNeighborhood() {
        long st = System.currentTimeMillis();
        long et = st + timeLimit;

        int[][] bestOutput = new int[1000][3];
        for (int i = 0; i < bestOutput.length; i++) {
            bestOutput[i] = Arrays.copyOf(ans[i], ans[i].length);
        }

        int[][] diff = makeDiff(bestOutput);
        int bestScore = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                bestScore += Math.abs(diff[i][j]);
            }
        }

        int loopCount = 0;
        while (System.currentTimeMillis() < et) {
            loopCount++;
            int[] tmpOutput = new int[3];
            int[] beforeOutput = new int[3];
            int n = rnd.nextInt(1000);
            beforeOutput[0] = bestOutput[n][0];
            beforeOutput[1] = bestOutput[n][1];
            beforeOutput[2] = bestOutput[n][2];

            // 近傍探索: 3 - 1 = 0 to 2 - 1 = [-1, 1]
            int x = Math.max(0, beforeOutput[0] + rnd.nextInt(3) - 1);
            int y = Math.max(0, beforeOutput[1] + rnd.nextInt(3) - 1);
            int h = Math.max(1, beforeOutput[2] + rnd.nextInt(3) - 1);
            tmpOutput[0] = Math.min(99, x);
            tmpOutput[1] = Math.min(99, y);
            tmpOutput[2] = Math.min(100, h);

            updateDiff(diff, beforeOutput, tmpOutput);
            int tmpScore = 0;
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    tmpScore += Math.abs(diff[i][j]);
                }
            }

            if (bestScore > tmpScore) {
                bestScore = tmpScore;
                bestOutput[n] = tmpOutput;
            } else {
                // rollback
                updateDiff(diff, tmpOutput, beforeOutput);
            }
        }

        System.err.println("loop:" + loopCount);
        for (int i = 0; i < bestOutput.length; i++) {
            ans[i] = Arrays.copyOf(bestOutput[i], bestOutput[i].length);
        }
    }

    /**
     * シミュレータを変更部分のみの計算でスコア算出できるようにした
     * 
     * my -> 9,991,126,728
     */
    void simulateFast() {
        long st = System.currentTimeMillis();
        long et = st + timeLimit;

        int[][] bestOutput = new int[1000][3];

        for (int i = 0; i < bestOutput.length; i++) {
            bestOutput[i] = Arrays.copyOf(ans[i], ans[i].length);
        }

        // diff作成
        int[][] diff = makeDiff(bestOutput);
        int bestScore = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                bestScore += Math.abs(diff[i][j]);
            }
        }

        int loopCount = 0;
        while (System.currentTimeMillis() < et) {
            loopCount++;
            int[] tmpOutput = new int[3];
            int[] beforeOutput = new int[3];
            int n = rnd.nextInt(1000);
            beforeOutput[0] = bestOutput[n][0];
            beforeOutput[1] = bestOutput[n][1];
            beforeOutput[2] = bestOutput[n][2];

            tmpOutput[0] = rnd.nextInt(100);
            tmpOutput[1] = rnd.nextInt(100);
            tmpOutput[2] = rnd.nextInt(100) + 1;

            // ランダム選択した状態の山型足し算をdiffから除外
            // 変わりの状態の山型足し算をdiffに適用
            updateDiff(diff, beforeOutput, tmpOutput);
            int tmpScore = 0;
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    tmpScore += Math.abs(diff[i][j]);
                }
            }

            if (bestScore > tmpScore) {
                bestScore = tmpScore;
                bestOutput[n] = tmpOutput;
            } else {
                // rollback
                updateDiff(diff, tmpOutput, beforeOutput);
            }
        }

        System.err.println("loop:" + loopCount);
        for (int i = 0; i < bestOutput.length; i++) {
            ans[i] = Arrays.copyOf(bestOutput[i], bestOutput[i].length);
        }
    }

    /**
     * 山型足し算を実行後、diff配列の作成
     * 
     * 今まではeval の中で処理していた一部と同じで、スコア算出はしていない
     * 
     * @param output
     * @return diff array
     */
    int[][] makeDiff(int[][] output) {
        int[][] ret = new int[row][col];
        int[][] ansMap = new int[row][col];

        for (int i = 0; i < output.length; i++) {
            int x = output[i][0];
            int y = output[i][1];
            int h = output[i][2];
            ansMap[x][y] += h;
            for (int plus = 1; plus < h; plus++) {
                int d = h - plus;
                x = output[i][0];
                y = output[i][1] - d;
                for (int j = 0; j < dx.length; j++) {
                    for (int k = 0; k < d; k++) {
                        x = x + dx[j];
                        y = y + dy[j];
                        if (outMap(x, y)) {
                            continue;
                        }
                        ansMap[x][y] += plus;
                    }
                }
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                ret[i][j] = map[i][j] - ansMap[i][j];
            }
        }
        return ret;
    }

    /**
     * 差分更新（シャローコピーのため）, 山型足し算
     * 
     * @param diff
     * @param before
     * @param after
     */
    void updateDiff(int[][] diff, int[] before, int[] after) {
        // subtract
        // makeDiff = inputMap - ansMap
        // input を基準にしているのでdiff に足すことは元に戻していることになる
        int x = before[0];
        int y = before[1];
        int h = before[2];
        diff[x][y] += h;
        for (int plus = 1; plus < h; plus++) {
            int d = h - plus;
            x = before[0];
            y = before[1] - d;
            for (int j = 0; j < dx.length; j++) {
                for (int k = 0; k < d; k++) {
                    x = x + dx[j];
                    y = y + dy[j];
                    if (outMap(x, y)) {
                        continue;
                    }
                    diff[x][y] += plus;
                }
            }
        }

        // add
        x = after[0];
        y = after[1];
        h = after[2];
        diff[x][y] -= h;
        for (int plus = 1; plus < h; plus++) {
            int d = h - plus;
            x = after[0];
            y = after[1] - d;
            for (int j = 0; j < dx.length; j++) {
                for (int k = 0; k < d; k++) {
                    x = x + dx[j];
                    y = y + dy[j];
                    if (outMap(x, y)) {
                        continue;
                    }
                    diff[x][y] -= plus;
                }
            }
        }
    }

    /**
     * シミュレータ, 山型足し算
     * 
     * @param output
     * @return score
     */
    private int eval(int[][] output) {
        int ret = 0;
        int[][] ansMap = new int[row][col];

        for (int i = 0; i < output.length; i++) {
            int x = output[i][0];
            int y = output[i][1];
            int h = output[i][2];
            ansMap[x][y] += h;
            for (int plus = 1; plus < h; plus++) {
                int d = h - plus;
                x = output[i][0];
                y = output[i][1] - d;
                // 四方
                for (int j = 0; j < dx.length; j++) {
                    // 移動距離
                    for (int k = 0; k < d; k++) {
                        x = x + dx[j];
                        y = y + dy[j];
                        if (outMap(x, y)) {
                            continue;
                        }
                        ansMap[x][y] += plus;
                    }
                }
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                ret += Math.abs(map[i][j] - ansMap[i][j]);
            }
        }

        return ret;
    }

    boolean inMap(int x, int y) {
        boolean inX = 0 <= x && x < row;
        boolean inY = 0 <= y && y < col;
        return inX && inY;
    }

    boolean outMap(int x, int y) {
        return !inMap(x, y);
    }
}
