# from django.http import
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
class SurveysessionMiddleware(MiddlewareMixin):
    """中间件判断是否有session"""
    inside_path = ['/index/', '/modify/', '/question/', '/question_sumbit/', '/delete/']
    def process_view(self, request, view_funce, *view_args, **view_kwargs):
        """在调用视图函数前调用"""
        print(view_funce)
        print(request.path)
        if request.path in SurveysessionMiddleware.inside_path:
            if request.session.has_key('username'):
                pass
            else:
                return redirect('/login/')

        # print(request.session['username'])
