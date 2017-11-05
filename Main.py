from Functions import *
from pygame import *
'''You just got to init! get it? well a mandatory to initialize pygame to make game works'''
pygame.init()

def mainmenuscreen():
    '''to create atmosphere one must use music'''
    bgm("music\\opening.mp3")

    while True:
        '''a format which I will always use for this game, which is using the function in Functions.py. Mainscreen basically init the screen
        like the width etc and most importantly screen background'''
        mainscreen =MainScreen("graphics\\menu\\bgmenu.png")
        logo = imagesprite("graphics\\menu\\bgtitle.png",10,20)
        ngame = imagesprite("graphics\\menu\\ngame.png", 70, 150)
        lgame = imagesprite("graphics\\menu\\lgame.png", 70, 200)
        qgame = imagesprite("graphics\\menu\\qgame.png", 70, 250)
        ''' the call function is a function in which used to basically blit inside the screen '''
        call_sprite(logo, "Image", mainscreen)
        call_sprite(ngame, "Image", mainscreen)
        call_sprite(lgame, "Image", mainscreen)
        call_sprite(qgame, "Image", mainscreen)
        display.update()

        '''don't ask me why but youtube taught me to use event.wait which is why I always use it'''
        e = event.wait()
        '''this code is to make that each time i click (because i use MOUSEBUTTONDOWN) will trigger action like if I click the newgame
        I would go into the scene while such as load and quit will quit because load game is just a dummy'''
        if ngame.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                trainscene1()
        if lgame.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                pygame.quit()
                break
        if qgame.rect.collidepoint(mouse.get_pos()):
            if e.type == MOUSEBUTTONDOWN:
                pygame.quit()
                break
        if e.type == QUIT:
                pygame.quit()
                break

def trainscene1():
    '''same as other file, at the beginning scene I would set the bgm and background screen using functions that I've made in Functions.py file'''
    bgm("sfx\\subwaytrain.mp3")
    mainscreen = MainScreen('graphics\\background\\trainstation.png')
    textbox = imagesprite("gui\\textbox.png",0,0)

    """Sprite template placement"""
    blanksprite = imagesprite("graphics\\character\\blanktemplate.png",-150,0)
    blanksprite2 = imagesprite("graphics\\character\\blanktemplate.png",350,0)

    """Dialogue template placement"""
    dialogueblank=  textsprite("gamefont\\ITCBLKAD.TTF"," ", 35, 20, 480, 255, 255, 255)
    dialogueblank2=  textsprite("gamefont\\ITCBLKAD.TTF"," ", 35, 20, 510, 255, 255, 255)

    '''Nametag template and character names'''
    unknownname = textsprite("gamefont\\ITCBLKAD.TTF","???", 35, 20, 400, 255, 255, 255)
    judemartinez = textsprite("gamefont\\ITCBLKAD.TTF","Jude Martinez", 35, 20, 400, 255, 255, 255)

    """character dialogue, put in manually just so coz I can't find a better and simpler way"""
    dialogue1= textsprite("gamefont\\ITCBLKAD.TTF","Ugh...", 35, 20, 450, 255, 255, 255)
    dialogue2= textsprite("gamefont\\ITCBLKAD.TTF","What could possibly go much worse than this?", 35, 20, 450, 255, 255, 255)
    dialogue3= textsprite("gamefont\\ITCBLKAD.TTF","I was living the barbie life of the grand lavish city of Tokyo.", 35, 20, 450, 255, 255, 255)
    dialogue3a= textsprite("gamefont\\ITCBLKAD.TTF","but it has come to this? this rural stinky area? how did grandpa",35, 20, 480, 255, 255, 255)
    dialogue3b= textsprite("gamefont\\ITCBLKAD.TTF","live this place anyway?",35, 20, 510, 255, 255, 255)
    dialogue4= textsprite("gamefont\\ITCBLKAD.TTF","Oh my by the way, my name is Jude Martinez, everyone calls", 35, 20, 450, 255, 255, 255)
    dialogue4a= textsprite("gamefont\\ITCBLKAD.TTF","me Jude. I was living in Tokyo but then stuffs happened and", 35, 20, 480, 255, 255, 255)
    dialogue4b=  textsprite("gamefont\\ITCBLKAD.TTF","here I am, in Fukuoka's countryside", 35, 20, 510, 255, 255, 255)
    dialogue5=  textsprite("gamefont\\ITCBLKAD.TTF","where my grandparent used to reside and my parent's hometown", 35, 20, 450, 255, 255, 255)
    dialogue6=  textsprite("gamefont\\ITCBLKAD.TTF","I'll be living here for the next 7 days for summer break", 35, 20, 450, 255, 255, 255)
    dialogue7=  textsprite("gamefont\\ITCBLKAD.TTF","I already miss tokyo...", 35, 20, 450, 255, 255, 255)
    dialogue8=  textsprite("gamefont\\ITCBLKAD.TTF","Oh well it's too late, it's almost Fukuoka...", 35, 20, 450, 255, 255, 255)
    dialogue9=  textsprite("gamefont\\ITCBLKAD.TTF","I guess I'll enjoy my stay in here for the next 7 days.", 35, 20, 450, 255, 255, 255)
    counterdialogue = 0
    while True:

        '''to make everything a lot easier, I use variable so there's no need to blit all the time'''
        nametag = unknownname
        character1= blanksprite
        character2= blanksprite2
        dialogueline1 = dialogue1
        dialogueline2 = dialogueblank
        dialogueline3 = dialogueblank2
        e = event.wait()

        '''counter dialogue so every click will change the text image only'''

        if e.type == MOUSEBUTTONDOWN:
            counterdialogue += 1
        if counterdialogue == 1:
            dialogueline1 = dialogue2
        if counterdialogue == 2:
            dialogueline1 = dialogue3
            dialogueline2 = dialogue3a
            dialogueline3 = dialogue3b
        if counterdialogue ==3:
            nametag = judemartinez
            dialogueline1 = dialogue4
            dialogueline2 = dialogue4a
            dialogueline3 = dialogue4b
        if counterdialogue ==4:
            nametag = judemartinez
            dialogueline1 = dialogue5
        if counterdialogue ==5:
            nametag = judemartinez
            dialogueline1 = dialogue6
        if counterdialogue ==6:
            nametag = judemartinez
            dialogueline1 = dialogue7
        if counterdialogue ==7:
            nametag = judemartinez
            dialogueline1 = dialogue8
        if counterdialogue ==8:
            nametag = judemartinez
            dialogueline1 = dialogue9
        if counterdialogue ==9:
            trainscene2()

        '''call sprite is a basically function to show sprite such as blit but I found it easier'''

        call_sprite(character1, "Image", mainscreen)
        call_sprite(character2, "Image", mainscreen)
        call_sprite(textbox, "Image", mainscreen)
        call_sprite(dialogueline1, "Image", mainscreen)
        call_sprite(dialogueline2, "Image", mainscreen)
        call_sprite(dialogueline3, "Image", mainscreen)
        call_sprite(nametag, "Image", mainscreen)
        '''display update to update... yeah self explainatory, all I can say is without the update the screen won't show 
        any picture that have been blit/call'''

        display.update()
        if e.type == QUIT:
            pygame.quit()
            break

def trainscene2():
    '''
    COPYPASTING EVERYWHERE (not from outsources, just copy pasting everything i've type hahah!)
    '''
    bgm("music\\cheerfulbgm.mp3")
    mainscreen = MainScreen('graphics\\background\\trainstation.png')
    textbox = imagesprite("gui\\textbox.png",0,0)

    """Sprite template placement"""
    blanksprite = imagesprite("graphics\\character\\blanktemplate.png",-150,0)
    blanksprite2 = imagesprite("graphics\\character\\blanktemplate.png",350,0)


    """Dialogue template placement"""
    dialogueblank=  textsprite("gamefont\\ITCBLKAD.TTF"," ", 35, 20, 480, 255, 255, 255)
    dialogueblank2=  textsprite("gamefont\\ITCBLKAD.TTF"," ", 35, 20, 510, 255, 255, 255)


    """Character List and Images"""
    maya = imagesprite("graphics\\character\\Maya\\mayanormal.png",-150,0)
    mayahappy1 = imagesprite("graphics\\character\\Maya\\happy1.png",-150,0)
    mayahappy2 = imagesprite("graphics\\character\\Maya\\happy2.png",-150,0)

    '''Nametag template and character names'''
    unknownname = textsprite("gamefont\\ITCBLKAD.TTF","???", 35, 20, 400, 255, 255, 255)
    judemartinez = textsprite("gamefont\\ITCBLKAD.TTF","Jude Martinez", 35, 20, 400, 255, 255, 255)
    mayaname = textsprite("gamefont\\ITCBLKAD.TTF","Maya", 35, 20, 400, 255, 255, 255)

    """player's dialogue, put in manually just so because I can't find a better and simpler way"""
    dialogue1= textsprite("gamefont\\ITCBLKAD.TTF","HEY!!! IT'S THAT YOU JUDE??", 35, 20, 450, 255, 255, 255)
    dialogue2= textsprite("gamefont\\ITCBLKAD.TTF","A familiar voice rang through my ears", 35, 20, 450, 255, 255, 255)
    dialogue3= textsprite("gamefont\\ITCBLKAD.TTF","Wait... is that you Maya?", 35, 20, 450, 255, 255, 255)
    dialogue4= textsprite("gamefont\\ITCBLKAD.TTF","Yes! it sure is!", 35, 20, 450, 255, 255, 255)
    dialogue5=  textsprite("gamefont\\ITCBLKAD.TTF","That's Maya, my childhood friend, never thought that I", 35, 20, 450, 255, 255, 255)
    dialogue5a=  textsprite("gamefont\\ITCBLKAD.TTF","would see her again, well I was told by my mother", 35, 20, 480, 255, 255, 255)
    dialogue5b=  textsprite("gamefont\\ITCBLKAD.TTF","that she would be here", 35, 20, 510, 255, 255, 255)
    dialogue6=  textsprite("gamefont\\ITCBLKAD.TTF","So how's Mia?", 35, 20, 450, 255, 255, 255)
    dialogue7=  textsprite("gamefont\\ITCBLKAD.TTF","Shy as always but look at you! you're big now!", 35, 20, 450, 255, 255, 255)
    dialogue8=  textsprite("gamefont\\ITCBLKAD.TTF","Uhm... yes... of course, I've grown up..", 35, 20, 450, 255, 255, 255)
    dialogue9=  textsprite("gamefont\\ITCBLKAD.TTF","By the way, I should show you around since you've arrived aready!", 35, 20, 450, 255, 255, 255)
    dialogue10=  textsprite("gamefont\\ITCBLKAD.TTF","Wait but I just arrived here!at least let me rest for today!", 35, 20, 450, 255, 255, 255)
    counterdialogue = 0
    while True:
        nametag = unknownname
        character1= blanksprite
        character2= blanksprite2
        dialogueline1 = dialogue1
        dialogueline2 = dialogueblank
        dialogueline3 = dialogueblank2
        e = event.wait()
        if e.type == MOUSEBUTTONDOWN:
            counterdialogue += 1
        if counterdialogue == 1:
            nametag = judemartinez
            dialogueline1 = dialogue2
        if counterdialogue == 2:
            nametag = judemartinez
            dialogueline1 = dialogue3
        if counterdialogue ==3:
            character1= mayahappy2
            nametag = mayaname
            dialogueline1 = dialogue4
        if counterdialogue ==4:
            nametag = judemartinez
            character1= maya
            dialogueline1 = dialogue5
            dialogueline2 = dialogue5a
            dialogueline3 = dialogue5b
        if counterdialogue ==5:
            nametag = judemartinez
            dialogueline1 = dialogue6
        if counterdialogue ==6:
            character1= mayahappy1
            nametag = mayaname
            dialogueline1 = dialogue7
        if counterdialogue ==7:
            nametag = judemartinez
            dialogueline1 = dialogue8
        if counterdialogue ==8:
            character1= mayahappy2
            nametag = mayaname
            dialogueline1 = dialogue9
        if counterdialogue ==9:
            nametag = judemartinez
            dialogueline1 = dialogue10

        call_sprite(character1, "Image", mainscreen)
        call_sprite(character2, "Image", mainscreen)
        call_sprite(textbox, "Image", mainscreen)
        call_sprite(dialogueline1, "Image", mainscreen)
        call_sprite(dialogueline2, "Image", mainscreen)
        call_sprite(dialogueline3, "Image", mainscreen)
        call_sprite(nametag, "Image", mainscreen)

        if counterdialogue ==10:
            simmenu()
        display.update()

        if e.type == QUIT:
            pygame.quit()
            break


def simmenu():
    bgm("music\\p4alone.mp3")
    '''number of days and relationship system are basically have the same logic as the text system'''
    mainscreen =MainScreen("graphics\\menu\\bgmenu.png")
    background =imagesprite("graphics\\button\\mainsim.png",0,0)
    numday = "Day 1"
    numday2 = "Day 2"
    numday3 = "Day 3"
    numday4 = "Day 4"
    numday5 = "Day 5"
    numday6 = "Day 6"
    numday7 = "Day 7"
    dayongame = numday
    trainbutton1= textsprite("gamefont\\ITCBLKAD.TTF","It's not time to leave yet", 35, 20, 450, 255, 255, 255)
    trainbutton2= textsprite("gamefont\\ITCBLKAD.TTF","Today is my last day, I should go to the train station", 35, 20, 450, 255, 255, 255)
    choosingaction= textsprite("gamefont\\ITCBLKAD.TTF","what should I do for today?", 35, 20, 450, 255, 255, 255)
    textbox = imagesprite("gui\\textbox.png",0,0)
    miarelationship = 0
    mayarelationship = 0
    day = 1
    while True:
        button1=imagesprite("graphics\\button\\buttontrainstation.png",450,50)
        button2=imagesprite("graphics\\button\\mayahouse.png",30,50)
        button3=imagesprite("graphics\\button\\crossroad.png",30,200)
        button4=imagesprite("graphics\\button\\bedroom.png",450,200)
        days=textsprite("gamefont\\ITCBLKAD.TTF",dayongame, 35, 350, 370, 255, 255, 255)
        strmayarelationship = "Maya relationship:"+ str(mayarelationship)
        strmiarelationship = "Mia relationship:"+ str(miarelationship)
        relationship1 = textsprite("gamefont\\ITCBLKAD.TTF",strmayarelationship, 35, 50, 0, 255, 255, 255)
        relationship2 = textsprite("gamefont\\ITCBLKAD.TTF",strmiarelationship, 35, 450, 0, 255, 255, 255)
        chooseaction=choosingaction
        e= event.wait()
        '''so if day before 7 == you still can do action coz at the end of the week you'll be going home'''
        if day<7:
            if button1.rect.collidepoint(mouse.get_pos()):
                if e.type == pygame.MOUSEBUTTONDOWN:
                    chooseaction = trainbutton1
            if button2.rect.collidepoint(mouse.get_pos()):
                if e.type == pygame.MOUSEBUTTONDOWN:
                    day += 1
                    mayarelationship += 20
            if button3.rect.collidepoint(mouse.get_pos()):
                if e.type == pygame.MOUSEBUTTONDOWN:
                    day += 1
                    miarelationship += 20
            if button4.rect.collidepoint(mouse.get_pos()):
                if e.type == pygame.MOUSEBUTTONDOWN:
                    day += 1
            if day == 2:
                dayongame = numday2
            if day == 3:
                dayongame = numday3
            if day == 4:
                dayongame = numday4
            if day == 5:
                dayongame = numday5
            if day == 6:
                dayongame = numday6
            if day == 7:
                dayongame = numday7
        if day == 7:
            chooseaction = trainbutton2
            if button1.rect.collidepoint(mouse.get_pos()):
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if mayarelationship >60:
                        mayaending()
                    elif miarelationship>60:
                        miaending()
                    elif mayarelationship == 60 and miarelationship == 60:
                        haremending()
                    else:
                        aloneending()
        call_sprite(background, "Image", mainscreen)
        call_sprite(button1, "Image", mainscreen)
        call_sprite(button2, "Image", mainscreen)
        call_sprite(button3, "Image", mainscreen)
        call_sprite(button4, "Image", mainscreen)
        call_sprite(textbox, "Image", mainscreen)
        call_sprite(chooseaction, "Image", mainscreen)
        call_sprite(relationship1, "Image", mainscreen)
        call_sprite(relationship2, "Image", mainscreen)
        call_sprite(days,"Image", mainscreen)
        display.update()

        if e.type == QUIT:
            pygame.quit()
            break

def mayaending():
    while True:
        mainscreen =MainScreen("graphics\\Ending\\maya.png")
        text= textsprite("gamefont\\ITCBLKAD.TTF","Maya's Ending", 70, 225, 270, 0, 0, 0)
        call_sprite(text, "Image", mainscreen)
        e= event.wait()
        if e.type == MOUSEBUTTONDOWN:
            mainmenuscreen()
        display.update()

        if e.type == QUIT:
            pygame.quit()
def miaending():
    while True:
        mainscreen =MainScreen("graphics\\Ending\\mia.png")
        text= textsprite("gamefont\\ITCBLKAD.TTF","Mia's Ending", 70, 225, 270, 255, 255, 255)
        call_sprite(text, "Image", mainscreen)
        e= event.wait()
        if e.type == MOUSEBUTTONDOWN:
            mainmenuscreen()
        display.update()

        if e.type == QUIT:
            pygame.quit()

def haremending():
    bgm("music\\kill.mp3")
    while True:
        mainscreen =MainScreen("graphics\\Ending\\harem.png")
        text= textsprite("gamefont\\ITCBLKAD.TTF","Harem Ending", 70, 225, 270, 255, 0, 0)
        call_sprite(text, "Image", mainscreen)
        e= event.wait()
        if e.type == MOUSEBUTTONDOWN:
            mainmenuscreen()
        display.update()

        if e.type == QUIT:
            pygame.quit()

def aloneending():
    bgm("music\\sadviolin.mp3")
    while True:
        mainscreen =MainScreen("graphics\\Ending\\alone.png")
        text= textsprite("gamefont\\ITCBLKAD.TTF","Forever Alone Ending", 70, 130, 250, 255, 255, 255)
        call_sprite(text, "Image", mainscreen)
        e= event.wait()
        if e.type == MOUSEBUTTONDOWN:
            mainmenuscreen()
        display.update()

        if e.type == QUIT:
            pygame.quit()

mainmenuscreen()
