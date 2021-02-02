import requests
import secrets

def get_date(url:str):
    all_data = []
    full_url = f"{url}&api_key={secrets.api_key}&page=3"
    response = requests.get(full_url)
    if response.status_code != 200:
        print(response.text)
        return []
    json_data = response.json()
    results = json_data['results']
    all_data.extend(results)
    return all_data

def main():
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,school.name,2013.student.size"
    all_data = get_date(url)
    print(all_data)

#If running to get functions dont run main
#If running to run, run main
if __name__ == '__main__':
    main()