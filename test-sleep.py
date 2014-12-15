import Tkinter
from flow_adder import flow_adder
from flow_deleter import flow_deleter
import thread
import tkMessageBox



#functions
def delete_action():
    thread.start_new_thread(flow_deleter,())
def add_action():
    thread.start_new_thread(flow_adder,())
def about():
    tkMessageBox.showinfo("About", "Opendaylight REST client, 2014")
#the main window

top=Tkinter.Tk(className='Opendaylight RRST client')

#flow frame
frame_flow = Tkinter.LabelFrame(top,text="Basic Flow functions")
frame_flow.pack()

button = Tkinter.Button(frame_flow,width=30,padx=5,pady=2)
button['text'] = 'Add default flows'
button['command'] =add_action
button['relief']='groove'
button.pack(side=Tkinter.LEFT)

button = Tkinter.Button(frame_flow,width=30,padx=5,pady=2)
button['text'] = 'Delete all default flows'
button['command'] =delete_action
button['relief']='groove'
button.pack(side=Tkinter.LEFT)






function_flow = Tkinter.LabelFrame(top,text="Network Functions")
function_flow.pack()

button = Tkinter.Button(function_flow,width=30,padx=5,pady=2)
button['text'] = 'Redundancy/'
button['command'] =add_action
button['relief']='groove'
button.pack(side=Tkinter.LEFT)

button = Tkinter.Button(function_flow,width=30,padx=5,pady=2)
button['text'] = 'Loadbalancer'
button['command'] =delete_action
button['relief']='groove'
button.pack(side=Tkinter.LEFT)

















L1 = Tkinter.Label(top, text="Flow Name")
L1.pack( side = Tkinter.LEFT)
E1 = Tkinter.Entry(top, bd =5)
E1.pack(side = Tkinter.LEFT)


L2 = Tkinter.Label(top, text="Switch ID")
L2.pack( side = Tkinter.LEFT)
E2 = Tkinter.Entry(top, bd =5)
E2.pack(side = Tkinter.LEFT)



L3 = Tkinter.Label(top, text="Incoming port")
L3.pack( side = Tkinter.LEFT)
E3 = Tkinter.Entry(top, bd =5)
E3.pack(side = Tkinter.LEFT)


L4 = Tkinter.Label(top, text="Actions")
L4.pack( side = Tkinter.LEFT)
E4 = Tkinter.Entry(top, bd =5)
E4.pack(side = Tkinter.LEFT)

button = Tkinter.Button(top,padx=5,pady=2)
button['text'] = 'Add flow'
button['command'] =add_action
button['relief']='groove'
button.pack(side=Tkinter.LEFT)




















menubar = Tkinter.Menu(top)
filemenu = Tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Close", command=top.quit)
menubar.add_cascade(label="System", menu=filemenu)


helpmenu = Tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About",command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

top.config(menu=menubar)

Tkinter.mainloop()
