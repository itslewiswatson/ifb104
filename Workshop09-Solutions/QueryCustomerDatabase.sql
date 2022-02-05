/* This SQLite script contains suggested solutions to the questions
   in the Customer Database exercise.  You should run each of
   these queries one at a time to see the results. */

/* 1. Show all details of customers who are 60 or older */
SELECT * FROM customers WHERE age >= 60;

/* 2. How many customers in the survey have a doctorate? */
SELECT COUNT(*) FROM customers WHERE education_level = 'Doctorate';

/* 3. Show all details of customers who are male and divorced. */
SELECT * FROM customers WHERE gender = 'Male' AND marital_status = 'Divorced';

/* 4. Show just the ages of male, divorced customers, ordered from
      youngest to oldest */
SELECT age FROM customers
WHERE gender = 'Male' AND marital_status = 'Divorced'
ORDER BY age;

/* 5. Show the average age of male, divorced customers */
SELECT AVG(age) FROM customers
WHERE gender = 'Male' AND marital_status = 'Divorced';

/* 6. Show the education level and number of cars
      of all customers with either a Master or Doctorate degree,
      ordered by number of cars from highest to lowest */
SELECT education_level, number_of_cars FROM customers
WHERE education_level = 'Master' OR education_level = 'Doctorate'
ORDER BY number_of_cars DESC;

/* 7. Show all details of the female customers who have a doctorate and
      have never married or have three or more cars */
SELECT * FROM customers WHERE gender = 'Female' AND
education_level = 'Doctorate' AND
(marital_status = 'Never Married' or number_of_cars >= 3);

/* 8. Show the customer ids and marital status of all customers
      with six or more cars */
SELECT customerID, marital_status FROM customers WHERE number_of_cars >= 6;

/* 9. Choose one of the customers returned by the previous query
      and show all the details for just that person */
SELECT * FROM customers WHERE customerID = 889674;

/* 10. Show the customer ids, ages and genders for all customers
       who have never married but have children */
SELECT customerID, age, gender FROM customers
WHERE marital_status = 'Never Married' AND number_of_children > 0;

/* 11. Find the youngest age of any customer who has a doctorate */
SELECT MIN(age) FROM customers
WHERE education_level = 'Doctorate';

/* 12. Determine the average number of cars owned by any customer
   who has a higher degree (master or doctorate) */
SELECT ROUND(AVG(number_of_cars), 1) FROM customers
WHERE education_level = 'Doctorate' OR education_level = 'Master';
