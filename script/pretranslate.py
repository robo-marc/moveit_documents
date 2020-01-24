import sys
import goslate
import polib
import time
from urllib.error import HTTPError

gs = goslate.Goslate()

podata = polib.pofile(sys.argv[1])

podata.metadata['PO-Revision-Date'] = time.strftime("%Y-%m-%d %H:%M%z"),

for entry in podata:
    if entry.msgstr == '':
        try:
            entry.msgstr = gs.translate(entry.msgid, 'ja')
        except HTTPError:
            pass
        print(entry.msgid, entry.msgstr)
        time.sleep(1)

podata.save(sys.argv[1])
