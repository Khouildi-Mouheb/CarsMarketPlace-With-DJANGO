from django.shortcuts import render , redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from rooms.models import Room


@login_required
def create_post_view(request,pk):
    #fetch the specific room
    room=get_object_or_404(Room,id=pk)
    if request.method=='POST':
        content=request.POST.get('content')
        Post.objects.create(
            room=room,
            author=request.user,
            content=content,
        )
        #redirect to the room
        return redirect('room_detail',pk=room.id)
    return render(request,'social/create_post.html',{'room':room})



@login_required
def delete_post_view(request,pk):
    post=get_object_or_404(Post,id=pk)
    if post.author!=request.user:
        return HttpResponse('you are not allowed to delete this post')
    post.delete()
    return redirect('room_detail',pk=post.room.id)


@login_required
def edit_post_view(request,pk):
    post=get_object_or_404(Post,id=pk)
    if post.author!=request.user:
        return HttpResponse ('you are not allowed to edit this post')
    
    if request.method=='POST':
        post.content=request.POST.get('content')
        post.save()
        return redirect('room_detail',pk=post.room.id)
    return render(request,'social/edit_post.html',{'post':post})