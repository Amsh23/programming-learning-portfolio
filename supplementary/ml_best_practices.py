"""
Machine Learning Best Practices: Train/Test Split & Cross-Validation

Supplementary material - not original class code.
This demonstrates essential ML practices that prevent overfitting and ensure models
actually work on new, unseen data.

This is THE most important skill for machine learning interviews and production use.
"""

import numpy as np
from sklearn.datasets import load_iris, make_classification
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt


# ============================================================================
# THE PROBLEM: Why we need train/test split
# ============================================================================

print("="*70)
print("THE PROBLEM: Why Train/Test Split Matters")
print("="*70)

"""
Imagine training a model on ALL your data, then evaluating it on the SAME data.

❌ WRONG approach:
  1. Train model on all 1000 data points
  2. Test model on the same 1000 data points
  3. Get 99% accuracy
  
  Problem: The model has memorized the training data!
  In production, with NEW data, it might perform terribly.
  This is called "OVERFITTING"

✓ CORRECT approach:
  1. Split data into 80% training, 20% testing
  2. Train model on 800 points
  3. Test model on 200 NEW points
  4. Get realistic accuracy (maybe 85%)
  
  This simulates how the model will perform in production!
"""

# Example: Model that memorizes training data
print("\nExample - Overfitting vs Generalization:")
print("-" * 70)

# Create simple data
X_all = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y_all = np.array([0, 0, 1, 1, 1])

# ❌ WRONG: Train and test on same data
from sklearn.tree import DecisionTreeClassifier
model_wrong = DecisionTreeClassifier(random_state=42)
model_wrong.fit(X_all, y_all)
wrong_accuracy = model_wrong.score(X_all, y_all)
print(f"❌ WRONG - Train and test on same data: {wrong_accuracy:.2%} accuracy")

# ✓ CORRECT: Split data
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=0.2, random_state=42)
model_right = DecisionTreeClassifier(random_state=42)
model_right.fit(X_train, y_train)
right_accuracy = model_right.score(X_test, y_test)
print(f"✓ CORRECT - Train on 80%, test on 20%: {right_accuracy:.2%} accuracy")


# ============================================================================
# TRAIN/TEST SPLIT: The Basic Pattern
# ============================================================================

print("\n" + "="*70)
print("TRAIN/TEST SPLIT: The Basic Pattern")
print("="*70)

# Load a real dataset
iris = load_iris()
X = iris.data
y = iris.target

print(f"\nDataset size: {len(X)} samples, {X.shape[1]} features")

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,        # Use 20% for testing
    random_state=42,      # For reproducibility
    stratify=y            # Keep class distribution same in train and test
)

print(f"Training set: {len(X_train)} samples (80%)")
print(f"Test set: {len(X_test)} samples (20%)")
print(f"Class distribution - Training: {np.bincount(y_train)}")
print(f"Class distribution - Test: {np.bincount(y_test)}")

# Train model
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Evaluate
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)

print(f"\nResults:")
print(f"  Training accuracy: {train_accuracy:.2%}")
print(f"  Test accuracy: {test_accuracy:.2%}")


# ============================================================================
# CROSS-VALIDATION: More Robust Evaluation
# ============================================================================

print("\n" + "="*70)
print("CROSS-VALIDATION: More Robust Than Single Train/Test Split")
print("="*70)

"""
Problem with single train/test split:
  - Results depend on which samples randomly ended up in train vs test
  - One lucky split might show great accuracy, another might show poor
  - How do you know if your result is reliable?

Solution: K-Fold Cross-Validation
  - Split data into K folds (usually K=5)
  - Train K models:
    * Model 1: Train on folds 2-5, test on fold 1
    * Model 2: Train on folds 1,3-5, test on fold 2
    * Model 3: Train on folds 1-2,4-5, test on fold 3
    * etc...
  - Average the K results
  - Get a more reliable accuracy estimate
"""

print("\n5-Fold Cross-Validation Process:")
print("-" * 70)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
model_cv = LogisticRegression(max_iter=1000, random_state=42)

scores = cross_val_score(model_cv, X, y, cv=cv, scoring='accuracy')

print(f"Fold scores: {scores}")
print(f"Mean accuracy: {scores.mean():.2%}")
print(f"Std deviation: {scores.std():.2%}")
print(f"Confidence: {scores.mean():.2%} ± {scores.std():.2%}")

"""
Interpretation:
  - If we train this model 5 times on different subsets:
    * Best case: 100% accuracy
    * Worst case: 93.3% accuracy  
    * Average: 98% accuracy
  
  This is much more reliable than a single 97% from one split!
"""


# ============================================================================
# COMPLETE ML WORKFLOW
# ============================================================================

print("\n" + "="*70)
print("COMPLETE ML WORKFLOW: How to Do It Right")
print("="*70)

"""
The proper workflow:

1. Load data
2. Exploratory analysis (optional)
3. Split into train/test
4. Preprocess (fit on training set ONLY)
5. Train model (on training set ONLY)
6. Evaluate on test set
7. Use cross-validation to validate results
8. If happy, deploy model and evaluate on production data
"""

# Step 1: Load data
print("\nStep 1: Load Data")
X, y = load_iris(return_X_y=True)
print(f"Loaded {len(X)} samples")

# Step 3: Split data
print("\nStep 3: Train/Test Split")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Training: {len(X_train)} samples | Test: {len(X_test)} samples")

# Step 4: Preprocessing - IMPORTANT: Fit on training set only!
print("\nStep 4: Preprocessing (fit on training set ONLY)")
scaler = StandardScaler()
scaler.fit(X_train)  # ← Only fit on training data
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use same transformation
print("Features normalized using training set statistics")

# Step 5: Train model
print("\nStep 5: Train Model")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)
print("Model trained on training set")

# Step 6: Evaluate on test set
print("\nStep 6: Evaluate on Test Set")
y_pred = model.predict(X_test_scaled)
test_acc = accuracy_score(y_test, y_pred)
print(f"Test accuracy: {test_acc:.2%}")

# Step 7: Cross-validation for robustness
print("\nStep 7: Cross-Validation (5-fold)")
cv_scores = cross_val_score(
    RandomForestClassifier(n_estimators=100, random_state=42),
    X_train_scaled, y_train, 
    cv=5, 
    scoring='accuracy'
)
print(f"CV scores: {[f'{s:.1%}' for s in cv_scores]}")
print(f"Mean CV accuracy: {cv_scores.mean():.2%} ± {cv_scores.std():.2%}")

print("\n✓ Model is robust and ready for deployment!")


# ============================================================================
# COMPREHENSIVE EVALUATION METRICS
# ============================================================================

print("\n" + "="*70)
print("COMPREHENSIVE EVALUATION METRICS")
print("="*70)

"""
Accuracy is NOT enough! 

Example: Medical test for rare disease
  - Disease affects 1% of population
  - If test always says "negative":
    * It's correct 99% of the time!
    * But it misses ALL the sick people
    * Accuracy: 99%, Utility: 0%

Solution: Use multiple metrics:
  - Accuracy: Overall correctness (good for balanced data)
  - Precision: Of positive predictions, how many are correct?
  - Recall: Of actual positives, how many did we find?
  - F1-Score: Harmonic mean of precision and recall
  - Confusion Matrix: See exactly which mistakes are made
"""

print("\nMetrics for our test set:")
print("-" * 70)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy:  {accuracy:.4f} - Correct predictions / total")
print(f"Precision: {precision:.4f} - True positives / all predicted positive")
print(f"Recall:    {recall:.4f} - True positives / all actual positive")
print(f"F1-Score:  {f1:.4f} - Balance between precision and recall")

print("\nConfusion Matrix (shows misclassifications):")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print("\nInterpretation:")
print("- Diagonal (correct predictions)")
print("- Off-diagonal (misclassifications)")


# ============================================================================
# CRITICAL MISTAKES TO AVOID
# ============================================================================

print("\n" + "="*70)
print("CRITICAL MISTAKES TO AVOID")
print("="*70)

mistakes = """
❌ MISTAKE 1: Data Leakage
   Problem: Information from test set leaks into training
   Example: Scaling on full dataset before splitting
   Fix: Always fit preprocessing on training set ONLY
   
❌ MISTAKE 2: Not Using Test Set
   Problem: Only evaluating on training data
   Example: Training accuracy 99%, actual performance 60%
   Fix: Always evaluate on separate, untouched test data
   
❌ MISTAKE 3: Random Train/Test Split
   Problem: Each run gives different results
   Example: Run 1 gives 95%, Run 2 gives 91%
   Fix: Use random_state=42 for reproducibility
   
❌ MISTAKE 4: Imbalanced Train/Test
   Problem: Test set has different class distribution
   Example: Training is 50/50, test is 99/1
   Fix: Use stratify=y to maintain distribution
   
❌ MISTAKE 5: Using Accuracy for Imbalanced Data
   Problem: Accuracy hides poor performance on minority class
   Example: 99% accuracy by predicting majority class
   Fix: Use precision, recall, F1-score instead
   
❌ MISTAKE 6: Optimizing on Test Set
   Problem: Overfitting to test set through repeated evaluation
   Example: Trying 100 models, reporting best test result
   Fix: Use cross-validation on training set only
   
❌ MISTAKE 7: Preprocessing Before Splitting
   Problem: Test set statistics leak into training
   Example: Removing outliers before splitting
   Fix: Always split first, then preprocess separately
"""

print(mistakes)


# ============================================================================
# VISUALIZATION: Train vs Test Performance Over Time
# ============================================================================

print("\n" + "="*70)
print("OVERFITTING VISUALIZATION")
print("="*70)

# Generate more data for this demonstration
X_large, y_large = make_classification(n_samples=300, n_features=20, n_informative=10, random_state=42)
X_train_l, X_test_l, y_train_l, y_test_l = train_test_split(X_large, y_large, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier

train_scores = []
test_scores = []
depths = range(1, 21)

for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train_l, y_train_l)
    train_scores.append(model.score(X_train_l, y_train_l))
    test_scores.append(model.score(X_test_l, y_test_l))

print("\nObservations:")
print(f"- Training accuracy increases with depth: {train_scores[0]:.2%} → {train_scores[-1]:.2%}")
print(f"- Test accuracy plateaus then decreases: {test_scores[0]:.2%} → {test_scores[-1]:.2%}")
print(f"- Optimal depth: ~{depths[np.argmax(test_scores)]}")
print("\n✓ This is why we need BOTH train and test evaluation!")


# ============================================================================
# PRACTICE CHECKLIST
# ============================================================================

print("\n" + "="*70)
print("PRACTICE CHECKLIST: Am I Following Best Practices?")
print("="*70)

checklist = """
Before training any model, verify:

☐ Data is split into training and test sets
☐ Test set is not used until final evaluation
☐ Train/test split uses stratify=y for classification
☐ Preprocessing is fit on training set only
☐ I'm evaluating on test set separately from training
☐ I'm using appropriate metrics for my problem
  ☐ Classification: precision, recall, F1, confusion matrix
  ☐ Regression: R², RMSE, MAE
☐ I'm using cross-validation to verify robustness
☐ Train accuracy and test accuracy are similar (no overfitting)
  ☐ If train >> test: Model is overfitting
  ☐ If train ≈ test: Model is generalizing well
☐ I can explain why I chose this train/test split ratio
☐ Results are reproducible (using random_state)
"""

print(checklist)


# ============================================================================
# SUMMARY: Train/Test Split & Cross-Validation
# ============================================================================

print("\n" + "="*70)
print("SUMMARY")
print("="*70)

summary = """
KEY CONCEPTS:

1. Train/Test Split:
   - Split data: 80% training, 20% testing (or 70/30, 75/25)
   - Train model ONLY on training data
   - Evaluate ONLY on test data
   - This gives realistic performance estimate

2. Why It Matters:
   - Prevents overfitting (memorizing training data)
   - Simulates real-world deployment
   - Test accuracy = production performance estimate

3. Cross-Validation:
   - Better than single train/test split
   - Splits into K folds, trains K models
   - Averages results for reliability
   - Use 5-fold or 10-fold

4. Critical Rule:
   - Never look at test data during training
   - Preprocess (scaling, etc) fits on train set only
   - No data leakage from test to train

5. Evaluation:
   - Use appropriate metrics for your problem
   - Accuracy alone is not sufficient
   - Check for overfitting (train accuracy >> test accuracy)

6. Interview Answer:
   When asked "How do you prevent overfitting?":
   - "Split data into training and test sets"
   - "Use cross-validation"
   - "Monitor train/test accuracy gap"
   - "Use regularization techniques"
   - "Validate on unseen data"
"""

print(summary)

print("\n✓ You now understand ML best practices - use them in every project!")
