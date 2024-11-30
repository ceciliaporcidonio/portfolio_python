from django.shortcuts import render, redirect
from .forms import CommentForm

def index(request):
    return render(request, 'core/index.html')

def comment_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment')
    else:
        form = CommentForm()
    return render(request, 'core/comment.html', {'form': form})

