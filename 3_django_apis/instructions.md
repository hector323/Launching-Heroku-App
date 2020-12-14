This activity is focused on understanding existing code.

Challenge 1
-----------

Get the code working.

1. Run the following commands:


    pipenv --python 3           # Create a new virtualenv
    pipenv shell                # Enter the virtualenv
    pipenv install django       # Download Django package into virtualenv
    pipenv install requests     # Download requests package into virtualenv
    python manage.py runserver  # Run the Django Python web-server itself

2. Now, visit http://localhost:8000 or http://127.0.0.1:8000 in your
web-browser to see the web application (both are equivalent)

3. What's the first thing you do with a new Python file? Add a print! Add a
print to the index function, just above the return statement.

4. Examine the code. Can you explain in your own words how all the files relate
to each other?
    - Hint: There are clues in the comments in the files.


---------------

Giggle News


        Start with this:

        {% for item in results %}
            <p> {{ item }} </p>
        {% endfor %}


Advanced Bonus Question #1:

- Adding date to the news page

- The Guardian API converts

- For more examples, check out this Stack Overflow question:
    - <https://stackoverflow.com/questions/214777/>

    from datetime import datetime
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    datetime.strptime('2008-09-26T01:51:42.000Z', date_format)


- In the template, use the date filter to format the date in the following format:
    Friday 10th, April 2020

