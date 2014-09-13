Python Bikes
============
Object-Oriented Program written in Python3 and Nosetests

###Classes
- Bike
- Person
- Station

###Technologies
- Python3
- Nosetests

###How do you use it? (Mac)
clone the repository:

`$ git clone https://github.com/mserino/python-bikes.git`

move into the directory:

`$ cd python-bikes`

run the interpreter:

`$ python3`

###Bike Class

import the Bike class: `>>> from bike.bike import Bike`

create your first bike: `>>> bike = Bike()`

and now break it: `>>> bike.break_bike()`

fix it: `>>> bike.fix_bike()`

###Person Class

import the Person class: `>>> from person.person import Person`

create your first person: `>>> John = Person()`

ride the bike: `>>> John.ride(bike)`

does John have bikes? `>>> John.has_bike()`

John can also fall from the bike (and break it): `John.falls_from(bike)`

release the bike `>>> John.release(bike)`

###Station, Van, Garage Class

import the class: `>>> from station.station import Station`

create your station: `>>> station = Station()`

can dock bikes: `>>> station.dock(bike)`

is it full?: `>>> station.is_full()`

check the available bikes: `>>> station.available_bikes`

and the broken bikes: `>>> station.broken_bikes`

can release a bike: `>>> station.release(bike)`

can release all the bikes to another class: `>>> station.release_broken_bikes_to(van)`

###Run the tests:
`$ cd python-bikes`

to run all the tests: `$ nosetests`
to run a specific class test: `$ nosetests tests/station_tests.py`

###What's missing?
~ This project is still work in progress ~