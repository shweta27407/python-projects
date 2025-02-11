# Import necessary libraries
from math import sqrt
from collections import Counter
import statistics
import numpy as np
from mlxtend.frequent_patterns import fpgrowth, association_rules
import pandas as pd
import itertools
import time

# Start tracking execution time
start_time = time.time()

# Load the groceries dataset (transactions with items)
groceries_dataset = pd.read_csv('groceries-trimmed.csv', header=None)
print(groceries_dataset.head())

# Convert all values to strings to ensure uniform processing
groceries_dataset = groceries_dataset.applymap(str)

# Convert the dataset into a list of transactions
groceries_list = groceries_dataset.values.tolist()

# Function to encode the dataset into a binary format (1 if an item is present, 0 otherwise)
def encode_dataset(dataset):
    # Extract unique items from all transactions
    unique_items = sorted(set(item for transaction in dataset for item in transaction))
    
    # Convert each transaction into a binary vector
    encoded_dataset = []
    for transaction in dataset:
        encoded_transaction = [int(item in transaction) for item in unique_items]
        encoded_dataset.append(encoded_transaction)
    
    # Return as a Pandas DataFrame
    return pd.DataFrame(encoded_dataset, columns=unique_items)

# Function to calculate skewness of item frequency distribution
def skewness(dataset):
    # Flatten the list of transactions into a list of individual items
    all_items = [item for transaction in dataset for item in transaction]
    
    # Count occurrences of each item
    item_frequencies = Counter(all_items)

    # Compute skewness using statistical formula
    skewness_value = np.mean((np.array(list(item_frequencies.values())) - np.mean(list(item_frequencies.values())))**3) / np.power(np.var(list(item_frequencies.values())), 1.5)
    
    return skewness_value

# Function to dynamically determine the minimum support threshold based on data distribution
def dynamic_min_support(multiplier, skewness, support_values):
    if -1 < skewness < 1:
        # If skewness is low, use mean-based calculation
        central_tendency = 'mean'
        central_value = statistics.mean(support_values)
        std_dev_value = sqrt(sum((x - central_value) ** 2 for x in support_values) / len(support_values))
        min_support_threshold = central_value - multiplier * std_dev_value
    else:
        # If skewness is high, use median-based calculation (more robust to outliers)
        central_tendency = 'median'
        central_value = statistics.median(support_values)
        q75, q25 = np.percentile(list(support_values), [75 ,25])
        iqr = q75 - q25
        min_support_threshold = central_value - multiplier * iqr

    return min_support_threshold

# Function to find frequent itemsets using the FP-Growth algorithm
def fpgrowth_algorithm(dataset, min_support):
    # Convert dataset into a binary (one-hot encoded) format
    encoded_dataset = encode_dataset(dataset)
    
    # Apply the FP-Growth algorithm to find frequent itemsets
    frequent_itemsets = fpgrowth(encoded_dataset, min_support=min_support, use_colnames=True)
    
    # Convert itemsets to frozenset for dictionary storage
    frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(lambda x: frozenset(x))
    
    # Convert frequent itemsets into a dictionary {itemset: support}
    frequent_itemsets_dict = dict(zip(frequent_itemsets['itemsets'], frequent_itemsets['support']))
    
    return frequent_itemsets_dict

# Compute the skewness of the dataset
skew = skewness(groceries_list)
print("\n\n SKEW : ", skew)

# Multiplier for adjusting the minimum support threshold dynamically
multiplier = 0.5

# Function to calculate support values for individual items
def calculate_item_support(transaction_data):
    # Flatten the list of transactions into a list of individual items
    all_items = [item for transaction in transaction_data for item in transaction]
    
    # Count occurrences of each item
    item_counts = pd.Series(all_items).value_counts()
    
    # Compute the total number of transactions
    total_transactions = len(transaction_data)
    
    # Compute support for each item
    item_support = item_counts / total_transactions
    
    return item_support.tolist()

# Calculate item support values
items_support = calculate_item_support(groceries_list)

# Determine the minimum support threshold dynamically
min_support = dynamic_min_support(multiplier, skew, items_support)
print("\n\nINITIAL Min SUPP : ", min_support)

# Find frequent itemsets using FP-Growth
frequent_itemsets = fpgrowth_algorithm(groceries_list, min_support)

# Find the maximum itemset length
max_length = max(len(itemset) for itemset in frequent_itemsets)

# Dictionary to store itemsets categorized by their length
length_support_dict = {length: [] for length in range(1, max_length + 1)}
final_itemsets = {}  # Dictionary to store final itemsets after filtering

# Populate the dictionary with itemsets categorized by length
for itemset, support in frequent_itemsets.items():
    length = len(itemset)
    length_support_dict[length].append((itemset, support))

# Display the frequent itemsets along with their support values
print("\n\n LENGTH ITEMSETS DICTIONARY")
for length, itemsets in length_support_dict.items():
    print(f"\nLength {length} itemsets:")
    support_value_of_each_length = []
    for itemset, support in itemsets:
        support_value_of_each_length.append(round(support, 3))
        print(f"{itemset}: Support = {support:.3f}")

    # Compute dynamic threshold for filtering
    threshold = dynamic_min_support(0.5, skew, support_value_of_each_length)
    print(f"\n\n Length {length} threshold = {threshold:.3f}")

    # Retain itemsets that meet or exceed the computed threshold
    final_itemsets[length] = [(itemset, support) for itemset, support in itemsets if support >= threshold]

# Display final frequent itemsets
print("\n\nFINAL ITEMSETS DICTIONARY")
for length, itemsets in final_itemsets.items():
    for itemset, support in itemsets:
        print(f"{itemset}: Support = {support:.3f}")

# Function to generate all possible subsets of a given itemset
def generate_combinations(itemset, length):
    combinations = []
    for combination in itertools.combinations(itemset, length):
        combinations.append(frozenset(combination))
    return combinations

# Function to filter itemsets based on subset presence in previous levels
def compare_and_filter_levels(final_itemsets):
    output_frequentpatterns = {}
    prev_level = None

    for length, current_level in final_itemsets.items():
        if prev_level is not None:
            filtered_current_level = []

            for current_itemset, support in current_level:
                all_combinations_present = True
                for combination in generate_combinations(current_itemset, len(prev_level[0][0])):
                    combination_present = False
                    for prev_itemset, prev_support in prev_level:
                        if combination.issubset(prev_itemset):
                            combination_present = True
                            break
                    if not combination_present:
                        all_combinations_present = False
                        break

                if all_combinations_present:
                    filtered_current_level.append((current_itemset, support))
            
            output_frequentpatterns[length] = filtered_current_level

        if length == 1:
            output_frequentpatterns[length] = current_level
        
        prev_level = output_frequentpatterns[length]

    return output_frequentpatterns

# Apply filtering process
result = compare_and_filter_levels(final_itemsets)

# Display final frequent itemsets after filtering
print("\n\nRESULT")
for length, itemsets in result.items():
    print(f"\n Result Length {length} itemsets:")
    for itemset, support in itemsets:
        print(f"{itemset}: Support = {support:.3f}")

# Convert results into a dictionary for further processing
output_patterns = {}
for length, itemsets in result.items():
    for itemset, support in itemsets:
        output_patterns[itemset] = support

# Convert output to DataFrame
output_df = pd.DataFrame(list(output_patterns.items()), columns=['itemsets', 'support'])

# Generate association rules
min_confidence = 0.8
min_lift = 3
association_rules_df = association_rules(output_df, metric="confidence", min_threshold=min_confidence)
association_rules_df = association_rules_df[association_rules_df['lift'] >= min_lift]

# Display the association rules
print("\n\nAssociation Rules:")
print(association_rules_df[['antecedents', 'consequents', 'confidence', 'lift']])

# Compute and display total execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"\n\nTotal Execution Time: {execution_time:.2f} seconds")