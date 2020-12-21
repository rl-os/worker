from typing import TextIO

import os
import re
import boto3
import tarfile
import logging
import tempfile
import requests
from logging import getLogger

# noinspection PyUnresolvedReferences
import src.entrypoint
from src.config import config

logging.basicConfig(level=logging.DEBUG)
log = getLogger(__name__)


s3 = boto3.client(
    's3',
    endpoint_url=config.storage.s3.endpoint_url,
    region_name='ru-1a',
    aws_access_key_id=config.storage.s3.access_key_id,
    aws_secret_access_key=config.storage.s3.secret_access_key,
)


REGEX_FILENAME = r'\/(\S+\w+)$'
REGEX_FILENAME_COMPILED = re.compile(REGEX_FILENAME)


def load_tar(tar_file: str):
    """
    Load tar file from temp file and upload it to s3

    """
    tar = tarfile.open(tar_file, mode="r:bz2")

    for item in tar.getmembers():
        log.info("uploading %s file", item.name)

        f = tar.extractfile(item)

        try:
            filename = REGEX_FILENAME_COMPILED \
                .search(item.name)\
                .group(1)

            s3.put_object(
                Body=f.read(),
                Bucket=config.storage.beatmaps_path,
                Key=filename,
            )

            log.info("done")
        except Exception as e:
            log.error("s3 uploading error: %s", e)


def run():
    """
    Load and update beatmaps from data url
    Загружает и обновляет карты с сервера
    """
    # update me
    data_url = "https://data.ppy.sh/2020_12_01_osu_files.tar.bz2"

    with tempfile.TemporaryDirectory() as tmpdirname:
        log.debug("created temporary directory %s", tmpdirname)
        tf = tempfile.NamedTemporaryFile(delete=False, dir=tmpdirname, mode='w+b')
        log.debug("created temporary file %s", tf.name)

        log.info("loading information from data server")
        with requests.get(data_url, stream=True) as r:
            log.debug("request status and header %d", r.status_code)

            if r.status_code != 200:
                log.error("invalid request status %d with %s", r.text, r.headers)
                return

            log.debug("downloading file from server")
            for chunk in r.iter_content(chunk_size=8192, decode_unicode=True):
                tf.write(chunk)

        tf.close()
        try:
            load_tar(tf.name)
        except Exception as e:
            log.error(e)
        finally:
            os.unlink(tf.name)


if __name__ == '__main__':
    run()
