"""
ICVL_HS_2016データセット(Hugging Face)のmat/ディレクトリを全件ダウンロードする。

事前準備:
    export HF_TOKEN="<取得済みのトークン>"
    pip install huggingface_hub

保存先:
    /mnt/data/MyData/HSID/ICVL-BGU/ICVL_HS_2016/mat/
"""
import os
from pathlib import Path

from huggingface_hub import snapshot_download

REPO_ID = "ICVL-BGU/ICVL_HS_2016"
LOCAL_DIR = Path("/mnt/data/MyData/HSID/ICVL-BGU/ICVL_HS_2016")


def main() -> None:
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise RuntimeError(
            "環境変数HF_TOKENが未設定である。'export HF_TOKEN=<トークン>' を実行してから再度実行すること。"
        )

    LOCAL_DIR.mkdir(parents=True, exist_ok=True)

    snapshot_download(
        repo_id=REPO_ID,
        repo_type="dataset",
        allow_patterns=["mat/*.mat"],
        local_dir=str(LOCAL_DIR),
        token=token,
    )

    n_files = len(list((LOCAL_DIR / "mat").glob("*.mat")))
    print(f"ダウンロード完了: {n_files}件の.matファイルを {LOCAL_DIR / 'mat'} に保存した")


if __name__ == "__main__":
    main()