from django.shortcuts import render , redirect , get_object_or_404
from .models import Room
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse

@login_required
def room_list_view(request):
    rooms=Room.objects.filter(
        Q(creator=request.user) |
        Q(participants=request.user)
    ).distinct()
    data={'rooms':rooms}
    return render(request,'rooms/room_list.html',data)



@login_required
def room_detail_view(request,pk):
    room=get_object_or_404(Room,id=pk)
    data={'room':room}
    return render(request,'rooms/room_detail.html',data)

@login_required
def delete_room_view(request,pk):
    room=get_object_or_404(Room,id=pk)
    #ensure only the creator can delete it
    if request.user==room.creator:
        room.delete()
        return redirect('room_list')
    else:
        return HttpResponse("you are not allowed to delete this room .")
    

@login_required
def edit_room_view(request,pk):
    room=get_object_or_404(Room,id=pk)
    #ensure only the creator can edit the room
    if room.creator != request.user:
        return HttpResponse("you are not allowed to edit this room .")
    else:
        if request.method=='POST':
            room.name=request.POST.get('room_edited_name')
            room.description=request.POST.get('room_edited_description')
            room.save()
            return redirect('room_list')
    return render(request,'rooms/edit_room.html',{'room':room})




@login_required
def create_room_view(request):
    if request.method=='POST':
        room_name=request.POST.get('name')
        room_description=request.POST.get('description')
        room=Room.objects.create(
            name=room_name,
            description=room_description,
            creator=request.user,#set the creator to the logged in user
        )
        #redirect to the room list after the creation of the room
        return redirect('room_list')
    return render(request,'rooms/create_room.html')


@login_required
def join_room_view(request,pk):
    room=get_object_or_404(Room,id=pk)
    room.participants.add(request.user)
    return redirect('room_list')
