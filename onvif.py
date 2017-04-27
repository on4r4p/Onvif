#!/usr/bin/python3
# coding: utf8
from tabulate import tabulate
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import sys

UserAgent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/51.0']


host = input('Set ip host : ')
user = input('Set Username : ')
passwd = input('Set Password : ')

options = ''

while options != "0":

     print(tabulate([['==FTP== :','1) Get Ftp Infos.' ,'2) Set Ftp Infos.','3) Test Ftp.'],[''],['==User== :','4) Get Users Infos.' ,'5) Set Users Infos.'],[''],['==System== :','6) Get Server Infos.' ,'7) Get Server Time.','8) Set Server Time.','9) Get Ntp Infos.','10) Set Ntp Infos.','11) Get Device infos.','12) Set Device infos.','13) Set size snapshot.','14) Reboot Device.','15) Reset Device.','16) Get Logs.','17) Delete Logs.'],[''],['==PTZ== :','18) Move Up.' ,'19) Move Down.','20) Move Left.','21) Move Right.'],[""],['==Motion Detection== :','22) Get Alarm Infos' ,'23) Set Alarm Detections.','24) Get Motion Detections Infos.','25) Set Motion Detections Infos.'],[''],['==Video/Audio==','26) Get Video Infos.','27) Get Image Infos','28) Set Video Infos','29) Set Image Infos','30) Get Overlay Attribute Time','31) Get Overlay Attribute Name','32) Set Overlay Attribute Time','33) Set Overlay Attribute Name','34) Get Volume Out .','35) Set Volume Out','36) Get Volume In','37) Set Volume In.'],[''],['==Infra Red==','38) Get Ir infos.','39) Set Ir Infos.'],[''],["==Network==",'40) Get Network Infos.','41) Get Onvif Infos.','42) Get Rtsp Port.'],['==Exit== :','0)Exit.']]))

     options = input('Please choose an option : ')


     if options  == "1":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getftpattr&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)
               print()

     if options  == "2":

          print("\nExample:\n")
          print("-ft_server=220.112.14.173&-ft_port=21&-ft_username=FTPUsername&-ft_password=FTPPassword&-ft_dirname=ProgramFiles&-ft_mode=1")
          cmd = input("\nEnter cmd :\n")
          
          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setftpattr&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)



     if options  == "3":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=testftp&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)


     if options  == "4":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getuserattr&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)



     if options  == "5":

          print("\nExample:\n")
          print("-at_username=admin&-at_password=instar")
          cmd = input("\nEnter cmd :\n")
          
          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setuserattr&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)



     if options  == "6":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getserverinfo&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)

     if options  == "7":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getservertime&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)



     if options  == "8":

          print("\nExample:\n")
          print("-time=2011.08.23.10.35.08&-timezone=Asia%2FHong_Kong&-dstmode=off")
          cmd = input("\nEnter cmd :\n")
          
          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setservertime&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)


     if options  == "9":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getntpattr&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()


     if options  == "10":

          print("\nExample:\n")
          print("-ntpenable=1&-ntpinterval=2&-ntpserver=time.nist.gov")
          cmd = input("\nEnter cmd :\n")
          
          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setservertime&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)



     if options  == "11":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getdevices&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()

     if options  == "12":

          print("\nExample:\n")
          print("-d_number=0&-d_alias=test1&-d_host=192.168.1.7&-d_port=80&-d_username=admin&-d_password=admin")
          cmd = input("\nEnter cmd :\n")
          
          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setdevices&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)

     if options  == "13":

          print("\nExample:\n")
          print("-chn=011 or -chn=012 or -chn=013")
          cmd = input("\nEnter cmd :\n")
          
          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setservertime&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)



     if options  == "14":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/sysreboot.cgi&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()   
               print(soup.get_text())
               print()
          except Exception as e:
               print()

     if options  == "15":

          try:
               ask =''
               while ask.lower() != "y" or ask.lower() != "n": 
                    ask = input("Are you sure you want to reset the device ?? Y/n")
               if ask.lower() == "y":


                    query = "http://"+str(host)+'/cgi-bin/hi3510/sysreset.cgi&usr='+str(user)+'&pwd='+str(passwd)
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-Agent', str(UserAgent))]
                    send = opener.open(query)
                    soup = BeautifulSoup(send,'lxml')
                    print()   
                    print(soup.get_text())
                    print()
          except Exception as e:
               print()



     if options  == "16":

          try:
               query = "http://"+str(host)+'/log/syslog.txt'
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()   
               print(soup.get_text())
               print()
          except Exception as e:
               print()



     if options  == "17":

          try:
               ask =''
               while ask.lower() != "y" or ask.lower() != "n": 
                    ask = input("Are you sure you want to delete the logs ?? Y/n")
               if ask.lower() == "y":


                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=cleanlog&-name=sys&usr='+str(user)+'&pwd='+str(passwd)
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-Agent', str(UserAgent))]
                    send = opener.open(query)
                    soup = BeautifulSoup(send,'lxml')
                    print()   
                    print(soup.get_text())
                    print()
          except Exception as e:
               print()


     if options  == "18":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/ptzup.cgi?&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)

     if options  == "19":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/ptzdown.cgi?&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)


     if options  == "20":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/ptzleft.cgi?&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)

     if options  == "21":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/ptzright.cgi?&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)

     if options  == "22":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getmdalarm&-aname=email&cmd=getmdalarm&-aname=emailsnap&cmd=getmdalarm&-aname=ftpsnap&cmd=getmdalarm&-aname=snap&cmd=getmdalarm&-aname=emailrec&cmd=getmdalarm&-aname=record&cmd=getmdalarm&-aname=ftprec&cmd=getmdalarm&-aname=relay&-aname=server&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)


     if options  == "23":

          print("\nExample:\n")
          print("-aname=type&-switch=on&cmd=setmdalarm&-aname=email&-switch=on&cmd=setmdalarm&-aname=snap&-switch=on&cmd=setmdalarm&-aname=record&-switch=on&cmd=setmdalarm&-aname=ftprec&-switch=on&cmd=setmdalarm&-aname=relay&-switch=on&cmd=setmdalarm&-aname=ftpsnap&-switch=on")
          cmd = input("\nEnter cmd :\n")
          
          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setmdalarm&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)



     if options  == "24":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getmdattr'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)

     if options  == "25":

          print("\nExample:\n")
          print("-enable=1&-s=50&-name=1&-x=0&-y=0&-w=60&-h=60")
          cmd = input("\nEnter cmd :\n")

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setmdattr&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)



     if options  == "26":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getvideoattr'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)


     if options  == "27":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getimageattr'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)

     if options  == "28":

          print("\nExample:\n")
          print("-vinorm=N")
          cmd = input("\nEnter cmd :\n")

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setvideoattr&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)






     if options  == "29":

          print("\nExample:\n")
          print("-brightness=1&-saturation=1&-contrast=1&-hue=1&-flip=on&-mirror=on&-scene=indoor&")
          cmd = input("\nEnter cmd :\n")

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setimageattr&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)



     if options  == "30":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getoverlayattr&-region=0'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)

     if options  == "31":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getoverlayattr&-region=1'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error: ",e)



     if options  == "32":

          print("\nExample:\n")
          print("-show=0")
          cmd = input("\nEnter cmd :\n")

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setoverlayattr&-region=0&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)

     if options  == "33":

          print("\nExample:\n")
          print("-show=0")
          cmd = input("\nEnter cmd :\n")

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setoverlayattr&-region=1&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)


     if options  == "34":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getaudioinvolume'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)

     if options  == "35":

          print("\nExample:\n")
          print("-volume=80")
          cmd = input("\nEnter cmd :\n")

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setaudioinvolume&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)

     if options  == "36":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getaudiooutvolume'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)

     if options  == "37":

          print("\nExample:\n")
          print("-volume=80")
          cmd = input("\nEnter cmd :\n")

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setaudiooutvolume&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)

     if options  == "38":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getinfrared'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)

     if options  == "39":

          print("\nExample:\n")
          print("auto, open and close")
          cmd = input("\nEnter cmd :\n")

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setinfrared&-infraredstat='+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)


     if options  == "40":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getnetattr'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)

     if options  == "41":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getonvifattr'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)

     if options  == "42":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getrtspport'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)


     if options == "0":

          print("\nBye")
          sys.exit()
