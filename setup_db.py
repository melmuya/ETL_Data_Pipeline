from database import DatabaseManager
from models import User
from datetime import date

def setup_database():

    db_manager = DatabaseManager()

    db_manager.create_tables()

    session = db_manager.get_session()

    try:
        test_user = User(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            signup_date=date.today()
        )

        session.add(test_user)
        session.commit()

        user = session.query(User).filter_by(email="john.doe@example.com").first()
        print(f"Successfully created user: {user}")
    
    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()

    finally:
        session.close()

if __name__ == "__main__":
    setup_database()