

---

## Distribution of Total Score (8) Among Sub-Indicators

### Step 1: Weights of Sub-Indicators  
The weights of the sub-indicators are as follows:  

| **Sub-Indicator** | **Weight (%)** | **Decimal Equivalent** |
|--------------------|----------------|-------------------------|
| Sub-indicator 1    | 20%            | 0.20                   |
| Sub-indicator 2    | 20%            | 0.20                   |
| Sub-indicator 3    | 25%            | 0.25                   |
| Sub-indicator 4    | 20%            | 0.20                   |
| Sub-indicator 5    | 15%            | 0.15                   |

---

### Step 2: Divide Total Score (8) According to Weights  
The score for each sub-indicator is calculated as:  
\[
\text{Score for each sub-indicator} = \text{Weight} \times 8
\]

| **Sub-Indicator** | **Weight (%)** | **Calculation**    | **Score** |
|--------------------|----------------|--------------------|-----------|
| Sub-indicator 1    | 20%            | \( 0.20 \times 8 \) | 1.6       |
| Sub-indicator 2    | 20%            | \( 0.20 \times 8 \) | 1.6       |
| Sub-indicator 3    | 25%            | \( 0.25 \times 8 \) | 2.0       |
| Sub-indicator 4    | 20%            | \( 0.20 \times 8 \) | 1.6       |
| Sub-indicator 5    | 15%            | \( 0.15 \times 8 \) | 1.2       |

---

### Step 3: Adjust Scores to Fit "Out of 2" Scale  
Since the maximum score for each sub-indicator is **2**, we normalize the scores proportionally while ensuring their sum equals **8**.  

The normalization formula:
\[
\text{Normalized Score} = \frac{\text{Score for Sub-Indicator}}{2} \times 2
\]

After applying this formula, the recalculated scores are the same as the original calculated scores:  

| **Sub-Indicator** | **Score (Out of 2)** |
|--------------------|----------------------|
| Sub-indicator 1    | 1.6                  |
| Sub-indicator 2    | 1.6                  |
| Sub-indicator 3    | 2.0                  |
| Sub-indicator 4    | 1.6                  |
| Sub-indicator 5    | 1.2                  |

---

### Step 4: Verify Total Score  
The sum of all sub-indicator scores:  
\[
1.6 + 1.6 + 2.0 + 1.6 + 1.2 = 8.0
\]

The total matches the required score of **8**.

---

### Final Result:

| **Sub-Indicator** | **Weight (%)** | **Score (Out of 2)** |
|--------------------|----------------|-----------------------|
| Sub-indicator 1    | 20%            | 1.6                  |
| Sub-indicator 2    | 20%            | 1.6                  |
| Sub-indicator 3    | 25%            | 2.0                  |
| Sub-indicator 4    | 20%            | 1.6                  |
| Sub-indicator 5    | 15%            | 1.2                  |

---

### python code

# Given data
weights = [20, 20, 25, 20, 15]  # Weightages in percentages
total_score = 8  # Total indicator score
max_score_per_sub_indicator = 2  # Maximum score per sub-indicator

# Step 1: Convert weights to fractions
weights_fraction = [w / 100 for w in weights]

# Step 2: Calculate raw scores for sub-indicators
raw_scores = [total_score * w for w in weights_fraction]

# Step 3: Scale raw scores to ensure they sum to 8
scaled_scores = [round(score / sum(raw_scores) * total_score, 4) for score in raw_scores]

# Step 4: Normalize adjusted scores to fit within the "out of 2" limit
final_scores = [round(score, 2) for score in scaled_scores]

# Step 5: Ensure total sum is exactly 8
scaling_factor = total_score / sum(final_scores)
final_scores = [round(score * scaling_factor, 2) for score in final_scores]

# Display the results
print("Sub-Indicator Scores Distribution:")
for i, score in enumerate(final_scores):
    print(f"Sub-Indicator {i+1}: Weightage = {weights[i]}%, Final Score = {score} (out of 2)")

# Sum check
print(f"\nSum of all sub-indicator scores: {sum(final_scores)} (should equal {total_score})")
