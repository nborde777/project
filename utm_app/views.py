from django.shortcuts import render,render_to_response, get_object_or_404
import psycopg2
from django.template import RequestContext
conn = psycopg2.connect(database="test_smile", user="postgres", password="postgres", host="127.0.0.1", port="5432")
cur=conn.cursor()

def welcome(request):

    cur.execute("Select * from onetable where source=%s",["google"])
    g_p=cur.fetchall()
    cur.execute("Select * from onetable where source=%s",["bing"])
    bing_p=cur.fetchall()
    cur.execute("Select * from onetable where source=%s or source=%s or source=%s or source=%s",["Facebook","facebook","Instagram","instagram"])
    fb_p=cur.fetchall()
    cur.execute("Select * from onetable where source=%s",["Pinterest"])
    pin_p=cur.fetchall()

    return render(request,'utm_app/display.html',
							  {'res1': g_p,'res2': fb_p,'res3': pin_p,'res4': bing_p})

