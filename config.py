from configparser import ConfigParser
import os
# Backup methods.
FULL_BACKUP = 1
PARTIAL_BACKUP = 2
LOG_BACKUP = 3
POSTGRES_DUMP = 4
MYSQL_DUMP = 5

BACKUP_METHODS = [FULL_BACKUP, PARTIAL_BACKUP, LOG_BACKUP, POSTGRES_DUMP, MYSQL_DUMP]

class Configuration:
    def __init__(self, filename='config.cfg'):
        base = os.path.dirname(os.path.abspath(__file__))
        config_object = ConfigParser()
        filename = base + "/" + filename
        config_object.read(filename)

        self.project = config_object.get("SETUP", "project")
        self.dataset = config_object.get("DATABASE", "dataset")
        self.table = config_object.get("DATABASE", "table")
        self.table_log = config_object.get("DATABASE", "table_log")

        self.project_log = base + "/" + config_object.get("LOGS", "project")
        self.auth_key =  base + "/" + config_object.get("LOGS", "auth_key")
        self.db_auth_key = base + "/" + config_object.get("LOGS", "db_auth_key")
        self.key_path =  base + "/" + config_object.get("AUTH_CONFIG", "key_path")

        self.image = config_object.get("DOCKER", "image")

        self.maincmd = config_object.get("DOCKER", "maincmd")
