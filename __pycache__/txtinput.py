file_path = "data.txt"

# Initialize an empty dictionary to store the extracted data
data = []

# Open the text file and read its contents
with open("data.txt", 'r') as file:
    lines = file.readlines()

# Process the lines and extract data
current_data = {}
for line in lines:
    if line.strip() == "":
        if current_data:
            data.append(current_data)
            current_data = {}
    else:
        key, value = line.strip().split(": ", 1)
        current_data[key] = value

# Print the extracted data
for row in data:
    print(f"Name: {row['Name']}, Age: {row['Age']}, Location: {row['Location']}")
