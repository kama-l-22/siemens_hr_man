from .models import *
from django.contrib import admin
# Register your model
admin.site.register(employee)
admin.site.register(hr)
admin.site.register(manager)
admin.site.register(qdmin)
admin.site.register([requestleave,approvedleave,report,request_employee,req_hr,req_man])