# excise_2.py

def grade_classifier(score):
    if score >= 90:
        return "Distinction"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"

test_scores = [55, 60, 75, 90, 30]

for score in test_scores:
    print(f"Score: {score} -> {grade_classifier(score)}")

scores = [45, 72, 91, 60, 38, 85]

for score in scores:
    print(f"Score: {score} -> {grade_classifier(score)}")