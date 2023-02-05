# simple-grpc-micro-service
gRPCを使用しているシンプルのマイクロサービスリポしトーリ

## grpc-server
- grpc-server について、grpcとpythonで実装されている
- grpc-server は `transcript`を受け取って、`openai`で間違った文法を修正する
- 最後に、修正された結果を返却する


## grpc-client
- grpc-clientはgrpcとgoで実装されている
- grpc-clientからTCP要求を送って、context timeout で待って

  成功したの場合、結果をターミナルに出力する。

  逆に、エラー時に、エラーのメッセージを出力する

フォローしてください: [manhhnv](https://github.com/manhhnv)

他のリポしトーリ: https://github.com/manhhnv?tab=repositories
