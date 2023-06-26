from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAuthorOnly

# Create your views here.


class PostListCreateView(GenericAPIView):
    permission_classes = [IsAuthorOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(author=self.request.user)

            response = {
                "message": "Blog post created",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        posts = self.get_queryset()

        serializer = self.serializer_class(instance=posts, many=True)

        response = {
            "message": "These are all the posts",
            "data": serializer.data
        }

        return Response(data=response, status=status.HTTP_200_OK)


class PostRetriveDeleteUpdateView(GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOnly]
    queryset = Post.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get(self, request: Request, id: int):
        post = get_object_or_404(self.get_queryset(), id=id)

        serializer = self.serializer_class(instance=post)

        response = {
            "message": "Post with particular id",
            "data": serializer.data
        }

        return Response(data=response, status=status.HTTP_200_OK)

    def put(self, request: Request, id: int):
        post = get_object_or_404(self.get_queryset(), id=id)
        data = request.data

        serializer = self.serializer_class(instance=post, data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "Post has been updated",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_202_ACCEPTED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int):
        post = get_object_or_404(self.get_queryset(), id=id)

        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PublicPosts(GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get(self, request: Request):
        posts = Post.objects.all()

        serializer = self.serializer_class(instance=posts, many=True)

        response = {
            "message": "These are all the posts for the public",
            "data": serializer.data
        }

        return Response(data=response, status=status.HTTP_200_OK)
