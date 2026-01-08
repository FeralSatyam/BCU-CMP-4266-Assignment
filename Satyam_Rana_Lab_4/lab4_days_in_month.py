import lab4_library

def days_in_month(month: int, year: int):
    days = lab4_library.get_days_of_month(month, year)
    if days == -1:
        print(f"Error: {month} is not a valid month.")
    else:
        print(f"Month {month} of year {year} has {days} days.")

# Example usage:
if __name__ == "__main__":
    days_in_month(2, 2024) 
    days_in_month(2, 2023)   
    days_in_month(11, 2025) 
    days_in_month(13, 2025)  