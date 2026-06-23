from __future__ import annotations
from bharatnum.words import number_to_words
from bharatnum.helpers import FinancialHelpers


class BharatNum(FinancialHelpers):
    """
    BharatNum - Indian Number & Currency Datatype
    Supports Indian formatting, lakh/crore conversion,
    arithmetic operations, and more.
    """

    def __init__(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError(f"BharatNum expects int or float, got {type(value).__name__}")
        self._value = float(value)

    # ─── Core Properties ───────────────────────────────

    @property
    def value(self) -> float:
        return self._value

    @property
    def lakh(self) -> float:
        return round(self._value / 1_00_000, 4)

    @property
    def crore(self) -> float:
        return round(self._value / 1_00_00_000, 4)
    
    @property
    def words(self) -> str:
        return number_to_words(self._value)

    # ─── Formatting ────────────────────────────────────

    def _indian_format(self) -> str:
        """Convert number to Indian comma format: 1,50,000"""
        num = int(self._value)
        is_negative = num < 0
        num = abs(num)
        s = str(num)

        # Last 3 digits alag, baaki 2-2 me
        if len(s) <= 3:
            result = s
        else:
            result = s[-3:]
            s = s[:-3]
            while s:
                result = s[-2:] + "," + result
                s = s[:-2]

        decimal = f"{self._value:.2f}".split(".")[1]
        result = f"₹{'-' if is_negative else ''}{result}.{decimal}"
        return result

    # ─── String Representation ─────────────────────────

    def __str__(self) -> str:
        return self._indian_format()

    def __repr__(self) -> str:
        return f"BharatNum({self._value})"

    # ─── Arithmetic Operations ─────────────────────────

    def __add__(self, other) -> BharatNum:
        if isinstance(other, BharatNum):
            return BharatNum(self._value + other._value)
        if isinstance(other, (int, float)):
            return BharatNum(self._value + other)
        return NotImplemented

    def __sub__(self, other) -> BharatNum:
        if isinstance(other, BharatNum):
            return BharatNum(self._value - other._value)
        if isinstance(other, (int, float)):
            return BharatNum(self._value - other)
        return NotImplemented

    def __mul__(self, other) -> BharatNum:
        if isinstance(other, (int, float)):
            return BharatNum(self._value * other)
        return NotImplemented

    def __truediv__(self, other) -> BharatNum:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("BharatNum: Division by zero")
            return BharatNum(self._value / other)
        return NotImplemented

    def __neg__(self) -> BharatNum:
        return BharatNum(-self._value)

    def __abs__(self) -> BharatNum:
        return BharatNum(abs(self._value))

    # ─── Comparison Operations ─────────────────────────

    def __eq__(self, other) -> bool:
        if isinstance(other, BharatNum):
            return self._value == other._value
        if isinstance(other, (int, float)):
            return self._value == other
        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, BharatNum):
            return self._value < other._value
        if isinstance(other, (int, float)):
            return self._value < other
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, BharatNum):
            return self._value > other._value
        if isinstance(other, (int, float)):
            return self._value > other
        return NotImplemented

    def __le__(self, other) -> bool:
        return self._value <= (other._value if isinstance(other, BharatNum) else other)

    def __ge__(self, other) -> bool:
        return self._value >= (other._value if isinstance(other, BharatNum) else other)

    # ─── Type Conversion ───────────────────────────────

    def __int__(self) -> int:
        return int(self._value)

    def __float__(self) -> float:
        return self._value
    

if __name__ == "__main__":
    r1 = BharatNum(2500000)
    r2 = BharatNum(500000)

    print(r1)           # ₹25,00,000.00
    print(r2)           # ₹5,00,000.00
    print(r1 + r2)      # ₹30,00,000.00
    print(r1 - r2)      # ₹20,00,000.00
    print(r1 * 2)       # ₹50,00,000.00
    print(r1.lakh)      # 25.0
    print(r1.crore)     # 0.25
    print(r1 > r2)      # True