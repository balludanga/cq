from django.shortcuts import render, get_object_or_404
from .models import Team_member

# Create your views here.
def team(request):
    
    team = Team_member.objects.all()
    
    


    
    context = {
        
        'team' : team,
        
        
    }
    return render(request, 'team.html', context )

def team_member(request, pk):
    
    
    team_member = get_object_or_404(Team_member, id=pk)

    

    

   

   
    context = {
        'team_member': team_member,
        
        
        
    }
    return render(request, 'team_member.html', context)