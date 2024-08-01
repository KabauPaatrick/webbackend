from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.
@api_view(['GET'])
def list_comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# get comment by id
@api_view(['GET'])
def details_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)

# create a new comment
@api_view(['POST'])
def create_comment(request):
    serializer = CommentSerializer(data=request.data, many=False)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

# create a new comment
@api_view(['POST', 'PUT'])
def update_comment(request,pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment, data=request.data, many=False)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# create a new comment
@api_view(['DELETE'])
def delete_comment(request,pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()

    return Response('Comment successfully deleted')