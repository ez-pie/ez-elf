import os
import shutil
import tarfile
import tempfile
import zipfile

WORKING_DIR = "/home/workspace"
ARTIFACTS_DIR = "/home/artifacts"
TAR_ARCHIVE_NAME = "archive.tar.gz"
ZIP_ARCHIVE_NAME = "archive.zip"


def ezecho(input):
    return input


def copy_working_dir(include_hidden_files=False):
    """将工作目录下的文件打包并拷贝到 artifacts 目录"""
    copy_dir(WORKING_DIR, include_hidden_files)


def copy_dir(dir: str, include_hidden_files=False):
    _ = create_zip_archive(dir, ARTIFACTS_DIR, ZIP_ARCHIVE_NAME)


# **************** utils ****************


def create_zip_archive(source_dir, destination_dir, archive_name):
    # 创建临时文件夹
    temp_dir = tempfile.mkdtemp()

    # 创建 zip 文件
    archive_path = os.path.join(temp_dir, archive_name)
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        # 遍历源目录中的所有文件和子目录
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, arcname=os.path.relpath(file_path, source_dir))

    # 将生成的 zip 文件移动到目标目录
    destination_path = os.path.join(destination_dir, archive_name)
    shutil.move(archive_path, destination_path)

    # 删除临时文件夹
    shutil.rmtree(temp_dir)

    # 返回 zip 文件的路径
    return destination_path


def create_tar_archive(source_dir, destination_dir, archive_name):
    # 创建临时文件夹
    temp_dir = tempfile.mkdtemp()

    # 创建 tar.gz 文件
    archive_path = os.path.join(temp_dir, archive_name)
    with tarfile.open(archive_path, "w:gz") as tar:
        # 遍历源目录中的所有文件和子目录
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                tar.add(file_path, arcname=os.path.relpath(file_path, source_dir))

    # 将生成的 tar 包移动到目标目录
    destination_path = os.path.join(destination_dir, archive_name)
    shutil.move(archive_path, destination_path)

    # 删除临时文件夹
    shutil.rmtree(temp_dir)

    # 返回 tar.gz 文件的路径
    return destination_path
