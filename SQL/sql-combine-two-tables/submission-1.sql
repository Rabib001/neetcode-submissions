SELECT p.first_name,
p.last_name,
a.city,
a.state

from address as a 

right join 

person as p on p.person_id = a.person_id