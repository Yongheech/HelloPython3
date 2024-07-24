# import sqlite3
import pymysql

from alpacatnt.oop.models import SungJuk

# 데이터베이스 연결 문자열
host = '54.180.227.105'
dbname = 'clouds2024'
user = 'clouds2024'
passwd = 'clouds2024'

# 성적 DAO 클래스
class SungJukDAO:

    # 데이터베이스 연결객체와 커서 생성
    @staticmethod
    def _make_conn():
        """
        파이썬에서 마리아디비로 콘솔을 연결하는 함수
        :return:
        """
        conn = pymysql.connect(host=host, user=user,
                               password=passwd, database=dbname, charset ='utf8')
        cursor = conn.cursor()
        return conn, cursor

    # 데이터베이스 연결객체와 커서 종료
    @staticmethod
    def _dis_conn(conn,cursor):
        """
        연결된 콘솔을 닫는 함수
        :param conn: 연결된 conn 을 닫는다
        :param cursor: 연결된 cursor 을 닫는다
        :return:
        """
        cursor.close()
        conn.close()
    @staticmethod
    def insert_sungjuk(sj):
        """
        입력한 성적데이터를 sungjuk 테이블에 저장
        :param sj: 테이블에 저장할 성적데이터
        :return: cnt: 테이블에 성공적으로 저장된 데이터 건수
        """
        sql = 'insert into sungjuk (name, kor, eng, mat, tot, avg, grd)\
            values (%s,%s,%s,%s, %s,%s,%s)'
        conn, cursor = SungJukDAO._make_conn()
        params = (sj.name,sj.kor,sj.eng,sj.mat,sj.tot,sj.avg,sj.grd)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn,cursor)
        return cnt

    @staticmethod
    def select_sungjuk():
        """
        sungjuk 테이블에서 모든 성적 데이터(번호/이름/국어/영어/수학/등록일)를 읽어옴
        :return: 조회된 성적데이터 객체
        """
        sjs = []
        sql = 'select sjno, name,kor,eng,mat, substr(regdate,1,11) regdate from sungjuk'
        conn,cursor = SungJukDAO._make_conn()
        cursor.execute(sql)
        rs = cursor.fetchall()

        for r in rs: # 조회결과를 SungJuk 객체에 개별 저장
            sj = SungJuk(r[1],r[2],r[3],r[4],)
            sj.sjno = r[0]
            sj.regdate = r[5]
            sjs.append(sj)

        SungJukDAO._dis_conn(conn, cursor)
        return sjs

    @staticmethod
    def selectone_sungjuk(sjno):
        """
        sungjuk 테이블에서 특정학생 성적데이터를 읽어옴
        :param sjno: 조회할 학생의 학생번호
        :return: sj: 조회된 학생의 성적데이터
        """
        sql = 'select * from sungjuk where sjno = %s'
        conn, cursor = SungJukDAO._make_conn()
        params = (sjno,)
        cursor.execute(sql,params)
        rs = cursor.fetchone()
        if rs:
            sj = SungJuk(rs[1],rs[2],rs[3],rs[4])
            sj.sjno = rs[0]
            sj.tot = rs[5]
            sj.avg = rs[6]
            sj.grd = rs[7]
            sj.regdate = rs[8]
        else:
            sj = None

        SungJukDAO._dis_conn(conn, cursor)
        return sj
    @staticmethod
    def update_sungjuk(sj):
        """
        sungjuk 테이블에 특정학생의 성적데이터를 새로운 성적데이터로 수정함
        :param sj: 수정할 학생의 성적데이터들
        :return:cnt: 테이블의 성공적으로 수정된 데이터 건수
        """
        sql = 'update sungjuk set  kor=%s, eng=%s, mat=%s, tot=%s, avg=%s, grd=%s \
           where sjno = %s'
        conn, cursor = SungJukDAO._make_conn()
        params = (sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd, sj.sjno)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return cnt

    @staticmethod
    def delete_sungjuk(sjno):
        """
        sungjuk 테이블의 특정학생의 성적데이터를 삭제함
        :param sjno: 삭제할 학생의 학생번호
        :return:cnt: 테이블의 성공적으로 삭제된 데이터 건수
        """
        sql = 'delete from sungjuk where sjno = %s'
        conn, cursor = SungJukDAO._make_conn()
        params = (sjno,)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn,cursor)
        return cnt