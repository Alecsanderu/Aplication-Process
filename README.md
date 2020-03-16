![](static/img/Screenshot%20from%202020-03-16%2018-18-18.png)

# Aplication-Process
application-process-python
Web and SQL with Python - Application process assignment - Basic SQL




The HR department wants answers to the following questions:

Write a query that returns the 2 name columns of the mentors table. columns: first_name, last_name
Write a query that returns the nick_name-s of all mentors working at Miskolc. column: nick_name
We had interview with an applicant, some Carol. We don't remember her name, but she left her hat at the school. We want to call her to give her back her hat. To look professional, we also need her full name when she answers the phone (for her full_name, you want to include a concatenation into your query, to get her full_name, like: "Carol Something" instead of having her name in 2 different columns in the result. This columns should be called: full_name). columns: full_name, phone_number
We called Carol, and she said it's not her hat. It belongs to another girl, who went to the famous Adipiscingenimmi University. You should write a query to get the same informations like with Carol, but for this other girl. The only thing we know about her is her school e-mail address ending: '@adipiscingenimmi.edu'. columns: full_name, phone_number
After we returned the hat, a new applicant appeared at the school, and he wants to get into the application process. His name is Markus Schaffarzyk, has a number: 003620/725-2666 and e-mail address: djnovus@groovecoverage.com Our generator gave him the following application code: 54823
After INSERTing the data, write a SELECT query, that returns with all the columns of this applicant! (use the unique application code for your condition!)

Jemima Foreman, an applicant called us, that her phone number changed to: 003670/223-7459 Write an UPDATE query, that changes this data in the database for this applicant. Also, write a SELECT query, that checks the phone_number column of this applicant. Use both of her name parts in the conditions!
Arsenio, an applicant called us, that he and his friend applied to Codecool. They both want to cancel the process, because they got an investor for the site they run: mauriseu.net
Write DELETE query to remove all the applicants, who applied with emails for this domain (e-mail address has this domain after the @ sign).

You need to extend the Flask application (which you will find in the classroom repo) with some simple menu, where each menu point answers one question (or does what the question asks) from the above list. If the question is to print out some table, please print it out in some readable way (e.g. different rows in a table or in a list).


Extend your previous application with the following pages and add links to them from the front page:

Mentors and schools page [/mentors]
On this page you should show the result of a query that returns the name of the mentors plus the name and country of the school (joining with the schools table) ordered by the mentors id column
columns: mentors.first_name, mentors.last_name, schools.name, schools.country

All school page [/all-school]
On this page you should show the result of a query that returns the name of the mentors plus the name and country of the school (joining with the schools table) ordered by the mentors id column. BUT include all the schools, even if there's no mentor yet (in that cell, "No data" should be displayed)!
columns: mentors.first_name, mentors.last_name, schools.name, schools.country

Mentors by country page [/mentors-by-country]
On this page you should show the result of a query that returns the number of the mentors per country ordered by the name of the countries
columns: country, count

Contacts page [/contacts]
On this page you should show the result of a query that returns the name of the school plus the name of contact person at the school (from the mentors table) ordered by the name of the school
columns: schools.name, mentors.first_name, mentors.last_name

Applicants page [ /applicants ]
On this page you should show the result of a query that returns the first name and the code of the applicants plus the creation_date of the application (joining with the applicants_mentors table) ordered by the creation_date in descending order
BUT only for applications later than 2016-01-01
columns: applicants.first_name, applicants.application_code, applicants_mentors.creation_date

Applicants and mentors page [ /applicants-and-mentors ]
On this page you should show the result of a query that returns the first name and the code of the applicants plus the name of the assigned mentor (joining through the applicants_mentors table) ordered by the applicants id column Show all the applicants, even if they have no assigned mentor in the database!
In this case use the string "No data" instead of the mentor name.
columns: applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name

Use proper HTML elements to represent the data on the query related pages.
