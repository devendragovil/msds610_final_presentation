# Hash Tables Final Project
This repo contains the code and relevant details for the final presentation (Assignment 7) for the course MSDS-610, part of the MS in Data Science program at the University of San Francisco.  
This repo contains contributions by the following team members (mail ids are mentioned in hyperlink):
- [Devendra Govil](mailto:dgovil@dons.usfca.edu)
- [Kayhan Eryilmaz](mailto:kkeryilmaz@dons.usfca.edu)
- [Ity Soni](mailto:isoni@dons.usfca.edu)

## Table of Contents
1. Abstract
2. Quick Review of Hash Tables
3. Pros of Hash Tables
4. Cons of Hash Tables
    1. Bad Hash Function
    2. Collisions
        1. Chaining
        2. Open Addressing
5. Flask App

## Abstract

In this project, we demonstrated the different scenarios you might run into when implementing a hash table. While it is a very nice data structure to use, there some things to keep in mind when implementing it. The following describes and summarizes the potential challenges you might face and what appropriate solution you should be using.

## Review and Pros of Hash Tables
### What are Hash Tables?

Hashtables are useful data structures that allow us to quickly organize, sort, and look up data.
The 4 important components for generating and using hashtables are:

keys
values
bins
hash function
This is the central component that is used to assign keys to respective bins.


### Why do we need Hash Tables?

In data science, we always come across large data sets and parsing through the data can be a cubersome task when we're searching for something we don't know the location of. The most simplistic way to search for a value in a list of values would be to iterate through it and stop once we find it. With hashtables we can speed up the process and make our lives much easier with constant look up times.

## Cons of Hash Tables

Not so much cons, as "considerations", here are some of the issues you might run into when implementing hash tables. Like a lot of concepts in computer/data science, there are some trade offs when picking one method over another. 

### Bad Hash Functions 

If we have a hashfunction that doesn’t separate the data into bins equally, then we’ll have an imbalance in bin sizes. 

In order to fix this problem, or even avoid it in the first place, is to modify your hashfunction to distribute the data more evenly. A common modification is taking the modulo with a prime number

### Collision

Some keys will have the same hashcode value, which results in them being in the same bin. If a bin is already occupied, another value cannot be appended.

#### Chaining 

There’s different ways to solve this problem, such as having your bins contain arrays, sets, etc. but the universal name for this solution is called chaining.
Chaining is when your bin uses a linked list to connect newly added values to previous ones. 

#### Open Addressing

Another method of collision resolution is open addressing. This is when instead of chaining values  together, the hashtable looks for the next available bin to put it the key value pair in. The types of open addressing are:

- Linear probing (the interval between probes is fixed)
- Quadratic probing (the interval between probes increases quadratically)
- Double hashing (the interval is computed by a second hash function)



## Interactive Session using Flask App

To gain an intuitive understanding of collisions as well as the different approaches to resolve collisions (Linear Probing and Chaining) the team built a flask app that was hosted on a GCP VM and accesible at devendragovil.com:5000/  

For the sake of convenience, a QR code was generated that was passed on to the audience via print outs. 

The landing page required students to input their favorite number and their first name.

Based on this data, the flask app generated real time visualizations (the awesome library, lolviz, available [here](https://github.com/parrt/lolviz) was used for the visualizations) of hash table implementations of both linear probing and chaining.

This was a pedagogical tool to illustrate the different collision resolution mechanisms and the considerations in using either of them. 

## Conclusion

We have jointly explored hash tables in some depth over the course of past couple of weeks.
- Initial Explanation
    - We started with an intuitive understanding of the hashtables and hashfunctions using examples
    - We developed intuition and justification behind widespread usage of hashtables
- Coding Demo
    - We learned to implement hashtables using the list of lists implementation in python
    - We also learned about hash functions and how to design them
    - We studied the impact of bucket numbers on time complexity 
- Final Presentation
    - Herein, we reviewed our understanding of hash tables
    - We discussed advanced considerations and things to be careful about while building/designing hash tables
    - We discussed what a bad hash function can mean and how to correct it 
    - We discussed collisions and the two approached to collision resolution
    - Via an interactive flask app we understood linear probing and chaining in greater depth and developed an intuition for them
