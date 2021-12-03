# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 04:10:06 2021

@author: cosmi

pip install pygame for graphics
"""

import pygame
from pygame.draw import line	
from math import sin,cos,radians

#for random variations:
import random

'''there are at least 3 things we can randomise here: branch length, angle and turn angle

Branch length is easy to radnomise, we can select a random int between a set branch length
You could play the same trick to randomize the angle. This is harder because you need 
to be able to undo the angle and it would be good if the left and right angles were 
not identical. One way to solve this would be to add a variable and break up the turn 
between the two branches into two separate turns.


Create a new angle variable and set it equal to your base angle (currently 45) 
plus some random amount between -45 and +45

Rather than the 90 degree turn to the right, 
turn right by this angle to undo the left turn

Immediately after this right turn, calculate a new random angle

Use this angle to turn right

After drawing the second smaller tree, use the new angle to turn left 
'''


pygame.init()

HIGHT,WITDH = 700,800


BLACK =(0,0,0)
WHITE =(255,255,255)
BLUE  =(0,0,255)
RED   =(255,0,0)

surface = pygame.display.set_mode((WITDH,HIGHT))


def ftree(pos,length,angle,turn_angle,depth,color,split):
	if depth==0:
		return
	x,y=pos
	new_x= x+ cos(radians(angle))*length 
	new_y= y- sin(radians(angle))*length
	line(surface,color,pos,(int(new_x),int(new_y)))

	new_pos = (new_x,new_y)
    
	length=round(random.uniform(0, 1), 2)*length  #make this part random
    
	color1=color2=color
	if split:
		color1=BLUE
		color2=RED
	ftree(new_pos, length,(angle+turn_angle), turn_angle, depth-1, color1,False)
	ftree(new_pos, length,(angle-turn_angle), turn_angle, depth-1, color2,False)


RUN = True

#variables
angle = 90 # for initial angle
length = 100 #start length
turn_angle=0   
depth = 16 # number of recursions
INIT_POS = (WITDH//2,HIGHT)

while RUN:
	surface.fill(BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN=False
	ftree(INIT_POS,length,angle,turn_angle,depth,WHITE,True)	
	turn_angle=random.randint(0, 45) # random angles
	pygame.display.update()