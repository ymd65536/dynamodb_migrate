import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

endpoint_url = 'http://localhost:8000'

# 問題毎のユーザスコアを格納するクラス
# UserScore モデルから参照
class ScoreMap(MapAttribute):
  q1 = NumberAttribute(null=True)
  q2 = NumberAttribute(null=True)
  q3 = NumberAttribute(null=True)

# 問題文のスコアを格納するモデル
class Score(Model):
  class Meta:
    table_name = 'Score'
    region = 'ap-northeast-1'
    aws_access_key_id = 'ACCESS_ID'
    aws_secret_access_key = 'ACCESS_KEY'
    host = endpoint_url

  question_id = UnicodeAttribute(hash_key=True)
  question = UnicodeAttribute()
  answer = UnicodeAttribute()
  score = NumberAttribute()

scores = Score
# ユーザスコアを格納するモデル
class UserScore(Model):
  class Meta:
    table_name = 'UserScore'
    region = 'ap-northeast-1'
    aws_access_key_id = 'ACCESS_ID'
    aws_secret_access_key = 'ACCESS_KEY'
    host = endpoint_url
  line_user_id = UnicodeAttribute(hash_key=True)
  scores = MapAttribute(of=ScoreMap)

if __name__ == '__main__':

  uset_input = 'q'
  event_type = 'follow'
  message_text = 'start'
  user_id = 'Yamada'

  # アカウントがフォローされたときと「start」が入力された時に出題開始
  if event_type == 'follow' or message_text == 'start' :
    
    # ユーザスコアが存在しない場合は作成する
    if not UserScore.exists():
      UserScore.create_table(read_capacity_units=1,
                            write_capacity_units=1, wait=True)

    # ユーザIDが存在しない場合は登録する
    UserScore(
                line_user_id=user_id,
                scores=ScoreMap(q1=None, q2=None, q3=None)
            ).save()
    
    # 最初の問題を取り出す
    first_question = scores.get_item(
                Key={"question_id": 'q1'}
            )['Item']['question']

    # クイズ開始のメッセージ
    greet_msg = "AWSにまつわる問題を用意しました。クイズを開始します。"
    print(greet_msg)

    # リプライトークンでFlexMessageを返信

  else:
    # 2問目以降
    user_score = UserScore.get(user_id)

    # 入力チェック
    if message_text.isnumeric():
      # 問題の途中であれば、正解または不正解を表示したあとに次の問題を取得

      insert_question = ''
      # 問題に対するスコアを取得

      # ユーザスコアを更新

      # 正解 or 不正解を 返す

      # 最後の問題を取得したかどうか
        # 合計点を返す

      # 最後の問題を取得していない場合は次の問題を取得

      print("得点を計算")
    else:
      print("数値を入力してください。")