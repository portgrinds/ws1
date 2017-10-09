# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.order_by('published_date')
	return render(request, 'WS/post_list.html', {'posts' : posts})

