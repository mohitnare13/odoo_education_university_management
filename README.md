# University Education Management (Odoo 18)

#This module helps to manage the university education system in #Odoo 18.

📚 University Education Management (Odoo 18)
A complete Odoo 18 module to manage a university’s education system, covering admissions, academics, faculty, exams, attendance, fees, portal, and communication.

🌟 Overview
This module serves as an advanced solution for effectively managing university operations in Odoo.
It enables administrators, teachers, and students to interact with a centralized and automated system.

It is suitable for:

Universities

Colleges

Institutes

Training schools

✨ Key Features
🎓 Student & Academic Management
Student registration & profile management

Department, course, semester, and subject configuration

Academic year & batch setup

Document upload & approval

📝 Admissions & Online Application
Online admission form (website)

Application evaluation & tracking

Approved/Rejected workflows

Auto-email notifications

🧑‍🏫 Faculty & Departments
Faculty management

Department-wise assignments

Course & subject mapping

📅 Attendance & Timetable
Timetable period master

Automated timetable generation

Attendance with validation & tracking

🧾 Fees & Accounting
Fee types, categories, and structures

Automatic journal entries

Student invoices & payments

Integrated with Odoo Accounting

🧪 Exams & Results
Exam types (internal/external)

Question evaluation & scoring

Results with grade calculation

Result sheet view per student

🌐 Student Portal
Students can view:

✔️ Profile
✔️ Exams
✔️ Courses
✔️ Fee details
✔️ Notices
✔️ Time table

📢 Communication
Notice board system

Email notifications using templates

🧩 Dependencies
This module requires the following Odoo apps:

base

mail

hr_recruitment

account

website

📦 Installation Guide
1️⃣ Clone the Repository
bash
Copy code
cd <your-addons-path>
git clone https://github.com/mohitnare13/odoo_education_university_management.git
2️⃣ Verify Module Location
Ensure directory structure looks like:

text
Copy code
/odoo-18.0/custom_module/education_university_management
3️⃣ Update addons path in odoo.conf
ini
Copy code
addons_path = /odoo-18.0/odoo/addons,/odoo-18.0/custom_module
4️⃣ Restart Odoo
For Linux:

bash
Copy code
./odoo-bin -c odoo.conf
For Windows:

Stop the server

Start again

5️⃣ Install Module
Activate Developer Mode

Go to Apps

Click Update Apps List

Search: University Education Management

Click Install

⚙️ Configuration
1. Academic Setup
Academic Year

Course

Semester

Batch

Menu:
University → Configuration

2. Department & Subjects
Department creation

Subject mapping

Menu:
University → Departments / Subjects

3. Fees
Fee category

Fee type

Fee structure

Menu:
University → Fees

4. Exams
Exam types

Exam creation

Result entry

Menu:
University → Exams

5. Timetable & Attendance
Period master

Timetable

Attendance

Menu:
University → Timetable

6. Website / Portal
Make sure following modules installed:

website

portal

Then student portal auto-enabled.

🧱 Module Folder Structure
text
Copy code
education_university_management/
│
├── __init__.py
├── __manifest__.py
│
├── controllers/
├── data/
├── demo/
├── models/
├── security/
├── static/
├── views/
└── wizard/
🧪 Demo Data
Optional sample data available:

text

demo/education_university_management_demo.xml
Enable "Load demo data" when creating database.

📸 Screenshots (Suggested)
Screenshots coming soon 

🚀 Future Improvements
Assignment & homework module

Hostel management

Library management

Transport system

Mobile student app

🤝 Contribution
Contributions are welcome!

Fork repository

Create branch

Commit your changes

Open pull request

📄 License
This module is licensed under the AGPL-3 license.

You must keep the same license for derived works.

👨‍💻 Author
Author:
💡 Mohit Nare

If you’re interested in improving, extending, or implementing this module, feel free to connect!

⭐ Support
If you like this project, please ⭐ star the repo on GitHub!

🎯 Summary
This module helps educational institutions automate:

Academic operations

Student lifecycle

Fee management

Exams & results

Timetable & attendance

Online portal & communication

Making university operations faster, smarter, and transparent.

📥 Repository Link
👉 GitHub Repo:
https://github.com/mohitnare13/odoo_education_university_management
