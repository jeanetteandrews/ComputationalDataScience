import pandas as pd
from scipy import stats

OUTPUT_TEMPLATE = (
    '"Did more/less users use the search feature?" p-value: {more_users_p:.3g}\n'
    '"Did users search more/less?" p-value: {more_searches_p:.3g}\n'
    '"Did more/less instructors use the search feature?" p-value: {more_instr_p:.3g}\n'
    '"Did instructors search more/less?" p-value: {more_instr_searches_p:.3g}'
)


def main():
    #searchdata_file = sys.argv[1]
    searchdata_file = 'searches.json'
    
    df = pd.read_json(searchdata_file, orient='records', lines=True)

    searched_even = df.loc[(df['uid'] % 2 == 0) & (df['search_count'] > 0),'search_count'].count()
    nosearched_even = df.loc[(df['uid'] % 2 == 0) & (df['search_count'] < 1),'search_count'].count()
    searched_odd = df.loc[(df['uid'] % 2 != 0) & (df['search_count'] > 0),'search_count'].count()
    nosearched_odd = df.loc[(df['uid'] % 2 != 0) & (df['search_count'] < 1),'search_count'].count()

    contingency = [[searched_even,nosearched_even],[searched_odd,nosearched_odd]]
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    
    za = df[df['uid'] % 2 == 0]
    zb = df[df['uid'] % 2 != 0]
    
    
    isearched_even = df.loc[df['is_instructor'] & (df['uid'] % 2 == 0) & (df['search_count'] > 0),'search_count'].count()
    inosearched_even = df.loc[df['is_instructor'] & (df['uid'] % 2 == 0) & (df['search_count'] < 1),'search_count'].count()
    isearched_odd = df.loc[df['is_instructor'] & (df['uid'] % 2 != 0) & (df['search_count'] > 0),'search_count'].count()
    inosearched_odd = df.loc[df['is_instructor'] & (df['uid'] % 2 != 0) & (df['search_count'] < 1),'search_count'].count()
    
    icontingency = [[isearched_even,inosearched_even],[isearched_odd,inosearched_odd]]
    ichi2, ip, idof, iexpected = stats.chi2_contingency(icontingency)
    
    zai = df[(df['uid'] % 2 == 0) & df['is_instructor']]   
    zbi = df[(df['uid'] % 2 != 0) & df['is_instructor']]

    # Output
    print(OUTPUT_TEMPLATE.format(
        more_users_p=p,
        more_searches_p=stats.mannwhitneyu(za['search_count'], zb['search_count']).pvalue*2,
        more_instr_p=ip,
        more_instr_searches_p=stats.mannwhitneyu(zai['search_count'], zbi['search_count']).pvalue*2,
    ))


if __name__ == '__main__':
    main()