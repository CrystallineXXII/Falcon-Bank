import pygame as pg

pg.init()

screen = pg.display.set_mode((500, 500),pg.RESIZABLE)
pg.display.set_caption("Falcon Bank")
pg.display.set_icon(pg.image.load("icon.png"))

#---#  Variables  #---#
clock = pg.time.Clock()
font = pg.font.Font("Menlo.ttf", 25)
sfont = pg.font.Font("Menlo.ttf", 15)

ACCOUNTS={1000:[1234,50000,"Steve"],2000:[5678,25000,"Lionel"],3000:[9090,30000,"Jonathan"]}

#----#  Classes  #----#
class Textbox:
    def __init__(self, x, y, width, height, textbox_list: list, text="", hidden=False):
        self.rect = pg.Rect(x, y, width, height)
        self.color  = "#dddddd"
        self.acolor = "#cccccc"
        self.tcolor = '#000000'
        self.text = text
        self.cursor = "_"
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.tapped = False
        self.hidden = hidden
        textbox_list.append(self)

    def draw(self, textbox_list: list):
        if pg.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pg.mouse.get_pos()):
                for i in textbox_list:
                    i.active = False
                self.active = True

        text = self.text if not self.hidden else "*" * len(self.text)
        text = (text + self.cursor) if self.active else text
        self.txt_surface = font.render(
            text, True, self.tcolor
        )
        pg.draw.rect(screen, self.acolor if self.active else self.color, self.rect)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        
class Text:
    def __init__(self, x, y, text, text_list: list,font = font,align = 'midright',color = 'black'):
        self.text = text
        self.x = x + 20
        self.y = y + 20
        self.txt_surface = font.render(text, True, color)
        if align == 'midright':
            self.rect = self.txt_surface.get_rect(midright=(self.x, self.y))
        elif align == 'midleft':
            self.rect = self.txt_surface.get_rect(midleft=(self.x, self.y))
        text_list.append(self)

    def draw(self):
        screen.blit(self.txt_surface, self.rect)

class Button:
    def __init__(self, x, y, width, height, text, color, acolor, action=None,font = font):
        self.rect = pg.Rect(x, y, width, height)
        self.rect.center = (x, y)
        self.color = color
        self.acolor = acolor
        self.text = text
        self.action = action
        self.tapped = False
        self.font = font

    def draw(self):
        pg.draw.rect(
            screen, self.acolor if self.tapped else self.color, self.rect, 0, 2
        )
        pg.draw.rect(
            screen, self.acolor if self.tapped else self.color, self.rect, 2, 2
        )

        if pg.mouse.get_pressed()[0] and not self.tapped:
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.tapped = True
                if self.action:
                    return self.action()
                else:
                    return self.tapped

        elif self.tapped and pg.mouse.get_pressed()[0] == 0:
            self.tapped = False


        text = self.font.render(self.text, True, "black")
        txtrect = text.get_rect(center=self.rect.center)
        screen.blit(text, txtrect)

#---#  Functions  #---#
def login(none = None):
    def challenge():
        

        if not (ACCNO.text.strip() == "" or PIN.text.strip() == ""):
            if int(ACCNO.text.strip()) in ACCOUNTS and (int(PIN.text.strip()) == ACCOUNTS[int(ACCNO.text.strip())][0]):

                return True

    textbox_list = []
    text_list = []
    doReturn = None
    ACCNO = Textbox(250, 300, 200, 40, textbox_list)
    PIN = Textbox(250, 350, 200, 40, textbox_list, hidden=True)
    Text(220, 300, "Account Number", text_list)
    Text(220, 350, "PIN", text_list)
    invalidate = False
    invalid_txt = Text(350, 390, "Invalid Account Number or PIN",[],font = sfont,color='red')
    ACCNO.draw(textbox_list)
    PIN.draw(textbox_list)

    logo = pg.image.load("logo.png").convert_alpha()
    logorect = logo.get_rect(center=(250, 150))

    button = Button(250, 450, 100, 40, "Login", "#dddddd", "#aaaaaa", challenge)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            for i in textbox_list.copy():
                if event.type == pg.KEYDOWN:
                    if i.active:
                        if event.key == pg.K_RETURN:
                            if i.text != "":
                                i.active = False
                                try:
                                    textbox_list[textbox_list.index(i) + 1].active = True
                                except IndexError as e:

                                    if challenge():
                                        doReturn = True
                                        break
                                    else:
                                        invalidate = True
                        elif event.key == pg.K_BACKSPACE:
                            i.text = i.text[:-1]
                        else:
                            if event.unicode.isdigit():
                                i.text += event.unicode

        screen.fill("white")
        screen.blit(logo, logorect)
        for i in text_list:
            i.draw()
        for i in textbox_list:
            i.draw(textbox_list)
        if doReturn == None:doReturn = button.draw()
        if invalidate:
            invalid_txt.draw()


        if doReturn:
            return menu, [ACCNO.text]
        
        pg.display.update()
        clock.tick(60)
def menu(accno):

    accno = int(accno[0])
    account = ACCOUNTS[accno]


    def home():
        text_list = []
        logo = pg.image.load("logo.png").convert_alpha()
        logo = pg.transform.rotozoom(logo,0,0.3)
        logorect = logo.get_rect(center=(60, 35))
        Text(450, 20, f"Welcome {account[2]} | {accno}", text_list,align='midright')

        home_button      =   Button(50, 100, 100, 20, "Home", "#dddddd", "#aaaaaa",font = sfont)
        withdraw_button  =   Button(50, 130, 100, 20, "Withdraw", "#dddddd", "#aaaaaa",font = sfont)
        transfer_button  =   Button(50, 160, 100, 20, "Transfer", "#dddddd", "#aaaaaa",font = sfont)
        loan_button      =   Button(50, 190, 100, 20, "Loan", "#dddddd", "#aaaaaa",font = sfont)
        invest_button    =   Button(50, 220, 100, 20, "Invest", "#dddddd", "#aaaaaa",font = sfont)
        logout_button    =   Button(50, 250, 100, 20, "Logout", "#dddddd", "#aaaaaa",font = sfont)


        Text(100, 70, "Home", text_list,align='midleft')

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            screen.fill("white")
            pg.draw.line(screen, "black", (100, 70), (100, 500), 2)
            pg.draw.line(screen, "black", (0,70), (500, 70), 2)

            for i in text_list:
                i.draw()


            #-# Drawing Buttons #-#
            if home_button.draw(): return home
            if withdraw_button.draw(): return withdraw
            if transfer_button.draw(): return transfer
            if loan_button.draw(): return loan
            if invest_button.draw(): return invest
            if logout_button.draw(): return login

            


            screen.blit(logo, logorect)

            pg.display.update()
            clock.tick(60)
    def withdraw():
        text_list = []
        logo = pg.image.load("logo.png").convert_alpha()
        logo = pg.transform.rotozoom(logo,0,0.3)
        logorect = logo.get_rect(center=(60, 35))
        Text(450, 20, f"Welcome {account[2]} | {accno}", text_list,align='midright')

        home_button      =   Button(50, 100, 100, 20, "Home", "#dddddd", "#aaaaaa",font = sfont)
        withdraw_button  =   Button(50, 130, 100, 20, "Withdraw", "#dddddd", "#aaaaaa",font = sfont)
        transfer_button  =   Button(50, 160, 100, 20, "Transfer", "#dddddd", "#aaaaaa",font = sfont)
        loan_button      =   Button(50, 190, 100, 20, "Loan", "#dddddd", "#aaaaaa",font = sfont)
        invest_button    =   Button(50, 220, 100, 20, "Invest", "#dddddd", "#aaaaaa",font = sfont)
        logout_button    =   Button(50, 250, 100, 20, "Logout", "#dddddd", "#aaaaaa",font = sfont)


        Text(100, 70, "Withdraw", text_list,align='midleft')

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            screen.fill("white")
            pg.draw.line(screen, "black", (100, 70), (100, 500), 2)
            pg.draw.line(screen, "black", (0,70), (500, 70), 2)

            for i in text_list:
                i.draw()


            #-# Drawing Buttons #-#
            if home_button.draw(): return home
            if withdraw_button.draw(): return withdraw
            if transfer_button.draw(): return transfer
            if loan_button.draw(): return loan
            if invest_button.draw(): return invest
            if logout_button.draw(): return login

            


            screen.blit(logo, logorect)

            pg.display.update()
            clock.tick(60)

    def transfer():
        text_list = []
        logo = pg.image.load("logo.png").convert_alpha()
        logo = pg.transform.rotozoom(logo,0,0.3)
        logorect = logo.get_rect(center=(60, 35))
        Text(450, 20, f"Welcome {account[2]} | {accno}", text_list,align='midright')

        home_button      =   Button(50, 100, 100, 20, "Home", "#dddddd", "#aaaaaa",font = sfont)
        withdraw_button  =   Button(50, 130, 100, 20, "Withdraw", "#dddddd", "#aaaaaa",font = sfont)
        transfer_button  =   Button(50, 160, 100, 20, "Transfer", "#dddddd", "#aaaaaa",font = sfont)
        loan_button      =   Button(50, 190, 100, 20, "Loan", "#dddddd", "#aaaaaa",font = sfont)
        invest_button    =   Button(50, 220, 100, 20, "Invest", "#dddddd", "#aaaaaa",font = sfont)
        logout_button    =   Button(50, 250, 100, 20, "Logout", "#dddddd", "#aaaaaa",font = sfont)


        Text(100, 70, "Transfer", text_list,align='midleft')

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            screen.fill("white")
            pg.draw.line(screen, "black", (100, 70), (100, 500), 2)
            pg.draw.line(screen, "black", (0,70), (500, 70), 2)

            for i in text_list:
                i.draw()


            #-# Drawing Buttons #-#
            if home_button.draw(): return home
            if withdraw_button.draw(): return withdraw
            if transfer_button.draw(): return transfer
            if loan_button.draw(): return loan
            if invest_button.draw(): return invest
            if logout_button.draw(): return login

            


            screen.blit(logo, logorect)

            pg.display.update()
            clock.tick(60)

    def loan():
        text_list = []
        logo = pg.image.load("logo.png").convert_alpha()
        logo = pg.transform.rotozoom(logo,0,0.3)
        logorect = logo.get_rect(center=(60, 35))
        Text(450, 20, f"Welcome {account[2]} | {accno}", text_list,align='midright')

        home_button      =   Button(50, 100, 100, 20, "Home", "#dddddd", "#aaaaaa",font = sfont)
        withdraw_button  =   Button(50, 130, 100, 20, "Withdraw", "#dddddd", "#aaaaaa",font = sfont)
        transfer_button  =   Button(50, 160, 100, 20, "Transfer", "#dddddd", "#aaaaaa",font = sfont)
        loan_button      =   Button(50, 190, 100, 20, "Loan", "#dddddd", "#aaaaaa",font = sfont)
        invest_button    =   Button(50, 220, 100, 20, "Invest", "#dddddd", "#aaaaaa",font = sfont)
        logout_button    =   Button(50, 250, 100, 20, "Logout", "#dddddd", "#aaaaaa",font = sfont)


        Text(100, 70, "Loan", text_list,align='midleft')

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            screen.fill("white")
            pg.draw.line(screen, "black", (100, 70), (100, 500), 2)
            pg.draw.line(screen, "black", (0,70), (500, 70), 2)

            for i in text_list:
                i.draw()


            #-# Drawing Buttons #-#
            if home_button.draw(): return home
            if withdraw_button.draw(): return withdraw
            if transfer_button.draw(): return transfer
            if loan_button.draw(): return loan
            if invest_button.draw(): return invest
            if logout_button.draw(): return login

            


            screen.blit(logo, logorect)

            pg.display.update()
            clock.tick(60)

    def invest():
        text_list = []
        logo = pg.image.load("logo.png").convert_alpha()
        logo = pg.transform.rotozoom(logo,0,0.3)
        logorect = logo.get_rect(center=(60, 35))
        Text(450, 20, f"Welcome {account[2]} | {accno}", text_list,align='midright')

        home_button      =   Button(50, 100, 100, 20, "Home", "#dddddd", "#aaaaaa",font = sfont)
        withdraw_button  =   Button(50, 130, 100, 20, "Withdraw", "#dddddd", "#aaaaaa",font = sfont)
        transfer_button  =   Button(50, 160, 100, 20, "Transfer", "#dddddd", "#aaaaaa",font = sfont)
        loan_button      =   Button(50, 190, 100, 20, "Loan", "#dddddd", "#aaaaaa",font = sfont)
        invest_button    =   Button(50, 220, 100, 20, "Invest", "#dddddd", "#aaaaaa",font = sfont)
        logout_button    =   Button(50, 250, 100, 20, "Logout", "#dddddd", "#aaaaaa",font = sfont)


        Text(100, 70, "Invest", text_list,align='midleft')

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            screen.fill("white")
            pg.draw.line(screen, "black", (100, 70), (100, 500), 2)
            pg.draw.line(screen, "black", (0,70), (500, 70), 2)

            for i in text_list:
                i.draw()


            #-# Drawing Buttons #-#
            if home_button.draw(): return home
            if withdraw_button.draw(): return withdraw
            if transfer_button.draw(): return transfer
            if loan_button.draw(): return loan
            if invest_button.draw(): return invest
            if logout_button.draw(): return login

            


            screen.blit(logo, logorect)

            pg.display.update()
            clock.tick(60)


    func = home
    while True:
        if func == login:
            return  login,None
        else:
            func = func()

#---#  Initalize  #---#
if __name__ == "__main__":
    func = login
    para = ('1000',)
    while True:
        func,para = func(para)
