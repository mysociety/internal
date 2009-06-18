#!/usr/bin/python2.5
#
# send_mails.py: Send out the mySociety site stats emails
#
# Copyright (c) 2009 UK Citizens Online Democracy. All rights reserved.
# Email: louise@mysociety.org; WWW: http://www.mysociety.org/
#

import optparse
import sys
import os
from datetime import date, timedelta
sys.path.append("../pylib")
import sitestats
os.environ['DJANGO_SETTINGS_MODULE'] = 'sitestats.settings'
from django.db import models
from django.contrib.auth.models import User
from sitestats.newsletters.models import CommonBaseMeasuresNewsletter, TWFYNewsletter, Newsletter, Subscription
from sitestats.newsletters.sources import piwik
from sitestats.newsletters.sources import google
from sitestats.newsletters.common import send_newsletter

###############################################################################
# Read parameters

parser = optparse.OptionParser()

parser.set_usage('''
./send_mails.py [OPTIONS]

Send out mySociety site stats emails. Run with "--help" to see available options.

''')

parser.add_option('--verbose', action='store_true', default=False, dest="verbose", help='Produce extra debugging output')
parser.add_option('--only', dest='only', default=None, help='Only send email for one user identified by username')
(options, args) = parser.parse_args()

sources = {'piwik' : piwik.Piwik(), 'google' : google.Google()}

date = date.today()

# get nearest past Sunday 
while date.weekday() != 6:
    date = date - timedelta(days=1)


newsletter_types = [CommonBaseMeasuresNewsletter, TWFYNewsletter]                 
                         
for newsletter_type in newsletter_types:
    for newsletter in newsletter_type.objects.all():
        send_newsletter(newsletter, date, sources, options)
