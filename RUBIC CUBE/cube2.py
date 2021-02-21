

moves = ""
top_rows = {
    "row1" : ["Ybr1--h","Yb1","Ybo1--j"],
    "row2" : ["Yr1","Y1","Yo1"],
    "row3" : ["Yrg1--k","Yg1","Ygo1--i"]
}

bottom_rows = {
    "row1" : ["Wbr2","Wb2","Wob2"],
    "row2" : ["Wr2","W2","Wo2"],
    "row3" : ["Wrg2","Wg2","Wgo2"]
}

front_rows = {
    "row1" : ["Gyr3--k","Gy3","Gyo3--i"],
    "row2" : ["Gr3","G3","Go3"],
    "row3" : ["Grw3","Gw3","Gow3"],
}
     
    
back_rows = {
    "row1" : ["Bry4--h","By4","Boy4--j"],
    "row2" : ["Br4","B4","Bo4"],
    "row3" : ["Brw4","Bw4","Bwo4"],
}

left_rows = {
    "row1" : ["Rby5--h","Ry5","Rgy5--k"],
    "row2" : ["Rb5","R5","Rg5"],
    "row3":  ["Rbw5","Rw5","Rwg5"],
}

right_rows = {
    "row1" : ["Ogy6--i","Oy6","Oby6--j"],
    "row2" : ["Og6","O6","Ob6"],
    "row3" : ["Ogw6","Ow6","Obw6"],
}

def shift_top() :
    global moves
    moves = moves + "U "
    line1 = [top_rows["row3"][0],top_rows["row2"][0], top_rows["row1"][0]]
    line2 = [top_rows["row3"][1],top_rows["row2"][1], top_rows["row1"][1]]
    line3 = [top_rows["row3"][2],top_rows["row2"][2], top_rows["row1"][2]]

    top_rows["row1"] = line1
    top_rows["row2"] = line2
    top_rows["row3"] = line3

    backl = left_rows["row1"]
    leftl = front_rows["row1"]
    frontl =right_rows["row1"]
    rightl = back_rows["row1"]

    back_rows["row1"] = [backl[2],backl[1],backl[0]]
    left_rows["row1"] = leftl
    right_rows["row1"] = [rightl[2], rightl[1], rightl[0]]
    front_rows["row1"] = frontl

def reverse_top() :
    global moves
    moves = moves + "U' "
    line1 = [top_rows["row1"][2],top_rows["row2"][2], top_rows["row3"][2]]
    line2 = [top_rows["row1"][1],top_rows["row2"][1], top_rows["row3"][1]]
    line3 = [top_rows["row1"][0],top_rows["row2"][0], top_rows["row3"][0]]

    top_rows["row1"] = line1
    top_rows["row2"] = line2
    top_rows["row3"] = line3

    frontl = left_rows["row1"]
    rightl = front_rows["row1"]
    backl = right_rows["row1"]
    leftl = back_rows["row1"]

    back_rows["row1"] = [backl[2],backl[1],backl[0]]
    left_rows["row1"] = [leftl[2], leftl[1], leftl[0]]
    right_rows["row1"] = [rightl[0],rightl[1], rightl[2]]
    front_rows["row1"] = frontl

##############  Bottom  #####################
def reverse_bottom() :
    global moves
    moves = moves +"D' "
    line1 = [bottom_rows["row3"][0],bottom_rows["row2"][0], bottom_rows["row1"][0]]
    line2 = [bottom_rows["row3"][1],bottom_rows["row2"][1], bottom_rows["row1"][1]]
    line3 = [bottom_rows["row3"][2],bottom_rows["row2"][2], bottom_rows["row1"][2]]

    bottom_rows["row1"] = line1
    bottom_rows["row2"] = line2
    bottom_rows["row3"] = line3

    frontl = right_rows["row3"]
    leftl = front_rows["row3"]
    backl = left_rows["row3"]
    rightl = back_rows["row3"]

    front_rows["row3"] = frontl
    back_rows["row3"] = [backl[2], backl[1], backl[0]] 
    left_rows["row3"] = leftl
    right_rows["row3"] = [rightl[2],rightl[1],rightl[0]]

def shift_bottom() :
    global moves
    moves = moves + "D "
    line1 = [bottom_rows["row1"][2],bottom_rows["row2"][2], bottom_rows["row3"][2]]
    line2 = [bottom_rows["row1"][1],bottom_rows["row2"][1], bottom_rows["row3"][1]]
    line3 = [bottom_rows["row1"][0],bottom_rows["row2"][0], bottom_rows["row3"][0]]

    bottom_rows["row1"] = line1
    bottom_rows["row2"] = line2
    bottom_rows["row3"] = line3

    backl = right_rows["row3"]
    rightl = front_rows["row3"]
    frontl = left_rows["row3"]
    leftl = back_rows["row3"]

    front_rows["row3"] = frontl
    back_rows["row3"] = [backl[2], backl[1], backl[0]]
    left_rows["row3"] = [leftl[2],leftl[1],leftl[0]]
    right_rows["row3"] = [rightl[0], rightl[1], rightl[2]]

########   front ########
def shift_front() :
    global moves
    moves = moves + "F "
    line1 = [front_rows["row3"][0],front_rows["row2"][0], front_rows["row1"][0]]
    line2 = [front_rows["row3"][1],front_rows["row2"][1], front_rows["row1"][1]]
    line3 = [front_rows["row3"][2],front_rows["row2"][2], front_rows["row1"][2]]

    front_rows["row1"] = line1
    front_rows["row2"] = line2
    front_rows["row3"] = line3

    leftl = bottom_rows["row3"]
    topl = [left_rows["row1"][2],left_rows["row2"][2],left_rows["row3"][2]]
    rightl = top_rows["row3"]
    bottoml = [right_rows["row1"][0],right_rows["row2"][0],right_rows["row3"][0]]

    top_rows["row3"] =  [topl[2],topl[1],topl[0]]
    bottom_rows["row3"] = [bottoml[2],bottoml[1],bottoml[0] ]
    left_rows["row1"][2] = leftl[0]
    left_rows["row2"][2] = leftl[1]
    left_rows["row3"][2] = leftl[2]
    right_rows["row1"][0] = rightl[0]
    right_rows["row2"][0] = rightl[1]
    right_rows["row3"][0] = rightl[2]

def reverse_front() :
    global moves
    moves = moves + "F' " 
    line1 = [front_rows["row1"][2],front_rows["row2"][2], front_rows["row3"][2]]
    line2 = [front_rows["row1"][1],front_rows["row2"][1], front_rows["row3"][1]]
    line3 = [front_rows["row1"][0],front_rows["row2"][0], front_rows["row3"][0]]

    front_rows["row1"] = line1
    front_rows["row2"] = line2
    front_rows["row3"] = line3

    rightl = bottom_rows["row3"]
    bottoml = [left_rows["row1"][2],left_rows["row2"][2],left_rows["row3"][2]]
    leftl = top_rows["row3"]
    topl = [right_rows["row1"][0],right_rows["row2"][0],right_rows["row3"][0]]

    top_rows["row3"] =  topl 
    bottom_rows["row3"] = bottoml 
    left_rows["row1"][2] = leftl[2]
    left_rows["row2"][2] = leftl[1]
    left_rows["row3"][2] = leftl[0]
    right_rows["row1"][0] = rightl[2]
    right_rows["row2"][0] = rightl[1]
    right_rows["row3"][0] = rightl[0]

###########  back  ################
def reverse_back() :
    global moves 
    moves = moves + "B' "
    line1 = [back_rows["row3"][0],back_rows["row2"][0], back_rows["row1"][0]]
    line2 = [back_rows["row3"][1],back_rows["row2"][1], back_rows["row1"][1]]
    line3 = [back_rows["row3"][2],back_rows["row2"][2], back_rows["row1"][2]]

    back_rows["row1"] = line1
    back_rows["row2"] = line2
    back_rows["row3"] = line3

    leftl = bottom_rows["row1"]
    topl = [left_rows["row1"][0],left_rows["row2"][0],left_rows["row3"][0]]
    rightl = top_rows["row1"]
    bottoml = [right_rows["row1"][2],right_rows["row2"][2],right_rows["row3"][2]]

    top_rows["row1"] =  [topl[2],topl[1],topl[0]]
    bottom_rows["row1"] = [bottoml[2],bottoml[1],bottoml[0]]
    left_rows["row1"][0] = leftl[0]
    left_rows["row2"][0] = leftl[1]
    left_rows["row3"][0] = leftl[2]
    right_rows["row1"][2] = rightl[0]
    right_rows["row2"][2] = rightl[1]
    right_rows["row3"][2] = rightl[2]

def shift_back() :
    global moves
    moves = moves + "B "
    line1 = [back_rows["row1"][2],back_rows["row2"][2], back_rows["row3"][2]]
    line2 = [back_rows["row1"][1],back_rows["row2"][1], back_rows["row3"][1]]
    line3 = [back_rows["row1"][0],back_rows["row2"][0], back_rows["row3"][0]]

    back_rows["row1"] = line1
    back_rows["row2"] = line2
    back_rows["row3"] = line3

    rightl = bottom_rows["row1"]
    bottoml  = [left_rows["row1"][0],left_rows["row2"][0],left_rows["row3"][0]]
    leftl = top_rows["row1"]
    topl= [right_rows["row1"][2],right_rows["row2"][2],right_rows["row3"][2]]

    top_rows["row1"] =  topl 
    bottom_rows["row1"] = bottoml 
    left_rows["row1"][0] = leftl[2]
    left_rows["row2"][0] = leftl[1]
    left_rows["row3"][0] = leftl[0]
    right_rows["row1"][2] = rightl[2]
    right_rows["row2"][2] = rightl[1]
    right_rows["row3"][2] = rightl[0]

#########  left ##############
def reverse_left() :
    global moves
    moves = moves + "L' "
    line1 = [left_rows["row1"][2],left_rows["row2"][2], left_rows["row3"][2]]
    line2 = [left_rows["row1"][1],left_rows["row2"][1], left_rows["row3"][1]]
    line3 = [left_rows["row1"][0],left_rows["row2"][0], left_rows["row3"][0]]

    left_rows["row1"] = line1
    left_rows["row2"] = line2
    left_rows["row3"] = line3

    frontl = [bottom_rows["row1"][0],bottom_rows["row2"][0],bottom_rows["row3"][0]]
    topl = [front_rows["row1"][0],front_rows["row2"][0],front_rows["row3"][0]]
    backl = [top_rows["row1"][0],top_rows["row2"][0],top_rows["row3"][0]]
    bottoml = [back_rows["row1"][0],back_rows["row2"][0],back_rows["row3"][0]]

    bottom_rows["row1"][0] =  bottoml[0]
    bottom_rows["row2"][0] =  bottoml[1]
    bottom_rows["row3"][0] =  bottoml[2]
    front_rows["row1"][0] =  frontl[2]
    front_rows["row2"][0] =  frontl[1]
    front_rows["row3"][0] =  frontl[0]
    top_rows["row1"][0] =  topl[0]
    top_rows["row2"][0] =  topl[1]
    top_rows["row3"][0] =  topl[2]
    back_rows["row1"][0] =  backl[2]
    back_rows["row2"][0] =  backl[1]
    back_rows["row3"][0] =  backl[0]

def  shift_left() :
    global moves 
    moves = moves + "L "
    line1 = [left_rows["row3"][2],left_rows["row2"][2], left_rows["row1"][2]]
    line2 = [left_rows["row3"][1],left_rows["row2"][1], left_rows["row1"][1]]
    line3 = [left_rows["row3"][0],left_rows["row2"][0], left_rows["row1"][0]]

    left_rows["row1"] = line3
    left_rows["row2"] = line2
    left_rows["row3"] = line1

    backl = [bottom_rows["row1"][0],bottom_rows["row2"][0],bottom_rows["row3"][0]]
    bottoml = [front_rows["row1"][0],front_rows["row2"][0],front_rows["row3"][0]]
    frontl = [top_rows["row1"][0],top_rows["row2"][0],top_rows["row3"][0]]
    topl = [back_rows["row1"][0],back_rows["row2"][0],back_rows["row3"][0]]

    bottom_rows["row1"][0] =  bottoml[2]
    bottom_rows["row2"][0] =  bottoml[1]
    bottom_rows["row3"][0] =  bottoml[0]
    front_rows["row1"][0] =  frontl[0]
    front_rows["row2"][0] =  frontl[1]
    front_rows["row3"][0] =  frontl[2]
    top_rows["row1"][0] =  topl[2]
    top_rows["row2"][0] =  topl[1]
    top_rows["row3"][0] =  topl[0]
    back_rows["row1"][0] =  backl[0]
    back_rows["row2"][0] =  backl[1]
    back_rows["row3"][0] =  backl[2]

########## right ##########
def shift_right() :
    global moves 
    moves = moves + "R "
    line1 = [right_rows["row3"][0],right_rows["row2"][0], right_rows["row1"][0]]
    line2 = [right_rows["row3"][1],right_rows["row2"][1], right_rows["row1"][1]]
    line3 = [right_rows["row3"][2],right_rows["row2"][2], right_rows["row1"][2]]

    right_rows["row1"] = line1
    right_rows["row2"] = line2
    right_rows["row3"] = line3

    frontl = [bottom_rows["row1"][2],bottom_rows["row2"][2],bottom_rows["row3"][2]]
    topl = [front_rows["row1"][2],front_rows["row2"][2],front_rows["row3"][2]]
    backl = [top_rows["row1"][2],top_rows["row2"][2],top_rows["row3"][2]]
    bottoml = [back_rows["row1"][2],back_rows["row2"][2],back_rows["row3"][2]]

    bottom_rows["row1"][2] =  bottoml[0]
    bottom_rows["row2"][2] =  bottoml[1]
    bottom_rows["row3"][2] =  bottoml[2]
    front_rows["row1"][2] =  frontl[2]
    front_rows["row2"][2] =  frontl[1]
    front_rows["row3"][2] =  frontl[0]
    top_rows["row1"][2] =  topl[0]
    top_rows["row2"][2] =  topl[1]
    top_rows["row3"][2] =  topl[2]
    back_rows["row1"][2] =  backl[2]
    back_rows["row2"][2] =  backl[1]
    back_rows["row3"][2] =  backl[0]

def reverse_right() :
    global moves
    moves = moves + "R' "
    line1 = [right_rows["row1"][2],right_rows["row2"][2], right_rows["row3"][2]]
    line2 = [right_rows["row1"][1],right_rows["row2"][1], right_rows["row3"][1]]
    line3 = [right_rows["row1"][0],right_rows["row2"][0], right_rows["row3"][0]]

    right_rows["row1"] = line1
    right_rows["row2"] = line2
    right_rows["row3"] = line3
    
    backl = [bottom_rows["row1"][2],bottom_rows["row2"][2],bottom_rows["row3"][2]]
    bottoml = [front_rows["row1"][2],front_rows["row2"][2],front_rows["row3"][2]]
    frontl = [top_rows["row1"][2],top_rows["row2"][2],top_rows["row3"][2]]
    topl = [back_rows["row1"][2],back_rows["row2"][2],back_rows["row3"][2]]

    bottom_rows["row1"][2] =  bottoml[2]
    bottom_rows["row2"][2] =  bottoml[1]
    bottom_rows["row3"][2] =  bottoml[0]
    front_rows["row1"][2] =  frontl[0]
    front_rows["row2"][2] =  frontl[1]
    front_rows["row3"][2] =  frontl[2]
    top_rows["row1"][2] =  topl[2]
    top_rows["row2"][2] =  topl[1]
    top_rows["row3"][2] =  topl[0]
    back_rows["row1"][2] =  backl[0]
    back_rows["row2"][2] =  backl[1]
    back_rows["row3"][2] =  backl[2]

def col(bl) :
    if  bl.find("1") != -1 :
        return "yellow"
    elif bl.find("2") != -1:
        return "white"
    elif  bl.find("3") != -1:
            return "green"
    elif bl.find("5") != -1:
        return "red"
    elif bl.find("4") != -1 :
        return "blue"
    else :
        return "orange"

import tkinter
from tkinter import *
from time import sleep

def side_line(line, sdl):
    block1 = PanedWindow(line,bd =4, relief="raised", bg = col(sdl[0]), width="200", height = "20")
    l = Label(text="0 = "+sdl[0])
    block1.add(l)
    line.add(block1)
    block2 = PanedWindow(line,bd =4, relief="raised", bg = col(sdl[1]), width="200", height = "20")
    l = Label(text="1 = "+sdl[1])
    block2.add(l)
    line.add(block2)
    block3 = PanedWindow(line,bd =4, relief="raised", bg = col(sdl[2]), width="200", height = "20")
    l = Label(text="2 = "+sdl[2])
    block3.add(l)
    line.add(block3)
    return line

def side(sd,bl):
    side = PanedWindow(bd =4, relief="raised" , orient=VERTICAL, width="200", height = "10")
    side.pack(fill=BOTH, expand=1)
    rightc = Label(text=bl)
    rightc.place(  anchor = 'ne')
    line1 = PanedWindow(side,bd =4, orient=HORIZONTAL)
    l = Label(text="1")
    line1.add(l)
    line1 = side_line(line1,sd["row1"])
    side.add(line1)

    line2 = PanedWindow(side,bd =4, orient=HORIZONTAL)
    l = Label(text="2")
    line2.add(l)
    line2 = side_line(line2,sd["row2"])
    side.add(line2)

    line3 = PanedWindow(side,bd =4, orient=HORIZONTAL)
    l = Label(text="3")
    line3.add(l)
    line3 = side_line(line3,sd["row3"])
    side.add(line3)
    return side

###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
############################################################################################################
#######################################################################################################
def top_edges_in_place(rows) :
    if rows["row1"][1].find("2") == -1 :
          return -1
    elif rows["row2"][0].find("2") == -1 : 
        return -1
    elif rows["row2"][2].find("2") == -1 :
        return -1
    elif rows["row3"][1].find("2") == -1 :
        return -1
    return 1


def out() :
    
    if bottom_rows["row1"][1] == "Wg2" and  bottom_rows["row2"][0] == "Wb2":
        reverse_left()
    elif bottom_rows["row1"][1] == "Wg2" and  bottom_rows["row2"][2] == "Wb2":
        shift_right()
    elif bottom_rows["row3"][1] == "Wg2" and  bottom_rows["row2"][0] == "Wb2":
        reverse_left()
    elif bottom_rows["row3"][1] == "Wg2" and  bottom_rows["row2"][2] == "Wb2":
        shift_right()
    elif bottom_rows["row2"][2] == "Wg2" and  bottom_rows["row1"][1] == "Wb2":
        shift_back()
    elif bottom_rows["row2"][2] == "Wg2" and  bottom_rows["row3"][1] == "Wb2":
        shift_front()
    elif bottom_rows["row2"][0] == "Wg2" and  bottom_rows["row1"][1] == "Wb2":
        shift_back()
    elif bottom_rows["row2"][0] == "Wg2" and  bottom_rows["row3"][1] == "Wb2":
        shift_front()
    elif bottom_rows["row1"][1] == "Wo2" and  bottom_rows["row2"][0] == "Wr2":
        reverse_left()
    elif bottom_rows["row1"][1] == "Wo2" and  bottom_rows["row2"][2] == "Wr2":
        shift_right()
    elif bottom_rows["row3"][1] == "Wo2" and  bottom_rows["row2"][0] == "Wr2":
        reverse_left()
    elif bottom_rows["row3"][1] == "Wo2" and  bottom_rows["row2"][2] == "Wr2":
        shift_right()
    elif bottom_rows["row2"][2] == "Wo2" and  bottom_rows["row1"][1] == "Wr2":
        shift_back()
    elif bottom_rows["row2"][2] == "Wo2" and  bottom_rows["row3"][1] == "Wr2":
        shift_front()
    elif bottom_rows["row2"][0] == "Wo2" and  bottom_rows["row1"][1] == "Wr2":
        shift_back()
    elif bottom_rows["row2"][0] == "Wo2" and  bottom_rows["row3"][1] == "Wr2":
        shift_front()
    elif bottom_rows["row1"][1] == "Wg2" and  bottom_rows["row2"][0] == "Wr2":
        reverse_left()
    elif bottom_rows["row1"][1] == "Wg2" and  bottom_rows["row2"][2] == "Wo2":
        shift_right()
    elif bottom_rows["row3"][1] == "Wg2" and  bottom_rows["row2"][0] == "Wo2":
        reverse_left()
    elif bottom_rows["row3"][1] == "Wg2" and  bottom_rows["row2"][2] == "Wr2":
        shift_right()
    elif bottom_rows["row2"][2] == "Wg2" and  bottom_rows["row1"][1] == "Wr2":
        shift_back()
    elif bottom_rows["row2"][2] == "Wg2" and  bottom_rows["row3"][1] == "Wo2":
        shift_front()
    elif bottom_rows["row2"][0] == "Wg2" and  bottom_rows["row1"][1] == "Wo2":
        shift_back()
    elif bottom_rows["row2"][0] == "Wg2" and  bottom_rows["row3"][1] == "Wr2":
        shift_front()
    elif bottom_rows["row1"][1] == "Wb2" and  bottom_rows["row2"][2] == "Wr2":
        reverse_left()
    elif bottom_rows["row1"][1] == "Wb2" and  bottom_rows["row2"][0] == "Wo2":
        shift_right()
    elif bottom_rows["row3"][1] == "Wb2" and  bottom_rows["row2"][2] == "Wo2":
        reverse_left()
    elif bottom_rows["row3"][1] == "Wb2" and  bottom_rows["row2"][0] == "Wr2":
        shift_right()
    elif bottom_rows["row2"][2] == "Wb2" and  bottom_rows["row3"][1] == "Wr2":
        shift_back()
    elif bottom_rows["row2"][2] == "Wb2" and  bottom_rows["row1"][1] == "Wo2":
        shift_front()
    elif bottom_rows["row2"][0] == "Wb2" and  bottom_rows["row3"][1] == "Wo2":
        shift_back()
    elif bottom_rows["row2"][0] == "Wb2" and  bottom_rows["row1"][1] == "Wr2":
        shift_front()
##########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################

def bottom_crose() :
    i = 0
    c = 0
    while i < 100: # top_edges_in_place(bottom_rows) != 1:
        out()
        if back_rows["row1"][1].find("2") != -1 :
                
            while bottom_rows["row1"][1].find("2") != -1 :
                reverse_bottom()
            shift_back()
        
        elif back_rows["row3"][1].find("2") != -1 :
            while bottom_rows["row1"][1].find("2") != -1 :
                reverse_bottom()
            shift_back()
        
        elif front_rows["row1"][1].find("2") != -1 :
            while bottom_rows["row1"][1].find("2") != -1 :
                reverse_bottom()
            shift_front()
        
        elif front_rows["row3"][1].find("2") != -1 :
            while bottom_rows["row1"][1].find("2") != -1 :
                reverse_bottom()
            shift_front() 

        elif top_rows["row3"][1].find("2") != -1 :
            while bottom_rows["row3"][1].find("2") != -1 :
                reverse_bottom()
            shift_front()

        elif top_rows["row1"][1].find("2") != -1 :
            while bottom_rows["row1"][1].find("2") != -1 :
                reverse_bottom()
            shift_back()
        
        elif top_rows["row2"][0].find("2") != -1 :
            while bottom_rows["row2"][0].find("2") != -1 :
                reverse_bottom()
            reverse_left()
            
        elif top_rows["row2"][2].find("2") != -1 :
            while bottom_rows["row2"][2].find("2") != -1 :
                reverse_bottom()
            shift_right()
        
        elif left_rows["row3"][1].find("2") != -1 :
            while bottom_rows["row2"][0].find("2") != -1 :
                reverse_bottom()
            reverse_left()
            
        elif left_rows["row1"][1].find("2") != -1 :
            while bottom_rows["row2"][0].find("2") != -1 :
                reverse_bottom()
            reverse_left()
        
        elif right_rows["row3"][1].find("2") != -1 :
            while bottom_rows["row2"][2].find("2") != -1 :
                reverse_bottom()
            shift_right()
    
        elif right_rows["row1"][1].find("2") != -1 :
            while bottom_rows["row2"][2].find("2") != -1 :
                reverse_bottom()
            shift_right()
        
        
        
        #################################################
        
        if front_rows["row2"][0].find("2") != -1 :
            while bottom_rows["row2"][0].find("2") != -1 :
                reverse_bottom()
            if front_rows["row2"][0] == "Wg2" and bottom_rows["row3"][1] != "Wb2" and bottom_rows["row3"][1] != "Wr2" and bottom_rows["row1"][1] != "Wb2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row2"][2] != "Wr2" :
                shift_left()
            
            elif front_rows["row2"][0] == "Wb2" and bottom_rows["row3"][1] != "Wg2" and bottom_rows["row3"][1] != "Wo2" and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row1"][1] != "Wr2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row2"][2] != "Wr2":
                shift_left()
            elif front_rows["row2"][0] == "Wo2" and bottom_rows["row3"][1] != "Wg2" and bottom_rows["row3"][1] != "Wr2" and bottom_rows["row1"][1] != "Wb2" and bottom_rows["row1"][1] != "Wr2" and bottom_rows["row2"][2] != "Wg2" and bottom_rows["row2"][2] != "Wb2":
                shift_left()
            elif front_rows["row2"][0] == "Wr2" and bottom_rows["row3"][1] != "Wb2" and bottom_rows["row3"][1] != "Wo2" and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row2"][2] != "Wg2" and bottom_rows["row2"][2] != "Wb2":
                shift_left()
            else :
                reverse_bottom()

        elif front_rows["row2"][2].find("2") != -1 :
            while bottom_rows["row2"][2].find("2") != -1 :
                reverse_bottom()
            if front_rows["row2"][2] == "Wg2" and bottom_rows["row1"][1] != "Wb2" and bottom_rows["row1"][1] != "Wr2" and bottom_rows["row3"][1] != "Wb2" and bottom_rows["row3"][1] != "Wo2" and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row2"][0] != "Wr2":
                reverse_right()
            elif front_rows["row2"][2] == "Wb2" and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row2"][1] != "Wg2" and bottom_rows["row2"][1] != "Wr2" and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row2"][0] != "Wr2":
                reverse_right()
            elif front_rows["row2"][2] == "Wo2" and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row1"][1] != "Wr2" and bottom_rows["row2"][1] != "Wb2" and bottom_rows["row2"][1] != "Wr2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row2"][0] != "Wb2":
                reverse_right()
            elif front_rows["row2"][2] == "Wr2" and bottom_rows["row1"][1] != "Wb2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row2"][1] != "Wg2" and bottom_rows["row2"][1] != "Wo2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row2"][0] != "Wb2":
                reverse_right()
            else :
                reverse_bottom()

        elif back_rows["row2"][0].find("2") != -1 :
            while bottom_rows["row2"][0].find("2") != -1 :
                reverse_bottom()
            if back_rows["row2"][0] == "Wg2" and bottom_rows["row1"][1] != "Wb2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row3"][1] != "Wb2" and bottom_rows["row3"][1] != "Wr2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row2"][2] != "Wr2" :
                reverse_left()
            elif back_rows["row2"][0] == "Wb2" and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row1"][1] != "Wr2" and bottom_rows["row3"][1] != "Wg2" and bottom_rows["row3"][1] != "Wo2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row2"][2] != "Wr2" :
                reverse_left()
            elif back_rows["row2"][0] == "Wo2" and bottom_rows["row1"][1] != "Wr2" and bottom_rows["row1"][1] != "Wb2" and bottom_rows["row3"][1] != "Wr2" and bottom_rows["row3"][1] != "Wg2" and bottom_rows["row2"][2] != "Wg2" and bottom_rows["row2"][2] != "Wb2" :
                reverse_left()
            elif back_rows["row2"][0] == "Wr2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row3"][1] != "Wo2" and bottom_rows["row3"][1] != "Wb2" and bottom_rows["row2"][2] != "Wg2" and bottom_rows["row2"][2] != "Wb2" :
                reverse_left()
            else :
                reverse_bottom()

        elif back_rows["row2"][2].find("2") != -1 :
            while bottom_rows["row2"][2].find("2") != -1 :
                reverse_bottom()
            
            if back_rows["row2"][2] == "Wg2" and bottom_rows["row3"][1] != "Wb2" and bottom_rows["row3"][1] != "Wo2" and bottom_rows["row1"][1] != "Wb2" and bottom_rows["row1"][1] != "Wr2" and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row2"][0] != "Wr2":
                shift_right()
            elif back_rows["row2"][2] == "Wb2" and bottom_rows["row3"][1] != "Wg2" and bottom_rows["row3"][1] != "Wr2" and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row2"][0] != "Wr2":
                shift_right()
            elif back_rows["row2"][2] == "Wo2" and bottom_rows["row3"][1] != "Wr2" and bottom_rows["row3"][1] != "Wb2" and bottom_rows["row1"][1] != "Wr2" and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row2"][0] != "Wb2":
                shift_right()
            elif back_rows["row2"][2] == "Wr2" and bottom_rows["row3"][1] != "Wo2" and bottom_rows["row3"][1] != "Wg2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row1"][1] != "Wb2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row2"][0] != "Wb2":
                shift_right()
            else :
                reverse_bottom()

        elif left_rows["row2"][0].find("2") != -1 :
            while bottom_rows["row1"][1].find("2") != -1 :
                reverse_bottom()
            if left_rows["row2"][0] == "Wg2" and bottom_rows["row2"][0] != "Wb2" and bottom_rows["row2"][0] != "Wr2" and bottom_rows["row2"][2] != "Wb2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row3"][1] != "Wo2" and bottom_rows["row3"][1] != "Wr2":
                shift_back()
            elif left_rows["row2"][0] == "Wb2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row2"][2] != "Wg2" and bottom_rows["row2"][2] != "Wr2" and bottom_rows["row3"][1] != "Wo2" and bottom_rows["row3"][1] != "Wr2":
                shift_back()
            elif left_rows["row2"][0] == "Wo2" and bottom_rows["row2"][0] != "Wr2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row2"][2] != "Wr2" and bottom_rows["row2"][2] != "Wb2" and bottom_rows["row3"][1] != "Wg2" and bottom_rows["row3"][1] != "Wb2":
                shift_back()
            elif left_rows["row2"][0] == "Wr2" and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row2"][0] != "Wb2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row2"][2] != "Wg2" and bottom_rows["row3"][1] != "Wg2" and bottom_rows["row3"][1] != "Wb2":
                shift_back()
           
            else :
                reverse_bottom()

        elif left_rows["row2"][2].find("2") != -1 :
            while bottom_rows["row3"][1].find("2") != -1 :
                reverse_bottom()
            if left_rows["row2"][2] == "Wg2" and bottom_rows["row2"][2] != "Wb2" and bottom_rows["row2"][2] != "Wr2" and bottom_rows["row2"][0] != "Wb2" and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row1"][1] != "Wr2":
                reverse_front()
            elif left_rows["row2"][2] == "Wb2" and bottom_rows["row2"][2] != "Wg2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row2"][0] != "Wr2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row1"][1] != "Wr2":
                reverse_front()
            elif left_rows["row2"][2] == "Wo2" and bottom_rows["row2"][2] != "Wr2" and bottom_rows["row2"][2] != "Wg2" and bottom_rows["row2"][0] != "Wr2" and bottom_rows["row2"][0] != "Wb2" and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row1"][1] != "Wb2":
                        reverse_front()
            elif left_rows["row2"][2] == "Wr2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row2"][2] != "Wb2" and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row1"][1] != "Wb2":
                        reverse_front()
            elif out() == 1 :
                c + 1
            else :
                reverse_bottom()

        elif right_rows["row2"][0].find("2") != -1 :
            while bottom_rows["row3"][1].find("2") != -1 :
                reverse_bottom()
            if right_rows["row2"][0] == "Wg2" and bottom_rows["row2"][0] != "Wb2" and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row2"][2] != "Wb2" and bottom_rows["row2"][2] != "Wr2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row1"][1] != "Wr2" :
                        shift_front()
            elif right_rows["row2"][0] == "Wb2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row2"][0] != "Wr2" and bottom_rows["row2"][2] != "Wg2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row1"][1] != "Wo2" and bottom_rows["row1"][1] != "Wr2" :
                        shift_front()
            elif right_rows["row2"][0] == "Wo2" and bottom_rows["row2"][0] != "Wr2" and bottom_rows["row2"][0] != "Wb2" and bottom_rows["row2"][2] != "Wr2" and bottom_rows["row2"][2] != "Wg2"  and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row1"][1] != "Wb2" :
                        shift_front()
            elif right_rows["row2"][0] == "Wr2" and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row2"][2] != "Wb2" and bottom_rows["row1"][1] != "Wg2" and bottom_rows["row1"][1] != "Wb2" :
                        shift_front()
            elif out() == 1 :
                c + 1
            else :
                reverse_bottom()
   
        elif right_rows["row2"][2].find("2") != -1 :
            while bottom_rows["row1"][1].find("2") != -1 :
                reverse_bottom()
            if right_rows["row2"][2] == "Wg2" and bottom_rows["row2"][2] != "Wb2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row2"][0] != "Wb2" and bottom_rows["row2"][0] != "Wr2" and bottom_rows["row3"][1] != "Wo2" and bottom_rows["row3"][1] != "Wr2" :
                reverse_back()
            
            elif right_rows["row2"][2] == "Wb2" and bottom_rows["row2"][2] != "Wg2" and bottom_rows["row2"][2] != "Wr2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row3"][1] != "Wo2" and bottom_rows["row3"][1] != "Wr2" :
                reverse_back()
            elif right_rows["row2"][2] == "Wo2" and bottom_rows["row2"][2] != "Wr2" and bottom_rows["row2"][2] != "Wb2" and bottom_rows["row2"][0] != "Wr2" and bottom_rows["row2"][0] != "Wg2" and bottom_rows["row3"][1] != "Wg2" and bottom_rows["row3"][1] != "Wb2" :
                reverse_back()
            elif right_rows["row2"][2] == "Wr2" and bottom_rows["row2"][2] != "Wo2" and bottom_rows["row2"][2] != "Wg2"  and bottom_rows["row2"][0] != "Wo2" and bottom_rows["row2"][0] != "Wb2" and bottom_rows["row3"][1] != "Wg2" and bottom_rows["row3"][1] != "Wb2" :
                reverse_back()
            else :
                reverse_bottom()
        i += 1
        
    if bottom_rows["row2"][0] == "Wg2":
        shift_bottom()
    elif  bottom_rows["row2"][2] == "Wg2":
        reverse_bottom()
    elif bottom_rows["row1"][1] == "Wg2":
        reverse_bottom()
        reverse_bottom()

###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################





def has_conner() :
    if right_rows["row1"][0].find("2") != -1 :
        return 11
    elif left_rows["row1"][0].find("2") != -1 :
        return 12
    elif back_rows["row1"][0].find("2") != -1 :
        return 13
    elif back_rows["row1"][2].find("2") != -1 :
        return 14
    elif front_rows["row1"][0].find("2") != -1 :
        return 15
    elif front_rows["row1"][2].find("2") != -1 :
        return 16
    elif right_rows["row1"][2].find("2") != -1 :
        return 17
    elif left_rows["row1"][2].find("2") != -1 :
        return 18
    return -1

########################
def has_lower_conners() :
    if right_rows["row3"][0].find("6") == -1 :
        return 1
    elif right_rows["row3"][2].find("6") == -1 :
        return 1
    elif back_rows["row3"][0].find("4") == -1 :
        return 1
    elif back_rows["row3"][2].find("4") == -1 :
        return 1
    elif front_rows["row3"][0].find("3") == -1 :
        return 1
    elif front_rows["row3"][2].find("3") == -1 :
        return 1
    elif left_rows["row3"][0].find("5") == -1 :
        return 1
    elif left_rows["row3"][2].find("5") == -1 :
        return 1
    return -1
########################
def bot() :
    i = 0
    if bottom_rows["row1"][0] == "Wbr2":
        i += 1
    if bottom_rows["row1"][1] == "Wb2" :
        i += 1
    if bottom_rows["row1"][2] == "Wob2":
        i += 1
    
    if bottom_rows["row2"][0] == "Wr2":
        i += 1
    if bottom_rows["row2"][1] == "W2" :
        i += 1
    if bottom_rows["row2"][2] == "Wo2":
        i += 1
    
    if bottom_rows["row3"][0] == "Wrg2" :
        i += 1
    if bottom_rows["row3"][1] == "Wg2" :
        i += 1
    if bottom_rows["row3"][2] == "Wgo2" :
        i += 1
    

    return i
########################
def lay_3() :
    i = 0
    while has_lower_conners() == 1:
        t  = 0
        while has_conner() != -1 :

            
            
            if back_rows["row1"][0].find("5") != -1  and left_rows["row1"][0].find("2") != -1:
                reverse_top()
            elif right_rows["row1"][2].find("5") != -1  and back_rows["row1"][2].find("2") != -1:
                shift_top()
                shift_top()
            elif front_rows["row1"][0].find("5") != -1  and right_rows["row1"][0].find("2") != -1:
                shift_top()
      
            elif left_rows["row1"][2].find("4") != -1  and front_rows["row1"][0].find("2") != -1:
                shift_top()
            elif right_rows["row1"][2].find("4") != -1  and back_rows["row1"][2].find("2") != -1:
                reverse_top()
          
            elif front_rows["row1"][2].find("4") != -1  and right_rows["row1"][2].find("2") != -1:
                shift_top()
                shift_top()
         
            elif right_rows["row1"][0].find("4") != -1  and front_rows["row1"][2].find("2") != -1:
                reverse_top()
          
            elif front_rows["row1"][0].find("4") != -1  and left_rows["row1"][2].find("2") != -1:
                shift_top()
                shift_top()
               
            elif left_rows["row1"][0].find("4") != -1  and back_rows["row1"][2].find("2") != -1:
                shift_top()
            
            elif right_rows["row1"][2].find("3") != -1  and back_rows["row1"][2].find("2") != -1:
                shift_top()
               
            elif back_rows["row1"][0].find("3") != -1  and left_rows["row1"][0].find("2") != -1:
                reverse_top()
                reverse_top()
            
            elif left_rows["row1"][2].find("3") != -1  and front_rows["row1"][0].find("2") != -1:
                reverse_top()
            
            elif right_rows["row1"][0].find("3") != -1  and front_rows["row1"][2].find("2") != -1:
                shift_top()
               
            elif back_rows["row1"][2].find("3") != -1  and right_rows["row1"][2].find("2") != -1:
                reverse_top()
                reverse_top()
                
            elif left_rows["row1"][0].find("3") != -1  and back_rows["row1"][0].find("2") != -1:
                reverse_top()
                
            elif back_rows["row1"][0].find("Oqw6") != -1  and left_rows["row1"][0].find("2") != -1:
                shift_top()
                
            elif left_rows["row1"][2].find("6") != -1  and front_rows["row1"][0].find("2") != -1:
                shift_top()
                shift_top()
                
            elif front_rows["row1"][2].find("6") != -1  and right_rows["row1"][0].find("2") != -1:
                reverse_top()
                
            elif back_rows["row1"][2].find("6") != -1  and right_rows["row1"][2].find("2") != -1:
                shift_top()
               
            elif left_rows["row1"][0].find("6") != -1  and back_rows["row1"][0].find("2") != -1:
                shift_top()
                shift_top()
               
            elif front_rows["row1"][0].find("6") != -1  and left_rows["row1"][2].find("2") != -1:
                reverse_top()
               
            elif front_rows["row1"][0].find("5") != -1  and left_rows["row1"][2].find("2") != -1:
                shift_top()
             
            elif right_rows["row1"][0].find("5") != -1  and front_rows["row1"][2].find("2") != -1:
                shift_top()
                shift_top()
           
            elif back_rows["row1"][2].find("5") != -1  and right_rows["row1"][2].find("2") != -1:
                reverse_top()
                
            
            if left_rows["row1"][2].find("5") != -1  and front_rows["row1"][0].find("2") != -1:
                shift_front()
                shift_top()
                reverse_front()

            elif left_rows["row1"][0].find("5") != -1  and back_rows["row1"][0].find("2") != -1:
                reverse_back()
                reverse_top()
                shift_back()
                
            elif right_rows["row1"][0].find("6") != -1  and front_rows["row1"][2].find("2") != -1:
                reverse_front()
                reverse_top()
                shift_front()

            elif right_rows["row1"][2].find("6") != -1  and back_rows["row1"][2].find("2") != -1:
                shift_back()
                shift_top()
                reverse_back()
            
            elif front_rows["row1"][2].find("3") != -1  and right_rows["row1"][0].find("2") != -1:
                shift_right()
                shift_top()
                reverse_right()

            elif front_rows["row1"][0].find("3") != -1  and left_rows["row1"][2].find("2") != -1:
                reverse_left()
                reverse_top()
                shift_left()
            
            elif back_rows["row1"][2].find("4") != -1  and right_rows["row1"][2].find("2") != -1:
                reverse_right()
                reverse_top()
                shift_right()

            elif back_rows["row1"][0].find("4") != -1  and left_rows["row1"][0].find("2") != -1:
                shift_left()
                shift_top()
                reverse_left()
            else :
                shift_top()
            
            t += 1

        if top_edges_in_place(top_rows) != 1:
            if top_rows["row3"][0].find("2") != -1:
                shift_front()
                shift_top()
                shift_top()
                reverse_front()
            elif top_rows["row3"][2].find("2") != -1:
                reverse_front()
                shift_top()
                shift_top()
                shift_front()
            elif top_rows["row1"][0].find("2") != -1:
                reverse_back()
                shift_top()
                shift_top()
                shift_back()
            elif top_rows["row1"][2].find("2") != -1:
                reverse_right()
                shift_top()
                shift_top()
                shift_right()
        if left_rows["row3"][0].find("2") != -1:
            shift_left()
            shift_top()
            shift_top()
            reverse_left()
        elif left_rows["row3"][2].find("2") != -1:
            shift_front()
            shift_top()
            shift_top()
            reverse_front()
        elif right_rows["row3"][2].find("2") != -1:
            reverse_right()
            shift_top()
            shift_top()
            shift_right()
        elif right_rows["row3"][0].find("2") != -1:
            shift_right()
            shift_top()
            shift_top()
            reverse_right()
        elif back_rows["row3"][0].find("2") != -1:
            shift_back()
            shift_top()
            shift_top()
            reverse_back()
        elif back_rows["row3"][2].find("2") != -1:
            shift_back()
            shift_top()
            shift_top()
            reverse_back()
        elif front_rows["row3"][0].find("2") != -1:
            shift_front()
            shift_top()
            shift_top()
            reverse_front()
        elif front_rows["row3"][2].find("2") != -1:
            shift_front()
            shift_top()
            shift_top()
            reverse_front()
        

        i += 1







###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################


def has_midlle_edges() :
    if right_rows["row2"][0].find("6") == -1 :
        return 1
    elif right_rows["row2"][2].find("6") == -1 :
        return 1
    elif back_rows["row2"][0].find("4") == -1 :
        return 1
    elif back_rows["row2"][2].find("4") == -1 :
        return 1
    elif front_rows["row2"][0].find("3") == -1 :
        return 1
    elif front_rows["row2"][2].find("3") == -1 :
        return 1
    elif left_rows["row2"][0].find("5") == -1 :
        return 1
    elif left_rows["row2"][2].find("5") == -1 :
        return 1
    return -1

def has_midlle_center_edges() :
    if right_rows["row1"][1].find("1") == -1 and top_rows["row2"][2].find("1") == -1 :
        return 1
    elif back_rows["row1"][1].find("1") == -1 and top_rows["row1"][1].find("1") == -1 :
        return 1
    elif front_rows["row1"][1].find("1") == -1 and top_rows["row3"][1].find("1") == -1:
        return 1
    elif left_rows["row1"][1].find("1") == -1 and top_rows["row2"][0].find("1") == -1 :
        return 1
    return -1

def lay_2() :
    i = has_midlle_center_edges()
    p = 0
    c = 0
    while  has_midlle_edges() != -1 :
        d = 0
        while has_midlle_center_edges()  == 1:
          
            if left_rows["row1"][1].find("3") != -1 and top_rows["row2"][0].find("6") != -1 :
                shift_right()
                shift_top()
                reverse_right()
                reverse_top()
                reverse_front()
                reverse_top()
                shift_front()
                
            
            elif right_rows["row1"][1].find("4") != -1 and top_rows["row2"][2].find("5") != -1 :
                shift_left()
                shift_top()
                reverse_left()
                reverse_top()
                reverse_back()
                reverse_top()
                shift_back()
             

            elif left_rows["row1"][1].find("4") != -1 and top_rows["row2"][0].find("6") != -1 :
                reverse_right()
                reverse_top()
                shift_right()
                shift_top()
                shift_back()
                shift_top()
                reverse_back()
                
            
            elif back_rows["row1"][1].find("6") != -1 and top_rows["row1"][1].find("3") != -1 :
                reverse_front()
                reverse_top()
                shift_front()
                shift_top()
                shift_right()
                shift_top()
                reverse_right()
                

            elif front_rows["row1"][1].find("6") != -1 and top_rows["row3"][1].find("4") != -1 :
                shift_back()
                shift_top()
                reverse_back()
                reverse_top()
                reverse_right()
                reverse_top()
                shift_right()
                
            
            elif back_rows["row1"][1].find("5") != -1 and top_rows["row1"][1].find("3") != -1 :
                shift_front()
                shift_top()
                reverse_front()
                reverse_top()
                reverse_left()
                reverse_top()
                shift_left()
                

            elif front_rows["row1"][1].find("5") != -1 and top_rows["row3"][1].find("4") != -1 :
                reverse_back()
                reverse_top()
                shift_back()
                shift_top()
                shift_left()
                shift_top()
                reverse_left()
            
            elif right_rows["row1"][1].find("3") != -1 and top_rows["row2"][2].find("5") != -1 :
                reverse_left()
                reverse_top()
                shift_left()
                shift_top()
                shift_front()
                shift_top()
                reverse_front()
                
            

            if back_rows["row1"][1].find("3") != -1 and top_rows["row1"][1].find("5") != -1 :
                shift_top()
              
            elif front_rows["row1"][1].find("3") != -1 and top_rows["row3"][1].find("5") != -1 :
                reverse_top()
                
            elif right_rows["row2"][0].find("3") != -1 and top_rows["row2"][0].find("5") != -1 :
                reverse_top()
                reverse_top()
            elif right_rows["row1"][1].find("5") != -1 and top_rows["row2"][2].find("4") != -1 :
                shift_top()
                
            elif left_rows["row1"][1].find("5") != -1 and top_rows["row2"][0].find("4") != -1 :
                reverse_top()
                
            elif back_rows["row1"][1].find("5") != -1 and top_rows["row1"][1].find("4") != -1 :
                reverse_top()
                reverse_top()
                
            elif left_rows["row1"][1].find("5") != -1 and top_rows["row2"][0].find("3") != -1 :
                shift_top()
        
            elif right_rows["row1"][1].find("5") != -1 and top_rows["row2"][2].find("3") != -1 :
                reverse_top()
                
            elif front_rows["row1"][1].find("5") != -1 and top_rows["row3"][1].find("3") != -1 :
                shift_top()
                shift_top()
                
            elif left_rows["row1"][1].find("6") != -1 and top_rows["row2"][0].find("4") != -1 :
                reverse_top()
                
            elif right_rows["row1"][1].find("6") != -1 and top_rows["row2"][2].find("4") != -1 :
                shift_top()
                
            elif back_rows["row1"][1].find("6") != -1 and top_rows["row1"][1].find("4") != -1 :
                reverse_top()
                reverse_top()
                
            elif left_rows["row1"][1].find("6") != -1 and top_rows["row2"][0].find("3") != -1 :
                shift_top()
                
            elif right_rows["row1"][1].find("6") != -1 and top_rows["row2"][2].find("3") != -1 :
                reverse_top()
                
            elif front_rows["row1"][1].find("6") != -1 and top_rows["row3"][1].find("3") != -1 :
                reverse_top()
                reverse_top()
                
            elif back_rows["row1"][1].find("4") != -1 and top_rows["row1"][1].find("5") != -1 :
                shift_top()
                
            elif front_rows["row1"][1].find("4") != -1 and top_rows["row3"][1].find("5") != -1 :
                reverse_top()
                
            elif left_rows["row1"][1].find("4") != -1 and top_rows["row2"][0].find("5") != -1 :
                shift_top()
                shift_top()
            
            elif front_rows["row1"][1].find("4") != -1 and top_rows["row3"][1].find("6") != -1 :
                shift_top()
                
            elif back_rows["row1"][1].find("4") != -1 and top_rows["row3"][1].find("6") != -1 :
                reverse_top
        
            elif right_rows["row1"][1].find("4") != -1 and top_rows["row2"][2].find("6") != -1 :
                shift_top()
                shift_top()
                
            elif front_rows["row1"][1].find("3") != -1 and top_rows["row3"][1].find("6") != -1 :
                shift_top()
                
            elif back_rows["row1"][1].find("3") != -1 and top_rows["row1"][1].find("6") != -1 :
                reverse_top()
            
            elif right_rows["row1"][1].find("3") != -1 and top_rows["row2"][2].find("6") != -1 :
                shift_top()
                shift_top()
            else :
                shift_top()
            
            d += 1

        if right_rows["row2"][0].find("6") == -1 :
            reverse_front()
            shift_top()
            shift_top()
            shift_front()
           
        elif right_rows["row2"][2].find("6") == -1 :
            shift_back()
            shift_top()
            shift_top()
            reverse_back()
            
        elif back_rows["row2"][0].find("4") == -1 :
            shift_left()
            shift_top()
            shift_top()
            reverse_left()

        elif back_rows["row2"][2].find("4") == -1 :
            reverse_right()
            shift_top()
            shift_top()
            shift_right()

        elif front_rows["row2"][0].find("3") == -1 :
            reverse_left()
            shift_top()
            shift_top()
            shift_left()

        elif front_rows["row2"][2].find("3") == -1 :
            shift_right()
            shift_top()
            shift_top()
            reverse_right()
           
        elif left_rows["row2"][0].find("5") == -1 :
            reverse_back()
            shift_top()
            shift_back()
            
        elif left_rows["row2"][2].find("5") == -1 :
            shift_front()
            shift_top()
            shift_top()
            reverse_front()
            
        lay_3()
        c +=1












###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################



def has_top_x() :
    if top_rows["row1"][1].find("1") == -1:
        return 1
    if top_rows["row2"][2].find("1") == -1:
        return 1
    if top_rows["row3"][1].find("1") == -1:
        return 1
    if top_rows["row2"][0].find("1") == -1:
        return 1

    return -1

def top_who()  :
    if  top_rows["row2"][0].find("1") != -1 and  top_rows["row2"][2].find("1") != -1 and  top_rows["row1"][1].find("1") != -1 and  top_rows["row3"][1].find("1") == -1:
        return 1
    if  top_rows["row2"][0].find("1") != -1 and  top_rows["row2"][2].find("1") != -1 and  top_rows["row1"][1].find("1") == -1 and  top_rows["row3"][1].find("1") == -1:
        return 1
    if  top_rows["row2"][0].find("1") != -1 and  top_rows["row2"][2].find("1") != -1 and  top_rows["row1"][1].find("1") == -1 and  top_rows["row3"][1].find("1") != -1:
        return 1
    if  top_rows["row2"][0].find("1") == -1 and  top_rows["row2"][2].find("1") != -1 and  top_rows["row1"][1].find("1") != -1 and  top_rows["row3"][1].find("1") != -1:
        return 2
    if  top_rows["row2"][0].find("1") != -1 and  top_rows["row2"][2].find("1") == -1 and  top_rows["row1"][1].find("1") != -1 and  top_rows["row3"][1].find("1") == -1:
        return 2
    if  top_rows["row2"][0].find("1") == -1 and  top_rows["row2"][2].find("1") == -1 and  top_rows["row1"][1].find("1") == -1 and  top_rows["row3"][1].find("1") == -1:
        return 4
    if  top_rows["row2"][0].find("1") != -1 and  top_rows["row2"][2].find("1") == -1 and  top_rows["row1"][1].find("1") != -1 and  top_rows["row3"][1].find("1") == -1:
        return 1
    if  top_rows["row2"][0].find("1") != -1 and  top_rows["row2"][2].find("1") == -1 and  top_rows["row1"][1].find("1") == -1 and  top_rows["row3"][1].find("1") != -1:
        return 2
    if  top_rows["row2"][0].find("1") == -1 and  top_rows["row2"][2].find("1") != -1 and  top_rows["row1"][1].find("1") != -1 and  top_rows["row3"][1].find("1") == -1:
        return 3

def top_x() :
    i = 0

    while  has_top_x() != -1 :
        if top_who() == 1 :
            shift_front()
            shift_right()
            shift_top()
            reverse_right()
            reverse_top()
            reverse_front()
            if has_top_x() != -1 :
                shift_front()
                shift_right()
                shift_top()
                reverse_right()
                reverse_top()
                reverse_front()
        elif top_who() == 2 :
            shift_top()
            shift_front()
            shift_right()
            shift_top()
            reverse_right()
            reverse_top()
            reverse_front()
            if has_top_x() != -1 :
                shift_front()
                shift_right()
                shift_top()
                reverse_right()
                reverse_top()
                reverse_front() 

        elif top_who() == 3 :
            reverse_top()
            shift_front()
            shift_right()
            shift_top()
            reverse_right()
            reverse_top()
            reverse_front()
            if has_top_x() != -1 :
                shift_front()
                shift_right()
                shift_top()
                reverse_right()
                reverse_top()
                reverse_front()

        elif top_who() == 4 :
            reverse_top()
            reverse_top()
            shift_front()
            shift_right()
            shift_top()
            reverse_right()
            reverse_top()
            reverse_front()
        else :
            shift_top()
        i += 1




###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################


def has_little_fish() :
    i = 0
    if front_rows["row1"][1] == "Gy3"  :
        i += 1
    if right_rows["row1"][1] == "Oy6" :
        i += 1
    if left_rows["row1"][1] == "Ry5" :
        i += 1
    if back_rows["row1"][1] == "By4" :
        i += 1
    return i


def do_fish() :
    i = 0
    while True :
        if top_rows["row1"][1] == "Yb1" and top_rows["row3"][1] == "Yg1" and top_rows["row2"][2] != "Yo1" : 
            shift_right()
            shift_top()
            reverse_right()
            shift_top()
            shift_right()
            shift_top()
            shift_top()
            reverse_right()

        elif top_rows["row1"][1] == "Yg1" and top_rows["row3"][1] == "Yb1" and top_rows["row2"][0] != "Yr1"  :
            shift_top()
            shift_top()
            shift_right()
            shift_top()
            reverse_right()
            shift_top()
            shift_right()
            shift_top()
            shift_top()
            reverse_right()

        elif top_rows["row2"][0] == "Yb1" and top_rows["row2"][2] == "Yg1" and top_rows["row1"][1] != "Yo1"  :
            reverse_top()
            shift_right()
            shift_top()
            reverse_right()
            shift_top()
            shift_right()
            shift_top()
            shift_top()
            reverse_right()

        elif top_rows["row2"][0] == "Yg1" and top_rows["row2"][2] == "Yb1" and top_rows["row3"][1] != "Yo1"  :
            shift_top()
            shift_right()
            shift_top()
            reverse_right()
            shift_top()
            shift_right()
            shift_top()
            shift_top()
            reverse_right()

        elif top_rows["row1"][1] == "Yr1" and top_rows["row3"][1] == "Yo1" and top_rows["row2"][0] != "Yg1"  :
            shift_top()
            shift_top()
            shift_front()
            shift_top()
            reverse_front()
            shift_top()
            shift_front()
            shift_top()
            shift_top()
            reverse_front()

        elif top_rows["row1"][1] == "Yo1" and top_rows["row3"][1] == "Yr1" and top_rows["row2"][2] != "Yg1" :
            reverse_top() 
            shift_top()
            shift_front()
            shift_top()
            reverse_front()
            shift_top()
            shift_front()
            shift_top()
            shift_top()
            reverse_front()

        elif top_rows["row2"][0] == "Yr1" and top_rows["row2"][2] == "Yo1" and top_rows["row3"][1] != "Yg1" :
            shift_top()
            shift_front()
            shift_top()
            reverse_front()
            shift_top()
            shift_front()
            shift_top()
            shift_top()
            reverse_front()

        elif top_rows["row2"][1] == "Yo1" and top_rows["row3"][2] == "Yr1" and top_rows["row2"][2] != "Yg1" :
            shift_top()
            shift_top()
            shift_top()
            shift_front()
            shift_top()
            reverse_front()
            shift_top()
            shift_front()
            shift_top()
            shift_top()
            reverse_front() 

        elif top_rows["row1"][1] == "Yr1" and top_rows["row2"][0] == "Yg1" and top_rows["row3"][1] != "Yo1" :
            reverse_top()
            shift_top()
            shift_left()
            shift_top()
            reverse_left()
            shift_top()
            shift_left()
            shift_top()
            shift_top()
            reverse_left()
            shift_top()

        elif top_rows["row2"][0] == "Yr1" and top_rows["row3"][1] == "Yg1" and top_rows["row2"][2] != "Yo1"  :
            shift_top()
            shift_top()
            shift_left()
            shift_top()
            reverse_left()
            shift_top()
            shift_left()
            shift_top()
            shift_top()
            reverse_left()

        elif top_rows["row2"][2] == "Yg1" and top_rows["row3"][1] == "Yr1" and top_rows["row1"][1] != "Yo1" :
            shift_top()
            shift_top()
            shift_left()
            shift_top()
            reverse_left()
            shift_top()
            shift_left()
            shift_top()
            shift_top()
            reverse_left()

        elif top_rows["row2"][2] == "Yr1" and top_rows["row1"][1] == "Yg1" and top_rows["row2"][0] != "Yo1" :
            shift_top()
            shift_top()
            shift_left()
            shift_top()
            reverse_left()
            shift_top()
            shift_left()
            shift_top()
            shift_top()
            reverse_left()
        
        elif top_rows["row1"][1] == "Yo1" and top_rows["row2"][0] == "Yb1" and top_rows["row2"][2] != "Yg1" :
            reverse_top()
            shift_right()
            shift_top()
            reverse_right()
            shift_top()
            shift_right()
            shift_top()
            shift_top()
            reverse_right()

        elif top_rows["row2"][0] == "Yo1" and top_rows["row3"][1] == "Yb1" and top_rows["row1"][1] != "Yg1"  : 
            shift_top()
            shift_top()
            shift_right()
            shift_top()
            reverse_right()
            shift_top()
            shift_right()
            shift_top()
            shift_top()
            reverse_right()

        elif top_rows["row2"][2] == "Yb1" and top_rows["row3"][1] == "Yo1" and top_rows["row2"][0] != "Yg1"  :
            shift_top()
            shift_right()
            shift_top()
            reverse_right()
            shift_top()
            shift_right()
            shift_top()
            shift_top()
            reverse_right()

        elif top_rows["row2"][2] == "Yo1" and top_rows["row1"][1] == "Yb1" and top_rows["row3"][1] != "Yg1"   :
            shift_right()
            shift_top()
            reverse_right()
            shift_top()
            shift_right()
            shift_top()
            shift_top()
            reverse_right()

        elif top_rows["row1"][1] == "Yo1" and top_rows["row2"][0] != "Yb1" and top_rows["row2"][2] == "Yg1" :
            shift_top()
            shift_front()
            shift_top()
            reverse_front()
            shift_top()
            shift_front()
            shift_top()
            shift_top()
            reverse_front()

        elif top_rows["row2"][0] == "Yo1" and top_rows["row3"][1] != "Yb1" and top_rows["row1"][1] == "Yg1"  : 
            shift_top()
            shift_top()
            shift_front()
            shift_top()
            reverse_front()
            shift_top()
            shift_front()
            shift_top()
            shift_top()
            reverse_front()

        elif top_rows["row2"][2] != "Yb1" and top_rows["row3"][1] == "Yo1" and top_rows["row2"][0] == "Yg1"  :
            shift_top()
            shift_front()
            shift_top()
            reverse_front()
            shift_top()
            shift_front()
            shift_top()
            shift_top()
            reverse_front()

        elif top_rows["row2"][2] == "Yo1" and top_rows["row1"][1] != "Yb1" and top_rows["row3"][1] == "Yg1"   :
            shift_front()
            shift_top()
            reverse_front()
            shift_top()
            shift_front()
            shift_top()
            shift_top()
            reverse_front()
        
        elif top_rows["row1"][1] == "Yb1" and top_rows["row3"][1] == "Yg1" and top_rows["row2"][2] == "Yo1" : 
            break
        elif top_rows["row1"][1] == "Yg1" and top_rows["row3"][1] == "Yb1" and top_rows["row2"][0] == "Yo1"  : 
            shift_top()
            shift_top()
        elif top_rows["row2"][0] == "Yb1" and top_rows["row2"][2] == "Yg1" and top_rows["row1"][1] == "Yo1"  : 
            shift_top()
        elif top_rows["row2"][0] == "Yg1" and top_rows["row2"][2] == "Yb1" and top_rows["row3"][1] == "Yo1"  : 
            reverse_top()
        else :
            while front_rows["row1"][1] != "Gy3" :
                shift_top()
            shift_right()
            shift_top()
            reverse_right()
            shift_top()
            shift_right()
            shift_top()
            shift_top()
            reverse_right()
        i += 1         




###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################

def second_last():
    i = 0
    if top_rows["row1"][0].find("h") != -1 and back_rows["row1"][0].find("h") != -1 and left_rows["row1"][0].find("h") != -1:
       i +=1
    if top_rows["row1"][2].find("j") != -1 and back_rows["row1"][2].find("j") != -1 and right_rows["row1"][2].find("j") != -1 :
       i +=1
    if top_rows["row3"][0].find("k") != -1 and front_rows["row1"][0].find("k") != -1 and left_rows["row1"][2].find("k") != -1 :
       i +=1
    if top_rows["row3"][2].find("i") != -1 and front_rows["row1"][2].find("i") != -1 and right_rows["row1"][0].find("i") != -1 :
       i +=1
    return i

def do_second_last():
    i = 0
    while True :
        if second_last() == 0  :
            shift_top()
            shift_right()
            reverse_top()
            reverse_left()
            shift_top()
            reverse_right()
            reverse_top()
            shift_left()
            
        elif second_last() == 4 :
            break
        elif second_last() == 2 or second_last() == 1 or second_last() == 3:
            if top_rows["row1"][0].find("h") != -1 and back_rows["row1"][0].find("h") != -1 and left_rows["row1"][0].find("h") != -1:
                shift_top()
                shift_left()
                reverse_top()
                reverse_right()
                shift_top()
                reverse_left()
                reverse_top()
                shift_right()
                
            elif top_rows["row1"][2].find("j") != -1 and back_rows["row1"][2].find("j") != -1 and right_rows["row1"][2].find("j") != -1 :
                shift_top()
                shift_back()
                reverse_top()
                reverse_front()
                shift_top()
                reverse_back()
                reverse_top()
                shift_front()

            elif top_rows["row3"][0].find("k") != -1 and front_rows["row1"][0].find("k") != -1 and left_rows["row1"][2].find("k") != -1 :
                shift_top()
                shift_front()
                reverse_top()
                reverse_back()
                shift_top()
                reverse_front()
                reverse_top()
                shift_back()

            elif top_rows["row3"][2].find("i") != -1 and front_rows["row1"][2].find("i") != -1 and right_rows["row1"][0].find("i") != -1 :
                shift_top()
                shift_right()
                reverse_top()
                reverse_left()
                shift_top()
                reverse_right()
                reverse_top()
                shift_left()
        i += 1




###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################



def last() :
    i = 0
    if front_rows["row1"][0] != "Gyr3--k" :
        i += 1
    elif front_rows["row1"][1] != "Gy3"  :
        i += 1
    elif  front_rows["row1"][2] != "Gyo3--i" :
        i += 1
    elif left_rows["row1"][0] != "Rby5--h" :
        i += 1
    elif left_rows["row1"][1] != "Ry5" :
        i += 1
    elif left_rows["row1"][2] != "Rgy5--k" :
        i += 1
    elif back_rows["row1"][0] != "Bry4--h" :
        i += 1
    elif back_rows["row1"][1] != "By4" :
        i += 1
    elif back_rows["row1"][2] != "Boy4--j" :
        i += 1
    elif right_rows["row1"][0] != "Ogy6--i":
        i += 1
    elif right_rows["row1"][1] != "Oy6" :
        i += 1
    elif right_rows["row1"][2] != "Oby6--j" :
        i += 1
    return i

def one_two() :
    reverse_right()
    reverse_bottom()
    shift_right()
    shift_bottom()
    reverse_right()
    reverse_bottom()
    shift_right()
    shift_bottom()

def do_last() :
     while  True :

        if  top_rows["row3"][1] == "Yg1" and top_rows["row3"][2] == "Ygo1--i" and  last()  != 0:
            shift_top()
        elif  top_rows["row3"][1] == "Yo1" and top_rows["row3"][2] == "Ybo1--j"  and  last()  != 0:
            shift_top()
        elif  top_rows["row3"][1] == "Yb1" and top_rows["row3"][2] == "Ybr1--h"  and  last()  != 0:
            shift_top()
        elif  top_rows["row3"][1] == "Yr1" and top_rows["row3"][2] == "Yrg1--k"  and  last()  != 0:
            shift_top()
        elif last()  == 0:
            break
        else :
            one_two()




###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
def main(mix):

    
    # reverse_back()
    global moves 
    mix = mix.split(" ")

    for mv in mix :
        if mv == "R" :
            shift_right()
        elif mv == "L" :
            shift_left()
        elif mv == "U" :
            shift_top()
        elif mv == "D'" : 
            reverse_bottom()
        elif mv == "F" :
            shift_front()
        elif mv == "B" :
            shift_back()
        elif mv == "R'" :
            reverse_right()
        elif mv == "L'" :
            reverse_left()
        elif mv == "U'" :
            reverse_top()
        elif mv == "D" :
            shift_bottom()
        elif mv == "F'" :
            reverse_front()
        elif mv == "B'" :
            reverse_back()
        elif mv == "R2" :
            shift_right()
            shift_right()
        elif mv == "L2" :
            shift_left()
            shift_left()
        elif mv == "U2" :
            shift_top()
            shift_top()
        elif mv == "D'2" :
            reverse_bottom()
            reverse_bottom()
        elif mv == "F2" :
            shift_front()
            shift_front()
        elif mv == "B2" :
            shift_back()
            shift_back()
        elif mv == "R'2" :
            reverse_right()
            reverse_right()
        elif mv == "L'2" :
            reverse_left()
            reverse_left()
        elif mv == "U'2" :
            reverse_top()
            reverse_top()
        elif mv == "D2" :
            shift_bottom()
            shift_bottom()
        elif mv == "F'2" :
            reverse_front()
            reverse_front()
        elif mv == "B'2" :
            reverse_back()
            reverse_back()
        else :
            print("movement incorrect : " + mv )
            return
    moves = moves + " : "

    moves = moves[moves.find(":") + 1:]
    i = 0

    # # res = moves.split(" ")

    if top_rows["row1"][0] == "Ybr1--h" :
        i += 1
    if top_rows["row1"][1] == "Yb1":
        i += 1
    if top_rows["row1"][2] == "Ybo1--j" :
        i += 1
    if top_rows["row2"][0] == "Yr1":
        i += 1
    if top_rows["row2"][1] ==  "Y1" :
        i += 1
    if top_rows["row2"][2] == "Yo1":
        i += 1
    if top_rows["row3"][0] == "Yrg1--k":
        i += 1
    if top_rows["row3"][1] == "Yg1":
        i += 1
    if top_rows["row3"][2] == "Ygo1--i":
        i += 1
    if bottom_rows["row1"][0] == "Wbr2":
        i += 1
    if bottom_rows["row1"][1] == "Wb2" :
        i += 1
    if bottom_rows["row1"][2] == "Wob2":
        i += 1
    
    if bottom_rows["row2"][0] == "Wr2":
        i += 1
    if bottom_rows["row2"][1] == "W2" :
        i += 1
    if bottom_rows["row2"][2] == "Wo2":
        i += 1
    
    if bottom_rows["row3"][0] == "Wrg2" :
        i += 1
    if bottom_rows["row3"][1] == "Wg2" :
        i += 1
    if bottom_rows["row3"][2] == "Wgo2" :
        i += 1
    
    if front_rows["row1"][0] ==  "Gyr3--k" :
        i += 1 
    if front_rows["row1"][1] ==  "Gy3" :
        i += 1 
    if front_rows["row1"][2] ==  "Gyo3--i":
        i += 1 
    if front_rows["row2"][0]== "Gr3" :
        i += 1 
    if front_rows["row2"][1]== "G3":
        i += 1 
    if front_rows["row2"][2]== "Go3":
        i += 1 
    if front_rows["row3"][0] == "Grw3":
        i += 1 
    if front_rows["row3"][1] =="Gw3" :
        i += 1 
    if front_rows["row3"][2] =="Gow3":
        i += 1 
    if back_rows["row1" ][0] == "Bry4--h" :
        i += 1 
    if back_rows["row1" ][1] == "By4" :
        i += 1 
    if back_rows["row1" ][2] == "Boy4--j":
        i += 1 
    if back_rows["row2" ][0] == "Br4" :
        i += 1 
    if back_rows["row2" ][1] == "B4" :
        i += 1 
    if back_rows["row2" ][2] == "Bo4":
        i += 1 
    if back_rows["row3" ][0]== "Brw4" :
        i += 1 
    if back_rows["row3" ][1]== "Bw4" :
        i += 1 
    if back_rows["row3" ][2]== "Bwo4":
        i += 1
    if i == 18 + 18 :
        return

    # print("@@@")
    if len(mix)  < 6 :
        i = 0
    elif len(mix)  > 5  and  len(mix)  < 30 :
        i = 1
    else :
        i = 3
    while i < 0:
        for mv in mix :
            if mv == "R" :
                shift_right()
            elif mv == "L" :
                shift_left()
            elif mv == "U" :
                shift_top()
            elif mv == "D'" : 
                reverse_bottom()
            elif mv == "F" :
                shift_front()
            elif mv == "B" :
                shift_back()
            elif mv == "R'" :
                reverse_right()
            elif mv == "L'" :
                reverse_left()
            elif mv == "U'" :
                reverse_top()
            elif mv == "D" :
                shift_bottom()
            elif mv == "F'" :
                reverse_front()
            elif mv == "B'" :
                reverse_back()
            elif mv == "R2" :
                shift_right()
                shift_right()
            elif mv == "L2" :
                shift_left()
                shift_left()
            elif mv == "U2" :
                shift_top()
                shift_top()
            elif mv == "D'2" :
                reverse_bottom()
                reverse_bottom()
            elif mv == "F2" :
                shift_front()
                shift_front()
            elif mv == "B2" :
                shift_back()
                shift_back()
            elif mv == "R'2" :
                reverse_right()
                reverse_right()
            elif mv == "L'2" :
                reverse_left()
                reverse_left()
            elif mv == "U'2" :
                reverse_top()
                reverse_top()
            elif mv == "D2" :
                shift_bottom()
                shift_bottom()
            elif mv == "F'2" :
                reverse_front()
                reverse_front()
            elif mv == "B'2" :
                reverse_back()
                reverse_back()
        i += 1
    # shift_front()
    # shift_top()
    # shift_top()
    # reverse_front()
    bottom_crose()
    lay_3() 
    lay_2()
    top_x()
    do_fish()
    do_second_last()
    do_last()
    # print("@@@")
    
    res = moves
    res = res.split(" ")
    b = len(res)
    c = 0
    zlt = ""
    while c < b - 1 :
        if res[c] == res[c + 1] :
            zlt = zlt +" "+ res[c] +"2"
            c += 2
        else :
             zlt = zlt +" "+ res[c]
             c += 1

    print(zlt)
    root = Tk()
    root.geometry("600x600")
    m1 = side(top_rows,"top")
    m2 = side(bottom_rows,"bottom")
    m3 = side(back_rows,"back")
    m4 = side(front_rows,"front")
    m5 = side(left_rows,"left")
    m6 = side(right_rows,"right")
    mainloop()

import sys

if __name__ == "__main__":
    if len(sys.argv) == 2 :
        main(sys.argv[1])
    else :
        print("input error")
    sys.exit(2)

