import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()

    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df.loc[df['education'] == 'Bachelors'].count()[0] / df.count()[0]) * 100

    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # percentage with salary >50K

    higher_educations = ['Bachelors', 'Masters', 'Doctorate']

    higher_educations = ['Bachelors', 'Masters', 'Doctorate']

    higher_education = df[df.education.isin(higher_educations)]

    higher_education_count = df[df.education.isin(higher_educations)].count()[0]

    higher_education_rich_count = higher_education[higher_education['salary'] == '>50K'].count()[0]

    higher_education_rich = higher_education_rich_count / higher_education_count * 100

    higher_education_rich = round(higher_education_rich, 1)

    lower_education = df[~df.education.isin(higher_educations)]

    lower_education_count = df[~df.education.isin(higher_educations)].count()[0]

    lower_education_rich_count = lower_education[lower_education['salary'] == '>50K'].count()[0]

    lower_education_rich = lower_education_rich_count / lower_education_count * 100

    lower_education_rich = round(lower_education_rich, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    min_work_hours = round(min_work_hours, 1)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]

    num_min_workers = df[df['hours-per-week'] == min_work_hours].count()[0]

    num_min_workers_rich = min_workers[min_workers['salary'] == '>50K'].count()[0]

    rich_percentage = num_min_workers_rich / num_min_workers * 100

    rich_percentage = round(rich_percentage, 1)

    # What country has the highest percentage of people that earn >50K?
    
    earnings = df.groupby(['native-country', 'salary'], as_index=True)['age'].count().reset_index(name='counts')

    earnings['%'] = 100 * earnings['counts'] / earnings.groupby('native-country')['counts'].transform('sum')

    salary_rich = earnings[earnings['salary'] == '>50K']

    highest_earning_country = salary_rich['native-country'][salary_rich['%'] == salary_rich['%'].max()]

    highest_earning_country = highest_earning_country.tolist()

    highest_earning_country = highest_earning_country[0]
    
    highest_earning_country_percentage = salary_rich['%'].max()

    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    india_rich_jobs = india_rich.groupby(['occupation'])['age'].count().reset_index(name='count')

    top_IN_occupation = india_rich_jobs['occupation'][india_rich_jobs['count'] == india_rich_jobs['count'].max()]

    top_IN_occupation = top_IN_occupation.tolist()

    top_IN_occupation = top_IN_occupation[0]

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
