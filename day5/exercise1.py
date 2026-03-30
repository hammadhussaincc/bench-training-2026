import pandas as pd


class TitanicAnalyzer:
    def __init__(self, file_path):
        # Encapsulation: dataset is stored inside the object
        self.dataset = pd.read_csv(file_path)

    def question_1_survival_counts_and_percentages(self):
        survival_counts = self.dataset['Survived'].value_counts()
        survival_percentage = (survival_counts / len(self.dataset)) * 100

        print("Question 1: Survival Counts:")
        print(survival_counts)

        print("\nQuestion 1: Survival Percentages:")
        print(survival_percentage)
        print("-" * 50)

    def question_2_survival_rate_by_class(self):
        survival_by_class = self.dataset.groupby('Pclass')['Survived'].mean()
        survival_percentage_by_class = survival_by_class * 100

        print("Question 2: Survival Rate by Passenger Class:")
        print(survival_percentage_by_class)
        print("-" * 50)

    def question_3_average_age_by_survival(self):
        average_age_by_survival = self.dataset.groupby('Survived')['Age'].mean()

        print("Question 3: Average Age of Survivors vs Non-Survivors:")
        print(average_age_by_survival)
        print("-" * 50)

    def question_4_highest_survival_port(self):
        survival_by_embarked = self.dataset.groupby('Embarked')['Survived'].mean() * 100

        print("Question 4: Survival Rate by Embarkation Port:")
        print(survival_by_embarked)

        highest_port = survival_by_embarked.idxmax()
        highest_rate = survival_by_embarked.max()

        print(f"\nThe port with the highest survival rate is: {highest_port} ({highest_rate:.2f}%)")
        print("-" * 50)

    def question_5_fill_missing_ages(self):
        missing_ages_count = self.dataset['Age'].isnull().sum()
        print(f"Question 5: Number of passengers with missing Age values: {missing_ages_count}")

        self.dataset['Age'] = self.dataset.groupby('Pclass')['Age'].transform(
            lambda x: x.fillna(x.median())
        )

        missing_ages_count_after = self.dataset['Age'].isnull().sum()
        print(f"Number of passengers with missing Age values after filling: {missing_ages_count_after}")
        print("-" * 50)

    def question_6_oldest_surviving_passenger(self):
        survivors = self.dataset[self.dataset['Survived'] == 1]
        oldest_survivor = survivors.loc[survivors['Age'].idxmax()]

        print("Question 6: Oldest surviving passenger:")
        print(f"Name: {oldest_survivor['Name']}")
        print(f"Age: {oldest_survivor['Age']}")
        print(f"Class: {oldest_survivor['Pclass']}")
        print("-" * 50)

    def question_7_survival_rate_by_gender(self):
        women_survival_rate = self.dataset[self.dataset['Sex'] == 'female']['Survived'].mean() * 100
        men_survival_rate = self.dataset[self.dataset['Sex'] == 'male']['Survived'].mean() * 100

        print("Question 7:")
        print(f"Survival percentage for women: {women_survival_rate:.2f}%")
        print(f"Survival percentage for men: {men_survival_rate:.2f}%")
        print("-" * 50)

    def question_8_survival_rate_by_agegroup(self):
        self.dataset['AgeGroup'] = self.dataset['Age'].apply(
            lambda x: 'Child' if x < 18 else 'Adult' if x <= 60 else 'Senior'
        )
        survival_rate_by_agegroup = self.dataset.groupby('AgeGroup')['Survived'].mean() * 100

        print("Question 8: Survival rate per AgeGroup:")
        print(survival_rate_by_agegroup)
        print("-" * 50)

    def question_9_third_class_survival_by_gender(self):
        third_class_passengers = self.dataset[self.dataset['Pclass'] == 3]
        women_survival_rate_3rd = third_class_passengers[third_class_passengers['Sex'] == 'female']['Survived'].mean() * 100
        men_survival_rate_3rd = third_class_passengers[third_class_passengers['Sex'] == 'male']['Survived'].mean() * 100

        print("Question 9:")
        print(f"Survival rate for women in 3rd class: {women_survival_rate_3rd:.2f}%")
        print(f"Survival rate for men in 3rd class: {men_survival_rate_3rd:.2f}%")
        print("-" * 50)

    def question_10_drop_missing_cabin(self):
        original_rows = len(self.dataset)
        dataset_cleaned = self.dataset.dropna(subset=['Cabin'])
        remaining_rows = len(dataset_cleaned)
        percentage_kept = (remaining_rows / original_rows) * 100

        print("Question 10:")
        print(f"Number of rows remaining: {remaining_rows}")
        print(f"Percentage of original data kept: {percentage_kept:.2f}%")
        print("-" * 50)

    def run_all_analysis(self):
        # Abstraction: user only calls one method, internal details stay hidden
        self.question_1_survival_counts_and_percentages()
        self.question_2_survival_rate_by_class()
        self.question_3_average_age_by_survival()
        self.question_4_highest_survival_port()
        self.question_5_fill_missing_ages()
        self.question_6_oldest_surviving_passenger()
        self.question_7_survival_rate_by_gender()
        self.question_8_survival_rate_by_agegroup()
        self.question_9_third_class_survival_by_gender()
        self.question_10_drop_missing_cabin()


# Create object and run analysis
analyzer = TitanicAnalyzer('titanic.csv')
analyzer.run_all_analysis()