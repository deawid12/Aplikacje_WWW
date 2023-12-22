from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoModelSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required, login_required
from django.core.exceptions import PermissionDenied
from .permissions import IsOwner
def index(request):
    return HttpResponse("Hello, world. You're at the polls index. xd")

@api_view(['GET'])
@permission_classes([DjangoModelPermissions])
def person_list_str(request, zx):
    if request.method == 'GET':
        osoby = Osoba.objects.filter(nazwisko__contains=zx)
        if osoby.exists():
            serializer = OsobaSerializer(osoby, many=True)
            return Response(serializer.data)
        else:
            return  Response("Brak osoby o nazwisku: ", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def person_detail(request,pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

@api_view(['GET'])
@login_required
def person_list(request):
    if request.method == 'GET':
        # Filtruj obiekty Osoba, aby wyświetlić tylko te, które należą do zalogowanego użytkownika
        osoby = Osoba.objects.filter(wlasciciel=request.user)
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

def person_view(request, pk):
    if not request.user.has_perm('polls.view_Osoba'):
        raise PermissionDenied()
    try:
        osoba = Osoba.objects.get(pk=pk)
        if osoba.wlasciciel == request.user or request.user.has_perm('polls.can_view_other_persons'):
            return HttpResponse(f"Nazwa użytkownika: {osoba.imie} {osoba.nazwisko}")
    except Osoba.DoesNotExist:
        return HttpResponse(f"Nie ma użytkownika  o id={pk}.")

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsOwner, IsAuthenticated])
def person_delete(request, pk):
    try:
        person = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@permission_classes([DjangoModelPermissions])
def person_update(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def team_list(request):
    if request.method == 'GET':
        stanowisk = Stanowisko.objects.all()
        serializer = StanowiskoModelSerializer(stanowisk, many=True)
        return Response(serializer.data)
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def team_members(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        osoby = Osoba.objects.filter(stanowisko=stanowisko)
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def team_detail(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(id=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        stanowisko = Stanowisko.objects.get(id=pk)
        serializer = StanowiskoModelSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StanowiskoModelSerializer(stanowisko,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#logowanie
class CustomAuthTokenLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username' : user.username,
        })

def register_user(request):
    try:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        if not (username and email and password):
            return Response({'error': 'Wymagane są wszystkie pola: username, email, password'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username, email, password)
        return Response({'message': 'Użytkownik został zarejestrowany'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)