import fileinput
import string
import time

import pygame
from pygame.locals import *
from pygame.compat import unichr_, unicode_
import sys
import locale

file = fileinput.input("pygame.txt")    # READ the Textfile

# '''CONTENT of pygame.txt'''
# Pygame is a set of Python modules designed for writing games.
# It is written on top of the excellent SDL library. This allows you
# to create fully featured games and multimedia programs in the python
# language. The package is highly portable, with games running on
# Windows, MacOS, OS X, BeOS, FreeBSD, IRIX, and Linux.

speed = 1
# Speed factor, 1 = Default, LOW means Fast, default is between 400 and 300 WPM


a=[]                        # Declare Arrays a and b for seperating
b=[]                        # The text file into single letters (including " ")

for i in file:              # doing
    a.append(i)
    for letter in i:
        b.append(letter)
        
c=[]                        # Declare Array c and String d to store words in 
d=""
for i in b:
    if i not in ("\t", "\n", "\r", "\x0b","\x0c"," "):      # Seperate markers and EMPTY SPACE
        d=d+i                                               # Append single letters to String d until markers are reached
    else:
        c.append(d)         # Add full word to c, then clear d
        d=""
c.append(d)                 # Neccessary for the Last words ends not upon one of the Markers (it's left out otherwise)
    
def main():
    count=0                     # for Words Per Minute
    n=0                         # ^
    pygame.init()
    width=1000
    resolution=width,int(width/3)   # Resolution based on width
    screen=pygame.display.set_mode(resolution)
    fg = 250, 240, 230              # Defining Colours
    bg = 5, 5, 5
    screen.fill(bg)
    font=pygame.font.SysFont("Helvetica",int(0.217*resolution[0]))  # Fontsize based on Screensize

    for i in c:                 # Every i in Array c is one WORD
        screen.fill(bg)         # Black Screen 
        
        size= font.size(i)      # Get word size 
               
        align = resolution[0]/3 - size[0] /2.5  # Align roughly to the middle, but more favorable for reading
        alx=int((resolution[1]/10)+align)       # could've been a one-liner IKR
        
        
        screen.blit(font.render(i, 0, fg), (alx, 10)) #Blit the text on screen
        
        pygame.display.flip()                   # Flip the Switch
        
        timefactor= 0.1+ 0.15* (size[0] / resolution[0]) # Give the readers Eyes some time to take up the Visual Information
        for letter in i:                        # Scale through the word(i) checking for punctation, meaning the end of sentence
            if letter in (".",",","!","?"):     # giving some extra time, as a speaker would also enlengthen their pause
                timefactor=timefactor+0.18      # adding .18s is fine, doubling also gives good results. not in case of "..." though, that's why I decided for the ADDition
        #for letter in i:                        # Tried to make "SDL" not go under in the sample text
        #    if letter in ("A","B","C","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"):
        #        timefactor=timefactor*1.4
        
        time.sleep(timefactor*speed)            # READ -ONE- WORD
        count=count+ timefactor*speed
        n= n+1
        print("\nWord No. "+ str(n)+": "+i+ " (Duration: "+str(timefactor*speed)+"s)")
        print("Words per Minute: "+ str(n/(count/60)))  #Statistics BB
    
        
  
if __name__ == '__main__': main()
