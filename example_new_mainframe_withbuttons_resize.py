# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 12:30:43 2015

@author: Alois_W
"""

#Example of gui running python 3.4.2.4

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

 
def quit():
    root.destroy()

#Action for Start button
def onstart():    
    messagebox.askyesno(message='Have you checked that Bias is set to Boost?', icon='question', title='Before Start')
    if messagebox.askyesno() == True:
        start_measurment()
        print("Start Measurement")
        #Start the Measurment
    if messagebox.askyesno() == False:
        window.destroy()
        #Destroy the dialog and go back
root = Tk()
root.title("Wayne Kerr Control Programm")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#Necessary for grid resize
mainframe.columnconfigure(1, weight=1,minsize=10)
mainframe.columnconfigure(1, pad=5)
mainframe.columnconfigure(2, weight=1,minsize=10)
mainframe.columnconfigure(2, pad=5)
mainframe.columnconfigure(3, weight=1,minsize=10)
mainframe.columnconfigure(3, pad=5)
mainframe.rowconfigure(1, weight=1,minsize=10)
mainframe.rowconfigure(2, weight=1,minsize=10)
mainframe.rowconfigure(3, weight=1,minsize=10)
mainframe.rowconfigure(4, weight=1,minsize=10)


#Variables for the Window

Bias_low = StringVar()
Bias_high = StringVar()
Bias_step= StringVar()
frequency_low = StringVar()
frequency_high = StringVar()
frequency_steps = StringVar()

material=StringVar()
number_of_turns=StringVar()
geometry=StringVar()

Temp_low=StringVar()
Temp_high=StringVar()
Temp_limit=StringVar()


fan = IntVar()

#Entries###################################################################
#First 3 Colum
Bias_low_entry = ttk.Entry(mainframe, width=7, textvariable=Bias_low)
Bias_low_entry.grid(column=1, row=1, sticky=(W, E))
Bias_high_entry = ttk.Entry(mainframe, width=7, textvariable=Bias_high)
Bias_high_entry.grid(column=1, row=2, sticky=(W, E))
Bias_step_entry = ttk.Entry(mainframe, width=7, textvariable=Bias_step)
Bias_step_entry.grid(column=1, row=3, sticky=(W, E))

material_entry = ttk.Entry(mainframe, width=7, textvariable=material)
material_entry.grid(column=1, row=5, sticky=(W, E))
number_of_turns_entry = ttk.Entry(mainframe, width=7, textvariable=number_of_turns)
number_of_turns_entry.grid(column=1, row=6, sticky=(W, E))
geometry_entry = ttk.Entry(mainframe, width=7, textvariable=geometry)
geometry_entry.grid(column=1, row=7, sticky=(W, E))

#Fourth Colum
frequency_low_entry = ttk.Entry(mainframe, width=7, textvariable=frequency_low)
frequency_low_entry.grid(column=4, row=1, sticky=(W, E))
frequency_high_entry = ttk.Entry(mainframe, width=7, textvariable=frequency_high)
frequency_high_entry.grid(column=4, row=2, sticky=(W, E))
frequency_steps_entry = ttk.Entry(mainframe, width=7, textvariable=frequency_steps)
frequency_steps_entry.grid(column=4, row=3, sticky=(W, E))

Temp_low_entry = ttk.Entry(mainframe, width=7, textvariable=Temp_low)
Temp_low_entry.grid(column=4, row=5, sticky=(W, E))
Temp_high_entry = ttk.Entry(mainframe, width=7, textvariable=Temp_high)
Temp_high_entry.grid(column=4, row=6, sticky=(W, E))
Temp_limit_entry = ttk.Entry(mainframe, width=7, textvariable=Temp_limit)
Temp_limit_entry.grid(column=4, row=7, sticky=(W, E))
##################################################################################

ttk.Label(mainframe, text="Bias lower Border").grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="A").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Bias high Border").grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="A").grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="Bias Steps").grid(column=0, row=3, sticky=W)

ttk.Label(mainframe, text="Frequency lower Border").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Hz").grid(column=5, row=1, sticky=W)
ttk.Label(mainframe, text="Frequency high Border").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Hz").grid(column=5, row=2, sticky=W)
ttk.Label(mainframe, text="Frequency Steps").grid(column=3, row=3, sticky=W)
#For the Filename
ttk.Label(mainframe, text="Material").grid(column=0, row=5, sticky=W)
ttk.Label(mainframe, text="Number of Turns").grid(column=0, row=6, sticky=W)
ttk.Label(mainframe, text="Geometry").grid(column=0, row=7, sticky=W)

#The Temperature things
ttk.Label(mainframe, text="Higher Temperature Border").grid(column=3, row=5, sticky=W)
ttk.Label(mainframe, text="Lower Temperature Border").grid(column=3, row=6, sticky=W)
ttk.Label(mainframe, text="Over Temperature Limit").grid(column=3, row=7, sticky=W)

ttk.Label(mainframe, text="°C").grid(column=5, row=5, sticky=W)
ttk.Label(mainframe, text="°C").grid(column=5, row=6, sticky=W)
ttk.Label(mainframe, text="°C").grid(column=5, row=7, sticky=W)

check = ttk.Checkbutton(mainframe, text='Fan Support',variable=fan,command=fan_required).grid(column=0, row=9, sticky=W)   

ttk.Button(mainframe, text="Start Measurment", command=onstart).grid(column=0, row=10, sticky=W)
ttk.Button(mainframe, text="Quit", command=quit).grid(column=5, row=10, sticky=W)


  

#Action for the fan support check box 
def fan_required():
   
   print("Fan on")
  
        
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
   

def start_measurment():
   print("Put control code in")
root.mainloop()