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

     print(tabulate([['==FTP== :','1) Get Ftp Infos.' ,'2) Set Ftp Infos.','3) Test Ftp.'],[''],['==User== :','4) Get Users Infos.' ,'5) Set Users Infos.'],[''],['==System== :','6) Get Server Infos.' ,'7) Get Server Time.','8) Set Server Time.','9) Get Ntp Infos.','10) Set Ntp Infos.','11) Get Device infos.','12) Set Device infos.','13) Reboot Device.','14) Reset Device.','15) Get Logs.','16) Delete Logs.'],[''],['==PTZ== :','17) Move Up.' ,'18) Move Down.','19) Move Left.','20) Move Right.','Rue) Go to center.','Marcel) Go to Marcel.','Garage) Go to garage.','Chemin) Go to Chemin.','Chemin2) Go to Chemin2.','Mamie) Go to Mamie.','SetRue) Set center.','SetMarcel) Set Marcel.','SetGarage) Set garage.','SetChemin) Set Chemin.','SetChemin2) Set Chemin2.','SetMamie) Set Mamie.',],[""],['==Motion Detection== :','21) Get Alarm Infos' ,'22) Set Alarm Detections.','23) Get Motion Detections Infos.','24) Set Motion Detections Infos.','25) Get Alarm Snap Count.','26) Set Alarm Snap Count.','27) Get Snapshot Infos','28) Set Snapshot Infos'],[''],['==Video==','29) Get Video Infos.','30) Get Image Infos','31) Set Video Infos','32) Set Image Infos','33) Get Overlay Attribute Time','34) Get Overlay Attribute Name','35) Set Overlay Attribute Time','36) Set Overlay Attribute Name','37) Get Video Encoder Info','38) Set Video Encoder Info'],[''],['==Audio==','39) Get Volume Out .','40) Set Volume Out','41) Get Volume In','42) Set Volume In.'],[''],['==Infra Red==','43) Get Ir infos.','44) Set Ir Infos.'],[''],["==Network==",'45) Get Network Infos.','46) Get Onvif Infos.','47) Get Rtsp Port.'],['==Exit== :','0)Exit.']]))

     options = input('Please choose an option : ')


     try:
          if options.lower()  == "rue":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=goto&-number=1&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass


     try:
          if options.lower()  == "marcel":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=goto&-number=2&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass



     try:
          if options.lower()  == "garage":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=goto&-number=3&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass



     try:
          if options.lower()  == "chemin":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=goto&-number=4&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass





     try:
          if options.lower()  == "mamie":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=goto&-number=5&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass


     try:
          if options.lower()  == "voisin":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=goto&-number=6&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass



     try:
          if options.lower()  == "kangoo":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=goto&-number=7&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass

     try:
          if options.lower()  == "setkangoo":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=set&-status=1&-number=7&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass








     try:
          if options.lower()  == "setrue":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=set&-status=1&-number=1&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass


     try:
          if options.lower()  == "setmarcel":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=set&-status=1&-number=2&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass



     try:
          if options.lower()  == "setgarage":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=set&-status=1&-number=3&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass



     try:
          if options.lower()  == "setchemin":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=set&-status=1&-number=4&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass



     try:
          if options.lower()  == "setmamie":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=set&-status=1&-number=5&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass


     try:
          if options.lower()  == "setvoisin":

               try:
                    query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=preset&-act=set&-status=1&-number=6&usr='+str(user)+'&pwd='+str(passwd)
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
     except:
          pass













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

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/sysreboot.cgi?&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print()   
               print(soup.get_text())
               print()
          except Exception as e:
               print(e)

     if options  == "14":

          try:
               ask =""
               while ask not in ("y","n"): 
                    ask = input("Are you sure you want to reset the device ?? y/n\n")
                    ask = str(ask.lower())
               if ask == "y":


                    query = "http://"+str(host)+'/cgi-bin/hi3510/sysreset.cgi?&usr='+str(user)+'&pwd='+str(passwd)
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



     if options  == "16":

          try:
               ask =""
               while ask not in ("y","n"): 
                    ask = input("Are you sure you want to delete the logs ?? y/n\n")
                    ask = str(ask.lower())
               if ask == "y":


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


     if options  == "17":

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

     if options  == "18":

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


     if options  == "19":

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

     if options  == "20":

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

     if options  == "21":

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


     if options  == "22":

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



     if options  == "23":

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

     if options  == "24":

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



     if options  == "25":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getalarmsnapattr'+'&usr='+str(user)+'&pwd='+str(passwd)
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

     if options  == "26":

          print("\nExample:\n")
          print("-snap_count=2")
          cmd = input("\nEnter cmd :\n")

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setalarmsnapattr&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
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



     if options  == "27":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=getsnaptimerattrex'+'&usr='+str(user)+'&pwd='+str(passwd)
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
          print("-as_enable=1&-as_interval=60&-as_type=snap")
          cmd = input("\nEnter cmd :\n")

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setsnaptimerattrex&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
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


     if options  == "30":

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

     if options  == "31":

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






     if options  == "32":

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



     if options  == "33":

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

     if options  == "34":

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



     if options  == "35":

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

     if options  == "36":

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

     if options  == "37":

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/getvencattr.cgi?-chn=11'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup = BeautifulSoup(send,'lxml')
               print("\nStream1\n")
               print(soup.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/getvencattr.cgi?-chn=12'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup1 = BeautifulSoup(send,'lxml')
               print("\nStream2\n")
               print(soup1.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/getvencattr.cgi?-chn=13'+'&usr='+str(user)+'&pwd='+str(passwd)
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]
               send = opener.open(query)
               soup2 = BeautifulSoup(send,'lxml')
               print("\nStream3\n")
               print(soup2.get_text())
               print()
          except Exception as e:
               print()
               print("Error : ",e)


     if options  == "38":

          print("\nExample:\n")
          print("-chn=11&-bps=1536&-fps=25&-brmode=1&-imagegrade=1&-gop=50")
          cmd = input("\nEnter cmd :\n")

          try:
               query = "http://"+str(host)+'/cgi-bin/hi3510/param.cgi?cmd=setvencattr&'+str(cmd)+'&usr='+str(user)+'&pwd='+str(passwd)
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

     if options  == "40":

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

     if options  == "41":

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

     if options  == "42":

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

     if options  == "43":

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

     if options  == "44":

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


     if options  == "45":

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

     if options  == "46":

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

     if options  == "47":

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
