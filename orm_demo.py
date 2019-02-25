#  SQLAlchemy框架负责orm映射
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 对象基类
Base = declarative_base()


# user类
class User(Base):
    # 表名
    __tablename__ = 'user'
    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接  '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库'
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/testdb')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session
session = DBSession()
# 创建query查询，filter是where条件，最后调用one（）返回唯一行，all（）返回所有行
user = session.query(User).filter(User.id == '1').one()
print(user.name + user.id)
session.close()

