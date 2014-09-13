Python Bikes
============
Object-Oriented Program written in Python3 and Nosetests

###Classes
- Bike
	- can be broken or not
- Person
	- can rent the bike from the station (only if available)
	- can ride the bike
	- can fall from the bike (and break it)
- Station
	- can have bikes (with maximum capacity)
	- can have available bikes
	- can have broken bikes
	- can release broken bikes (only if present)
- Van
	- can release available bikes (only if present)
	- can release broken bikes (only if present)
- Garage
	- can fix all the broken bikes (only if present)
	- can release all the available bikes (only if present)

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

import the classes: `>>> from station.station import Station`
`>>> from garage.garage import Garage`
`>>> from van.van import Van`

create your station: `>>> station = Station()`

create your van: `>>> van = Van()`

create your garage: `>>> garage = Garage()`

can dock bikes: `>>> station.dock(bike)`

is it full?: `>>> station.is_full()`

check the available bikes: `>>> station.available_bikes`

and the broken bikes: `>>> station.broken_bikes`

can release a bike: `>>> station.release(bike)`

can release all the broken bikes to another class:
`>>> station.release_broken_bikes_to(van)`
`>>> van.release_broken_bikes_to(garage)`

garage can fix all the broken bikes: `>>> garage.fix_bikes()`

can release all the fixed bikes:
`>>> garage.release_available_bikes_to(van)`
`>>> van.release_available_bikes_to(station)`

###Run the tests:
move in the root folder of the project `$ cd python-bikes`

to run all the tests: `$ nosetests`
to run a specific class test: `$ nosetests tests/station_tests.py`