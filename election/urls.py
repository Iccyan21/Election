from mysite.urls import path
from election import views

urlpatterns = [
    path('',views.select, name='select'),
    path('select/<int:pk>/',views.Choose,name='Choose'), #候補者詳細ページ
    path('judge/<int:pk>/',views.judge,name='judge'), #投票確定確認画面
    path('vote/<int:pk>/',views.vote,name='vote'), #投票ページ
]
