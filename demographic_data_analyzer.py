import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    MASKs = df['sex'] == 'Male'

    average_age_men = round(df[MASKs]['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    maa = df['education'] == 'Bachelors'
    mask = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    
    percentage_bachelors = round(((df[maa].size / df.size) * 100), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?


    # with and without `Bachelors`, `Masters`, or `Doctorate`
    mask1 = (df['salary'] == '>50K') & ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) 
    higher_education = round((df[mask].size / df.size) * 100, 1)
    mask2 = (df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')
    mask3 = (df['salary'] == '>50K') & ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'))
    lower_education = round((df[mask2].size / df.size) * 100, 1)

    # percentage with salary >50K
    higher_education_rich = round((df[mask1].size / df[mask].size) * 100, 1)
    lower_education_rich = round((df[mask3].size / df[mask2].size) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask4 = df['hours-per-week'] == min_work_hours
    mask5 = (df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')

    num_min_workers = df[mask4].size

    rich_percentage = round((df[mask5].size / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    high_earning_country = df[df['salary'] == '>50K']
    country_count = high_earning_country['native-country'].value_counts()
    country_count_general = df['native-country'].value_counts()
    rich = (country_count/country_count_general) * 100

    highest_earning_country = rich.idxmax()
    

    highest_earning_country_percentage = round(rich.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    Mask = (df['native-country'] == 'India') & (df['salary'] == '>50K')
    occupation = df[Mask]['occupation'].value_counts()

    top_IN_occupation = occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
