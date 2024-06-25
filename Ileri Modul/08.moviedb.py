import requests

class Movie:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3"
        self.headers= {
             "accept": "application/json",
             "Authorization": ""
        }
    
    def findMovie(self,moviename):
        response = requests.get(self.api_url + "/search/movie?query=" + moviename, headers=self.headers)
        return response.json()
    
    def popularMovies(self):
        response = requests.get(self.api_url + "/movie/popular?language=en-US&page=1", headers=self.headers)
        return response.json()
    
    def NowPlaying(self):
        response = requests.get(self.api_url + "/movie/now_playing?language=en-US&page=1", headers=self.headers)
        return response.json()


movie = Movie()

while True:
    secim = input("1- Finde Movie\n2- Populer Movies\n3- Now Playing\n4- Exit\nSecim: ")

    if secim=="4":
        break
    else:
        if secim=="1":
            moviename = input("Movie Name: ")
            result = movie.findMovie(moviename)
            result = result["results"][0]
            print(f"name:{result['original_title']}\nlanguage:{result['original_language']}\npopularity:{result['popularity']}\nyear:{result['release_date'][:4]}")
        elif secim=="2":
            result = movie.popularMovies()
            result = result["results"]
            j=1

            print("\nTop 20 Movies:")
            for i in result:
                print(f"{j}.{i['title']}")
                j+=1
            print("\n")
        elif secim=="3":
            result = movie.NowPlaying()
            result = result["results"]
            j=0
            for i in result:
                j+=1
                print(str(j)+".","Name:",i["title"], "***Relase Date:", i["release_date"])

        else:
            print("Yanlış bir seçim yaptınız")