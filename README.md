<div align="center">

# 🇮🇳 BharatNum

### Indian Number & Currency Datatype for Python

[![PyPI version](https://badge.fury.io/py/bharatnum.svg)](https://badge.fury.io/py/bharatnum)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI Downloads](https://img.shields.io/pypi/dm/bharatnum.svg)](https://pypi.org/project/bharatnum/)

**BharatNum** is a Python library built for India 🇮🇳 — handling Indian number formatting, Lakh/Crore conversions, number-to-words, GST helpers, EMI calculator, and Pandas integration — all in one clean package.

[Installation](#-installation) • [Usage](#-usage) • [Features](#-features) • [Pandas](#-pandas-integration) • [Contributing](#-contributing)

---

</div>

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🏷️ Indian Formatting | `₹25,00,000.00` — proper Indian comma system |
| 📊 Lakh / Crore | Instant conversion to Lakh and Crore |
| 🔤 Number to Words | `2500000` → `"Twenty Five Lakh"` |
| ➕ Arithmetic Ops | `+`, `-`, `*`, `/` operator support |
| ⚖️ Comparison Ops | `>`, `<`, `==`, `>=`, `<=` support |
| 🧾 GST & Tax | Add/remove tax in one line |
| 💸 Discount | Apply discounts instantly |
| 🏦 EMI Calculator | Monthly EMI from loan details |
| 🐼 Pandas Ready | Direct integration with DataFrames |

---

## 📦 Installation

```bash
pip install bharatnum
```

---

## 🚀 Usage

### Basic Example

```python
from bharatnum import BharatNum

salary = BharatNum(2500000)

print(salary)               # ₹25,00,000.00
print(salary.lakh)          # 25.0
print(salary.crore)         # 0.25
print(salary.words)         # Twenty Five Lakh
```

---

### ➕ Arithmetic Operations

```python
r1 = BharatNum(1000000)
r2 = BharatNum(500000)

print(r1 + r2)    # ₹15,00,000.00
print(r1 - r2)    # ₹5,00,000.00
print(r1 * 2)     # ₹20,00,000.00
print(r1 / 4)     # ₹2,50,000.00
```

---

### ⚖️ Comparison Operations

```python
r1 = BharatNum(1000000)
r2 = BharatNum(500000)

print(r1 > r2)    # True
print(r1 == r2)   # False
print(r1 >= r2)   # True
```

---

### 🧾 GST & Tax Helpers

```python
price = BharatNum(1000)

print(price.tax(18))           # ₹1,180.00  → 18% GST added
print(price.tax_amount(18))    # ₹180.00    → only GST amount
print(price.remove_tax(18))    # ₹847.46    → original price from GST-inclusive price
```

---

### 💸 Discount Calculator

```python
price = BharatNum(5000)

print(price.discount(10))          # ₹4,500.00  → 10% off
print(price.discount_amount(10))   # ₹500.00    → discount amount only
```

---

### 🏦 EMI Calculator

```python
loan = BharatNum(500000)

# emi(annual_rate%, months)
print(loan.emi(8.5, 24))    # ₹22,727.84  → monthly EMI
print(loan.emi(10, 12))     # ₹43,954.28  → monthly EMI
```

---

### 📊 Other Utilities

```python
salary = BharatNum(50000)

print(salary.percentage_of(20))           # ₹10,000.00  → 20% of salary
print(salary.split(4))                    # ₹12,500.00  → split among 4

old = BharatNum(40000)
new = BharatNum(50000)
print(old.percent_change(new))            # 25.0  → 25% hike
```

---

## 🐼 Pandas Integration

```python
import pandas as pd
from bharatnum import format_indian, to_words, to_lakh, add_tax_column

df = pd.DataFrame({
    'name':   ['Amit', 'Priya', 'Rahul', 'Sara'],
    'salary': [2500000, 500000, 1500000, 7500000],
    'price':  [1000, 5000, 2000, 8000]
})

df['salary_formatted'] = format_indian(df['salary'])
df['salary_words']     = to_words(df['salary'])
df['salary_lakh']      = to_lakh(df['salary'])
df = add_tax_column(df, 'price', 18)

print(df)
```

**Output:**

```
    name   salary  salary_formatted       salary_words  salary_lakh  price  price_with_tax
0   Amit  2500000    ₹25,00,000.00   Twenty Five Lakh         25.0   1000          1180.0
1  Priya   500000     ₹5,00,000.00          Five Lakh          5.0   5000          5900.0
2  Rahul  1500000    ₹15,00,000.00       Fifteen Lakh         15.0   2000          2360.0
3   Sara  7500000    ₹75,00,000.00  Seventy Five Lakh         75.0   8000          9440.0
```

---

## 📁 Project Structure

```
bharatnum/
├── bharatnum/
│   ├── __init__.py       → Package entry point
│   ├── core.py           → BharatNum main class
│   ├── words.py          → Number to Words engine
│   ├── helpers.py        → Tax, GST, EMI, Discount
│   └── pandas_ext.py     → Pandas integration
├── README.md
├── setup.py
└── LICENSE
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

---

## 👨‍💻 Author

**Prathamesh Chaudhari**
- GitHub: [@Prathameshchaudhari2004](https://github.com/Prathameshchaudhari2004)
- PyPI: [bharatnum](https://pypi.org/project/bharatnum/)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ for India 🇮🇳

⭐ Star this repo if you found it useful!

</div>
