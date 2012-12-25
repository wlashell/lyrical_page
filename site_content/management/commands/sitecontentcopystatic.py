import os.path
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

import site_content.settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        print 'You have configured the following entries for your static file directories:'
        filedirs = getattr(settings, 'STATICFILES_DIRS')

        print '----'
        cnt = 0
        for filedir in filedirs:
            print '%s) %s' % (cnt, filedir)
            cnt += 1

        print '----'

        selected_filedir = filedirs[int(raw_input('Please select the entry to install the boilerplate files into: '))]

        if not os.path.exists(selected_filedir):
            raise CommandError('The specified static file directory does not exist. Please create the directory and try again.')

        print 'You have selected the following entry: '
        print '%s' % selected_filedir

        confirm_str = str(raw_input('Please confirm the boilerplate file installation (Y/N): '))

        if confirm_str.upper() not in ('Y', 'N'):
            raise CommandError('You have selected an invalid entry. Files will not be installed')
        elif confirm_str.upper() == 'N':
            print 'File installation is not confirmed. Cancelling operation'
        else:
            print 'File installation confirmed. Installing files now.'

        # iterate across static entries and copy files
        # This is a two pass operation, if any file already exists the command will stop
        # operations.
        try:
            print 'Testing path: %s' % os.path.join(selected_filedir, 'css')
            if not os.path.exists(os.path.join(selected_filedir, 'css')):
                os.mkdir(os.path.join(selected_filedir, 'css'))

            print 'Testing path: %s' % os.path.join(selected_filedir, 'js')
            if not os.path.exists(os.path.join(selected_filedir, 'js')):
                os.mkdir(os.path.join(selected_filedir, 'js'))

        except IOError:
            raise CommandError('Holding directory write error has occurred. Please check your path configuration.')

        files_to_copy = getattr(site_content.settings, 'STATICFILES_TO_COPY')

        for file_to_copy in files_to_copy['css']:
            if os.path.exists(os.path.join(selected_filedir, 'css', file_to_copy)):
                raise CommandError('%s already exists in the target directory. Files will not be installed.' % file_to_copy)
            elif not os.access(os.path.join(selected_filedir, 'css'), os.W_OK):
                raise CommandError('%s cannot be created. Files will not be installed.' % file_to_copy)
            else:
                shutil.copy(os.path.join(site_content.settings.SITE_CONTENT_DOC_ROOT, file_to_copy),
                            os.path.join(selected_filedir, 'css', file_to_copy))

        for file_to_copy in files_to_copy['js']:
            if os.path.exists(os.path.join(selected_filedir, 'js', file_to_copy)):
                raise CommandError('%s already exists in the target directory. Files will not be installed.' % file_to_copy)
            elif not os.access(os.path.join(selected_filedir, 'js'), os.W_OK):
                print 'tried: %s' % os.path.join(selected_filedir, 'js', file_to_copy)
                raise CommandError('%s cannot be created. Files will not be installed.' % file_to_copy)
            else:
                shutil.copy(os.path.join(site_content.settings.SITE_CONTENT_DOC_ROOT, file_to_copy),
                            os.path.join(selected_filedir, 'js', file_to_copy))

        print 'All files have been installed correctly.'
