#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:08:33 2021

@author: eborges
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib


nx=[ 0.0,  1.0,  1.0,  0.0, -1.0, -1.0,  0.0,  1.0, -1.0,  0.0, -1.0,  1.0,  1.0, -2.0,  1.0, -1.0,  2.0, -1.0,  1.0,  1.0, -2.0, -1.0,  2.0, -1.0 ]
ny=[-1.0,  0.0,  1.0, -1.0,  0.0,  1.0,  1.0,  0.0,  1.0,  1.0,  0.0,  1.0, -1.0, -1.0,  2.0,  2.0, -1.0, -1.0, -2.0,  1.0,  1.0,  1.0,  1.0, -2.0 ]
nz=[ 1.0,  1.0,  0.0,  1.0,  1.0,  0.0,  1.0,  1.0,  0.0,  1.0,  1.0,  0.0,  2.0, -1.0, -1.0, -1.0, -1.0,  2.0, -1.0,  2.0, -1.0,  2.0, -1.0, -1.0 ]

mx=[-1.0, -1.0, -1.0,  1.0,  1.0,  1.0, -1.0, -1.0, -1.0,  1.0,  1.0,  1.0, -1.0, -1.0, -1.0,  1.0,  1.0,  1.0, -1.0, -1.0, -1.0,  1.0,  1.0,  1.0 ]
my=[ 1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0 ]
mz=[ 1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0 ]

#load
lx = -1.0 
ly = 4.0
lz = 9.0

schmid_list = []
SS_list = []

plt.rc('xtick', labelsize=5)    # fontsize of the tick labels
plt.rc('ytick', labelsize=5)    # fontsize of the tick labels
fig, ax = plt.subplots()
for i in range(len(nx)):
    cos_phi = (nx[i]*lx + ny[i]*ly + nz[i]*lz)/(np.sqrt((nx[i]**2 + ny[i]**2 + nz[i]**2)*(lx**2 + ly**2 + lz**2)))
    cos_lambda = (mx[i]*lx + my[i]*ly + mz[i]*lz)/(np.sqrt((mx[i]**2 + my[i]**2 + mz[i]**2)*(lx**2 + ly**2 + lz**2)))
    schmid = cos_phi*cos_lambda
    schmid_list.append(abs(schmid))
    SS_list.append(i+1)
    print("SS",i+1,"(",nx[i],ny[i],nz[i],")","[",mx[i],my[i],mz[i],"]", "-Schmid Factor = ", "%.2f" % schmid)
    string = "SS " + str(i+1) + ' (' + str(int(nx[i])) + ' ' + str(int(ny[i])) + ' ' + str(int(nz[i])) + ')' + ' [' + str(int(mx[i])) + ' ' + str(int(my[i])) + ' ' + str(int(mz[i])) + ']'
    plt.text(26.,0.53 - i*0.025,string, fontsize=8, fontname = 'Diploma')


plt.xticks(SS_list, SS_list)
ax.bar(SS_list, schmid_list, color = 'DarkBlue', align='center')
ax.set(xlabel='Slip System', ylabel='Schmid Factor',
       title='Load Direction (' + str(int(lx))+ ' ' + str(int(ly)) + ' ' + str(int(lz)) +')' )
ax.grid(linewidth=0.5)

plt.tight_layout()
plt.savefig('schmidfactors.pdf')
plt.show()


#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

