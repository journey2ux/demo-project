import pandas as pd

# Example data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

# Create DataFrame
df = pd.DataFrame(data)

df.head(2)  # Display the first few rows of the DataFrame
