from . import views
from django.urls import path

app_name = 'exam'
urlpatterns = [
    path('',views.index),#默认访问首页
    path('index/',views.index,name='index'),
    path('studentLogin/',views.studentLogin,name='studentLogin'),#学生登录
    path('startExam/',views.startExam,name='startExam'),#开始考试
    path('calculateGrade/',views.calculateGrade,name='calculateGrade'),#考试评分
    path('stulogout/',views.stulogout,name='stulogout'), # 学生退出登录
    path('userfile/',views.userfile,name='userfile'), # 个人信息
    path('examinfo/',views.examinfo,name='examinfo'), # 考试信息
]