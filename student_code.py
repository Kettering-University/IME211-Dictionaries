# Homework Assignment: Managing Inventory with Dictionaries

# ----------------------------------------------------
# region Introduction
# ----------------------------------------------------
# In this assignment, you will apply your knowledge of dictionaries to manage an inventory system.
# This scenario is common in industrial engineering, where efficient inventory management is crucial.

# ----------------------------------------------------
# region Setup
# ----------------------------------------------------
# The inventory for a small hardware store is provided as a dictionary.
# Manipulate the inventory directly (do not create a new dictionary variable)
# Each key is a product name, and the value is another dictionary containing the quantity and price per unit.

inventory = {
    "bolts": {"quantity": 100, "price_per_unit": 0.05},
    "nuts": {"quantity": 150, "price_per_unit": 0.04},
    "washers": {"quantity": 200, "price_per_unit": 0.03}
}


# Your first task is to perform an audit of the inventory.
# Print the total quantity of items in the inventory.
# Your code here:


# A new shipment has arrived. Update the inventory with the following items:
# - Add 50 bolts.
# - Add 100 nuts.
# - Add 150 washers.
# Your code here:


# The store has decided to start selling screws. Add "screws" to the inventory with a quantity of 300 and a price per unit of 0.06.
# Your code here:

# Due to supplier price changes, update the price per unit as follows:
# - Bolts: Increase by 1 cent.
# - Nuts: Decrease by 1 cent.
# - Washers: No change.
# - Screws: Increase by 2 cents.
# Your code here:

# The store has decided to discontinue selling washers. Remove them from the inventory.
# Your code here:

