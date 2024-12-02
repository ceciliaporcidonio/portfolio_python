from django.shortcuts import render, get_object_or_404
from .models import Post

# View para listar os posts
def post_list(request):
    posts = Post.objects.all()  # Recupera todos os posts
    return render(request, 'post_list.html', {'posts': posts})

# View para detalhes de um post específico
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Recupera o post pelo ID ou retorna 404
    return render(request, 'post_detail.html', {'post': post})

