
import math


def parse_booking(text):
    if not isinstance(text, str) or text.count(":") != 1:
        return None

    pet, days = text.split(":")
    pet = pet.strip()

    if not pet:
        return None

    try:
        days = float(days)
    except ValueError:
        return None

    if not math.isfinite(days) or days <= 0:
        return None

    return pet.title(), days


def stay_average(days_csv):
    if not isinstance(days_csv, str) or not days_csv.strip():
        return 0

    try:
        values = [int(r.strip()) for r in days_csv.split(",")]
    except ValueError:
        return 0

    if not values or any(value < 0 for value in values):
        return 0

    return sum(values) / len(values)


def payable_fee(text):
    if not isinstance(text, str) or text.count("|") != 1:
        return 0.0

    fee, discount = text.split("|")

    try:
        fee = float(fee)
        discount = float(discount)
    except ValueError:
        return 0.0

    if not all(math.isfinite(x) for x in (fee, discount)):
        return 0.0

    if fee < 0 or discount < 0:
        return 0.0

    total = fee * 1.18 - discount
    return max(total, 0.0)


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter pet:days (e.g. dog:5): ")
    result = parse_booking(user_input)
    print("Pet and Days:", result)

    print("\n==== Running stay_average ====")
    user_input = input("Enter stay lengths in days as CSV (e.g. 2,5,7): ")
    result = stay_average(user_input)
    print("Average Stay:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 1500|100): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result)


if __name__ == "__main__":
    main()
