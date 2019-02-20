# Calculates the cost of normal ground shipping given weight
def ground_shipping(weight):
    if weight <= 2:
        cost = weight * 1.5 + 20
        return cost
    elif weight <= 6:
        cost = weight * 3.00 + 20
        return cost
    elif weight <= 10:
        cost = weight * 4.00 + 20
        return cost
    else:
        cost = weight * 4.75 + 20
        return cost

# Cost of premium ground shipping is independent of weight
prem_ground_shipping = 125.00

# Calculates the cost of drone shipping given weight
def drone_shipping (weight):
    if weight <= 2:
        cost = weight * 4.5
        return cost
    elif weight <= 6:
        cost = weight * 9.00
        return cost
    elif weight <= 10:
        cost = weight * 12.00
        return cost
    else:
        cost = weight * 14.25
        return cost

# Compares the cost of each shipping method and prints the cheapest method and how much it costs
def cheapest_shipping(weight):
    if (drone_shipping(weight) < prem_ground_shipping) and (drone_shipping(weight) < ground_shipping(weight)):
        print("You should ship using drone shipping, it will cost $" + str(drone_shipping(weight)))
    elif ground_shipping(weight) < prem_ground_shipping:
        print("You should ship using ground shipping, it will cost $" + str(ground_shipping(weight)))
    else:
        print("You should ship using premium ground shipping, it will cost $" + str(prem_ground_shipping))
