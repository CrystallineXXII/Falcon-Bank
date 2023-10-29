import pygame as pg
import csv

pg.init()

screen = pg.display.set_mode((500, 500))
pg.display.set_caption("Falcon Bank")
pg.display.set_icon(pg.image.load("icon.png"))

# ---#  Variables  #---#
clock = pg.time.Clock()
font = pg.font.Font("Menlo.ttf", 25)
sfont = pg.font.Font("Menlo.ttf", 15)
bfont = pg.font.Font("Menlo.ttf", 35)

ACCOUNTS = {}
with open("accounts.csv") as f:
    for i in csv.reader(f):
        if i[0] == "AccNo":
            continue
        ACCOUNTS[int(i[0])] = [int(i[1]), int(i[2]), str(i[3])]


# ----#  Classes  #----#
class Textbox:
    def __init__(self, x, y, width, height, textbox_list: list, text="", hidden=False):
        self.rect = pg.Rect(x, y, width, height)
        self.color = "#dddddd"
        self.acolor = "#cccccc"
        self.tcolor = "#000000"
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
        self.txt_surface = font.render(text, True, self.tcolor)
        pg.draw.rect(screen, self.acolor if self.active else self.color, self.rect)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))


class Text:
    def __init__(
        self, x, y, text, text_list: list, font=font, align="midright", color="black"
    ):
        self.text = text
        self.x = x + 20
        self.y = y + 20
        self.txt_surface = font.render(text, True, color)
        if align == "midright":
            self.rect = self.txt_surface.get_rect(midright=(self.x, self.y))
        elif align == "midleft":
            self.rect = self.txt_surface.get_rect(midleft=(self.x, self.y))
        elif align == "center":
            self.rect = self.txt_surface.get_rect(center=(self.x, self.y))
        elif align == "d-center":
            self.rect = self.txt_surface.get_rect(center=(self.x + 50, self.y))
        text_list.append(self)

    def draw(self):
        screen.blit(self.txt_surface, self.rect)


class Button:
    def __init__(
        self, x, y, width, height, text, color, acolor, action=None, font=font
    ):
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


# ---#  Functions  #---#
def login(none=None):
    def challenge():
        if not (accno.text.strip() == "" or pin.text.strip() == ""):
            if int(accno.text.strip()) in ACCOUNTS and (
                int(pin.text.strip()) == ACCOUNTS[int(accno.text.strip())][0]
            ):
                return True

    textbox_list = []
    text_list = []
    doReturn = None
    accno = Textbox(270, 300, 200, 40, textbox_list)
    pin = Textbox(270, 350, 200, 40, textbox_list, hidden=True)
    Text(240, 300, "Account Number:", text_list)
    Text(240, 350, "PIN           :", text_list)
    invalidate = False
    invalid_txt = Text(
        250,
        390,
        "Invalid Account Number or pin",
        [],
        font=sfont,
        color="red",
        align="center",
    )
    accno.draw(textbox_list)
    pin.draw(textbox_list)

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
                                    textbox_list[
                                        textbox_list.index(i) + 1
                                    ].active = True
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
        if doReturn == None:
            doReturn = button.draw()
        if invalidate:
            invalid_txt.draw()

        if doReturn:
            return menu, [accno.text]

        pg.display.update()
        clock.tick(60)


def menu(accno):
    accno = int(accno[0])
    account = ACCOUNTS[accno]

    def home():
        text_list = []
        textbox_list = []
        logo = pg.image.load("logo.png").convert_alpha()
        big_logo = pg.transform.rotozoom(logo, 0, 1)
        logo = pg.transform.rotozoom(logo, 0, 0.3)
        logorect = logo.get_rect(center=(60, 35))

        Text(450, 20, f"Welcome {account[2]} | {accno}", text_list, align="midright")
        Text(
            280,
            400,
            f"Balance : {ACCOUNTS[accno][1]}",
            text_list,
            align="center",
            font=bfont,
        )

        home_button = Button(50, 100, 100, 20, "Home", "#dddddd", "#aaaaaa", font=sfont)
        withdraw_button = Button(
            50, 130, 100, 20, "Withdraw", "#dddddd", "#aaaaaa", font=sfont
        )
        transfer_button = Button(
            50, 160, 100, 20, "Transfer", "#dddddd", "#aaaaaa", font=sfont
        )
        loan_button = Button(50, 190, 100, 20, "Loan", "#dddddd", "#aaaaaa", font=sfont)

        logout_button = Button(
            50, 480, 100, 20, "Logout", "#dddddd", "#aaaaaa", font=sfont
        )

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            screen.fill("white")
            pg.draw.line(screen, "black", (100, 70), (100, 500), 2)
            pg.draw.line(screen, "black", (0, 70), (500, 70), 2)

            for i in text_list:
                i.draw()

            # -# Drawing Buttons #-#
            if home_button.draw():
                return home
            if withdraw_button.draw():
                return withdraw
            if transfer_button.draw():
                return transfer
            if loan_button.draw():
                return loan

            if logout_button.draw():
                return login

            screen.blit(logo, logorect)
            screen.blit(big_logo, big_logo.get_rect(center=(300, 250)))

            pg.display.update()
            clock.tick(60)

    def withdraw():
        def challenge():
            print(account)
            if int(pin.text) == account[0]:
                return True

        text_list = []
        textbox_list = []
        errors = []
        logo = pg.image.load("logo.png").convert_alpha()
        logo = pg.transform.rotozoom(logo, 0, 0.3)
        logorect = logo.get_rect(center=(60, 35))
        Text(450, 20, f"Welcome {account[2]} | {accno}", text_list, align="midright")
        doReturn = None
        success = False

        home_button = Button(50, 100, 100, 20, "Home", "#dddddd", "#aaaaaa", font=sfont)
        withdraw_button = Button(
            50, 130, 100, 20, "Withdraw", "#dddddd", "#aaaaaa", font=sfont
        )
        transfer_button = Button(
            50, 160, 100, 20, "Transfer", "#dddddd", "#aaaaaa", font=sfont
        )
        loan_button = Button(50, 190, 100, 20, "Loan", "#dddddd", "#aaaaaa", font=sfont)

        logout_button = Button(
            50, 480, 100, 20, "Logout", "#dddddd", "#aaaaaa", font=sfont
        )

        Text(230, 120, "Amount:", text_list, font=font)
        Text(230, 170, "PIN   :", text_list, font=font)
        Amount = Textbox(
            300,
            120,
            160,
            40,
            textbox_list,
        )
        pin = Textbox(300, 170, 160, 40, textbox_list, hidden=True)
        button = Button(
            300,
            370,
            160,
            40,
            "Confirm",
            "#dddddd",
            "#aaaaaa",
            font=font,
            action=challenge,
        )

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                for tb in textbox_list.copy():
                    if tb.active:
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_RETURN:
                                if tb.text != "":
                                    tb.active = False
                                    try:
                                        textbox_list[
                                            textbox_list.index(tb) + 1
                                        ].active = True
                                    except IndexError as e:
                                        print(e)
                                        if challenge():
                                            print("Valid")
                                            doReturn = True
                                            break
                                        else:
                                            invalidate = True
                            elif event.key == pg.K_BACKSPACE:
                                tb.text = tb.text[:-1]
                            else:
                                if event.unicode.isdigit():
                                    tb.text += event.unicode

            screen.fill("white")
            pg.draw.line(screen, "black", (100, 70), (100, 500), 2)
            pg.draw.line(screen, "black", (0, 70), (500, 70), 2)

            for i in text_list:
                i.draw()
            for i in textbox_list:
                i.draw(textbox_list)
            for i in errors:
                i.draw()
            # -# Drawing Buttons #-#
            if home_button.draw():
                return home
            if withdraw_button.draw():
                return withdraw
            if transfer_button.draw():
                return transfer
            if loan_button.draw():
                return loan

            if logout_button.draw():
                return login

            if doReturn == None:
                doReturn = button.draw()

            if doReturn:
                if Amount.text != "":
                    if int(Amount.text) <= account[1]:
                        ACCOUNTS[accno][1] -= int(Amount.text)
                        success = True
                    else:
                        errors.clear()
                        Text(
                            400,
                            300,
                            "Insufficient Balance",
                            errors,
                            font=sfont,
                            color="red",
                        )
                        doReturn = None
                else:
                    errors.clear()
                    Text(
                        400,
                        300,
                        "Please Enter an Amount",
                        errors,
                        font=sfont,
                        color="red",
                    )
                    doReturn = None

            if success:
                errors.clear()
                Text(
                    400,
                    300,
                    "Transaction Successful",
                    errors,
                    font=sfont,
                    color="green",
                )
                with open("accounts.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    for i in ACCOUNTS:
                        l = [i, ACCOUNTS[i][0], ACCOUNTS[i][1], ACCOUNTS[i][2]]
                        writer.writerow(l)
                success = False
                doReturn = None
                Amount.text = ""
                pin.text = ""
            screen.blit(logo, logorect)

            pg.display.update()
            clock.tick(60)

    def transfer():
        def challenge():
            print(account)

            if int(RAccNo.text) in ACCOUNTS:
                if int(pin.text) == account[0]:
                    if int(Amount.text) <= account[1]:
                        return True
                    else:
                        errors.clear()
                        Text(
                            400,
                            300,
                            "Insufficient Balance",
                            errors,
                            font=sfont,
                            color="red",
                        )
                        return False
                else:
                    errors.clear()
                    Text(400, 300, "Incorrect Pin", errors, font=sfont, color="red")
                    return False
            else:
                errors.clear()
                Text(
                    400, 300, "Invalid Account Number", errors, font=sfont, color="red"
                )
                return False

        text_list = []
        textbox_list = []
        errors = []
        logo = pg.image.load("logo.png").convert_alpha()
        logo = pg.transform.rotozoom(logo, 0, 0.3)
        logorect = logo.get_rect(center=(60, 35))
        Text(450, 20, f"Welcome {account[2]} | {accno}", text_list, align="midright")
        doReturn = None
        success = False

        home_button = Button(50, 100, 100, 20, "Home", "#dddddd", "#aaaaaa", font=sfont)
        withdraw_button = Button(
            50, 130, 100, 20, "Withdraw", "#dddddd", "#aaaaaa", font=sfont
        )
        transfer_button = Button(
            50, 160, 100, 20, "Transfer", "#dddddd", "#aaaaaa", font=sfont
        )
        loan_button = Button(50, 190, 100, 20, "Loan", "#dddddd", "#aaaaaa", font=sfont)

        logout_button = Button(
            50, 480, 100, 20, "Logout", "#dddddd", "#aaaaaa", font=sfont
        )

        Text(230, 120, "Amount :", text_list, font=font)
        Text(230, 170, "R-AccNo:", text_list, font=font)
        Text(230, 220, "PIN    :", text_list, font=font)

        Amount = Textbox(300, 120, 160, 40, textbox_list)
        RAccNo = Textbox(300, 170, 160, 40, textbox_list)
        pin = Textbox(300, 220, 160, 40, textbox_list, hidden=True)

        button = Button(
            300,
            370,
            160,
            40,
            "Confirm",
            "#dddddd",
            "#aaaaaa",
            font=font,
            action=challenge,
        )

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                for tb in textbox_list.copy():
                    if tb.active:
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_RETURN:
                                if tb.text != "":
                                    tb.active = False
                                    try:
                                        textbox_list[
                                            textbox_list.index(tb) + 1
                                        ].active = True
                                    except IndexError as e:
                                        print(e)
                                        if challenge():
                                            print("Valid")
                                            doReturn = True
                                            break
                                        else:
                                            invalidate = True
                            elif event.key == pg.K_BACKSPACE:
                                tb.text = tb.text[:-1]
                            else:
                                if event.unicode.isdigit():
                                    tb.text += event.unicode

            screen.fill("white")
            pg.draw.line(screen, "black", (100, 70), (100, 500), 2)
            pg.draw.line(screen, "black", (0, 70), (500, 70), 2)

            for i in text_list:
                i.draw()
            for i in textbox_list:
                i.draw(textbox_list)
            for i in errors:
                i.draw()
            # -# Drawing Buttons #-#
            if home_button.draw():
                return home
            if withdraw_button.draw():
                return withdraw
            if transfer_button.draw():
                return transfer
            if loan_button.draw():
                return loan

            if logout_button.draw():
                return login

            if doReturn == None:
                doReturn = button.draw()

            if doReturn:
                if Amount.text != "":
                    if int(Amount.text) <= account[1]:
                        ACCOUNTS[accno][1] -= int(Amount.text)
                        ACCOUNTS[int(RAccNo.text)][1] += int(Amount.text)
                        success = True
                    else:
                        errors.clear()
                        Text(
                            400,
                            300,
                            "Insufficient Balance",
                            errors,
                            font=sfont,
                            color="red",
                        )
                        doReturn = None
                else:
                    errors.clear()
                    Text(
                        400,
                        300,
                        "Please Enter an Amount",
                        errors,
                        font=sfont,
                        color="red",
                    )
                    doReturn = None

            if success:
                errors.clear()
                Text(
                    400,
                    300,
                    "Transaction Successful",
                    errors,
                    font=sfont,
                    color="green",
                )
                with open("accounts.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    for i in ACCOUNTS:
                        l = [i, ACCOUNTS[i][0], ACCOUNTS[i][1], ACCOUNTS[i][2]]
                        writer.writerow(l)
                success = False
                doReturn = None
                Amount.text = ""
                pin.text = ""
                RAccNo.text = ""
            screen.blit(logo, logorect)

            pg.display.update()
            clock.tick(60)

    def loan():
        def challenge():
            print(account)
            try:
                if int(pin.text) == account[0]:
                    if int(Amount.text) <= 20000:
                        return True
                    else:
                        errors.clear()
                        Text(
                            400,
                            300,
                            "Must be less than 20000",
                            errors,
                            font=sfont,
                            color="red",
                        )
                        return False
                else:
                    errors.clear()
                    Text(
                        250,
                        300,
                        "Incorrect Pin",
                        errors,
                        font=sfont,
                        color="red",
                        align="d-center",
                    )
                    return False
            except ValueError:
                errors.clear()
                Text(
                    250,
                    300,
                    "Invalid Amount",
                    errors,
                    font=sfont,
                    color="red",
                    align="d-center",
                )
                return False

        text_list = []
        textbox_list = []
        errors = []
        logo = pg.image.load("logo.png").convert_alpha()
        logo = pg.transform.rotozoom(logo, 0, 0.3)
        logorect = logo.get_rect(center=(60, 35))
        Text(450, 20, f"Welcome {account[2]} | {accno}", text_list, align="midright")
        doReturn = None
        success = False

        home_button = Button(50, 100, 100, 20, "Home", "#dddddd", "#aaaaaa", font=sfont)
        withdraw_button = Button(
            50, 130, 100, 20, "Withdraw", "#dddddd", "#aaaaaa", font=sfont
        )
        transfer_button = Button(
            50, 160, 100, 20, "Transfer", "#dddddd", "#aaaaaa", font=sfont
        )
        loan_button = Button(50, 190, 100, 20, "Loan", "#dddddd", "#aaaaaa", font=sfont)

        logout_button = Button(
            50, 480, 100, 20, "Logout", "#dddddd", "#aaaaaa", font=sfont
        )

        Text(230, 120, "Amount :", text_list, font=font)
        Text(230, 170, "PIN    :", text_list, font=font)

        Amount = Textbox(300, 120, 160, 40, textbox_list)
        pin = Textbox(300, 170, 160, 40, textbox_list, hidden=True)

        button = Button(
            300,
            370,
            160,
            40,
            "Confirm",
            "#dddddd",
            "#aaaaaa",
            font=font,
            action=challenge,
        )

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                for tb in textbox_list.copy():
                    if tb.active:
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_RETURN:
                                if tb.text != "":
                                    tb.active = False
                                    try:
                                        textbox_list[
                                            textbox_list.index(tb) + 1
                                        ].active = True
                                    except IndexError as e:
                                        print(e)
                                        if challenge():
                                            print("Valid")
                                            doReturn = True
                                            break
                                        else:
                                            invalidate = True
                            elif event.key == pg.K_BACKSPACE:
                                tb.text = tb.text[:-1]
                            else:
                                if event.unicode.isdigit():
                                    tb.text += event.unicode

            screen.fill("white")
            pg.draw.line(screen, "black", (100, 70), (100, 500), 2)
            pg.draw.line(screen, "black", (0, 70), (500, 70), 2)

            for i in text_list:
                i.draw()
            for i in textbox_list:
                i.draw(textbox_list)
            for i in errors:
                i.draw()
            # -# Drawing Buttons #-#
            if home_button.draw():
                return home
            if withdraw_button.draw():
                return withdraw
            if transfer_button.draw():
                return transfer
            if loan_button.draw():
                return loan

            if logout_button.draw():
                return login

            if doReturn == None:
                doReturn = button.draw()

            if doReturn:
                if Amount.text != "":
                    if int(Amount.text) <= account[1]:
                        ACCOUNTS[accno][1] += int(Amount.text)
                        success = True
                    else:
                        errors.clear()
                        Text(
                            400,
                            300,
                            "Insufficient Balance",
                            errors,
                            font=sfont,
                            color="red",
                        )
                        doReturn = None
                else:
                    errors.clear()
                    Text(
                        400,
                        300,
                        "Please Enter an Amount",
                        errors,
                        font=sfont,
                        color="red",
                    )
                    doReturn = None

            elif doReturn != None:
                doReturn = None

            if success:
                errors.clear()
                Text(
                    400,
                    300,
                    "Transaction Successful",
                    errors,
                    font=sfont,
                    color="green",
                )
                with open("accounts.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    for i in ACCOUNTS:
                        l = [i, ACCOUNTS[i][0], ACCOUNTS[i][1], ACCOUNTS[i][2]]
                        writer.writerow(l)
                success = False
                doReturn = None
                Amount.text = ""
                pin.text = ""
            screen.blit(logo, logorect)

            pg.display.update()
            clock.tick(60)

    func = home
    while True:
        if func == login:
            return login, None
        else:
            func = func()


# ---#  Initalize  #---#
if __name__ == "__main__":
    func = login
    para = ("1000",)
    while True:
        func, para = func(para)
