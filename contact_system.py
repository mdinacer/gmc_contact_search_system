"""
Contact Search System
A system to manage contacts using doubly linked lists and hash tables
"""


class Contact:
    """Represents a single contact with name and phone number"""
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def __str__(self):
        return f"{self.name} - {self.phone}"


class Node:
    """Node for doubly linked list"""
    
    def __init__(self, contact):
        self.contact = contact
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Doubly linked list to store contacts in insertion order"""
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, contact):
        """Add a contact to the end of the list"""
        new_node = Node(contact)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def display_forward(self):
        """Display all contacts from head to tail"""
        contacts = []
        current = self.head
        while current:
            contacts.append(current.contact)
            current = current.next
        return contacts
    
    def display_backward(self):
        """Display all contacts from tail to head"""
        contacts = []
        current = self.tail
        while current:
            contacts.append(current.contact)
            current = current.prev
        return contacts


class SubstringMatcher:
    """Implements naive substring search algorithm"""
    
    @staticmethod
    def naive_search(text, pattern):
        """
        Naive substring search algorithm
        Returns True if pattern is found in text (case-insensitive)
        """
        text = text.lower()
        pattern = pattern.lower()
        
        if len(pattern) == 0:
            return True
        
        for i in range(len(text) - len(pattern) + 1):
            if text[i:i + len(pattern)] == pattern:
                return True
        return False


class ContactSystem:
    """Main contact management system"""
    
    def __init__(self):
        self.contacts_list = DoublyLinkedList()
        self.contacts_dict = {}  # Hash table: name -> contact
        self.matcher = SubstringMatcher()
    
    def add_contact(self, name, phone):
        """Add a new contact to both list and hash table"""
        if name in self.contacts_dict:
            print(f"Error: Contact '{name}' already exists.")
            return
        
        contact = Contact(name, phone)
        self.contacts_list.add(contact)
        self.contacts_dict[name] = contact
        print("Contact added.")
    
    def search_by_keyword(self, keyword):
        """Search for contacts by substring matching"""
        matches = []
        for contact in self.contacts_list.display_forward():
            if self.matcher.naive_search(contact.name, keyword):
                matches.append(contact)
        return matches
    
    def search_by_name(self, name):
        """Search for a contact by exact name using hash table"""
        if name in self.contacts_dict:
            return self.contacts_dict[name]
        return None
    
    def display_all_forward(self):
        """Display all contacts in forward order"""
        return self.contacts_list.display_forward()
    
    def display_all_backward(self):
        """Display all contacts in backward order"""
        return self.contacts_list.display_backward()


def print_menu():
    """Print the main menu"""
    print("\n" + "="*40)
    print("1. Add Contact")
    print("2. Search by Keyword")
    print("3. Search by Exact Name")
    print("4. View All (Forward)")
    print("5. View All (Backward)")
    print("6. Exit")
    print("="*40)


def main():
    """Main function to run the contact system"""
    system = ContactSystem()
    
    while True:
        print_menu()
        option = input("\nEnter option: ").strip()
        
        if option == "1":
            # Add Contact
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                system.add_contact(name, phone)
            else:
                print("Error: Name and phone cannot be empty.")
        
        elif option == "2":
            # Search by Keyword
            keyword = input("Search keyword: ").strip()
            matches = system.search_by_keyword(keyword)
            if matches:
                print(f"\nMatches found ({len(matches)}):")
                for contact in matches:
                    print(f"  Match found: {contact}")
            else:
                print(f"No matches found for '{keyword}'.")
        
        elif option == "3":
            # Search by Exact Name
            name = input("Enter name: ").strip()
            contact = system.search_by_name(name)
            if contact:
                print(f"Match found: {contact}")
            else:
                print(f"Contact '{name}' not found.")
        
        elif option == "4":
            # View All (Forward)
            contacts = system.display_all_forward()
            if contacts:
                print("\nAll Contacts (Forward):")
                for i, contact in enumerate(contacts, 1):
                    print(f"  {i}. {contact}")
            else:
                print("No contacts yet.")
        
        elif option == "5":
            # View All (Backward)
            contacts = system.display_all_backward()
            if contacts:
                print("\nAll Contacts (Backward):")
                for i, contact in enumerate(contacts, 1):
                    print(f"  {i}. {contact}")
            else:
                print("No contacts yet.")
        
        elif option == "6":
            # Exit
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
