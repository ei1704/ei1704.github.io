#-*-coding:euc-jp-*-

import mcpi.minecraft as minecraft
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from time import sleep

li=[0 for i in range(101)]
mp=[[0 for i in range(3)]for i in range(8)]
cnt=1
item_id=0
mc = 0

sx=0
sy=0
gx=0
gy=0
xSize=0
ySize=0
stage=[[0 for i in range(100)]for i in range(100)]


def readLevel(filename):
    global mc
    if mc==0:
        messagebox.showerror("Alert","マインクラフトが接続されていません")
        return
    try:
        file=open(str("./levels/")+filename)
        global xSize,ySize,stage
        
        lines=file.readlines()

        xy = [int(s) for s in lines[0].split() if s.isdigit()] 

        xSize=int(xy[0])
        ySize=int(xy[1])

        print("{0} {1}".format(xSize,ySize))

        for i in range(1,ySize+1):
            stage[i]=[int(s) for s in lines[i].split() if s.isdigit()]
            print(stage[i])

        global sx,sy,gx,gy

        
        mc.setBlocks(-100,1,-100,100,100,100,0)
        mc.setBlocks(-100,0,-100,100,0,100,2)

        xSide=xSize/2
        ySide=ySize/2
        mc.player.setPos(xSide,10,ySide)

        mc.setBlocks(-1,0,-1,xSize,0,ySize,35,0)
        mc.setBlocks(-1,1,-1,-1,1,ySize,35,15)
        mc.setBlocks(-1,1,-1,xSize,1,-1,35,15)
        mc.setBlocks(xSize,1,ySize,-1,1,ySize,35,15)
        mc.setBlocks(xSize,1,ySize,xSize,1,-1,35,15)

        #xSide-=1
        #ySide-=1
        
        for y in range(1,ySize+1):
            for x in range(0,xSize):
                sleep(0.1)
                if stage[y][x]==0:
                    mc.setBlock(x,1,y-1,35,8)
                elif stage[y][x]==2:
                    mc.setBlock(x,0,y-1,35,14)
                    mc.setBlocks(x,1,y-1,x,2,y-1,85,0)
                    sx=x
                    sy=y-1
                elif stage[y][x]==3:
                    mc.setBlock(x,0,y-1,35,1)
                    gx=x
                    gy=y-1

    except Exception as e:
        print(e)
    finally:
        file.close()

class Application(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master

class blocks():
    def __init__(self,filename,num,x,y,tag,kind):
        self.num=num
        self.defFname=filename#元のファイル名
        if num>0:
            self.filename=filename+str(num)+'.png'
        else:
            self.filename=filename+'.png'
        self.img=Image.open(self.filename);
        self.img=ImageTk.PhotoImage(self.img)
        self.x=x
        self.y=y
        if kind==1:
            self.dx=50
            self.dy=70
        elif kind==2:
            self.dx=50
            self.dy=200
        else:
            self.dx=50
            self.dy=330

        self.tag=str(tag)
        self.flag=False
        self.kind=kind
        #self.move=0

        self.pressed_x = self.pressed_y = 0

        ID=canvas.create_image(x,y,image=self.img,tags=tag)
        print(ID)
        self.setid(ID)

        canvas.tag_bind(self.tag,"<Button-1>",self.pressed)
        canvas.tag_bind(self.tag,"<B1-Motion>",self.dragged)
        canvas.tag_bind(self.tag,"<ButtonRelease-1>",self.Released)

        #self.ID=num
        #self.item_id=num

    def setid(self,id):
        self.id=id

    def pressed(self,event):
        global canvas

        x = event.x
        y = event.y
        if self.x+20<x and x<self.x+50 and self.y-50<y and y<self.y-30:
            if self.num>0:
                self.num=(self.num+1)%5
                if self.num==0:
                    self.num=1
                self.filename=self.defFname+str(self.num)+'.png'
                self.img=Image.open(self.filename);
                self.img=ImageTk.PhotoImage(self.img)
                canvas.itemconfig(self.id,image=self.img)

    def dragged(self,event):
        global canvas,li,cnt
        x = event.x
        y = event.y

        if self.x+20<x and x<self.x+50 and self.y-50<y and y<self.y-30:
            return
        #if x>self.x+30 and x<self.x+50 and self.y<y and y<self.y+30:

        #    if self.num>0:
        #        self.num=(self.num+1)%5
        #        if self.num==0:
        #            self.num=1
        #            self.filename=self.defFname+str(self.num)+'.png'
        #            self.img=Image.open(self.filename);
        #            self.img=ImageTk.PhotoImage(self.img)
        #            canvas.itemconfig(self.id,image=self.img)
        #else:
        canvas.coords(self.id,x,y)
        #print(str(x)+" "+str(y))
        #if x>=140 and self.flag==False:
        #    li[cnt]=blocks(self.filename,self.dx,self.dy,cnt,self.kind)

            #canvas.tag_bind(li[cnt].tag,"<B1-Motion>",li[cnt].dragged)
        #    cnt+=1

        #    self.flag=True
        #elif x<140:

    def Released(self,event):

        global canvas,li,cnt,mp

        x = event.x
        y = event.y
        #if x-50>=100:
        if x>=100:
            if self.flag==False:
                li[cnt]=blocks(self.defFname,self.num,self.dx,self.dy,cnt,self.kind)
                self.flag=True
                cnt+=1
            nx=(int)(x/100)*100#100の位を抽出
            ny=(int)(y/100)*100
            if nx==self.x-50 and ny==self.y-50:
                canvas.coords(self.id,self.x,self.y)
                return
            print(str(nx)+" "+str(ny))
            if mp[(int)(ny/100)][(int)(nx/100)-1]==0:
                mp[(int)(self.y/100)][(int)(self.x/100)-1]=0
                self.x=nx+50
                self.y=ny+50
                mp[(int)(ny/100)][(int)(nx/100)-1]=self
            #挿入処理
            else:
                #ブロックの元の場所を保存
                tempx=self.x
                tempy=self.y
                #一旦空にする
                if self.x-50>=100: 
                    mp[(int)((self.y-50)/100)][(int)((self.x-50)/100)-1]=0
                    
                hx=((int)(nx/100)-1)
                hy=(int)(ny/100)
                if(hy!=7): 
                    judge=self.rec(hx,hy+1)
                else: 
                    judge=self.rec(hx+1,0)
                if judge==0:
                    self.x=nx+50
                    self.y=ny+50                    
                    mp[(int)(ny/100)][(int)(nx/100)-1]=self
                else:
                    mp[(int)(self.y/100)][(int)(self.x/100)-1]=self
                print(mp)
            canvas.coords(self.id,self.x,self.y)
            
        elif x<100:
            mp[(int)(self.y/100)][(int)(self.x/100)-1]=0
            canvas.coords(self.id,self.dx,self.dy)    
    
    def rec(self,x,y):
        global mp
        print(str(x)+"-"+str(y))
        if y==0 and x==3:
            return 1
        if mp[y][x]==0:
            if y==0:
                mp[7][x-1].x=(x+1)*100+50
                mp[7][x-1].y=y*100+50
                canvas.coords(mp[7][x-1].id,mp[7][x-1].x,mp[7][x-1].y)
                mp[y][x]=mp[7][x-1]
            else:
                mp[y-1][x].x=(x+1)*100+50
                mp[y-1][x].y=y*100+50
                canvas.coords(mp[y-1][x].id,mp[y-1][x].x,mp[y-1][x].y)
                mp[y][x]=mp[y-1][x]
            return 0
        else:
            save=0
            if y==7:
                save=self.rec(x+1,0)
            else:
                save=self.rec(x,y+1)
            print(str(x)+" "+str(y))
            
            if save==0:        
                if y==0:
                    mp[7][x-1].x=(x+1)*100+50
                    mp[7][x-1].y=y*100+50
                    canvas.coords(mp[7][x-1].id,mp[7][x-1].x,mp[7][x-1].y)
                    mp[y][x]=mp[7][x-1]
                else:
                    mp[y-1][x].x=(x+1)*100+50
                    mp[y-1][x].y=y*100+50
                    canvas.coords(mp[y-1][x].id,mp[y-1][x].x,mp[y-1][x].y)
                    mp[y][x]=mp[y-1][x]
            return save

root=tk.Tk()
app = Application(master=root)

def on_closing():

    if messagebox.askokcancel("Quit","Quit?"):
        root.destroy()

def start():
    global mp,mc,sx,sy,gx,gy
    if mc==0:
        messagebox.showerror("Alert","マインクラフトが接続されていません")
        print('マインクラフトが接続されていません')
        return
    sclipt=[0 for i in range(0,24)]
    c=0
    direc='n'
    print(mp)
    for i in range(3):
        for j in range(8):
            print(str(i)+" "+str(j))
            sclipt[c]=mp[j][i]
            c+=1


    x=sx
    z=sy
    #mc.setBlock(x,0,z,35,14)
    for i in range(3):
        for j in range(8):
          if mp[j][i]==0 or mp[j][i].kind==3:
             break
          elif mp[j][i].kind==1:
            for s in range(mp[j][i].num):
                mc.setBlock(x,0,z,35,0)
                mc.setBlocks(x,1,z,x,2,z,0,0)
                if direc=='e':
                    x+=1
                elif direc=='w':
                    x-=1
                elif direc=='s':
                    z+=1
                elif direc=='n':
                    z-=1
                mc.setBlock(x,0,z,35,14)
                blockstate=mc.getBlockWithData(x,1,z)
                mc.setBlocks(x,1,z,x,2,z,85,0)
                sleep(0.5)

                if blockstate.id==35:
                    messagebox.showerror("Alert","壁に衝突しました")
                    mc.setBlock(x,1,z,35,blockstate.data)
                    mc.setBlock(x,2,z,0,0)
                    mc.setBlock(x,0,z,35,0)
                    mc.setBlock(sx,0,sy,35,14)
                    mc.setBlocks(sx,1,sy,sx,2,sy,85,0)
                    mc.setBlocks(gx,1,gy,gx,2,gy,0,0)
                    mc.setBlock(gx,0,gy,35,1)
                    return 
                elif x==gx and z==gy:
                    messagebox.showinfo("Alert","ゴールしました")
                    mc.setBlock(x,0,z,35,0)
                    mc.setBlock(sx,0,sy,35,14)
                    mc.setBlocks(sx,1,sy,sx,2,sy,85,0)
                    mc.setBlock(gx,0,gy,35,1)
                    mc.setBlocks(gx,1,gy,gx,2,gy,0,0)
                    return
          elif mp[j][i].kind==2:
            for s in range(mp[j][i].num):
                if direc=='n':
                 direc='e'
                elif direc=='e':
                 direc='s'
                elif direc=='s':
                 direc='w'
                elif direc=='w':
                 direc='n'
                 sleep(0.5)

    if x!=gx and z!=gy:
        messagebox.showinfo("Alert","ゴールできませんでした")
        mc.setBlock(x,0,z,35,0)
        mc.setBlocks(x,1,z,x,2,z,0,0)
        mc.setBlock(sx,0,sy,35,14)
        mc.setBlocks(sx,1,sy,sx,2,sy,85,0)
        mc.setBlocks(gx,1,gy,gx,2,gy,0,0)
        mc.setBlock(gx,0,gy,35,1)


    print("実行完了")

def connect():
    global mc
    mc = minecraft.Minecraft.create()
    mc.postToChat("Conecting complete")

def reset():
    global mc,sx,sy
    sx=0
    sy=0
    if mc==0:
        messagebox.showerror("Alert","マインクラフトが接続されていません")
        print('マインクラフトが接続されていません')
        return

    x=0
    z=0
    
    mc.setBlocks(-100,1,-100,100,100,100,0)
    mc.setBlocks(-100,0,-100,100,0,100,2)
    mc.player.setPos(0,10,0)

    mc.setBlocks(-5,0,-5,5,0,5,35,0)
    mc.setBlocks(-5,1,-5,-5,1,5,35,15)
    mc.setBlocks(-5,1,-5,5,1,-5,35,15)
    mc.setBlocks(5,1,5,-5,1,5,35,15)
    mc.setBlocks(5,1,5,5,1,-5,35,15)


    mc.setBlock(x,0,z,35,14)



def main():

    root.title("ROBOCHART in Minecraft")
    root.minsize(900,900)
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)

    #mae=blocks('images/mae.png',50,70,"mae")
    #migi=blocks('images/migi.png',50,200,"migi")
    #end=blocks('images/end.png',50,330,"end")
    global canvas,li,cnt

    #readLevel("level1.txt")

    #canvas = tk.Canvas(width=100,height=480,bg="white")

    canvas = tk.Canvas(width=400,height=800,bg="white")

    li[cnt]=blocks('images/mae',1,50,70,cnt,1)
    li[cnt+1]=blocks('images/migi',1,50,200,cnt+1,2)
    li[cnt+2]=blocks('images/end',0,50,330,cnt+2,3)
    cnt+=14

    #root.protocol("WM_DELETE_WINDOW", on_closing)



    canvas.create_line(100,0,100,800,fill='black')
    canvas.create_line(200,0,200,800,fill='gray')
    canvas.create_line(300,0,300,800,fill='gray')
    canvas.create_line(400,0,400,800,fill='gray')

    for i in range(1,8):
        canvas.create_line(100,100*i,400,100*i,fill='gray')

    canvas.place(x=0,y=100)

    Button1 = tk.Button(text=u'スタート',command=start)
    Button2 = tk.Button(text=u'接続',command=connect)
    Button3 = tk.Button(text=u'リセット',command=reset)
    Button4 = tk.Button(text=u'レベル1構築',command=lambda:readLevel("level1.txt"))
    Button5 = tk.Button(text=u'レベル2構築',command=lambda:readLevel("level2.txt"))
    
    Button6 = tk.Button(text=u'レベル3構築',command=lambda:readLevel("level3.txt"))


    Button1.place(x=600,y=400)
    Button2.place(x=600,y=450)
    Button3.place(x=600,y=500)
    Button4.place(x=600,y=550)
    Button5.place(x=600,y=600)
    Button6.place(x=600,y=650)

    #canvas.tag_bind(mae.tag,"<Button-1>",mae.pressed)
    #canvas.tag_bind(migi.tag,"<Button-1>",migi.pressed)
    #canvas.tag_bind(end.tag,"<Button-1>",end.pressed#)

    #canvas.tag_bind(mae.tag,"<B1-Motion>",mae.dragged)
    #canvas.tag_bind(migi.tag,"<B1-Motion>",migi.dragged)
    #canvas.tag_bind(end.tag,"<B1-Motion>",end.dragged)

    root.mainloop()


if __name__=="__main__":
    main()
