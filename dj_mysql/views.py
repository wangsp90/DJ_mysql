#encoding:utf-8

from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.db import connection


#HttpResponse template
#def news_list(request):
#	return HttpResponse("新闻列表")

def index(request):
#	context={"tpm":"This is DTL parameter test!","names":["wangsp","Jane"],"age":16}
	cursor=connection.cursor()
	cursor.execute("insert into book (ID,Name,author) value (null,'简爱','忘了')")
	return render(request,'index.html')