-- 사원 - empid,fname,lname,email,phone ,
-- hdate,jobid,sal,comm,mgrid,deptid

drop table emp;

create table emp (
     empid integer primary key ,
     fname varcar(30) not null ,
     lname varcar(30) not null ,
     email varcar(100) not null ,
     phone varcar(15) not null ,
     hdate data not null ,
     jobid varcar(20) not null ,
     sal   integer not null ,
     comm  decimal(5,2)  ,
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