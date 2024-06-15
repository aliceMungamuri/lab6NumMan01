'''
Author:Alice Mungamuri
Homework 2 Questions 1 and 2
''''
import numpy as np
import scipy
from scipy import signal
import matplotlib.pyplot as plt
# Question 1


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


# Question 2

def generate_unit_impulse(length, position):
  if position < 0 or position >= length:
        raise ValueError("Position must be within the range [0, length-1].")
    
    impSig = [0] * length
    impSig[position] = 1   
    return impulse_signal
    
def generate_sinusoidal(amplitude, frequency, time):
    sinSig = amplitude * np.sin(2 * np.pi * frequency * time)
    return sinSig

def generate_exponential(amplitude, decay_rate, time):
    expSig = amplitude * np.exp(-decay_rate * time)
    return expSig
