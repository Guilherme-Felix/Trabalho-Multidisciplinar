# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import scipy.io.wavfile
import numpy as np
import math

"""
UNIVERSIDADE FEDERAL DE JUIZ DE FORA
DEPARTAMENTO DE MECANICA APLICADA E COMPUTACIONAL
MAC020 - Trabalho Multidisciplinar

Script usado no trabalho 1 da disciplina no segundo semestre de 2017

Gisele Goulart    - gisele.goulart@engenharia.ufjf.br
Guilherme Felix   - guilherme.felix@engenharia.ufjf.br

RESUMO

Esse script recebe um arquivo no formato .wav, contendo a gravacao de uma 
unica nota emitida por um instrumento e, apos aplicar a transformada rapida
de fourier (fft) identifica qual a frequencia do harmonico fundamental. Com
essa informacao e possivel determinar qual a nota que esta sendo emitida.

A saida do script e o espectro de frequencia da amostra, no qual sao identi-
ficados o harmonico fundamental e qual a nota referente a essa frequencia, 
no sistema de 12 notas.

"""

# ============================================================================
plt.close('all')
path = './'
arq_nota = 'Nota1' #'A' 'Kurzweil-K2000-Dual-Bass-C1'
ext = '.wav'
f0 = 32.703194
notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


rate, data = wav.read(path+arq_nota+ext)
data = data[:,0]  # Quando Stereo


y = [abs(f) for f in data]
y = np.max(y)
data = [float((data[i])/y) for i in range(len(data))]

data = list(fft(data))

scipy.io.wavfile.write('teste_nota1.wav', rate, data2)

del data[0]
del data[len(data)/2]
data = [abs(np.real(f)) for f in data]
data = np.squeeze(data)
data = [data[i] for i in range(len(data)/2)]
f = np.linspace(0,rate/2,len(data))
y_max = max(data)
x_max = data.index(y_max)
fi = f[x_max]
print f[x_max]
i = int(round(math.log(fi/f0)/(math.log(2))*12))
print notas[i%12]
print len(f), len(data)

plt.title('Dominio da Frequencia '+str(notas[i%12])+' - '+ str(f[x_max]) )
#plt.xlim(0,6000)
plt.xlabel('$Frequencia(Hz)$')
plt.ylabel('$Intensidade(W/m^2)$')
plt.plot(f,data)
plt.show()
