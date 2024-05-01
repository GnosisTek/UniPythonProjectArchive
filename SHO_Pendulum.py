# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, no-member, C0301, C0411, W0511, W0613

''' 

Comparing the amplitude and period of a pendulum

'''

import numpy as np
from scipy import interpolate
from scipy import integrate
import matplotlib.pyplot as plt


class pendulum:
    ''' defines a simple pendulum '''

    def __init__(self, pendulum_length, mass):
        self._length = pendulum_length
        self._mass = mass


    def set_g(self, g):
        ''' small g to be used in calculations '''
        self._g = g


    def dydt(self, y, t):
        """ Calculating the derivatives for a pendulum

        Parameters
        ----------
        y: array-like
            vector of unknowns for the ode equation at time t

        t: float
            time t

        Returns
        -------
        ret: numpy array of float
            the derivatives of y
        """
        
        # y[0] : (angular acceleration), y[1] : (angular velocity)
        return np.array([y[1], -(self._g/self._length)*np.sin(y[0])])
        


    def period(self, maximum_amplitude):
        ''' Calculating the period of the periodic motion.

        For amplitude=0 the small amplitude analytical solution is returned.
        Otherwise the period is calculated by integrating the ODE using
        scipy.integrate.odeint() and determining the time between release at
        maximum amplitude and the first angle=0 crossing. The exact zero
        crossing is determined using scipy.interpolate.interp1d().

        In the calculation it is assumed that the period has a value between
        90% and 150% of the small amplitude period.

        Parameters
        ----------
        maximum_amplitude: float
            maximum amplitude of the periodic motion

        Returns
        -------
        p: float
            the period
        '''
        
        # small amplitude analytical solution
        period_0 = 2*np.pi*np.sqrt(self._length/self._g)
        # check for small amplitude
        if maximum_amplitude == 0:
            period = period_0
        else:
            t = np.linspace(0, 1.5*period_0/4, 75)
            solution = integrate.odeint(self.dydt, [maximum_amplitude, 0], t)
            func = interpolate.interp1d(solution[:, 0], t, kind='cubic')
            # period is 4x the time from maximum amplitude to 0
            period = func(0) * 4
        return period
        

if __name__ == '__main__':
    #some test code
    pen = pendulum(1, 1)
    pen.set_g(9.81)

    #generate data for figure
    angles = np.linspace(0, np.pi/2, 31)
    period_ode = [pen.period(a) for a in angles]

    # generate a plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(angles, period_ode, 'b', label='generated using ode')
    ax.set_title('Period of a 1m Pendulum as a Function of Amplitude')
    ax.set_xlabel('amplitude/rad')
    ax.set_ylabel('period/s')
    ax.legend(loc='upper left')
    plt.show()
    