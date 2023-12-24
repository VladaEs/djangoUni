from django.urls import path
from . import views

urlpatterns= [
    path('', views.PostView.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comment'),
    path('book_table/', views.bookTable.as_view(), name='booking_page'),
    path('book_review/', views.BookingPost.as_view(), name='booking_table'),
    # path('login/', views.LoginPage.as_view(), name="login"),
    # path('register/', RegisterUser.as_view(), name="register")
    ]