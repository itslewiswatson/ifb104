/* This SQLite script contains suggested solutions to the "Elements Database"
   questions.  You should run each of the SQLite statements below one at a
   time to see the results. */

/* 1. The first action, adding Scandium to the database,
      can be done by using the interactive interface to execute a
      script equivalent to the following */
INSERT INTO atomic_symbols VALUES ('Scandium', 'Sc');
INSERT INTO atomic_numbers VALUES ('Scandium', 21);

/* 2. Inserting Titanium into the database can be done
      using the following SQLite statements */
INSERT INTO atomic_symbols VALUES ('Titanium', 'Ti');
INSERT INTO atomic_numbers VALUES ('Titanium', 22);

/* 3. A query which returns all element names with
      atomic weights less than or equal to 10 is as follows */
SELECT element FROM atomic_numbers
WHERE number <= 10;

/* 4. A query which matches abbreviations to atomic numbers
      is as follows */
SELECT symbol, number FROM atomic_symbols, atomic_numbers
WHERE atomic_symbols.element = atomic_numbers.element;

/* 5. A query which returns the symbols for all elements
      with atomic weights greater than 10 is as follows */
SELECT symbol FROM atomic_symbols, atomic_numbers
WHERE atomic_symbols.element = atomic_numbers.element AND
      number > 10;

