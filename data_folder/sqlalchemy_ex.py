import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = sa.create_engine('sqlite:///:memory:')
conn = engine.connect()
meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
               sa.Column('critter', sa.String, primary_key=True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float))
meta.create_all(engine)
conn.execute(zoo.insert().values(critter='bear', count=2, damages=1000.0))
conn.execute(zoo.insert().values(critter='weasel', count=1, damages=2000.0))
conn.execute(zoo.insert().values(critter='duck', count=10, damages=0))
result = conn.execute(zoo.select())
rows = result.fetchall()
print(rows)



conn = sa.create_engine('sqlite:///zoo.db')
Base = declarative_base()
class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)
    
    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages
    
    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)
    
Base.metadata.create_all(conn)
first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)
first

Session = sessionmaker(bind=conn)
session = Session()
session.add(first)
session.add_all([second, third])
session.commit()