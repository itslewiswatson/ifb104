/* This SQLite script contains queries that answer the questions
   from the Airline Queries exercise.  You should run these
   queries one at a time. */

/* Query 1: Display all the types of aircraft used in the Flights table */
SELECT DISTINCT AircraftType FROM flights;

/* Query 2: Display all the city names starting with the letters J, K or L */
SELECT CityName FROM cities
WHERE CityName LIKE 'J%' OR CityName LIKE 'K%' OR CityName LIKE 'L%';

/* Query 3: Display the total number of flights 
   which have fewer than 50 seats remaining */
SELECT COUNT(*) FROM flights WHERE SeatsRemaining < 50;

/* Query 4: Display the largest number of seats remaining 
   for any flight leaving from city code BNE */
SELECT MAX(SeatsRemaining) FROM flights
WHERE FromCityCode = 'BNE';

/* Query 5: For each city, display the CityName and CountryName */
SELECT CityName, CountryName 
FROM cities, countries
WHERE cities.CountryCode = countries.CountryCode;

/* Query 6: Display all Australian cities served by the airline,
   specifying the country by name not code */
SELECT CityName 
FROM cities, countries
WHERE cities.CountryCode = countries.CountryCode AND
      CountryName = 'Australia';