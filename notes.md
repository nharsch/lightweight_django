
##Chapter 1

* You can do a one file app with Django
* you can create app templates for Django

##Chapter 2 Stateless App

* Why stateless?
    * HTTP is a stateless protocol
    * managing state via cookies is messy and hard :(
* Resuable Apps vs Composable Services    
    * Large applications with different components often have a fairly
      complex architectural style
    * better to break large websites into composable services
    * REST APIs are great cadidates for breaking out into separate Django projects

* Placeholder image server
    * url cpature groups:
        * captured pattern groups are passed to the view as positional args
        * named groups are passed as keyword args
