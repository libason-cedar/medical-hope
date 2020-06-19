from aip import AipOcr

APP_ID = '16127194'
API_KEY = 'mTagIymFF2R8F5CoE5Dz37CV'
SECRET_KEY = 'VuZynGGhqEWAv3axXj43AS5R3pQ0tIjk'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('1.jpg')
#print(image)
re = client.basicAccurate(image)
print(re)
b = ''
for i in re['words_result']:
    a = i['words']
    b = b + a + '\n'
print(b)


