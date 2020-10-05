# FERI-time_table
 Za vse, ki jih gre klikanje po timetable počasi na živce™


### Za kaj gre?
  - avtomatizacijski program, napisan v Pythonu, ki s pomočjo Seleniuma dostopa do vsebin na spletni strani Wise Time Table. 


### Kako stvar deluje?
  - najprej preneses ustrezno različico webdriver-ja za tvoj chrome iz https://chromedriver.chromium.org/downloads (različico lahko preveriš z odpiranje Chrome-a, potem izbereš tri pike na desnem delu okna in klikneš *Pomoč > O Google Chromu*)
  - webdriver premakneš v mapo, kamor boš shranil/a kodo programa (.py končnica) oz. sam program (če kodo programa pretvoriš v .exe datoteko)
  - program zdaj samo zaženeš in se ti magično prikaže tvoj urnik

### Kako program uporabim?
  - če imaš na svojem računalniku že naložen program, ki lahko "bere" in izvaja kodo programa, lahko tega uporabiš
  - če se prvič srečaš s kodo in ti je beseda Python tuja, boš potreboval/a kodo programa pretvoriti v .exe datoteko (glej spodaj)

### Zakaj se mi magično prikaže napačen urnik?
  - preveri ali se tvoj urnik nahaja na naslovu https://www.wise-tt.com/wtt_um_feri/
  - če se ne, prekopiraj svoj url wise_timetable urnika v kodo, kjer se nahaja  *driver = start_chrome()* in znotraj oklepajav vnesi svoj url kot "moj_url" ali 'moj_url'
  - če se urnik nahaj na prej omenjenem naslovu, ampak ne prikazuje pravega programa ali letnika, poišči del kode  *navigate_to_right_program_year(driver)*  in vanj dopiši svoj program in letnik v obliki  *navigate_to_right_program_year(driver, "moj_program", "letnik")* ali  *navigate_to_right_program_year(driver, 'moj_program', 'letnik')*
  - npr. si študent/ka drugega letnika visoko šolskega programa informatike, zato zapišeš  *navigate_to_right_program_year(driver, "INFORMATIKA IN TEHNOLOGIJE KOMUNICIRANJA (BV30)", 2)*  ali *navigate_to_right_program_year(driver, "INFORMATIKA IN TEHNOLOGIJE KOMUNICIRANJA (BV30)", "2")*
  - ime tvojega programa more biti **NUJNO** enak tistemu, ki je zapisan med opcijami pri izbiri urnikov
  - zgoraj omenjene stvari lahko spreminjaš v navadni *Beležnici (Notebook)*, samo desno klikni na kodo programa in izberi  *Za odpiranje uporabi > Beležnica* in tam spreminjaj zadeve (na koncu ne pozabi shraniti datoteke 😉)

### Kako lahko pretvorim kodo programa v .exe datoteko?
  - za pretvorbo boš potreboval/a programski jezik Python, preneseš si ga tu https://www.python.org/downloads/
  - slediš lahko navodilu [prve spletne strani](https://www.geeksforgeeks.org/convert-python-script-to-exe-file/) ali [druge spletne strani](https://nitratine.net/blog/post/convert-py-to-exe/) (priporočam ti, da poskusiš s prvo spletno stranjo, saj Python občasno posodabljajo in se lahko zgodi, da druga rešitev ne bo delovala)
