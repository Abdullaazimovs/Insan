from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import serializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Category, Portfolio, Block
from .serializers import InsanCategory, UserSerializer, InsanPortfolio, InsanBlock


class RegistrationUser(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginUser(ObtainAuthToken):
    """
        That class shows us Login part
    """
    def post(self, request, *args, **kwargs):
        """
            In that func we get data
            and aunthenticate the data
        """
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            print(token)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutUser(generics.GenericAPIView):
    """
        In that class we should be log in
        and that class responsible for log out
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryListCreateApiView(generics.ListCreateAPIView):
    """
        That class responsible for Creating Category and Showing
    """
    queryset = Category.objects.all()
    serializer_class = InsanCategory

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated()]


class PortfolioRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    """
        That class responsible for Updating Portfolio information
    """

    queryset = Portfolio.objects.all()
    serializer_class = InsanPortfolio
    permission_classes = [IsAuthenticated]


class PortfolioListCreateApiView(generics.ListCreateAPIView):
    """
       That class responsible for Creating and Listing Portfolio information
    """

    queryset = Portfolio.objects.all()
    serializer_class = InsanPortfolio
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = InsanPortfolio(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PortfolioBlockListCreateView(generics.ListCreateAPIView):
    """
        That class responsible for creating Blocks
    """

    queryset = Block.objects.all()
    serializer_class = InsanBlock
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        portfolio_id = self.kwargs.get('portfolio_id')
        return Block.objects.filter(portfolio_id=portfolio_id)

    def perform_create(self, serializer):
        portfolio_id = self.kwargs.get('portfolio_id')
        portfolio = get_object_or_404(Portfolio, id=portfolio_id)
        if Block.objects.filter(portfolio=portfolio, author=self.request.user).exists():
            raise serializers.ValidationError({'Message': 'You have already added comment on this blog'})
        serializer.save(author=self.request.user, portfolio=portfolio)


class PortfolioBlockDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        That class responsible for Updating Retriving and Destroying Blocks
    """
    queryset = Block.objects.all()
    serializer_class = InsanBlock
    permission_classes = [IsAuthenticated]

    def get_object(self):
        block_id = self.kwargs.get('block_id')
        block = get_object_or_404(Block, id=block_id)

        portfolio_id = self.kwargs.get("portfolio_id")
        if block.portfolio.id != portfolio_id:
            raise serializers.ValidationError({"Message": "This comment is not related to the requested blog"},
                                              status=status.HTTP_401_UNAUTHORIZED)
        return block

    def delete(self, request, *args, **kwargs):
        block = self.get_object()
        if block.author != request.user:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"},
                                              status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        block = self.get_object()

        if block.author != request.user:
            raise serializers.ValidationError({"Message": "You are not authorized to perform this action"},
                                              status=status.HTTP_401_UNAUTHORIZED)
        return super().put(request, *args, **kwargs)
