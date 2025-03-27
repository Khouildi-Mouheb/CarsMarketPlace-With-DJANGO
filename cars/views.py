from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Car ,Wishlist
from .forms import CarCreationForm
from django.contrib import messages
from django.db.models import Q


def car_shop_view(request):
    #"q":is the name of the input and "query":is the value of the search input
    query=request.GET.get('q')#retrieves the search term from the url query parameter
    if query:
        cars=Car.objects.filter(
            #Q allows to perform complexe queries , like searching multiple fields
            Q(model__icontains=query)|#search by title
            Q(description__icontains=query)#serch by description
        )
    else:
        #fetch all cars from the database
        cars=Car.objects.all()
    data={'cars':cars,'query':query}
    return render(request,'cars/car_shop.html',data)




def car_detail_view(request,pk):
    car=get_object_or_404(Car,id=pk)
    #fetch the related cars with the same engine type and exclude the current car
    related_cars=Car.objects.filter(type=car.type).exclude(id=car.id)[:5]
    data={'car':car,'related_cars':related_cars}
    return render(request,'cars/car_detail.html',data)


@login_required
def add_car(request):
    if request.method=='POST':
        form=CarCreationForm(request.POST,request.FILES)
        if form.is_valid():
            car=form.save(commit=False)
            #assign the logged_in user to the seller
            car.owner=request.user
            car.save()
            #redirect to the car shop
            return redirect('car_shop')
    else:
        form=CarCreationForm()
    
    return render(request,'cars/add_car.html',{'form':form})


@login_required
def delete_car_view(request,pk):
    #ensure the car bellong to the logged-in user
    car=get_object_or_404(Car,id=pk,owner=request.user)
    data={'car':car}
    if request.method=='POST':
        car.delete()
        messages.success(request,'Car deleted successfully !')
        return redirect('dashbord')
    return render(request,'cars/confirm_delete_car.html',data)


@login_required
def edit_car_view(request,pk):
    car=get_object_or_404(Car,id=pk,owner=request.user)
    if request.method=='POST':
        #the the existing car data to the form for the editing
        form=CarCreationForm(request.POST,request.FILES,instance=car)
        if form.is_valid():
            form.save()
            return redirect('dashbord')
    else:
        form=CarCreationForm(instance=car)
    return render(request,'cars/edit_car.html',{'form':form,'car':car})


@login_required
def wishlist_view(request):
    Wishlist_items=Wishlist.objects.filter(user=request.user)
    cars_number=Wishlist_items.count()
    data={'Wishlist_items':Wishlist_items,'cars_number':cars_number}
    return render(request,'cars/wishlist.html',data)


@login_required
def add_to_wishlist_view(request,pk):
    #get the car
    car=get_object_or_404(Car,id=pk)
    #add to the wishlist
    #the wishlist item is an object
    wishlist_item , created=Wishlist.objects.get_or_create(
        user=request.user,
        car=car,
        )
    if created:
        messages.success(request,f"{car.model} is added to the wishlist")
    else:
        messages.info(request,f"{car.model} is already in your wishlist")
    return redirect('car_detail',pk=car.id)
    

@login_required
def remove_from_wishlist_view(request,pk):
    car_to_remove=get_object_or_404(Car,id=pk)
    #get the wishlist item to remove it
    Wishlist_item=Wishlist.objects.filter(user=request.user,car=car_to_remove)
    if Wishlist_item:
        Wishlist_item.delete()
        messages.success(request,f"{car_to_remove.model} has been removed")
    else:
         messages.success(request,f"{car_to_remove.model} was not in your wishlist")
    return redirect('wishlist')

