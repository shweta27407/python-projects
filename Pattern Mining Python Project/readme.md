# **Frequent Itemset Mining Using FP-Growth Algorithm**  

## **Project Overview**  
This project aims to identify **frequent itemsets** in large datasets using the **FP-Growth (Frequent Pattern Growth) algorithm**. Frequent itemset mining is a fundamental step in **association rule mining**, which helps uncover valuable patterns in transactional datasets. The project dynamically determines the minimum support threshold based on the dataset's **skewness** to improve the effectiveness of frequent item discovery.  

## **Algorithms Used**  
### 1. **FP-Growth Algorithm**  
   - Unlike the Apriori algorithm, FP-Growth does not require candidate generation.  
   - It uses a **compact tree structure (FP-tree)** to store transactions efficiently.  
   - Frequent itemsets are extracted by recursively mining the tree structure.  

### 2. **Dynamic Minimum Support Calculation**  
   - The **skewness of the dataset** is used to decide whether to use the mean or median for threshold determination.  
   - If skewness is between **-1 and 1**, the **mean and standard deviation** are used.  
   - Otherwise, the **median and interquartile range (IQR)** are used.  

### 3. **Support and Association Rule Mining**  
   - The support of each itemset is calculated to identify **frequent itemsets**.  
   - **Association rules** are generated based on **confidence** and **lift** measures.  

---

## **Libraries Used**  
The project is implemented in Python using the following libraries:  

| Library        | Purpose |
|---------------|---------|
| `pandas`      | Data handling and manipulation |
| `numpy`       | Mathematical operations |
| `mlxtend`     | FP-Growth algorithm and association rules |
| `itertools`   | Combinatorial operations for itemset generation |
| `statistics`  | Mean, median, and standard deviation calculations |
| `collections` | Counting item occurrences efficiently |
| `math`        | Mathematical functions (e.g., square root for standard deviation) |
| `time`        | Execution time measurement |

---

## **Dataset Used**  
- **Dataset Name**: `groceries-trimmed.csv` (Kaggle)  
- **Description**:  
  - A **transactional dataset** where each row represents a shopping transaction.  
  - Items are represented as **strings** in each transaction.  
  - No predefined columns since the number of items per transaction varies.  

---

## **Project Workflow**  

### **1. Data Preprocessing**  
- Load the `groceries-trimmed.csv` dataset.  
- Convert all items into **string format** for consistency.  
- Transform the dataset into a **list of transactions**.  

### **2. Encoding Transactions**  
- Convert transactions into a **binary matrix**, where:  
  - `1` indicates the presence of an item in a transaction.  
  - `0` indicates the absence of the item.  

### **3. Skewness Calculation**  
- Skewness is measured to determine the distribution of item frequencies.  
- If skewness is between **-1 and 1**, the mean is used; otherwise, the median is used.  

### **4. Dynamic Minimum Support Calculation**  
- Support threshold is computed using **mean & standard deviation** or **median & IQR** based on the skewness value.  
- Helps in setting an **adaptive** and **optimal** minimum support threshold.  

### **5. Frequent Itemset Mining (FP-Growth Algorithm)**  
- The FP-Growth algorithm is applied to find **frequent itemsets** using the computed minimum support.  

### **6. Filtering and Threshold Adjustments**  
- Itemsets are grouped by their length.  
- Thresholds are recalculated dynamically for different lengths.  

### **7. Association Rule Mining**  
- Generate **association rules** from frequent itemsets.  
- Rules are filtered based on:  
  - **Minimum confidence (≥ 0.8)**  
  - **Minimum lift (≥ 3.0)**  

### **8. Result Display**  
- Display the frequent itemsets and their support values.  
- Print **final association rules** with support, confidence, and lift values.  
- Measure **total execution time**.  

---

## **Practical Applications**  

### 🛒 **Market Basket Analysis**  
   - Identifies which products are frequently purchased together.  
   - Helps businesses in **cross-selling** and **recommendation systems**.  

### 📊 **Customer Behavior Analysis**  
   - Detects shopping patterns and **customizes promotions**.  
   - Enhances **personalized marketing**.  

### 🔍 **Fraud Detection**  
   - Identifies **unusual purchase patterns** in banking transactions.  
   - Detects fraudulent activities by analyzing transaction frequency.  

### 🏥 **Healthcare & Medical Diagnosis**  
   - Identifies **frequent disease co-occurrences** in patient records.  
   - Helps in medical **diagnosis and treatment recommendations**.  

### 🌐 **Web & Clickstream Mining**  
   - Analyzes **user navigation behavior** on websites.  
   - Improves **website design and user experience**.  

---

## **Conclusion**  
This project provides an **efficient** and **adaptive** approach to frequent itemset mining by leveraging **FP-Growth** and **dynamic support thresholding**. It enhances the traditional method by considering **data skewness**, ensuring a more realistic and optimized extraction of frequent patterns. The extracted patterns can be further utilized for **decision-making and predictive analytics** in various domains. 🚀  
