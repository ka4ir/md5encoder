import hashlib

sifreleyici = hashlib.md5()
metin = input("lütfen Hashlenecek metini giriniz: ")
sifreleyici.update(metin.encode("utf-8"))
hash = sifreleyici.hexdigest()
print("Çıktı>>> %s" % hash)