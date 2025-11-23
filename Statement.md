

Project Statement

Problem Statement

In many colleges, creating a weekly timetable is still done manually using pen and paper or spreadsheets. This process is time-consuming and often leads to human errors such as:

Assigning the same professor to two classes at once.

Double-booking a lecture hall.

Uneven distribution of workload.
Modifying a manual timetable usually requires starting over from scratch. There is a need for an automated tool that can handle these constraints instantly.

Scope of the Project

The scope of this project is limited to generating a weekly schedule for a single department or batch. It handles:

Inputting course and faculty details.

Allocating time slots (Mon-Fri, 9 AM - 4 PM).

Handling basic "hard constraints" (Room and Professor availability).

Visualizing the output and exporting data.

It does not currently cover multi-departmental synchronization or student-specific elective choices.

Target Users

College Administrators / HODs: Who need to draft schedules at the start of a semester.

Clerks: Who perform data entry for the schedule.

High-Level Features

Input Module: Form-based entry for Course Name, Professor, Room, and Frequency.

Processing Engine: A logic core that maps requirements to empty slots using constraint satisfaction.

Output Module: A grid-based view to display the final schedule and a file writer to export results.