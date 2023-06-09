---
title: 【SAP BTP】SAP認定試験の受験体験記、資格試験の情報と解説について
tags: 資格 SAP KYOSO
author: fusassy
slide: false
---

# はじめに

SAP 社のエンタープライズ PaaS 製品である、SAP Business Technology Platform（BTP） でアプリケーション開発をしている@fussasy です。SAP の世界に入って 1 年が経ち、そろそろ SAP 認定試験を受験してみようかと思い、会社からの推奨されている試験領域（区分）で SAP 認定資格試験を受験し資格取得をしました。SAP 製品はエンタープライズ領域において、市場シェアがトップクラスなのですが、SAP 認定試験に関する情報や受験体験記があまりに出回っていないので、記事にまとめておきたいと思います。

# SAP 認定試験について

![SAP公式アイコン（大）.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/2a3fc0d6-ff79-dc65-6870-9d8a0c8ab257.png)

### SAP 製品の世界シェアと SAP 認定試験について

SAP 認定試験は、SAP の製品や技術に関する深い知識と実践的なスキルを持つ専門家を認定する試験です。SAP は世界中でビジネスに必要なソフトウェアを提供しており、SAP 認定試験に合格することで、その製品や技術に関する専門知識を証明することができます。例えば、Gartner 社が発表した 2021 年度の調査によると ERP（Enterprise Resource Planning（企業資源計画））、CRM（Customer Relationship Management（顧客関係管理））、SCM（Supply Chain Management（供給連鎖管理））、HCM（Human Capital Management（人的資本管理））領域の製品の世界シェアランキングでは、以下の通りとなっており、SAP 製品が高いシェアを占めていることが分かります。

**【ERP】SAP：23.6%、Oracle：12.3%、Workday：9.2%、他**
**【CRM】Salesforce：19.5%、SAP：11.0%、Oracle：9.5%、他**
**【SCM】SAP：21.2%、Oracle：16.3%、JDA Software：4.8%、他**
**【HCM】SAP：16.1%、Oracle：13.6%、Workday：12.7%、他**

そのため当試験を受験し、SAP 認定試験の有資格者となることは、自身のエンジニア（またはコンサルタント）として、市場価値の向上へ役に立つことが分かります。SAP 認定技術者は、SAP の製品や技術に関する深い知識と実践的なスキルを持つ専門家として見なされます。

・SAP の製品に関する深い知識を持っている。
・SAP の製品を実際に導入、設定、運用、保守することができる。
・システムの問題を特定し、解決策を提供することができる。
・プロジェクトマネジメントのスキルを持っている。
・ユーザーとコミュニケーションを取りながら、彼らのニーズを理解し、システムを改善することができる。

### SAP 認定試験の受験方法について

SAP 認定試験の受験方法はオンライン試験が主となります。自宅やオフィスなどからインターネット経由で受験することになります。

まず、SAP Certification より、Certification Hub の 1 回分または 6 回分のサブスクリプションを購入します。為替の影響を受けるので、対米ドルで円安の場合、購入費用が高くなります。SAP 認定試験では、同じ試験区分を 3 回までしか受験できないため、2 科目 ×3 回分として提供されています。過去には 1 つのサブスクリプションに対して、2 科目までしか取得できなかったという情報がありますが、最近では仕様が変わったのか、受験可能回数残があれば追加で SAP 認定試験の受験・資格取得をすることができるみたいです。このサブスクリプションの有効期限は購入から 1 年間となります。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/4640557b-d6cd-7151-4ea7-cf1cd9de4ba8.png)

サブスクリプションを購入後、「Subscription へのアクセス」にて画面を移動します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/c4da0eb8-312d-acef-8b55-ae8cebb7ac43.png)

画面を遷移した先で、「Access the Certification Hub」を押下します。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/b2211148-4444-cc22-fe6d-7308b7a52042.png)

「My account」の「Edit」タブから、「time zone」を必ず「Asia/Tokyo」にします。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/aa9b255a-3825-c16e-5a78-0bc4cb6bf341.png)
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/b5cd2e15-e19e-a9aa-d6d0-e9276bec5fed.png)
次に、「Questionmark Secure browser（ https://support.questionmark.com/content/get-questionmark-secure ）」をインストールしましょう。インストールが完了したら、同ページにてサンプルブラウザを立ち上げることができるので、テストします。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/dfdf2549-89a7-0097-f005-f478b9070260.png)
後は、「Exam Dashborad」のタブから、「Online Exam Subscriptions」の「Schedule an exam」で試験の予約に移っていきます。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/bd650f24-715a-7e09-c7d8-f58f1341ca9c.png)
この試験区分の一覧表より、自身が受験したい試験科目を選択し、DatePicker アイコンを押下すると、「Schedule Appointment」のサブ画面が開き、試験日時を選択することができます。「Select Timezone」を「Asia/Tokyo」に設定することで、自動的に UTC + 9:00 されるようになります。（JST 時刻になる）
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/28915444-b5f3-2139-348a-7fd326b127d6.png)

試験スケジュールの予約ができれば、登録メールアドレスに予約完了のメールが届きます。このメールには、当日の注意事項が詳しく書かれていますので、よく読んでおきましょう。ちなみに一度、予約した試験スケジュールは、直前でない限りは何度でも取り消すことができます。キャンセルした場合でも、サブスクリプションの受験可能回数が減ることはありません。

### SAP 認定試験の学習方法について

一般的に、SAP 認定試験の勉強方法としては、以下のような方法があります。

・SAP の公式トレーニングを受講する
・SAP Learning Hub に登録して、学習資料や模擬試験を受ける
https://training.sap.com/learninghub
・SAP システムを使用して、実際に操作しながら学習する
・インターネット上にあるオンライン学習サイトや参考書を活用する
・受験対策のための模擬試験を受ける

個人的に、SAP 認定試験をパスすることだけを目的とする場合、オンライン学習サイトの予想問題にて学習する方が効率的だと思います。
予想問題集で学習する場合は、以下の様な予想問題集を利用すると良いです。
https://www.topexam.jp/
SAP 認定試験の予想問題は、日本語版がないものが多く、ほとんどが英語版だったりします。英語での学習に抵抗がなければ、英語版での学習を強くオススメします。予想問題も、当日の試験問題さえも日本語訳がおかしくて、困惑してしまうからです。予想問題の 6 割～ 7 割程度が似た問題として出題されるため、いったん問題と回答を丸暗記してしまうのが良いです。残りは当日に問題文を読み、回答する必要があります。

# 試験当日の諸注意（予約メール記載の内容）

試験当日までに、忘れずに準備してください。

システムの準備状況を確認する。試験を受けるには、Questionmark Secure ブラウザを使用する必要があります。最新版がコンピュータにインストールされていることを確認してください。最新のバージョンをインストールする前に、古いバージョンをアンインストールする必要がある場合があります。要件については、この記事を参照してください。
身分証明書有効な身分証明書（期限切れのものは不可）を 2 つご提示いただきます。どちらの身分証明書にもお客様のお名前と署名があり、少なくとも 1 つは政府発行の有効な写真付き身分証明書である必要があります。写真付き身分証明書は、試験を受ける前に遠隔監視員によって確認されます。

有効な身分証明書には以下のものがあります。

**a. 署名入りの政府発行のパスポート**
**b. 署名入りの運転免許証（写真付きであること）**
**c. 署名入りの軍用身分証明書**
**d. 銀行/クレジットカード**

試験当日は、以下を忘れないようにしてください。
https://training.sap.com にログインし、Certification をクリックし、Access Certification Hub をクリックします。
Certification Hub で、Exam Appointments をクリックすると、Upcoming Exams の下にあなたの予約が表示されます。
Start Exam（受験開始）リンクは、実際の予約時間から ±15 分の 30 分間有効です。
Start Exam] リンクをクリックします。

以下の標準的なルールに従うことが求められます。

### 標準ルール

試験中、部屋には必ず一人でいてください。
机とワークスペースが確保されていること。
コンピュータは電源に接続されている必要があります。
試験中に携帯電話やスマートウォッチを使用することはできません。
試験中に複数のモニターを使用することはできません。追加で持っている場合は、今すぐプラグを抜いてください。
Web カメラを使用して、部屋と机を 360 度回転させる必要があります。許可されていないものはすべて取り除いてください。
試験中は、適切な照明のもとで、ウェブカメラからはっきりと見える範囲にいる必要があります。
ウェブカメラ、スピーカー、スクリーンシェア、マイクは、試験中常にオンにしておいてください。

### 特別な注意事項

試験中は、話したり、音読したりすることはできません。
試験中に席を離れることはできません。
試験中の行動 1) 携帯電話の使用、2) カメラの電源オフまたはミュート、3) 部屋に別の人物が隠れている、4) 許可されていない資料の使用、5) 試験室を出る、6) 監督官の警告に応じない受験者、7) 代理受験、8) 部屋への入室拒否などの不正行為が認められた場合、試験監督は直ちに試験を終了させるものとします。
試験中は、ヘッドホンの使用が許可されています。

# 個人の体験から、試験当日の諸注意（予約メール記載以外の内容）

・当日、試験で利用する PC に Zoom をインストールしておきましょう。
・Quickmark ブラウザは必ずインストール＋事前稼働の確認をしておきましょう。
・当日の試験画面を進んでいくと、Zoom に繋ぐことになります。試験監督者は英語会話者なので、英語でやり取りする必要があります。
・Zoom で画面共有でブラウザ上に何も開いていない、余計なものがインストールされていないことを見せる必要があります。
・Zoom のビデオで自分の顔と、証明書（運転免許証等）を見せなければいけません。2 種類が必要なので、運転免許証とパスポートの提示で良いと思います。
・Zoom のビデオで部屋の周辺や、机上を見せなければいけません
・指示があれば、試験画面のボタンを押下していき、Quickmark ブラウザを開くことになります
・Quickmark ブラウザ上にて試験を実施します（試験時間は最大 2 時間）
・問題を解いていき、最後に Submit ボタンを押下して、終了。その場で採点されます。（合格点 63 ～ 64%以上）
・試験監督者はよく席を立ちます。終わったら画面クローズして Zoom チャットで呼び出しましょう。

# 試験に合格したら

SAP 認定試験に合格すると、「Exam Dashboard」タブの「Exam Results」の Outcome に「Passed」が付きます。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/0608cb9a-05ab-4e27-a85f-0b9188e3576b.png)
その後、登録メールアドレス宛にバッジの登録依頼が届きますので、メール文の手順に沿って登録していきましょう。Credly にて自身が取得したバッジが登録されています。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/fdc9e1a6-2afc-527d-5567-15b9c797dfea.png)
SAP 認定資格の中には 5 年間の有効期限が明記されているものがありますが、基本的に資格に有効期限はありません。ただ、SAP のシステム・製品とバージョンに依存しているため、そこは留意すべき点となります。

# 試験に関する問い合わせ先

SAP 認定試験に関する問い合わせについては、SAP の E-learning Team（e-learning@sap.com）にメールをする必要があります。
本文は英語で、記載しなければいけません。

Email Address:
User ID:
Complete Course ID:
Describe the issue:
Full Screenshot:

# さいごに

SAP 認定資格は SAP 製品導入プロジェクトに携わっているエンジニア・コンサルタントにとっては馴染みの深い資格です。SAP 認定資格を取得して終わりではなく、日々アップデートされる SAP 製品の情報をキャッチアップし、実務を通して実際のユーザーに価値を届けることが最大のミッションとなりますので、SAP 認定資格の取得後も日々勉強が続いていくことになります。
私もエンジニア歴はそれなりに長いものの、SAP 製品導入・開発経験はまだまだ学ぶべきことが多いと、日々悩んでいたりもしますので、実務で身に着ける知識はもちろん、SAP 社から提供される情報は能動的に得るようにしていきたいです。
