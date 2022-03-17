#-*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import pandas as pd
import mechanicalsoup
import time
import logging
import selenium as sl

def main():
    ##########
    #mainの処理
    ##########
    browser = mechanicalsoup.StatefulBrowser()
    logging.info("Let's Go...")

    username = "idm-japan" #あなたのユーザー名を入れてください
    password = "Idmjapan75900805" #あなたのパスワードを入れてください

        #ログインページを開く
    browser.open("https://idm-japan.sakura.ne.jp/ems/")
    time.sleep(1)

    browser.select_form()

    browser["username-121"] = username
    browser["user_password-121"] = password

    logging.info("Signing in...")
    browser.submit_selected()
    time.sleep(1)

    browser.open("https://idm-japan.sakura.ne.jp/ems/staffmonthly/?setdatestaffmonth=2022/03/01&setstaffid=3")
    time.sleep(1)

    top = browser.get_current_page().select('h1')
    print(top) #[ダッシュボード, リンクの挿入/編集]
    #print(top.text)はエラーになります。
    for wp in browser.get_current_page().select('.welcome-panel-content h2'):
        print(wp.text)

    #################
    #mainの処理おわり
    #################

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()


st.title('Streamlit 超入門')

st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# dfg = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

dfga = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

# st.write(df)

# st.dataframe(df, width=100, height=100)

# st.dataframe(df.style.highlight_max(axis=0))

# st.table(df.style.highlight_max(axis=0))

# st.line_chart(dfg)

# st.area_chart(dfg)

# st.bar_chart(dfg)

st.map(dfga)

"""

# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

