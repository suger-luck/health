from django.contrib import admin
from survey.models import user, questions
# Register your models here.
# 注册用户类
class UserTabularInline(admin.TabularInline):
    """在编辑页中显示子类信息(表格的形式显示)"""
    # 关联子类对象
    model = questions
    list_display = ['submit_time']
    # 显示额外的编辑对象
    extra = 1
class UserAdmin(admin.ModelAdmin):
    inlines = [UserTabularInline]
admin.site.register(user, UserAdmin)
admin.site.register(questions)