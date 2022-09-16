from tkinter import *
from TSP import *
from libs.GeneticAlgorithm import GeneticAlgorithm

def addtolist():
    global List

    List = []
    for item in varList:
        if item.get() != "":
            List.append(item.get())
    
    for i in List:
        x.append(d[i])
    
    s=[]
    l=List
    for i in range(len(l)):
        s.append(Itemloc(l[i],x[i]))
    WareHouse = Item()
    
        
    WareHouse.add(s)

    
    print('Selected Items:', end=' ')
    print(*(item for item in WareHouse.items), sep=', ')
    ga = GeneticAlgorithm(100, mutation_rate=0.5, ptype=Route, args=(WareHouse.items,))
    ga.run(seconds=40)
    fittest = ga.alltime_best
    best_fitness = fittest.fitness
    print('Best route:', fittest)
    print('Best fitness:', best_fitness)
    print('Generations:', ga.generation)
    #print(s)


List = []
varList = []
myApp = Tk()
myApp.title("Items-picking list")
myApp.geometry("1000x800")
d = {'Watch':(50,35),'Television':(37,39),'Bag':(26,35),'Book':(14,6),'Mobile':(7,18),'Laptop':(27,15),'Refrigerator':(9,12),'Air Conditioner':(42,36),'Pendrives':(16,8),'HDD':(31,37),'Flash card':(45,20),'Bottles':(35,8),'Fan':(9,24),'Ear phones':(5,24),'Electric Bulbs':(8,8),'Deodrants':(33,26),'Vaccum Cleaner':(32,40),'Sandals':(43,25),'Cameras':(29,24),'Power Banks':(46,27),'Blankets':(25,37),'Hair Dryer':(18,26),'Trimmer':(22,24),'Soaps':(18,20),'Washing Machine':(29,35),'Shoes':(20,41),'Goggles':(30,42),'Kerchiefs':(35,42),'Cosmetics':(44,21),'Shirts':(15,17),'Pants':(12,23),'Chairs':(23,32),'Tables':(24,39)}
x=[]


    
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
Check("Tables")

b1 = Button(myApp, text="Add to Picking List", command=addtolist)
b1.grid(row=30, column=50)
