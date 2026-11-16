# Project Report: Hotel Room Booking System

**Problem Statement No:** 59
**Developer:** K Tejas Rao
**Course/University:** B.Tech CSE, Rungta International Skills University

## 1. Problem Definition
The objective of this project is to build a console application for a hotel. The system must allow users to view available rooms, book a room for a specific number of nights, cancel existing bookings, and generate an itemized bill including a 12% GST. All booking data must be saved persistently in a file to prevent data loss between program executions.

## 2. Logic and Approach
- **Static Inventory:** A global dictionary (`ROOMS`) acts as the single source of truth for room types and prices (101 Single, 102 Double, 201 Suite).
- **Dynamic Storage:** A list of dictionaries (`current_bookings`) holds the active reservations in memory during runtime.
- **File Handling:** The `json` module is used to serialize the `current_bookings` list into `my_bookings.txt` upon any state change (booking or cancellation). On startup, `os.path.exists()` checks for the file and loads existing data, ensuring continuity.
- **Validation:** Exception handling (`try-except`) is used to catch invalid integer inputs for nights, and conditional checks prevent double-booking of already occupied rooms.

## 3. Test Cases Verified
1. **Normal Input:** Booked Room 101 for 2 nights. Output generated a base bill of 4000 + 480 GST = Rs. 4480. Data saved successfully.
2. **Boundary Input:** Booked Room 102 for minimum 1 night. Output generated 3500 + 420 GST = Rs. 3920.
3. **Invalid Input:** Attempted to book an already occupied room; system successfully blocked the transaction and prompted the user to choose another room.
4. **Cancellation Scenario:** Cancelled an active booking; system removed the entry from the text file and made the room instantly available in the "View Available Rooms" menu.

## 4. Conclusion
All bare minimum requirements have been successfully implemented. The code is modularized into dedicated functions, handles edge cases gracefully, and maintains persistent state via text file storage.
