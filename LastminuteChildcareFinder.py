import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Sample dataset of babysitters (replace this with actual data from care.com)
data = {
    'name': ['Alice', 'Bob', 'Cathy', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jill'],
    'phone_number': ['123-456-7890', '234-567-8901', '345-678-9012', '456-789-0123', '567-890-1234',
                     '678-901-2345', '789-012-3456', '890-123-4567', '901-234-5678', '012-345-6789'],
    'availability': ['frequently available', 'occasionally available', 'rarely available', 'frequently available',
                    'occasionally available', 'frequently available', 'rarely available', 'frequently available',
                    'occasionally available', 'frequently available'],
    'rating': [4.8, 4.5, 3.9, 5.0, 4.3, 4.7, 4.6, 5.0, 4.8, 4.1],
    'hourly_rate': [15, 12, 20, 18, 10, 14, 16, 20, 13, 11],
    'experience_level': [5, 3, 2, 10, 1, 4, 7, 8, 6, 3],  # years of experience
    'age_group': ['2 to 7', '2 to 7', '7 to 12', '2 to 7', '2 to 7', '2 to 7', '2 to 7', '2 to 7', '2 to 7', '2 to 7'],
    'zipcode': ['10001', '10001', '10001', '10001', '10001', '10001', '10001', '10001', '10001', '10001'],
    'available_time_slots': [['9 AM to 12 PM', '1 PM to 5 PM'], ['10 AM to 2 PM'], 
                             ['6 PM to 9 PM'], ['8 AM to 11 AM', '3 PM to 7 PM'], 
                             ['1 PM to 4 PM'], ['9 AM to 11 AM', '5 PM to 8 PM'],
                             ['12 PM to 3 PM'], ['7 PM to 10 PM'], 
                             ['2 PM to 5 PM'], ['10 AM to 1 PM']]
}

df = pd.DataFrame(data)

# Convert categorical data to numerical
availability_mapping = {'frequently available': 2, 'occasionally available': 1, 'rarely available': 0}
age_group_mapping = {'0 to 2': 0, '2 to 7': 1, '7 to 12': 2}

df['availability_numeric'] = df['availability'].map(availability_mapping)
df['age_group_numeric'] = df['age_group'].map(age_group_mapping)

# Availability classification
X_availability = df[['availability_numeric']]
y_availability = df['availability_numeric']
X_train, X_test, y_train, y_test = train_test_split(X_availability, y_availability, test_size=0.2, random_state=42)

knn_availability = KNeighborsClassifier(n_neighbors=2)
knn_availability.fit(X_train, y_train)

# Suitability classification
X_suitability = df[['rating', 'hourly_rate', 'experience_level', 'age_group_numeric']]
y_suitability = df['age_group_numeric']  # Target based on suitability (age group)
X_train_suitability, X_test_suitability, y_train_suitability, y_test_suitability = train_test_split(X_suitability, y_suitability, test_size=0.2, random_state=42)

knn_suitability = KNeighborsClassifier(n_neighbors=2)
knn_suitability.fit(X_train_suitability, y_train_suitability)

# Function to check if the requested time slot is available
def is_time_slot_available(babysitter_slots, start_time, end_time):
    for time_slot in babysitter_slots:
        start, end = time_slot.split(' to ')
        if (start_time >= start and start_time < end) or (end_time > start and end_time <= end):
            return True
    return False

# Function to recommend babysitter
def recommend_babysitter(num_kids, ages, hourly_rate, start_time, end_time, zipcode):
    # Dummy criteria based on availability
    availability_score = 1 if df['availability'].str.contains('frequently').any() else 0
    
    # Convert ages to age group inputs
    age_group_input = [age_group_mapping[age] for age in ages]
    
    # Filter available babysitters by zipcode
    available_sitters = df[df['availability_numeric'] == availability_score]
    available_sitters = available_sitters[available_sitters['zipcode'] == zipcode]
    
    # Recommend based on suitability and time slots
    recommendations = []
    for index, sitter in available_sitters.iterrows():
        if is_time_slot_available(sitter['available_time_slots'], start_time, end_time):
            suitability_score = knn_suitability.predict([[sitter['rating'], sitter['hourly_rate'], sitter['experience_level'], sitter['age_group_numeric']]])[0]
            if suitability_score in age_group_input and sitter['hourly_rate'] <= hourly_rate:
                recommendations.append(sitter)
    
    return recommendations

# User input
num_kids = int(input("Enter the number of kids: "))
ages = []
for i in range(num_kids):
    age = input(f"Enter the age of kid {i + 1} (0 to 2, 2 to 7, 7 to 12): ")
    ages.append(age)

hourly_rate = float(input("Enter the maximum hourly rate you are willing to pay: "))
start_time = input("Enter the start time slot when care is needed (e.g., '6 PM'): ")
end_time = input("Enter the end time slot when care is needed (e.g., '9 PM'): ")
zipcode = input("Enter the zip code where care is needed: ")

# Get recommendations
recommended_sitters = recommend_babysitter(num_kids, ages, hourly_rate, start_time, end_time, zipcode)

# Output recommendations
if recommended_sitters:
    print("\nRecommended Babysitters:")
    for sitter in recommended_sitters:
        print(f"Name: {sitter['name']}, Phone: {sitter['phone_number']}, Rating: {sitter['rating']}")
else:
    print("No suitable babysitters found.")

