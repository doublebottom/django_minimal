import django
from django.conf import settings
import config.settings.local as localsettings
import pprint


class DjangoInit:
    def __init__(self):
        """
        Manuelle Initialisierung der Django settings:
        settings.configure() lädt die default settings aus django.conf.global_settings.py
        überschreibt diese mit den individuellen settings aus config.settings (= **conf)
        und django.setup() initialisiert Django. Im Anschluß können alle Funktionen (Datenbank,
        Templatesystem usw. auch extern in Scripten genutzt werden können.
        """

        if not settings.configured:

            # Baue dictionary von allen Settings (config.settings) aus dem aktuellen Projekt
            conf = dict()
            for setting in dir(localsettings):
                if setting.isupper():
                    conf.update({setting: getattr(localsettings, setting)})

            settings.configure(**conf)
            django.setup()


    @classmethod
    def show_settings(cls, query='all'):

        """
        Printet die aktuellen Settings in die Konsole

        :param query: 'all' für alle Settings oder einzelner Setting-Name
        :return:
        """

        # Doppelte Settings in dir(settings), deshalb set -> sort -> list
        available_settings = list(sorted({name for name in dir(settings) if name.isupper()}))

        if query == 'all':
            print(pprint.pprint({name: getattr(settings, name) for name in available_settings}))

        elif query in available_settings:
            print({query: getattr(settings, query)})
            return

        else:
            print('Setting does not exist.')
            return


if __name__ == '__main__':
    DjangoInit().show_settings('BASE_DIR')
    DjangoInit().show_settings('STATICFILES_DIRS')








