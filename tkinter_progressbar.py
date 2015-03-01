# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 23:33:02 2015

@author: Alois_W
"""

from tkinter import *
import ttk
root = Tk()
progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200, mode='determinate')
progressbar.pack(side="bottom")
progressbar.start()
root.mainloop()