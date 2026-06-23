from bharatnum import BharatNum
import pandas as pd

r1 = BharatNum(2500000)
r2 = BharatNum(150000)
r3 = BharatNum(25000000)

print(r1)        # ₹25,00,000.00
print(r1.words)  # Twenty Five Lakh
print(r2.words)  # One Lakh Fifty Thousand
print(r3.words)  # Two Crore Fifty Lakh
print(r1.lakh)   # 25.0
print(r1.crore)  # 0.25



price = BharatNum(1000)
salary = BharatNum(50000)
loan = BharatNum(500000)

print(price.tax(18))               # ₹1,180.00  (18% GST)
print(price.tax_amount(18))        # ₹180.00     (sirf GST)
print(price.discount(10))          # ₹900.00     (10% off)
print(price.discount_amount(10))   # ₹100.00     (kitna discount)
print(price.split(4))              # ₹250.00     (4 me baant do)
print(salary.percentage_of(20))    # ₹10,000.00  (20% of salary)
print(loan.emi(8.5, 24))           # Monthly EMI




from bharatnum import (
    format_indian, to_words,
    to_lakh, to_crore,
    add_tax_column, add_discount_column
)

# Sample DataFrame
df = pd.DataFrame({
    'name': ['Amit', 'Priya', 'Rahul', 'Sara'],
    'salary': [2500000, 500000, 1500000, 7500000],
    'product_price': [1000, 5000, 2000, 8000]
})

print("─── Original DataFrame ───")
print(df)

print("\n─── Indian Format ───")
df['salary_formatted'] = format_indian(df['salary'])
print(df[['name', 'salary_formatted']])

print("\n─── Salary in Words ───")
df['salary_words'] = to_words(df['salary'])
print(df[['name', 'salary_words']])

print("\n─── Salary in Lakh ───")
df['salary_lakh'] = to_lakh(df['salary'])
print(df[['name', 'salary_lakh']])

print("\n─── Price with 18% GST ───")
df = add_tax_column(df, 'product_price', 18)
print(df[['name', 'product_price', 'product_price_with_tax']])

print("\n─── Price after 10% Discount ───")
df = add_discount_column(df, 'product_price', 10)
print(df[['name', 'product_price', 'product_price_after_discount']])