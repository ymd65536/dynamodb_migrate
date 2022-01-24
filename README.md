
# DynamoDBにデータを挿入するスクリプト

## セットアップ

IAMからプログラムからのアクセスができるアクセスキーとシークレットアクセスキーを発行する。

.env_sample を コピーして.envにリネーム

`aws_access_key_id`と`aws_secret_access_key`のイコールから後ろをそれぞれ置き換える。

```txt
aws_access_key_id=aws_access_key_id
aws_secret_access_key=aws_secret_access_key
```