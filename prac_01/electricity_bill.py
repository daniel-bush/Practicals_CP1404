TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")

# price_per_kwh = int(input("Enter cents per kWh: "))
tariff = int(input("Which tariff? 11 or 31: "))
while tariff != 11 and tariff != 31:
    print("Invalid!")
    tariff = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

if tariff == 11:
    estimated_bill = (TARIFF_11 * daily_use * billing_days)
else:
    estimated_bill = (TARIFF_31 * daily_use * billing_days)

print("Estimated bill: ${:.2f}".format(estimated_bill))
