# ─── Basic Building Blocks ───────────────────────────

ONES = [
    "", "One", "Two", "Three", "Four", "Five",
    "Six", "Seven", "Eight", "Nine", "Ten",
    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
    "Sixteen", "Seventeen", "Eighteen", "Nineteen"
]

TENS = [
    "", "", "Twenty", "Thirty", "Forty", "Fifty",
    "Sixty", "Seventy", "Eighty", "Ninety"
]

# ─── Core Helper: 0-999 tak words ────────────────────

def _below_thousand(n: int) -> str:
    """
    0 se 999 tak ka number words me convert karo
    Example: 150 → "One Hundred Fifty"
    """
    if n == 0:
        return ""

    result = ""

    # Hundred handle karo
    if n >= 100:
        result += ONES[n // 100] + " Hundred "
        n = n % 100

    # 1-19 directly ONES se
    if n < 20:
        result += ONES[n]

    # 20-99 TENS + ONES se
    else:
        result += TENS[n // 10]
        if n % 10 != 0:
            result += " " + ONES[n % 10]

    return result.strip()


# ─── Main Function: Indian System ────────────────────

def number_to_words(n: float) -> str:
    """
    Indian number system me words convert karo
    Example:
        2500000   → "Twenty Five Lakh"
        150000    → "One Lakh Fifty Thousand"
        25000000  → "Two Crore Fifty Lakh"
    """

    # Negative handle karo
    if n < 0:
        return "Minus " + number_to_words(-n)

    n = int(n)

    # Zero special case
    if n == 0:
        return "Zero"

    result = ""

    # Crore (1,00,00,000)
    if n >= 1_00_00_000:
        crore_part = n // 1_00_00_000
        result += _below_thousand(crore_part) + " Crore "
        n = n % 1_00_00_000

    # Lakh (1,00,000)
    if n >= 1_00_000:
        lakh_part = n // 1_00_000
        result += _below_thousand(lakh_part) + " Lakh "
        n = n % 1_00_000

    # Thousand (1,000)
    if n >= 1_000:
        thousand_part = n // 1_000
        result += _below_thousand(thousand_part) + " Thousand "
        n = n % 1_000

    # Remaining (0-999)
    if n > 0:
        result += _below_thousand(n)

    return result.strip()


if __name__ == "__main__":
    print(number_to_words(2500000))   # Twenty Five Lakh
    print(number_to_words(150000))    # One Lakh Fifty Thousand
    print(number_to_words(25000000))  # Two Crore Fifty Lakh
    print(number_to_words(5500))      # Five Thousand Five Hundred
    print(number_to_words(999))       # Nine Hundred Ninety Nine
    print(number_to_words(0))         # Zero
    print(number_to_words(-5000))     # Minus Five Thousand