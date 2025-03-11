from logging_handler import Backup_Logger
import datetime
from export import CloudSQL

if __name__ == "__main__":
    log = Backup_Logger()
    log.process_start()

    project_id="ti-ca-infrastructure"
    instance_id="ti-mysql-us-we-14"
    save_path="Backups/Current/POSTGRESQL/"
    date_prefix="20241021"
    bucket_name="ti-dba-prod-sql-01"
    CloudSQL.export(project_id, instance_id, save_path, date_prefix, bucket_name)
    #print(Database.getServerType("mysqldbv8", "ti-dba-devenv-01"))
