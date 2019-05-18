import os
import datetime

def genTableTodo(filename, BOXlist):   
    tableTempS = r'''\begin{tabular}{|c|c||c|}
            Time &Planned &Completed\\
            \hline'''

    tableTempF = r'''\end{tabular}'''

    tablerows = " "

    for i in range(0, 24):
        print("Time " + str(i) + ":00" )
        datain = input("Enter Task at time:")
        tablerows = tablerows + str(i) + ":00 &" + datain + " &%INSERT%" + str(i) + " \\\\ \n"
        BOXlist[i] = datain

    tableTotal = tableTempS + "\n" + tablerows + tableTempF
    print(filename)
    print(tableTotal)

    s = open(filename).read()
    s = s.replace("%TABLE%", tableTotal)
    f = open(filename,"w+")
    f.write(s)
    f.close()
    return BOXlist

def updateTable(filename):
    s = open(filename).read()
    
    sltNr = input("What slot number do you want to replace?:")
    sltInfo = input("What do you want to replace it with?:")
    searchT = "%INSERT%" + str(sltNr)
    
    s = s.replace(searchT, str(sltInfo))
    f2 = open(filename,"w")
    f2.write(s)
    f2.close()

def printTable(filename):
    s = open(filename).read()
    print(s)


################################################

def genMorningR(filename):
    s = open(filename).read()
    search = "%MORNING%"
    update = r'''\subsubsection*{Morning Routine}
        \begin{center}
        \begin{tabular}{c|c|c}
        Task &Completed &Failed \\
        \hline      
        Meditate    & %MC%1  & %MF%1 \\
        Jellyman    & %MC%2  & %MF%2 \\
        Coffee      & %MC%3  & %MF%3 \\
        Wake Early  & %MC%4  & %MF%4 \\
        \hline
        \end{tabular}
        \end{center}
    '''
    s = s.replace(search, update)
    f = open(filename,"w")
    f.write(s)
    f.close()





def updateMorningR(MRMenu, MRAlt, MRloop):
    print("Meditate 1\nJellyman 2\nCoffee 3\nWake Early 4\n")
    
    sltNr = input("What Morning Routine task you like to update?:")
    sltCF = input("C or F?:")    

    while True:
        if str(sltCF) == (str("C") || str("c")):
            sltCF = str("C")
            alt = str("F")
            break
        elif str(sltCF) == (str("F") || str("f")):
            sltCF = str("F")
            alt = str("C")
            break
        else:
            print("Invalid character.")
            sltCF = input("C or F?:") 
            print(str(sltCF))

    MRMenu[sltNr] = sltCF
    MRAlt[sltNr] = alt
    
    # Remember to add "invalid key" later

    print("Would you like to continue updating?")
    key = input("Y/N")
    
    if str(key) == (str("Y") || (str("y")):
        MRloop = True
    elif str(key) == (str("F") || (str("F")):
        MRloop = False
    else:
        print("Invalid character, returning (FIX THIS LATER)")

    return MRMenu, MRloop





def finalMorningR(filename, MRMenu, MRAlt): 
    s = open(filename).read()
    f = open(filename,"w")

    for x, y in MRMenu.items():
         # print(x, y) 
        search = "%M" + str(y) + "%" + str(x)
        update = "X"
        s = s.replace(search, update)
        f.write(s)
    
    for x, y in MRAlt.items():
         # print(x, y) 
        search2 = "%M" + str(x) + "%" + str(y)
        update2 = " "
        s = s.replace(search2,update2)
        f.write(s)

    f.close()

    
################################################

def genGeneralTasks(filename):
    s = open(filename).read()
    search = "%GENTASK%"
    update = r'''\subsection*{General Tasks}
    \begin{center}
    \begin{tabular}{c|c|c}
        Tasks &Completed &Failed \\
        \hline
        %TASK%1     &%GC%1 &%GF%1 \\
        %TASK%2     &%GC%2 &%GF%2 \\
        %TASK%3     &%GC%3 &%GF%3 \\
        %TASK%4     &%GC%4 &%GF%4 \\
        %TASK%5     &%GC%5 &%GF%5 \\
        %TASK%6     &%GC%6 &%GF%6 \\
        %TASK%7     &%GC%7 &%GF%7 \\
        %TASK%8     &%GC%8 &%GF%8 \\
        %TASK%9     &%GC%9 &%GF%9 \\
        %TASK%10    &%GC%10 &%GF%10 \\
    \end{tabular}
    \end{center}
    '''
    s = s.replace(search, update)
    f = open(filename,"w")
    f.write(s)
    f.close()

def updateGeneralTasks(GENMenu, GENAlt, GENloop):
    sltNr = input("What General Task would you like to update?:")
    sltCF = input("C or F?:")
    
    while True:
        if str(sltCF) == (str("C") || str("c")):
            sltCF = str("C")
            alt = str("F")
            break
        elif str(sltCF) == (str("F") || str("f")):
            sltCF = str("F")
            alt = str("C")
            break
        else:
            print("Invalid character.")
            sltCF = input("C or F?:") 
            print(str(sltCF))

    GENMenu[sltNr] = sltCF
    GENAlt[sltNr] = alt

    print("Would you like to continue updating?")
    key = input("Y/N")
    
    if str(key) == (str("Y") || (str("y")):
        GENloop = True
    elif str(key) == (str("F") || (str("F")):
        GENloop = False
    else:
        print("Invalid character, returning (FIX THIS LATER)")

    return GENMenu, GENloop


def finalGeneralTasks(filename, GENMenu, GENAlt): 
    s = open(filename).read()
    f = open(filename,"w")

    for x, y in GENMenu.items():
         # print(x, y) 
        search = "%M" + str(y) + "%" + str(x)
        update = "X"
        s = s.replace(search, update)
        f.write(s)
    
    for x, y in GENAlt.items():
         # print(x, y) 
        search2 = "%M" + str(x) + "%" + str(y)
        update2 = " "
        s = s.replace(search2,update2)
        f.write(s)

    f.close()


def defineGeneralTasks(filename):
    s = open(filename).read()
    print(s)
    sltNr = input("What task would you like to define?:")
    sltInfo = input("Task description:")
    search = "%TASK%" + str(sltNr)
    update = sltInfo
    
    s = s.replace(search, update)
    f = open(filename,"w")
    f.write(s)
    f.close()


################################################


def genResp(filename):
    s = open(filename).read()
    search = "%RESPONS%"
    update = r'''\subsubsection*{Responsibilities}
    \begin{center}
        \begin{tabular}{c|c|c||c|c|c}
        Task &Completed &Failed &Task &Completed &Failed \\
        \hline      
        Kitchen     & %RC%1  & %RF%1 &Bullet        & %RC%6  & %RF%6  \\
        Table       & %RC%2  & %RF%2 &Trash         & %RC%7  & %RF%7  \\
        Sofa        & %RC%3  & %RF%3 &Bank Account  & %RC%8  & %RF%8  \\
        Floor       & %RC%4  & %RF%4 &Time-Box      & %RC%9  & %RF%9  \\
        Bedroom    & %RC%5  & %RF%5 &Data update   & %RC%10  & %RF%10 \\
        \hline
        \end{tabular}
    \end{center}
    '''
    s = s.replace(search, update)
    f = open(filename,"w")
    f.write(s)
    f.close()

def updateResp(RESPMenu, RESPAlt, RESPloop):
    print("Kitchen 1\n Table 2\n Sofa 3\n Floor 4\n Bedroom 5\n Bullet 6\n Trash 7\n Bank account 8\n Time-box 9\n Data update 10\n")

    sltNr = input("What would you like to update?:")
    sltCF = input("C or F?:") 

    while True:
        if str(sltCF) == (str("C") || str("c")):
            sltCF = str("C")
            alt = str("F")
            break
        elif str(sltCF) == (str("F") || str("f")):
            sltCF = str("F")
            alt = str("C")
            break
        else:
            print("Invalid character.")
            sltCF = input("C or F?:") 
            print(str(sltCF))
    
    RESPMenu[sltNR] = sltCF 
    RESPAlt[sltNR] = alt

    print("Would you like to continue updating?")
    key = input("Y/N")
    
    if str(key) == (str("Y") || (str("y")):
        GENloop = True
    elif str(key) == (str("F") || (str("F")):
        GENloop = False
    else:
        print("Invalid character, returning (FIX THIS LATER)")

    return RESPMenu, RESPloop



def finalResp(filename, RESPMenu, RESPAlt):
    s = open(filename).read()
    f = open(filename,"w")

    for x, y in RESPMenu.items():
         # print(x, y) 
        search = "%M" + str(y) + "%" + str(x)
        update = "X"
        s = s.replace(search, update)
        f.write(s)
    
    for x, y in RESPAlt.items():
         # print(x, y) 
        search2 = "%M" + str(x) + "%" + str(y)
        update2 = " "
        s = s.replace(search2,update2)
        f.write(s)

    f.close()




################################################


def genTemplate(filename):
    f = open(filename,"w+")
    stamp = datetime.datetime.now()
    templateStart = "\subsection{"+ stamp.strftime("%d. %A") + "}\n"
    template = r'''%MORNING%
    
    %GENTASK%
    
    %RESPONS%
    \subsubsection*{Time-Box}
    \begin{center}
    %TABLE%
    \end{center}
    \clearpage
    '''
    totalTemplate = templateStart + template
    f.write(totalTemplate)
    f.close()

def makeRead(filename):
    s = open(filename).read()
    update = " "
    updateF = "X (auto)"
    for i in range(25,-1,-1):
        searchMC = "%MC%"+(str(i))
        searchMF = "%MF%"+(str(i))
        print(searchMF)

        searchGC = "%GC%"+(str(i))
        searchGF = "%GF%"+(str(i))

        searchRC = "%RC%"+(str(i))
        searchRF = "%RF%"+(str(i))
        
        searchINSERT = "%INSERT%"+(str(i))
        searchTASK = "%TASK%"+(str(i))
                
        if searchMC in s:
            s = s.replace(searchMC,update)
        if searchMF in s:
            s = s.replace(searchMF,updateF)
        if searchGC in s:
            s = s.replace(searchGC,update)
        if searchGF in s:
            s = s.replace(searchGF,updateF)
        if searchRC in s:
            s = s.replace(searchRC,update)
        if searchRF in s:
            s = s.replace(searchRF,updateF)
        if searchINSERT in s:
            s = s.replace(searchINSERT,updateF)
        if searchTASK in s:
            s = s.replace(searchTASK,update)
        

    f = open(filename,"w")
    f.write(s)
    f.close()

#############################################################

# Todo list:

############################################################
# 1) Additional confirmation when generating the bullet.
# 2) More robust menu
#   a) when instructing with numbers
#   b) when instructing with strings
#
# 3) Additional flexibility for menu items in file, so that the file can be compiled without the need to finalize the document.
#
# 4) More editing friendly
# 5) Easier configuration and insertion of tasks.
# 6) Data graphs for monthly statistics.
# 7) Add "file already exists" in confirmation.
# 8) Find a way to keep tags within the tex file, without it disrupting everything else. Basically: Change the "%" tags.
# 9) Put functions in an external file.
# 10) Add submenues to minimize bad design.
# 11) Fix latex indentation.
# 12) Make monthly directories through python.



#############################################################

# Patch Notes:

############################################################
# Changes from saturday 06/04 - 2019
# 
# Decided to split the update functions into 2, one for updating the data (dictionaries) and one
# for finalizing the latex doc. I may change this later since you cannot close the program and
# restart it again, since the data you have saved temporary.
# Possible solution to this is to add a temporary txt/data file, to access for later usage, when
# closing and restarting the program.

# 1) Because of the above, I have created dictionaries for every program function, storing every
# action and alternative action (C/F).
# 
# 2) I have also made loops for every program function. The idea was to ensure that you stay
# within the submenu until you are finished updating.
#
# 3) I have tried adding a dictionary that stores the Timebox updates.
#
# 4) I have tried making the sub menu input more robust, taking upper/lower case letters into
# consideration. I have also added an invalid response, for when the input is wrong.
#
# Potential issues that may occur are:
#
# Issues with the menu.
# Issues with certain while loops
# Issues with printing the data.
#
# The code has not been tested yet.
#
# Plans for next programming session:
# 1) Test.
# 2) Add an edit function.
# 3) Add a txt/data file to store temporary data for later usage.
# 4) Test.



s = input("Enter bullet name:")
filename = s + ".tex"

MRloop = True
MRMenu = {}
MRAlt = {}

GENloop = True
GENMenu = {}
GENAlt = {}

RESPloop = True
RESPMenu = {}
RESPAlt = {}


BOXlist = {}


menu = {}
menu['1']="Generate Bullet" 
menu['2']="Update Morning Routine"
menu['3']="Update General Tasks"
menu['4']="Update Responsibilities"
menu['5']="Update Table"
menu['6']="Finalize"
menu['9']="Exit"
while True: 
    os.system('clear')
    options=menu.keys()
    for entry in sorted(options): 
        print(entry, menu[entry])
    selection=input("Please Select:") 
    if selection =='1': 
        os.system('clear')

        genTemplate(filename)
        genMorningR(filename)
        genGeneralTasks(filename)
        genResp(filename)
        BOXlist = genTableTodo(filename)

    elif selection == '2': 
        while MRloop == True:
    # Stay in this menu and strike out the already tapped options (Make it so that the data is overwritten every time)
        os.system('clear')
        MRmenu, MRloop = updateMorningR(MRmenu, MRloop)
        
    
    elif selection == '3': 
        os.system('clear')
        updateGeneralTasks(filename)
    
    elif selection == '4': 
        os.system('clear')
        updateResp(filename)
    
    elif selection == '5': 
        os.system('clear')
        updateTable(filename)
    
    elif selection == '6': 
        os.system('clear')
        finalMorningR(filename, MRmenu, MRAlt)
        makeRead(filename)    
        print("bling!")
    
    elif selection == '9':
        print("Exit") 
        break
    else: 
        os.system('clear')
        print("Unknown Option Selected!")
