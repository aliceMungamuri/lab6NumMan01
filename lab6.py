'''
Author:Alice Mungamuri
Homework 2 Questions 1,2,3
''''
import numpy as np
import scipy
from scipy import signal
import matplotlib.pyplot as plt


time = np.linspace(0, 1, 1000)
amplitude = 1
frequency = 100


def watts_to_dbw(watts):
    # write your code to here
   dbw = 10 * math.log10(watts)
    return dbw

def watts_to_dbm(watts):
   dbm = 10 * math.log10(1000 * watts)
    return dbm

def dbw_to_watts(dbw):
    # write your code to here
  watts = 10 ** (dbw / 10)
    return watts

def dbm_to_mW(dbm):
  mW = 10 ** (dbm / 10)
   return mW


# Question 2 Part 1



def generate_unit_impulse(length, position):
  if position < 0 or position >= length:
        raise ValueError("Position must be within the range [0, length-1].")
    
    impSig = [0] * length
    impSig[position] = 1   
    return impulse_signal
    
def generate_sinusoidal(amplitude, frequency, time):
    sinSig = amplitude * np.sin(2 * np.pi * frequency * time)
    return sinSig


time = np.linspace(0, 1, 1000)# for Question3
amplitude = 1
frequency = 100

def generate_exponential(amplitude, decay_rate, time):
    expSig = amplitude * np.exp(-decay_rate * time)
    return expSig


# Question2 Part 2




def plot_signals(signals, titles):
    numSig = len(signals)
    numCol = min(numSig, 3)  
    
    fig, axes = plt.subplots(nrows=(numSig + numCol - 1) // numCol, ncols=numCol, figsize=(15, 4*numCOl))
    axes = axes.flatten()
    
    for i in range(numSig):
        axes[i].plot(signals[i])
        axes[i].set_title(titles[i])
        axes[i].grid(True)
    
    for j in range(numSIg, len(axes)):
        axes[j].axis('off')
    
    plt.tight_layout()
    plt.show()

# QUESTION 3

plt.figure(figsize=(10, 4))
plt.plot(time, sin_signal, label=f'Sinusoidal Signal: {amplitude} * sin(2π * {frequency} * t)')
plt.title('Sinusoidal Signal with Frequency 100 Hz')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

def add_noise(signal, noiseLev):
   
    noise = np.random.normal(loc=0, scale=noiseLev, size=len(signal))

    noisySig = signal + noise
    
    return noisySig
