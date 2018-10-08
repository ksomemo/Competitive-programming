# AtCoder Regular Contest

## 過去のARC/ABC問題の難易度推定
推定についての記事と推定結果のURL

- <https://topcoder.g.hatena.ne.jp/tomerun/20161201/1480518557>
- <https://tomerun.github.io/atcoder_statistics/estimated_scores.html>

下記のJavaScriptは
ABC-001_040,ARC-001_057の点数推定値のテーブルをB問題に限定するため
(ABC-AとB,ARC-Aは解き終わった,Bの難易度にばらつきがある)

```js
document.querySelectorAll("#main > tbody > tr:not(:nth-child(4n-2)").forEach((el, idx) => {
  el.remove();
});
document.querySelectorAll("#main > tbody > tr").forEach((el, idx) => {
  var a = el.querySelector("td:nth-child(3) > a");
  var contest = a.href.split("//")[1].split(".")[0];
  el.querySelector("td").innerHTML = contest;
});
```
