# Computational Data Science Assignments

### Repository in progress! 

Snippets of assignments for Computational Data Science (CMPT 353) at Simon Fraser University.

### Table of Contents
1. [Pup Inflation: Analyzing Tweets](https://github.com/jeanetteandrews/ComputationalDataScience#1-pup-inflation-analyzing-tweets)
2. [CPU Noise Reduction: LOESS & Kalman Smoothing](https://github.com/jeanetteandrews/ComputationalDataScience#2-cpu-noise-reduction-loess--kalman-smoothing)
3. [GPS Tracks: How Far Did I Walk?](https://github.com/jeanetteandrews/ComputationalDataScience#3-gps-tracks-how-far-did-i-walk)
4. [Movie Title Entity Resolution](https://github.com/jeanetteandrews/ComputationalDataScience#4-movie-title-entity-resolution)
5. [Cities: Temperatures and Density](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/README.md#5-cities-temperatures-and-density)
6. [Reddit Weekends](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/README.md#6-reddit-weekends)

### Libraries used:
* pandas
* numpy 
* matplotlib.pyplot
* scipy
* seaborn
* statsmodels.nonparametric.smoothers_lowess
* pykalman
* xml.etree.ElementTree 
* difflib

## Assignments

### 1. [Pup Inflation](https://github.com/jeanetteandrews/ComputationalDataScience/tree/master/1_PupInflation): Analyzing Tweets

Has there been grade inflation on the [@dog_rates](https://twitter.com/dog_rates) Twitter, which rates the cuteness of users' dog pictures?

Code: [dog-rates.ipynb](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/1_PupInflation/dog-rates.ipynb) – Notebook that uses simple linear regression to demonstrate increasing grade inflation on a plot. <br />
Input: [dog_rates_tweets.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/1_PupInflation/dog_rates_tweets.csv) – CSV of scraped Tweets from the [@dog_rates](https://twitter.com/dog_rates) Twitter.

### 2. [CPU Noise Reduction](https://github.com/jeanetteandrews/ComputationalDataScience/tree/master/2_CPUNoiseReduction): LOESS & Kalman Smoothing

[sysinfo.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/2_CPUNoiseReduction/sysinfo.csv) contains samples of CPU temperature (in °C), CPU usage (in percent), and one-minute system load (number of processes running/waiting averaged over the last minute). You will see that there's a certain amount of noise from the temperature sensor, but it also seems like there are some legitimate changes in the true temperature.

We want to adjust the parameters of the LOESS and Kalman filters to get as much signal with as little noise as possible. The contrasting factors: (1) when the temperature spikes (because of momentary CPU usage), the high temperature values are reality and we don't want to smooth that information out of existence, but (2) when the temperature is relatively steady (where the computer is not in use), not jumping randomly between 30°C and 33°C as the data implies.

Code: [smooth_temperature.py](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/2_CPUNoiseReduction/smooth_temperature.py) <br />
Input: [sysinfo.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/2_CPUNoiseReduction/sysinfo.csv) <br />
Output: [cpu.png](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/2_CPUNoiseReduction/cpu.png) (the image below)

<p align="center">
<img src="https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/2_CPUNoiseReduction/cpu.png" width="500"/>
</p>

It looks like the Kalman filter picks up smaller variations in the data, whereas the LOESS smoothing removes smaller variations that actually might've existed.

### 3. [GPS Tracks](https://github.com/jeanetteandrews/ComputationalDataScience/tree/master/3_GPSTracks): How Far Did I Walk?

[walk1.gpx](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/3_GPSTracks/walk1.gpx) includes a recorded path from walking around downtown Vancouver.

How far did I walk? The answer to this can't be immediately calculated from the tracks, since the noise makes it look like I ran across the street, crossed back, backed up, and jumped forward. I actually walked in mostly-straight lines. On the other hand, we can't just take the difference between the starting and ending points; I didn't walk a completely straight line either.

Code: [calc_distance.py](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/3_GPSTracks/calc_distance.py) <br />
Input: [walk1.gpx](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/3_GPSTracks/walk1.gpx) <br />
Output: [out.gpx](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/3_GPSTracks/out.gpx) (converted using [MyGPSFiles](http://www.mygpsfiles.com/app/))

<p align="center">
<img src="https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/3_GPSTracks/MyGPSFiles.png" width="400"/>
</p>

Unfiltered distance: 3186.44 meters <br />
Filtered distance: 1407.33 meters

### 4. [Movie Title Entity Resolution](https://github.com/jeanetteandrews/ComputationalDataScience/tree/master/4_MovieTitleEntityResolution)

[movie_list.txt](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/4_MovieTitleEntityResolution/movie_list.txt) is a list of movie titles.

[movie_ratings.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/4_MovieTitleEntityResolution/movie_ratings.csv)  contains users' rating of movies: titles and ratings. Except... the users have misspelled the titles. There are also some completely incorrect titles that have nothing to do with the movie list that should be ignored.

Using [Python difflib.get_close_matches](https://docs.python.org/3/library/difflib.html#difflib.get_close_matches), we want to determine the average rating for each movie, compensating for the bad spelling in the [movie_ratings.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/4_MovieTitleEntityResolution/movie_ratings.csv) file.

Code: [average_ratings.py](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/4_MovieTitleEntityResolution/average_ratings.py) <br />
Input: [movie_list.txt](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/4_MovieTitleEntityResolution/movie_list.txt) and [movie_ratings.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/4_MovieTitleEntityResolution/movie_ratings.csv) <br />
Output: [output.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/4_MovieTitleEntityResolution/output.csv)

### 5. [Cities](https://github.com/jeanetteandrews/ComputationalDataScience/tree/master/5_CitiesTempAndDensity): Temperatures and Density

Is there any correlation between population density and temperature? It's an artificial question, but one we can answer.

We have [stations.json.gz](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/5_CitiesTempAndDensity/stations.json.gz), a collection of weather stations, and [city_data.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/5_CitiesTempAndDensity/city_data.csv) a collection of cities.

Both data sets contain a latitude and longitude, but they don't refer to exactly the same locations. A city's “location” is some point near the center of the city. That is very unlikely to be the exact location of a weather station, but there is probably one nearby.

We'll need to find the weather station that is closest to each city. This takes an O(mn) kind of calculation–the distance between every city and station pair must be calculated. 

Code: [temperature_correlation.py](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/5_CitiesTempAndDensity/temperature_correlation.py) <br />
Input: [stations.json.gz](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/5_CitiesTempAndDensity/stations.json.gz) and [city_data.csv](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/5_CitiesTempAndDensity/city_data.csv) <br />
Output: [output.png](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/5_CitiesTempAndDensity/output.png)

For the record, daily temperatures is not a good way to predict population density.

### 6. [Reddit Weekends](https://github.com/jeanetteandrews/ComputationalDataScience/tree/master/6_RedditWeekends)

Are there a different number of Reddit comments posted on weekdays than on weekends in [/r/canada](https://www.reddit.com/r/canada/)? To answer this, there few things we can do with our data:

1. Transform the data. A histogram of the data shows us it's skewed. In order to make it normally distributed, we'll square root the data, which so far, gets us closest to satisfying the assumptions of a T-test.

2. Use the Central Limit Theorem. The Central Limit Theorem says that if our numbers are large enough, and we look at sample means, the result should be normal. We will combine all weekdays and weekend days from each year/week pair and take the mean of their (non-transformed) counts. Now we can apply a T-test. We should note that we're subtly changing the question here to: do the number of comments on weekends and weekdays for each week differ?

3. Use a non-parametric test. The [Mann–Whitney U-test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test) doesn't care about the shape of its input as much–it does not assume normally-distributed values, or equal variance. We'll perform a U-test on the original non-transformed, non-aggregated counts. If we reach a conclusion because of a U-test, it's something like: it's not equally-likely that the larger number of comments occur on weekends vs weekdays.

Code: [reddit_weekends.py](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/6_RedditWeekends/reddit_weekends.py) <br />
Input: [reddit-counts.json.gz](https://github.com/jeanetteandrews/ComputationalDataScience/blob/master/6_RedditWeekends/reddit-counts.json.gz) – Contains a count of the number of comments posted daily in each Canadian-province subreddit, and in [/r/canada](https://www.reddit.com/r/canada/).

Based on all our tests, yes, there are a different number of comments posted on weekdays than on weekends. More Reddit comments in [/r/canada](https://www.reddit.com/r/canada/) are posted, on average, during weekdays. The Central Limit Theorem probably got us the closest to the normality of the distributions. We could say that the t-test on this distribution gives us a more confident answer.

