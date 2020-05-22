from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from survey.models import user, questions
from datetime import datetime
# Create your views here.
# index/ 首页
def index(request):
    """首页"""
    # if request.session.has_key('username'):
    #     return render(request, 'survey/index.html')
    # else:
    #     return redirect('/login/')
    return render(request, 'survey/index.html')

#  login/ 登录
def login(request):
    """登录"""
    # print(0)
    if request.session.has_key('rember'):
        # print(1)
        return redirect('/index/')
    return render(request, 'survey/login.html')

# login_username 校验用户名
def login_user(request):
    username = request.GET.get('username')
    print(username)
    if user.objects.filter(stu_id=username):
        return JsonResponse({'c':1})
    else:
        # 用户不存在
        return JsonResponse({'c':0})

# login_check/ 登录校验
def login_check(request):
    """登录校验"""
    # 获取登录的用户
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 获取数据库中的用户
    if user.objects.filter(stu_id=username):
        username_c = user.objects.get(stu_id=username)
        # print(f'username:{username}')
        # print(f'username_c:{username_c}')
        # print(f'password:{password}')
        # print(f'password_c:{username_c.password}')
        # 是否两周内免密登录
        rember = request.POST.get('rember')
        print(f'免密登录:{rember}')
        if username_c.password == password:

            if rember == 'true':
                # 免密登录
                request.session['rember'] = True
                request.session['username'] = username
                print('免密')
            else:
                request.session['username'] = username
                request.session.set_expiry(0)
                print(112345)
            return JsonResponse({'res':1})
        else:
            # 密码错误
            return JsonResponse({'res':0})
    else:
        # 用户不存在
        return JsonResponse({'res':0})

    # if username == 'suger' and password == 'chd123..':
    #     return JsonResponse({'res': 1})
    # return JsonResponse({'res': 0})

# 退出登录
def delete(request):
    """退出登录，清除session"""
    request.session.flush()
    return redirect('/login/')

# registered/ 注册页面
def registered(request):
    """注册页面"""
    return render(request, 'survey/registered.html')

# password_check/ 注册用户
def registered_check(request):
    """注册用户验证"""
    # 1. 查询
    # 姓名
    name = request.POST.get('name')
    # 学号/工号
    stu_id = request.POST.get('stu_id')
    # 学院/部门
    college = request.POST.get('college')
    # 密码
    password = request.POST.get('password_1')
    # 班级
    stu_class = request.POST.get('stu_class')
    # 2. 项数据库添加数据
    stu = user()
    stu.stu_id = stu_id
    stu.name = name
    stu.college = college
    stu.password = password
    stu.stu_class = stu_class
    stu.save()
    return redirect('/login/')

# check_id/ 验证用户是否注册
def check_id(request):
    """验证用户是否注册"""
    a = request.GET.get('stu_id')
    # print(a)
    # stu = user.objects.filter()
    # print(stu)
    if user.objects.filter(stu_id=a):
        # print('存在')
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': ''})

#  modify/ 修改信息
def modify(request):
    """修改信息"""
    # 未完成 修改时间5.20
    username = request.session['username']
    print(request.session['username'])
    user_id = user.objects.get(stu_id= username)
    password = user_id.password
    stu_class =  user_id.stu_class
    college = user_id.college
    name = user_id.name
    data = {'name' : name, 'stu_id' : user_id, 'password' : password, 'college' : college, 'stu_class' : stu_class}
    # print(password)
    return render(request,'survey/modify.html', data)

# question/ 调查问卷
def question(request):
    """ 调查问卷 """
    return render(request, 'survey/question.html')


# question_submit/ 提交调查问卷
def question_submit(request):
    """提交调查问卷"""
    # 获取提交数据
    # 温度
    temp = request.GET.get('temp')
    # 发热
    heat = request.GET.get('heat')
    # 生病
    sick = request.GET.get('sick')
    # 接触境外人员
    contact = request.GET.get('contact')
    # 旅居史
    overseas = request.GET.get('overseas')
    # 高风险地区
    high_rish = request.GET.get('high_rish')
    # 疑似/确诊/无症状
    virus = request.GET.get('virus')
    # 备注
    remarks = request.GET.get('remarks')
    print(f'temp:{ temp }\n heat:{ heat }\nsick:{sick}\ncontact:{contact}\noverseas:{overseas}\nhigh_rish:{high_rish}\nvirus：{virus}\nremark:{remarks}')
    # 获取父标签
    father = request.session['username']
    print(father)

    s = questions()
    # print(s)
    s.temperture = temp
    s.heat = heat
    s.sick = sick
    s.contact =contact
    s.overseas = overseas
    s.high_rish = high_rish
    s.virus =virus
    s.remarks =remarks
    s.submit_time = datetime.now()
    s.father = user.objects.get(stu_id=father)
    # print(s)
    s.save()
    return redirect('/index/')