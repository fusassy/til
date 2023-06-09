---
title: 【マネジメント】クリティカルチェーン・プロジェクトマネジメント（CCPM）の解説、システム開発（SI）での適用失敗談も含めて
tags: CCPM プロジェクト管理 学習
author: fusassy
slide: false
---

# はじめに

現在、受託開発企業でプロジェクトリードをしている、@fussasy です。直近で参画したプロジェクトにおいて、あくまで 2 次請けという立場ですが、試験的にクリティカルチェーン・プロジェクトマネジメント（CCPM）を採用し、プロジェクトマネジメントを実施していました。自身は実業務で経験したことがなかったため、事前学習をした内容と、実プロジェクト適用への感想をまとめておきます。

# 「エリヤフ・ゴールドラット(著), 三本木亮(著)：クリティカルチェーン－なぜ、プロジェクトは予定どおりに進まないのか？」

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/fd4f9b31-00b8-932a-46f0-dd9a89f3816e.png)
プロジェクトには「目的（scope）」「資源（resource/money）」「期限（Time）」の三つの要素が含まれ、これを[プロジェクトの三角形]と呼びます。プロジェクトはこの三角形のバランスを保ちながら推進していく必要があります。内的要因・外的要因から、三角形のバランスに影響を及ぼす制約（ボトルネック）が発生します。制約は予測できれば良いものの、たいていは精緻に見積もることが困難です。そのため、プロジェクトマネジメントというのは、ビジネスにおいて非常に難易度の高い業務の一つとなります。

その解決手段としての一つとして、考え出されたプロジェクトマネジメント手法の一つが、「クリティカルチェーン・プロジェクトマネジメント（CCPM）」となります。

「クリティカルチェーン」とは、プロジェクト管理において遅延やコスト超過を引き起こす要因を特定し、効率的なプロジェクト管理手法を提供する理論です。本書では、この理論を基にプロジェクト管理の問題点と解決策について詳しく説明しています。

### 本書の要点

**・プロジェクト管理において、タスクの長さを最適化し、余裕時間を確保することが重要。**
**・プロジェクト管理において、予測不可能性を考慮した時間管理が必要。**
**・「クリティカルチェーン」という手法を活用することで、プロジェクトの遅延や余裕時間不足を解消できる。**
**・「パーキンソンの法則」による余裕時間不足を回避するため、タスクの長さを最適化し、余裕時間を確保する必要がある。**
**・プロジェクトの進捗管理やリスク管理、チームビルディングなどのスキルを磨くことが、プロジェクト管理の効率性を高めることにつながる。**

### 書評

著者は、世界中の企業でクリティカルチェーンを導入し、プロジェクトマネジメントの改善に取り組んできました。本書では、クリティカルチェーンの理論に基づくプロジェクトマネジメント手法を紹介しつつ、プロジェクトが進まない原因や解決策についても詳しく解説されています。本書は理論だけでなく、事例と併せた説明が豊富であり、クリティカルチェーンの理論は単なるスケジューリング手法ではなく、プロジェクトマネジメントのあり方自体を変えるものである、という点が強調されています。
本書より、プロジェクトマネージャーとして、多くの考え方を知ることができました。特にリソースの制約や、タスクの見積もりに対する新しい視点を得ることが出来たと思います。クリティカルチェーンを実プロジェクトで活用してみる際には、一読の価値があると思いました。

# 「宇治川浩一(著), アジャイル CCPM：プロジェクトのマネジメントを少し変えて組織全体のパフォーマンスを大きくのばす」

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/b899d5ee-f994-da5b-bdb1-7b1317a8b236.png)
本書は、クリティカルチェーン・プロジェクトマネジメント（CCPM）とアジャイル開発を組み合わせた手法について説明したものです。CCPM はプロジェクトの遅延や余裕時間不足を解消する手法であり、アジャイル開発は短い期間でスプリントを実施してプロダクトを開発する手法です。本書では、この 2 つの手法を組み合わせることで、プロジェクトマネジメントの効率性を高め、組織全体のパフォーマンスを向上させる方法を紹介しています。

### 本書の要点

**・CCPM とアジャイル開発を組み合わせることで、プロジェクトマネジメントの効率性を向上させることができる。**
**・CCPM の手法において、タスクの長さを最適化し、余裕時間を確保することで、プロジェクトの遅延や余裕時間不足を解消することができる。**
**・アジャイル開発においては、短い期間でスプリントを実施することで、プロダクトの開発効率を高めることができる。**
**・CCPM とアジャイル開発を組み合わせることで、プロジェクトの優先順位を明確にし、プロジェクトチーム全体の意識を高めることができる。**
**・CCPM とアジャイル開発を組み合わせることで、組織全体のパフォーマンスを向上させることができる。**

### 書評

CCPM はプロジェクトのタスクの依存関係を解決することができるが、開発のスピードを抑える要因ともなっています。一方、アジャイル開発手法は迅速かつ柔軟に開発を進めることができるが、開発に関する情報共有が不足しているという問題があります。本書は、CCPM とアジャイル開発手法を組み合わせ、プロジェクトの進捗管理と迅速な開発を両立する手法を、事例と効果を併せて提唱しています。
プロジェクトの優先順位付けや、CCPM の進行状況を可視化するためのツールの選定、チームのモチベーションを高めるための方法などが紹介されており、CCPM を実際に導入する場合に役立つ情報も記されています。CCPM の導入にあたっての課題や障壁も率直に取り上げられており、具体的な解決策も提供されています。本書は、CCPM の理論的な解説から実践的な導入方法までを網羅しており、CCPM を導入したいと考えているプロジェクトマネージャーや、組織運営において課題を感じている経営者・リーダーにとっても有益であると思いました。

# クリティカルチェーン・プロジェクトマネジメント（CCPM）を利用してみる

### クリティカルチェーン・プロジェクトマネジメント（CCPM）における、バッファマネジメント

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/ec0e4787-36ce-b3e6-9c7b-28a6364110a2.png)
プロジェクトの遅れやリスクに対応するためのバッファを設定し、そのバッファを管理することで、プロジェクトの進行をコントロールする手法です。バッファマネジメントでは、タスクの完了までの時間を見積もり、タスク間にバッファを配置します。プロジェクトの進行状況を監視し、バッファの使用状況に応じて、遅れが発生する可能性が高いタスクに優先的にリソースを割り当てたり、リスクを軽減するために予防措置を講じたりします。タスクから無理やりバッファを出すことは、バッファの役割を無効化することにつながり、プロジェクトの進捗管理に影響を与える可能性があります。基本的には、以下の 3 点を意識する必要があります。

**・バッファを正確に設定して、プロジェクトが計画通りに進む余裕が生ませ、遅れに対処できるようにする。**
**・バッファの使用状況を定期的に監視し、必要に応じて適切なアクションを講じます。例えば、リスクが発生した場合は、バッファを使用して対応する。**
**・バッファを出す必要が生じる原因を分析し原因を解決することで、バッファを出す必要性をなくす。**

CCPM では、マルチプロジェクトでのバッファマネジメントにも対応しています。異なるプロジェクト間で共有されるリソースを適切に管理し、全体最適化をする方法も先述の書籍に記載されています。

### クリティカルチェーン・プロジェクトマネジメント（CCPM）における、バッファートレンドグラフ

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1727556/ab8be376-df7b-f8f2-daf5-4d60e28cccbd.png)
バッファートレンドグラフは、時間の経過とともに、プロジェクトのバッファーの状況を示すグラフです。各タスクの終了予定日と実際の完了日の間の余裕時間を示す「タスクバッファー」と、プロジェクト全体の終了予定日と実際の完了日の間の余裕時間を示す「プロジェクトバッファー」の予想値と実際値を示し、進捗状況を可視化します。
このグラフの利点は、プロジェクトの進捗状況を視覚的に理解することができることです。ただ、バッファートレンドグラフは、情報を正確に入力しなければ、正しい進捗状況を示すことができません。また、グラフはあくまでも予想値と実際値を示すため、プロジェクトがどのようなリスクを抱えているかを正確に把握することができません。よって、バッファートレンドグラフは、プロジェクトの進捗状況を把握するための重要なツールですが、情報を正確に入力し、他の情報と照らし合わせながら分析する必要があります。

### クリティカルチェーン・プロジェクトマネジメント（CCPM）を利用できるツール・サービス

様々なツール・サービスが展開されていますが、国内では以下が主要なものと思います。

Kintone：https://www.kintone.com/
Lychee-redmin：https://lychee-redmine.jp/
他

### クリティカルチェーン・プロジェクトマネジメント（CCPM）において、各タスクのバッファが生み出せない件

一般的に以下の方法が取られるものの、必ずしもバッファが生み出せるとは限りません。CCPM では、バッファを生み出すことが目的ではなく、タスクの最短化と納期の確保が重要視されています。

**・タスクの見積もりが正確かどうか確認**
**・リソースを適切に割り当てているか確認**
**・並列化できるタスクがないか検討**
**・プロジェクトのボトルネックを特定**

# おわりに（システム開発（SI）での適用失敗談も含めて）

PMP PMBoK 第 7 版のスケジュールマネジメントでも、「スケジュール・モデルの選択」→「クリティカル・チェーン・マネジメントの概要」→「クリティカル・チェーンの特定」→「バッファー・マネジメント」→「CCPM の実装」といった具合に、CCPM の記載は含まれます。プロジェクトマネジメントに接する機会がある場合、手段の一つとしては認識しておいた方が良いと思いました。

ただ、あくまで 2 次請けという立場で、プロジェクト全体統括である立場ではないものの、実プロジェクトで CCPM を適用した正直な感想として語ると、「破綻していたな……、」と感じました。実際に目で見た、CCPM が破綻していく様子は以下の通りです。（CCPM の手法が悪いという意味では決してありません。）

**① プロジェクト全体では、従来型のクライアントワーク系のウォーターフォール開発であるため、クライアント側のタスクは完全にブラックボックスとなっている。**
**②CCPM を実施するために、各タスクの作業見積もりを 80%に抑え 20%をバッファーとするような、いわゆるバッファーを捻出することが目的化している。**
**③ 結果、各タスクは当たり前のように、見積もり内で終わることはなく、バッファーを喰い始める。**
**④ さらに上流で仕様変更が多発することで、全体のバッファも喰い潰し始める。**
**⑤ バッファーが枯渇。バッファートレンドグラフが赤信号を常時点灯。よくあるプロジェクト炎上状態となる。**

簡潔に書くとこんな感じです。CCPM 自体はプロジェクトマネジメントのコストも下がりますし、マルチプロジェクトでも適用できるので、良い手法なはずなのですが、やはり従来型のクライアントワーク系のウォーターフォール開発への適用は困難なように思われました。よって、CCPM が威力を発揮してくるのは自社内開発かつ、アジャイル型の開発プロジェクトに限られてくる気がします。個人的には、自チーム（≒ 自社プロジェクト）で CCPM でマネジメントをしてみて、勘所は掴むことが出来たので、今後、CCPM に適した開発プロジェクトがあれば試していきたいな、とは思っています。

# 参考図書

エリヤフ・ゴールドラット(著), 三本木亮(著)：クリティカルチェーン－なぜ、プロジェクトは予定どおりに進まないのか？

宇治川浩一(著), アジャイル CCPM：プロジェクトのマネジメントを少し変えて組織全体のパフォーマンスを大きくのばす

プロジェクトマネジメント協会（PMI） (著) ：プロジェクトマネジメント知識体系ガイド（PMBOK ガイド）第 7 版＋プロジェクトマネジメント標準
