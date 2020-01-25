import sys
import goslate
import polib
import langdetect
import time
from urllib.error import HTTPError

gs = goslate.Goslate()

podata = polib.pofile(sys.argv[1])

podata.metadata['PO-Revision-Date'] = time.strftime("%Y-%m-%d %H:%M%z"),

for entry in podata:
    langs = {}
    for l in langdetect.detect_langs(entry.msgid):
        langs[l.lang] = l.prob
    print(entry.msgid, langs)
    if entry.msgstr == '' and not langs.get('ja'):
        try:
            entry.msgstr = gs.translate(entry.msgid, 'ja')
        except HTTPError as e:
            print(e)
            break
        print(entry.msgstr)
        time.sleep(3)

podata.save(sys.argv[1])
