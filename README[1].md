# Hotel Room Booking System 🏨

A Python 3 console-based application to manage hotel room reservations, built as a solution for Problem Statement No. 59. The system handles room availability, booking generation, tax (GST) calculation, and persistent storage using file handling.

## Features
- **View Available Rooms:** Dynamically checks and displays rooms that are not currently booked.
- **Book a Room:** Accepts guest details, validates room existence and availability, and enforces a 1-30 night limit.
- **Cancel Booking:** Frees up a room and securely updates the database.
- **Automated Billing:** Automatically calculates the base rate and applies a 12% GST to the final bill.
- **Persistent Storage:** Uses JSON file handling (`my_bookings.txt`) to save and retrieve active bookings across sessions.

## Technologies & Concepts Used
- **Language:** Python 3
- **Data Structures:** Dictionaries (for room catalog) and Lists (for active bookings).
- **Core Concepts:** Functions, Exception Handling (`ValueError`), and File Handling (`os` and `json` modules).

## How to Run
1. Clone the repository to your local machine.
2. Ensure you have Python 3 installed.
3. Open a terminal in the project directory and run:
   ```bash
   python main.py
   ```
