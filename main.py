debug=False
ios=True

import os
from appdirs import *
appname = ""
appauthor = "Acme"
a= (user_config_dir(appname, appauthor))
#a2=open(a,'w')
#a2.write('test')
#from os import *

if ios==True:
    HOME = environ.get("HOME", "/")
    BUNDLE = environ.get("KIVY_BUNDLE_ID", "/")
    environ["PYTHON_EGG_CACHE"] = f"{HOME}/Library/Caches/{BUNDLE}"
    config_file=(f"{HOME}/Library/Caches/{BUNDLE}")

if ios==False:
    HOME = os.environ.get("USERPROFILE" )
    BUNDLE = os.environ.get("KIVY_BUNDLE_ID" )
    #os.environ["PYTHON_EGG_CACHE"] = f"{HOME}/Library/Caches/{BUNDLE}"
    config_file=(f"{HOME}"+'/kt/')

#####
####
#####
from kivy.app import App
app = App.get_running_app()
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition,FadeTransition,CardTransition,SwapTransition
from kivy.core.image import Image
from kivy.uix.colorpicker import ColorWheel
from kivy.uix.popup import Popup
import ssl
import kivy.utils
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.textfield import MDTextField
from kivy.uix.image import AsyncImage
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from kivymd.uix.taptargetview import MDTapTargetView

from kivy.core.window import Window
from os.path import expanduser

import json

# some JSON:






ssl.verify = False

f_size=50

from kivy.config import Config
user_g=''
pass_g=''
loc_g=''




def writeuserdata():
    with open(config_file+'data77.txt') as json_file:
        data = json.load(json_file)

    #print (data)
    #print (type(data))
    (data['username'])=user_g
    (data['password'])=pass_g
    (data['city'])=loc_g
    #print (data['username'])
    #data=str(data)
    data = json.dumps(data, indent = 4)  

    #print (data)
    x=open(config_file+'data77.txt','w')
    x.write(data)
    x.close()

def writeuserdata_init():
    global user_g

                                    
    #user=user_g
    if user_g=='':  
        user_g='blankfuck'
    print (user_g,'testtest')
    print (dir(user_g))
    

    x = ' { "username":"test", "password":"30", "city":"lasvegas","ios":"False","usecache":"True","pcolor":"Black","scolor":"White"}'
    y = json.loads(x)
    #y = json.dumps(x)
    with open(config_file+'data77.txt', 'w') as outfile:
        json.dump(y, outfile)
    print ('writedata')

def readuserdata():
    with open(config_file+'data77.txt') as json_file:
        print (json_file)
        data = json.load(json_file)
        username=(data['username'])
        password=(data['password'])
        location=(data['city'])
        isios=(data['ios'])
        usecache=((data['usecache']))
        print (usecache,'usecachewtf')
        pcolor=(data['pcolor'])
        scolor=(data['scolor'])
        return username,password,location,isios,usecache,pcolor,scolor
try:
    temp=open(config_file+'data77.txt','r')
    temp.close()
    
except:
    print ('writing new data')
    writeuserdata_init()

username,password,location,isios,usecache,pcolor,scolor=readuserdata()
user_g=username
pass_g=password
loc_g=location



import webbrowser


import mechanize
from bs4 import BeautifulSoup
w=1125/2
h=2436/2
w=int(w)
h=int(h)
w=str(w)
h=int(h)
w=int(w)
rhino_x_g=w
rhino_y_g=h
try:
    w,g=str.split(w,'.')
except:
    ''
try:
    h,g=str.split(h,'.')
except:
    ''
w=int(w)
h=int(h)

Config.set('graphics', 'width', str(w))
Config.set('graphics', 'height', str(h))
if 1==1:
    #b=open('test.txt','w')
    #b.write('test')
    #b.close()
    #ios=False
    Config.set('graphics', 'width', str(w))
    Config.set('graphics', 'height', str(h))
    Window.size = (w,h)
#except:
#    ios=True

conf=False
mj=[]
mj2=[]
l=[]
index=3
gindex=99
ad=''
au=''
first_color_g=(.0, 0.9, .1, .3)
second_color_g=(.0, 0.8, .1, .3)
#third color text
#first color backgrounds
rhino_color_hex='#f7941c'
first_color_g=kivy.utils.get_color_from_hex('#232323')
second_color_g=kivy.utils.get_color_from_hex('#343434')
third_color_g=kivy.utils.get_color_from_hex('#aaaaaa')
fourth_color_g=kivy.utils.get_color_from_hex('#aaaaaa')
rhino_color_g=kivy.utils.get_color_from_hex(rhino_color_hex)









import os
ssl._create_default_https_context = ssl._create_unverified_context
import emoji

def login(self):
        global usecache

        #app = App.get_running_app()
        #print("app.directory = ", app.directory)
        usecache=bool(usecache)
        print (type(usecache),usecache,'usecache2')
        

        #if usecache==True:
        #    print ('using fake data')
        #if usecache==False:
        print (username,password,location,'lolsecurity')
        #if usecache==False:
        if 1==1:
            print ("using real data")
            ssl.verify = False
            
            


            PE_LOGIN = 'https://www.thinkrhino.com/employee/lasvegas/index.aspx'
            PE_LOGIN = 'https://www.thinkrhino.com/employee/'+location+'/index.aspx'
            PE_COUNTRIES = 'https://www.thinkrhino.com/employee/'+location+'/Schedule.aspx'

            #USERNAME = c.text
            dir_path = os.path.dirname(os.path.realpath(__file__))
            # aaa=open(dir_path+'/test2.html','wb')
            #global browser
            browser = mechanize.Browser()
            
            browser.set_handle_robots(False)
            browser.set_handle_equiv(False)
            browser.addheaders = [('User-agent',
                                'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            browser.open(PE_LOGIN)
            browser.select_form(name="ctl00")
            browser['emailaddress'] = username
            browser['mypassword'] = password

            
            res = browser.submit()

            res = browser.open(PE_COUNTRIES)
            
            aa = res.get_data()  # HTML source of the page

            b2=open(ad+'/4cache.html','wb')
            b2.write(aa)
            
            for i in res.readlines():

                try:
                    if "allrights" in i or 'copyright -' in i or 'ino Women’s Cold Crew P' in i:
                        ##print
                        i, 'copy1'
                        i = ''

                    i = i.encode('utf-8')
                    u = u + (i)
                except:

                    'fauil', i


            parse('junk')
        #except:
        if usecache==True:
            print ('lolfail')
            parse('junk2')



def parse(aa):
    global mj
    global mj2
    global l
    #print ('google')

    l=[]
    
    d=[]
    ti=[]
    j=[]
    s=[]
    v=[]
    l=[]
    l2=[]
    c=[]
    ty=[]
    p=[]
    st=[]
    n=[]
    tk=[]
    pl=[]
    dd={}
    mj=[]
    mj2=[]
    off=[]

    


    if usecache==True:
        print ('asdfasdfasdf')
        aaa=open(ad+'/4cache.html','r')
        print (aaa,'2asdf')
    #if usecache==True:
    #    print ('using cache data')
    #    aaa=open(ad+'/conf.html','r')


    #ab=aaa.read()
    soup = BeautifulSoup(aaa, 'html.parser')

    ab=(soup.find_all('td'))
    dn=15
    dm=dn-1
    
    #for i in range(15,len(ab)-15):
    for i in range(dn,len(ab)-dn):
        asds= str(ab[i].contents)
        if 'input name' not in asds:


            l.append( (ab[i].get_text()))
        


    print (l,'onelasttime')
    
    for z in range(len(l)):


        if z%dm==0:
            d.append(l[z])
        if z%dm==1:
            ti.append(l[z])
        if z%dm==2:
            j.append(l[z])
        if z%dm==3:
            s.append(l[z])
            
        if z%dm==4:
            v.append(l[z])
            
        if z%dm==5:
            l2.append(l[z])
        if z%dm==6:
            c.append(l[z])
        if z%dm==7:
            ty.append(l[z])
        if z%dm==8:
            p.append(l[z])
        if z%dm==9:
            st.append(l[z])
        if z%dm==10:
            n.append(l[z])
        if z%dm==11:
            tk.append(l[z])
        if z%dm==12:
            pl.append(l[z])
        if z%dm==13:
            off.append(l[z])
    print ('lololol',off)



    for q in range(len(d)):
        em=''
        
        if p[q]=="ME":
            print ('omg ME🔌')
            em=em+(emoji.emojize(':electric_plug:'))
        if "L" in p[q]:
            em=em+(emoji.emojize(':light_bulb:'))
        if "V" in p[q]:
            em=em+(emoji.emojize(':television:'))
        if "VGK" in s[q]:
            em=em+(emoji.emojize(':ice_hockey:'))
        if 'MGM' in l[q]:
            em=em+(emoji.emojize(':lion:'))
            
        #mjp.append d[q]
        #mjp.append ti[q]
        print (d[q])
        month='bad'
        date='bad'
        try:
            month,date,year=str.split(d[q],'/')
            month=str(int(month))
            #print (n[q],'wtfyouass')
        except:
            ''
            #print (d[q],'shit')
        try:
            if 'onfirmed' in n[q]:

                #print ('omg its confirmed')
                n[q]='[color='+rhino_color_hex+']'+n[q]+'[/color]'
        except:
            ''
        try:
            print (off(q),'p11')
        except:
            ''
        try:
            showjunk,showreal=str.split(s[q],') ')
        except:
            showreal=s[q]
        #joob='[color=ff3333]'+d[q]+'[/color] '+ti[q]+' ~ '+v[q]+' ~ '+l[q]+' ~ '+ti[q]+' ~  '+c[q]+' ~ '+ty[q]+' ~ '+p[q]+' ~ '+st[q]+' ~ '+j[q]+' ~ '+n[q]
        try:
            joob=d[q]+' '+ti[q]+' ~ '+v[q]+' ~ '+l2[q]+' ~ '+s[q]+' ~ \n '+c[q]+' ~ '+ty[q]+' ~ '+p[q]+' ~ '+st[q]+' ~ '+j[q]+' ~ '+n[q]+ ' ~ '+off[q]
            joob2='[color='+rhino_color_hex+']'+month+'/'+date+'[/color] '+ti[q]+'  '+' \n[b]'+showreal+'[/b]  \n'+v[q]+'\n[size=40]'+ty[q]+'  '+p[q]+em+'  '+st[q]+'  '+n[q]
        except:
            ''
        if 'aken off call' in off[q]:
            joob2="[color=red]"+joob2+' '+off[q]+"[/color]"
            
        
        print (joob)
        mj.append(joob)
        mj2.append(joob2)

        #print (joob)
        #mdict={'text': [mj]}
        #dd.update(mdict)
        #check(joob,d[q],ti[q],v[q],l[q],s[q],ty[q],st[q],p[q],n[q],c[q],em)
    #self.data = [{'text': str(x)} for x in range(10)]
#root.RV.data=5
    #print (dir(App.get_running_app().root.ids),'junk')
    #print (dir(App.get_running_app().root),'lol')
    #print (dir(App.get_running_app().root.get_screen('RVScreen')))
    #$print ((App.get_running_app().root.get_screen('RVScreen').ids))
    #root = App.get_running_app().root
    #print (root.ids.viewkeys)
    #self.data.ids.RVScreen.ids.password.text = str('asdf')
    my_dict = {"name": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
    #print (dd)


Builder.load_string('''
#:import random random.random
#:import webbrowser webbrowser
#:import emoji emoji
#:import Factory kivy.factory.Factory
#:import toast kivymd.toast.toast


<BackgroundColor@Widget>
    #background_color: 1, 1, 1, 1
    #canvas.before:
    #    Color:
    #        rgba: root.background_color
    #    Rectangle:
    #        size: self.size
    #        pos: self.pos
# Now you can simply Mix the `BackgroundColor` class with almost
# any other widget... to give it a background.
<BackgroundLabel@Label+BackgroundColor>
    #background_color: 0, 0, 0, 0



<Info>:
    MDFloatingActionButton:
        id: button
        icon: "plus"
        pos: 10, 10
        #on_release: app.tap_target_start()
<MDC>:

    MDCard:
        focus_behavior: True
        ripple_behavior: True

        orientation: "vertical"
        #padding: "8dp"
        size_hint: None, None
        size: "280dp", "180dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: "Title"
            theme_text_color: "Secondary"
            adaptive_height: True

        MDSeparator:
            height: "1dp"

        MDLabel:
            text: "Body"

    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "280dp", "180dp"
        #pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: "Title"
            theme_text_color: "Secondary"
            adaptive_height: True

        MDSeparator:
            height: "1dp"

        MDLabel:
            text: "Body"

    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "280dp", "180dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: "Title"
            theme_text_color: "Secondary"
            adaptive_height: True

        MDSeparator:
            height: "1dp"

        MDLabel:
            text: "Body"
<CustomScreen>:
    


    #hue: random()
    Image:
        source: 'r.png'
        source: 'rh.jpg'
        size: self.width,self.height
    BoxLayout:
        orientation: "vertical"
        spacing:20,20
        

        Label:
            #background_color: 1, 0, 0, 1
            #color(0,0,1,.6)
            font_size: dp(100)
            text_size: self.size
            halign: 'center'
            valign: 'bottom'
            #text: '[color=ff3333]Think[/color]'
            #text: 'ThINK'
            text: 'think'
            color: root.rhino_color
            markup: True
            #spacing:500
            font_name: 'zuume2.ttf'
        Label:
            text_size: self.size
            valign: 'top'
            halign: 'center'
            font_size: dp(100)
            text: "RHINO"
            #text: (emoji.emojize(":red_heart:"))
            color: root.rhino_color
            font_name: 'zuume2.ttf'
            #spacing:500

    
    BoxLayout:
        #orientation: "horizontal"
        #Button:
        spacing: dp(20)
        padding: dp(40)


        MDFillRoundFlatButton
            #pos: root.rhino_x+dp(50),50
            icon: "tune"
            text: 'Options'
            #size: 150, 50
            #size_hint: None, None
            #pos_hint: {'right':2}
            on_release:
                root.manager.current = 'Options'
        MDFillRoundFlatButton:
            icon: "login"
            #halign: 'center'
            text: 'Schedule'
            text_color: 'white'
            md_bg_color: root.rhino_color

            user_font_size: dp(80)
            on_release: 
                root.manager.transition.direction = 'up'
                #transition=FadeTransition()
                root.manager.current = root.manager.next()

        
<Options>:
    Image:
        source: 'r.png'
        source: 'rh.jpg'
        size: self.width,self.height
    MDBoxLayout:
        #md_bg_color: 0, 1, 1, .5
      ##  canvas.before:
        #    Color:
         #       rgba: .5, .5,.5, .5
          #  Rectangle:
           #     pos: self.pos
            #    size: self.size



    
        #md_bg_color: app.theme_cls.primary_color
        orientation: "vertical"
        #padding: 20,20
        size_hint:(.7,.8)
        h_align: 'center'
        pos_hint: {'center_x': .5}
        
            
        MDCard:
            md_bg_color: .1,.1,.1, .7
            background: "black"
            orientation: "horizontal"
            padding: dp(20)
            #spacing:dp(10)

            BoxLayout:
                
                orientation: "vertical"
                MDLabel:
                    color: app.theme_cls.primary_light
                    text: 'Account:'
                MDSeparator:
                    height: "1dp"
                MDLabel:
                    color: app.theme_cls.primary_light
                    id: un2
                    text: root.username2
                
            MDRaisedButton:
                text: 'Login'
                width: dp(20)
                padding: dp(30),dp(30)
                #on_release: Factory.MyPopup().open()
                #on_release: root.show_popup()
                on_release:root.manager.current = 'LogIn'
            MDRectangleFlatButton:

                text: 'clear'
                width: dp(20),dp(30)
                #padding: dp(30)
        MDCard:
            
            md_bg_color: .1,.1,.1, .7
            padding: dp(20)
            orientation: "horizontal"
            MDLabel:
                color: app.theme_cls.primary_light
                text: 'option1'
                
            MDSwitch:
                width: dp(55)
        MDCard:
            md_bg_color: .1,.1,.1, .9
            padding: dp(20)
            orientation: "horizontal"
            MDLabel:
                color: app.theme_cls.primary_light
                text: 'option2'
                
            MDSwitch:
                width: dp(55)
        MDCard:
            padding: dp(20)
            md_bg_color: .1,.1,.1, .7
            size: '300dp','100dp'
            orientation: "horizontal"
            MDLabel:
                color: app.theme_cls.primary_light
                text: 'option3'
                
            MDSwitch:
                valighn: 'center'
                padding: dp(50),dp(70)
                width: dp(45)
        MDCard:
            md_bg_color: .1,.1,.1, .9
            padding: dp(20)
            orientation: "horizontal"
            MDLabel:
                color: app.theme_cls.primary_light
                text: 'option4'
                
            MDSwitch:
                width: dp(20)
                padding: dp(30)

        BoxLayout:
            
            #orientation: "horizontal"
            #Button:
            spacing: dp(0)
            padding: dp(-40),dp(40)


            #MDFillRoundFlatButton
                #pos: root.rhino_x+dp(50),50
                #icon: "tune"
                #text: 'Options'
                #size: 150, 50
                #size_hint: None, None
                #pos_hint: {'right':2}
                #on_release:
                   # root.manager.current = 'Options'
            MDFillRoundFlatButton:
                icon: "login"
                #halign: 'center'
                text: 'Back2'
                #text_color: root.custom_font_color
                #md_bg_color: root.rhino_color

                user_font_size: dp(80)
                on_release: 
                    root.manager.transition.direction = 'up'
                    #transition=FadeTransition()
                    root.manager.current = 'Think Rhino'
    
<LogIn>:
    Image:
        source: 'r.png'
        source: 'rh.jpg'
        size: self.width,self.height

    #width: dp(300)
    #height:dp(200)
    #size: '30dp','100dp'
    #padding: dp(50)
    #size_hint:(.8, .2)
    #title: 'Login'


    MDBoxLayout:
        orientation: "vertical"
        Label:
        MDBoxLayout:
            md_bg_color: .1,.1,.1, .7
            
            orientation: "vertical"
            size_hint:.9,.97
            spacing: dp(25)
            padding: dp(50)
            pos_hint: {"center_x": .5, "center_y": .1}
            #pos_hint: {"center_x": .5}

            MDBoxLayout:
                
                size_hint:(.8,dp(.38))
                orientation: "horizontal"
                Label:
                    color: app.theme_cls.accent_color
                    text: 'Email:'
                    

                MDTextFieldRect:
                    valign: 'bottom'
                    mode: "fill"
                    fill_color: .5, .5, .5, .9
                    text: root.user_l
                    hint_text: 'EXAMPLE@EXAMPLE.COM'
                    id: email
                    
                    multiline: False
            MDBoxLayout:
                padding: dp(10)
                size_hint:.8,dp(.49)
                orientation: "horizontal"
                Label:
                    color: app.theme_cls.accent_color
                    text: 'Password:'

                #TextInput:
                MDTextFieldRect:

                    valign: 'top'
                    width: dp(100)
                
                    text: root.pass_l
                    hint_text: 'PASSWORD'
                    password: True
                    #text:'blank password'
                    id:pass2
                    
                    multiline: False
                    color_active: app.theme_cls.accent_color
                    normal_color: app.theme_cls.primary_light
                    color_mode: 'accent'
                    helper_text_mode: "on_focus"
                    helper_text: "Color is defined by 'line_color_focus' property"
                    line_color_focus: 1, 0, 1, 1

                
            MDBoxLayout:
                size_hint:.8,.19
                orientation: "horizontal"        
                Label:
                    text: 'Loaction:'
                    color: app.theme_cls.accent_color





                Spinner:
                #MDDropDownItem:
                    values: app.locations
                    id: loc
                    color: app.theme_cls.accent_color
                    text:'location'

        MDBoxLayout:
            padding: dp(40)
            spacing: dp(40)
            orientation: "horizontal"  
            halign: "right"





            pos_hint: { "center_y": .9}      
            MDRectangleFlatButton:
                text: 'Clear'



            
            MDRectangleFlatButton:
                text: "Cancel"
                on_release: root.manager.current = 'Think Rhino'
            MDRaisedButton:
                text: "Save"
                on_release: root.saveconfig()

<SelectableLabel>:


    padding: dp(30),dp(30)
    height: self.texture_size[1]





    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            #size_h: self.size_h

        Color:
            #rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
            #rgba: (.1, .1, .1, 1) if root.font_size > root.ff else (0,0,0, 1)
            rgba: root.first_color if root.font_size > root.ff else root.second_color
        
            
        Rectangle:
            pos: self.pos
            size: self.size

    canvas:
        Color:
            rgba:1,1,1,1
        Line:
            width:1 if self.selected else .01
            rectangle:(self.x,self.y,self.width,self.height)
    
    
    #text_size: self.size
    text_size : self.width, None
    #halign:'left'
    #width: 9000
    markup: True
    
                                    


    #canvas.before:
    #    Color:
    #        rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
    #    Rectangle:
    #        pos: self.pos
    #        size: self.size
<RV>:

    viewclass: 'SelectableLabel'
    id: rv

    SelectableRecycleBoxLayout:
        spacing: dp(15)
        padding: dp(10)
        canvas:
            #backgroundcolorforreal
            Color:
                rgba:0,0,0,.1
            Rectangle:
                pos: self.pos
                size: self.size
            
        #font_size: dp(196)
        default_size: dp(335), dp(20)
        #default_size: 6000, dp(30)
        #default_size_hint: 5000,dp(64)
        size_hint_y: None
        height: self.minimum_height+10
        orientation: 'vertical'
        #multiselect: False
        #touch_multiselect: True
        halign:'left'
        size: 500,9000
        

<RVScreen>:
    canvas:
        Color:
            rgba:0,1,0,1
    text_size : self.width, None
    halign:'left'
    #root.load()
    font_size_hint: dp(20)
    Image:
        id: jpgs
        source: 'rh.jpg'
        size: self.width,self.height
        opacity: 1
    #text_color: 'white'
    #spacing: dp(15)
    #padding: dp(30)


    MDBoxLayout:
    #FloatLayout:
        #text_color: 'white'
        #spacing: dp(105)
        canvas:
            Color:
                rgba:0,1,0,0
        orientation: "vertical"
        #adaptive_height: True
        height:50
        #size:50,50
        RV:
            #padding: dp(30)
            #on_press:   root.manager.current = root.manager.next()
            size: 1500, 50
            
            height:500
            
            
        MDBoxLayout:
            padding: dp(40),dp(20)
            spacing: dp(20)

            adaptive_height: True
            orientation: "horizontal"
            size: 400, 500
            height:20
            default_size: 50,50
            MDFillRoundFlatButton:
                icon: "keyboard-backspace"
                user_font_size: "32sp"
                elevation_normal: 12
                background_normal: ''
                
                #background_color: 1, .9, .4, .1
                text: 'Back'
                size_hint: None, None
                #size: 150,150
                #elevation:50
                adaptive_height: True
                
                on_release: root.manager.current = root.manager.previous()
            MDFillRoundFlatButton:
                icon: "information-outline"
                text: 'Info'
                #root.wow()
                size_hint: None, None
                size: 150,150
                #on_release: root.manager.current = 'Info23'
                on_release:
                    root.wow()
                    root.manager.current = 'menu'

<MenuScreen>:
    canvas:
        Color:
            rgba:0,1,0,1
    text_size : self.width, None
    halign:'left'
    #root.load()
    font_size_hint: dp(20)
    Image:
        id: jpgs
        source: 'ven/tmo.jpg'
        size: self.width,self.height
        opacity: 1
    BoxLayout:
        
        text_size : self.width, None
        halign:'left'
        orientation: "vertical"
        #text_color:'white'
        font_size_hint:19


        Label:
            text_size : self.width, None
            
            halign:'left'
            id: date
            text: root.name


        Label:
            text_size : self.width, None
            halign:'left'
            id: show
            text: root.name

        Label:
            text_size : self.width, None
            halign:'left'
            id: venue
            text: root.name
            markup: True
            on_ref_press:
                webbrowser.open('http://google.com')
                


        Label:
            text_size : self.width, None
            halign:'left'
            id: location
            text: root.name

        Label:
            text_size : self.width, None
            halign:'left'
            id: client
            text: root.name

        Label:
            text_size : self.width, None
            halign:'left'
            id: type
            text: root.name

        Label:
            text_size : self.width, None
            halign:'left'
            id: position
            text: root.name
        Label:
            text_size : self.width, None
            halign:'left'
            id: details
            text: root.name
        Label:
            text_size : self.width, None
            halign:'left'
            id: status
            text: root.name

        Label:
            text_size : self.width, None
            halign:'left'
            id: notes
            text: root.name
            width: 50

        Label:
            text_size : self.width, None
            halign:'left'
            id: tk
            text: root.name
        Label:
            text_size : self.width, None
            halign:'left'
            id: jobid
            text: root.name


        Button:
            text: 'Back-info'
            size_hint: None, None
            size: 150, 50
            on_release: root.manager.current = 'RVScreen'

        Button:
            text: str(root)
            size_hint: None, None
            size: 150, 50
            on_release: root.manager.current = 'RVScreen'
''')





class CustomScreen(Screen):
    hue = NumericProperty(0)

    global rhino_color_g
    global rhino_x_g
    global rhino_y_g
    rhino_color=rhino_color_g

    rhino_x=rhino_x_g/2

    rhino_y=rhino_y_g/2
    if debug==True:

        print ("login")

    def wow(self):
        print ("OMG")

    #def login(self, b, c, d):

    def build(self):
        screen = Builder.load_string(KV)
        self.tap_target_view = MDTapTargetView(
            widget=screen.ids.button,
            title_text="This is an add button",
            description_text="This is a description of the button",
            widget_position="left_bottom",
        )

        return screen

    def tap_target_start(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()
    




    

class Widgets(Screen):
    def btn(self):
        show_popup(self)

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    global index
    global f_size
    global first_color_g
    global second_color_g

    first_color=first_color_g
    second_color=second_color_g
    
    #index = None
    ff=f_size
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        global gindex
        
        self.index = index
        gindex=index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        global gindex
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            #print("selection changed to {0}".format(rv.data[index]))
            #manager.current = manager.previous()
            1
        else:
            #print("selection removed for {0}".format(rv.data[index]))
            1
        gindex=index
        

xxx=[{'text':'hello'},{'text':'bye'}]

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
         
# Driver code
mj = ['a', 1, 'b', 2, 'c', 3]
mj2=(Convert(mj))




class RV(RecycleView):
    
    #global mj
    def __init__(self, **kwargs):
        #global mj
        global gindex
        global ad
        global au
        global third_color_g
        global fourth_color_g

        
        super(RV, self).__init__(**kwargs)
        
        
        app = App.get_running_app()
        print("app.directory = ", app.directory)
        print("app.user_data_dir = ", app.user_data_dir)
        au=app.directory
        ad=app.user_data_dir
        
        login(1)
        #self.data = [{'text': str(x)} for x in range(1)]
        #print (type(mj2),'wtff')
        #self.data=mj2
        self.data = [{'text': str(x),'text':'wow'} for x in range(len(mj))]
        #print (mj2,'MOTHERUFCKER')
        #self.change_line()
        odd=0
        try:
            for i in range(len(mj)):
                odd=odd+1
                self.data[i]={'text': mj2[i]}
                if odd%2==0:
                    pass
                    self.data[i]={'text': mj2[i],'color':third_color_g,'font_size':f_size}
                if odd%2==1:
                    pass
                    self.data[i]={'text': mj2[i],'color':fourth_color_g,'font_size':f_size+.01}

                    print ('DISPLAY DATA')
        except:
            print ('keyerror')
    #login()
    def change_line(self):
        self.data[0] = '101'
        
    #login(1)
    

class RVScreen(Screen):
    def wow(self):
        #global index
        print (gindex,'rvscreen')
        self.infoo={'text': mj2[gindex],'color':'blue','font_size':35}
        self.manager.screens[3].ids.date.text=str( l[(gindex*14)]+' '+l[(gindex*14)+1])
        self.manager.screens[3].ids.jobid.text=l[(gindex*14)+2]
        self.manager.screens[3].ids.show.text=l[(gindex*14)+3]
        self.manager.screens[3].ids.venue.text=l[(gindex*14)+4]
        self.manager.screens[3].ids.venue.text=l[(gindex*14)+4]+'[ref=some]google.com[/ref]'

        self.manager.screens[3].ids.location.text=l[(gindex*14)+5]
        self.manager.screens[3].ids.client.text=l[(gindex*14)+6]
        self.manager.screens[3].ids.type.text=l[(gindex*14)+7]
        self.manager.screens[3].ids.position.text=l[(gindex*14)+8]
        self.manager.screens[3].ids.details.text=l[(gindex*14)+9]
        self.manager.screens[3].ids.status.text=l[(gindex*14)+10]
        self.manager.screens[3].ids.notes.text=l[(gindex*14)+11]
        self.manager.screens[3].ids.tk.text=l[(gindex*14)+12]
        #wimg = Image(self,source='t.jpg')
        print (l[(gindex*14)+4])
        if 'WYNN' in l[(gindex*14)+4]:
            print ('wynn234234')
            self.manager.screens[3].ids.jpgs.source='wynn.jpg'

        if 'PARK' in l[(gindex*14)+4]:
            self.manager.screens[3].ids.jpgs.source='park.jpg'
            print ('park234234')
        if 'MOBILE' in l[(gindex*14)+4]:
            self.manager.screens[3].ids.jpgs.source='tmo.jpg'
        print(self.manager.screens[3].ids)




class Info23(Screen):
    pass
class Info(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class MDC(Screen):
    pass



class LogIn(Screen):
    global user_g
    global pass_g
    global loc_g
    user_l=user_g
    pass_l=pass_g
    loc_l=loc_g

    def saveconfig(self):
        #print ('wowowoow')
        global user_g
        global pass_g
        global loc_g



        xxu=self.manager.get_screen('LogIn').ids.email.text
        xxp=self.manager.get_screen('LogIn').ids.pass2.text
        xxl=self.manager.get_screen('LogIn').ids.loc.text
        print (xxl)

        self.manager.get_screen('Options').ids.un2.text=xxu
        user_g=xxu
        pass_g=xxp
        loc_g=xxl
        writeuserdata()

class Options(Screen):
    global username
    username2=username
    locations=['lasvegas','notlasvegas']

    custom_font_color=(.9,0,.9,.9)
    #color: app.theme_cls.primary_light
    def open_popup(self):
        pops = MyPopup()
        pops.open()
    
    
    
    
    def on_color(self, instance, value):
            print("\non_color:")
            print("\tvalue(rgba)={}".format(value))
            print("\tcolor(rgba)={}".format(instance.color))
            print("\tcolor(hex)={}".format(instance.hex_color))
            print("\tcolor(hsv)={}".format(instance.hsv))

class MenuScreen(Screen):
    print (index)
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        print (gindex,'OMGWTFMAN')
    



class ScreenManagerApp(MDApp):
    rloc=[]
    locations=[]
    locations2=['denver', 'Colorado','dc', 'DC','florida' , 'Florida','georgia' , 'Georgia','indiana' , 'Indiana','kentucky' , 'Kentucky','lasvegas' , 'Las Vegas','losangeles' , 'Los Angeles' ,'louisiana' , 'Louisiana','michigan' , 'Michigan','minnesota' , 'Minnesota','missouri' , 'Missouri','mississippi' , 'Mississippi','montana' , 'Montana','newmexico' , 'New Mexico','northerncalifornia' , 'Northern California' ,'northwest' , 'Northwest','ohio' , 'Ohio','reno' , 'Reno','california' , 'San Diego','southcarolina' , 'South Carolina','tempe' , 'Tempe','memphis' , 'Tennessee','texas' , 'Texas','tucson' , 'Tucson','wisconsin' , 'Wisconsin',]
    
    locations3=['denver', 'dc', 'florida' ,'georgia' , 'indiana' ,'kentucky' , 'lasvegas' ,'losangeles' , 'louisiana' , 'michigan' , 'minnesota' , 'missouri' , 'mississippi' , 'montana' ,'newmexico' , 'northerncalifornia'  ,'northwest' ,'ohio' , 'reno' , 'california' , 'southcarolina' ,'tempe' , 'memphis' , 'texas' , 'tucson' ,'wisconsin'  ]
    for i in range(0,len(locations2),2):
        rloc.append( (locations2[i]))
        locations.append((locations2[i+1]))
    locations=locations3
    def saveconfig(self):
        print ('wowow')
        #((self.root.screens[4].username2))='bob'
        print (dir(self.root.get_screen('Options')))
        #print (username2,'username2')
        print(self.root.get_screen('Options').ids)
    print (rloc,'rloc')
        
    def build(self):
        self.theme_cls.primary_palette = "Orange" 
        
        root = ScreenManager(transition=FadeTransition())
        #sm = ScreenManager(transition=WipeTransition())
        root.add_widget(CustomScreen(name='Think Rhino'))
        root.add_widget(RVScreen(name='RVScreen'))
        root.add_widget(Info23(name='Info23'))
        root.add_widget(MenuScreen(name='menu'))
        root.add_widget(Options(name='Options'))
        root.add_widget(MDC(name='MDC'))
        #root.add_widget(Ytube(name='Ytube'))
        root.add_widget(Info(name='Info'))
        root.add_widget(LogIn(name='LogIn'))
        self.items = [f"Item {i}" for i in range(50)]



        
        return root
        

    

if __name__ == '__main__':
    print (app,'lolz')
    ScreenManagerApp().run()
