import pygame as pg;from random import shuffle

pg.init()

class Maze:
    
    def __init__(self):
        self.size=(800,800)#definition de la taille
        self.windows=pg.display.set_mode(self.size)#creation de la fenêtre de départ
        pg.display.set_caption("Maze")#nommage de la fenêtre de départ
        self.clock=pg.time.Clock()#définition d'une horloge
        self.cursor=self.init=(0,0)#position initiale du curseur et de joueur
        self.bankStack=[]#initialisation de la pile
        self.valid=True#si le labbyrinthe doit encore être travailler
        self.voidMaze()#création d'un labyrinthe encore vierge, chaque case est représenter par une liste [False,False]
                       #le premier booléen est le mur à droite de la case et le second est le mur sous la case,
                       #un False représente un mur et un True un passage
    def stack(self,act,pos=None):#gestionnaire de la pile seul fonction à agir dessus
        if act=="add":self.bankStack.append(pos)#ajouter
        elif act=="del" and len(self.bankStack)>0:self.cursor=self.bankStack.pop()#prendre et supprimer la dernière valeur
        else:
            self.valid=False#arrêt de la fonction drill
            self.maze[19][19][0]=True#percage de la sortie
            self.adjacent.append(None)
        
    def voidMaze(self):self.maze=[[[False,False] for _ in range(20)] for _ in range(20)]#création du labyrinthe

    def show(self):
        self.windows.fill((255,255,255))#background blanc
        pg.draw.line(self.windows,(0,0,0),(0,40),(0,self.size[1]),3)#mur de gauche
        pg.draw.line(self.windows,(0,0,0),(0,0),(self.size[0],0),3)#mur du haut
        for y in range(len(self.maze)):#parcour sur l'axe des absysses
            for x in range(len(self.maze[y])):#parcour sur l'axe des ordonnée
                if not self.maze[y][x][0]:pg.draw.line(self.windows,(0,0,0),((x+1)*40-1,y*40-1),((x+1)*40-1,(y+1)*40-1),3)#murs des gauches
                if not self.maze[y][x][1]:pg.draw.line(self.windows,(0,0,0),(x*40-1,(y+1)*40-1),((x+1)*40-1,(y+1)*40-1),3)#murs des droites

    def drill(self):#fonction qui va percer mon labyrinthe
        self.adjacent=self.unvisited()#regarde toute les case libre autour
        while len(self.adjacent)==0:#si il n'y en à aucune
            self.stack("del")#le curseur repart en arrière
            if len(self.adjacent)==0:
                self.adjacent=self.unvisited()#regarde les case libre proche de cette nouvelle position
        if self.adjacent[0]==None:return
        shuffle(self.adjacent)#mélange la liste de case libre
        des=self.adjacent[0]#prend la première valeur de cette liste mélanger et donc une valeur aléatoire
        if des[1]=="r":self.maze[self.cursor[1]][self.cursor[0]][0]=True
        if des[1]=="b":self.maze[self.cursor[1]][self.cursor[0]][1]=True
        self.cursor=des[0]
        if des[1]=="l":self.maze[self.cursor[1]][self.cursor[0]][0]=True
        if des[1]=="t":self.maze[self.cursor[1]][self.cursor[0]][1]=True
        self.stack("add",self.cursor)#ajoute la position actuelle du curseur à la pile
            
    def unvisited(self):
        no=[]
        if self.cursor[1]!=0 and self.maze[self.cursor[1]-1][self.cursor[0]]==[False,False]:no.append([(self.cursor[0],self.cursor[1]-1),"t"])
        if self.cursor[1]!=19 and self.maze[self.cursor[1]+1][self.cursor[0]]==[False,False]:no.append([(self.cursor[0],self.cursor[1]+1),"b"])
        if self.cursor[0]!=19 and self.maze[self.cursor[1]][self.cursor[0]+1]==[False,False]:no.append([(self.cursor[0]+1,self.cursor[1]),"r"])
        if self.cursor[0]!=0 and self.maze[self.cursor[1]][self.cursor[0]-1]==[False,False]:no.append([(self.cursor[0]-1,self.cursor[1]),"l"])
        return no

    def running(self):#boucle de jeu
        run=True#invariant
        while run:#départ
            if self.valid:self.drill()#vérifie que le labyrinthe n'es pas déja visitable
            self.show()#affiche le labyrinthe
            for event in pg.event.get():#condition d'arrêt
                if event.type==pg.QUIT:run=False#destruction de la boucle
            pg.display.flip();self.clock.tick(60)#MaJ de la fenêtre,limitation de la vitesse d'éxecution du jeu
        pg.quit()
            
maze=Maze();maze.running()
pg.quit()