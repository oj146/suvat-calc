#!/usr/bin/python3
from math import sqrt

class Suvat:

    def __init__(self,s,u,v,a,t,mode='r'): 
        """mode is 'r' or 'c', raw or in context. Choose to return raw values (float, makes reusability easier) or
        as a statement (to avoid confusion). returns raw as default."""
        self.s = s
        self.u = u
        self.v = v
        self.a = a
        self.t = t
        self.mode = mode

    def s1(self):
        if self.t == '?':
            exp = lambda a: (self.u**2 + self.v**2)/(2*a)
            if self.mode == 'c':
                return f"Displacement: {exp(self.a)}m"
            return exp(self.a)
        if self.a == '?':
            exp = lambda t: (t/2) * (self.u + self.v)
        elif self.v == '?':
            exp = lambda t: self.u*t + (0.5 * self.a * t**0)
        elif self.u == '?':
            exp = lambda t: self.v*t - (0.5 * self.a * t**0)
        if self.mode == 'c':
            return f"Displacement: {exp(self.t)}m"
        return exp(self.t)

    def u1(self):
        if self.t == '?':
            exp = lambda a: sqrt((2*a*self.s)-self.v**2)
            if self.mode == 'c':
                return f"Initial Velocity: {exp(self.a)}ms^-1"
            return exp(self.a)
        elif self.a == '?':
            exp = lambda t: ((2*self.s)/t)+self.v
        elif self.v == '?':
            exp = lambda t: (self.s-(self.a*(t**2)))/(2*t)
        elif self.s == '?':
            exp = lambda t: self.v-(self.a*t)
        if self.mode == 'c':            
            return f"Initial Velocity: {exp(self.t)}ms^-1"
        return exp(self.t)
    
    def v1(self):
        if self.t == '?':
            exp = lambda a: sqrt((2*a*self.s)+(self.u**2))
            if self.mode == 'c':
                return f"Final Velocity: {exp(self.a)}ms^-1"
            return exp(self.a)
        elif self.a == '?':
            exp = lambda t: ((2*self.s)/t)-self.u
        elif self.u == '?':
            exp = lambda t: (self.s+(self.a*t**2))/(2*t)
        elif self.s == '?':
            exp = lambda t: self.u+(self.a*t)
        if self.mode == 'c':
            return f"Final Velocity: {exp(self.t)}ms^-1"   
        return exp(self.t)

    def a1(self):
        if self.t == '?':
            exp = lambda v: (v**2-self.u**2)/(2*self.s)
            if self.mode == 'c':
                return f"Acceleration: {exp(self.v)}ms^-2"
            return exp(self.v)
        elif self.v == '?':
            exp = lambda t: (2*(self.s-(self.u*self.t)))/t**2
        elif self.u == '?':
            exp = lambda t: (2*((self.v*self.t)-self.s))/t**2
        elif self.s == '?':
            exp = lambda t: (self.v-self.u)/t
        if self.mode == 'c':
            return f"Acceleration: {exp(self.t)}ms^-2"   
        return exp(self.t)      

    def t1(self):
        if self.a == '?':
            exp = lambda s: (2*s)/(self.u+self.v)
            if self.mode == 'c':
                return f"Time: {exp(self.s)}s"
            return exp(self.s)
        if self.s == '?':
            exp = lambda a: (self.v - self.u)/a
        elif self.v == '?':
            exp = lambda a: (sqrt((2*a*self.s)+(self.u**2))-self.u)/a
        elif self.u == '?':
            exp = lambda a: (self.v-(sqrt((self.v**2)-(2*a*self.s))))/a
        if self.mode == 'c':
            return f"Time: {exp(self.a)}s"
        return exp(self.a)     

    def all(self):
        myDict = {}
        if self.s == '?':
            myDict["s"] = self.s1()
        else:
            myDict["s"] = self.s
        if self.u == '?':
            myDict["u"] = self.u1()
        else:
            myDict["u"] = self.u
        if self.v == '?':
            myDict["v"] = self.v1()
        else:
            myDict["v"] = self.v
        if self.a == '?':
            myDict["a"] = self.a1()
        else:
            myDict["a"] = self.a
        if self.t == '?':
            myDict["t"] = self.t1()
        else:
            myDict["t"] = self.t
        return myDict

suvat = Suvat('?',0,17,3.4,'?')
print(suvat.all())



                  

        

        
