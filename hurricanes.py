'''
Name - Siddhant Bhardwaj
Collaborator - Vibhor Mehta
Programming HW3
'''

import numpy as np, scipy as sp, pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats
from distribution import Distribution

class HurricaneSeason(Distribution):
    def likelihood(self,data,hypothesis):
        return sp.stats.poisson.pmf(data,hypothesis)

    def update(self,data):
        for k in self.dist:
            self.dist[k] *= self.likelihood(data,k)
        self.normalize()

    def fit(self,df,start_yr,end_yr):
        for i in range(start_yr,end_yr + 1):
            self.update(df.loc[i,'Hurricanes'])

    def mean(self):
        return sum(key1 * self.dist[key1] for key1 in self.dist)

    def predict(self,n):
        simulations = []
        for i in range(n):
            gamma = self.sample()
            simulations.append(sp.stats.poisson.rvs(gamma))
        return simulations
        
    def posterior_interval(self,c):
        lower = 0
        upper = 0
        total = 0
        lower_bound = (1 - c)/2
        upper_bound = (c + (1 - c)/2)
        for key in self.dist:
            if total + self.dist[key] > lower_bound and lower == 0:
                lower = key
            if total + self.dist[key] > upper_bound and upper == 0:
                upper = key
            total += self.dist[key]
        return [lower,upper]
    
    
    def predictive_interval(self,c):
        simulations = sorted(self.predict(1000))
        lower_bound = int(((1 - c)/2) * len(simulations))
        upper_bound = int((c + (1 - c)/2) * len(simulations))
        simulations  = list(set(simulations[lower_bound:upper_bound]))
        return [simulations[0],simulations[-1]]
            
def fit_models(df):
    grid1 = np.linspace(0,11,114)
    grid2 = np.linspace(2,12,35)
    grid3 = np.linspace(2,15,17)
    y1 = sp.stats.norm.pdf(grid1,5.11,2.31)
    y2 = sp.stats.norm.pdf(grid2,6.14,2.46)
    y3 = sp.stats.norm.pdf(grid3,6.76,3.43)
    prior1 = {grid1[i]:y1[i] for i in range(len(grid1))}
    prior2 = {grid2[i]:y2[i] for i in range(len(grid2))}
    prior3 = {grid3[i]:y3[i] for i in range(len(grid3))}
    model1 = HurricaneSeason(prior1)
    model2 = HurricaneSeason(prior2)
    model3 = HurricaneSeason(prior3)
    model1.fit(df,1851,1964)
    model2.fit(df,1965,2000)
    model3.fit(df,2001,2017)
    return [model1,model2,model3]

def make_histogram(hm):
    simulations = np.array(hm.predict(500))
    fig,ax = plt.subplots(1,1)
    ax.hist(simulations,bins = np.arange(1,30,1) - 0.5)
    ax.set_title("Histogram of Simulations")
    ax.set_xlabel("Simulated Hurricanes")
    ax.set_ylabel("Frequency")
    plt.show()
    
def main():
    df = pd.read_csv('hurricanes.csv',index_col=0)
    lst1 = fit_models(df)
    for i in range(len(lst1)):
        print("---------------")
        if i == 0:
            print("Year range: 1851-1964")
        elif i == 1:
            print("Year range: 1965-2000")
        else:
            print("Year range: 2001-2017")
        print("Mean: " + str(lst1[i].mean()))
        print("Posterior Interval: " + str(lst1[i].posterior_interval(0.9)))
        print("Predictive Interval: " + str(lst1[i].predictive_interval(0.9)))
        print("----------------")
        make_histogram(lst1[i])
    
if __name__ == "__main__":
    main()