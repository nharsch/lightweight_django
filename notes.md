
#Chapter 1

* You can do a one file app with Django
* you can create app templates for Django

#Chapter 2 Stateless App

###Why stateless?

* HTTP is a stateless protocol
* managing state via cookies is messy and hard :(

###Resuable Apps vs Composable Services    

* Large applications with different components often have a fairly
  complex architectural style
* better to break large websites into composable services
* REST APIs are great cadidates for breaking 
  out into separate Django projects

###Placeholder image server

* url cpature groups:
    * captured pattern groups are passed to the view as positional args
        * named groups are passed as keyword args

* Caching
    * server side or client side 
    * etag decorator 
        * will generate content on first request
        * otherwise sends a 304 Not Modified response

* Creating the Home Page View
    * need to serve static files

#Chapter 3 Building a Static Site Generator 

##Rapid protyping process.

1. Observer and analyze.
    * Figure out your end uder goals
2. Build
    * Create minimum viable product
3. Ship
    * Create a seamless way to deploy changes
4. Adopt and educate
    * Teach your users how to use the new features
5. Iterate and maintain
    * Take your users' feedback and iterate back through
    the process

###Initial Project Layout

###Basic Styling

* use bootstrap

###Custom Management Command

* generate out output HTML

###Building a Single Page

* add optional arg to parser is defferent in Django 1.8

###Hashing Our CSS and JS Files

###Compressing static files

* using Django Compressor
* we now have a cache folder in build/static

###Generating Dynamic Content

* Using JSON as context in page

# Chapter 4 - Building a REST API

* let's build a SCRUM style task board

## Designing the API

the url strucuture should look like this:
    /api/
        /sprints/
            /<id>/
        /tasks/
            /<id>/
        /users/
            /<username>

### Sprint Endpoints

The `ModelViewSet` provides scaffolding for CRUD operations.
Auth, permissions, pagination, and filtering are controlled
by the `REST_FRAMEWORK` settings dictionary if not set on the view

### Task and User Endpoints

### Connecting to the Router

connect ViewSets to the URL routing system
