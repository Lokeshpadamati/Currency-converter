import requests

# Replace with your own ExchangeRate-API key
API_KEY = "1517f02a0379a3ea46a00f58"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def get_exchange_rate(base_currency):
    """Fetch exchange rates for the base currency"""
    try:
        response = requests.get(BASE_URL + base_currency.upper())
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rates']
        else:
            print("Error fetching exchange rates:", data.get('error-type', 'Unknown error'))
            return None
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None

def convert_currency(amount, rate):
    """Convert the amount using the exchange rate"""
    try:
        return amount * rate
    except TypeError:
        print("Invalid conversion")
        return None

def main():
    print("Welcome to the Python Currency Converter!")
    while True:
        base_currency = input("\nEnter base currency (e.g., USD, EUR) or 'exit' to quit: ").strip()
        if base_currency.lower() == 'exit':
            print("Thank you for using the converter!")
            break

        rates = get_exchange_rate(base_currency)
        if not rates:
            continue

        target_currency = input("Enter target currency (e.g., INR, GBP): ").strip().upper()
        if target_currency not in rates:
            print(f"Currency '{target_currency}' not supported. Try again.")
            continue

        try:
            amount = float(input(f"Enter amount in {base_currency.upper()}: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        converted_amount = convert_currency(amount, rates[target_currency])
        if converted_amount is not None:
            print(f"{amount} {base_currency.upper()} = {converted_amount:.2f} {target_currency}")

        cont = input("\nDo you want to perform another conversion? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
