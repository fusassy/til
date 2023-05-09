---
title: 【Aidemy成果物】ウマ娘のスペシャルウィークを判別するアプリを作成しました
tags: aidemy
author: fusassy
slide: false
---

# 1. アプリの作成背景

自分は元々システムエンジニアとして受託開発現場で業務システムを作成しておりました。

日々の業務を続けている中、縁あって社外の研究活動に参加することになり、クラウド AI を利用したチャットボットを製作することになりました。機械学習に関する知識は[G 検定](https://www.jdla.org/certificate/general/)の受験で概要的な知識はあったものの、実際の開発となると手も足も出ず、自身の技術知識の無さに反省する毎日でした。今後も、エンジニアとして生きていくうえでは、機械学習は避けて通れない技術であると確信しておりましたので、Aidemy で基礎から勉強してみようと思いました。

# 2. 成果物の概要

ウマ娘に登場するキャラクターである、「スペシャルウィーク」かどうかを判別する WEB アプリケーションを、最終成果物として作成しました。Web ブラウザをインターフェイスとしてアニメキャラクターの写真を投稿すると、その写真が「スペシャルウィーク」か、そうでないかを文字として出力します。

# 3. 製作環境

- PowerDirector v19
- Google Colaboratory
- python 3.8.8
- anaconda 2021.05
- tensorflow 2.6.0

# 4. 画像収集

**実行環境**：Google Colaboratory

ウマ娘のスペシャルウィークの顔写真を集めるため、PowerDirector を利用して Youtube から動画を取得し、各場面における静止画を収集しました。また、学習の側面も兼ねて、Bing クローラーより検索した画像を数枚程度含めております。下記に使用したコードを記載します。

```python
!pip install icrawler
from icrawler.builtin import BingImageCrawler
import glob

# 検索リストの生成
search_words = ["スペシャルウィーク　ウマ娘"]     # カンマ区切りで複数設定可能
dir_names = ["spe_img"]     # カンマ区切りで複数設定可能

for search_word,dir_name in zip(search_words,dir_names):
  # Bing用クローラーの生成
  bing_crawler = BingImageCrawler(
      downloader_threads=4,          # ダウンローダーのスレッド数
      storage={'root_dir': "/content/drive/MyDrive/"+dir_name}) # ダウンロード先のディレクトリ名

  # クロール（キーワード検索による画像収集）の実行
  bing_crawler.crawl(
      keyword=search_word,   # 検索キーワード（日本語もOK）
      max_num=10)                    # ダウンロードする画像の最大枚数
```

# 5. 画像加工

**実行環境**：Google Colaboratory

本項以降で使用するライブラリをインポートしています。

```python
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense, Dropout, Flatten, Input
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras import optimizers
```

Youtube と bing クローラーにて収集した「スペシャルウィーク」の画像（img_spe）と、「スペシャルウィーク以外」として女性の画像（img_female）を、モデルへ学習させるため一律でリサイズしています。

```python
# 収集した画像が格納されているパスを取得
path_female = os.listdir('/content/6100_gender_recognition_data/female')
path_spe_img = os.listdir('/content/SpeChan')
path_spe_bing = os.listdir('/content/drive/MyDrive/spe_img')
path_spe = path_spe_img + path_spe_bing

img_female = []
img_spe = []

# 画像をリサイズし、「img_female」リストへ追加（133枚）
for i in range(len(path_spe)):
    img = cv2.imread('./6100_gender_recognition_data/female/' + path_female[i])
    img = cv2.resize(img, (50,50))
    img_female.append(img)

# 画像をリサイズし、「img_spe」リストへ追加（10枚）
for i in range(len(path_spe_img)):
    img = cv2.imread('./SpeChan/' + path_spe_img[i])
    # print(img)
    img = cv2.resize(img, (50,50))
    img_spe.append(img)

# 画像をリサイズし、「img_spe」リストへ追加（123枚）※「img_spa」合計133枚
for i in range(len(path_spe_bing)):
    img = cv2.imread('./drive/MyDrive/spe_img/' + path_spe_bing[i])
    # print(img)
    img = cv2.resize(img, (50,50))
    img_spe.append(img)
```

モデルが判別できるよう、正解ラベル「0」に「スペシャルウィーク」を、正解ラベル「1」に「スペシャルウィーク以外」に設定しています。画像とラベルにつきランダムに並び変えた後、訓練データ（80%）とテストデータ（20%）に分割しています。なお、ラベルについては one-hot ベクトル形式に変換しています。

```python
# クラス「0」→「スペシャルウィーク」、「1」→「female」
X = np.array(img_spe + img_female)
y = np.array([0]*len(img_spe) + [1]*len(img_female))

# Xとyの配列をランダムに並び変える
rand_index = np.random.permutation(np.arange(len(X)))
X = X[rand_index]
y = y[rand_index]

# データの分割
X_train = X[:int(len(X)*0.8)]
y_train = y[:int(len(y)*0.8)]
X_test = X[int(len(X)*0.8):]
y_test = y[int(len(y)*0.8):]

# モデルの予測のため、one-hotベクトル形式に変換
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
```

# 6. モデルの作成・学習

**実行環境**：Google Colaboratory

今回作成するモデルでは、出力層（全結合層）は変更した上で、VGG16※の転移学習を活用しています。VGG16 で抽出した特徴量については 19 層までに固定しています。学習処理について指定した後、一度サマリを出力しています。

※TensorFlow では、ImageNet（120 万枚，1000 クラスからなる巨大な画像のデータセット）で学習した画像分類モデルとその重みをダウンロードし使用できます。VGG16 は公開されているモデルの一つです。VGG16 は、小さい畳み込みを 2〜4 回連続で行った後にプーリングしており、畳み込み 13 層（重みがある層）と全結合層 3 層の計 16 層のニューラルネットワークになっています。

```python
# vgg16の転移学習
input_tensor = Input(shape=(50, 50, 3))
vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)

top_model = Sequential()
top_model.add(Flatten(input_shape=vgg16.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dense(2, activation='softmax'))

model = Model(inputs=vgg16.input, outputs=top_model(vgg16.output))

model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])

for layer in model.layers[:19]:
    layer.trainable = False

model.summary()
```

モデルの学習を開始します。

```python
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=32, epochs=5)
```

# 7. 精度評価・予測

**実行環境**：Google Colaboratory

上記で作成したモデルについて、精度の評価、予測値の二乗誤差を出力しました。また、画像を受け取って判定可能かどうかも検証しました。

```python
# 画像を一枚受け取り、「スペシャルウィーク」かどうかを判定して返す関数
def pred_spe(img):

    img = cv2.resize(img, (50, 50))
    pred = np.argmax(model.predict(np.array([img])))
    if pred == 0:
        return 'スペシャルウィーク'
    else:
        return 'スペシャルウィーク以外'

# 精度の評価
scores = model.evaluate(X_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

#予測値を出力し二乗誤差を算出
y_pred = model.predict(X_test)
mse= mean_squared_error(y_test, y_pred)
print("REG RMSE : %.2f" % (mse** 0.5))

# pred_spe関数に顔写真を渡して予測
for i in range(5):
    img = cv2.imread('./SpeChan/' + path_spe_img[i])
    b,g,r = cv2.split(img)
    img = cv2.merge([r,g,b])
    plt.imshow(img)
    plt.show()
    print(pred_spe(img))
```

著作権の関係で、出力した画像については搭載することはできませんが、「スペシャルウィーク」かどうかは判定できました。精度の出力結果は以下の通りです。

```python
Test loss: 0.16258060932159424
Test accuracy: 0.9814814925193787
REG RMSE : 0.14
```

作成したモデルに関して、epochs 値を増やして精度の検証も実施しました。epochs=5 の周辺で収束しているので、epochs 値は適切であると判断しました。

```python
loss=history.history['loss']
val_loss=history.history['val_loss']
epochs=len(loss)

plt.plot(range(epochs), loss, marker = '.', label = 'loss')
plt.plot(range(epochs), val_loss, marker = '.', label = 'val_loss')
plt.legend(loc = 'best')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
```

**出力結果**
![ブログ画像_epochs検証.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/4ac32fc4-dc42-aa6b-918f-137af39d9cfa.png)
最後に、作成したモデルを重みファイル（h5）として保存しました。

```python
#モデルの保存
from google.colab import files

#resultsディレクトリを作成
result_dir = 'results'
if not os.path.exists(result_dir):
    os.mkdir(result_dir)

# 重みを保存
model.save(os.path.join(result_dir, 'model.h5'))

files.download( '/content/results/model.h5' )
```

次に、フレームワークである Flask を利用し、WEB アプリケーションを作成しました。

# 8. WEB アプリケーションの作成

サーバーサイド側は Flask を利用して実装しています。

```python
import os
from flask import Flask, request, redirect, render_template, flash
from werkzeug.utils import secure_filename
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing import image

import numpy as np


classes = ["スペシャルウィーク","スペシャルウィーク以外"]
image_size = 50

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

model = load_model('./model.h5')#学習済みモデルをロード


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            filepath = os.path.join(UPLOAD_FOLDER, filename)

            #受け取った画像を読み込み、np形式に変換
            img = image.load_img(filepath, target_size=(image_size,image_size))
            img = image.img_to_array(img)
            data = np.array([img])
            #変換したデータをモデルに渡して予測する
            result = model.predict(data)[0]
            predicted = result.argmax()
            pred_answer = "これは " + classes[predicted] + " です"

            return render_template("index.html",answer=pred_answer)

    return render_template("index.html",answer="")
if __name__ == "__main__":
    # app.run()
    port = int(os.environ.get('PORT', 8080))
    app.run(host ='0.0.0.0',port = port)
```

フロントエンド側のコード（HTML/CSS）は以下の通りです。

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Special Week Classifier</title>
    <link rel="stylesheet" href="./static/stylesheet.css" />
  </head>
  <body>
    <header>
      <a class="header-logo" href="#">Special Week Classifier</a>
    </header>

    <div class="main">
      <h2>
        AIが送信された画像を識別し、「スペシャルウィーク」かどうかを判別します。<br />※スペシャルウィークはウマ娘に登場するキャラクターです。
      </h2>
      <p><b>以下に、画像を送信してください</b></p>
      <form method="POST" enctype="multipart/form-data">
        <input class="file_choose" type="file" name="file" />
        <input class="btn" value="画像送信" type="submit" />
      </form>
      <div class="answer">{{answer}}</div>
    </div>

    <footer>
      <img class="footer_img" src="./static/uma_black.jpg" alt="Aidemy" />
      <img class="footer_img" src="./static/uma_white.jpg" alt="Aidemy" />
      <img class="footer_img" src="./static/uma_black.jpg" alt="Aidemy" />
      <small>&copy; 2021 Aidemy, inc.</small>
    </footer>
  </body>
</html>
```

```css
header {
  background-color: hsl(315, 69%, 54%);
  height: 60px;
  margin: -8px;
  display: flex;
  justify-content: space-between;
}

.header-logo {
  color: #fff;
  font-size: 25px;
  margin: 15px 25px;
}

.main {
  height: 370px;
}

h2 {
  color: #444444;
  margin: 90px 0px;
  text-align: center;
}

p {
  color: #444444;
  margin: 70px 0px 30px 0px;
  text-align: center;
}

.answer {
  color: #444444;
  margin: 70px 0px 30px 0px;
  text-align: center;
}

form {
  text-align: center;
}

footer {
  background-color: #f7f7f7;
  height: 110px;
  margin: -8px;
  position: relative;
}

.footer_img {
  height: 25px;
  margin: 15px 25px;
  width: 50px;
  height: auto;
}

small {
  margin: 15px 25px;
  position: absolute;
  left: 0;
  bottom: 0;
}
```

各種コード、設定ファイルとモデルを併せて、heroku にデプロイしました。以下が実際に製作した WEB アプリケーションです。画像を送信すると「スペシャルウィーク」か「スペシャルウィーク以外」かを判定して文字で返します。
![ブログ画像_WEBアプリケーション.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/b7628cfc-53b1-13d1-68ff-8fdabc88b4b9.png)

# 9. 考察・振り返り

新たにウマ娘の画像を集め、当 WEB アプリケーション使用してみて、特に以下 3 点に関連する画像について誤判定が多い印象を持ちました。

- キャラクター自体が遠くに配置されている画像
- ウマ娘の特徴である、ウマ耳が切れている画像
- ウマ娘の特徴である、前髪に白いメッシュのあるウマ娘の画像

「スペシャルウィーク以外」として利用した画像が、ヒトの女性だったことが大きな要因の一つと考えています。実際、ヒトの画像で検証すると、「スペシャルウィーク以外」として判定されています。スペシャルウィーク以外のキャラクター（例：トーカイテイオー、オグリキャップ等）を学習データとして含めれば、判定精度も改善されると考えています。また、ウマ娘に登場するキャラクター間での誤判定（他キャラが「スペシャルウィーク」として判定される現象）は、キャラクター分類数が増えると解消される可能性があると考えています。

今回の最終課題を通して、Aidemy で学習した内容を振り返りつつ、カウンセリングも存分に活用しチューターの方々に密なご指導をいただきながら、WEB アプリケーションを製作しました。モデル製作やチューニング作業はもちろんながら、モデル作成のために画像データを用意する作業も大変でした。（Aidemy の講座では mnist 等のデータセットを利用していました。）Aidemy で提供されている講座で学習した内容について、理解がより深まったと感じています。

最後に、製作した WEB アプリケーションについては、heroku にデプロイしておりますので、ご興味があれば見ていただけると幸いです。実際のソースコードについては、Github に公開しています。

**heroku**
https://aidemy-umachan.herokuapp.com/
**Github**
https://github.com/meimenno/aidemy-umachan.git
