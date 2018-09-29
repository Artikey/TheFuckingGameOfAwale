from Const import *
from Btn import Btn

class Board:
    def __init__(self):
        self.dictTrou = {1:[4,blanc],
                         2:[4,blanc],
                         3:[4,blanc],
                         4:[4,blanc],
                         5:[4,blanc],
                         6:[4,blanc],
                         7:[1,blanc],
                         8:[4,blanc],
                         9:[4,blanc],
                        10:[4,blanc],
                        11:[4,blanc],
                        12:[4,blanc]
                        }
        self.btnList = []
        a = 1
        while a < 7:
            self.btnList.append(Btn(-35+110*a,400,100,50))
            a += 1
        self.scorePlayer = 0
        self.scoreEnemy = 0

    def draw(self):
        window.fill((0,0,0))
        window.blit(fontSize(45).render("Player: "+str(self.scorePlayer), True, blanc),(100,100))
        window.blit(fontSize(45).render("Enemy: "+str(self.scoreEnemy), True, blanc),(700,100))
        pygame.draw.rect(window,blanc,(50,392,700,5))

        trot=0
        for t in self.dictTrou:
            trot+=1
            pygame.draw.ellipse(window, self.dictTrou[t][1],(-35+110*trot,400,100,50))
            window.blit(fontSize(45).render(str(self.dictTrou[t][0]), True, noir),(-35+40+110*trot,420))
            if trot == 6:
                break
        trot=0
        for t in self.dictTrou:
            if t >= 7:
                trot+=1
                pygame.draw.ellipse(window, self.dictTrou[t][1],(735-(110*trot),340,100,50))
                window.blit(fontSize(45).render(str(self.dictTrou[t][0]), True, noir),(760-(110*trot),350))


    """ not GUI part"""
    def ref(self):
        trot = 0
        slct = 0
        for btn in self.btnList:
            btn.ref()
            trot+=1
            prss = btn.getPress()
            self.dictTrou[trot][1] = blanc
            if prss[0]:
                self.dictTrou[trot][1] = noir
                if prss[1]:
                    slct = trot
        if slct != 0:
            if self.dictTrou[slct][0] != 0:
                trot=slct
                while self.dictTrou[slct][0] > 0:
                    trot += 1
                    if trot == 13:
                        trot = 1
                    self.dictTrou[trot][0] += 1
                    self.dictTrou[slct][0] -= 1
                print("whoup! \o/\n")
                if (self.dictTrou[trot][0] == 2 or self.dictTrou[trot][0] == 3) and \
                (trot>=7 and trot<=12):
                    self.scorePlayer += self.dictTrou[trot][0]
                    self.dictTrou[trot][0] = 0

            else:
                print("Ce trou est vide!!! (connard)")

