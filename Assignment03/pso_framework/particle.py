import random

class Particle:
    def __init__(self, dim, limits):
        self.dim = dim
        self.limits = limits

        self.pos = [random.randint(limits[0][0],limits[0][1]),random.randint(limits[1][0],limits[1][1])]
        point1 = [random.randint(limits[0][0],limits[0][1]),random.randint(limits[1][0],limits[1][1])]
        point2 = [random.randint(limits[0][0],limits[0][1]),random.randint(limits[1][0],limits[1][1])]
        self.vel = [(point1[0]-point2[0]/2), (point1[1]-point2[1]/2)] # Picking half the velocity from two random points
        self.bestPostion=[]
        self.bestFitness=0
        self.bestPostionInformant=[]
        self.bestFitnessInformnat = 0

    # TODO: further functions of a particle
    def get_pos(self):
        return self.pos

    def get_vel(self):
        return self.vel

    def set_pos(self,pos):
        self.pos=pos

    def set_vel(self,vel):
        self.vel=vel

    def getParticleBestFitnessInformnat(self):
        return self.bestFitnessInformnat

    def getParticleBestPostion(self):
        return self.bestPostion

    def updateParticle(self,updated_Velocity):
        self.pos= [sum(i) for i in zip(self.pos, updated_Velocity)]
        self.vel=updated_Velocity

    def updateParticleBestPostion(self,fitness):
        if self.bestPostion ==0 or  self.bestFitness<fitness:
            self.bestPostion=self.pos
            self.bestFitness=fitness

    def getParticleBestPostionInformants(self,informants):
        informantBest=0
        for i in informants:
            if informantBest==0 or i.getParticleBestFitnessInformnat()<self.bestFitnessInformnat:
                self.bestPostionInformant=i.pos
        return self.bestPostionInformant






