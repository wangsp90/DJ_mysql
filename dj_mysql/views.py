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
#	cursor.execute("insert into book (ID,NAME,PRICE) value (null,'金瓶梅',88)")
	cursor.execute("select * from books")
	rows = cursor.fetchall()
	for row in rows:
		print (row)
	return HttpResponse("Fuck You!")