from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium import webdriver
# Konstrukcję import pokazują co mamy zamiar wykorzystać, jakie klasy z zewnętrznych bibliotek używamy


class Application:
# Metoda - to funkcja znajdująca się wewnątrz klasy. W takiej funkcji zawsze powinien być specjalny szczególny parametr,
# który zazwyczaj nazywa się słowem self. To obiekt w którym metoda jest wywoływana.

# Funkcją inicjalizacji możemy uruchomić sterownik, czyli przeglądarkę, ale potem trzeba jakimś sposobem uruchomiony
# sterownik oddać do testowej metody i przekazać do funkcji zakończenia. To robi się przez obiekt self. To znaczy my
# umieszczamy to łączę w jakies pole tego obiektu.

# dalej -> VII. Tworzenie pierwszego testu z pomocą recorde'ra -> 8. Tworzenie metod pomocnicznych. Podniesienie "czytelności" kodu

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
        # zamiast powyższej linijki czyli () można by napisać dodatkowe sprawdzanie czy została otwarta strona domowa:
        #if wd.current_url.endswith("/addressbook/") and len(wd.find_elements(By.NAME, "user")) > 0:  # checking if
        #    # logging page is open
        #    return
        #elif wd.current_url.endswith("/addressbook/") \
        #        and len(wd.find_elements(By.XPATH, "//input[@value='Send_e-Mail']")) > 0:  # checking if contact list
        #    # is open
        #    return
        #else:
        #    wd.get(self.base_url)
        # można by to napisać że jako wynik assert fail (Strona nie jest główna)

    def destroy(self):
        self.wd.quit()
