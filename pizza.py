def make_pizza(size, *toppings):
    """Summarize the izza we are about to make."""
    print(f"\n Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")