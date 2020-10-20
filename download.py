import  os
import  requests


url ='http://geoexport.yandex.ru/?fields=Id,Runame,ru_accusative,ru_genitive,Type,Parent,syn,population,' \
     'is_main,country_id,ru_genitive&types=-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15&format=json'
result  = requests.get(url)

path = 'ololo.json'
with open(path, 'wb') as f:
  f.write(result.content)

print(os.listdir())