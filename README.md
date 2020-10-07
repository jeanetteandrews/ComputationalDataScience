# Computational Data Science Assignments

### Repository in progress! 

Snippets of assignments for Computational Data Science (CMPT 353) at Simon Fraser University.

### Table of Contents
1. [Pup Inflation: Analyzing Tweets](https://github.com/jeanetteandrews/ComputationalDataScience#1-pup-inflation-analyzing-tweets)
2. [CPU Noise Reduction: LOESS & Kalman Smoothing](https://github.com/jeanetteandrews/ComputationalDataScience#2-cpu-noise-reduction-loess--kalman-smoothing)
3. [GPS Tracks: How Far Did I Walk?](https://github.com/jeanetteandrews/ComputationalDataScience#3-gps-tracks-how-far-did-i-walk)

### Libraries used:
* pandas
* numpy 
* matplotlib.pyplot
* scipy
* seaborn
* statsmodels.nonparametric.smoothers_lowess
* pykalman
* xml.etree.ElementTree 

## Assignments

### 1. [Pup Inflation](https://github.com/jeanetteandrews/ComputationalDataScience/tree/master/1_PupInflation): Analyzing Tweets

Has there been grade inflation on the [@dog_rates](https://twitter.com/dog_rates) Twitter, which rates the cuteness of users' dog pictures?

Code: [dog-rates.ipynb](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/1_PupInflation/dog-rates.ipynb) – Notebook that uses simple linear regression to demonstrate increasing grade inflation on a plot. <br />
Input: [dog_rates_tweets.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/1_PupInflation/dog_rates_tweets.csv) – CSV of scraped Tweets from the [@dog_rates](https://twitter.com/dog_rates) Twitter.

### 2. [CPU Noise Reduction](https://github.com/jeanetteandrews/ComputationalDataScience/tree/master/2_CPUNoiseReduction): LOESS & Kalman Smoothing

[sysinfo.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/2_CPUNoiseReduction/sysinfo.csv) contains samples my prof's CPU temperature, including temperature (in °C), CPU usage (in percent), and one-minute system load (number of processes running/waiting averaged over the last minute). You will see that there's a certain amount of noise from the temperature sensor, but it also seems like there are some legitimate changes in the true temperature.

We want to adjust the parameters of the LOESS and Kalman filters to get as much signal as possible with as little noise as possible. The contrasting factors: (1) when the temperature spikes (because of momentary CPU usage), the high temperature values are reality and we don't want to smooth that information out of existence, but (2) when the temperature is relatively steady (where the computer is not in use), not jumping randomly between 30°C and 33°C as the data implies.

Code: [smooth_temperature.py](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/2_CPUNoiseReduction/smooth_temperature.py) <br />
Input: [sysinfo.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/2_CPUNoiseReduction/sysinfo.csv) <br />
Output: [cpu.png](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/2_CPUNoiseReduction/cpu.png) (the image below)

<img src="https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/2_CPUNoiseReduction/cpu.png" width="500"/>

It looks like the Kalman filter picks up smaller variations in the data, whereas the LOESS smoothing removes smaller variations that actually might've existed.

### 3. [GPS Tracks](https://github.com/jeanetteandrews/ComputationalDataScience/tree/master/3_GPSTracks): How Far Did I Walk?

[walk1.gpx](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/3_GPSTracks/walk1.gpx) includes a recorded path from walking around downtown Vancouver.

How far did I walk? The answer to this can't be immediately calculated from the tracks, since the noise makes it look like I ran across the street, crossed back, backed up, jumped forward, etc. I actually walked in mostly-straight lines. On the other hand, we can't just take the difference between the starting and ending points: I didn't walk a completely straight line either.

Code: [calc_distance.py](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/3_GPSTracks/calc_distance.py) <br />
Input: [walk1.gpx](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/3_GPSTracks/walk1.gpx) <br />
Output: [out.gpx](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/3_GPSTracks/out.gpx) (converted using [MyGPSFiles](http://www.mygpsfiles.com/app/))

<img src="https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/3_GPSTracks/MyGPSFiles.png" width="500"/>

Unfiltered distance: 3186.44 meters <br />
Filtered distance: 1407.33 meters

### 4. Movie Title Entity Resolution

### 5. Cities: Temperatures and Density
