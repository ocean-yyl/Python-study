import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,JSON,SmallInteger,Boolean,DateTime

import datetime

engine = sqlalchemy.create_engine("mysql+pymysql://test:123456@127.0.0.1:3306/sailor",echo=True)
Base = declarative_base()


class Pool(Base):
	__tablename__ = 'pool'
	id = Column(Integer, nullable=False,
				   primary_key=True, comment='id自增主键')
	api = Column(String(32), nullable=False, comment='接口名称')
	url = Column(String(255), nullable=False, comment='接口地址')
	request_id = Column(String(32), nullable=False,
						   comment='标识特定请求，根据request生成md5')
	request = Column(JSON, nullable=False,
						comment='请求体，包括header、cookie、method、body or query')
	state = Column(SmallInteger, nullable=False,
					  comment='0-未爬取，1-成功，2-失败，3-爬取中')
	times = Column(Integer, nullable=True, comment='抓取次数')
	need_update = Column(Boolean, default=None, comment='是否需要更新：0-不需要，1-需要')
	last_success_time = Column(
		DateTime, default=None, comment='上次抓取成功的时间')
	created = Column(DateTime, nullable=False,
						default=datetime.datetime.now, comment='创建时间')
	update = Column(DateTime, nullable=False,
					   default=datetime.datetime.now, comment='更新时间')
	remark = Column(String(128), default='', comment='备注')


class Config(Base):
	__tablename__ = 'config'
	id = Column(Integer, nullable=False,
				primary_key=True, comment='id自增主键')
	api = Column(String(32), nullable=False, comment='api名称')
	md5_type = Column(SmallInteger, nullable=True,
				   comment='md5类型：1-白名单，2-黑名单')
	md5_field = Column(JSON,nullable=True,comment='md5值')
	times = Column(Integer,nullable=True,comment='失败最大爬取次数')
	interval = Column(Integer,nullable=True,comment='爬取中状态重新爬取间隔，单位秒')
	need_update = Column(SmallInteger,nullable=True,comment='是否需要更新：0-不需要，1-需要')
	created = Column(DateTime,nullable=False,default=datetime.datetime.now, comment='创建时间')
	updated = Column(DateTime, nullable=False,
				  default=datetime.datetime.now, comment='更新时间')
	remark = Column(String(128), default='', comment='备注')

if __name__ == '__main__':
	# 创建继承自Base的所有表
	Base.metadata.create_all(engine)

