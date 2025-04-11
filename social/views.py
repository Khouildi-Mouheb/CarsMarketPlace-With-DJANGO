from django.shortcuts import render , redirect,get_object_or_404
from django.http import HttpResponse , HttpResponseForbidden
from .models import Post , Comment
from django.contrib.auth.decorators import login_required
from rooms.models import Room
from django.db.models import Q


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

########################  comment-views   ############################

@login_required
def create_comment_view(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    room=post.room
    creator_queryset=[room.creator]
    participants_queryset=list(room.participants.all())
    members=creator_queryset+participants_queryset
    ids=[participant.id for participant in room.participants.all()]
    ids.append(room.creator.id)
    if request.user.id not in ids:
    #if request.user.id not in room.participants.values_list('id',flat=True) and request.user.id!=room.creator.id and request.user.id!=post.author.id:
        return HttpResponse("you are not allowed to comment on this post !")    
    else:
        if request.method=='POST':
            content=request.POST.get('content')
            post.comments.create(
                author=request.user,
                content=content,
            )
            #redirect to the room
            return redirect('room_detail',pk=post.room.id)
        
    return render(request,'social/create_comment.html',{'post':post})




@login_required
def delete_comment_view(request,comment_id):
    comment=get_object_or_404(Comment,id=comment_id)
    if comment.author!=request.user:
        return HttpResponseForbidden('you are not allowed to delete this comment')
    comment.delete()
    return redirect('room_detail',pk=comment.post.room.id)



@login_required
def edit_comment_view(request,comment_id):
    comment=get_object_or_404(Comment,id=comment_id)
    if comment.author!=request.user:
        return HttpResponseForbidden('you are not allowed to edit this comment')
    
    if request.method=='POST':
        comment.content=request.POST.get('content')
        comment.save()
        return redirect('room_detail',pk=comment.post.room.id)
    return render(request,'social/edit_comment.html',{'comment':comment})