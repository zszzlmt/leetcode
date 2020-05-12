# Write your MySQL query statement below
SELECT A.Name as Customers from Customers A where A.id NOT IN (SELECT B.CustomerId FROM Orders B)