def search_phone_number():
    # Dictionary with tuples as keys and phone numbers as values
    phonebook = {
        ("safi", "khan"): "012345",
        ("khan", "safi"): "67890",
    }

    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()

    search_key = (first_name, last_name)

    # Searching in the dictionary
    if search_key in phonebook:
        print("Phone Number:" + phonebook[search_key])
    else:
        print("Name not found in record.")

# Run the function
search_phone_number()
