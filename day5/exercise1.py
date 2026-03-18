import pandas as pd

dataset = pd.read_csv('titanic.csv')

# Question#1: How many passengers survived vs. didn't? Show as counts and percentages.
# Count the number of passengers who survived(1) and who didn't(0)
survival_counts = dataset['Survived'].value_counts()
survival_percentage = (survival_counts / len(dataset)) * 100

# Display results
print("Survival Counts:")
print(survival_counts)

print("\nSurvival Percentages:")
print(survival_percentage)


# Question#2: What was the survival rate by passenger class (1st, 2nd, 3rd)?
survival_by_class = dataset.groupby('Pclass')['Survived'].mean()

survival_percentage_by_class = survival_by_class * 100

# Display results
print("Survival Rate by Passenger Class:")
print(survival_percentage_by_class)


# Question#3: Average age of survivors vs. non-survivors.
average_age_by_survival = dataset.groupby('Survived')['Age'].mean()
# Display results
print("Average Age of Survivors vs Non-Survivors:")
print(average_age_by_survival)


# Question#4: Which embarkation port had the highest survival rate? Group by embarkation port and calculate the survival rate
survival_by_embarked = dataset.groupby('Embarked')['Survived'].mean() * 100

# Display results
print("Survival Rate by Embarkation Port:")
print(survival_by_embarked)

highest_port = survival_by_embarked.idxmax()
highest_rate = survival_by_embarked.max()

print(f"\nThe port with the highest survival rate is: {highest_port} ({highest_rate:.2f}%)")


# Question# 5: How many passengers have missing age values? Fill missing ages with the median age for that passenger class.
missing_ages_count = dataset['Age'].isnull().sum()
print(f"Number of passengers with missing Age values: {missing_ages_count}")

dataset['Age'] = dataset.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.median()))

missing_ages_count_after = dataset['Age'].isnull().sum()
print(f"Number of passengers with missing Age values after filling: {missing_ages_count_after}")


# Question# 6: Who was the oldest surviving passenger? Print their name, age, class
survivors = dataset[dataset['Survived'] == 1]

oldest_survivor = survivors.loc[survivors['Age'].idxmax()]

# Display  Results
print(f"Oldest surviving passenger: {oldest_survivor['Name']}")
print(f"Age: {oldest_survivor['Age']}")
print(f"Class: {oldest_survivor['Pclass']}")

# Question# 7: What % of women survived vs. what % of men?
women_survival_rate = dataset[dataset['Sex'] == 'female']['Survived'].mean() * 100
men_survival_rate = dataset[dataset['Sex'] == 'male']['Survived'].mean() * 100

# Display  results
print(f"Survival percentage for women: {women_survival_rate:.2f}%")
print(f"Survival percentage for men: {men_survival_rate:.2f}%")


# Question# 8: Create a new column 'AgeGroup': Child (<18), Adult (18-60), Senior (60+). Show survival rate per group
dataset['AgeGroup'] = dataset['Age'].apply(lambda x: 'Child' if x < 18 else 'Adult' if x <= 60 else 'Senior')
survival_rate_by_agegroup = dataset.groupby('AgeGroup')['Survived'].mean() * 100

# Display results
print(survival_rate_by_agegroup)


# Question# 9: Among 3rd class passengers, what was the survival rate for men vs. women?
third_class_passengers = dataset[dataset['Pclass'] == 3]
women_survival_rate_3rd = third_class_passengers[third_class_passengers['Sex'] == 'female']['Survived'].mean() * 100
men_survival_rate_3rd = third_class_passengers[third_class_passengers['Sex'] == 'male']['Survived'].mean() * 100

# Display results
print(f"Survival rate for women in 3rd class: {women_survival_rate_3rd:.2f}%")
print(f"Survival rate for men in 3rd class: {men_survival_rate_3rd:.2f}%")


# Question# 10: Drop all rows with missing Cabin data. How many rows remain? What % of original data did you keep?
original_rows = len(dataset)
dataset_cleaned = dataset.dropna(subset=['Cabin'])
remaining_rows = len(dataset_cleaned)
percentage_kept = (remaining_rows / original_rows) * 100

# Display results
print(f"Number of rows remaining: {remaining_rows}")
print(f"Percentage of original data kept: {percentage_kept:.2f}%")

