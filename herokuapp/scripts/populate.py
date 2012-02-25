import os
import sys
import transaction

from sqlalchemy import engine_from_config

from ..models import (
    DBSession,
    MyModel,
    Base,
    )


def main(argv=sys.argv):
    settings = {'sqlalchemy.url': os.environ['DATABASE_URL']}
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        model = MyModel(name='one', value=1)
        DBSession.add(model)


if __name__ == '__main__':
    main()
