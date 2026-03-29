# Contact Search System
# Using doubly linked lists and hash tables

class Contact:
    # represents a contact
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def __str__(self):
        return f"{self.name} - {self.phone}"


class Node:
    def __init__(self, contact):
        self.contact = contact
        self.prev = None
        self.next = None


class DoublyLinkedList:
    # doubly linked list for storing contacts
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, contact):
        new_node = Node(contact)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def display_forward(self):
        # get all contacts forward
        contacts = []
        current = self.head
        while current:
            contacts.append(current.contact)
            current = current.next
        return contacts
    
    def display_backward(self):
        # get all contacts in reverse
        contacts = []
        current = self.tail
        while current:
            contacts.append(current.contact)
            current = current.prev
        return contacts


class SubstringMatcher:
    # basic substring search
    @staticmethod
    def naive_search(text, pattern):
        # simple substring matching - case insensitive
        text = text.lower()
        pattern = pattern.lower()
        
        if len(pattern) == 0:
            return True
        
        for i in range(len(text) - len(pattern) + 1):
            if text[i:i + len(pattern)] == pattern:
                return True
        return False


class ContactSystem:
    # main system for managing contacts
    def __init__(self):
        self.contacts_list = DoublyLinkedList()
        self.contacts_dict = {}  # for fast lookup
        self.matcher = SubstringMatcher()
    
    def add_contact(self, name, phone):
        # add new contact
        if name in self.contacts_dict:
            print(f"Error: Contact '{name}' already exists.")
            return False
        
        contact = Contact(name, phone)
        self.contacts_list.add(contact)
        self.contacts_dict[name] = contact
        print("Contact added.")
        return True
    
    def search_by_keyword(self, keyword):
        # search by keyword substring
        matches = []
        for contact in self.contacts_list.display_forward():
            if self.matcher.naive_search(contact.name, keyword):
                matches.append(contact)
        return matches
    
    def search_by_name(self, name):
        # lookup by exact name
        return self.contacts_dict.get(name, None)
    
    def display_all_forward(self):
        return self.contacts_list.display_forward()
    
    def display_all_backward(self):
        return self.contacts_list.display_backward()


def print_menu():
    print("\n" + "="*40)
    print("1. Add Contact")
    print("2. Search by Keyword")
    print("3. Search by Exact Name")
    print("4. View All (Forward)")
    print("5. View All (Backward)")
    print("6. Exit")
    print("="*40)


def main():
    system = ContactSystem()
    
    while True:
        print_menu()
        option = input("\nEnter option: ").strip()
        
        if option == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                system.add_contact(name, phone)
            else:
                print("Name and phone needed")
        
        elif option == "2":
            keyword = input("Search keyword: ").strip()
            matches = system.search_by_keyword(keyword)
            if matches:
                print(f"\nFound {len(matches)} matches:")
                for contact in matches:
                    print(f"  - {contact}")
            else:
                print("No matches")
        
        elif option == "3":
            name = input("Enter name: ").strip()
            contact = system.search_by_name(name)
            if contact:
                print(f"Found: {contact}")
            else:
                print("Not found")
        
        elif option == "4":
            contacts = system.display_all_forward()
            if contacts:
                print("\nContacts (Forward):")
                for i, contact in enumerate(contacts, 1):
                    print(f"  {i}. {contact}")
            else:
                print("No contacts")
        
        elif option == "5":
            contacts = system.display_all_backward()
            if contacts:
                print("\nContacts (Backward):")
                for i, contact in enumerate(contacts, 1):
                    print(f"  {i}. {contact}")
            else:
                print("No contacts")
        
        elif option == "6":
            print("Bye!")
            break
        
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
