Synopsis: 

	Python Web App for viewing, adding and deleting
	subscribers in/from a mailing list
	using the campaigns monitor API (http://www.campaignmonitor.com/api/). 


Description:

	This project is written in Python.

	The back-end component implements a class
	that communicates with the monitor tool.
	In order to initiate the class, the user must pass
		- the API Key
		- the client name
		- the list name
	as arguments to the constructor.
	If any of the above does not match the correct data,
	a custom Error is raised and the user is redirected
	to an error page containing the message error.

	The front-end component uses the Flask framework
	in order to create a fully functional web app.
	Templates where used to create
		- the login page
		- the subscribers' list page
	The second one contains buttons to manipulate the list
	and add/remove subscribers.
	Whenever a button is pressed (for login, insert a subscriber or delete one),
	an HTTP request via jQuery library takes place in order to miodify the list.
	Then, the list page is reloaded.

Dependencies:

	All the dependencies are included in the requirement.pip file
	and can be installed with the following command:
	 pip install -r requirements.pip

Known bugs:

	It appears that in some cases, when a subscriber is added,
	while he/she is added correctly,
	when the list is queried to fetch the new data,
	the not updated list is returned
	(It probably has something to do with data caching).


Problems faced and total effort:
	
	The total effort that was needed is about 8 hours (1 working day).

	For the back-end component, including the familiarization with the API,
	took me around 3 hours,
	while the front-end component, including the integration with the back-end,
	took me another 5.
	
	That is because I only have academic experience with front-end applications
	and I needed time to familiarize with jQuery (the requesting mechanism most)
	and the Flask framework, which I hadn't used before.

	In order to save time, I used html code and css found online that modified
	to meet my needs.
	For the jQuery functionality, which was the biggest challenge,
	I used various sources, mostly from StackOverflow.

	The html code used can be found in the following links. 
		https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
		http://www.w3schools.com/w3css/tryw3css_templates_analytics.htm 

Author:
  Written by Stefanos Georgakis
