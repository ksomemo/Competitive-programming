# beta
## old to beta
参考: <http://ebicochineal.blogspot.jp/2017/09/atcoderbeta.html>

## code
```js
(() => {
    const href = location.href;
    const host = location.host;
    const oldHost = 'atcoder.jp';
    const betaHost = 'beta.atcoder.jp';
    const isBeta = host === betaHost;
    const hostData = host.split('.');

    if (! isBeta && hostData.length === 4 && hostData[1] === "contest") {
        const contestName = hostData[0];
        const betaContest = betaHost + "/contests/" + contestName;
        location.href = href.replace(host, betaContest);
    } else if (! isBeta) {
        location.href = href.replace(host, betaHost);
    }
})();
```
### minify and bookmarklet
using: <https://skalman.github.io/UglifyJS-online/>

```js
javascript:(()=>{const t=location.href,e=location.host,o="beta.atcoder.jp"===e,c=e.split(".");if(o||4!==c.length||"contest"!==c[1])o||(location.href=t.replace(e,"beta.atcoder.jp"));else{const o="beta.atcoder.jp/contests/"+c[0];location.href=t.replace(e,o)}})();
```