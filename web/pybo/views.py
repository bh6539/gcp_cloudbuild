from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Question
import psycopg2
import time

def main(request):
    return render(request, 'base.html')

def board(request):
    return render(request, 'board.html')

def test(request):
    db = psycopg2.connect(host='34.64.201.252', dbname='board',user='postgres',password='test',port=5432)
    cursor = db.cursor()
    #cursor.execute("INSERT INTO board VALUE (5, 'test', 'tttt', '2023-04-21')")
    cursor.execute("SELECT * FROM board")
    data = cursor.fetchall()
    return render(request, 'test.html', {'value' : data})

def Insert_data(request):
    str = "a"
    if request.method == 'POST':
        db = psycopg2.connect(host='34.64.201.252', dbname='board',user='postgres',password='test',port=5432)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM board")
        data = cursor.fetchall()
    
        index = len(data) + 1
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        name = request.POST['name']
        content = request.POST['content']

        cursor.execute("INSERT INTO public.board VALUES(%s, %s, %s, %s)", (index, name, content, date))
        db.commit()
    return redirect('test')
