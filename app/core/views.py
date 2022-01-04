from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
import datetime
from core.models import User
from func import functions as fnc



class WelcomeView(View):


    template_name = "core/welcome.html"
    

    def get(self, request, *args, **kwargs):

        return render(
            request, 
            self.template_name, 
            self.get_context(request)
            )
    

    def get_context(self, request):
        """
        Context zwracany do GET
        """
        
        lan_ip = fnc.get_ip_lan()
        server_type = fnc.get_server_type()
        platform = fnc.get_platform_info()
        get_wan = fnc.get_wan()
        get_db = fnc.get_db()
        pip_packages = fnc.get_pip_packages()

        context = {
            "get_wan": get_wan,
            "get_ip_lan": lan_ip,
            "get_db": get_db,
            "get_server_type": server_type,
            "get_platform_info": platform,
            "get_pip_packages": pip_packages

        }


        return context
