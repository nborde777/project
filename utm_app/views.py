from django.shortcuts import render,render_to_response, get_object_or_404
import psycopg2
from django.template import RequestContext
conn = psycopg2.connect(database="test_smile", user="postgres", password="postgres", host="127.0.0.1", port="5432")
cur=conn.cursor()

def welcome(request):
    res={}
    cur.execute("Select * from google_params")
    g_p=cur.fetchall()
    cur.execute("Select * from facebook_params")
    fb_p=cur.fetchall()
    cur.execute("Select * from pinterest_params")
    pin_p=cur.fetchall()
    cur.execute("Select * from bing_params")
    bing_p=cur.fetchall()
    res['google_params']=g_p
    res['google_params']=fb_p
    res['google_params']=pin_p
    res['google_params']=bing_p

    return render(request,'utm_app/display.html',
							  {'res1': g_p,'res2': fb_p,'res3': pin_p,'res4': bing_p})

