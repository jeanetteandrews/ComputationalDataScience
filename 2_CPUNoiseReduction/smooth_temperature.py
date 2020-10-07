import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
from pykalman import KalmanFilter

filename1 = "sysinfo.csv"

cpu_data = pd.read_csv(filename1, parse_dates=['timestamp'])


kalman_data = cpu_data[['temperature', 'cpu_percent', 'sys_load_1', 'fan_rpm']]

initial_state = kalman_data.iloc[0]
observation_covariance = np.diag([3.306, 7.011, 0.807, 68.949]) ** 2
# The numbers above are the standard deviations of each column
transition_covariance = np.diag([0.08, 0.18, 0.02, 1.72]) ** 2 
transition = [[.97,.5,0.2,-0.001], [.01,0.4,2.2,0], [0,0,.95,0], [0,0,0,1]]


kf = KalmanFilter(
    initial_state_mean=initial_state,
    observation_covariance=observation_covariance,
    transition_covariance=transition_covariance,
    transition_matrices=transition
)

loess_smoothed = lowess(cpu_data['temperature'], cpu_data['timestamp'], frac=.01)
kalman_smoothed, _ = kf.smooth(kalman_data)

plt.figure(figsize=(12, 4))
plt.plot(cpu_data['timestamp'], cpu_data['temperature'], 'b.', alpha=0.5)
plt.plot(cpu_data['timestamp'], loess_smoothed[:, 1], 'r-')
plt.plot(cpu_data['timestamp'], kalman_smoothed[:, 0], 'g-')
plt.legend(['Temperature', 'LOESS Smoothing', 'Kalman Smoothing'])
plt.savefig('cpu.png') 
