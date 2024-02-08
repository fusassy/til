---
title: 【Tips】SAP Business Application Studio (SAP BAS) でhtmlファイルをブラウザで開く
tags: SAPUI5 SAPBTP KYOSO
author: fusassy
slide: false
---
# 概要
現在、主にSAP BTPでのアプリケーション開発に携わっている@fussasyといいます。SAP BTPにはWeb IDEのサービスとして「[SAP Business Application Studio](https://help.sap.com/docs/bas?locale=en-US)」があり、SAP S/4HANA導入プロジェクトにおいて、[Side By Side開発](https://qiita.com/Yanagawa_Yoshihisa/items/4dd3694800576e094b0a)で広く現場で活用されています。このSAP BASでのちょっとしたTipsの記事になります。

# 課題
たまたま現場での環境上、SAP Business Application Studioしか使えない状態で、簡単なhtmlファイルを開きたい、という場面に遭遇しました。パッと考えうる様々な手段を試したのですが、htmlファイルを表示することができませんでした。

# 解決策
拡張機能を入れてファイルを表示させるしかなさそうです。「[【簡単】HTMLをリアルタイムでプレビューする2つの方法【VS Code・Code Pen】](https://rilaks.jp/blog/html-preview/)」を参考に、使えそうな拡張機能を探してみました。
![BASの拡張アプリ検索結果.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/83e2f7b1-79c6-cf8b-5f0e-8f962ef726c1.png)
VSCodeだと「Live Server」と「HTML Preview」はありますが、SAP BASでは「Live Server」しかありませんでした。なので、こちらを導入してさっそくhtmlファイルを開き、「Go Live」をクリックしてローカルサーバーを立ち上げて確認したところ、無事にhtmlファイルをブラウザで表示することができました。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/2d51f58c-03ea-d384-c1a8-0ff9835cb3ad.png)
※右下のアイコンをクリックします。


# 補足
SAP Business Application Studio は基本的にVSCodeと酷似しているので、何か困ったことがあればVSCodeで検索してしまった方が解決が早く、スムーズです。（会社の後輩に教えてもろた）

# 関連リンク
https://help.sap.com/docs/bas?locale=en-US
https://qiita.com/Yanagawa_Yoshihisa/items/4dd3694800576e094b0a
https://rilaks.jp/blog/html-preview/
