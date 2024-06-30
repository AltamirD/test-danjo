from django.shortcuts import render

def home(request):
  print('home')

  context = {
    'text': 'Estamos da HOME, estudando'
  }

  return render(request,
  'home/index.html',
    context,
  )

# def home(request):
#   print('home')
#   return render(request,
#                 'global/base.html'
#   )