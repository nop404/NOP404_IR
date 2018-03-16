# coding=gbk
import wx
import serial
import configparser
import serial.tools.list_ports
import struct
import time
global_ser=serial.Serial()
class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"NOP404_IR V1.0",size=(300,1280))
        panel=wx.Panel(self,-1)
        
        self.ser=global_ser;
        
        self.ser.baudrate=115200
        self.timeout=1
        for n, (portname, desc, hwid) in enumerate(sorted(serial.tools.list_ports.comports())):
            print(portname)
            print(desc)
            print(hwid)
            if(hwid=="USB VID:PID=1A86:7523 SER=5 LOCATION=1-2"):#自动查找串口
                self.ser.port=portname
                print("发现串口%s"%portname)
                
        try:
            self.ser.port="COM8"
            self.ser.open()
            self.ser.close()
            print("打开串口成功:%s"%self.ser.port)
        except:
            print("打开串口失败:%s"%self.ser.port)
        self.config = configparser.ConfigParser()
        self.config.read('remote.ini')        
        print(self.config.sections());
        poswidth=30
        poshight=10
        buttonwidth=60
        buttonhight=30
        self.Current_IR_Mode=""
        self.Btn_IRKEY_POWER = wx.Button(panel, -1, pos=(poswidth,poshight), label="电源", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_MUTE = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*2+poswidth,poshight), label="静音", size=(buttonwidth, buttonhight))

        self.Btn_IRKEY_NUM_1 = wx.Button(panel, -1, pos=(poswidth,(poshight+buttonhight)*1+buttonhight), label="1", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_NUM_2= wx.Button(panel, -1, pos=((poswidth+buttonwidth)*1+poswidth,(poshight+buttonhight)*1+buttonhight), label="2", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_NUM_3 = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*2+poswidth,(poshight+buttonhight)*1+buttonhight), label="3", size=(buttonwidth, buttonhight))


        self.Btn_IRKEY_NUM_4 = wx.Button(panel, -1, pos=(poswidth,(poshight+buttonhight)*2+buttonhight), label="4", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_NUM_5 = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*1+poswidth,(poshight+buttonhight)*2+buttonhight), label="5", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_NUM_6 = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*2+poswidth,(poshight+buttonhight)*2+buttonhight), label="6", size=(buttonwidth, buttonhight))


        self.Btn_IRKEY_NUM_7 = wx.Button(panel, -1, pos=(poswidth,(poshight+buttonhight)*3+buttonhight), label="7", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_NUM_8 = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*1+poswidth,(poshight+buttonhight)*3+buttonhight), label="8", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_NUM_9 = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*2+poswidth,(poshight+buttonhight)*3+buttonhight), label="9", size=(buttonwidth, buttonhight))


        self.Btn_IRKEY_CHANNEL_FAV_LIST = wx.Button(panel, -1, pos=(poswidth,(poshight+buttonhight)*4+buttonhight), label="喜爱", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_NUM_0 = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*1+poswidth,(poshight+buttonhight)*4+buttonhight), label="0", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_CHANNEL_RETURN = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*2+poswidth,(poshight+buttonhight)*4+buttonhight), label="回看", size=(buttonwidth, buttonhight))


        self.Btn_IRKEY_SLEEP = wx.Button(panel, -1, pos=(poswidth,(poshight+buttonhight)*5+buttonhight), label="睡眠", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_PC    = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*1+poswidth,(poshight+buttonhight)*5+buttonhight), label="电脑", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_HDMI  = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*2+poswidth,(poshight+buttonhight)*5+buttonhight), label="高清", size=(buttonwidth, buttonhight))


        self.Btn_IRKEY_AUTOADJUST = wx.Button(panel, -1, pos=(poswidth,(poshight+buttonhight)*6+buttonhight), label="自动", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_INFO = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*2+poswidth,(poshight+buttonhight)*6+buttonhight), label="屏显", size=(buttonwidth, buttonhight))


        self.Btn_IRKEY_UP = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*1+poswidth,(poshight+buttonhight)*7+buttonhight), label="上", size=(buttonwidth, buttonhight))
        

        self.Btn_IRKEY_LEFT = wx.Button(panel, -1, pos=(poswidth,(poshight+buttonhight)*8+buttonhight), label="左", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_SELECT = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*1+poswidth,(poshight+buttonhight)*8+buttonhight), label="确认", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_RIGHT = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*2+poswidth,(poshight+buttonhight)*8+buttonhight), label="右", size=(buttonwidth, buttonhight))


        self.Btn_IRKEY_DOWN = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*1+poswidth,(poshight+buttonhight)*9+buttonhight), label="下", size=(buttonwidth, buttonhight))
       
        self.Btn_IRKEY_MENU = wx.Button(panel, -1, pos=(poswidth,(poshight+buttonhight)*10+buttonhight), label="菜单", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_EXIT = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*2+poswidth,(poshight+buttonhight)*10+buttonhight), label="退出", size=(buttonwidth, buttonhight))

        self.Btn_IRKEY_VOLUME_PLUS = wx.Button(panel, -1, pos=(poswidth,(poshight+buttonhight)*11+buttonhight), label="VOL+", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_INPUT_SOURCE = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*1+poswidth,(poshight+buttonhight)*11+buttonhight), label="输入", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_CHANNEL_PLUS = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*2+poswidth,(poshight+buttonhight)*11+buttonhight), label="CH+", size=(buttonwidth, buttonhight))


        self.Btn_IRKEY_VOLUME_MINUS = wx.Button(panel, -1, pos=(poswidth,(poshight+buttonhight)*12+buttonhight), label="VOL-", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_ZOOM = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*1+poswidth,(poshight+buttonhight)*12+buttonhight), label="缩放", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_CHANNEL_MINUS = wx.Button(panel, -1, pos=((poswidth+buttonwidth)*2+poswidth,(poshight+buttonhight)*12+buttonhight), label="CH-", size=(buttonwidth, buttonhight))


        self.Btn_IRKEY_RED = wx.Button(panel, -1, pos=(poswidth*0.75,(poshight+buttonhight)*13+buttonhight), label="红", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_GREEN = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*1+poswidth)*0.75,(poshight+buttonhight)*13+buttonhight), label="绿", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_YELLOW = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*2+poswidth)*0.75,(poshight+buttonhight)*13+buttonhight), label="黄", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_BLUE = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*3+poswidth)*0.75,(poshight+buttonhight)*13+buttonhight), label="蓝", size=(buttonwidth, buttonhight))

        self.Btn_IRKEY_BACKWARD = wx.Button(panel, -1, pos=(poswidth*0.75,(poshight+buttonhight)*14+buttonhight), label="快退", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_FORWARD  = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*1+poswidth)*0.75,(poshight+buttonhight)*14+buttonhight), label="快进", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_PREVIOUS = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*2+poswidth)*0.75,(poshight+buttonhight)*14+buttonhight), label="上一曲", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_NEXT = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*3+poswidth)*0.75,(poshight+buttonhight)*14+buttonhight), label="下一曲", size=(buttonwidth, buttonhight))


        self.Btn_IRKEY_PLAY = wx.Button(panel, -1, pos=(poswidth*0.75,(poshight+buttonhight)*15+buttonhight), label="播放", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_STOP = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*1+poswidth)*0.75,(poshight+buttonhight)*15+buttonhight), label="停止", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_PICTURE = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*2+poswidth)*0.75,(poshight+buttonhight)*15+buttonhight), label="图像", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_AUDIO = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*3+poswidth)*0.75,(poshight+buttonhight)*15+buttonhight), label="声音", size=(buttonwidth, buttonhight))
        
        self.Btn_IRKEY_AV = wx.Button(panel, -1, pos=(poswidth*0.75,(poshight+buttonhight)*16+buttonhight), label="AV", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_TV = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*1+poswidth)*0.75,(poshight+buttonhight)*16+buttonhight), label="TV", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_VGA = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*2+poswidth)*0.75,(poshight+buttonhight)*16+buttonhight), label="VGA", size=(buttonwidth, buttonhight))
        self.Btn_IRKEY_HDMI = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*3+poswidth)*0.75,(poshight+buttonhight)*16+buttonhight), label="HDMI", size=(buttonwidth, buttonhight))        
        
        self.Btn_IRKEY_USB = wx.Button(panel, -1, pos=(poswidth*0.75,(poshight+buttonhight)*17+buttonhight), label="USB", size=(buttonwidth, buttonhight))
        
        self.Btn_KEY_K0 = wx.Button(panel, -1, pos=(poswidth*0.75,(poshight+buttonhight)*18+buttonhight), label="K0", size=(buttonwidth, buttonhight))
        self.Btn_KEY_K1 = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*1+poswidth)*0.75,(poshight+buttonhight)*18+buttonhight), label="K1", size=(buttonwidth, buttonhight))
        self.Btn_KEY_K2 = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*2+poswidth)*0.75,(poshight+buttonhight)*18+buttonhight), label="K2", size=(buttonwidth, buttonhight))
        self.Btn_KEY_K3 = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*3+poswidth)*0.75,(poshight+buttonhight)*18+buttonhight), label="K3", size=(buttonwidth, buttonhight))            
        
        self.Btn_KEY_K4 = wx.Button(panel, -1, pos=(poswidth*0.75,(poshight+buttonhight)*19+buttonhight), label="K4", size=(buttonwidth, buttonhight))
        self.Btn_KEY_K5 = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*1+poswidth)*0.75,(poshight+buttonhight)*19+buttonhight), label="k5", size=(buttonwidth, buttonhight))
        self.Btn_KEY_K6 = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*2+poswidth)*0.75,(poshight+buttonhight)*19+buttonhight), label="K6", size=(buttonwidth, buttonhight))
        self.Btn_KEY_K7 = wx.Button(panel, -1, pos=(((poswidth+buttonwidth)*3+poswidth)*0.75,(poshight+buttonhight)*19+buttonhight), label="K7", size=(buttonwidth, buttonhight))              
        
        
        
        self.Choice_IR_Mode=wx.Choice(panel, -1,pos=(poswidth,(poshight+buttonhight)*21+buttonhight),size=(4*buttonwidth, 3*buttonhight))
        self.Choice_IR_Mode.Append(self.config.sections())
        self.Choice_IR_Mode.SetSelection(0)
        self.Current_IR_Mode=(self.Choice_IR_Mode.GetStringSelection())
        self.Bind(wx.EVT_CHOICE,self.Event_IR_Mode,self.Choice_IR_Mode)
        
       # self.Remote_Info=wx.TextCtrl(panel, -1,pos=(poswidth,(poshight+buttonhight)*20+buttonhight),size=(4*buttonwidth, 3*buttonhight))
       # self.Remote_Info.SetLabelText("www.nop404.com")
        
        
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_POWER, self.Btn_IRKEY_POWER)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_MUTE, self.Btn_IRKEY_MUTE)

        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_NUM_1, self.Btn_IRKEY_NUM_1)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_NUM_2, self.Btn_IRKEY_NUM_2)   
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_NUM_3, self.Btn_IRKEY_NUM_3)

        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_NUM_4, self.Btn_IRKEY_NUM_4)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_NUM_5, self.Btn_IRKEY_NUM_5)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_NUM_6, self.Btn_IRKEY_NUM_6)

        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_NUM_7, self.Btn_IRKEY_NUM_7)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_NUM_8, self.Btn_IRKEY_NUM_8)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_NUM_9, self.Btn_IRKEY_NUM_9)

        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_CHANNEL_FAV_LIST, self.Btn_IRKEY_CHANNEL_FAV_LIST)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_NUM_0, self.Btn_IRKEY_NUM_0)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_CHANNEL_RETURN, self.Btn_IRKEY_CHANNEL_RETURN)
    
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_SLEEP, self.Btn_IRKEY_SLEEP)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_PC, self.Btn_IRKEY_PC)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_HDMI, self.Btn_IRKEY_HDMI)
        
    
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_AUTOADJUST, self.Btn_IRKEY_AUTOADJUST)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_INFO, self.Btn_IRKEY_INFO)
        
    
       
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_UP, self.Btn_IRKEY_UP)
      
        
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_LEFT, self.Btn_IRKEY_LEFT)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_SELECT, self.Btn_IRKEY_SELECT)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_RIGHT, self.Btn_IRKEY_RIGHT)
        
        
       
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_DOWN, self.Btn_IRKEY_DOWN)
       
        
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_MENU, self.Btn_IRKEY_MENU)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_EXIT, self.Btn_IRKEY_EXIT)
        
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_VOLUME_PLUS,self.Btn_IRKEY_VOLUME_PLUS)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_INPUT_SOURCE, self.Btn_IRKEY_INPUT_SOURCE)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_CHANNEL_PLUS, self.Btn_IRKEY_CHANNEL_PLUS)
        
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_VOLUME_MINUS, self.Btn_IRKEY_VOLUME_MINUS)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_ZOOM, self.Btn_IRKEY_ZOOM)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_CHANNEL_MINUS, self.Btn_IRKEY_CHANNEL_MINUS)
        
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_RED, self.Btn_IRKEY_RED)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_GREEN, self.Btn_IRKEY_GREEN)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_YELLOW, self.Btn_IRKEY_YELLOW)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_BLUE, self.Btn_IRKEY_BLUE)
        
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_BACKWARD, self.Btn_IRKEY_BACKWARD)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_FORWARD, self.Btn_IRKEY_FORWARD)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_PREVIOUS, self.Btn_IRKEY_PREVIOUS)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_NEXT, self.Btn_IRKEY_NEXT)
        
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_PLAY, self.Btn_IRKEY_PLAY)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_STOP, self.Btn_IRKEY_STOP)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_PICTURE, self.Btn_IRKEY_PICTURE)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_AUDIO, self.Btn_IRKEY_AUDIO)      
        
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_AV, self.Btn_IRKEY_AV)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_TV, self.Btn_IRKEY_TV)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_VGA, self.Btn_IRKEY_VGA)
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_HDMI, self.Btn_IRKEY_HDMI)   
        
        self.Bind(wx.EVT_BUTTON, self.Event_IRKEY_USB, self.Btn_IRKEY_USB)   
        
        
        self.Bind(wx.EVT_BUTTON, self.Event_KEY_K0, self.Btn_KEY_K0) 
        self.Bind(wx.EVT_BUTTON, self.Event_KEY_K1, self.Btn_KEY_K1) 
        self.Bind(wx.EVT_BUTTON, self.Event_KEY_K2, self.Btn_KEY_K2) 
        self.Bind(wx.EVT_BUTTON, self.Event_KEY_K3, self.Btn_KEY_K3) 
        self.Bind(wx.EVT_BUTTON, self.Event_KEY_K4, self.Btn_KEY_K4) 
        self.Bind(wx.EVT_BUTTON, self.Event_KEY_K5, self.Btn_KEY_K5) 
        self.Bind(wx.EVT_BUTTON, self.Event_KEY_K6, self.Btn_KEY_K6) 
        self.Bind(wx.EVT_BUTTON, self.Event_KEY_K7, self.Btn_KEY_K7) 
        
        
    
     
    def Event_IR_Mode(self,event):
        self.Current_IR_Mode=(self.Choice_IR_Mode.GetStringSelection())
        
    def Event_IRKEY_POWER(self, event): 
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_POWER")
       

    def Event_IRKEY_MUTE(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_MUTE")

    def Event_IRKEY_NUM_1(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_NUM_1")
    def Event_IRKEY_NUM_2(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_NUM_2")
    def Event_IRKEY_NUM_3(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_NUM_3")


    def Event_IRKEY_NUM_4(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_NUM_4")
    def Event_IRKEY_NUM_5(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_NUM_5")
    def Event_IRKEY_NUM_6(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_NUM_6")

    def Event_IRKEY_NUM_7(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_NUM_7")
    def Event_IRKEY_NUM_8(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_NUM_8")
    def Event_IRKEY_NUM_9(self, event):  
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_NUM_9")

    def Event_IRKEY_CHANNEL_FAV_LIST(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_CHANNEL_FAV_LIST")
    def Event_IRKEY_NUM_0(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_NUM_0")
    def Event_IRKEY_CHANNEL_RETURN(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_CHANNEL_RETURN")
        
    def Event_IRKEY_SLEEP(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_SLEEP")
    def Event_IRKEY_PC(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_PC")
    def Event_IRKEY_HDMI(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_HDMI")  
        
    def Event_IRKEY_AUTOADJUST(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_AUTOADJUST")
    def Event_IRKEY_INFO(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_INFO")
        
    def Event_IRKEY_UP(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_UP")
        
    def Event_IRKEY_LEFT(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_LEFT")        
    def Event_IRKEY_SELECT(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_SELECT")      
    def Event_IRKEY_RIGHT(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_RIGHT")         
    
    def Event_IRKEY_DOWN(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_DOWN")   
        
    def Event_IRKEY_MENU(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_MENU")      
    def Event_IRKEY_EXIT(self, EXIT):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_EXIT")   
        
    def Event_IRKEY_VOLUME_PLUS(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_VOLUME_PLUS") 
    def Event_IRKEY_INPUT_SOURCE(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_INPUT_SOURCE") 
    def Event_IRKEY_CHANNEL_PLUS(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_CHANNEL_PLUS")     
    
    def Event_IRKEY_VOLUME_MINUS(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_VOLUME_MINUS") 
    def Event_IRKEY_ZOOM(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_ZOOM") 
    def Event_IRKEY_CHANNEL_MINUS(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_CHANNEL_MINUS")          
        
    def Event_IRKEY_RED(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_RED") 
    def Event_IRKEY_GREEN(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_GREEN") 
    def Event_IRKEY_YELLOW(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_YELLOW")   
    def Event_IRKEY_BLUE(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_BLUE")           
        
    def Event_IRKEY_BACKWARD(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_BACKWARD") 
    def Event_IRKEY_FORWARD(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_FORWARD") 
    def Event_IRKEY_PREVIOUS(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_PREVIOUS")   
    def Event_IRKEY_NEXT(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_NEXT")           
    
    def Event_IRKEY_PLAY(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_PLAY") 
    def Event_IRKEY_STOP(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_STOP") 
    def Event_IRKEY_PICTURE(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_PICTURE")   
    def Event_IRKEY_AUDIO(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_AUDIO")           
        
    def Event_IRKEY_AV(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_AV") 
    def Event_IRKEY_TV(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_TV") 
    def Event_IRKEY_VGA(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_VGA")   
    def Event_IRKEY_HDMI(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_HDMI")    
        
    def Event_IRKEY_USB(self, event):
        self.Send_IRKEY(self.Current_IR_Mode,"IRKEY_USB")           
   
   
    def Event_KEY_K0(self, event):
        self.Send_KEY("0")  
    def Event_KEY_K1(self, event):
        self.Send_KEY("1") 
    def Event_KEY_K2(self, event):
        self.Send_KEY("2") 
    def Event_KEY_K3(self, event):
        self.Send_KEY("3") 
    def Event_KEY_K4(self, event):
        self.Send_KEY("4") 
    def Event_KEY_K5(self, event):
        self.Send_KEY("5") 
    def Event_KEY_K6(self, event):
        self.Send_KEY("6") 
    def Event_KEY_K7(self, event):
        self.Send_KEY("7") 

        
        
    def Send_KEY(self,keyname):
        if(self.ser.isOpen()==False):
            self.ser.open()
        try:
            tmp=keyname.encode();
        except:
            print("获取配置失败:"+keyname)
        tmp+=('\n'.encode())
        self.ser.write(tmp)  
       
    
    def Send_IRKEY(self,remotename,irkeyname):
        if(self.ser.isOpen()==False):
            self.ser.open()
      
        #tmp=bytes().fromhex(self.config.get(remotename,irkeyname)) #字符串转换为bytes
        tmp=(self.config.get(remotename,'head_code').encode())
        
        try:
            tmp+=(self.config.get(remotename,irkeyname).encode())
        except:
            print("获取配置失败:"+irkeyname)
        tmp+=('\n'.encode())
        self.ser.write(tmp)  
        print(irkeyname)
        print(self.config.get(remotename,irkeyname))
        
      
        
class MyApp(wx.App):
    def OnInit(self):
        Frame=TextFrame()
        Frame.Show(True)
        return  True
        
def main():
    app=MyApp()
    app.MainLoop()
if __name__=="__main__":
    main()

