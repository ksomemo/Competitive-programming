import time
import pandas as pd
import requests

# 2018-05-15現在(取得できるデータはABC/ARCでCD問題統合後)
MAX_PAGE = 2
headers = {'User-agent': 'Mozilla/5.0'}
df_list = []
categories = {
    4: "ARC",
    5: "ABC",
}
for category in categories.keys():
    for page in range(1, MAX_PAGE+1):
        domain = "beta.atcoder.jp"
        action = "contests/archive"
        params = "category={category}&keyword=&page={page}".format(
            category=category, page=page
        )
        url = "https://{domain}/{action}/?{params}".format(
            domain=domain, action=action, params=params
        )
        print("url:", url)
        try:
            res = requests.get(url, headers)
            tables = pd.read_html(res.text, header=0)
            if len(tables) == 0:
                break
            df_list.append(tables[0])
            time.sleep(2)
        except Exception as e:
            print(e)
            #import sys
            # sys.exit(0)
            break

df = pd.concat(df_list)
df.columns = ["start_time", "contest_name", "duration", "rated_range"]
contest = (
    df.contest_name
    .str.replace("AtCoder |Contest ", "")
    .str.split(" ", expand=True)
)
df = df.drop(["contest_name", "duration", "rated_range"], axis=1)
df["contest_type"] = contest.iloc[:, 0].map({
    "Beginner": "abc",
    "Regular": "arc",
})
df["contest_num"] = contest.iloc[:, 1]
df = df.loc[df["contest_type"].notnull()]
nums = df.pivot(
    "start_time", "contest_type", "contest_num"
).reset_index(drop=True).dropna().astype(int)

with open("abc2arc_arc2abc.js", "w") as f:
    f.write("const abc2arc = ")
    nums[nums.abc.notnull()].set_index("abc").to_json(f)
    f.write(";\n")

    f.write("const arc2abc = ")
    nums[nums.arc.notnull()].set_index("arc").to_json(f)
    f.write(";\n")
