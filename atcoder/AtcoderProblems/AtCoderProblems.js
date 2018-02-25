"use strict";

(() => {
    /**
     * https://qiita.com/simiraaaa/items/2e7478d72f365aa48356
     * @param {string} string
     * @return {bool}
     */
    const execCopy = (string) => {
        const temp = document.createElement('div');

        temp.appendChild(document.createElement('pre')).textContent = string;

        const s = temp.style;
        s.position = 'fixed';
        s.left = '-100%';

        document.body.appendChild(temp);
        document.getSelection().selectAllChildren(temp);

        const result = document.execCommand('copy');

        document.body.removeChild(temp);

        return result;
    }

    /**
     * 2018-02-25 時点htmlから作成
     * @return {string}
     */
    const makeCSV = () => {
        const records = document.querySelectorAll(`
            #root > div > div > div > div
            > div.react-bs-table-container
            > div.react-bs-table.react-bs-table-bordered
            > div.react-bs-container-body > table > tbody tr
        `);

        const baseURL = "https://beta.atcoder.jp"
        const contestPrefix = baseURL + "/contests/"
        const header = [
            "date", "contestName", "rank", "result", "problemTitle", "problemURL", "submissionURL"
        ];
        let data = header.join(",") + "\n";

        // NodeListにはmapがない
        records.forEach(r => {
            const date = r.querySelector("td:nth-child(1) > div").textContent;
            const a = r.querySelector("td:nth-child(2) > a");
            const problemURL = a.href;
            const contestName = problemURL.replace(contestPrefix, "").split("/")[0]
            const problemTitle = a.textContent;
            const rank = problemTitle[0]
            const result = r.querySelector("td:nth-child(3) > h5 > span").textContent;
            const submissionURL = r.querySelector("td:nth-child(4) > a").href;

            const record = [date, contestName, rank, result, problemTitle, problemURL, submissionURL]
            data += record.join(",") + "\n";
        });
        return data;
    };

    const csv = makeCSV();
    if (!execCopy(csv)) {
        alert("fail copying");
    }
})();