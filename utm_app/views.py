from django.shortcuts import render,render_to_response, get_object_or_404
import psycopg2
# from django.views.decorators import csrf
from django.http import HttpResponseRedirect

conn = psycopg2.connect(database="test_smile", user="postgres", password="postgres", host="127.0.0.1", port="5432")
cur=conn.cursor()

def welcome(request):

    cur.execute("Select * from onetable where source=%s order by id",["google"])
    g_p=cur.fetchall()
    cur.execute("Select * from onetable where source=%s order by id",["bing"])
    bing_p=cur.fetchall()
    cur.execute("Select * from onetable where source=%s or source=%s or source=%s or source=%s order by id",["Facebook","facebook","Instagram","instagram"])
    fb_p=cur.fetchall()
    cur.execute("Select * from onetable where source=%s order by id",["Pinterest"])
    pin_p=cur.fetchall()

    return render(request,'utm_app/display.html',
							  {'res1': g_p,'res2': fb_p,'res3': pin_p,'res4': bing_p})

def edit_view(request):

    if request.POST and len(request.POST)==8:
        id_col=int(request.POST.get('id_col'))
        col1=request.POST.get('col1')
        col2=request.POST.get('col2')
        col3=request.POST.get('col3')
        col4=request.POST.get('col4')
        col5=request.POST.get('col5')
        update_list=[col1,col2,col3,col4,col5,id_col]

        cur.execute("update onetable set source=%s,campaign=%s,geo=%s,prospecting_retargeting=%s,brand_nobrand=%s where id=%s"\
                    ,update_list)
        conn.commit()

    return HttpResponseRedirect('/')

