from django.urls import path
from survey import  views

urlpatterns = [
    path('index/', views.index, name='index'), # 首页
    path('login/', views.login,name='login'), # 登录页面
    path('login_user/', views.login_user, name='login_user'), # 登录用户名校验
    path('login_check/', views.login_check, name='login_check'), # 登录校验
    path('registered/', views.registered, name='registered'), # 注册页面
    path('registered_check/', views.registered_check, name='registered_check'), # 注册验证页面
    path('check_id/', views.check_id, name='check_id'), # 验证注册是否已经注册
    path('modify/', views.modify, name='modify'), # 修改信息
    path('delete/', views.delete, name='delete'), # 退出登录，清除session
    path('question/', views.question, name='question'), # 调查问卷
    path('question_sumbit/', views.question_submit, name='question_sumbit'), #提交调查问卷
]
