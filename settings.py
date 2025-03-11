"settings.py" 35L, 983B                                                                                                                                                                                       1,1           All
import os
import datetime
import time
from google.oauth2 import service_account
from config import Configuration
from google.cloud import logging


def init():
    global today, timestamp, wday, now
    global _my_cfg
    global credentials
    global _logging_client, _logger

    now = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    today = time.strftime("%Y-%m-%d")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    wday = time.strftime("%u")

    _my_cfg = Configuration()

    credentials = service_account.Credentials.from_service_account_file(
        _my_cfg.auth_key, scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=_my_cfg.auth_key

    #print(_my_cfg.project_log, _my_cfg.auth_key)
    _logging_client = logging.Client(
                project="ti-dba-prod-01"
            ).from_service_account_json(_my_cfg.auth_key)
    _logger = _logging_client.logger("backups_log")

if __name__ == "__main__":
    init()
