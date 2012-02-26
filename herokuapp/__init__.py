from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from fanstatic import Fanstatic

from herokuapp.models import appmaker
from herokuapp import models, forms

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    appmaker(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'herokuapp:static', cache_max_age=3600)
    config.add_view('herokuapp.views.view_home',
                    name="",
                    renderer="templates/home.pt")

    config.include('pyramid_formalchemy')
    # Adding the jquery libraries
    config.include('fa.bootstrap')
    # Adding the package specific routes
    config.include('herokuapp.routes')

    config.formalchemy_admin("/admin",
                             models=models,
                             forms=forms,
                             session_factory=models.DBSession,
                             view="herokuapp.forms.ModelView")

    return Fanstatic(config.make_wsgi_app())
