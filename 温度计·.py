from machine import Pin
import utime
from DHT22 import DHT22


dht_sensor=DHT22(Pin(0,Pin.IN,Pin.PULL_UP),dht11=True)
T,H = dht_sensor.read()
t = str(T)
h = str(H)


la=Pin(10,Pin.OUT)
lb=Pin(14,Pin.OUT)
lc=Pin(19,Pin.OUT)
ld=Pin(21,Pin.OUT)
le=Pin(22,Pin.OUT)
lf=Pin(11,Pin.OUT)
lg=Pin(18,Pin.OUT)

l1=Pin(9,Pin.OUT)
l2=Pin(12,Pin.OUT)
l3=Pin(13,Pin.OUT)
l4=Pin(17,Pin.OUT)

l1.value(0)
l2.value(1)
l3.value(1)
l4.value(1)

def fill(a,b):
    l1.value(a)
    l2.value(a)
    l3.value(a)
    l4.value(a)

    la.value(b)
    lb.value(b)
    lc.value(b)
    ld.value(b)
    le.value(b)
    lf.value(b)
    lg.value(b)
def fill1():

    la.value(0)
    lb.value(0)
    lc.value(0)
    ld.value(0)
    le.value(0)
    lf.value(0)
    lg.value(0)
    
def sz1():
    lb.value(1)
    lc.value(1)
def sz2():
    la.value(1)
    lb.value(1)
    lg.value(1)
    le.value(1)
    ld.value(1)
def sz3():
    la.value(1)
    lb.value(1)
    lg.value(1)
    lc.value(1)
    ld.value(1)
def sz4():
    lf.value(1)
    lb.value(1)
    lg.value(1)
    lc.value(1)
def sz5():
    lf.value(1)
    la.value(1)
    lg.value(1)
    lc.value(1)
    ld.value(1)
def sz6():
    lf.value(1)
    la.value(1)
    lg.value(1)
    lc.value(1)
    ld.value(1)
    le.value(1)
def sz7():
    lb.value(1)
    lc.value(1)
    la.value(1)
def sz8():
    lf.value(1)
    la.value(1)
    lg.value(1)
    lc.value(1)
    ld.value(1)
    le.value(1)
    lb.value(1)
def sz9():
    lf.value(1)
    la.value(1)
    lg.value(1)
    lc.value(1)
    ld.value(1)
    lb.value(1)
def sz0():
    lf.value(1)
    la.value(1)
    lc.value(1)
    ld.value(1)
    le.value(1)
    lb.value(1)
    
    
    

    
def t10():
    if t[0] in['0']:
        sz0()
    if t[0] in['2']:
        sz2()
    if t[0] in['3']:
        sz3()
    if t[0] in['4']:
        sz4()
    if t[0] in['5']:
        sz5()
    if t[0] in['6']:
        sz6()
    if t[0] in['7']:
        sz7()
    if t[0] in['8']:
        sz8()
    if t[0] in['9']:
        sz9()
    if t[0] in['1']:
        sz1()
        
        
        
        
def t01():
    if t[-1] in['0']:
        sz0()
    if t[-1] in['2']:
        sz2()
    if t[-1] in['3']:
        sz3()
    if t[-1] in['4']:
        sz4()
    if t[-1] in['5']:
        sz5()
    if t[-1] in['6']:
        sz6()
    if t[-1] in['7']:
        sz7()
    if t[-1] in['8']:
        sz8()
    if t[-1] in['9']:
        sz9()
    if t[-1] in['1']:
        sz1()
    
        
def h10():
    if h[0] in['0']:
        sz0()
    if h[0] in['2']:
        sz2()
    if h[0] in['3']:
        sz3()
    if h[0] in['4']:
        sz4()
    if h[0] in['5']:
        sz5()
    if h[0] in['6']:
        sz6()
    if h[0] in['7']:
        sz7()
    if h[0] in['8']:
        sz8()
    if h[0] in['9']:
        sz9()
    if h[0] in['1']:
        sz1()
    
def h01():
    if h[-1] in['0']:
        sz0()
    if h[-1] in['2']:
        sz2()
    if h[-1] in['3']:
        sz3()
    if h[-1] in['4']:
        sz4()
    if h[-1] in['5']:
        sz5()
    if h[-1] in['6']:
        sz6()
    if h[-1] in['7']:
        sz7()
    if h[-1] in['8']:
        sz8()
    if h[-1] in['9']:
        sz9()
    if h[-1] in['1']:
        sz1()



a = 0        
while True:
    a+=1
    
    if a==1000:
        a = 0
        dht_sensor=DHT22(Pin(0,Pin.IN,Pin.PULL_UP),dht11=True)
        T,H = dht_sensor.read()
        t = str(T)
        h = str(H)
    l1.value(0)
    t10()
    utime.sleep(0.005)
    fill(1,0)
    
    
    
       
    l2.value(0)
    t01()
    utime.sleep(0.005)
    fill(1,0)
    
            
    l3.value(0)
    h10()
    utime.sleep(0.005)
    fill(1,0)
    
    
    r = int(h)
    if r>9:
        r =str(h)
        l4.value(0)
        ho1()
        utime.sleep(0.005)
        fill(1.0)
        
   