import components.classes
import components.prints

import os

# Environmnent variables
server_type = os.environ['APPSERVER'] # <- 1 - Developing, 2- Production
port = os.environ['PORT']
host = os.environ['ADDRESS']
db_host = os.environ.get("DB_ADDRESS")
db_port = os.environ.get("DB_PORT")

# Instances
app_operations = components.classes.AppOperations(
    app_path="./app/", python="3"
    )
sys_operations = components.classes.SystemOperations(
    python="3"
    )
    
    
if __name__ == "__main__":

    if sys_operations.is_service_up(host=db_host,port=db_port,count=3, sleep=1):
        
        app_operations.make_migrations()
        app_operations.test("app")
        app_operations.cover()
        app_operations.get_cover_raport()
        app_operations.migrate()
        
        while True:
            if server_type == "developer":
                app_operations.run_dev_server(host=host, port=port)
                
            elif server_type == "production":
                app_operations.collect_static()
                app_operations.run_pro_server(host=host, port=port)
            
            else:
                print("You have provided wrong type of option! Please try again")
    
    
    

