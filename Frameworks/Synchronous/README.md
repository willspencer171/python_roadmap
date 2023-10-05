# Synchronous Web Frameworks

## What does this even mean?

To know what this means, we need to be able to compare synchronous development to asynchronous development as methods of implementing *concurrency*. This is basically the ability of a processor to process multiple processes at the same time (wordy, I know). The important bit is the *same time* bit.

Synchronous frameworks use a load balancer to receive any tasks that are requested to be completed. With respect to a web framework context, a web server acts as the load balancer and public interface for clients. The web server then allocates tasks to workers to complete tasks concurrently.

<p align=center> <img src=SyncDiagram.png> </p>

The problem posed by this setup is that there are still bottlenecks in terms of processing if requests are handled slowly. If there are more requests than there are workers, the excess requests will be held in a queue. This is in contrast to async processes which uses a loop to run consistently and listen out for instructions (in some applications this is known as the event loop).

## So what's better to use?

In terms of "what's better", synchronous applications are typically good for small applications that are not resource intensive. For example, a CRUD (Create, Read, Update, Delete) application is good for a synchronous framework.

Frameworks that use this approach include:

- [Django](https://github.com/willspencer171/python_roadmap/tree/master/Frameworks/Synchronous/Django)
- [Flask](https://github.com/willspencer171/python_roadmap/tree/master/Frameworks/Synchronous/Flask)
- [Pyramid](https://github.com/willspencer171/python_roadmap/tree/master/Frameworks/Synchronous/Pyramid)
