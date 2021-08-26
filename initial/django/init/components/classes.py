# This file contains classes

import components.interfaces


import os
import time


class AppOperations(components.interfaces.OperationsInterface):
    """
    Django class for basic operations on application
    """
    
    def __init__(self, app_path: str, python=None):
        super().__init__(python)
        self.__app_path = app_path
        self.__manage_file = os.path.join(app_path,"manage.py")


    def run_dev_server(self, host: str, port: int) -> None:
        """
        Runs django developing server
        """
        super().log(f"Starting developing server: {host}:{port}")
        return os.system(f"{self.get_python_version()} {self.__manage_file} runserver {host}:{port}")
        
        
    def run_pro_server(self, host: str, port: int) -> None:
        """
        Runs django production server
        """
        super().log(f"Starting gunicorn production server: {host}:{port}")
        return os.system(f"cd ./app && gunicorn --bind {host}:{port} project.wsgi")
    
    
    def make_migrations(self, params="") -> None:
        """
        Make migrations
        """
        super().log(f"Preparing migration files...")
        return os.system(f"{self.get_python_version()} {self.__manage_file} makemigrations {params}")
    
    
    def migrate(self, params="") -> None:
        """
        Migrates migrations
        """
        super().log(f"Applying migrations...")
        return os.system(f"{self.get_python_version()} {self.__manage_file} migrate {params}")
    
    def collect_static(self, params="") -> None:
        """
        Migrates migrations
        """
        super().log(f"Collecting statics...")
        return os.system(f"cd ./app && python3 manage.py collectstatic --noinput")
    
    
    def test(self, app="") -> None:
        """
        Runs complete test sequence
        """
        super().log(f"Running tests...")
        return os.system(f"{self.get_python_version()} {self.__manage_file} test {app}")
    
    
    def cover(self, app="") -> None:
        """
        Covering tests
        """
        super().log(f"Covering tests...")
        return os.system(f"coverage run {self.__manage_file} test {app}")
    
    
    def get_cover_raport(self) -> None:
        """
        Returns coverage raport
        """
        return os.system("coverage report")  
 
              
class SystemOperations(components.interfaces.OperationsInterface):
    """
    System and network operations
    """
    
    def __init__(self, python=None):
        super().__init__(python)
    
    
    def is_service_up(self, host: str, port: str, count: int, sleep: int) -> bool:
        """
        Checks if service is available using ping method
        """
        super().log(f"Checking host availability... {host}:{port}")
        cmd = "ping -i 0.1 -c 1 {0} -p {1}  > /dev/null".format(host,port)
        flag = False
        failed = 0
        while flag == False:
            for x in range(count):
                time.sleep(sleep)
                host_up = True if os.system(cmd) == 0 else False
                if host_up:
                    flag = True
                    break
                else:
                    super().log(f"Failed to connect! (attempt: {failed+1}/{count})")
                    failed += 1
                    if failed == count:
                        super().log(f"All attempts failed. Exiting...")
                        return False
        return flag
    
    
    
    





    