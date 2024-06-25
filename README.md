# Python CRUD Application for Yellow Pages

A comprehensive Python application for managing Business Listing data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the digital directory industry, specifically addressing the need to manage business listing data efficiently. A business listing typically includes information about specific business such as name, category, contact information, and location. This information plays a significant role in connecting businesses with consumers or businesses alike to relevant services or products in their area.

**Benefits:**

* Centralized database making it easy to access and manage. Contacts are organized in a structured format, ensuring consistency and ease of use.
* Quick access to contact information and automates the processes of adding, updating, and deleting contacts, reducing manual effort and errors.
* User-friendly interface, provides clear prompts for each CRUD operation and includes error handling to guide users and prevent incorrect operations.
* Scalability to handle a growing number of listings and user interactions. Can be easily expanded or integrated with other systems to accommodate growing needs.
* The program can be customized with additional fields and functionalities, and its settings can be configured to suit various use cases and preferences.


**Target Users:**

This application is designed for consumers, investor, and business partners to facilitate their search and connection with other businesses. It aims to streamline the tasks of finding, contacting, and exploring information related to various businesses listed in the Yellow Pages directory.

## Features

* **Create:**
    * Add new business listing entries with essential details like business code as primary key, name, phone number, website, industry, and location
    * Implement validation rules to ensure data integrity using unique identifiers and data type checks.
* **Read:**
    * Search and retrieve specific business listing records by applying filters based on business code.
    * Display comprehensive information for each business listing in a user-friendly format.
* **Update:**
    * Modify existing business listing data to reflect changes in relevant details.
    * Provide clear confirmation or error messages based on update success or failure.
* **Delete:**
    * Allow for the removal of unwanted business listing records with appropriate authorization checks.

## Installation

1. **Prerequisites:**
    * Python version 3.12.3

2. **Installation:**
    ```bash
    git clone [https://github.com/](https://github.com/)DindaSularyono/Yellow_Pages_Python_CRUD.git
    cd Yellow_Pages_Python_CRUD
    ```


## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new business record, providing details like name, phone, website, industry, address. 
    * **Read:** Search and retrieve business information by business code or other relevant criteria.
    * **Update:** Modify business details, such as updating their address or contact details.
    * **Delete:** Remove a business record from the system with appropriate authorization.

## Data Model
Represent contact data in the Yellow Pages CRUD Program. The following fields are typically stored:
Code: (String, Primary Key) - A unique identifier for each business.
Name: (String) - The name of the business.
Phone Number: (String) - The primary phone number for the business.
Email: (String) - The email address of the business.
Address: (String) - The physical address of the business.
These fields are designed to capture all necessary information for each business, ensuring comprehensive and organized data management within the Yellow Pages CRUD Program.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to [your_email] or submit an issue if you encounter any problems or have suggestions for improvements.


