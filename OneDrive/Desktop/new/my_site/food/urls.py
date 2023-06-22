from . import views  # "." (dot) here means "current directory)"
from django.urls import include,path


app_name = 'food'
urlpatterns = [
    # the pattern below works when we type in "  /food/  "
    path('',views.IndexClassView.as_view(),name='index'),

    # the pattern below works when we type in "  /food/1  " OR "  /food/2  " OR "  /food/3  " etc
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),

    path('item/',views.item,name='item'),
    # additems
    path('add',views.CreateItem.as_view(),name='create_item'),
    # edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    # delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'),





    path('testing/',views.testing,name='testing'),
    path('movie/',views.movie,name='movie'),
]