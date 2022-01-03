import os
import socket
from requests import get
import platform
import psutil

def get_ip_lan():

    return socket.gethostbyname(socket.gethostname())

def get_wan():

    ip = get('https://api.ipify.org').content.decode('utf8')
    port = os.environ.get("SERVER_URL").split(":")[2].split("/")[0]

    info = {
        "ip": ip,
        "port": port ,
        "port_status": get_port_status(ip,port),
        "pingable": ping(ip)
    }

    return info

def ping(hostname):
    response = os.system("ping -c 1 " + hostname)

    if response == 0:
        pingstatus = True
    else:
        pingstatus = False

    return pingstatus

def get_ip_wan():

    return get('https://api.ipify.org').content.decode('utf8')

def get_port():

    return os.environ.get("SERVER_URL").split(":")[2].split("/")[0]

def get_db():

    address = os.environ.get("DB_ADDRESS")

    info = {
        "engine": os.environ.get("DB_ENGINE"),
        "address": address,
        "port": os.environ.get("DB_PORT"),
        "pingable": ping(address)
    }

    return info

def get_db_engine():

    return os.environ.get("DB_ENGINE")

def get_port_status(HOST,port,is_hostname=False):

    host = HOST
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        if is_hostname:
            host = socket.gethostbyname(HOST)
        s.connect((host, int(port)))
        s.shutdown(2)
        return True
    except:
        return False

def get_db_address():

    return os.environ.get("DB_ADDRESS")

def get_db_port():

    return os.environ.get("DB_PORT")

def get_server_type():

    return os.environ.get("APPSERVER")

def get_platform_info():

    info = {
        "platform": platform.platform(),
        "machine": platform.machine(),
        "cores": psutil.cpu_count(),
        "memory_percent": psutil.virtual_memory().percent
    }

    return info