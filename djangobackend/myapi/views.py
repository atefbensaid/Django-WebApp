from rest_framework import generics, status
from .models import User
from .serializers import UserSerializer, RegisterUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login



@api_view()
def hello_world(request):  # returns hello world
    return Response({"message": "Hello, world!"})


@api_view(['GET'])
def usersList(request):  # returns a list of all users OK
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def UserOperations(request, user_pk):
    if request.method == 'GET':  # return a user by id user_pk OK
        try:
            user = User.objects.get(pk=user_pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':  # update a user by id user_pk
        try:
            user = User.objects.get(pk=user_pk)
            serializer = RegisterUserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':  # delete a user by id user_pk OK
        try:
            user = User.objects.get(pk=user_pk)
            user.delete()
            return Response({"message": "User deleted"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message": "Invalid method"}, status=405)


@api_view(['POST'])
def registerUser(request):  # register a user OK
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        phone_number = serializer.validated_data['phone_number']
        preferences = serializer.validated_data['preferences']
        user = User(name=name, email=email, password=password, preferences=preferences, phone_number=phone_number)
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginUser(request):  # login a user
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"message": "User logged in"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)


##############################
#  à faire
##############################


@api_view(['POST'])
def createPost(request):  # takes form data and creates a post NOK
    return Response({"message": "Hello, world!"})


@api_view(['GET'])
def postsList(request):  # returns a list of all posts NOK
    return Response({"message": "Hello, world!"})


@api_view(['GET', 'PUT', 'DELETE'])
def PostOperations(request, post_pk):  # operations on posts: delete, update and get NOK
    return Response({"message": "Hello, world!"})


@api_view(['POST'])
def submitCandidature(request):  # takes form data and PDF and creates candidate and candidacy NOK
    return Response({"message": "Hello, world!"})
