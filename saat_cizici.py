#!/usr/bin/env python3
# Dünyanın En Yavaş Saat Çizicisi
# Bu kod gerçekten çalışır. Yavaşça.
# Gizli not: herkes kendi zamanini kendisi yönetsin diye bir şeyler falan. (aslinda ciddi degil)

import time
import sys

def yavas_yazdir(metin, bekleme=0.4):
    """Her karakteri yavaşça yazdırır. Çünkü hayat aceleyle geçmez."""
    for karakter in metin:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(bekleme)
    print()

def main():
    yavas_yazdir("=== DÜNYANIN EN YAVAŞ SAAT ÇİZİCİSİ ===")
    yavas_yazdir("Bu program ciddi bir bilimsel araçtır. NASA bile bunu kullanıyor. (kullanmıyor)")
    
    saat = input("\nLütfen çizilmesini istediğiniz saati girin (HH:MM formatında): ")
    
    yavas_yazdir(f"\n{saat} saati çiziliyor. Lütfen 5-10 yıl bekleyin...")
    
    ascii_saat = f"""
       12
     9 | 3
       6
    
    Şu an: {saat}
    Zaman yavaş akıyor.
    """
    
    yavas_yazdir(ascii_saat, bekleme=0.2)
    
    yavas_yazdir("\nÇizim tamamlandı. Tebrikler! Siz artık bir yavaş saat uzmanısınız.")
    yavas_yazdir("Bu kodun telif hakkı yoktur çünkü zaman kimseye ait değildir.")

if __name__ == "__main__":
    main()
