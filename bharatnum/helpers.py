from __future__ import annotations

class FinancialHelpers:
    """
    BharatNum ke liye financial helper methods
    Tax, GST, Discount, EMI, Split sab yahan hain
    """

    # ─── Tax & GST ─────────────────────────────────────

    def tax(self, percent: float):
        """
        Tax add karke naya amount return karo
        Example: salary.tax(18) → 18% GST add karega
        """
        tax_amount = self._value * percent / 100
        return self.__class__(self._value + tax_amount)

    def tax_amount(self, percent: float):
        """
        Sirf tax ka amount return karo (total nahi)
        Example: price.tax_amount(18) → sirf GST kitna hua
        """
        return self.__class__(self._value * percent / 100)

    def remove_tax(self, percent: float):
        """
        Tax inclusive price se original price nikalo
        Example: agar 118 rupye me 18% GST included hai
        toh original price kya thi?
        """
        original = self._value / (1 + percent / 100)
        return self.__class__(round(original, 2))

    # ─── Discount ──────────────────────────────────────

    def discount(self, percent: float):
        """
        Discount apply karke final price return karo
        Example: price.discount(10) → 10% off
        """
        discount_amount = self._value * percent / 100
        return self.__class__(self._value - discount_amount)

    def discount_amount(self, percent: float):
        """
        Sirf discount ka amount return karo
        Example: price.discount_amount(10) → kitna discount mila
        """
        return self.__class__(self._value * percent / 100)

    # ─── Split ─────────────────────────────────────────

    def split(self, n: int):
        """
        Amount ko n logo me barabar baant do
        Example: bill.split(4) → 4 logo me divide
        """
        if n <= 0:
            raise ValueError("Split count must be greater than 0")
        return self.__class__(round(self._value / n, 2))

    # ─── Percentage ────────────────────────────────────

    def percentage_of(self, percent: float):
        """
        Amount ka X% nikalo
        Example: salary.percentage_of(20) → salary ka 20%
        """
        return self.__class__(self._value * percent / 100)

    def percent_change(self, other) -> float:
        """
        Do amounts ke beech percentage change nikalo
        Example: old_salary.percent_change(new_salary)
        """
        if self._value == 0:
            raise ZeroDivisionError("Cannot calculate percent change from zero")
        return round(((other._value - self._value) / self._value) * 100, 2)

    # ─── EMI Calculator ────────────────────────────────

    def emi(self, rate: float, months: int):
        """
        Loan ka monthly EMI calculate karo
        rate = annual interest rate (%)
        months = loan duration in months

        Example: loan.emi(8.5, 24) → 8.5% rate pe 24 months ka EMI
        """
        if rate == 0:
            return self.__class__(round(self._value / months, 2))

        monthly_rate = rate / (12 * 100)
        emi_amount = (self._value * monthly_rate * (1 + monthly_rate) ** months) / \
                     ((1 + monthly_rate) ** months - 1)
        return self.__class__(round(emi_amount, 2))