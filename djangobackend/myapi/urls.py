from django.urls import path
from .views import UserOperations, hello_world, usersList, registerUser, loginUser, submitCandidature, postsList, \
    PostOperations, createPost

urlpatterns = [

    path('hello', hello_world, name='user-hello_world'),
    path('register', registerUser, name='register User'),
    path('login', loginUser, name='login user'),
    path('users', usersList, name='users List'),
    path('user/<uuid:user_pk>', UserOperations, name='user Operations'),
    path('createpost', createPost, name='create Post'),
    path('<uuid:post_pk>', submitCandidature, name='submit Candidature'),
    path('<posts>', postsList, name='posts List'),
    path('post/<uuid:post_pk>', PostOperations, name='post Operations'),

]
