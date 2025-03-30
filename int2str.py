from colorama import init, Fore, Style

# Activate colors in the terminal
init()

def number_to_words(n: float) -> str:
    is_negative = n < 0
    if is_negative:
        n = abs(n)

    if n > 999_999_999_999:
        return "Tal uden for rækkevidde"

    ones = [
        "nul", "en", "to", "tre", "fire", "fem",
        "seks", "syv", "otte", "ni", "ti", "elleve",
        "tolv", "tretten", "fjorten", "femten",
        "seksten", "sytten", "atten", "nitten"
    ]

    tens = [
        "", "", "tyve", "tredive", "fyrre", "halvtreds",
        "tres", "halvfjerds", "firs", "halvfems"
    ]

    scale_data = [
        ("", ""),
        ("et tusind", " tusind"),
        ("en million", " millioner"),
        ("en milliard", " milliarder")
    ]

    def under_hundred(n):
        if n < 20:
            return ones[n]
        unit = n % 10
        ten = n // 10
        return f"{ones[unit]}og{tens[ten]}" if unit else tens[ten]

    def under_thousand(n):
        if n < 100:
            return under_hundred(n)
        h = n // 100
        rest = n % 100
        hundred_text = "et hundrede" if h == 1 else f"{ones[h]} hundrede"
        return f"{hundred_text} og {under_hundred(rest)}" if rest else hundred_text

    def convert_integer_part(n):
        if n == 0:
            return "nul"

        parts = []
        for group, (singular, plural) in enumerate(scale_data):
            chunk = n % 1000
            if chunk:
                if group == 0:
                    text = under_thousand(chunk)
                elif group == 1 and chunk == 1:
                    text = singular
                else:
                    text = under_thousand(chunk) + (plural if chunk > 1 else f" {singular.strip()}")
                parts.insert(0, text)
            n //= 1000
            if n == 0:
                break

        return ", ".join(parts)

    # Split into kroner and ører
    total_ore = int(round(n * 100))
    kroner, ore = divmod(total_ore, 100)

    kroner_text = f"{convert_integer_part(kroner)} kroner"
    ore_text = f"{under_hundred(ore)} ører" if ore else ""

    result = f"{kroner_text} og {ore_text}" if ore else kroner_text
    return f"minus {result}" if is_negative else result


# User input loop
while True:
    try:
        user_input = input("\nIndtast et beløb (fx 822,25)\n(eller skriv 'exit' for at afslutte): ")
        if user_input.lower() == 'exit':
            print("Afslutter programmet.")
            break

        cleaned_input = user_input.replace(",", ".")
        number = float(cleaned_input)
        result = number_to_words(number)

        # Colored output
        farvet_resultat = (Fore.RED if number < 0 else Fore.GREEN) + result + Style.RESET_ALL
        print(f"\n\n Beløbet {user_input} \n er {farvet_resultat}")

    except ValueError:
        print("Fejl: Ugyldigt talformat – prøv igen.")
