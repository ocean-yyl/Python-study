# -*- coding:utf-8 -*-
# 创建session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from cook_db.db_create import engine, Pool, Config
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

session: Session = sessionmaker(bind=engine)()  # 线程不安全


def add(i: int):
	con = Config()
	con.api = str(i)

	session.add(con)  # 添加数据
	session.commit()  # 提交数据


if __name__ == '__main__':
	add(1123)
