
top_rows = {
    "row1" : ["Ybr1","Yb1","Ybo1"],
    "row2" : ["Yr1","Y1","Yo1"],
    "row3" : ["Yrg1","Yg1","Ygo1"]
}

bottom_rows = {
    "row1" : ["Wbr2","Wb2","Wob2"],
    "row2" : ["Wr2","W2","Wo2"],
    "row3" : ["Wrg2","Wg2","Wgo2"]
}

front_rows = {
    "row1" : ["Gyr3","Gy3","Gyo3"],
    "row2" : ["Gr3","G3","Go3"],
    "row3" : ["Grw3","Gw3","Gow3"],
}

back_rows = {
    "row1" : ["Bry4","By4","Boy4"],
    "row2" : ["Br4","B4","Bo4"],
    "row3" : ["Brw4","Bw4","Bwo4"],
}

left_rows = {
    "row1" : ["Rby5","Ry5","Rgy5"],
    "row2" : ["Rb5","R5","Rg5"],
    "row3":  ["Rbw5","Rw5","Rwg5"],
}

right_rows = {
    "row1" : ["Ogy6","Oy6","Oby6"],
    "row2" : ["Og6","O6","Ob6"],
    "row3" : ["Ogw6","Ow6","Obw6"],
}

def shift_top() :
    print("U")
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
    print("U'")
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
def shift_bottom() :
    print("D")
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

def reverse_bottom() :
    print("D'")
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
    print("F")
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
    print("F'")
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
    print("B'")
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
    print("B")
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
def shift_left() :
    print("L")
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

def  reverse_left() :
    print("L'")
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
    print("R")
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
    print("R'")
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

####################
def place_front_row_1_right() : 
    shift_right()
    shift_top()
    reverse_right()
    print("place_front_right")

def place_front_row_1_left() : 
    shift_left()
    reverse_top()
    reverse_left()
    print("place_front_left")

def place_back_row_1_left() : 
    reverse_left()
    shift_top()
    shift_left()
    print("place_back_left")

def place_back_row_1_right() : 
    reverse_right()
    reverse_top()
    shift_right()
    print("place_back_right")

def place_right_row_1_left():
    reverse_front()
    reverse_top()
    shift_front()
    print("place_right_left")

def place_right_row_1_right():
    reverse_back()
    shift_top()
    shift_back()
    print("place_right_right")

def place_left_row_1_right():
    shift_front()
    shift_top()
    reverse_front()
    print("place_left_right")

def place_left_row_1_left():
    shift_back()
    reverse_top()
    reverse_back()
    print("place_left_left")

###################
def place_right_row_2_right() :
    shift_right()
    reverse_top()
    reverse_right()
    shift_top()
    place_right_row_1_right()

def place_right_row_2_left() :
    reverse_right()
    shift_top()
    shift_right()
    reverse_top()
    place_right_row_1_left()

def place_left_row_2_right() :
    shift_left()
    reverse_top()
    reverse_left()
    shift_front()
    place_left_row_1_right()

def place_left_row_2_left() :
    reverse_left()
    shift_top()
    shift_left()
    reverse_front()
    place_left_row_1_left()

def place_back_row_2_right() :
    shift_back()
    reverse_top()
    reverse_back()
    shift_top()
    place_back_row_1_right()

def place_back_row_2_left() :
    reverse_back()
    shift_top()
    shift_back()
    reverse_top()
    place_back_row_1_left()

def place_front_row_2_right() :
    shift_front()
    shift_top()
    reverse_front()
    reverse_top()
    place_front_row_1_right()

def place_front_row_2_left() :
    reverse_front()
    reverse_top()
    shift_front()
    shift_top()
    place_front_row_1_left()

#################
def front_cross() :
    shift_front()
    shift_right()
    shift_top()
    reverse_right()
    reverse_top()
    reverse_front()

def back_cross() :
    reverse_back()
    reverse_left()
    shift_top()
    shift_left()
    reverse_top()
    shift_back()

def right_cross() :
    shift_right()
    reverse_back()
    shift_top()
    shift_back()
    reverse_top()
    reverse_right()

def left_cross() :
    reverse_left()
    shift_front()
    shift_top()
    reverse_front()
    reverse_top()
    shift_left()

###################
def front_big_fish() :
    shift_right()
    reverse_top()
    reverse_top()
    reverse_right()
    reverse_top()
    shift_right()
    reverse_top()
    reverse_right()

def right_big_fish() :
    reverse_back()
    reverse_top()
    reverse_top()
    shift_back()
    reverse_top()
    reverse_back()
    reverse_top()
    shift_back()

def left_big_fish() :
    shift_front()
    reverse_top()
    reverse_top()
    reverse_front()
    reverse_top()
    shift_front()
    reverse_top()
    reverse_front()

def back_big_fish() :
    reverse_left()
    reverse_top()
    reverse_top()
    shift_left()
    reverse_top()
    reverse_left()
    reverse_top()
    shift_left()

#######################
def front_little_fish() :
    shift_right()
    shift_top()
    reverse_right()
    shift_top()
    shift_right()
    shift_top()
    shift_top()
    reverse_right()

def back_little_fish() :
    reverse_left()
    shift_top()
    shift_left()
    shift_top()
    reverse_left()
    shift_top()
    shift_top()
    shift_left()

def left_little_fish() :
    shift_front()
    shift_top()
    reverse_left()
    shift_top()
    shift_front()
    shift_top()
    shift_top()
    reverse_front()

def right_little_fish() :
    reverse_back()
    shift_top()
    shift_back()
    shift_top()
    reverse_back()
    shift_top()
    shift_top()
    shift_back()

##########################
def front_double_fish() :
    front_little_fish()
    front_little_fish()

def back_double_fish() :
    back_little_fish()
    back_little_fish()

def left_double_fish() :
    left_little_fish()
    left_little_fish()

def right_double_fish() : 
    right_little_fish()
    right_little_fish()

###################

def left_left_kick() :
    shift_back()
    reverse_top()
    reverse_top()
    reverse_back()

def left_right_kick() :
    shift_front()
    shift_top()
    shift_top()
    reverse_front()

def right_right_kick() :
    reverse_back()
    shift_top()
    shift_top()
    shift_back()

def right_left_kick() :
    reverse_front()
    shift_top()
    shift_top()
    shift_front()

def front_left_kick() :
    shift_left()
    shift_top()
    shift_top()
    reverse_left()

def front_right_kick() :
    shift_right()
    shift_top()
    shift_top()
    reverse_right()

def back_right_kick() :
    reverse_right()
    shift_top()
    shift_top()
    shift_right()

def back_left_kick() :
    reverse_left()
    shift_top()
    shift_top()
    shift_left()


###################
def place_front_row_3() :
    shift_right()
    shift_right()
    shift_top()
    shift_right()
    shift_top()
    reverse_right()
    reverse_top()
    reverse_right()
    reverse_top()
    reverse_right()
    shift_top()
    reverse_right()

def place_front_row_3() :
    shift_front()
    shift_front()
    shift_top()
    shift_front()
    shift_top()
    reverse_front()
    reverse_top()
    reverse_front()
    reverse_top()#
    reverse_front()
    shift_top()
    reverse_front()

def place_right_row_3() :
    reverse_back()
    reverse_back()
    shift_top()
    reverse_back()
    shift_top()
    shift_back()
    reverse_top()
    shift_back()
    reverse_top()
    shift_back()
    shift_top()
    shift_back()

def place_back_row_3() :
    reverse_left()
    reverse_left()
    shift_top()
    reverse_left()
    shift_top()
    shift_left()
    reverse_top()
    shift_left()
    reverse_top()
    shift_left()
    shift_top()
    shift_left()

########################
#########################
def has_edges(rows) :
    if rows["row1"][1].find("2") != -1 :
        return 1
    elif rows["row2"][0].find("2") != -1 :
        return 1
    elif rows["row2"][2].find("2") != -1 :
        return 1
    elif rows["row3"][1].find("2") != -1 :
        return 1
    return -1

def front_edges() :
    while True :
        if  has_edges(front_rows) == -1:
            break
        if front_rows["row1"][1].find("2") != -1 :
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
            shift_front()
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
            shift_right()
        
        if front_rows["row3"][1].find("2") != -1 :
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
            shift_front()
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
            shift_left()
        
        if front_rows["row2"][2].find("2") != -1 :
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
            shift_right()

        if front_rows["row2"][0].find("2") != -1 :
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
            shift_left()
        

def right_edges() :
    while  True :
        if has_edges(right_rows) == -1:
            break
        if right_rows["row1"][1].find("2") != -1 :
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
            reverse_right()
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
            reverse_front()

        if right_rows["row3"][1].find("2") != -1 :
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
            shift_right()
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
            shift_back()
        
        if right_rows["row2"][2].find("2") != -1 :
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
            shift_back()

        if right_rows["row2"][0].find("2") != -1 :
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
            reverse_front()
        

def left_edges() :
    while  True:
        if has_edges(left_rows) == -1:
            break
        if left_rows["row1"][1].find("2") != -1 :
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
            reverse_left()
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
            shift_front()
            
        
        if left_rows["row3"][1].find("2") != -1 :
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
            shift_left()
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
            reverse_back()
            
        
        if left_rows["row2"][2].find("2") != -1 :
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
            shift_front()
            

        if left_rows["row2"][0].find("2") != -1 :
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
            reverse_back()


def back_edges() :
  
    while  True :
        
        if  has_edges(back_rows) == -1:
            break
        if back_rows["row1"][1].find("2") != -1 :
            print("aaaaaa3") 
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
            shift_back()
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
            reverse_left()
        
        if back_rows["row3"][1].find("2") != -1 :
            print("aaaaaa1")
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
            shift_back()
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
            reverse_right()
            print("aaaaaa1")
        
        if back_rows["row2"][0].find("2") != -1 :
            print("aaaaaa2") 
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
            reverse_left()

        if back_rows["row2"][2].find("2") != -1 :
            print("aaaaaa4") 
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
            reverse_right()
            
def bottom_edges() :
    while   True:
        if has_edges(bottom_rows)  == -1:
            break
        if bottom_rows["row1"][1].find("2") != -1 :
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
            reverse_back()
            reverse_back()
        
        if bottom_rows["row3"][1].find("2") != -1 :
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
            shift_front()
            shift_front()

        if bottom_rows["row2"][0].find("2") != -1 :
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
            shift_left()
            shift_left()

        if bottom_rows["row2"][2].find("2") != -1 :
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
            shift_right()
            shift_right()


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

def top_edges() : 
    i = 0
    while top_edges_in_place(top_rows)  != 1 :
        front_edges()
        back_edges()
        left_edges()
        right_edges()
        bottom_edges()
        if top_edges_in_place(top_rows)  == 1 :
            break
        i += 1

def bottom_crose() :
    while True :
        if front_rows["row1"][1].find("3") != -1 and top_rows["row3"][1].find("2") != -1:
            shift_front()
            shift_front()

        if right_rows["row1"][1].find("6") != -1 and top_rows["row2"][2].find("2") != -1 :
            shift_right()
            shift_right()

        if back_rows["row1"][1].find("4") != -1 and top_rows["row1"][1].find("2") != -1:
            shift_back()
            shift_back()

        if left_rows["row1"][1].find("5") != -1 and top_rows["row2"][0].find("2") != -1:
            shift_left()
            shift_left()

        if top_edges_in_place(bottom_rows)  == 1 :
            break
        shift_top()


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

########################
def lay_3() :# has_lower_conners() == 1
    i = 0 
    while has_lower_conners() == 1:
        t  = 0
        while has_conner() != -1 :

            if left_rows["row1"][2].find("5") != -1  and front_rows["row1"][0].find("2") != -1:
                    # place_left_row_1_right()
                shift_front()
                shift_top()
                reverse_front()
                print("#1")

            if left_rows["row1"][0].find("5") != -1  and back_rows["row1"][0].find("2") != -1:
                # place_left_row_1_left()
                reverse_back()
                reverse_top()
                shift_back()
                print("#2")
                
            if right_rows["row1"][0].find("6") != -1  and front_rows["row1"][2].find("2") != -1:
                # place_right_row_1_left()
                reverse_front()
                reverse_top()
                shift_front()
                print("#3")

            if right_rows["row1"][2].find("6") != -1  and back_rows["row1"][2].find("2") != -1:
                # place_right_row_1_right()
                shift_back()
                shift_top()
                reverse_back()
                print("#4")
            
            if front_rows["row1"][2].find("3") != -1  and right_rows["row1"][0].find("2") != -1:
                # place_front_row_1_right()
                shift_right()
                shift_top()
                reverse_right()
                print("#5")

            if front_rows["row1"][0].find("3") != -1  and left_rows["row1"][2].find("2") != -1:
                # place_front_row_1_left()
                shift_left()
                reverse_top()
                reverse_left()
                print("#6")
            
            if back_rows["row1"][2].find("4") != -1  and right_rows["row1"][2].find("2") != -1:
                # place_back_row_1_right()
                reverse_right()
                shift_top()
                shift_right()
                print("#7")

            if back_rows["row1"][0].find("4") != -1  and left_rows["row1"][0].find("2") != -1:
                # place_back_row_1_left()
                reverse_left()
                shift_top()
                shift_left()
                print("#8")
            print("--------")
            shift_top()
            print("--------")
            t += 1

        if top_rows["row3"][0].find("2") != -1:
            shift_front()
            shift_top()
            shift_top()
            reverse_front()
            print("*1")
        elif top_rows["row3"][2].find("2") != -1:
            reverse_front()
            shift_top()
            shift_top()
            shift_front()
            print("*2")
        elif top_rows["row1"][0].find("2") != -1:
            reverse_back()
            shift_top()
            shift_top()
            shift_back()
            print("*3")
        elif top_rows["row1"][2].find("2") != -1:
            shift_back()
            shift_top()
            shift_top()
            reverse_back()
            print("*4")
        elif right_rows["row3"][2].find("2") != -1:
            reverse_right()
            shift_top()
            shift_top()
            shift_right()
            print("*5")
        elif right_rows["row3"][0].find("2") != -1:
            shift_right()
            shift_top()
            shift_top()
            reverse_right()
            print("*6")
        elif left_rows["row3"][2].find("2") != -1:
            shift_left()
            shift_top()
            shift_top()
            reverse_left()
            print("*7")
        elif left_rows["row3"][0].find("2") != -1:
            reverse_left()
            shift_top()
            shift_top()
            shift_left()
            print("*8")
        elif front_rows["row3"][0].find("2") != -1:
            shift_front()
            shift_top()
            shift_top()
            reverse_front()
            print("*9")
        elif front_rows["row3"][2].find("2") != -1:
            reverse_front()
            shift_top()
            shift_top()
            shift_front()
            print("*10")
        elif back_rows["row3"][2].find("2") != -1:
            shift_back()
            shift_top()
            shift_top()
            reverse_back()
            print("*11")
        elif back_rows["row3"][0].find("2") != -1:
            reverse_back()
            shift_top()
            shift_top()
            shift_back()
            print("*12")
        
        i += 1

##########################

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
    while c < 100 :
        d = 0
        while  has_midlle_center_edges()  == 1:
           
            if front_rows["row1"][1].find("3") != -1 and top_rows["row3"][1].find("6") != -1 :
                shift_top()
                shift_right()
                shift_top()
                reverse_right()
                reverse_top()
                reverse_front()
                reverse_top()
                shift_front()
                print("shift_top - front")
            
            elif back_rows["row1"][1].find("4") != -1 and top_rows["row1"][1].find("5") != -1 :
                shift_top()
                reverse_left()
                shift_top()
                shift_left()
                reverse_top()
                reverse_back()
                reverse_top()
                shift_back()
                print("shift_top - back")

            elif back_rows["row1"][1].find("4") != -1 and top_rows["row1"][1].find("6") != -1 :
                reverse_top()
                reverse_right()
                reverse_top()
                shift_right()
                shift_top()
                shift_back()
                shift_top()
                reverse_back()
                print("reverse_top - back")
            
            elif right_rows["row1"][1].find("6") != -1 and top_rows["row2"][2].find("3") != -1 :
                reverse_top()
                reverse_front()
                reverse_top()
                shift_front()
                shift_top()
                shift_right()
                shift_top()
                reverse_right()
                print("reverse_top - right")

            elif right_rows["row1"][1].find("6") != -1 and top_rows["row2"][2].find("4") != -1 :
                shift_top()
                shift_back()
                shift_top()
                reverse_back()
                reverse_top()
                reverse_right()
                reverse_top()
                shift_right()
                print("shift_top - right")
            
            elif left_rows["row1"][1].find("5") != -1 and top_rows["row2"][0].find("3") != -1 :
                shift_top()
                shift_front()
                shift_top()
                reverse_front()
                reverse_top()
                shift_left()
                reverse_top()
                reverse_left()
                print("reverse_top - left")

            elif left_rows["row1"][1].find("5") != -1 and top_rows["row2"][0].find("4") != -1 :
                reverse_top()
                reverse_back()
                reverse_top()
                shift_back()
                shift_top()
                reverse_left()
                shift_top()
                shift_left()
                print("shift_top - left")
            
            elif front_rows["row1"][1].find("3") != -1 and top_rows["row3"][1].find("5") != -1 :
                reverse_top()
                shift_left()
                reverse_top()
                reverse_left()
                shift_top()
                shift_front()
                shift_top()
                reverse_front()
        
            shift_top()
            d += 1

        if right_rows["row2"][0].find("6") == -1 :
            print("-1")
            reverse_front()
            reverse_top()
            shift_top()
            shift_front()
           
        elif right_rows["row2"][2].find("6") == -1 :
            print("-2")
            shift_back()
            shift_top()
            shift_top()
            reverse_back()
            
        elif back_rows["row2"][0].find("4") == -1 :
            print("-3")
            reverse_left()
            shift_top()
            shift_top()
            shift_left()
           
        elif back_rows["row2"][2].find("4") == -1 :
            print("-4")
            reverse_right()
            shift_top()
            shift_top()
            shift_right()
            
        elif front_rows["row2"][0].find("3") == -1 :
            print("-5")
            shift_left()
            shift_top()
            shift_top()
            reverse_left()
            
        elif front_rows["row2"][2].find("3") == -1 :
            print("-6") 
            shift_right()
            shift_top()
            shift_top()
            reverse_right()
           
        elif left_rows["row2"][0].find("5") == -1 :
            print("-7") 
            reverse_back()
            shift_top()
            shift_back()
            
        elif left_rows["row2"][2].find("5") == -1 :
            print("-1") 
            shift_front()
            shift_top()
            shift_top()
            reverse_front()
            
        lay_3()
        c +=1
##########################
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
    while has_top_x() != -1 :
        if top_who() == 1 :
            shift_front()
            shift_right()
            shift_top()
            reverse_right()
            reverse_top()
            reverse_front()
            print("x-1")
            if has_top_x() != -1 :
                shift_front()
                shift_right()
                shift_top()
                reverse_right()
                reverse_top()
                reverse_front()
                print("x-1.1")
        if top_who() == 2 :
            shift_top()
            shift_front()
            shift_right()
            shift_top()
            reverse_right()
            reverse_top()
            reverse_front()
            print("x-1")
            if has_top_x() != -1 :
                shift_front()
                shift_right()
                shift_top()
                reverse_right()
                reverse_top()
                reverse_front()
                print("x-1.1")

        elif top_who() == 3 :
            reverse_top()
            shift_front()
            shift_right()
            shift_top()
            reverse_right()
            reverse_top()
            reverse_front()
            print("x-1")
            if has_top_x() != -1 :
                shift_front()
                shift_right()
                shift_top()
                reverse_right()
                reverse_top()
                reverse_front()
                print("x-1.1")

        elif top_who() == 4 :
            reverse_top()
            reverse_top()
            shift_front()
            shift_right()
            shift_top()
            reverse_right()
            reverse_top()
            reverse_front()
            print("x-1")
            # if has_top_x() != -1 :
            #     shift_front()
            #     shift_right()
            #     shift_top()
            #     reverse_right()
            #     reverse_top()
            #     reverse_front()
            #     print("x-1.1")
        else :
            shift_top()
        i += 1

############################
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

def side_match() :
    i = 0
    p = 0
    while i < 5 :
        t =  has_little_fish()
        if t > p :
            p = t
        # print("///////////////////////// " + str(p))
        i += 1
        shift_top()
    print("///////////////////////// " + str(p))
    return p

def do_fish() :
    i = 0
    p = 0
    while i < 5 :
        t =  has_little_fish()
        if t > p :
            p = t
        # print("///////////////////////// " + str(p))
        i += 1
        shift_top()
    
    if p == 1 :
        shift_right()
        shift_top()
        reverse_right()
        shift_top()
        shift_right()
        shift_top()
        shift_top()
        reverse_right()
        print("$---1")
    elif p == 2 :

        print("$---2")

    elif i == 4 :
         print("$---4")

############################


# mix = "U D L R U D L E F2 L D' L L' R R'"
# pri   nt(mix)

shift_left()
# shift_top()
# shift_right()
shift_front()
shift_bottom()
# shift_back()
# reverse_left()
reverse_bottom()
# reverse_right()
# reverse_top()
# reverse_front()
# reverse_back()


print("*****11111111111***********************************")
top_edges()
print("****************22222222222************************")
bottom_crose()
 
lay_3()
print("****************333333333333333333333************************")
lay_2()
print("********************44444444444444444*****************")
top_x()
print("*********************555555555555************************")
do_fish()
# mix = mix.split(" ")

# for mv in mix :
#     print(mv)

root = Tk()
root.geometry("600x600")
m1 = side(top_rows,"top")
m2 = side(bottom_rows,"bottom")
m3 = side(back_rows,"back")
m4 = side(front_rows,"front")
m5 = side(left_rows,"left")
m6 = side(right_rows,"right")
mainloop()