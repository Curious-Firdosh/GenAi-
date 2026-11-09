from sqlalchemy.orm  import sessionmaker
from sqlalchemy import create_engine



db_url = "postgresql://neondb_owner:npg_vig5f0JTLBkX@ep-late-mode-ah128t13-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)