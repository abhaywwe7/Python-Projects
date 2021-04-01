import pyqrcode
from pyqrcode import QRCode
link = "https://www.google.com/search?q=love+quotes&rlz=1C1GCEA_enIN899IN899&oq=lov&aqs=chrome.2.69i57j46i433j0i433l2j0i131i433j46i433j0i433j69i61.7547j0j7&sourceid=chrome&ie=UTF-8"
url = pyqrcode.create(link)
url.svg("lovequoteR.svg", scale=7)