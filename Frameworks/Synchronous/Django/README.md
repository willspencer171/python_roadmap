# Django

## Unchained? Or just speedy?

Django is a synchronous, open-source web development framework that was designed to streamline otherwise long-winded and complex tasks such as user authentication, content administration, site maps and RSS feeds. It is also easily scalable :)

It utilises the model-template-view architecture that is common in web development

I'm gonna need to dedicate some real time to this, so here's a few quick links for me to refer to, and for everyone to see where I'm getting my information from:

> - [Django Tutorial](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
> - [YouTube Tutorial](https://www.youtube.com/watch?v=rHux0gMZ3Eg) (1 hr)

## The YouTube Video

I'm just gonna make a few notes on each of the sections as I'm watching the video.

A huge number of large companies use Django in their tech stack because it is so useful and ubiquitous to learn. It also makes creating developer APIs easy (take Spotify for example, I've looked at their API a little bit).

Django isn't the fastest thing in the world, but that's not so much a problem because of the amount of versatility it provides. Some think that the optional features that come default with Django are just bloatware, but it doesn't make so much a difference.

### Some basic Web Fundamentals

A website will have two main features: the frontend and backend. The frontend is the pretty bit that a user will interact with, while the backend is all the processing that carries out tasks that the frontend creates. For example, accessing a webpage by clicking a link (on the user interface) sends a request from the client to the server, where the request is processed and a webpage is sent as a response by the backend of the site. This backend may have handled a few operations like data access and user authentication.

The request-response system is handled by the server by following the Hypertext Transfer Protocol (HTTP). The web server decides how to respond to the client's request. Either the server will generate a new HTML document for the client based on the request, and send it back; otherwise, data can be sent back to the client to be processed by the client's machine and update an HTML document that way. The latter is preferred by today's standards as it frees up some processing space server-side to allow for a higher number of clients, increasing scalability.

Django is a server-side framework that puts the processing responsibility on the client. This essentially makes the server a gateway to the data, that a client accesses via an API (Application Program Interface) with multiple endpoints for the user to interact with.

### Setting up the Development Environment


