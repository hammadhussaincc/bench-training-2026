# Output

codingcops@codingcops-IdeaPad-3-15IAU7:~/Code/pre-training/day3$ python3 exercise1.py add "Get up and go to work!"
codingcops@codingcops-IdeaPad-3-15IAU7:~/Code/pre-training/day3$ python3 exercise1.py list
ID: 1, Title: Get up and go to work!, Status: todo, Created at: 2026-03-18 15:37:47
codingcops@codingcops-IdeaPad-3-15IAU7:~/Code/pre-training/day3$ python3 exercise1.py done 1
codingcops@codingcops-IdeaPad-3-15IAU7:~/Code/pre-training/day3$ python3 exercise1.py list
ID: 1, Title: Get up and go to work!, Status: done, Created at: 2026-03-18 15:37:47
codingcops@codingcops-IdeaPad-3-15IAU7:~/Code/pre-training/day3$

# Why I used a class instead of using functions?

I created two classes one for TaskTracker handling the operation and second for Task as I want to treat task as a seperate entity,
defining its attributes and everything. Using classes make the code more cleaner, readable, and understandablet to other and we can
treat all the different entities as different modules.
