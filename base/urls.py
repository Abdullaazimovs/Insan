from django.urls import path

from .views import (RegistrationUser, LoginUser, LogoutUser, CategoryListCreateApiView, PortfolioListCreateApiView,
                    PortfolioRetrieveUpdateDestroyApiView, PortfolioBlockListCreateView, PortfolioBlockDetail)

urlpatterns = [
    path('register/', RegistrationUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),

    path('category_list/', CategoryListCreateApiView.as_view(), name='category'),

    path('portfolio_list/', PortfolioListCreateApiView.as_view(), name='portfolio_list'),
    path('portfolio_detail/<int:pk>/', PortfolioRetrieveUpdateDestroyApiView.as_view(), name='portfolio_detail'),

    path('portfolio/<int:portfolio_id>/blocks/', PortfolioBlockListCreateView.as_view(), name='portfolio_block_list'),
    path('portfolio_detail/<int:portfolio_id>/block/<int:block_id>/', PortfolioBlockDetail.as_view(), name="blog_comment_detail"),

]
