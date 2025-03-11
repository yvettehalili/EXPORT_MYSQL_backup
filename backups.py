import settings as settings
import argparse
import logging
#from createcronjob import k8s
from data import Servers
from export import CloudSQL

settings.init()
logging.basicConfig(level=logging.INFO)

def start_process():
    servers_list = Servers.list_all()
    for servers in servers_list:
        server_name = servers.name
        k8s.schedule(server=server_name, backup_date=settings.today)

def export_process(args):
    server_info = Servers.get_server_info(args.server)

    for server in server_info:
        #print(server)
        #uri = 'gs://' + server.bucket + '/' + server.save_path + server.name + '/'
        CloudSQL.export(server.project, server.name, server.save_path, args.date, server.bucket)

def check_process():
    print("Executing Checking" )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--command", type=str, choices=['start','export','check'])
    parser.add_argument("-s", "--server", help="Name of the Server", type=str)
    parser.add_argument("-d", "--date", help="Date to be performed", default=settings.today)

    args = parser.parse_args()

    if args.command == 'start':
        start_process()
    elif args.command == 'export':
        export_process(args)
    elif args.command == 'check':
        check_process()

    else:
        print("Not valid choice passed")
