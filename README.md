# CS340

## How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
Building code in such a way that it can be re-used, potentially in many different ways, is one of the best ways to obtain maintainable, readable, and adaptable code. For this project, we were able to achieve this by implementing our CRUD operations (AnimalShelter.py) in a separate file/module, and then used that module in two different 
Jupyter notebooks, one for testing the CRUD operations, and one for implementing the actual dashboard which makes use of those CRUD operations.

This Python module could also be re-used in future projects, by making some small alterations to the AnimalShelter.py file to accept any MongoDB port and database/collection name.

## How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
The way I approach problems as a computer scientist is to break the problem down into smaller chunks, and then tackling those smaller chunks, one at a time, until the entire project is finished. I've actually worked on dashboards before, so this project followed very closely to how I would've developed it from the start.
  * Create/Load the database
  * Create the interface for interacting with the database
  * Create the dashboard using that interface

## What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
Computer Scientists, and more specifically data scientists, compile all the massive amounts of data, and condense it into a form that is much easier to digest, as well as to interpret and understand. It allows them to make much better decisions based on data, in a much quicker fashion than would otherwise be capable. As a computer scientist, being able to compile data and present it in a form such as the dashboard like we've created here will be a huge asset to other companies.
