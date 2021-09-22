# iNAZO

iNAZO とは北大が公開している成績データを見やすく纏めた Web アプリケーションです。

## Features

- グラフで表示
- 検索
- ソート機能
- ブックマーク登録

## Local Usage

./clientでの作業
```
yarn install
yarn dev
```

./serverでの作業
```
pipenv sync
cp .env.example .env
```
.envのDATABASE_URLを絶対パスで適切に設定する
example: sqlite:////tmp/my-tmp-sqlite.db
```
pipenv run migrate
pipenv run dev
```

初期データは別途スクレイピングをしてDBに保存してください。

## Source

北海道大学 成績分布ＷＥＢ公開システム
http://educate.academic.hokudai.ac.jp/seiseki/GradeDistSerch.aspx

## How To Contribute

- 機能追加の要望やバグの発見などは、既存のものがないか確認してください。

- プルリクエストはまずレポジトリに Fork してからコードの追加、修正をします。その後 develop ブランチに変更点を簡単に書いて送ってください。

## Relevant repository

OGP IMAGEを動的に生成するツール
[iNAZO-opg-image](https://github.com/karintou8710/iNAZO-ogp-image)

## License

このプロジェクトは [MIT license](https://en.wikipedia.org/wiki/MIT_License) です。


