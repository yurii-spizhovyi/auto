from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine("postgresql://admin:admin@localhost:5432/hw26")
auto_commit = engine.execution_options(isolation_level="AUTOCOMMIT")
session: Session = sessionmaker(auto_commit)()
