from django.shortcuts import render
from blog.data import posts

def blog(request):
  print('blog')

  context = {
    'text': 'Estamos da BLOG, estudando',
    'posts': posts
  }
  return render(request,
  'blog/index.html',
  context
  )

def exemplo(request):
  print('exemplo')

  context = {
    'text': 'Estamos em EXEMPLO, estudando',
    'title': 'Página de EXEMPLO - ',
  }
  return render(request,
    'blog/exemplo.html',
    context
  )