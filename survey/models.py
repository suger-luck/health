from django.db import models

# Create your models here.
class user(models.Model):
    """用户表"""
    # id = models.AutoField(auto_created=True, serialize=False, verbose_name='ID')
    # 账号（工号/学号）  设置成主键
    stu_id  = models.CharField( verbose_name='工号/学号', max_length=20, unique = True)

    # 姓名
    name = models.CharField(verbose_name='姓名', max_length=20)

    # 学院/部门
    college = models.CharField(verbose_name='学院/部门', max_length=100)

    # 班级/职工可以不填写
    stu_class = models.CharField(verbose_name='班级', max_length=100, null=True,blank=True)

    # 密码
    password = models.CharField(verbose_name='密码', max_length=20)
    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.stu_id


class questions(models.Model):
    """问卷调查"""
    # 温度
    temperture = models.FloatField(verbose_name='体温')

    # 是否发热
    heat = models.BooleanField(verbose_name='发热')

    # 是否生病
    sick = models.BooleanField(verbose_name='生病')

    # 是否接触过境外人员
    contact = models.BooleanField(verbose_name='接触过及境外人员')

    # 是否有境外旅居史
    overseas = models.BooleanField(verbose_name='有旅居史')

    # 是否在高风险地区停留过
    high_rish = models.BooleanField(verbose_name='在高风险地区停留过')

    # 是否是疑似/确诊/无症状感染者
    virus = models.BooleanField(verbose_name='疑似/确诊/无症状感染', default=False)
    # 备注
    remarks = models.CharField(verbose_name='备注', max_length=1000, null=True, blank=True)

    # 提交时间
    submit_time =  models.DateTimeField(verbose_name='提交时间',auto_now_add=True)

    # 父级,取消外键的约束
    father = models.ForeignKey(user, on_delete=models.CASCADE, db_constraint=False)

    def __str__(self):
        # 设置显示填写的时间
        time = self.submit_time.strftime('%Y-%m-%d %H:%M:%S')
        # print(self.submit_time)
        # print(time)
        return time

    class Meta:
        db_table = 'question'


