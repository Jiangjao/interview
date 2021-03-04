from django.conf.urls import url
from . import views

urlpatterns = [
    # 职位列表
    url(r"^joblist/", views.joblist, name='joblist'),
    # url(r"^job/(?P<job_id>\d+)/$",views.detail, name='detail')
    # 职位详情
    url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),
]
