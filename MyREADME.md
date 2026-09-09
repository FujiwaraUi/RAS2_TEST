# RAS2S 環境構築・現状メモ

補足: ファイル名を「MyREWADME.md」と指定されたが、`README`の綴りと解釈し`MyREADME.md`として作成した。異なる意図であれば指示してほしい。

## プロジェクトの場所

```
/mnt/data/MyData/Code/git_hsi/01_RAS2S/RAS2S
```

`pyproject.toml`・`uv.lock`が存在し、uvで管理する構成に変更済み(`src`レイアウト)。

## 環境構築

| 項目 | 内容 |
|---|---|
| conda環境名 | `py37` |
| PyTorch | 1.13.1+cu117 |
| GPU | GeForce GTX 1080(認識確認済み) |
| 環境ファイル | `requirements.yaml`(README記載の`environment.yml`とはファイル名不一致。作成時に`-n py37`で環境名を明示指定し、原著者のパスを含む`prefix`行の影響を回避した) |
| `caffe`依存 | `basic/`配下のコードで未使用と確認済み。動作に影響なし |

## データセット(ICVL)の入手方法

会津大学のBGU公式ページは再編されており、現在はHugging Faceにミラーが存在する。今回は`https://huggingface.co/datasets/ICVL-BGU/ICVL_HS_2016`からダウンロードした。

- リポジトリ: `ICVL-BGU/ICVL_HS_2016`
- 構成: `mat/`(31バンド、202ファイル)、`raw/`(519バンド)、`preview/`(RGB JPEG)
- 学習・評価に必要なのは`mat/`のみ(`rad`キーを保持し、`lmdb_data.py`・`mat_data.py`の読み込みキーと整合)
- アクセスにはHugging Faceアカウントでの利用条件同意とトークンが必要(ゲート付き)

### ダウンロードスクリプト

```
/mnt/data/MyData/Code/git_hsi/01_RAS2S/RAS2S/src/fy/data_downlad.py
```

`mat/*.mat`を全件、以下に保存する設定。

```
/mnt/data/MyData/HSID/ICVL-BGU/ICVL_HS_2016/mat/
```

実行前に`export HF_TOKEN=<トークン>`が必要。
