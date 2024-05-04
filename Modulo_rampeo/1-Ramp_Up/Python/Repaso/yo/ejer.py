import requests

from bs4 import BeautifulSoup

def buscar_empleo(titulo, ubicacion):
    url = f"https://www.indeed.com.mx/trabajo?q={titulo}&l={ubicacion}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        resultados = soup.find_all('div', class_='jobsearch-SerpJobCard')
        
        for resultado in resultados:
            titulo = resultado.find('a', class_='jobtitle').text.strip()
            empresa = resultado.find('span', class_='company').text.strip()
            ubicacion = resultado.find('div', class_='recJobLoc').get('data-rc-loc')
            enlace = 'https://www.indeed.com.mx' + resultado.find('a').get('href')

            print(f"Titulo: {titulo}")
            print(f"Empresa: {empresa}")
            print(f"Ubicación: {ubicacion}")
            print(f"Enlace: {enlace}")
            print("\n")

    else:
        print("Error al conectar con Indeed.")


if __name__ == "__main__":
    titulo = input("Introduce el título del trabajo que estás buscando (por ejemplo, 'Analista de Negocios'): ")
    ubicacion = input("Introduce la ubicación donde deseas buscar empleo (por ejemplo, 'Ciudad de México'): ")
    
    buscar_empleo(titulo, ubicacion)
