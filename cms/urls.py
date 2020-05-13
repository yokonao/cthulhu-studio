from django.urls import path
from .views import (CharaDetail, CharaList, CharaUpdate, CharaDelete, CharaAdd)

app_name = 'cms'
urlpatterns = [
    # 一覧
    path('chara/', CharaList.as_view(), name='chara_list'),
    # 詳細
    path('chara/detail/<int:pk>/<str:what>/', CharaDetail.as_view(), name='chara_detail'),
    # 追加、登録(r)と新規作成(c)がある、新規作成ならダイスロールで能力値を決定する
    path('chara/add/<str:r_or_c>/', CharaAdd.as_view(), name='chara_add'),
    # 修正
    path('chara/mod/<int:pk>/<str:what>/', CharaUpdate.as_view(), name='chara_edit'),
    # 削除
    path('chara/del/<int:pk>/', CharaDelete.as_view(), name='chara_del'),
]
