---
title: 【SAP BTP】アーキテクチャ・ダイアグラムを描きたいけど公式アイコンが見つからない件
tags: SAPCF SAPBTP アイコン KYOSO
author: fusassy
slide: false
---

# はじめに

SAP 社のエンタープライズ PaaS 製品である、SAP Business Technology Platform（BTP） でアプリケーション開発をしている@fussasy です。上流工程において、アーキテクチャ・ダイアグラムを描く際に、AWS のようなクラウドベンダーが出している[アーキテクチャ・ダイアグラム][AWS Archetest Icon]の公式アイコンを利用したかったのですが、なかなか見つからなかったのでメモです。

# SAP の公式アイコン（icon）はどこにある？

以前まで、以下のリンクから利用規約と、SAP BTP（S4/HANA 含）のアイコンセットが記載された MS PowerPoint スライドが提供されており、このスライドからアイコンを取ってきて利用できました。
https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=477829554
しかし、現在は 301 リダイレクトされ SAP BTP の紹介ページに飛んでしまうみたいです……。
SlidePlayer にアップロードされているような、ppt スライドがあったんですけどね……。
https://slideplayer.fr/slide/18117778/

さて、どこかに残っていないかなと探したところ、以下の SAP ブログにダウンロードリンクが残っておりました。
（「Using the Solution Diagram Guidelines in MS PowerPoint」の項です）
https://blogs.sap.com/2018/01/05/be-visual-use-official-icons-and-samples-for-sap-cloud-platform-solution-diagrams/

ちなみに、以下がダウンロードリンクとなります。
https://d.dam.sap.com/a/JPUXye

他にも、PNG と SVG での zip 形式ファイルのダウンロードリンクも残っていました。
https://d.dam.sap.com/a/s9tyyJJ?rc=10

余談ですが、[Icon Explorer][Icon Explorer]ではイメージ画像を取得できません。
コチラは SAP UI5 に記述して画面表示させる際に利用します。

# おわりに

SAP 社の方から公式アナウンスがあれば、記事を更新したいと思います。
もし、SAP 社の方々が見てくださっていれば、AWS のような案内ページを作ってくださると、開発者としてはとても嬉しいです。

[Icon Explorer]: https://sapui5.hana.ondemand.com/test-resources/sap/m/demokit/iconExplorer/webapp/index.html
[AWS Archetest Icon]: https://aws.amazon.com/jp/architecture/icons/
