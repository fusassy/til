---
title: 【備忘録】SAP BTPアプリ開発プロジェクトで、コーディング規約・命名規約の作成したときの資料一覧
tags: 備忘録 システム開発
author: fusassy
slide: false
---

# はじめに

SAP 社のエンタープライズ PaaS 製品である、SAP Business Technology Platform（BTP） でアプリケーション開発をしている@fussasy です。アプリケーション開発プロジェクトを経験する中で、コーディング規約や命名規約をイチから作成することがありました。その際の参考資料を簡単に整理しておきます。

# 命名・コーディングガイドライン

### JavaScript（SAPUI5）公式ガイドライン

Development Conventions and Guidelines
https://help.sap.com/saphelp_uiaddon10/helpdata/en/75/3b32617807462d9af483a437874b36/frameset.htm

### Java11（Spring Framework）各社ガイドライン

・フューチャー株式会社（Future Enterprise Coding Standards）
https://future-architect.github.io/coding-standards/
・フューチャー株式会社（Future Enterprise Coding Standards > Java コーディング規約）
https://future-architect.github.io/coding-standards/documents/forJava/
・Google Style Guides
https://google.github.io/styleguide/
・Google Style Guides（Java）
https://google.github.io/styleguide/javaguide.html

### Spring リファレンスドキュメント（SpringBoot）

https://spring.pleiades.io/

### Java 非推奨 API

・Oracle 提供
https://docs.oracle.com/javase/jp/8/docs/api/deprecated-list.html

# セキュリティコーディング

以下、基本的なセキュリティ対策は考慮して実装する旨を記載
実装方法については、検索すると具体的な内容がたくさんヒットしますので割愛します

・SQL インジェクション対策
・OS コマンドインジェクション対策
・ディレクトリ・トラバーサル対策
・セッション管理の不備対策
・クロスサイト・リクエスト・フォージェリ対策
・HTTP ヘッダインジェクション対策
・メールの第三者中継対策

# 暗号化

機密性を確保する必要がある情報は、当該情報の保存期間や取得難度に応じて、暗号化の必要性を検討
こちらも、実装方法については、検索すると具体的な内容がたくさんヒットしますので割愛します

・暗号アルゴリズム
・暗号ライブラリ
・暗号鍵
・電子署名

# その他

他、システム構成によっては、OData（CloudSDK）の利用規約や CAP（SAP Cloud Application Programming Model）の規約も、それなりに決めておくと良いと思います。

# おわりに

2 次請けだと、コーディング規約や命名規約が発注元（大手システムインテグレーターや、コンサルティングファーム等）から提供されている場合が多いですが、1 次請けだとイチから作る必要があり、中には成果物としてお客様から求められることもあります。そういう時は、先述したフューチャー株式会社様が提供しているコーディングガイドラインや、各種フレームワークの公式ガイドライン等を読み込み、引用していくのが早いと思います。また、各種フォーマッターに規約の設定を盛り込んでおけば、レビューの際に細かくコードを見る必要もなくなるので開発効率も上がって良いと思います。

# おまけ

SAP BTP アプリケーション開発プロジェクトを推進する際のために、レビュー用のチェックシートも作成しましあ。併せてご活用ください。

【チェックシート】システム開発において、基本・詳細設計書のレビューでよくある指摘観点をまとめる
https://qiita.com/fusassy/items/109c7e1f1f49573a1310

【チェックシート】システム開発において、Java11・SpringFramework で実装した際のコードレビューでよくある指摘観点をまとめる
https://qiita.com/fusassy/items/9c275570b1241ec68e75

【チェックシート】システム開発において、SAPUI5 で実装した際のコードレビューでよくある指摘観点をまとめる
https://qiita.com/fusassy/items/80ae30b1863c9834fded

【チェックシート】システム開発において、テスト設計・テストのレビューでよくある指摘観点をまとめる
https://qiita.com/fusassy/items/ad9828e93e17652d6d73
