from quickbbee import set_dparams
from quickbbee import set_cparams
import matplotlib.pyplot as plt
import math as m
import numpy as np


#Testing Set_dparams
H0, Alens, r, tau, ns, As, ombh2, omch2 = 68, 0.2, 0.02, 0.035, 0.97, m.exp(3.3)*10**-10, 0.020, 0.05
model = set_dparams(H0, Alens, r, tau, ns, As, ombh2, omch2, 2400)
interval = model.get_params_interval()
BB_EE = model.get_spectra()
ell_range = len(BB_EE[0])




#Testing Set_cparams
ranges = np.array([[65, 75],
                           [0, 1],
                           [0, 0.5],
                           [0.03, 0.09],
                           [0.94, 0.99],
                           [m.exp(3.0)*10**-10, m.exp(3.5)*10**-10],
                           [0.02, 0.025],
                           [0.05, 0.3]
                           ])



modelc = set_cparams(H0, Alens, r, tau, ns, As, ombh2, omch2, '../EE_BB__models/cp_NN_BB', ranges, True ,False,2400)
intervalc = modelc.get_params_interval()
BB_c = modelc.get_spectra()
ell_rangec = len(BB_c[0])

modelc = set_cparams(H0, Alens, r, tau, ns, As, ombh2, omch2, '../EE_BB__models/cp_NN_EE', ranges, False ,True,2400)
intervalc = modelc.get_params_interval()
EE_c = modelc.get_spectra()
ell_rangec = len(EE_c[0])




#Plot the spectras obtained using set_dparams
x = [i for i in range(ell_range)]
BB_spectre = BB_EE[0]
EE_spectre = BB_EE[1]

# First figure: Spectra BB
plt.figure(figsize=(8, 6))  
plt.plot(x, BB_spectre, label='Spectra BB', color='blue')  
plt.title('Spectra BB as a function of the index $\\ell$ using set_dparams')  
plt.xlabel('Index $\\ell$')  
plt.ylabel('Amplitude')  
plt.legend()  
plt.grid(True)  
plt.show()

# Second figure: Spectra EE
plt.figure(figsize=(8, 6))  
plt.plot(x, EE_spectre, label='Spectra EE', color='red')  
plt.title('Spectra EE as a function of the index $\\ell$ using set_dparams')  
plt.xlabel('Index $\\ell$')  
plt.ylabel('Amplitude')  
plt.legend()  
plt.grid(True)  
plt.show()



#Plot the spectras obtained using set_cparams
x = [i for i in range(ell_rangec)]
BB_spectrec = BB_c[0]
EE_spectrec = EE_c[0]

# First figure: Spectra BB
plt.figure(figsize=(8, 6))  
plt.plot(x, BB_spectrec, label='Spectra BB', color='blue')  
plt.title('Spectra BB as a function of the index $\\ell$ using set_cparams')  
plt.xlabel('Index $\\ell$')  
plt.ylabel('Amplitude')  
plt.legend()  
plt.grid(True)  
plt.show()


# First figure: Spectra BB
plt.figure(figsize=(8, 6))  
plt.plot(x, EE_spectrec, label='Spectra EE', color='red')  
plt.title('Spectra EE as a function of the index $\\ell$ using set_cparams')  
plt.xlabel('Index $\\ell$')  
plt.ylabel('Amplitude')  
plt.legend()  
plt.grid(True)  
plt.show()