The task is to write an API that allows you to search for books and view reviews about them. Share the task using a generally available version control system (e.g. [https://github.com/](https://github.com/)).

### Back-end

On the backend side, we have Django 3 exposing an API in REST or GraphQl format, but something simple, without the use of external libraries.

We load the data into the database [by [command manager](https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/)] from csv files (sample files attached). One with a list of books, the other with a list of opinions.

Assumptions:

- The book has one author.
- A book can have many opinions.
- We search for books by titles.
- The opinion has a rating and description.
