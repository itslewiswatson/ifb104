/* This SQLite script contains suggested solutions to the "Airline Database"
   questions. Having imported the Airline database, you should run these
   queries and statements one at a time to see the results. */

/* 1. The first query, reproduced below, produces 11 rows */
SELECT * FROM cities;

/* 2. The second query, reproduced below, produces 5 rows */
SELECT * FROM cities WHERE CountryCode = 'AUS';

/* 3. A query to produce all Australian cities is as follows */
SELECT CityName FROM cities WHERE CountryCode = 'AUS';

/* 4a. A query that displays rows for all aircraft with a
       capacity of at least 150 seats, but not more than 250 seats
       is as follows */
SELECT SeatingCapacity FROM aircraft
WHERE SeatingCapacity >= 150 AND SeatingCapacity <= 250;

/* 4b. Here's an alternative answer to Question 4 */
SELECT SeatingCapacity FROM aircraft
WHERE SeatingCapacity BETWEEN 150 AND 250;

/* 5. A query that displays just the aircraft description and
      aircraft type columns for all aircraft is as follows */
SELECT AircraftDescription, AircraftType FROM aircraft;

/* 6. A query that displays the flight number, destination city,
      and the number of remaining seats of all the flights that
      depart from Brisbane and have more than 20 seats left is
      as follows */
SELECT FlightNum, ToCityCode, SeatsRemaining FROM flights
WHERE FromCityCode = 'BNE' AND SeatsRemaining > 20;

/* 7. The following statement will change the number of seats
      remaining on Flight 10 */
UPDATE flights SET SeatsRemaining = 25 WHERE FlightNum = 10;

/* 8. The following statement will change the destination
      for Flight 3 */
UPDATE flights SET ToCityCode = 'ADL' WHERE FlightNum = 3;

/* 9. The following statement will add two new rows to the
      collection of country codes */
INSERT INTO countries VALUES ('CA', 'Canada'), ('ES', 'Spain');

/* 10. The following command will delete the obsolete
       Boeing 747-338 entry */
DELETE FROM aircraft WHERE AircraftDescription = 'Boeing 747-338';

/* 11. The following statement will add the Airbus A380
       to our fleet of aircraft */
INSERT INTO aircraft VALUES ('A380', 'Airbus A380', 853);

/* 12. The following statements will update the number of seats
       remaining for Flights 1 and 2 to allow for the ten people
       travelling from Brisbane to Sydney via Canberra */
UPDATE flights SET SeatsRemaining = 0 WHERE FlightNum = 1;
UPDATE flights SET SeatsRemaining = 10 WHERE FlightNum = 2;

/* 13. The following statement will delete all flights to
       Los Angeles */
DELETE FROM flights WHERE ToCityCode = 'LAX';
