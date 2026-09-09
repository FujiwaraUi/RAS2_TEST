from pathlib import Path
import random
import shutil

SRC_DIR = Path('/mnt/data/MyData/HSID/ICVL-BGU/ICVL_HS_2016/mat')
TRAIN_DIR = Path('/mnt/data/MyData/HSID/ICVL-BGU/ICVL_HS_2016/icvl_train')
TEST_DIR = Path('/mnt/data/MyData/HSID/ICVL-BGU/ICVL_HS_2016/icvl_test')


def main():
    if not SRC_DIR.exists():
        raise FileNotFoundError(f'Source directory not found: {SRC_DIR}')

    mat_files = sorted(SRC_DIR.glob('*.mat'))
    if not mat_files:
        raise FileNotFoundError(f'No .mat files found in: {SRC_DIR}')

    random.seed(42)
    random.shuffle(mat_files)

    train_count = int(len(mat_files) * 0.7)
    train_files = mat_files[:train_count]
    test_files = mat_files[train_count:]

    for target_dir in [TRAIN_DIR, TEST_DIR]:
        target_dir.mkdir(parents=True, exist_ok=True)
        for existing in target_dir.glob('*.mat'):
            existing.unlink()

    for file_path in train_files:
        shutil.copy2(file_path, TRAIN_DIR / file_path.name)

    for file_path in test_files:
        shutil.copy2(file_path, TEST_DIR / file_path.name)

    print(f'Total .mat files: {len(mat_files)}')
    print(f'Train files: {len(train_files)} -> {TRAIN_DIR}')
    print(f'Test files: {len(test_files)} -> {TEST_DIR}')


if __name__ == '__main__':
    main()
