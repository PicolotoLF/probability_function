# -*- coding: utf-8 -*-

import random
import math

class geometric(object):
    """
    :param p: probability of success
    :param r: number of attempts
    """
    def __init__(self, p, r):
        self.p = p
        self.r = r
        self.q = 1-p
        # NOTE(picoloto): P(X=r), r is attempts
        self.equals_r = self.p*(self.q**(self.r-1))
        # NOTE(picoloto): P(X>r)
        self.major_r = self.q**self.r
        # NOTE(picoloto): P(X=<r)
        self.minor_equals_r = 1-self.major_r
        self.E = 1/self.p
        self.var = self.q/(self.p**2)


    def results(self):
        return ("For {} attempts: \n #Probability first success ocur {}: {:03.3f} \n"
                " #Probability of more than {} attempts: {:03.3f}\n"
                " #Probability of less than or equal {} attempts: {:03.3f}\n"
                " #Expected value: {}\n"
                " #Variance: {:03.3f}"
                .format(self.r, self.r, self.equals_r, self.r, self.major_r, self.r, 
                        self.minor_equals_r, self.E, self.var))


class binomial(object):
    """
    :param n: number of objects, attempts
    :param r: number of success attempts
    :param p: probability of success
    """
    def __init__(self, n, r, p):
        self.n = n
        self.r = r
        self.p = p
        self.q = 1-p
        self.comb = self.combinations(self.n, self.r)
        self.value = self.calc()
        self.E = self.n*self.p
        self.var = self.n*self.p*self.q
    
    
    def combinations(self, n, r):
        return math.factorial(n)/(math.factorial(r)*math.factorial((n-r)))


    def calc(self):
        return self.comb * (self.p**self.r) * (self.q**(self.n-self.r))


    def results(self):
        return print("In {} attempts, to hit {}, with probability of success {}\n "
                    "#You have probability {} to hit".format(self.n, self.r, self.p, self.value))


class poisson(object):
    """
    :param lamb: mean
    :param r: value that may ocur
    """    
    def __init__(self, lamb, r):
        self.lamb = lamb
        self.r = r
        self.value = self.calc()


    def calc(self):
        return(((math.exp(1))**-self.lamb) * (self.lamb**self.r)) / math.factorial(self.r)


    def results(self):
        return(print("With mean {}, the probability to ocur {} is: {}".format(self.lamb, self.r, self.value)))
