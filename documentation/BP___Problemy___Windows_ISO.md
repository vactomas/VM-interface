# Nelze vytvořit bootovatelné ISO
	- Při pokusu rozjet Windows jako testovací systém jsem se pokoušel vytvořit ISO soubor, který by fungoval podobně jako LiveCD u Linuxu
	- Celá tato část byla založena na existujícím disku instalace VM
		- Formát RAW (.img) -> pro změnu na ISO by mělo stačit změnit příponu
	- Nefungovala ani verze s instalací Win11 (UEFI) ani Win10 (UEFI i pokus se SeaBIOS instalací)
	- K Windows není žádná dokumentace, která by naznačovala, že je toto možné
	- Lze vytvořit bootovatelné USB, které bude přenášené mezi PC ale ne ISO