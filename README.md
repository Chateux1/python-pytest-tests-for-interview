# Task Notes
## Task
As discussed, below you'll find a link to a demo QA site which contains a mocked online store. I do not expect full exhaustive test coverage, of course. I also won't provide direct instruction regarding exactly which area of the application to build tests for. I would like you to do some analysis and identify use case(s) within the application that you think would experience heavy user traffic and hence need to be kept airtight and bug free. Bonus points available for challenging yourself to build functions for more complex or awkward element types :-)

Use of Python 3 is required as it is the primary language used for our test frameworks. Please provide any information on setup and dependencies you think I will need to install in order to run your solution.

The cut off time for supplying an answer to the test is at the end of day, this Sunday, March 7th.  As the time allotted to you to deliver your answer is limited, I would also like you to deliver a brief analysis of your work:

- An explanation of the flow(s) you decided to cover with automated tests and the reasons behind your decision. Feel free to provide this in the form of a test plan document.
- In your opinion, using a percentage value, how complete is your answer judged by your own standards? (E.G. "The tests are 75% complete, as I didn't have time to do XYZ...)
- What improvements, if given more time, would you make to your answer? (E.G. "Given one more day to work on this further, I would add feature X because....")
- What areas, if any, proved difficult, and why?

Base URL - http://automationpractice.com/index.php
## Setup
I was using PyCharm, Python (v3.9.2) and pytest (v6.2.2) for this task. Additional packages where used:
- Selenium (used to be able to manipulate DOM elements of a site)
- chromedriver-py (used to run tests on Chrome browser)
- openpyxl (used to read data from excel file for DDT)
## Test Plan
As this is an online store page, I think that the most important areas that will get a lot of traffic are:
- Users registering,
- Users signing in,
- Users adding items to cart,
- Users reviewing their cart,
- Users checking out.

Initially I wanted to cover some cases in the user registration, user logging, user adding items and reviewing them in the cart, but because I was able to commit very limited time for this task (around 10 hours in total) and because I had no prior knowledge of Python and pytest, I was only able to cover these flows:
- Feature: User logs in
  - Scenario: An existing user logs in using correct information
    - Given there is an existing user,
    - When user information is entered,
    - Then user is logged in and “My Account” title is visible on the page. 
  - Scenario: User information for an existing user is verified
    - Given there is an existing user,
    - When the user signs in,
    - Then user information can be checked if it is correct (matches information provided during the registration).
- Feature: User registration
  - Scenario: A new user is created
    - Given a user does not exist with an email that is provided and that there is all the necessary information (mandatory fields)
    - When the user information is entered,
    - Then user is successfully created and “My Account” title is visible on the page.
  - Scenario: DDT type user registration where one user is created, and others are not created due to missing information in mandatory fields
    - Given there is a file with user information and that those users do not exist,
    - When that information is used to create users,
    - One user is successfully created, others are not created due to missing information and the test passes.
## Coverage Analysis
I have decided to cover these flows as they seem to be very important and would probably be used by every user. It is hard to judge how completed are these flows. Some of the issues:
1.	There is no coverage for logging in with incorrect information,
2.	Not all the fields are tried to be left empty when creating a new user,
3.	Only those fields that are mandatory for the registration process are covered,
4.	Not all fields are checked if they have correct information after user registration.

1st issue could be covered by refactoring the logging in test to a DDT and provide invalid information. 2nd, 3rd and 4th issues could be covered by expanding the existing tests. Based on this analysis I would say that these flows are covered around 60%.
## Improvements
- As this is my first experience with Python, pytest and DDT, I am not sure whether the DDT scenario is made in a good way. The assertion part seems kind of strange and complicated. The whole test is missing some logging information which would provide valuable information in the case of the test failing. 
- I am not sure about the usage of fixtures for the driver setup and teardown, maybe there is a better way to do this.
- I believe that POM classes could have static methods, but I was not able to make it work.
## Difficulties
- I tried implementing logging information during the tests but ran into difficulties with making it work and decided to not do it. 
- I ran into an issue when providing paths for different files that are used by the tests: when “.\\location\\file” notation is used then the tests are working when called through the console, but when “../location/file” notation is used then the tests work when right clicking on a test title in PyCharm and running them through there. I did not find a way to make them work both ways, but I guess it should be possible. I decided to leave them to work when running though the console.
