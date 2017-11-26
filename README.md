デュエルリンクスのスキル「バランス」のバラツキ調査
===
2017年11月6日のアップデートで、スキル「バランス」の効果が調整され、一定のランダム性が付与されたそうです。ここでは初期手札配布画面のスクリーンショットから自動的にモンスター・魔法・罠の枚数を数えるプログラムを用いて、「バランス」のバラツキ調査を実施します。

# 概要
モンスター10枚・魔法5枚・罠5枚デッキで「バランス」を用いた際の初期手札配布画面でスクリーンショットを撮り「img」フォルダ内に保存します。「img」フォルダ内に配置した全ての画像について、duellinks_balance.pyを実行すると、自動的にモンスター・魔法・罠の枚数を数え、割合を導出します。

# 手法
1. 画像から、手札の1枚ずつの領域を取り出す
1. それぞれの領域内のRGB値の平均を導出し特徴量とする
1. 全てのデータ（特徴量＋各ラベル）からKmeans法でモンスター・魔法・罠に分類する
1. 集計して棒グラフを出力する

# 画像処理のイメージ
https://github.com/upura/duellinks_balance/blob/master/demo_duellinks_balance.ipynb

# スクリーンショット募集
~~データ量が大事なので、同条件でのスクリーンショットを下記フォルダにアップロードいただけると大変ありがたいです。~~
~~https://drive.google.com/drive/folders/1N4kV_Mu0qq--IEJO0EwoLKBk4ygD_r3M?usp=sharing~~
