
drop table emp;

CREATE TABLE emp (
                     empid int PRIMARY KEY,
                     fname varchar(30) NOT NULL,
                     lname varchar(30) NOT NULL,
                     email varchar(100) NOT NULL,
                     phone varchar(15) NOT NULL,
                     hdate date NOT NULL,
                     jobid varchar(20) NOT NULL,
                     sal int NOT NULL,
                     comm decimal(5,2),
                     mgrid integer,
                     deptid integer
);

-- 데이터 추가
insert into emp
(empid, fname, lname, email, phone,
 hdate, jobid, sal, comm, mgrid, deptid)
values (100,'steven','king','SKING','515.123.4567','2003-06-17','AD_PRES',24000, null, null, 90);

-- 데이터 조회 1 - 리스트
select empid, fname, email, jobid, deptid from emp;

-- 데이터 조회 2 - 상세
select * from emp where empid = 100;