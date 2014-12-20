from Tkinter import*
import tkFont
from flow_adder import flow_adder
from flow_deleter import flow_deleter
from topo_monitor import topo_monitor
import thread
import tkMessageBox



#functions
def delete_action():
    thread.start_new_thread(flow_deleter,())
def add_action():
    thread.start_new_thread(flow_adder,())
def about():
    tkMessageBox.showinfo("About", "Opendaylight REST client, 2014")
def odl_setting():
    odl_set = Toplevel(class_='Opendaylight Connection Setting')
def red_action():
    thread.start_new_thread(topo_monitor,())


    frame = Frame(odl_set)
    frame.pack()

    ODLL1 = Label(frame, text="Opendaylight Address",width=20,anchor="e")
    ODLL1.pack( side = LEFT)
    ODLE1 = Entry(frame, bd =5)
    ODLE1.pack(side = LEFT)

    frame = Frame(odl_set)
    frame.pack()

    ODLL2 = Label(frame, text="User Name",width=20,anchor="e")
    ODLL2.pack( side= LEFT)
    ODLE2 = Entry(frame, bd =5)
    ODLE2.pack(side = LEFT)

    frame = Frame(odl_set)
    frame.pack()

    ODLL3 = Label(frame, text="Password",width=20,anchor="e")
    ODLL3.pack( side = LEFT)
    ODLE3 = Entry(frame, bd =5)
    ODLE3.pack(side = LEFT)
def add_a_flow():
    odl_set = Toplevel(class_='Add a new flow')


    frame = Frame(odl_set)
    frame.pack()

    ODLL1 = Label(frame, text="Flow Name",width=20,anchor="e")
    ODLL1.pack( side = LEFT)
    ODLE1 = Entry(frame, bd =5)
    ODLE1.pack(side = LEFT)

    frame = Frame(odl_set)
    frame.pack()

    ODLL2 = Label(frame, text="Switch ID",width=20,anchor="e")
    ODLL2.pack( side= LEFT)
    ODLE2 = Entry(frame, bd =5)
    ODLE2.pack(side = LEFT)

    frame = Frame(odl_set)
    frame.pack()

    ODLL3 = Label(frame, text="Incoming Port",width=20,anchor="e")
    ODLL3.pack( side = LEFT)
    ODLE3 = Entry(frame, bd =5)
    ODLE3.pack(side = LEFT)

    frame = Frame(odl_set)
    frame.pack()

    ODLL4 = Label(frame, text="Actions",width=20,anchor="e")
    ODLL4.pack( side = LEFT)
    ODLE4= Entry(frame, bd =5)
    ODLE4.pack(side = LEFT)

    frame = Frame(odl_set)
    frame.pack()

    button = Button(frame,padx=5,pady=2)
    button['text'] = 'Add!'
    button['relief']='groove'
    button.pack(side=TOP)


#font
    
#the main window

top=Tk(className='Opendaylight RRST client')
top.resizable(False, False)
top.geometry("800x600")
top.option_add("*Font","Times New Roman")

top_1= Frame(top,height=200,width=600)
top_1.pack(side=TOP)

#flow frame
function_flow = LabelFrame(top_1,text="Additional Functions")
function_flow.pack(side=RIGHT)

button = Button(frame_flow,width=30,padx=5,pady=2)
button['text'] = 'Add default flows'
button['command'] =add_action
button['relief']='groove'
button['bd']= 2
button.pack(side=TOP)

button = Button(frame_flow,width=30,padx=5,pady=2)
button['text'] = 'Delete all default flows'
button['command'] =delete_action
button['relief']='groove'
button.pack(side=TOP)

#function frame
function_flow = LabelFrame(top_1,text="Additional Functions")
function_flow.pack(side=RIGHT)

button = Button(function_flow,width=30,padx=5,pady=2)
button['text'] = 'Start Redundancy Service'
button['command'] =red_action
button['relief']='groove'
button.pack(side=TOP)

button = Button(function_flow,width=30,padx=5,pady=2)
button['text'] = 'Start Loadbalancer Service'
button['command'] =delete_action
button['relief']='groove'
button.pack(side=TOP)

#log frame
frame_log = LabelFrame(top,text="System Info")
frame_log.pack(side=BOTTOM)
text = Text(frame_log)
text.pack()
text.bind("<KeyPress>", lambda e : "break")

#Menu
menubar = Menu(top)

systemmenu = Menu(menubar, tearoff=0)
systemmenu.add_command(label="Opendaylight Connection Settings",command=odl_setting)
menubar.add_cascade(label="System", menu=systemmenu)

toolsmenu = Menu(menubar, tearoff=0)
toolsmenu.add_command(label="Add a new flow", command=add_a_flow)
menubar.add_cascade(label="Tools", menu=toolsmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About",command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

top.config(menu=menubar)

mainloop()
