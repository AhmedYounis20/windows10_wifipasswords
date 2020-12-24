import subprocess
from tkinter import *
from tkinter.font import Font

from tkscrolledframe import ScrolledFrame
a=subprocess.check_output(['netsh','wlan', 'show', 'profiles']).decode('utf-8').split(' ')
a=' '.join(a)
l=[]
for i in range(len(a.split('\n'))):
    x=a.split('\n')[i]
    if x.startswith("    All User Profile"):
        wifi=x.split(':')[1]
        if wifi not in l:l+=[wifi]
for i in range(len(l)):
        l[i]=l[i][1:]
        l[i]=l[i].replace('\r','')
def profile(a):
    b=subprocess.check_output(['netsh','wlan','show','profile',a,'key=clear']).decode('utf-8').split(' ')
    b=' '.join(b)
    b=b.split('\n')
    return b
results={}
max_len=0
for j in l:
    a=profile(j)
    for i in a:
        if i.startswith('    Key Content'):
            results[j]=i.split(': ')[1]
            if len(i.split(': ')[1]) > max_len: max_len=len(i.split(': ')[1])

root =Tk()
root.config(width=400,height=400,bg='#231e1e')
root.iconbitmap('passicon.ico')
#for i in
inner = ScrolledFrame(root, width=450+max_len, height=70*len(results)/(4/3), bg="#231e1e", scrollbars="vertical", )
inner.pack(expand=1, fill="y", )
inner.bind_arrow_keys(root)
inner.bind_scroll_wheel(root)
inner2 = inner.display_widget(Frame)  ## main window
inner2.config(background="black")
frams={}
for i in results:
        frams[i]=Frame(inner2,bg='#231e1e',width=450+max_len,height=70)
        Label(frams[i],text='{} :{}'.format(i,results[i]),bg="#231e1e",fg='pink',font=('arial',14,"bold")).place(y=20,x=11)
        frams[i].pack(pady=2)

root.title('wifi password')

root.mainloop()
