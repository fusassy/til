---
title: 【SAP BTP】Alert Notification ServiceをSlackやメールに通知する設定方法
tags: SAPCP SAPBTP Webhook jsug KYOSO
author: fusassy
slide: false
---

# はじめに：SAP Alert Notification Service for SAP BTP とは

SAP 社のエンタープライズ PaaS 製品である、**SAP Business Technology Platform（BTP）** で業務アプリケーションを開発している@fussasy です。

SAP BTP で提供するサービスの一つである「**Alert Notification Service**」は BTP 開発においては必須です。Alert Notification Service は、リアルタイムに通知や警告を送信するための共通 API を作成・提供するサービスです。これは外部のメールやチャットサービス（Slack 等）へ発信する設定が可能です。主に、Java 等で開発し SAP BTP にデプロイしたアプリケーションを Alert Notification Service に Bind し、何かしらの情報を通知させるという利用の仕方をします。ちなみに、Alert Notification Service は再試行、フォールバックや送信順序についての設定も可能です。

今回は、[Japan SAP Users' Group（JSUG）][JSUG]でのハンズオンで学んだ内容をベースに、メールや Slack での通知設定を整理します。

# Alert Notification の内容を Slack に通知する設定手順

SAP BTP Trial アカウントを利用して Alert Notification Service を Slack やメールに通知する設定手順を整理します。

### ①Alert Notification Service のインスタンスを作成する

trial のサブアカウントに入ります。
![素材画像_1.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/7c8d195c-57f3-6bd5-cf96-9807bc34ef23.png)
SAP BTP コックピッドで Alert Notification Service のインスタンスを作成します。（Instance Name は任意）
![素材画像_2.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/be4a5883-6702-e70d-becb-fd970db31f89.png)
インスタンスを作成しましたら、Manage Instance に移動します。
![素材画像_3.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/417c96c7-67bf-ed07-6b89-4f66b0735368.png)

### ②Alert Notification Service の Manage Instance で Action を作成する

まずは、Action を作成します。ここでは、どういったサービスに配信するのか、配信するアドレス、タイトルや内容等を編集し設定することができます。
**Actions**を選択 → **Create**を選択すると以下の選択画面が表示されます。メール通知設定をする場合は Email、Slack であれば Slack を選択してください。
![素材画像_4.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/10d52842-163d-38e9-7fda-8891d08ddce5.png)
**Next**を押下すると以下の画面に移ります。配信したい先のメールアドレスを入力してください。
![素材画像_5.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/c8fafee1-2a3d-882f-2916-d27b20c2c7e5.png)
Slack の場合、**Next**を押下すると以下の画面に移ります。
![素材画像_6.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/fdcbf723-7a3e-ae17-4647-02afebee0eaf.png)
Slack の App Directory で**Incoming Webhook**で配信したいチャンネルを選択して追加し、Webhook URL を取得してください。これを Slack で設定する URL Address に設定します。
![素材画像_22.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/8235d154-7ffd-c4d1-f03d-4edda0cf2b2d.png)
![素材画像_23.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/9eeea54f-6777-43fa-783a-18282ed31ade.png)
補足ですが、最初の Action Type で Teams 等を選択した場合も、同様に Teams 等において Incoming Webhook で URL を発行して設定すれば大丈夫です。

Action を有効にする場合、メールであれば設定したメールアドレス宛に有効化に関するメールが届きますので、有効化を実施してください。
![素材画像_9.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/02f8576e-2622-6531-e195-a456afd2345c.png)
他に、作成済の Action 一覧から、Action を選択して個別に有効・無効とすることもできます。
![素材画像_7.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/eec35f4a-cd9a-0069-4224-b7396d19e173.png)
![素材画像_8.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/667d1bef-e20b-ef45-7cb7-521b72cb27e1.png)

### ③Alert Notification Service の Manage Instance で Condition を作成する

次に、Condtion を作成します。条件に一致すれば情報が配信されるようになります。**Conditions**を選択 → **Create**を選択すると以下の画面が表示されます。
![素材画像_10.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/d80a719e-6b11-ea3f-2e64-1bf88f3fff7a.png)

今回は、ユーザーが Cloud Foundry スペースに追加されるか、スペースに既に存在するユーザーに、開発者ロールが割り当てられたときをトリガーとするため、Condtion を「eventType」「Is Equal To」「audit.user.space_developer_add」とします。他に、ユーザー削除された場合等、パターン別による条件の追加方法は Help Portal (Documentation)の SAP Alert Notification for SAP BTP で、**Built-In Event** → **User Lifecycle Events**の一覧から確認してください。

### ④Alert Notification Service の Manage Instance で Subscription を作成する

最後に、Subscription を作成します。これに先ほどの Action と Condtion を繋げます。**Subscriptions**を選択 → **Create**を選択すると以下の画面が表示されます。
![素材画像_11.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/4ea7ceb5-4c05-d65a-e145-34521d3469ad.png)
必須項目を入力し、**Create**を押下すると以下の画面に移ります。
![素材画像_12.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/6648e008-8eb3-0c1b-251f-3810a5eb1a42.png)
作成済の Condition を選択し、**Assign**を押下すると以下の画面に移ります。
![素材画像_13.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/f91227b5-5ed5-31fa-f382-fa20d658a159.png)
作成済の Action を選択し、**Assign**を押下して設定完了です。

### ⑤Alert Notification Service の Manage Instance でイベントを発火させてみる

作成した Subscription が機能するかどうか、イベント発火テストをしてみましょう。
![素材画像_14.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/c2993921-67c0-9cc9-b36b-03671c71d057.png)
作成済 Subscription を選択し、**Send Test Event**を押下します。
![素材画像_15.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/e16cef38-f6be-3ada-4cb2-cdc1bb281d83.png)
"eventType"を"sampleType"から"audit.user.space_developer_add"に修正して、**Send**を押下します。
![素材画像_16.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/20a623d8-fafb-0d72-2064-cace601a1d56.png)
すると、以下のようなメールが飛んでいることが分かります。
![素材画像_20.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/cb0caed8-b5b1-7f42-9f2c-0a892182698a.png)
Slack に配信すると以下の様になります。
![素材画像_17.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/55654d16-a268-6eaa-1dcc-eb8a1cc4f7b1.png)

イベント発火テストがうまくいけば、実際の BTP コックピッド上の行動でイベント発火をしてみましょう。Cloud Foundry の trial サブアカウントから dev スペースに移動し、**Members**を選択してください。Cloud Foundry は US East (VA) で作成しておりますので、**Add Members**で技術ユーザ「`sap_cp_us10_ans@sap.com`」を追加します。
![素材画像_19.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/66750245-4f59-845b-eb24-56dac20daae6.png)
もし、US East (VA) でない場合（Azure や AWS Japan（Tokyo）等）、Help Portal (Documentation)の、**Built-In Event** → **User Lifecycle Events**で、対応するユーザーを確認してください。
![素材画像_18.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/a266f6e9-c946-9ee4-3c5e-7176cd7f89de.png)
その後、新たにメンバーを追加するとイベント発火より、メールや Slack に情報が通知されたことが確認できます。
![素材画像_21.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/f5e75d6e-c8c0-a0d4-b59e-4bf7e127bd13.png)

# おわりに

以上、簡単ではありますが、Alert Notification Service を利用して、Slack やメールに通知する設定方法の基本的な流れを整理しました。国内だけでなく世界的に見ても、SAP BTP の活用は今後も増え続けていくと確実視されますので、私自身も関連する技術情報を習得しどんどん発信していきたいと思います。

[JSUG]: https://www.jsug.org/
