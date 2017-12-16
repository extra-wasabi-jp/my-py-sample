# my-py-sample
Python お勉強用リポジトリです

## mongo db
以下のながれでコレクションを登録しておきます
````
# mongo localhost:28002/strz01t -u appuser -p
db.createCollection("user")
db.user.insert({accountId: "direct.k", empNo: "85001", email: "direct.k@maildomain", password: "pass123", userNm: "ダイレクト　会長", userNmKn: "ダイレクト　カイチョウ", userNmEn: "Direct, K", joinDt: "19850401", quitDt: ""})
````
