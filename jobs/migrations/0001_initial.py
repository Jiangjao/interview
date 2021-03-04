# Generated by Django 3.0 on 2021-03-02 12:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=135, verbose_name='姓名')),
                ('city', models.CharField(max_length=135, verbose_name='城市')),
                ('phone', models.CharField(max_length=135, verbose_name='手机号码')),
                ('email', models.EmailField(blank=True, max_length=135, verbose_name='邮箱')),
                ('apply_position', models.CharField(blank=True, max_length=135, verbose_name='应聘职位')),
                ('born_address', models.CharField(blank=True, max_length=135, verbose_name='生源地')),
                ('gender', models.CharField(blank=True, max_length=135, verbose_name='性别')),
                ('picture', models.ImageField(blank=True, upload_to='images/', verbose_name='个人照片')),
                ('attachment', models.FileField(blank=True, upload_to='file/', verbose_name='简历附件')),
                ('bachelor_school', models.CharField(blank=True, max_length=135, verbose_name='本科学校')),
                ('master_school', models.CharField(blank=True, max_length=135, verbose_name='研究生学校')),
                ('doctor_school', models.CharField(blank=True, max_length=135, verbose_name='博士生学校')),
                ('major', models.CharField(blank=True, max_length=135, verbose_name='专业')),
                ('degree', models.CharField(blank=True, choices=[('本科', '本科'), ('硕士', '硕士'), ('博士', '博士')], max_length=135, verbose_name='学历')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('candidate_introduction', models.TextField(blank=True, max_length=1024, verbose_name='自我介绍')),
                ('work_experience', models.TextField(blank=True, max_length=1024, verbose_name='工作经历')),
                ('project_experience', models.TextField(blank=True, max_length=1024, verbose_name='项目经历')),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='申请人')),
            ],
            options={
                'verbose_name': '简历',
                'verbose_name_plural': '简历列表',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.SmallIntegerField(choices=[(0, '技术类'), (1, '产品类'), (2, '运营类'), (3, '设计类'), (4, '市场营销类')], verbose_name='职位类别')),
                ('job_name', models.CharField(max_length=250, verbose_name='职位名称')),
                ('job_city', models.SmallIntegerField(choices=[(0, '北京'), (1, '上海'), (2, '深圳'), (3, '杭州'), (4, '广州')], verbose_name='工作地点')),
                ('job_responsibility', models.TextField(max_length=1024, verbose_name='职位职责')),
                ('job_requirement', models.TextField(max_length=1024, verbose_name='职位要求')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '职位',
                'verbose_name_plural': '职位列表',
            },
        ),
    ]
