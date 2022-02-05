/* Display the names of the diatomic non-metals appearing in our database */

SELECT element FROM atomic_numbers
WHERE number = 1 OR (number >= 7 AND number <= 9)
ORDER BY element ASC;

/* Here's an alternative way of doing the query above */

SELECT element FROM atomic_numbers
WHERE number = 1 OR (number BETWEEN 7 AND 9)
ORDER BY element ASC;

/* Display the full details of the alkili metals appearing in our database */

SELECT  number, atomic_symbols.element, symbol
FROM atomic_symbols, atomic_numbers
WHERE (number = 3 OR number = 11 or number =19) AND
                atomic_symbols.element = atomic_numbers.element
ORDER BY number ASC;