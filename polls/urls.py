from django.urls import path
from . import views


# path(route, view, kwargs, name)
# 주소, 호출할 뷰, 뷰에 전달할 값, route의 이름(이 이름으로 원하는 곳에서 주소를 호출해 출력하거나 사용할 수 있음)
app_name = 'polls'
urlpatterns = [
    # ex : /polls/
    path('', views.index, name='index'),
    # ex : /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex : /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex : /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

