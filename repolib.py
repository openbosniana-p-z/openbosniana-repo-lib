#!/usr/bin/python3

import subprocess

def block1():
    put_do_paketa ="/home/deni/Desktop/hdd/openbosnianp-za-repo-p-z/dodaj"
    tacka_deb = "/*.deb"
    reprepro_prvo = "reprepro --ask-passphrase -Vb . includedeb OpenBosniana-LIB"
    komanda_reprepro_sastavi = reprepro_prvo + " " + put_do_paketa + tacka_deb
    komanda_reprepro = komanda_reprepro_sastavi

    subprocess.run(komanda_reprepro, shell=True)
    
    print("Zavrseno dodavanje paketa sa patha "+ put_do_paketa)

def block2():
    brisanje="/home/deni/Desktop/openbosniana-repo-p-z/openbosniana-repo-lib"
    imena_paketa_brisanje=input("Imena paketa sa jednim razmakom: ")
    reprepro_jedan="reprepro --ask-passphrase -Vb "
    reprepro_dva = " remove OpenBosniana-LIB "
    brisanje_sastavi= reprepro_jedan + brisanje + reprepro_dva + imena_paketa_brisanje
    brisi_reprepro = brisanje_sastavi

    subprocess.run(brisi_reprepro, shell=True)

def block3():
    bez_indexa ="/home/deni/Desktop/openbosniana-repo-p-z/openbosniana-repo-lib"
    prikaz_postojeci_bez_indexa = "sudo reprepro -Vb "
    dump_bezindexa =" dumpunreferenced"
    sastavi_bez_indexa = prikaz_postojeci_bez_indexa + bez_indexa + dump_bezindexa
    bez_indexa_su = sastavi_bez_indexa

    subprocess.run(bez_indexa_su, shell=True)
    
    print("Bez indexa su "+ bez_indexa_su)

def block4():
    bez_indexa_brisanje ="/home/deni/Desktop/openbosniana-repo-p-z/openbosniana-repo-lib"
    prikaz_postojeci_bez_indexa_brisanje = "sudo reprepro -Vb "
    dump_bezindexa_brisanje =" deleteunreferenced"
    sastavi_bez_indexa_brisanje = prikaz_postojeci_bez_indexa_brisanje + bez_indexa_brisanje + dump_bezindexa_brisanje
    bez_indexa_su_brisanje = sastavi_bez_indexa_brisanje

    subprocess.run(bez_indexa_su_brisanje, shell=True)

def block5():
    export_put ="/home/deni/Desktop/openbosniana-repo-p-z/openbosniana-repo-lib"
    export_prvo = "reprepro --ask-passphrase -Vb "
    export_drugo =" export"
    sastavi_export = export_prvo + export_put + export_drugo
    export_komanda = sastavi_export

    subprocess.run(export_komanda, shell=True)

def block6():
    deb_put =input("Put do .deb paketa: ")
    deb_prvo = "dpkg-deb --build "
    sastavi_deb = deb_prvo + deb_put
    deb_komanda = sastavi_deb

    subprocess.run(deb_komanda, shell=True)

def block7():
    deb_put_root =input("Put do .deb paketa: ")
    deb_prvo_root = "dpkg-deb --build --root-owner-group "
    sastavi_deb_root = deb_prvo_root + deb_put_root
    deb_komanda_root = sastavi_deb_root

    subprocess.run(deb_komanda_root, shell=True)


def main():
    print("Izaberi opciju:")
    print("1. Dodavanje 1")
    print("2. Brisanje 2")
    print("3. Prikazi postojecih bez indeksa 3")
    print("4. Brisanje postojecih bez indeksa 4")
    print("5. Export upisanih paketa 5")
    print("6. Sastavi deb paket 6")
    print("7. Sastavi deb paket kao ROOT 7")
    choice = input("Upisi broj: ")
    
    if choice == "1":
        block1()
    elif choice == "2":
        block2()
    elif choice == "3":
        block3()
    elif choice == "4":
        block4()
    elif choice == "5":
        block5()
    elif choice == "6":
        block6()
    elif choice == "7":
        block7()
    else:
        print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()

#print("-     SOURCE PAKETI         -")
#print("dpkg-buildpackage -us -uc -S")
#print("reprepro -b /home/repo/1 includedsc OpenBosniana-P-Z /home/denios/Desktop/source_packages/MJESTOPAKETA.dsc")
#print("--------------------------------------------------------")"""
