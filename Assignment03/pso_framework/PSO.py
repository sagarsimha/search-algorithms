import random

from particle import Particle
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPoint
import math

class PSO:
    def __init__(self, swarm_size, dim, limits, params=[0.05, .05, 0.5, 1, 1]): #[0.05, .05, .5, 1, 1] 
        """
        TODO: play around with the default parameters in the argument list
        :param swarm_size: integer, defining how many individuals the population holds
        :param dim: dimension of the problem (for visualization 2 is used)
        :param limits: array defining the limits for each dimension (eg. for 2 dims: [[x_min, x_max], [y_min, y_max]])
        :param params: [alpha, beta, gamma, delta, epsilon] default=[0.75, 0.4, 0.5, 0.6, 0.05]
        """
        self.alpha = params[0]
        self.beta = params[1]
        self.gamma = params[2]
        self.delta = params[3]
        self.epsilon = params[4]
        self.dim = dim
        self.limits = limits
        self.population = self.initialization(swarm_size)
        
        self.best = self.population[0]
        self.swarm_size=swarm_size
        self.n_Informents=int(0.4*self.swarm_size)
        # TODO: implement further problem initialization

    def update(self, mouse_pos):

        """
        One call of update represents one iteration of the outer loop of the PSA algorithm.
        There is no return value.
        After each call of this function, the points are redrawn
        :param mouse_pos:
        """ 

        # best is the particle which is closest to the mouse_pos
        for x in self.population:
            fitness=self.assess_fitness(x.get_pos(),mouse_pos)
            x.updateParticleBestPostion(fitness)
            if self.best==self.population[0] or  fitness < self.assess_fitness(self.best.get_pos(),mouse_pos):
                #print(x.get_pos())
                self.best=x

        for x in self.population:
            informants=[ self.population[i] for i in random.sample(range(1, self.swarm_size), self.n_Informents)]

            xSelfBest=x.getParticleBestPostion()
            xFittestInforment=x.getParticleBestPostionInformants(informants)
            xGlobalBest=self.best.get_pos()
            updated_Velocity=[]
            current_Velocity=x.get_vel()
            current_location=x.get_pos()

            for i in range(self.dim):
                b = random.uniform(0, self.beta)
                c = random.uniform(0, self.gamma)
                d = random.uniform(0, self.delta)
                partA=self.alpha*current_Velocity[i]
                partB=b*(xSelfBest[i] - current_location[i])
                partC=c*(xFittestInforment[i] - current_location[i])
                #partD=d*(xGlobalBest[i] - current_location[i])
                partD=d*(mouse_pos[i] - current_location[i])# The global optimum keeps changing
                updated_Velocity.append(self.epsilon*(partA + partB + partC+ partD))


            x.updateParticle(updated_Velocity)
      

    def draw(self, painter):
        color = QColor(0, 0, 0)
        painter.setBrush(color)
        painter.setPen(QColor(0, 0, 0, 0))
        for item in self.population:
            position = QPoint(item.pos[0], item.pos[1])
            painter.drawEllipse(position, 4, 4)

    def assess_fitness(self,pos, mouse_pos):
        #Euclidean distance between mouse_pos and particle pos
    	return math.sqrt((mouse_pos[0]-pos[0])**2 + (mouse_pos[1]-pos[1])**2)
    	

    def initialization(self,swarm_size):
        pop=[]
        for i in range(swarm_size):
            pop.append(Particle(self.dim, self.limits))
        return pop


#Reference
#Jupyter Notebook - Lecture Notes