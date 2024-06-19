# Introduction to Dictionaries

# ----------------------------------------------------
# region Creating Dictionaries
# ----------------------------------------------------
# Dictionaries in Python are collections of key-value pairs.
# They are created using curly braces {} with keys and values separated by colons.
# Keys must be unique and immutable (e.g., strings, numbers, tuples).

# Example: Creating a Simple Dictionary
employee = {
    "name": "John Doe",
    "age": 30,
    "department": "Engineering"
}

# ----------------------------------------------------
# region Accessing Dictionary Elements
# ----------------------------------------------------
# Values in a dictionary can be accessed using square brackets [] with the key.
# Attempting to access a non-existent key will raise a KeyError.

# Example: Accessing Elements


# Handling Missing Keys
# To avoid KeyError, use the get() method which returns None if the key is not found.


# ----------------------------------------------------
# region Modifying Dictionaries
# ----------------------------------------------------
# You can add new key-value pairs, update values, or delete key-value pairs from a dictionary.

# Adding a New Key-Value Pair


# Updating an Existing Value


# Deleting a Key-Value Pair


# Example: Updated Dictionary


# endregion

# ----------------------------------------------------
# region Student Activity: Working with Dictionaries
# ----------------------------------------------------
# Given the following dictionary representing a product in inventory, perform the specified tasks below.

product_info = {
    "product_id": 112233,
    "name": "Wireless Mouse",
    "quantity": 150,
    "price": 29.99
}

# TODO: Activity 1 - Using Dictionaries
# First, access the price of the product from the dictionary and print it out.
# Next, the inventory received an additional 50 units of the wireless mouse. Update the quantity in the dictionary.
# The product is on sale. Add a new key-value pair to indicate the sale status of the product ("on_sale": True).
# Due to a pricing update, remove the price key from the dictionary temporarily.
# Your code here:


# endregion
