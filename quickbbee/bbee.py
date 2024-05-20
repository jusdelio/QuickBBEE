#!/usr/bin/env python
# Author : Giulio GANCI and Emmanuel RASOLOFO
import math as m
import numpy as np
from cosmopower import cosmopower_NN
from cosmopower import cosmopower_PCAplusNN
from numbers import Number
import os
dirname = os.path.dirname(os.path.abspath(__file__))


def verify(val, interval, indice):
    params_name = ['H0', 'Alens', 'r', 'tau', 'ns', 'As', 'ombh2', 'omch2']
    if isinstance(val, list):
        for i in range(len(val)):
            if val[i] < interval[0] or val[i] > interval[1]:
                raise ValueError(f"Invalid Interval Usage: The parameters {params_name[indice]} = {val[i]} is not in {interval}\n")
    else:
        if val < interval[0] or val > interval[1]:
                raise ValueError(f"Invalid Interval Usage: The parameters {params_name[indice]} = {val} is not in {interval}\n")
        return True
    
        

class set_dparams:     
    def __init__(self, 
                 H0:None, 
                 Alens:None, 
                 r:None, 
                 tau:None, 
                 ns:None, 
                 As:None, 
                 ombh2:None, 
                 omch2:None, 
                 lmax=2400):
        
        '''CONSTRUCTOR'''
        super(set_dparams, self).__init__()
        
        #verify variables
        verify(H0, [65, 75], 0)
        verify(Alens, [0, 1], 1) 
        verify(r, [0, 0.5], 2) 
        verify(tau ,[0.03, 0.09], 3) 
        verify(ns, [0.94, 0.99], 4) 
        verify(As, [m.exp(3.0)*10**-10, m.exp(3.5)*10**-10], 5) 
        verify(ombh2, [0.020, 0.025], 6) 
        verify(omch2, [0.05, 0.3], 7)
        
        if lmax < 0 or lmax > 2400:
            raise ValueError("lmax should be between: 0 and 2400.")
        
        #set variables
        self.lmax = lmax
        self.H0 = H0
        self.Alens = Alens
        self.r = r
        self.tau = tau
        self.ns = ns
        self.As = As
        self.ombh2 = ombh2
        self.omch2 = omch2
        self.range_default = np.array([[65, 75],
                           [0, 1],
                           [0, 0.5],
                           [0.03, 0.09],
                           [0.94, 0.99],
                           [m.exp(3.0)*10**-10, m.exp(3.5)*10**-10],
                           [0.02, 0.025],
                           [0.05, 0.30]
                           ])
        #model params_range specified by the user
        self.range = None
        
    def check(self):
        attribut = [self.H0, self.Alens,
                    self.r,
                    self.tau,
                    self.ns,
                    self.As,
                    self.ombh2,
                    self.omch2]
        all_l = 0
        all_num = 0
        
        for att in attribut:
            if isinstance(att, list):
                all_l += 1
            if isinstance(att, Number):
                all_num += 1
        if all_l == len(attribut):
            return True
    
        if all_num == len(attribut):
            return False

        else:
            raise ValueError("All parameters are not the same type.")
        
    def get_spectra(self):       
        cp_nn_EE = cosmopower_NN(restore=True,
                        restore_filename = os.path.join(dirname,'./EE_BB_models/cp_NN_EE'),
                        )
        cp_nn_BB = cosmopower_NN(restore=True,
                        restore_filename = os.path.join(dirname,'./EE_BB_models/cp_NN_BB'),
                        )
        
        if self.check():
            params = {
                'H0' : self.H0,
                'Alens':self.Alens,
                'r':self.r,
                'tau':self.tau,
                'ns':self.ns,
                'As':self.As,
                'ombh2':self.ombh2,
                'omch2':self.omch2
            }
        else:
            params = {
                'H0' : [self.H0],
                'Alens':[self.Alens],
                'r':[self.r],
                'tau':[self.tau],
                'ns':[self.ns],
                'As':[self.As],
                'ombh2':[self.ombh2],
                'omch2':[self.omch2]
            }            
        predicted_EE = cp_nn_EE.ten_to_predictions_np(params)[:, :self.lmax]
        predicted_BB = cp_nn_BB.ten_to_predictions_np(params)[:, :self.lmax]
        return np.vstack((predicted_BB, predicted_EE))
    
    def get_params_interval(self, show=True, new_params=None):
        if show:
            print(f"Intervals:\nH0: {self.range_default[0]}\nAlens: {self.range_default[1]}\nr: {self.range_default[2]}\ntau: {self.range_default[3]}\nns: {self.range_default[4]}\nAs: {self.range_default[5]}\nombh2: {self.range_default[6]}\nomch2: {self.range_default[7]}\n")
        return self.range_default
    
class set_cparams:
    def __init__(self, 
                 H0:None, 
                 Alens:None, 
                 r:None, 
                 tau:None, 
                 ns:None, 
                 As:None, 
                 ombh2:None, 
                 omch2:None,
                 filepath_model:None,
                 params_range:None,
                 is_PCA:bool,
                 logspectra:bool,
                 lmax:None
                 ):
        
        '''CONSTRUCTOR'''
        super(set_cparams, self).__init__()
              
        if lmax < 0:
            raise ValueError("lmax should be positif.")
        
        #set variables
        self.lmax = lmax
        self.H0 = H0
        self.Alens = Alens
        self.r = r
        self.tau = tau
        self.ns = ns
        self.As = As
        self.ombh2 = ombh2
        self.omch2 = omch2
        self.filepath_model = filepath_model
        self.params_range = params_range
        self.is_PCA = is_PCA
        self.logspectra = logspectra

        #verify variables
        verify(H0, self.params_range[0], 0)
        verify(Alens, self.params_range[1], 1) 
        verify(r, self.params_range[2], 2) 
        verify(tau ,self.params_range[3], 3) 
        verify(ns, self.params_range[4], 4) 
        verify(As, self.params_range[5], 5) 
        verify(ombh2, self.params_range[6], 6) 
        verify(omch2, self.params_range[7], 7)

    def check(self):
        attribut = [self.H0, self.Alens,
                    self.r,
                    self.tau,
                    self.ns,
                    self.As,
                    self.ombh2,
                    self.omch2]
        all_l = 0
        all_num = 0
        
        for att in attribut:
            if isinstance(att, list):
                all_l += 1
            if isinstance(att, Number):
                all_num += 1
        if all_l == len(attribut):
            return True
    
        if all_num == len(attribut):
            return False

        else:
            raise ValueError("All parameters are not the same type.")
        
        
    def get_spectra(self):
        if self.check():
            params = {
                'H0' : self.H0,
                'Alens':self.Alens,
                'r':self.r,
                'tau':self.tau,
                'ns':self.ns,
                'As':self.As,
                'ombh2':self.ombh2,
                'omch2':self.omch2
            }
        else:
            params = {
                'H0' : [self.H0],
                'Alens':[self.Alens],
                'r':[self.r],
                'tau':[self.tau],
                'ns':[self.ns],
                'As':[self.As],
                'ombh2':[self.ombh2],
                'omch2':[self.omch2]
            }     
        
        chemin_absolu = os.path.abspath(self.filepath_model) 
        print(f"Model used in: {chemin_absolu}\n")
          

        cp_nn = None
        predicted = None
        if(self.is_PCA):
            cp_nn = cosmopower_PCAplusNN(restore=True,
                        restore_filename=chemin_absolu,
                        )
            if self.logspectra:
                predicted = cp_nn.ten_to_predictions_np(params)[:, :self.lmax]
            else:
                predicted = cp_nn.predictions_np(params)[:, :self.lmax]
            return predicted
            
        else:
            cp_nn = cosmopower_NN(restore=True,
                        restore_filename=chemin_absolu,
                        )
            if self.logspectra:
                predicted = cp_nn.ten_to_predictions_np(params)[:, :self.lmax]
            else:
                predicted = cp_nn.predictions_np(params)[:, :self.lmax]
            return predicted
        
            
        
        

    
    def get_params_interval(self, show=True):
        if show:
            print(f"Intervals:\nH0: {self.params_range[0]}\nAlens: {self.params_range[1]}\nr: {self.params_range[2]}\ntau: {self.params_range[3]}\nns: {self.params_range[4]}\nAs: {self.params_range[5]}\nombh2: {self.params_range[6]}\nomch2: {self.params_range[7]}\n")
        return self.params_range

