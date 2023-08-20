class Pojistenci:

    def __init__(self, jmeno: str, prijmeni: str, vek: int, tel_cislo: str):

        """
        Všechny níže uvedené atributy jsou zadávány uživatelem ve třídě EvidencePojistencu
        Instance třídy Pojistenci() vytvářejí kolekci v instanci třídy EvidencePojistencu()

        :param jmeno: křestní jméno pojištěnce -> STR
        :param prijmeni: příjmení pojištěnce -> STR
        :param vek: věk pojištěnce -> INT
        :param tel_cislo: telefonní kontakt na daného pojištěnce -> STR
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def __str__(self) -> str:

        return str("{:<10} {:<10} {:<10} {:<10} ".format(self.jmeno, self.prijmeni, self.vek, self.tel_cislo))

    def je_nalezen(self, jmeno_prijmeni: str) -> bool:

        """
        Metoda použita v metodě vyhledej_pojistence().
        Metoda ověřuje zda zadané jméno a přijmení odpovídá nějakému z pojištěnců.
        :param jmeno_prijmeni: -> STR
        :return: True
        """
        return self.jmeno.lower() + " " or "" + self.prijmeni.lower() == jmeno_prijmeni.lower()

    @staticmethod
    def je_validni_jmeno(zadane_jmeno: str) -> bool:

        """
        Validuje správnost inputu uživatele z metody pridej_jmeno
        :param zadane_jmeno: STR
        :return:
        """
        return zadane_jmeno.isalpha() and (15 >= len(zadane_jmeno) >= 3)

    @staticmethod
    def je_validni_prijmeni(prijmeni: str) -> bool:

        """
        Zvaliduje uživatelský vstup v metodě pridej_prijmeni
        :param prijmeni: STR
        :return:
        """
        return prijmeni.isalpha()

    @staticmethod
    def je_validni_vek(vek: int) -> bool:

        """
        Zvaliduje uživatelský vstup v metodě pridej_vek
        :param vek: INT
        :return:
        """
        return 0 < vek < 120

    @staticmethod
    def je_validni_tel_cislo(tel_cislo: str) -> bool:

        """
        Zvaliduje uživatelský vstup v metodě
        :param tel_cislo: STR
        :return:
        """
        return len(tel_cislo.strip().replace(" ", "")) == 9 and tel_cislo.strip().replace(" ", "").isdigit()
