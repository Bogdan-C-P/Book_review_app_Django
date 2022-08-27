from django.urls import path
from .views import BookDetail,BookList,ReviewUpdate,deleteReview,loginPage,registerPage,logoutUser
urlpatterns = [
    path('', BookList, name='book_list'),
    path('book_detail/<str:pk>/', BookDetail, name='book_detail'),
    path('review_detail/<str:pk>/', ReviewUpdate, name='review_detail'),
    path('delete_review/<str:pk>/', deleteReview, name='delete_review'),
    path('login/', loginPage,name="login"),
    path('register/', registerPage,name="register"),
    path('logout/', logoutUser,name="logout"),

    #path('review', review_list, name='review_list'),
    #path('review_detail/<int:pk>/', review_detail, name='review_detail'),
]
