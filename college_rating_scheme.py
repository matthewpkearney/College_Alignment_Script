# Matthew Kearney
# College Alignment Script

# Made originally with Swift around March 2021 and remade in Python on August 8, 2023

# 'get_match_score(college)' : returns the percent match of a specific 'college' to your interests
# Class(College) -> int*float + ... + int*float -> float
def get_match_score(college):
    match = sum(college.attributes[attr] * weights[attr] for attr in weights)
    return match

# 'College' assigns the college name to the attributes specified for it
class College:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes


# 1. Create your personalized criteria
# Make variables representing the attributes you want to rate among colleges
loc  ="Location"            # warm climate, high population density, etc
cost ="Cost of Attendance"  # coa, roi, and other metrics
progs="Programs Alignment"  # stem schools/programs
car  ="Career Support"      # career development , internships
size ="Size"                # a size that promotes community (4000-10000 students)
# Add more...



# 2. Weigh your attributes in their influence in your decision
# You should also input the amount of weight each criteria holds in your decision
weights={
    loc:   0.25,
    cost:  0.25,
    progs: 0.2,
    car:   0.2,
    size:  0.1}


# 3. Create the object for each college where you rank each college based on all criteria
stevens    =  College("Stevens Institute of Technology",    {loc: 10,   cost: 6,    progs: 9,   car: 8, size:8})
wentworth  =  College("Wentworth Institute of Technology",  {loc: 10,   cost: 8,    progs: 10,  car: 9, size:6})
unh        =  College("University of New Hampshire",        {loc: 5,    cost:5,     progs: 9,   car: 8, size:7})
olin       =  College("Olin College of Engineering",        {loc: 8,    cost: 10,   progs: 9,   car: 9, size:4})
ucsd       =  College("University of California, San Diego",{loc: 9,    cost:8,     progs: 9,   car: 7, size:4})
asu        =  College("Arizona State University",           {loc: 9,    cost:7,     progs: 9,   car: 7, size:3})


# 4. Make a list/lists which you can use to reveal the top match colleges
# The 'colleges' list below holds all of the colleges you would like to assess the level of match

colleges=[
    stevens,
    wentworth,
    olin,
    ucsd,
    asu,
    unh
]

# you can also organize colleges by specific areas, institution types, climates, etc 

colleges_near_home =[
    wentworth,
    olin,
    unh
]

schools_public =[
    unh,
    asu,
    ucsd
]

warm_schools=[
    asu,
    ucsd
]


# Create an attriubute 'match' paired with the function evaluation of 'get_match_score'

# We are asking for the ranking between all 7 colleges I've inputted, as I loop through the 'colleges' list
#To change the list we want to rank, change 'colleges' on lines 85 and 90 to the name of the list you want to rank
for college in colleges:
    college.match = get_match_score(college)


# next, sort the colleges based on the highest to the lowest match score
sorted_colleges = sorted(colleges, key=lambda college: college.match, reverse=True)

# Print the ranked colleges
print("College Rankings based on match score:")
for rank, college in enumerate(sorted_colleges, start=1):
    print(f"{rank}. {college.name}: Match Score = {college.match:.2f}")

# Check README for more.