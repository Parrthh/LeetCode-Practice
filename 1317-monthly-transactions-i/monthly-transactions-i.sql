# Write your MySQL query statement below
Select 
Date_format(trans_date, '%Y-%m') as month,
country,
count(id) as trans_count,
Count(if(state = 'approved',1,Null)) as approved_count,
Sum(amount) as trans_total_amount,
Sum(if(state = 'approved', amount, 0)) as approved_total_amount
From Transactions
Group By Date_format(trans_date, '%Y-%m'), country
Order by null;
