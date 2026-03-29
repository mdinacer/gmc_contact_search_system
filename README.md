# Contact Search System

A Python-based contact management system that leverages data structures like doubly linked lists and hash tables for efficient contact storage and retrieval.

## Features

- **Contact Management**: Add and manage contacts with names and phone numbers
- **Doubly Linked List**: Store contacts in insertion order with bidirectional traversal capabilities
- **Hash Table**: Fast O(1) lookup of contacts by name
- **Substring Search**: Find contacts using naive substring matching algorithm (case-insensitive)
- **Bidirectional Display**: View contacts in forward or reverse order

## Core Components

### Contact
Represents a single contact with a name and phone number.

### DoublyLinkedList
Stores contacts in insertion order, supporting:
- Forward traversal (head to tail)
- Backward traversal (tail to head)
- O(1) insertion at the end

### SubstringMatcher
Implements naive substring search algorithm for finding contacts by name pattern.

### ContactSystem
Main system class that coordinates contact management using both the doubly linked list and hash table data structures.

## Files

- `contact_system.py` - Main implementation file containing all classes and functionality
- `public/` - Public assets directory
- `src/` - Source files directory
  - `assets/` - Asset files

## Usage

```python
# Create a contact system
system = ContactSystem()

# Add contacts
system.add_contact("John Doe", "555-1234")
system.add_contact("Jane Smith", "555-5678")

# Search for contacts
system.search_by_name("John")

# Display all contacts
system.list_contacts()
```

## Data Structures

- **Doubly Linked List**: Maintains insertion order and allows traversal in both directions
- **Hash Table (Dictionary)**: Provides O(1) lookup by contact name for quick access

## Algorithm

- **Substring Search**: Uses naive string matching with O(n*m) complexity, where n is the text length and m is the pattern length

## Getting Started

1. Clone the repository
2. Ensure Python 3.x is installed
3. Run the main contact system file

## License

Open source project

## Author

GMC Contact Search System
