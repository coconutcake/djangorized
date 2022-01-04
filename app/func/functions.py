import os
import socket
from requests import get
import platform
import psutil
import datetime
from django.contrib.auth import get_user_model
from django.forms import model_to_dict
from rest_framework.authtoken.models import Token
from typing import List


#Funckje 
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

def get_pip_packages():

    packages = [package for package in os.popen("pip3 freeze").read().split("\n")]

    packages.remove("")

    packages_dict = [{"name":package.split("==")[0],"version":package.split("==")[1]} for package in packages]

    return packages_dict


#Funkcje pomocnicze
def get_current_time():
    return datetime.datetime.now()

def get_yesterday_date():
    yesterday = get_current_time() - datetime.timedelta(days=1)
    return yesterday.date()

def get_created_yesterdays(model):
    return model.objects.filter(created__date=get_yesterday_date())

def get_updated_yesterdays(model):
    return model.objects.filter(updated__date=get_yesterday_date())

def create_user(**params):
    return get_user_model().objects.create_user(**params)

def get_user(**params):
    return get_user_model().objects.get(**params)

def get_pks_list(objects):
    return [x.pk for x in objects]

def get_token(user_instance):
    instance = get_user_model().objects.get(pk=user_instance.pk)
    return Token.objects.get(user=instance)

def create_token(user_instance):
    instance = get_user_model().objects.get(pk=user_instance.pk)
    return Token.objects.create(user=instance)

def model_to_dict_no_instances(
    instance: object, fields: List[str], instance_fields: List[str]
) -> dict:
    """
    :param instance: Takes an instance of model object
    :param instance_fields: Takes a List of field names which will be converted to their pk's
    :return: Returns dict from instance and converts fields 
    provided in List into its pk's
    """

    model_dict = model_to_dict(instance, fields=fields)

    for key, value in model_dict.items():
        if key in instance_fields:
            instance = value
            model_dict[key] = instance

    return model_dict

def model_to_dict_with_instances(
    instance: object, fields: List[str], instance_fields: List[str]
) -> dict:
    """
    :param instance: Takes an instance of model object
    :param instance_fields: Takes a List of field names which will be converted into instances
    :return: Returns dict from instance and converts id fields into instances
    """

    model_dict = model_to_dict(instance, fields=fields)

    for key, value in model_dict.items():
        if key in instance_fields:
            model = eval(f"instance.{key}._meta.model")
            obj = model.objects.get(pk=value)
            model_dict[key] = obj

    return model_dict

def get_model_payload_instances_fields(payload: dict) -> dict:
    """
    :param payload: Takes dict as a payload of model instance
    :return: Returns List of instances fields from dict
    """
    lista = list()
    for key, value in payload.items():
        try:
            if value._meta.model.__name__:
                lista.append(key)
        except:
            pass

    return lista

def get_model_payload_origin_instances_fields(payload: dict) -> dict:
    """
    :param payload: Takes dict as a payload of model instance
    :return: Returns List of original instances used in payload
    """
    lista = list()
    for key, value in payload.items():
        try:
            if value._meta.model.__name__:
                lista.append(value._meta.model.__name__)
        except:
            pass

    return lista

def convert_model_payload_no_instances(payload: dict):
    """
    :param payload: Takes dictionary payload of instance object
    :return: Converts dictionary payload instances to their pks
    """
    obj_dict = dict()
    for key, value in payload.items():
        try:
            if value._meta.model.__name__:
                obj_dict[key] = value.id
        except:
            obj_dict[key] = value

    return obj_dict

def exclude_fields(excluded_fields: List, payloads: List):
    """
    Exclude fields from given payloads in List
    """
    if len(excluded_fields) > 0 and len(payloads) > 0:
        for payload in payloads:
            for field in excluded_fields:
                try:
                    payload.pop(field)
                except:
                    raise Exception


