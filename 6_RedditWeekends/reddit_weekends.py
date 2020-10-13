import pandas as pd
import numpy as np
from scipy import stats

OUTPUT_TEMPLATE = (
    "Initial (invalid) T-test p-value: {initial_ttest_p:.3g}\n"
    "Original data normality p-values: {initial_weekday_normality_p:.3g} {initial_weekend_normality_p:.3g}\n"
    "Original data equal-variance p-value: {initial_levene_p:.3g}\n"
    "Transformed data normality p-values: {transformed_weekday_normality_p:.3g} {transformed_weekend_normality_p:.3g}\n"
    "Transformed data equal-variance p-value: {transformed_levene_p:.3g}\n"
    "Weekly data normality p-values: {weekly_weekday_normality_p:.3g} {weekly_weekend_normality_p:.3g}\n"
    "Weekly data equal-variance p-value: {weekly_levene_p:.3g}\n"
    "Weekly T-test p-value: {weekly_ttest_p:.3g}\n"
    "Mann–Whitney U-test p-value: {utest_p:.3g}"
)


def main():
    reddit_counts = 'reddit-counts.json.gz'

    counts = pd.read_json(reddit_counts, lines=True)
    
    counts['iso_year'] = counts['date'].apply(lambda x: int(x.isocalendar()[0]))
    counts['iso_week'] = counts['date'].apply(lambda x: int(x.isocalendar()[1]))

    counts = counts[counts['iso_year'] < 2014]
    counts = counts[counts['iso_year'] > 2011]
    counts['day_of_week']= counts['date'].apply(lambda x: int(x.weekday()))
    counts = counts[counts['subreddit']=='canada']
    
    weekday=counts[counts['day_of_week']<5]
    weekend=counts[counts['day_of_week']>4]
    
    x1 = weekday['comment_count']
    x2 = weekend['comment_count']
    
    #plt.hist(x1,density=True, bins=50)
    #plt.hist(x2,density=True, bins=50)
     
    x1_sqrt = np.sqrt(x1)
    x2_sqrt = np.sqrt(x2)
    
    x1_weekly = weekday.groupby(["iso_year", "iso_week"])["comment_count"].sum()
    x2_weekly = weekend.groupby(["iso_year", "iso_week"])["comment_count"].sum()
    

    print(OUTPUT_TEMPLATE.format(
        initial_ttest_p=stats.ttest_ind(x1, x2).pvalue,
        initial_weekday_normality_p=stats.normaltest(x1).pvalue,
        initial_weekend_normality_p=stats.normaltest(x2).pvalue,
        initial_levene_p=stats.levene(x1, x2).pvalue,
        transformed_weekday_normality_p=stats.normaltest(x1_sqrt).pvalue,
        transformed_weekend_normality_p=stats.normaltest(x2_sqrt).pvalue,
        transformed_levene_p=stats.levene(x1_sqrt, x2_sqrt).pvalue,
        weekly_weekday_normality_p=stats.normaltest(x1_weekly).pvalue,
        weekly_weekend_normality_p=stats.normaltest(x2_weekly).pvalue,
        weekly_levene_p=stats.levene(x1_weekly, x2_weekly).pvalue,
        weekly_ttest_p=stats.ttest_ind(x1_weekly, x2_weekly).pvalue,
        utest_p=stats.mannwhitneyu(x1, x2).pvalue,
    ))


if __name__ == '__main__':
    main()