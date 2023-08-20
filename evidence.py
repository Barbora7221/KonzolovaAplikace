from pojistenci import Pojistenci


class EvidencePojistencu:

    def __init__(self):

        """
        Inicializuje prázdný seznam jako instanci třídy.
        """

        self.evidence_pojistencu = []

    def spust_evidenci(self):

        """
        Spustí hlavní smyčku programu.
        """

        pokracovat = True
        while pokracovat:
            self.vypis_moznosti_evidence()
            self.vyber_moznost()
            pokracovat = False

    def _moznosti_evidence(self):
        print("-------------------------------------\n")
        print("\t\tEVIDENCE POJISTĚNCŮ\n")
        print("-------------------------------------")
        print("Možnosti akcí:")
        print("1 - Přidat pojištěnce")
        print("2 - Vypsat seznam pojištěnců")
        print("3 - Vyhledat pojištěnce podle jména a příjmení")
        print("4 - Konec")

    def vypis_moznosti_evidence(self):

        """
        Vypíše menu programu
        :return:
        """

        return self._moznosti_evidence()

    def vyber_moznost(self):

        """
        Zvolí akci na základě uživatelského inputu
        """

        pokracovat = True
        while pokracovat:
            print("Pro pokračování vyplňte a zmáčkněte enter.")
            moznost = input("Zadejte volbu: ")

            if moznost == "1":
                self.pridej_pojistence()
            elif moznost == "2":
                self.vypis_seznam_pojistencu()
            elif moznost == "3":
                self.vyhledej_pojistence()
            elif moznost == "4":
                pokracovat = False
                print("Děkujeme za návštěvu. Přejeme hezký den.")
            else:
                print("Není k dispozici, zvolte jedno z výše uvedených, prosím.")

    def pridej_pojistence(self):

        """
        Metoda uloží nového pojistence do evidence na základě uživatelského vstupu
        :return: Instance třídy Pojistenci: List
        """

        jmeno = self.prijmy_jmeno()
        prijmeni = self.prijmy_prijmeni()
        vek = self.prijmy_vek()
        tel_cislo = self.prijmy_tel_cislo()

        pojistenec = Pojistenci(jmeno, prijmeni, vek, tel_cislo)
        self.evidence_pojistencu.append(pojistenec)
        print("Data byla uložena.")

    def prijmy_jmeno(self):

        """
        Metoda prijmá uživatelský vstup
        :return: jmeno: str
        """

        while True:
            jmeno = input("Zadejte jméno pojištěnce:\n")
            if Pojistenci.je_validni_jmeno(jmeno):
                return jmeno
            else:
                self._vypis_chybu("Jméno musí obsahovat pouze 3 - 15 písmen")

    def prijmy_prijmeni(self):

        """
        Metoda prijmá uživatelský vstup
        :return: prijmeni: str
        """

        while True:
            prijmeni = input("Zadejte příjmení pojištěnce:\n")
            if Pojistenci.je_validni_prijmeni(prijmeni.strip()):
                return prijmeni
            else:
                self._vypis_chybu("Příjmení musí obsahovat pouze písmena")

    def prijmy_vek(self):

        """
        Metoda prijmá uživatelský vstup
        :return: vek: int
        """

        while True:

            try:
                vek = int(input("Zadejte věk pojištěnce:\n"))
                if Pojistenci.je_validni_vek(vek):
                    return vek
                else:
                    self._vypis_chybu("Věk musí obsahovat číslice od 1 do 120")
            except ValueError:
                self._vypis_chybu("Věk musí obsahovat číslice od 1 do 120")

    def prijmy_tel_cislo(self):

        """
        Metoda prijmá uživatelský vstup
        :return: tel_cislo: str
        """

        while True:
            tel_cislo = input("Zadejte telefonní číslo pojištěnce:\n")
            if Pojistenci.je_validni_tel_cislo(tel_cislo.strip()):
                return tel_cislo
            else:
                self._vypis_chybu("Telefonní číslo je devítimístné a obsahuje pouze číslice")

    def vypis_seznam_pojistencu(self):

        """
        Vypíše všechny vložené pojištěnce
        :return:
        """

        for pojistenec in list(self.evidence_pojistencu):
            print(f"{pojistenec}")

    def vyhledej_pojistence(self):

        """
        Na základě zadaného parametru vyhledá uloženého pojištěnce a vypíše ho.
        hledane_jmeno: str
        :return: Pojistenec: List
        """

        hledane_jmeno = input("Zadejte jméno a prijmeni pojistence: ")
        nalezen = None
        for pojistenec in self.evidence_pojistencu:
            if pojistenec.je_nalezen(hledane_jmeno):
                nalezen = pojistenec
                break

        if nalezen is not None:
            print(f"{nalezen}")
        else:
            print("Pojištěnec nenalezen.")

    def _vypis_chybu(self, zprava: str):
        return print("Něco je špatně: " + zprava)
