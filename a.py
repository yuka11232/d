class CurrencyConverter:
    def __init__(self, sell_rate_usd):
        self.sell_rate_usd = sell_rate_usd

    def azn_to_usd(self, amount_azn):
        if amount_azn < 0:
            raise ValueError("the amount cannot be negative.")
        return amount_azn / self.sell_rate_usd

if __name__ == "__main__":
   
    sell_rate_usd = 1.7020

    converter = CurrencyConverter(sell_rate_usd)

    try:
        amount_azn = float(input("enter the amount in AZN: "))
        amount_usd = converter.azn_to_usd(amount_azn)
        print(f"{amount_azn:.2f} AZN is equal to {amount_usd:.2f} USD.")
    except ValueError as e:
        print(f"error: {e}")
    except Exception as e:
        print(f"error: {e}")
