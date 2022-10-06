

1

Introduction to PostgreSQL

The Open Source Object-Relational Database Management

System

V arlena,L L C

A.Elein M ustain

w w w .varlena.com

elein@ varlena.com





2

PostgreSQL BSD License

Redistribution and use in source and binary forms,

with or without modification, are permitted provided

that the following conditions are met:

Redistribution in source or binary must maintain copyright and

following disclaimer

Neither the name of the organization nor the names of its

contributors may be used to endorse or promote products.





3

Agenda

PostgreSQL Features

Installation and Configuration

Maintenance and Monitoring

Command Line Interface

Database Basics in PostgreSQL





4

Not the Agenda

Client Interfaces

Inheritance

Comparisons to other Databases

Replication, Point in Time Recovery

Full Text Search





5

History of Postgres

1992

1986

1995

postgres95

Miró/Illustra

UCB

1996

PostgreSQL

Global Dev

Informix

2000

2001

Informix

IUS 9

IBM

2006





6

What is PostgreSQL?

Relational Database Management System

Object-Relational Database

Ability to add First Class simple and complex objects,

with methods, that can be used in a Relational

Context (SQL)





7

PostgreSQL Relational Features

Foreign keys

Triggers

Views

Transactional Integrity

ACID compliance

Complex Queries





8

Data Centricity

Data stands on its own

Data is money

Many applications one database

Database centric logic

Integrity cannot be circumvented by applications





9

ACID Compliance

Atomic

transactions seen in full or not at all

Consistent

system enforced contraints

Isolated

transactions do not interfere with each other transactions

Durable

On Commit, result will not be lost





10

Multi-Version Concurrency Control

Snapshot of data for command or transaction

Virtually eliminates need for locking

Reading does not block writing and vice versa

SET TRANSACTION ISOLATION LEVEL

READ COMMITTED

SERIALIZABLE





11

SQL and PostgreSQL

Excellent Standards Compliance

SQL89, SQL92, SQL98, SQL2003

Documentation includes Compliance

Design Issues decided by Standards





12

Object Relational Features

Data types

Functions

Operators

Rules

Aggregates

Index Methods





13

PostgreSQL Queries with Objects

select hotel\_name, hotel\_address

from hotels h, airports a

where a.name = 'OAK' and

h.loc @ Circle(a.loc, '5 miles');

select name, num\_kids from people;

select pdf( doc, '/home/me')

from doc d

where dnameget(doc) = 'myresume';





14

Client GUI Interfaces

PgAdmin III

www.pgadmin.org

phppgadmin

phppgadmin.sourceforge.net

DbVisualizer

www.minq.se/products/dbvis/

Others, e.g. pgaccess

See sourceforge.net





15

Client Programming Interfaces

psql - Command Line

libpq – C library

ECPG – Embedded SQL

pgtcl – Tcl binding library

Drivers

JDBC

ODBC

DBI: Perl, Python, PHP, etc.

.NET





16

Server Side Languages

PL/pgsql

SQL

C

Other server side languages

PL/perl, PL/pythonu,

PL/R, PL/Tcl, PL/Ruby,

PL/bash, PL/Java

etc.





17

Downloading PostgreSQL

http://www.postgresql.org

By Source: ftp, bittorrent

By CVS tree

In Packages: RPM, Debian

Company Distributions





18

Operating System Distributions

Most Linux like OS distributions

MacOSX:

[www.entropy.ch/software/macosx/](http://www.entropy.ch/software/macosx/)[ ](http://www.entropy.ch/software/macosx/)postgresql

8.1 Native Win32 Version

pginstaller at pgfoundry.org

Cygwin:

www.cygwin.com





19

Configuration Points

Build Time

Build directives

Installation directory

PL Language options

Server Environment

postgresql.conf, pg\_hba.conf

Runtime/Client Environment

PG environment variables





20

Configuration Points

Build Time

As user postgres ...

$ ./configure \

--prefix=/local/pgsql81 \

--with-perl \

--with-python \

--with-tcl \

--enable-depend

$ make

$ sudo make install





21

Initdb -D $PGDATA

Creates Data Directory with:

configuration files

postgresql.conf

pg\_hba.conf

template databases

template0

template1

super user database





22

Configuration Points

Server Environment

Global User Configuration

$PGDATA/postgresql.conf

Environment variables for server startup

Access Security

$PGDATA/pg\_hba.conf

Host, user and database access.





23

Configuration Points

Global User Configuration

Environment Variables for Server Startup

postgresql.conf

See also:

[www.varlena.com/GeneralBits/](http://www.varlena.com/GeneralBits/)

Tidbits/#Performance





24

Configuration Points

Global User Configuration

V ariable

D efault

100

@ 2G RAM

m ax\_connections

sh ared \_ bu ffers

w ork\_m em

100

25000

16384

16384

\*

1000

1024

m aintenance\_w ork\_m em 16384

m ax\_ fsm \_pages

m ax\_ fsm \_ relatio n s

effective\_ cach e\_ size

log\_destination

20000

1000

1000

std err

off

\*

82500

std err

on

red irect\_ std err





25

Configuration Points

Global User Configuration

V ariable

log\_directory

D efault @ 2G RAM

pg\_log /varl/lo g /p g sq l

log\_m in\_duration\_statem

lo g\_line\_p refix

lo g \_ statem ent

stats\_ start\_ co llecto r

stats\_ co m m and \_string

stats\_ b lo ck\_ level

stats\_ ro w \_ level

autovacuum

-1

500

[% p - % t ]

none

on

ddl

on

on

on

on

on

off

off

off

off





26

Configuration Points Basic Security

\# Host

\# "local" is for Unix domain socket connections only

DB USER

ADDRESS METHOD

local

\# IPv4 local:

host

\# IPv6 local:

host

all

all

all

all

all

trust

trust

trust

reject

127.0.0.1/32

::1/128

all

all

\# bad bernie

host

bernie 163.555.9.9

\# demo

host

demo varlena163.555.9.9 trust

\# users

host

all all

163.555.9.9

md5





27

Configuration Points

Runtime/Client Environment

Environment Variables

PGHOST – default localhost

PGPORT – default 5432

PGUSER – default $USER

PGDATABASE – default $PGUSER

Different for multiple installations





28

Configuration Points

Session Setting

View: pg\_settings

Show values and descriptions

SELECT name, setting, short\_desc

FROM pg\_settings

ORDER BY name;

What can be set in a session?

SELECT name

FROM pg\_settings

where context='user';





29

Housekeeping PostgreSQL Start and Stop

Starting & Stopping PostgreSQL

Installation Specific Script (/etc/init.d)

$ pg\_ctl start -D $PGDATA

$ pg\_ctl stop

Windows PostgreSQL--> Programs





30

Housekeeping PostgreSQL Logging

Log Maintenance

Rotate Log Settings in postgresql.conf

Alternative:

$ pg\_ctl start -D $PGDATA |\

rotatelogs $PGDATA/pglog 86400 2>&1;

Always know where your log file is!





31

Housekeeping PostgreSQL Vacuuming

Autovacuum

Configure in postgresql.conf

Vacuum

$ vacuumdb --analyze --full

Updates Statistics

Improves Performance

Recovers Disk Space

Frequency tuning required





32

Housekeeping PostgreSQL Backing Up

Backup

pg\_dumpall > \

.../`date +%Y%m%d`dump.sql

Restore

psql -f 20061231dump.sql

Backup! Now!

No excuses! Really!





33

Monitoring PostgreSQL

Client Server Architecture

pg\_stat\_activity

Set pg\_stats\_command in postgresql.conf

ps -alx

Log files

check pgfoundry for log parsers





34

Documentation and Help

Online & Downloadable Docs

Mailing Lists: www.postgresql.org

IRC #postgresql freenode.net

PostgreSQL General Bits :-)

http://www.varlena.com/GeneralBits





35

Creating Databases

$ createdb accounts





36

Adding Users

$ createuser bob

Shall the new role be a superuser?

(y/n) n

Shall the new role be allowed to create

databases? (y/n) y

Shall the new role be allowed to create

more new roles? (y/n) y

CREATE ROLE





37

psql Basics

Always learn help first.

Command Line options

$ psql --help

Backslash Command Help

$ psql db

db=# \?

SQL Help

$ psql db

db=# \help [SQL command]





38

Database Design Elements

Data Types & Sequences

Nulls

Keys

Constraints & Defaults

Triggers, Functions & Operators

Tablespaces

Simple domains

Rules





39

Create Table

AS, LIKE

WITH OIDS

Current default WITH may change

See default\_with\_oids

Temporary Tables

PRESERVE ROWS, DELETE ROWS, DROP

INHERITS

CONSTRAINTS

TABLESPACE





40

Create Table

CREATE TABLE people (

id SERIAL PRIMARY KEY,

name text,

dept\_no int REFERENCES dept(dept\_no)

);

CREATE temp TABLE ships\_temp as

SELECT ship\_id, cargo\_no, voyage

FROM ships;





41

Data Types

Integers, big and small

Serials

Arbitrary precision–numeric

Floating points

Boolean

Geometric

Network Addresses

Bit Types

Serial Types–Identity

Character Types

Binary Data, big and small

Date/Time/Timestamp

Arrays

Oids

Pseudo Types





42

Data Type Mapping

Integers................. 2, 4, 8 bytes

Serials.................... Identity, Autoincrement

Numeric.................. Money

Floats..................... Arithmetic

Text....................... Character Types

Date/Time/Interval... Dates & Times

Timestamp.............. Timestamps

Boolean................... Boolean

bytea...................... Byte stream, images





43

Keys

Primary Keys

Implemented as B-Tree Unique indexes

Foreign Keys

Implement Referential Integrity.

A FK in table A says that this value references a unique

value in table B.

Cascading updates, deletes

Nulls OK





44

Defaults & Constraints

Initialize column with constants

Check value for validity

UNIQUE, [NOT] NULL, KEYS

CREATE TABLE players (

nick\_name text PRIMARY KEY,

team\_name text REFERENCES teams(team\_name),

age integer CHECK (age > 15) NOT NULL,

games\_played integer DEFAULT 0

);





45

Nulls

A NULL is a NULL is a NULL

NULLS are not equal to each other

NULLS are not equivalent to an empty string

NULLS are not equivalent to 0

NULLS are not indexed





46

TableSpaces

Creating a tablespace

CREATE TABLESPACE bd LOCATION '/bigdisk';

Using a tablespace

CREATE TABLE FOO (...) TABLESPACE bd;

Altering a tablespace

alter owner, alter name

Alter a table's tablespace

ALTER TABLE SET TABLE SPACE TO bd;





47

SELECT

Target List – list of columns to be returned

any expression,

aggregate,

subquery,

function,

columns from FROM clause data sources





48

SELECT

FROM – data sources

Tables,

Views,

Set Returning Functions,

SubQueries,

JOINS,

UNIONS





49

SELECT

WHERE – boolean expression qualifying data

Expressions,

Columns,

Functions,

SubQueries





50

SELECT

GROUP BY – scope of Aggregate

Elements of Target List not involved in aggregation.

Determines Break columns

select tname, count(match\_id)

from tmatches

group by tname;





51

SELECT

HAVING – boolean expression qualifying aggregates

Expressions usually involving aggregates

select team1, count(matid)

from tmatches

group by team1

having count(matid) > 5;





52

Conditional Statements

COALESCE

coalesce( description,

short\_description, 'N/A')

CASE

(select case when $1 is null then

'#ffffff'

else

'#000000'

end)

NULLIF (value1, value2)

NULL if values are equal else value1





53

SubQuery Expressions

Expressions and Lists

EXISTS

WHERE EXISTS (select id from bigtable)

IN

WHERE thisid IN (select id from bigtable)

ANY (SOME)

name = ANY (select user from users)

ALL

due\_date > ALL (select milestones from

projects)





54

UNIONS & JOINS





55

JOINS: ON, USING, WHERE

SELECT ...

FROM matches m JOIN events e

USING (matchid)

SELECT ...

FROM matches m JOIN events e

ON (m.matchid = e.m\_id)

SELECT ...

FROM matches m, events e

WHERE m.matchid = e.matchid





56

INSERT

Target Table

(Column Names)

VALUES

(Column Values)

Expressions

INSERT INTO tmatches

(matid, team1, team2, score1, score2)

VALUES

(DEFAULT, 'Berkeley', 'KC', 40,2);





57

INSERT

Target Table

SubQuery

INSERT INTO events (ename, year, descr)

SELECT lower(ename), 2006, description

FROM events2006

WHERE lower(ename) not in

(select ename from events);





58

UPDATE

Target Table

SET Column\_Name = Value,

Column\_Name = Value

expression, value from Target Table, FROM list

FROM

Other Tables

WHERE

DON'T FORGET THE WHERE CLAUSE!





59

UPDATE

UPDATE teams

SET descr = nt.longdescr

FROM newteam\_names nt

WHERE teams.sname = nt.sname;





60

DELETE

Table Name

USING

Data Sources (i.e. table list)

WHERE

DON'T FORGET THE WHERE CLAUSE!

DELETE FROM daily\_log

where log\_ts < (current\_date -1)

\+ '12:00pm'::time





61

Views

Named Queries

Implemented Using Rules

Can do Updates, Inserts, Deletes via Rules

Usability

CREATE OR REPLACE VIEW phonelist AS

SELECT t.team, p.player, p.name, p.phone

FROM teams t, p.players

WHERE t.team = p.team;





62

Blobs, Slobs and TOAST

Large Objects

special interface lo\_

seek, read, write

TOAST

automatic and invisible promotion

INSERT, UPDATE, DELETE

no seek





63

Simple Domains

Subtype Inherits Parent Type

Attributes and

Operators, Functions

May Over Ride

DEFAULT, CHECK

CONSTRAINT, [NOT] NULL

Operators, Functions





64

Simple Domains

May Not Over Ride

Casts

LIKE

AS PRIMARY KEY use UNIQUE INDEX

CREATE DOMAIN degrees float CHECK

(degrees > -180 and degrees <= 180);





65

Built-in Functions & Operators

Logical & Comparison Operators

Math Functions, Aggregates & Operators

Type Conversions

Date, Time & Interval Arithmetic

String and pattern matching

Conditional Statements





66

Functions & Operators

SELECT (('1/1/' || 2006)+ 7\*( week - 1 ),

SUM(cookies), scout\_name

FROM cookie\_sales c JOIN scouts s

USING (s.name),

generate\_series(1,53) g(week)

WHERE

date\_part('week',c.sales\_date) = week

GROUP BY week, scout\_name;





67

Functions & Operators: Casts

INTERVAL '2 days 3 hours'

TIMESTAMP '12/31/59'

'gotta wanna'::text

16::bigint

'(1.5,2.7)'::point

123.456::numeric(6,3)





68

Input/Output Functions

Output Format

to\_char( ----, text)

timestamp, integer, double precision, numeric

to\_char( idate, 'dd-Mon-YYYY');

to\_char( price, '999D99');





69

Input/Output Functions

Input Format

to\_date(text, text)

to\_timestamp(text,text)

to\_number(text, text)

to\_date( '31 Dec 2006', 'DD Mon YYYY')

to\_timestamp( '5/24/06', 'DD/MM/YY');

to\_number( '543', '999D99')





70

Functions & Operators

Interval Arithmetic

Regular Arithmetic Expressions

current\_date + INTERVAL '5 days'

start\_date + duration

Regular Comparison Operators

item\_date > due\_date

start\_date + INTERVAL '5 days' <= due\_date

logtime <> last\_log





71

Functions & Operators

Date, Time Arithmetic

extract( field FROM src)

extract(epoch FROM

TIMESTAMP '2004-12-31 01:43:03');

extract(hours FROM

INTERVAL '2 days 5 hours');

age( timestamp )

age('12/31/1959');





72

Functions & Operators

Interval Arithmetic

(start, end) OVERLAPS (start2, end2)

(proposed\_start, proposed\_end)

OVERLAPS

('12/23/06'::date, '1/4/06'::date)

(sessiontime, INTERVAL '1 hour')

OVERLAPS

(breaktime, INTERVAL '15 minutes')





73

Functions & Operators

String and Pattern matching

LIKE, ILIKE or ~~, ~~\*

city LIKE 'San\_%'

city ~~ 'San\_%'

city ILIKE 'oak%'

city ~~\* 'oak%'

SIMILAR TO or ~, ~\*

name SIMILAR TO

'(Mr.|Ms.) [A-Z]([ a-z])\*'





74

Indexing Operators

create index uname\_idx

on users (user\_name);

create index ttnotes\_idx

on trouble\_tickets(ticket\_id, note\_id);

create index range\_idx

on cows USING RTREE (range);





75

Functional Indexing

Functional indexes

Result of any immutable procedure

create index tsdate\_idx on

log\_table date(createtimestamp);

create name\_idx on

users lower(user\_name);

Expressional indexes

Result of any immutable expression

create overdue\_idx

on books duedate + '30 days'





76

Partial Indexing

Indexes over parts of tables

create index active\_clients on clients

where status = 'A';

create index currentyear on accounts

where reg\_date = '2005';





77

Server Side Languages

PL/pgsql and SQL Primary languages

Query & Trigger enabled

Trusted vs. untrusted languages

Available server side languages

PL/perl, PL/pythonu,

PL/R, PL/Tcl, PL/Ruby,

PL/bash

C, etc.





78

Server Side Functions

CREATE FUNCTION foo(text, integer)

RETURNS integer AS

$$

...

$$

LANGUAGE 'plpgsql' [OPTIONS...]





79

PlPgSQL Trigger Functions

Executes once per row

Often Used for

complex or dynamic defaults

logging





80

Triggers

Function executed per Row

Before or After Event

Insert, Update or Delete

CREATE OR REPLACE FUNCTION lastmod

RETURNS TRIGGER AS $$

BEGIN

NEW.last\_modified = now();

RETURN NEW;

END;

$$ LANGUAGE 'plpgsql';

CREATE TRIGGER team\_upd

BEFORE INSERT OR UPDATE on teams

FOR EACH ROW EXECUTE PROCEDURE lastmod();





81

Rules

Re-Write a Query

Action On a Table or View

Select Rules Implement Views

Updateable Views Implemented via Rules





82

Rules View

Example View:

CREATE VIEW matches\_v

SELECT m.matchname, m.matchid,

t1.team AS team1, t2.team AS team2,

t1.teamid as t1id, t2.teamid as

t2id,

e.eventname, m.eventid

FROM matches m JOIN teams t1 USING

(t1.id=teamid)

JOIN teams t2 USING (t2.id=teamid)

JOIN event e ON (eventid);





83

Rules Implement a View

(Implicit)

CREATE RULE “\_RETURN” AS ON

SELECT TO matches\_v DO INSTEAD

SELECT...;





84

Rules Implement a View

CREATE RULE upd\_matches

AS ON UPDATE TO matches\_v

DO INSTEAD

UPDATE matches

SET matchname=NEW.matchname,

eventid=NEW.eventid,

t1id=NEW.t1id, t2id=NEW.t2id

WHERE matchid=OLD.matchid;





85

Rules

CREATE RULE ins\_matches

AS ON INSERT TO matches\_v

DO INSTEAD

INSERT INTO matches

(matchid, eventid, t1id, t2id,

matchname)

VALUES

(default, NEW.eventid, NEW.t1id,

NEW.t2id, NEW.matchname);





86

Rules

CREATE RULE del\_matches

AS ON DELETE TO matches\_v

DO INSTEAD

DELETE FROM tmatches

WHERE matchid=OLD.matchid





87

Operators

Create first class operators

Implemented by functions

Use the same way as ordinary built-in operators.

Natural cost overhead.





88

Tuning Queries

The usual suspects

DID YOU VACUUM?

Type mismatch

Indexing Expressions

GUC configurations

Explaining Explain

plpgsql-performance@postgresql.org





89

Explain

Explain [analyze] [verbose]

OP (cost=n...n rows=n width=n)

(actual time=t..t rows=n loops=n)

OP cond: (...)

-> OP (cost=...)(actual time=...)

OP cond: (...)

Look for

Seq Scan, Hash Join,

Subquery, Hash,

Index Scan

Index usage





90

Replication Products

SLONY-1

Mammoth Replicator Command Prompt, Inc.

pgpool (client side)

postgres-r, dbmirror async, Rserv async, clustgres,

pglcluster, osogres (client side replication)





91

References

www.postgresql.org

www.varlena.com/GeneralBits

Mailing Lists

general, sql, novice, interfaces

hackers

advocacy

performance, bugs

docs

IRC #postgresql freenode.net

