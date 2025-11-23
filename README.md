College Timetable Generator

Overview

The College Timetable Generator is a desktop application built with Python that automates the process of creating weekly class schedules. It replaces manual, error-prone Excel sheets with an intelligent system that assigns courses to time slots while ensuring no two professors or rooms are double-booked.

Features

User-Friendly Interface: Simple GUI built with Tkinter for easy data entry.

Conflict Detection: Automatically checks availability of Rooms and Professors before assigning slots.

Randomized Scheduling Algorithm: Uses a randomized greedy approach to find a valid solution.

Visual Grid Output: Displays the generated timetable in a clean, color-coded grid with clear borders.

CSV Export: Allows users to save the generated schedule as a .csv file for printing or sharing.

Retry Mechanism: Automatically retries multiple times if a perfect schedule isn't found immediately.

Technologies/Tools Used

Language: Python 3.x

GUI Library: Tkinter (Standard Python Library)

File Handling: CSV Module

Logic: Random Module (for shuffling and slot selection)

Steps to Install & Run

Prerequisites:

Ensure Python is installed on your system. You can check by running python --version in your terminal.

Download the Project:

Download timetable_final.py to a folder on your computer.

Run the Application:

Open your terminal or command prompt.

Navigate to the folder where you saved the file.

Run the following command:

python timetable_final.py


Instructions for Testing

Launch the App: Run the script to open the window.

Add Data:

Subject: Enter "Maths"

Teacher: Enter "Prof. Sharma"

Room: Enter "101"

Lectures: Enter "3"

Click Add Subject.

Add Conflicts (to test logic):

Add another subject "Physics" with "Prof. Sharma" (same teacher).

Add another subject "Chemistry" in Room "101" (same room).

Generate: Click Generate Table.

Observation: Verify that Prof. Sharma is not placed in two slots at the same time.

Observation: Verify that Room 101 is not double-booked.

Export: Click Save as CSV and check the generated file in Excel.

Screenshots

(Please add your screenshots here manually after taking them from the running app)
