from Const import *

class Board:
    def __init__(self):
        self.dictTrou = {1:4,
                        2:4,
                        3:4,
                        4:4,
                        5:4,
                        6:4,
                        7: 4,
                        8: 4,
                        9: 4,
                        10: 4,
                        11: 4,
                        12:4
                        }
        self.scorePlayer = 0
        self.scoreFDP = 0
    
    def draw(self):
        window.fill((0,0,0))
        trot=0
        troty=1
        for t in self.dictTrou:
            trot+=1
            pygame.draw.ellipse(window, (255,255,255),(-35+110*trot,280+60*troty,100,50))
            if trot == 6:
                troty = 2
                trot = 0

    def ref(self):
        badKey=True
        while badKey:
            slct = int(input("-> "))
            if slct <=6 and slct >=1:
                badKey = False
        
        if self.dictTrou[slct] != 0:
            trot=slct
            while self.dictTrou[slct] > 0:
                trot += 1
                if trot == 13:
                    trot = 1     
                self.dictTrou[trot] += 1
                self.dictTrou[slct] -= 1
            print("whoup! \o/\n")
            if (self.dictTrou[trot] == 2 or self.dictTrou[trot] == 3) and \
            (trot>=7 and trot<=12):
                self.scorePlayer += self.dictTrou[trot]
                self.dictTrou[trot] = 0
                    
        else:
            print("Ce trou est vide!!! (connard)")
            self.ref()
        
