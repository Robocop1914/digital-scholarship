#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pywikibot import family
import pywikibot, json, csv, sys

"""
    Notes:
    We need to remove the built in throttling because we 
    are working on our own localhost running wikibase, we don't
    care if we do a ton of requests, we are likely the only user
"""
# over write it
def wait(self, seconds):
    """Wait for seconds seconds.
    Announce the delay if it exceeds a preset limit.
    """
    pass
    # if seconds <= 0:
    #     return

    # message = (u"Sleeping for %(seconds).1f seconds, %(now)s" % {
    #     'seconds': seconds,
    #     'now': time.strftime("%Y-%m-%d %H:%M:%S",
    #                          time.localtime())
    # })
    # if seconds > config.noisysleep:
    #     pywikibot.output(message)
    # else:
    #     pywikibot.log(message)

    
    # time.sleep(seconds)

pywikibot.throttle.Throttle.wait = wait

# # if len(sys.argv) == 1:
# #     raise ValueError('Missing input CSV file')

# # csv_path = sys.argv[1]
# # csv_file = open(csv_path,'r')

# # csv_reader = csv.DictReader(csv_file)

# # If you changed the name of the site to something else make sure to change it here
    
site = pywikibot.Site('ldwg', 'ldwg')
site.login()

repo = site.data_repository()

some_labels = {"en": "Clifford B. Anderson"}
new_item = pywikibot.ItemPage(repo)
new_item.editLabels(labels=some_labels, summary="Setting labels")

claim = pywikibot.Claim(repo, u'P4') # employer
target = pywikibot.ItemPage(repo, u"Q3") # Vanderbilt University
claim.setTarget(target)
new_item.addClaim(claim, summary=u'Adding employer claim')
    
claim = pywikibot.Claim(repo, u'P6') # instance of
target = pywikibot.ItemPage(repo, u"Q5") # human
claim.setTarget(target)
new_item.addClaim(claim, summary=u'Adding type claim')

#P39 position held
#P101 field of work
#P106 occupation
#P463 member of

print(new_item.getID())
