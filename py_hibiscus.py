#!/usr/bin/env python

import xmlrpclib

class HibiscusSocket(object):

  def __init__(self, password,xmlrpc_host="localhost",xmlrpc_port=8080,proto="https",username="admin"):
    """
    see http://www.willuhn.de/wiki/doku.php?id=develop:xmlrpc:init
    """
  
    self.proto=proto
    sock = xmlrpclib.ServerProxy ('%s://%s:%s@%s:%s/xmlrpc/' % (
        self.proto, username, password, xmlrpc_host, xmlrpc_port))
    self.sock = sock
    
  def get_bank_name(self,blz):
    return self.sock.hibiscus.xmlrpc.konto.getBankname(str(blz))
    
  def konto_find(self):
    return self.sock.hibiscus.xmlrpc.konto.find()
    
  def extract_umsatz_row(self,row):
    cols = row.split(":")
    i = 0
    res={}
    for col in cols:
      res[self.umsatz_list_spaltenname(i)] = col 
      i=i+1
    return res

  def umsatz_list_raw(self,first_day="01.01.1980",last_day="31.12.2999"):
    return self.sock.hibiscus.xmlrpc.umsatz.list("",first_day,last_day)

  def umsatz_list(self,first_day="01.01.1980",last_day="31.12.2999"):
    ul = self.umsatz_list_raw(first_day,last_day)
    res = []
    for u in ul:
      r = self.extract_umsatz_row(u)
      res.append(r)
    return res
  
  def list_methods(self):
    return self.sock.list_methods()  

            
  def umsatz_list_spaltenname(self,n):
    """
    10 : "primanota"
      Das ist eine Bankinterne Angabe. Die prima nota ist traditionell eine Liste 
      auf der alle Angaben in der Reihenfolge ihrer Eingabe aufgezeichnet sind. 
      Die Angabe dieser Primanota Seite diente dazu eine Zeile spaeter ggfs schneller 
      wieder zu finden. Heute bei der elektronischen Aufzeichnung wird es eine 
      gleiche Bedeutung haben, allerdings eben ohne dass die Liste gedruckt wird.
    """
    spalte = {
      4 : "betrag",
      5 : "datum1",
      6 : "datum2",
      7 : "verwendungszweck1",
      8 : "verwendungszweck2",
      9 : "zwischensumme",
      10 : "primanota",
      11 : "kundenreferenz"
    }
    if spalte.has_key(n):
      return spalte[n]
    return "f%s" % n   
      
              
              
              