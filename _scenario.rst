>>> from login import login
>>> from config import config
>>> from py_hibiscus import HibiscusSocket

>>> s = HibiscusSocket(login.password,config.xmlrpc_host,config.xmlrpc_port,config.proto,login.username)
>>> s is not None
True

>>> alle_konten = s.konto_find()
>>> len(alle_konten) > 0
True

>>> k0 = alle_konten[0]

>>> k0.has_key("id") # zb '1'
True

>>> k0.has_key("kundennummer") # zb '9876543210'
True

>>> k0.has_key("name") # zb 'Martin Muster'
True

>>> k0.has_key("blz")
True

>>> k0.has_key("saldo_datum")
True

>>> k0.has_key("bic") # zb 'DRESDEFFXXX', 
True

>>> k0.has_key("iban") # zB 'DE37370800400321321300', 
True

>>> k0.has_key("saldo")
True

>>> k0.has_key("kontonummer")
True

>>> k0.has_key("waehrung") # zB 'EUR'
True

>>> k0.has_key("bezeichnung") # zB 'Kontokorrent'
True

>>> k0.has_key("kommentar") # zb ''
True

>>> bankname = s.get_bank_name("37010050")
>>> bankname == "Postbank"
True

>>> s.umsatz_list_spaltenname(1)
'f1'

>>> s.umsatz_list_spaltenname(4)
'betrag'

>>> s.umsatz_list_spaltenname(7)
'verwendungszweck1'

>>> s.extract_umsatz_row("::::14,50:14.10.2020")
{'f0': '', 'f1': '', 'f2': '', 'f3': '', 'betrag': '14,50', 'datum1': '14.10.2020'}
 
>>> ul = s.umsatz_list()
>>> u0 = ul[0]
>>> u0.has_key("datum1")
True

>>> u0.has_key("betrag")
True


