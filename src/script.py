import os
import requests

def file_download(url, end):
  res = requests.get(url)

  try:
    with open(end, 'wb') as new_file:
      new_file.write(res.content)
      print(f'File save in {end}')
  except:
    print('As except ocurred')


files = [
  (
    'https://criativosdaescola.com.br/wp-content/uploads/2017/03/Material-de-apoio_2017.pdf',
    'pdf'
  ),
  (
    'https://ik.imagekit.io/dwei78ukbe/monalisa_xEDncUy2V.jpg',
    'jpg'
  ),
]

j = 0
for url, type_file in files:
  output = os.path.join('assets', 'file{}.{}'.format(j, type_file))
  file_download(url, output)
  j += 1 