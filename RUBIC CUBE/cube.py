
def shift_top() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = top["line1"]
    line2 = top["line2"]
    line3 = top["line3"]

    l1[0] = line3[0]
    l1[1] = line2[0]
    l1[2] = line1[0]

    l2[0] = line3[1]
    l2[1] = line2[1]
    l2[2] = line1[1]

    l3[0] = line3[2]
    l3[1] = line2[2]
    l3[2] = line1[2]

    top["line1"] = l1
    top["line2"] = l2
    top["line3"] = l3

    backl = [left["line3"][2],left["line2"][2], left["line1"][2]]
    leftl = front["line1"]
    frontl = [right["line3"][0],right["line2"][0], right["line1"][0]]
    rightl = back["line3"]

    front["line1"] = frontl
    back["line3"] = backl
    left["line3"][2] = leftl[0]
    left["line2"][2] = leftl[1]
    left["line1"][2] = leftl[2]
    right["line3"][0] = rightl[0]
    right["line2"][0] = rightl[1]
    right["line1"][0] = rightl[2]

def reverse_top() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = top["line1"]
    line2 = top["line2"]
    line3 = top["line3"]

    l1[0] = line1[2]
    l1[1] = line2[2]
    l1[2] = line3[2]

    l2[0] = line1[1]
    l2[1] = line2[1]
    l2[2] = line3[1]

    l3[0] = line3[0]
    l3[1] = line2[0]
    l3[2] = line1[0]

    top["line1"] = l1
    top["line2"] = l2
    top["line3"] = l3

    backl = [right["line3"][0],right["line2"][0], right["line1"][0]]
    leftl = back["line3"]
    frontl = [left["line3"][2],left["line2"][2], left["line1"][2]]
    rightl = front["line1"]

    front["line1"] = frontl
    back["line3"] = backl
    left["line3"][2] = leftl[0]
    left["line2"][2] = leftl[1]
    left["line1"][2] = leftl[2]
    right["line3"][0] = rightl[0]
    right["line2"][0] = rightl[1]
    right["line1"][0] = rightl[2]

##############  Bottom  #####################

def shift_bottom() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = bottom["line1"]
    line2 = bottom["line2"]
    line3 = bottom["line3"]

    l1[0] = line3[0]
    l1[1] = line2[0]
    l1[2] = line1[0]

    l2[0] = line3[1]
    l2[1] = line2[1]
    l2[2] = line1[1]

    l3[0] = line3[2]
    l3[1] = line2[2]
    l3[2] = line1[2]

    bottom["line1"] = l1
    bottom["line2"] = l2
    bottom["line3"] = l3

    backl = [right["line3"][2],right["line2"][2], right["line1"][2]]
    leftl = front["line3"]
    frontl = [left["line3"][0],left["line2"][0], left["line1"][0]]
    rightl = back["line1"]

    front["line3"] = backl 
    back["line1"] = frontl
    left["line3"][0] = leftl[0]
    left["line2"][0] = leftl[1]
    left["line1"][0] = leftl[2]
    right["line3"][2] = rightl[0]
    right["line2"][2] = rightl[1]
    right["line1"][2] = rightl[2]

def reverse_bottom() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = bottom["line1"]
    line2 = bottom["line2"]
    line3 = bottom["line3"]

    l1[0] = line3[0]
    l1[1] = line2[0]
    l1[2] = line1[0]

    l2[0] = line3[1]
    l2[1] = line2[1]
    l2[2] = line1[1]

    l3[0] = line3[2]
    l3[1] = line2[2]
    l3[2] = line1[2]

    bottom["line1"] = l1
    bottom["line2"] = l2
    bottom["line3"] = l3

    backl = [left["line3"][0],left["line2"][0], left["line1"][0]]
    leftl = back["line1"]
    frontl = [right["line3"][2],right["line2"][2], right["line1"][2]]
    rightl = front["line3"]

    front["line1"] = frontl
    back["line3"] = backl
    left["line3"][2] = leftl[0]
    left["line2"][2] = leftl[1]
    left["line1"][2] = leftl[2]
    right["line3"][0] = rightl[0]
    right["line2"][0] = rightl[1]
    right["line1"][0] = rightl[2]

########   front ########

def shift_front() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = front["line1"]
    line2 = front["line2"]
    line3 = front["line3"]

    l1[0] = line3[0]
    l1[1] = line2[0]
    l1[2] = line1[0]

    l2[0] = line3[1]
    l2[1] = line2[1]
    l2[2] = line1[1]

    l3[0] = line3[2]
    l3[1] = line2[2]
    l3[2] = line1[2]

    front["line1"] = l1
    front["line2"] = l2
    front["line3"] = l3

    leftl = left["line3"]
    topl = top["line3"]
    rightl = right["line3"]
    bottoml = bottom["line1"]

    top["line3"] =  leftl 
    bottom["line1"] = rightl 
    left["line3"] = bottoml
    right["line3"] = topl
    print("front")

def reverse_front() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = front["line1"]
    line2 = front["line2"]
    line3 = front["line3"]

    l1[0] = line1[2]
    l1[1] = line2[2]
    l1[2] = line3[2]

    l2[0] = line1[1]
    l2[1] = line2[1]
    l2[2] = line3[1]

    l3[0] = line1[0]
    l3[1] = line2[0]
    l3[2] = line3[0]

    front["line1"] = l1
    front["line2"] = l2
    front["line3"] = l3

    leftl = left["line3"]
    topl = top["line3"]
    rightl = right["line3"]
    bottoml = bottom["line1"]

    top["line3"] =   rightl 
    bottom["line1"] = leftl
    left["line3"] = topl
    right["line3"] = bottoml


###########  back  ################
def shift_back() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = back["line1"]
    line2 = back["line2"]
    line3 = back["line3"]

    l1[0] = line3[0]
    l1[1] = line2[0]
    l1[2] = line1[0]

    l2[0] = line3[1]
    l2[1] = line2[1]
    l2[2] = line1[1]

    l3[0] = line3[2]
    l3[1] = line2[2]
    l3[2] = line1[2]

    back["line1"] = l1
    back["line2"] = l2
    back["line3"] = l3

    leftl = left["line1"]
    topl = top["line1"]
    rightl = right["line1"]
    bottoml = bottom["line3"]

    top["line1"] = leftl
    bottom["line3"] = rightl
    left["line1"] =  bottoml
    right["line1"] = topl

def reverse_back() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = back["line1"]
    line2 = back["line2"]
    line3 = back["line3"]

    l1[0] = line1[0]
    l1[1] = line2[0]
    l1[2] = line3[0]

    l2[0] = line1[1]
    l2[1] = line2[1]
    l2[2] = line3[1]

    l3[0] = line1[2]
    l3[1] = line2[2]
    l3[2] = line3[2]

    back["line1"] = l1
    back["line2"] = l2
    back["line3"] = l3

    leftl = left["line1"]
    topl = top["line3"]
    rightl = right["line1"]
    bottoml = bottom["line1"]

    top["line3"] = rightl
    bottom["line1"] = leftl
    left["line1"] = topl
    right["line1"]=  bottoml

#########  left ##############
def shift_left() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = left["line1"]
    line2 = left["line2"]
    line3 = left["line3"]

    l1[0] = line3[2]
    l1[1] = line2[2]
    l1[2] = line1[2]

    l2[0] = line3[1]
    l2[1] = line2[1]
    l2[2] = line1[1]

    l3[0] = line3[0]
    l3[1] = line2[0]
    l3[2] = line1[0]

    left["line1"] = l1
    left["line2"] = l2
    left["line3"] = l3

    backl = [back["line3"][0],back["line2"][0], back["line1"][0]]
    topl = [top["line3"][0],top["line2"][0], top["line1"][0]]
    frontl = [front["line3"][0],front["line2"][0], front["line1"][0]]
    bottoml = [bottom["line3"][0],bottom["line2"][0], bottom["line1"][0]]

    front["line3"][0] = bottoml[0]
    front["line2"][0] = bottoml[1]
    front["line1"][0] = bottoml[2]
    back["line3"][0] = topl[0]
    back["line2"][0] = topl[1]
    back["line1"][0] = topl[2]
    top["line3"][0] = frontl[0]
    top["line2"][0] = frontl[1]
    top["line1"][0] = frontl[2]
    bottom["line3"][0] = backl[0]
    bottom["line2"][0] = backl[1]
    bottom["line1"][0] = backl[2]

def  reverse_left() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = left["line1"]
    line2 = left["line2"]
    line3 = left["line3"]

    l1[0] = line3[0]
    l1[1] = line2[0]
    l1[2] = line1[0]

    l2[0] = line3[1]
    l2[1] = line2[1]
    l2[2] = line1[1]

    l3[0] = line3[2]
    l3[1] = line2[2]
    l3[2] = line1[2]

    left["line1"] = l1
    left["line2"] = l2
    left["line3"] = l3

    backl = [back["line3"][0],back["line2"][0], back["line1"][0]]
    topl = [top["line3"][0],top["line2"][0], top["line1"][0]]
    frontl = [front["line3"][0],front["line2"][0], front["line1"][0]]
    bottoml = [bottom["line3"][0],bottom["line2"][0], bottom["line1"][0]]

    front["line3"][0] = topl[0]
    front["line2"][0] = topl[1]
    front["line1"][0] = topl[2]
    back["line3"][0] = bottoml[0]
    back["line2"][0] = bottoml[1]
    back["line1"][0] = bottoml[2]
    top["line3"][0] = backl[0]
    top["line2"][0] = backl[1]
    top["line1"][0] = backl[2]
    bottom["line3"][0] = frontl[0]
    bottom["line2"][0] = frontl[1]
    bottom["line1"][0] = frontl[2]


########## right ##########

def shift_right() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = right["line1"]
    line2 = right["line2"]
    line3 = right["line3"]

    l1[0] = line3[0]
    l1[1] = line2[0]
    l1[2] = line1[0]

    l2[0] = line3[1]
    l2[1] = line2[1]
    l2[2] = line1[1]

    l3[0] = line3[2]
    l3[1] = line2[2]
    l3[2] = line1[2]

    right["line1"] = l1
    right["line2"] = l2
    right["line3"] = l3

    backl = [back["line3"][2],back["line2"][2], back["line1"][2]]
    topl = [top["line3"][2],top["line2"][2], top["line1"][2]]
    frontl = [front["line3"][2],front["line2"][2], front["line1"][2]]
    bottoml = [bottom["line3"][2],bottom["line2"][2], bottom["line1"][2]]

    front["line3"][2] = bottoml[0]
    front["line2"][2] = bottoml[1]
    front["line1"][2] = bottoml[2]
    back["line3"][2] = topl[0]
    back["line2"][2] = topl[1]
    back["line1"][2] = topl[2]
    top["line3"][2] = frontl[0]
    top["line2"][2] = frontl[1]
    top["line1"][2] = frontl[2]
    bottom["line3"][2] = backl[0]
    bottom["line2"][2] = backl[1]
    bottom["line1"][2] = backl[2]

def reverse_right() :
    l1 = ["","",""]
    l2 = ["","",""]
    l3 = ["","",""]

    line1 = right["line1"]
    line2 = right["line2"]
    line3 = right["line3"]

    l1[0] = line1[2]
    l1[1] = line2[2]
    l1[2] = line3[2]

    l2[0] = line1[1]
    l2[1] = line2[1]
    l2[2] = line3[1]

    l3[0] = line1[0]
    l3[1] = line2[0]
    l3[2] = line3[0]

    right["line1"] = l1
    right["line2"] = l2
    right["line3"] = l3

    backl = [back["line3"][2],back["line2"][2], back["line1"][2]]
    topl = [top["line3"][2],top["line2"][2], top["line1"][2]]
    frontl = [front["line3"][2],front["line2"][2], front["line1"][2]]
    bottoml = [bottom["line3"][2],bottom["line2"][2], bottom["line1"][2]]

    front["line3"][2] = topl[0]
    front["line2"][2] = topl[1]
    front["line1"][2] = topl[2]
    back["line3"][2] = bottoml[0]
    back["line2"][2] = bottoml[1]
    back["line1"][2] = bottoml[2]
    top["line3"][2] = backl[0]
    top["line2"][2] = backl[1]
    top["line1"][2] = backl[2]
    bottom["line3"][2] = frontl[0]
    bottom["line2"][2] = frontl[1]
    bottom["line1"][2] = frontl[2]



top = {
    "line1" : ["Ybr1","Yb1","Ybo1"],
    "line2" : ["Yr1","Y1","Yo1"],
    "line3" : ["Yrg1","Yg1","Ygo1"]
}

bottom = {
    "line1" : ["Wrg2","Wg2","Wgo2"],
    "line2" : ["Wr2","W2","Wo2"],
    "line3" : ["Wbr2","Wb2","Wob2"],
}



front = {
    "line1" : ["Gyr3","Gy3","Gyo3"],
    "line2" : ["Gr3","G3","Go3"],
    "line3" : ["Grw3","Gw3","Gow3"],
}

back = {
    "line1" : ["Brw4","Bw4","Bwo4"],
    "line2" : ["Br4","B4","Bo4"],
    "line3" : ["Bry4","By4","Boy4"],
}

left = {
    "line1" : ["Rbw5","Rb5","Rby5"],
    "line2" : ["Rw5","R5","Ry5"],
    "line3" : ["Rwg5","Rg5","Rgy5"],
}

right = {
    "line1" : ["Oby6","Ob6","Obw6"],
    "line2" : ["Oy6","O6","Ow6"],
    "line3" : ["Ogy6","Og6","Ogw6"],
}

top_rows = {
    "row1" : [],
    "row2" :[],
    "row3" : []
}

bottom_rows = {
    "row1" : [],
    "row2" :[],
    "row3" : []
}

back_rows = {
    "row1" : [],
    "row2" :[],
    "row3" : [],
}

front_rows = {
    "row1" : [],
    "row2" :[],
    "row3" : [],
}

right_rows = {
    "row1" : [],
    "row2" :[],
    "row3" : [],
}

left_rows = {
    "row1" : [],
    "row2" :[],
    "row3": [],
}


def update_rows():
    top_rows["row1"] = top["line1"]
    top_rows["row2"] = top["line2"]
    top_rows["row3"] = top["line3"]
    bottom_rows["row1"] = bottom["line3"]
    bottom_rows["row2"] = bottom["line2"]
    bottom_rows["row3"] = bottom["line1"]
    front_rows["row1"] = front["line1"]
    front_rows["row2"] = front["line2"]
    front_rows["row3"] = front["line3"]
    back_rows["row1"] = back["line3"]
    back_rows["row2"] = back["line2"]
    back_rows["row3"] = back["line1"]
    right_rows["row1"] = [right["line3"][0],right["line2"][0],right["line1"][0]]
    right_rows["row2"] = [right["line3"][1],right["line2"][1],right["line1"][1]]
    right_rows["row3"] = [right["line3"][2],right["line2"][2],right["line1"][2]]
    left_rows["row1"] = [left["line1"][2],left["line2"][2],left["line3"][2]]
    left_rows["row2"] = [left["line1"][1],left["line2"][1],left["line3"][1]]
    left_rows["row3"] = [left["line1"][0],left["line2"][0],left["line3"][0]]


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
    l = Label(text=sdl[0])
    block1.add(l)
    line.add(block1)
    block2 = PanedWindow(line,bd =4, relief="raised", bg = col(sdl[1]), width="200", height = "20")
    l = Label(text=sdl[1])
    block2.add(l)
    line.add(block2)
    block3 = PanedWindow(line,bd =4, relief="raised", bg = col(sdl[2]), width="200", height = "20")
    l = Label(text=sdl[2])
    block3.add(l)
    line.add(block3)
    return line


def side(sd,bl):
    side = PanedWindow(bd =4, relief="raised" , orient=VERTICAL, width="200", height = "10")
    side.pack(fill=BOTH, expand=1)
    rightc = Label(text=bl)
    rightc.place(  anchor = 'ne')
    # side.add(rightc)
    line1 = PanedWindow(side,bd =4, orient=HORIZONTAL)
    line1 = side_line(line1,sd["row1"])
    side.add(line1)

    line2 = PanedWindow(side,bd =4, orient=HORIZONTAL)
    line2 = side_line(line2,sd["row2"])
    side.add(line2)

    line3 = PanedWindow(side,bd =4, orient=HORIZONTAL)
    line3 = side_line(line3,sd["row3"])
    side.add(line3)

    return side
####################

def place_front_row_1_right() : 
    shift_right()
    shift_top()
    reverse_right()
    reverse_top()

def place_front_row_1_left() : 
    shift_left()
    reverse_top()
    reverse_left()
    shift_top()

def place_back_row_1_left() : 
    shift_right()
    shift_top()
    reverse_right()
    reverse_top()

def place_back_row_1_right() : 
    shift_left()
    reverse_top()
    reverse_left()
    shift_top()

def place_right_row_1_right():
    shift_front()
    shift_top()
    reverse_front()
    reverse_top()

def place_right_row_1_left():
    shift_back()
    reverse_top()
    reverse_back()
    shift_top()

def place_left_row_1_right():
    shift_front()
    shift_top()
    reverse_front()
    reverse_top()

def place_left_row_1_left():
    shift_back()
    reverse_top()
    reverse_back()
    shift_top()

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
    reverse_top()#
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
    print("front")
    while True :
        if  has_edges(front_rows) == -1:
            break
        if front_rows["row1"][1].find("2") != -1 :
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
                update_rows()
            shift_front()
            update_rows()
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
                update_rows()
            shift_right()
            update_rows()
        
        if front_rows["row3"][1].find("2") != -1 :
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
                update_rows()
            shift_front()
            update_rows()
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
                update_rows()
            shift_left()
            update_rows()
        
        if front_rows["row2"][2].find("2") != -1 :
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
                update_rows()
            shift_right()
            update_rows()

        if front_rows["row2"][0].find("2") != -1 :
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
                update_rows()
            shift_left()
            update_rows()


def right_edges() :
    print("right")
    while  True :
        if has_edges(right_rows) == -1:
            break
        if right_rows["row1"][1].find("2") != -1 :
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_right()
            update_rows()
            while top_rows["row3"][2].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_front()
            update_rows()

        if right_rows["row3"][2].find("2") != -1 :
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
                update_rows()
            shift_right()
            update_rows()
            while top_rows["row1"][2].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_back()
            update_rows()
        
        if right_rows["row2"][2].find("2") != -1 :
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_back()
            update_rows()

        if right_rows["row2"][0].find("2") != -1 :
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_front()
            update_rows()


def left_edges() :
    print("left")
    while  True:
        if has_edges(left_rows) == -1:
            break
        if left_rows["row1"][2].find("2") != -1 :
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_left()
            update_rows()
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
                update_rows()
            shift_front()
            update_rows()
        
        if left_rows["row3"][2].find("2") != -1 :
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
                update_rows()
            shift_left()
            update_rows()
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
                update_rows()
            shift_back()
            update_rows()
        
        if left_rows["row2"][2].find("2") != -1 :
            while top_rows["row3"][2].find("2") != -1 :
                shift_top()
                update_rows()
            shift_front()
            update_rows()

        if left_rows["row2"][0].find("2") != -1 :
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
                update_rows()
            shift_back()
            update_rows()


def back_edges() :
  
    while  True :
        print("back")
        if  has_edges(back_rows) == -1:
            break
        if back_rows["row1"][1].find("2") != -1 :
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_back()
            update_rows()
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_right()
            update_rows()
            print(5)
        
        if back_rows["row3"][2].find("2") != -1 :
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_back()
            update_rows()
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_left()
            update_rows()
            print(6)
        
        if back_rows["row2"][2].find("2") != -1 :
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_right()
            update_rows()
            print(7)

        if back_rows["row2"][2].find("2") != -1 :
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
                update_rows()
            reverse_left()
            update_rows()
            print(8)


def bottom_edges() :
    while   True:
        if has_edges(bottom_rows)  == -1:
            break
        if bottom_rows["row1"][1].find("2") != -1 :
            while top_rows["row1"][1].find("2") != -1 :
                shift_top()
                update_rows()
            shift_back()
            update_rows()
            shift_back()
            update_rows()
            print("1")
        
        if bottom_rows["row3"][1].find("2") != -1 :
            while top_rows["row3"][1].find("2") != -1 :
                shift_top()
                update_rows()
            shift_front()
            update_rows()
            shift_front()
            update_rows()
            print("2")

        if bottom_rows["row2"][0].find("2") != -1 :
            while top_rows["row2"][0].find("2") != -1 :
                shift_top()
                update_rows()
            shift_left()
            update_rows()
            shift_left()
            update_rows()
            print("3")

        if bottom_rows["row2"][2].find("2") != -1 :
            while top_rows["row2"][2].find("2") != -1 :
                shift_top()
                update_rows()
            shift_right()
            update_rows()
            shift_right()
            update_rows()
            print("4")
        print("bottom")
        sleep(1)

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
    while True  :
        front_edges()
        back_edges()
        left_edges()
        right_edges()
        bottom_edges()
        if top_edges_in_place(top_rows)  == 1 :
            break
        print("top_edges")
        
def bottom_crose() :
    while True :
        if front_rows["row2"][2].find("2") != -1 :
            shift_front()
            shift_front()
            update_rows()

        if right_rows["row2"][2].find("2") != -1 :
            shift_right()
            shift_right()
            update_rows()

        if back_rows["row2"][2].find("2") != -1 :
            shift_back()
            shift_back()
            update_rows()

        if left_rows["row2"][2].find("2") != -1 :
            shift_left()
            shift_left()
            update_rows()

        if top_edges_in_place(bottom_rows)  == 1 :
            break
        shift_top()
        update_rows()
########################
shift_right()

shift_front()
shift_left()
shift_right()
shift_front()
shift_back()
shift_back()


shift_left()
update_rows()
top_edges()
bottom_crose()

update_rows()
root = Tk()
root.geometry("600x600")
m1 = side(top_rows,"top")
m2 = side(bottom_rows,"bottom")
m3 = side(back_rows,"back")
m4 = side(front_rows,"front")
m5 = side(left_rows,"left")
m6 = side(right_rows,"right")
mainloop()