class NATTable:
    def __init__(self):
        self.table = {}

    def add_mapping(self, internal_ip, translated_ip):
        self.table[internal_ip] = translated_ip
        print(f"Mapping added: {internal_ip} -> {translated_ip}")

    def remove_mapping(self, internal_ip):
        if internal_ip in self.table:
            del self.table[internal_ip]
            print(f"Mapping removed: {internal_ip}")
        else:
            print(f"No mapping found for {internal_ip}")

    def get_mapping(self, internal_ip):
        translated_ip = self.table.get(internal_ip, "Not Found")
        print(f"Translated IP for {internal_ip}: {translated_ip}")

    def display_table(self):
        print("\nNAT Table:")
        print("Internal IP\tTranslated IP")
        for internal_ip, translated_ip in self.table.items():
            print(f"{internal_ip}\t\t{translated_ip}")

def main():
    nat_table = NATTable()

    while True:
        print("\n1. Add Mapping\n2. Remove Mapping\n3. Get Mapping\n4. Display Table\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            internal_ip = input("Enter internal IP: ")
            translated_ip = input("Enter translated IP: ")
            nat_table.add_mapping(internal_ip, translated_ip)

        elif choice == "2":
            internal_ip = input("Enter internal IP to remove mapping: ")
            nat_table.remove_mapping(internal_ip)

        elif choice == "3":
            internal_ip = input("Enter internal IP to get mapping: ")
            nat_table.get_mapping(internal_ip)

        elif choice == "4":
            nat_table.display_table()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
