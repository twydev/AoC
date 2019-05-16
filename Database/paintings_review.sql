-- try it in sqlfiddle.com

-- QUESTIONS:
-- 1. Find the titles of all paintings created by Vincent Van Gogh.	
-- 2. Find all years that have a painting that received a rating of 4 or 5, and sort them in increasing order.	
-- 3. Find the titles of all paintings that have no ratings	
-- 4. For each painting that has at least one rating, find the highest score that the painting received. Return the painting title and score. Sort by painting title.	
-- 5. For each painting that has at least one rating, find the painting title and total score, the highest score and the critic who gave the highest score.	
-- 6. For all cases where the same critic rated the same painting twice and gave it a higher rating the second time, return the critic's name and the title of the painting.	
-- 7. For each painting, return the title and the 'rating spread', that is, the difference between highest and lowest ratings given to that painting. Sort by rating spread from highest to lowest, then by painting title.	
-- 8. Find the names of critics for every artist (one row per artist with all critics)	

-- Schema generation code below
drop table if exists Painting;	
drop table if exists Rating;	
drop table if exists Critic;	
	
create table Painting(pid integer, title varchar(100), commissionedOn integer, artist varchar(100));	
create table Critic(cid integer, name varchar(100));	
create table Rating(rid integer, pid integer, score integer, reviewedOn date);	
 	
insert into Painting values(101, 'Mona Lisa', 1517, 'Leonardo Da Vinci');	
insert into Painting values(102, 'Girl with a Pearl Earring', 1665, 'Johannes Vermeer');	
insert into Painting values(103, 'The Birth of Venus', 1486, 'Sandro Botticelli');	
insert into Painting values(104, 'The Starry Night', 1889, 'Vincent van Gogh');	
insert into Painting values(105, 'Arrangement in Grey and Black No. 1', 1871, 'James Abbott McNeil Whistler');	
insert into Painting values(106, 'The Kiss', 1908, null);	
insert into Painting values(107, 'Sunflower', 1889, 'Vincent van Gogh');	
insert into Painting values(108, 'The Arnolfini Portrait', 1434, 'Jan van Eyck');	
 	
insert into Critic values(201, 'Gina Linetti');	
insert into Critic values(202, 'Jake Peralta');	
insert into Critic values(203, 'Rosa Diaz');	
insert into Critic values(204, 'Raymond Holt');	
insert into Critic values(205, 'Charles Boyle');	
insert into Critic values(206, 'Amy Santiago');	
insert into Critic values(207, 'Terry Jeffords');	
insert into Critic values(208, 'Scully');
insert into Critic values(209, 'Hitchcock');	
 	
insert into Rating values(201, 101, 2, date_format('2012-01-22','%Y-%m-%d'));	
insert into Rating values(201, 101, 4, date_format('2013-01-27','%Y-%m-%d'));	
insert into Rating values(202, 106, 4, null);	
insert into Rating values(203, 103, 2, date_format('2008-01-20','%Y-%m-%d'));	
insert into Rating values(203, 108, 4, date_format('2002-01-12','%Y-%m-%d'));	
insert into Rating values(203, 108, 2, date_format('2009-01-30','%Y-%m-%d'));	
insert into Rating values(204, 101, 3, date_format('2010-01-09','%Y-%m-%d'));	
insert into Rating values(205, 103, 3, date_format('2010-01-27','%Y-%m-%d'));	
insert into Rating values(205, 104, 2, date_format('2010-01-22','%Y-%m-%d'));	
insert into Rating values(205, 108, 4, null);	
insert into Rating values(206, 107, 3, date_format('2013-01-15','%Y-%m-%d'));	
insert into Rating values(206, 106, 5, date_format('2014-01-19','%Y-%m-%d'));	
insert into Rating values(207, 107, 5, date_format('2000-01-20','%Y-%m-%d'));	
insert into Rating values(208, 104, 3, date_format('1999-01-02','%Y-%m-%d'));	
