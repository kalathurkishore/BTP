from tkinter import *
from TSP import *
from libs.GeneticAlgorithm import GeneticAlgorithm
import pygame
import matplotlib.pyplot as plt
import numpy as np

gen = []
fitn = []
List = []
varList = []
myApp = Tk()
myApp.title("Items-picking list")
myApp.geometry("1000x800")
d = {'Watch':(50,35),'Television':(37,39),'Bag':(26,35),'Book':(14,6),'Mobile':(7,18),'Laptop':(27,15),'Refrigerator':(9,12),'Air Conditioner':(42,36),'Pendrives':(16,8),'HDD':(31,37),'Flash card':(45,20),'Bottles':(35,8),'Fan':(9,24),'Ear phones':(5,24),'Electric Bulbs':(8,8),'Deodrants':(33,26),'Vaccum Cleaner':(32,40),'Sandals':(43,25),'Cameras':(29,24),'Power Banks':(46,27),'Blankets':(25,37),'Hair Dryer':(18,26),'Trimmer':(22,24),'Soaps':(18,20),'Washing Machine':(29,35),'Shoes':(20,41),'Goggles':(30,42),'Kerchiefs':(35,42),'Cosmetics':(44,21),'Shirts':(15,17),'Pants':(12,23),'Chairs':(23,32)}
p=[]

#myApp.configure(background='')


    
def map_items_onto_screen(items):
    for item in items:
        y = -int(15 * (item.x - 54))
        x = int(20 * (item.y - 3.5))
        yield (x, y)


def text_labels(items, population_size, mutation_rate):
    global arial_norm, arial_small
    arial_norm = pygame.font.SysFont('arial', 25)
    arial_small = pygame.font.SysFont('arial', 16)
    labels = []
    for item, (posx, posy) in zip(items, map_items_onto_screen(items)):
        labels.append((arial_norm.render(item.name, 1, (255, 255, 255)), (posx - 45, posy - 15)))
    labels.append((arial_small.render('Population size: {}'.format(population_size), 1, (255, 255, 255)), (1100, 10)))
    labels.append((arial_small.render('item count: {}'.format(len(items)), 1, (255, 255, 255)), (1100, 25)))
    labels.append((arial_small.render('Mutation rate: {}'.format(mutation_rate), 1, (255, 255, 255)), (1100, 40)))
    return labels


def addtolist():
    global List

    List = []
    for item in varList:
        if item.get() != "":
            List.append(item.get())
    
    for i in List:
        p.append(d[i])
    
    s=[]
    l=List
    for i in range(len(l)):
        s.append(Itemloc(l[i],p[i]))
    WareHouse = Item()
    
        
    WareHouse.add(s)

    population_size = 20
    mutation_rate = 0.01
    skipped_frames = 108

    pygame.init()
    pygame.display.set_caption('Picking Routes in warehouse')
    screen = pygame.display.set_mode((1300, 780))
    stat_labels = text_labels(WareHouse.items, population_size, mutation_rate)
    ga = GeneticAlgorithm(population_size, mutation_rate, ptype=Route, args=(WareHouse.items,))
    alltime_fittest = ga.alltime_best
    alltime_fitness = 0
    refresh = True

    ''' Main loop '''
    while refresh:
        ''' Event handling '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                refresh = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = True
                    while pause:
                        event2 = pygame.event.wait()
                        if event2.type == pygame.KEYDOWN and event2.key == pygame.K_SPACE:
                            pause = False
                        elif event2.type == pygame.QUIT:
                            pause = False
                            refresh = False

        ''' Genetic Algorithm process + statistics '''
        ga.run(reps=skipped_frames)
        current_best = ga.best()
        alltime_fittest = ga.alltime_best
        alltime_fitness = alltime_fittest.raw_fitness
		
		
	
        ''' Drawing part '''
        screen.fill((0, 0, 0))
        for point in map_items_onto_screen(WareHouse.items):
            pygame.draw.circle(screen, (255, 255, 255), point, 3)
        pygame.draw.aalines(screen, (100, 100, 25), True, list(map_items_onto_screen(current_best.genes)))
        pygame.draw.aalines(screen, (255, 255, 255), True, list(map_items_onto_screen(alltime_fittest.genes)))
		#gen.append(ga.generation)
		#fit.append(current_best.raw_fitness)
        x=ga.generation
        y=current_best.raw_fitness
        gen.append(x)
        fitn.append(y)
        screen.blit(arial_small.render('Generation: {}'.format(x), 1, (255, 255, 255)), (1100, 55))
        screen.blit(arial_small.render('Fitness: {:.4f}'.format(alltime_fitness), 1, (255, 255, 255)), (1100, 70))
        screen.blit(arial_small.render('Current Fitness: {:.4f}'.format(y), 1, (255, 255, 0)), (1100, 85))
        for label in stat_labels:
            screen.blit(label[0], label[1])
        pygame.display.flip()
        
    print('Selected Items:', end=' ')
    print(*(item for item in WareHouse.items), sep=', ')
    print('Best route:', alltime_fittest)
    print('Best fitness:', alltime_fitness)
    plt.plot(gen,fitn)
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.show()
    
class Check:
    x = 0
    def __init__(self, lbl):
        self.var = StringVar()
        self.cb = Checkbutton(myApp, text=lbl, variable=self.var,
                              onvalue=lbl, offvalue="")
        self.cb.grid(row=Check.x, column=1, sticky=W)
        Check.x += 1
        varList.append(self.var)


Check("Watch")
Check("Television")
Check("Bag")
Check("Book")
Check("Mobile")
Check("Laptop")
Check("Refrigerator")
Check("Air Conditioner")
Check("Pendrives")
Check("HDD")
Check("Flash card")
Check("Bottles")
Check("Fan")
Check("Ear phones")
Check("Electric Bulbs")
Check("Deodrants")
Check("Vaccum Cleaner")
Check("Sandals")
Check("Cameras")
Check("Power Banks")
Check("Blankets")
Check("Hair Dryer")
Check("Trimmer")
Check("Soaps")
Check("Washing Machine")
Check("Shoes")
Check("Goggles")
Check("Kerchiefs")
Check("Cosmetics")
Check("Shirts")
Check("Pants")
Check("Chairs")


b1 = Button(myApp, text="Add to Picking List", command=addtolist)
b1.grid(row=30, column=50)
