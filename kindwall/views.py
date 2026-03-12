from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from django.shortcuts import get_object_or_404




def wall(request):
    
    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('wall')

    else:
        form = MessageForm()

    messages = Message.objects.all().order_by('-created_at')

    message_count = Message.objects.count()

    return render(request, 'kindwall/wall.html', {
        'messages': messages,
        'form': form,
        'message_count': message_count
    })
     
def like_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.likes += 1
    message.save()

    return redirect('wall')