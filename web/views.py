from django.shortcuts import render,redirect,reverse
from django.db import connection

def get_cursor():
	return connection.cursor()

# Create your views here.
def index(request):
	cursor=get_cursor()
	cursor.execute("select * from books.books")
	books=cursor.fetchall()
	context={
		"books":books
		}
	return render(request,'index.html',context=context)

def add_book(request):									 #提交时，csrf认证防攻击防止了，需要初期学习先在setting中注释掉
	if request.method=='GET':
		return render(request,'add_book.html')
	else:
		bookname=request.POST.get("bookname")
		bookprice=request.POST.get("bookprice")
		cursor=get_cursor()
		cursor.execute("INSERT INTO books.books (NAME, PRICE,ID) VALUES ('%s', '%s',null)" % (bookname,bookprice) )		#游标中传递参数的方式
		return redirect(reverse('index'))

def book_info(request,name):
	cursor=get_cursor()
#	cursor.execute("select * from books.books where ID=%s" % id)
	cursor.execute("select * from books.books where NAME='%s'" % name)	
	book_info=cursor.fetchone()
	context={
		"book":book_info
	}
	return render(request,'book_info.html',context=context)

def del_book(request):
	if request.method=='POST':
		name=request.POST.get("name")
		cursor=get_cursor()
		cursor.execute("delete from books where NAME='%s'" % name )		#游标中传递参数的方式
		return redirect(reverse('index'))
	else:
		return render(request,'index')