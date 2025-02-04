from django.shortcuts import render
from django.http import HttpResponse
from index.models import Post
from datetime import datetime
from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")
#def homepage(request):
    posts = Post.objects.all()
  #  now = datetime.now()
   # return render(request,"index.html",locals())
    post_lists = list()
    for count,post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count))+str(post)+"<br>")
    return HttpResponse(post_lists)
#

# Create your views here.
