from __future__ import annotations
import pandas as pd
from bharatnum.core import BharatNum


def to_bharatnum(series: pd.Series) -> pd.Series:
    """
    Pandas Series ke har element ko BharatNum me convert karo
    Example: df['salary'].apply(to_bharatnum)
    """
    return series.apply(lambda x: BharatNum(x))


def format_indian(series: pd.Series) -> pd.Series:
    """
    Pandas Series ke numbers ko Indian format me convert karo
    Example: df['salary'].pipe(format_indian)
    → ₹25,00,000.00, ₹5,00,000.00 ...
    """
    return series.apply(lambda x: str(BharatNum(x)))


def to_words(series: pd.Series) -> pd.Series:
    """
    Pandas Series ke numbers ko words me convert karo
    Example: df['salary'].pipe(to_words)
    → "Twenty Five Lakh", "Five Lakh" ...
    """
    return series.apply(lambda x: BharatNum(x).words)


def to_lakh(series: pd.Series) -> pd.Series:
    """
    Pandas Series ke numbers ko Lakh me convert karo
    Example: df['salary'].pipe(to_lakh)
    → 25.0, 5.0 ...
    """
    return series.apply(lambda x: BharatNum(x).lakh)


def to_crore(series: pd.Series) -> pd.Series:
    """
    Pandas Series ke numbers ko Crore me convert karo
    Example: df['salary'].pipe(to_crore)
    → 0.25, 0.05 ...
    """
    return series.apply(lambda x: BharatNum(x).crore)


def add_tax_column(df: pd.DataFrame, column: str, percent: float) -> pd.DataFrame:
    """
    DataFrame me ek naya tax column add karo
    Example: add_tax_column(df, 'price', 18) → 'price_with_tax' column add hoga
    """
    df[f"{column}_with_tax"] = df[column].apply(
        lambda x: float(BharatNum(x).tax(percent))
    )
    return df


def add_discount_column(df: pd.DataFrame, column: str, percent: float) -> pd.DataFrame:
    """
    DataFrame me ek naya discount column add karo
    Example: add_discount_column(df, 'price', 10) → 'price_after_discount' column add hoga
    """
    df[f"{column}_after_discount"] = df[column].apply(
        lambda x: float(BharatNum(x).discount(percent))
    )
    return df