import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time#プログレスバー

st.title('Streamlit 超入門')#タイトル入力


#プログレスバーの表示
st.write('プログレスバー')
'Start!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)#プログレスバー表示
    time.sleep(0.1)#何秒刻みにするかの設定

'Done!'

#画像の表示
st.write('Display Image')

#チェックボックスを使ってインタラクティブな表示
if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='test image', use_column_width=True)

#セレクトボックスを使って任意の数字を選ばせる
option = st.selectbox(
    '好きな数字を選択',
    list(range(1, 11))
)
'選択されたのは ', option, 'です。'

#スライダーを使って入力 サイドバーへの表示
#condition = st.sidebar.slider('今の調子は', 0, 100, 50)

#テキスト入力　サイドバーへの表示
#text = st.sidebar.text_input('あなたの趣味を入力')

#'コンディション：', condition
#'あなたの趣味は ', text, 'です'


#カラムわけして左右で表示
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

#エキスパンダーの表示
expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容を書く')


#pandasで表の表示　
df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

#st.write(df)
#dataframeの方が表のサイズ(ピクセル単位)など指定できる
#st.dataframe(df, width=500, height=1000)
#列の中で最大の値をハイライトさせる 列axis=0　行axis=1
#st.dataframe(df.style.highlight_max(axis=0), width=500, height=1000)

#静的な表（ソートなどできない）を作りたいときは
st.table(df.style.highlight_max(axis=0))

#表示についての詳しい設定は
#https://docs.streamlit.io/library/api-reference

#マジックコマンドを利用　マークダウンによる表示
#stremlit.textとかstreamlit.markdown
"""
# 章
## 節
### 項

コードを入力
```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

#グラフの表示
#https://docs.streamlit.io/library/api-reference/charts
#ランダム数値でデータ生成
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

#折れ線グラフの作成 線のみと塗りあり
st.line_chart(df)
st.area_chart(df)
#棒グラフ
st.bar_chart(df)

#map 緯度経度マッピング
#新宿付近の座標作成
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
#map上に作成した座標でマッピング
st .map(df)

#画像の表示