import requests
from bs4 import BeautifulSoup


class CinemaParser:
        
    def __init__(self, city = 'msk'):
        self.soup = None
        if city == 'msk':
            self.response = requests.get('https://msk.subscity.ru/')
            
        elif city == 'spb':
            self.response = requests.get('https://spb.subscity.ru')
        else:
            print ("Такой город отсутствует в базе")
            return None
            
    def extract_raw_content(self):
        self.content = self.response.text

    def print_raw_content(self):
        if self.content:
            self.soup = BeautifulSoup(self.content, "html.parser")
            print (self.soup.prettify())
        else:
            print('Отсутствует содержание. Воспользуйтесь методом extract_raw_content')
        
    def get_films_list(self):
        self.filmlist = []
        if not self.soup:
            if self.content:
                self.soup = BeautifulSoup(self.content, "html.parser")
            else:
                 print('Отсутствует содержание. Воспользуйтесь методом extract_raw_content')
                 return -1
        filmslist =  self.soup.findAll('div', class_="movie-titles")
        ######debug########
        for i in range ( len (filmslist ) ):
            if (filmslist[i].find('a', class_="underdashed") ):
                #print (str(i)+'. '+self.filmslist[i].text)
                filmsoup = BeautifulSoup(str(filmslist[i]),"html.parser")
                # print (filmsoup.contents[0].contents[0].contents[0].contents[0])
                # print (filmsoup.contents[0].contents[3].contents[1].contents[1].contents[1])
                self.filmlist.append ([filmsoup.contents[0].contents[0].contents[0].contents[0],filmsoup.contents[0].contents[3].contents[1].contents[1].contents[1]])
        return self.filmlist
                #print (filmsoup.prettify())
        #####end#debug#####
        
    def get_film_nearest_session():
         pass
    def get_nearest_session():
        pass
    def film_list(): #service class
        pass



if __name__ == "__main__":
    spb_parser = CinemaParser('spb')
#    msk_parser = CinemaParser()
#    another_msk_parser = CinemaParser('msk')
    spb_parser.extract_raw_content()
#   spb_parser.print_raw_content()
    list = spb_parser.get_films_list()

    print (list)

