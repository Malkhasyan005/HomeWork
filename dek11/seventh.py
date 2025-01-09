def book_ticket(destination, price, discount=0, *extras, **details):
    print(f"Booking to {destination} for ${price - discount}")
    if extras:
        print(f"Extras: {', '.join(extras)}")
    if details:
        print(f"Details: {details}")

book_ticket("Paris", 10, 100, "window seat", "meal")

