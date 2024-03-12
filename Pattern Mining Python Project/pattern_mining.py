from math import sqrt
from collections import Counter
import statistics
import numpy as np
from mlxtend.frequent_patterns import fpgrowth, association_rules
import pandas as pd
import itertools
import time

start_time = time.time()
# Load the groceries-trimmed dataset
groceries_dataset = pd.read_csv('groceries-trimmed.csv', header=None)
print(groceries_dataset.head())
groceries_dataset = groceries_dataset.applymap(str)
groceries_list = groceries_dataset.values.tolist()

def encode_dataset(dataset):
    unique_items = sorted(set(item for transaction in dataset for item in transaction))
    
    encoded_dataset = []
    for transaction in dataset:
        encoded_transaction = [int(item in transaction) for item in unique_items]
        encoded_dataset.append(encoded_transaction)
    
    return pd.DataFrame(encoded_dataset, columns=unique_items)

def skewness(dataset):
    all_items = [item for transaction in dataset for item in transaction]
    item_frequencies = Counter(all_items)
    skewness = np.mean((np.array(list(item_frequencies.values())) - np.mean(list(item_frequencies.values())))**3) / np.power(np.var(list(item_frequencies.values())), 1.5)
    return skewness

def dynamic_min_support(multiplier, skewness, support_values):
    if -1 < skewness < 1:
        central_tendency = 'mean'
        central_value = statistics.mean(support_values)
        std_dev_value = sqrt(sum((x - central_value) ** 2 for x in support_values) / len(support_values))
        min_support_threshold = central_value - multiplier * std_dev_value
    else:
        central_tendency = 'median'
        central_value = statistics.median(support_values)
        q75, q25 = np.percentile(list(support_values), [75 ,25])
        iqr = q75 - q25
        min_support_threshold = central_value - multiplier * iqr

    return min_support_threshold

def fpgrowth_algorithm(dataset, min_support):
    encoded_dataset = encode_dataset(dataset)
    frequent_itemsets = fpgrowth(encoded_dataset, min_support=min_support, use_colnames=True)
    frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(lambda x: frozenset(x))
    frequent_itemsets_dict = dict(zip(frequent_itemsets['itemsets'], frequent_itemsets['support']))
    return frequent_itemsets_dict

# Use groceries dataset
skew = skewness(groceries_list)
print("\n\n SKEW : ", skew)

multiplier = 0.5

def calculate_item_support(transaction_data):
   
    all_items = [item for transaction in transaction_data for item in transaction]      # Flatten the list of items in transactions
    item_counts = pd.Series(all_items).value_counts()     # Count the frequency of each item
    total_transactions = len(transaction_data)
    item_support = item_counts / total_transactions      #Calculate support for each item 

    return item_support.tolist()
    
items_support = calculate_item_support(groceries_list)   # Set your desired minimum support value

min_support = dynamic_min_support(multiplier, skew, items_support)
print("\n\nINITIAL Min SUPP : ", min_support)
#min_support = 0.01  # Set your desired minimum support value

frequent_itemsets = fpgrowth_algorithm(groceries_list, min_support)

max_length = max(len(itemset) for itemset in frequent_itemsets)

length_support_dict = {length: [] for length in range(1, max_length + 1)}  # Populate the dictionary
final_itemsets = {}  # To store the final itemsets as itemset-support dictionary

for itemset, support in frequent_itemsets.items():
    length = len(itemset)
    length_support_dict[length].append((itemset, support))

# Display the results
print("\n\n LENGTH ITEMSETS DICTIONARY")
for length, itemsets in length_support_dict.items():
    print(f"\nLength {length} itemsets:")
    support_value_of_each_length = []
    for itemset, support in itemsets:
        support_value_of_each_length.append(round(support, 3))
        print(f"{itemset}: Support = {support:.3f}")

    threshold = dynamic_min_support(0.5, skew, support_value_of_each_length)
    print(f"\n\n Length {length} threshold = {threshold:.3f}")

    # Append itemsets to final_itemsets with key as itemset and value as support
    final_itemsets[length] = [(itemset, support) for itemset, support in itemsets if support >= threshold]


print("\n\nFINAL ITEMSETS DICTIONARY")
for length, itemsets in final_itemsets.items():
    for itemset, support in itemsets:
        print(f"{itemset}: Support = {support:.3f}")

def generate_combinations(itemset, length):
    combinations = []
    for combination in itertools.combinations(itemset, length):
        combinations.append(frozenset(combination))
    return combinations

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


result = compare_and_filter_levels(final_itemsets)

print("\n\nRESULT")
for length, itemsets in result.items():
    print(f"\n Result Length {length} itemsets:")
    for itemset, support in itemsets:
        print(f"{itemset}: Support = {support:.3f}")

output_patterns = {}

for length, itemsets in result.items():
    for itemset, support in itemsets:
        output_patterns[itemset] = support

# Convert output_patterns to a DataFrame
output_df = pd.DataFrame(list(output_patterns.items()), columns=['itemsets', 'support'])

# Generate association rules
min_confidence = 0.8
min_lift = 3

association_rules_df = association_rules(output_df, metric="confidence", min_threshold=min_confidence)

# Filter rules based on minimum lift
association_rules_df = association_rules_df[association_rules_df['lift'] >= min_lift]

# Display the association rules
print("\n\nAssociation Rules:")
print(association_rules_df[['antecedents', 'consequents', 'antecedent support', 'consequent support', 'confidence', 'lift']])

end_time = time.time()
execution_time = end_time - start_time
print(f"\n\nTotal Execution Time: {execution_time:.2f} seconds")