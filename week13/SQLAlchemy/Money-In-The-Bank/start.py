from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base
from controllers import MainController
from views import MainView

from settings import DB_NAME


engine = create_engine(DB_NAME)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

main_controller = MainController(session)
main_view = MainView(main_controller)

main_view.render()
