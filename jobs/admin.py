from django.contrib import admin
from jobs.models import Job
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    # 特定含义的属性
    exclude = ('creator','created_date','modified_date')
    list_display = ('job_name','job_type','job_city','creator','created_date','modified_date')
   
    # 自动填充字段，提交到数据库
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)
    


admin.site.register(Job,JobAdmin)

