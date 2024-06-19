import sys
import student_code as sc

# Correct inventory defined at the top of the script
correct_inventory = {
    "bolts": {"quantity": 100, "price_per_unit": 0.05},
    "nuts": {"quantity": 150, "price_per_unit": 0.04},
    "washers": {"quantity": 200, "price_per_unit": 0.03}
}
correct_inventory["bolts"]["quantity"] += 50
correct_inventory["nuts"]["quantity"] += 100
correct_inventory["washers"]["quantity"] += 150
correct_inventory.update({"screws": {"quantity": 300, "price_per_unit": 0.06}})
correct_inventory["bolts"]["price_per_unit"] += 0.01
correct_inventory["nuts"]["price_per_unit"] -= 0.01
correct_inventory["screws"]["price_per_unit"] += 0.02
del correct_inventory["washers"]


def grade_homework():
    try:
        # Calculating total quantity from the student's inventory
        student_total_quantity = sum(item['quantity'] for item in sc.inventory.values())
        # Calculating total price from the student's inventory
        student_total_price = sum(item['quantity'] * item['price_per_unit'] for item in sc.inventory.values())

        # Calculating the correct total quantity
        correct_total_quantity = sum(item['quantity'] for item in correct_inventory.values())
        # Calculating the correct total price
        correct_total_price = sum(item['quantity'] * item['price_per_unit'] for item in correct_inventory.values())

        # Comparing student's totals with the correct totals
        if student_total_quantity != correct_total_quantity:
            print("The total quantity of items in the inventory does not match the expected total.")
            return False  # Fail if the total quantity does not match

        if student_total_price != correct_total_price:
            print("The total price of items in the inventory does not match the expected total.")
            return False  # Fail if the total price does not match

    except Exception as e:
        print(f"Error during grading: {e}")
        return False  # Fail on encountering any error

    return True  # Pass if all checks are correct


# Execute the grading function
if grade_homework():
    sys.exit(0)  # Pass with exit code 0
else:
    sys.exit(1)  # Fail with exit code 1
