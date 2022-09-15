[Link to Heroku app](https://azra-catalog.herokuapp.com/katalog/)

1. Create a diagram containing client request to the Django web application and its response. Also explain the flow of the diagram and how the urls.py, views.py, models.py and HTML files connected each other.


    ![Diagram](https://user-images.githubusercontent.com/93767914/190314125-96c8f28c-9e4d-4a5f-a8df-4cdc4ef8563e.jpg)

    
    First, the request would be processed in urls.py as it defines URL addresses and functions that would be executed.
    Then, the request would be forwarded to the appropriate view in views.py.
    From there, it would either read/write data in models.py, use the katalog.html to execute the display,
    or send the http response back to client.
    
2. Explain why do we use virtual environments? Let's say, if we do not use the virtual environments, can we still create a Django web application?

    We need to use virtual environments because we also need to install the requirements.
    The virtual environment will manage packages for different projects so the installment won't be installed globally.
    Without it, the installment may lead to broken system tools or projects.
    
3. Explain how did you implement the steps on point 1 to point 4 above. 
    First, I copied the provided template to a new repository and followed the steps from previous labs.
    Since the steps to implement step 1-4 is quite familiar to previous labs, I only applied minor changes to names or variables.
    I also followed the steps provided in Lab 0 to deploy to Heroku.
