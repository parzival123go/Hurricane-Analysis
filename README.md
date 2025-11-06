# Hurricane-Analysis

## Overview

This project analyzes data on **Category 5 hurricanes**, the strongest hurricanes as measured by their wind speed. Unlike step-by-step tutorials, this project is open-ended and requires building multiple functions to organize, manipulate, and analyze hurricane data.

The goal is to practice Python skills including **lists, dictionaries, loops, conditionals, string manipulation, and function creation**, while exploring real-world environmental data.

> Note: Category 5 hurricanes have sustained winds ≥ 157 mph (252 km/h) and are extremely destructive.

---

## Project Goals

You will write several functions to handle and analyze data about the 34 strongest Atlantic hurricanes. Each function has a specific task, such as updating data, counting occurrences, or rating hurricanes based on different metrics.

---

## Project Requirements

### 1. Update Recorded Damages

The dataset contains a list of damages caused by each hurricane. Some values are missing (`"Damages not recorded"`), while others are in string format with **M** (millions) or **B** (billions).

**Task:**
Write a function that converts recorded damages into numeric values (`float`) while leaving missing data as `"Damages not recorded"`.

**Test:** Use the `damages` list provided.

---

### 2. Create Hurricane Dictionary

Additional hurricane data is provided in separate lists:

* `names` — names of the hurricanes
* `months` — month of occurrence
* `years` — year of occurrence
* `max_sustained_winds` — maximum sustained winds (mph)
* `areas_affected` — list of affected areas
* `deaths` — total number of deaths

**Task:**
Create a dictionary where each hurricane name is a key, and its value is another dictionary containing all associated data:

```python
{
    'Name': 'Cuba I',
    'Month': 'October',
    'Year': 1924,
    'Max Sustained Wind': 165,
    'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
    'Damage': 'Damages not recorded',
    'Deaths': 90
}
```

---

### 3. Organize Hurricanes by Year

**Task:**
Convert the hurricane dictionary into a new dictionary where keys are years, and values are lists of hurricanes that occurred in that year.

---

### 4. Count Affected Areas

**Task:**
Write a function that counts how often each area of the Atlantic was affected by these hurricanes. Return a dictionary with areas as keys and counts as values.

---

### 5. Most Affected Area

**Task:**
Determine which area was hit by the most hurricanes and how many times it was affected.

---

### 6. Deadliest Hurricane

**Task:**
Find the hurricane that caused the greatest number of deaths, along with the number of deaths.

---

### 7. Rate Hurricanes by Mortality

Using the mortality scale below, rate each hurricane by the number of deaths:

```python
mortality_scale = {
    0: 0,
    1: 100,
    2: 500,
    3: 1000,
    4: 10000
}
```

* Rating 1 → 1–100 deaths
* Rating 2 → 101–500 deaths
* Rating 3 → 501–1,000 deaths
* Rating 4 → 1,001–10,000 deaths
* Rating 5 → >10,000 deaths

**Task:**
Create a dictionary where keys are mortality ratings, and values are lists of hurricanes that fall into each rating.

---

### 8. Most Damaging Hurricane

**Task:**
Identify the hurricane that caused the greatest financial damage and the total cost.

---

### 9. Rate Hurricanes by Damage

Using the damage scale below, categorize hurricanes by their economic impact:

```python
damage_scale = {
    0: 0,
    1: 100_000_000,
    2: 1_000_000_000,
    3: 10_000_000_000,
    4: 50_000_000_000
}
```

* Rating 1 → >0 and ≤ $100M
* Rating 2 → >$100M and ≤ $1B
* Rating 3 → >$1B and ≤ $10B
* Rating 4 → >$10B and ≤ $50B
* Rating 5 → >$50B

**Task:**
Create a dictionary where keys are damage ratings, and values are lists of hurricanes in each category.

---

## Notes

* This project emphasizes **data organization, analysis, and categorization**.
* It is intended to strengthen your Python skills while exploring real-world hurricane data.
* For best results, complete the **Loops** and **Dictionaries** sections of the Codecademy Python 3 course or the Data Scientist Career Path before starting.
