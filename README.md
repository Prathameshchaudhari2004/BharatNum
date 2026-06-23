# BharatNum 🇮🇳

Indian Number & Currency Datatype for Python.

## Install
pip install bharatnum

## Usage
from bharatnum import BharatNum

salary = BharatNum(2500000)

print(salary)              # ₹25,00,000.00
print(salary.lakh)         # 25.0
print(salary.crore)        # 0.25
print(salary.words)        # Twenty Five Lakh
print(salary.tax(18))      # ₹29,50,000.00
print(salary.discount(10)) # ₹22,50,000.00
print(salary.split(4))     # ₹6,25,000.00
print(salary.emi(8.5, 24)) # Monthly EMI

## Pandas Integration
import pandas as pd
from bharatnum import format_indian, to_words, to_lakh

df = pd.DataFrame({'salary': [2500000, 500000, 1500000]})
df['formatted'] = format_indian(df['salary'])
df['words']     = to_words(df['salary'])
df['in_lakh']   = to_lakh(df['salary'])
print(df)

## Features
- Indian number formatting (₹25,00,000.00)
- Lakh / Crore conversion
- Number to Words (Indian system)
- Arithmetic operators (+, -, *, /)
- Comparison operators (>, <, ==)
- GST / Tax helpers
- Discount calculator
- EMI calculator
- Pandas integration