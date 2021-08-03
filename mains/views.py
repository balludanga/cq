from django.shortcuts import render, get_object_or_404
from .models import Mains

# Create your views here.
def mains(request, pk):
    
    
    mains = get_object_or_404(Mains, id=pk)

    mains.views = mains.views + 1
    mains.save()

    

   

   
    context = {
        'mains': mains,
        
        
        
    }
    return render(request, 'mains-ques.html', context)