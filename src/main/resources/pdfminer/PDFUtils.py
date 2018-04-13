try: import requests
except: from Lib import requests

try:
    from .pdfinterp import PDFResourceManager, PDFPageInterpreter
    from .pdfpage import PDFPage
    from .converter import XMLConverter, HTMLConverter, TextConverter
    from .layout import LAParams
except:
    from Lib.pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from Lib.pdfminer.pdfpage import PDFPage
    from Lib.pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
    from Lib.pdfminer.layout import LAParams

from cStringIO import StringIO
from io import BytesIO, SEEK_SET, SEEK_END

class ResponseStream(object):
    def __init__(self, request_iterator):
        self._bytes = BytesIO()
        self._iterator = request_iterator

    def _load_all(self):
        self._bytes.seek(0, SEEK_END)
        for chunk in self._iterator:
            self._bytes.write(chunk)

    def _load_until(self, goal_position):
        current_position = self._bytes.seek(0, SEEK_END)
        while current_position < goal_position:
            try:
                current_position = self._bytes.write(next(self._iterator))
            except StopIteration:
                break

    def tell(self):
        return self._bytes.tell()

    def read(self, size=None):
        left_off_at = self._bytes.tell()
        if size is None:
            self._load_all()
        else:
            goal_position = left_off_at + size
            self._load_until(goal_position)

        self._bytes.seek(left_off_at)
        return self._bytes.read(size)
    
    def seek(self, position, whence=SEEK_SET):
        if whence == SEEK_END:
            self._load_all()
        else:
            self._bytes.seek(position, whence)

def PDFUrlToString(url):
    resp = requests.get(url, stream=True)
    fp = ResponseStream(resp.iter_content(1024))
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        yield retstr.getvalue()
    raise StopIteration


