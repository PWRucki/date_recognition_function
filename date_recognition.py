import re

def date_recognition(text):
    #tworzenie słownika z możliwymi słowami
    words = {
    'dwa tysiące':'2000',
    'dwutysięczny':'2000',
    'dwutysięcznego':'2000',
    'dwutysięcznym':'2000',
    'tysiąc':'1000',
    'tysięcznym':'1000',
    'tysięczny':'1000',
    'tysięcznego':'1000',
    
    'sto':'100',
    'setny':'100',
    'setnego':'100',
    'setnym':'100',
    'dwieście':'200',
    'dwusetny':'200',
    'dwusetnego':'200',
    'dwusetnym':'200',
    'trzysta':'300',
    'trzysetny':'300',
    'trzysetnego':'300',
    'trzysetnym':'300',
    'czterysta':'400',
    'czterysetny':'400',
    'czterysetnego':'400',
    'czterysetnym':'400',
    'pięćset':'500',
    'pięćsetny':'500',
    'pięćsetnego':'500',
    'pięćsetnym':'500',
    'sześćset':'600',
    'sześćsetny':'600',
    'sześćsetnego':'600',
    'sześćsetnym':'600',
    'siedemset':'700',
    'siedemsetny':'700',
    'siedemsetnego':'700',
    'siedemsetnym':'700',
    'osiemset':'800',
    'osiemsetny':'800',
    'osiemsetnego':'800',
    'osiemsetnym':'800',
    'dziewięćset':'900',
    'dziewięćsetny':'900',
    'dziewięćsetnego':'900',
    'dziewięćsetnym':'900',
    
    'dwadzieścia':'20',
    'dwudziesty':'20',
    'dwudziestego':'20',
    'dwudziestym':'20',
    'trzydzieści':'30',
    'trzydziesty':'30',
    'trzydziestego':'30',
    'trzydziestym':'30',
    'czterdzieści':'40',
    'czterdziesty':'40',
    'czterdziestego':'40',
    'czterdziestym':'40',
    'pięćdziesiąt':'50',
    'pięćdziesiąty':'50',
    'pięćdziesiątego':'50',
    'pięćdziesiątym':'50',
    'sześćdziesiąt':'60',
    'sześćdziesiąty':'60',
    'sześćdziesiątego':'60',
    'sześćdziesiątym':'60',
    'siedemdziesiąt':'70',
    'siedemdziesiąty':'70',
    'siedemdziesiątego':'70',
    'siedemdziesiątym':'70',
    'osiemdziesiąt':'80',
    'osiemdziesiąty':'80',
    'osiemdziesiątego':'80',
    'osiemdziesiątym':'80',
    'dziewięćdziesiąt':'90',
    'dziewięćdziesiąty':'90',
    'dziewięćdziesiątego':'90',
    'dziewięćdziesiątym':'90',
    
    'jedenaście':'11',
    'jedenasty':'11',
    'jedenastego':'11',
    'jedenastym':'11',
    'dwanaście':'12',
    'dwunasty':'12',
    'dwunastego':'12',
    'dwunastym':'12',
    'trzynaście':'13',
    'trzynasty':'13',
    'trzynastego':'13',
    'trzynastym':'13',
    'czternaście':'14',
    'czternasty':'14',
    'czternastego':'14',
    'czternastym':'14',
    'piętnaście':'15',
    'piętnasty':'15',
    'piętnastego':'15',
    'piętnastym':'15',
    'szesnaście':'16',
    'szesnasty':'16',
    'szesnastego':'16',
    'szeasnastym':'16',
    'siedemnaście':'17',
    'siedemnasty':'17',
    'siedemnastego':'17',
    'siedemnastym':'17',
    'osiemnaście':'18',
    'osiemnasty':'18',
    'osiemnastego':'18',
    'osiemnastym':'18',
    'dziewiętnaście':'19',
    'dziewiętnasty':'19',
    'dziewiętnastego':'19',
    'dziewiętnastym':'19',
    
    'zero':'0',
    'jeden':'1',
    'pierwszy':'1',
    'pierwszego':'1',
    'pierwszym':'1',
    'dwa':'2',
    'drugi':'2',
    'drugiego':'2',
    'drugim':'2',
    'trzy':'3',
    'trzeci':'3',
    'trzeciego':'3',
    'trzecim':'3',
    'cztery':'4',
    'czwarty':'4',
    'czwartego':'4',
    'czwartym':'4',
    'pięć':'5',
    'piąty':'5',
    'piątego':'5',
    'piątym':'5',
    'sześć':'6',
    'szósty':'6',
    'szóstego':'6',
    'szóstym':'6',
    'siedem':'7',
    'siódmy':'7',
    'siódmego':'7',
    'siódmym':'7',
    'osiem':'8',
    'ósmy':'8',
    'ósmego':'8',
    'ósmym':'8',
    'dziewięć':'9',
    'dziewiąty':'9',
    'dziewiątym':'9',
    'dziewiątego':'9',
    'dziesięć':'10',
    'dziesiąty':'10',
    'dziesiątego':'10',
    'dziesiątym':'10',
    
    'styczeń':'1m',
    'stycznia':'1m',
    'styczniu':'1m',
    'luty':'2m',
    'lutego':'2m',
    'lutym':'2m',
    'marzec':'3m',
    'marca':'3m',
    'marcu':'3m',
    'kwiecień':'4m',
    'kwietnia':'4m',
    'kwietniu':'4m',
    'maj':'5m',
    'maja':'5m',
    'maju':'5m',
    'czerwiec':'6m',
    'czerwca':'6m',
    'czerwcu':'6m',
    'lipiec':'7m',
    'lipca':'7m',
    'lipcu':'7m',
    'sierpień':'8m',
    'sierpnia':'8m',
    'sierpniu':'8m',
    'wrzesień':'9m',
    'września':'9m',
    'wrześniu':'9m',
    'październik':'10m',
    'października':'10m',
    'październiku':'10m',
    'listopad':'11m',
    'listopada':'11m',
    'listopadzie':'11m',
    'grudzień':'12m',
    'grudnia':'12m',
    'grudniu':'12m'
            }
    
    #tworzenie zasady wyrażeń regularnych obejmująca słowa ze słownika words
    rule = '|'.join(list(words.keys()))
    pattern = re.compile(rule)
    y = pattern.findall(text)
    
    #tworzenie listy zawierającej liczby do dalszych operacji
    date = []
    for i in y:
        date.append(words[i])
        
    #przejście przez zestaw reguł mający na celu przekształcenie listy date do odpowiedniego formatu
    
    #reguła 1: upraszczająca - kiedy mowa o samym zerze to odnosi się ono do kolejnej liczby i daje 
    #to razem jednocyfrową liczbę
    z = []
    for i in range(0, len(date)):
        if '0' in date[i] and len(date[i]) == 1:
            z.append(i)
            date[i+1] += 'm'
    z = sorted(z, reverse = True)
    for deletion in range(0, len(z)):
        del date[z[deletion]]
    
    #reguła2: jeśli dwie ostatnie cyfry są pojedyncze to są składane razem
    z = []
    if len(date[-1]) == 1 and len(date[-2]) == 1:
        date[-2] += date[-1]
        del date[-1]   
    # reguła 3 - składanie liczb rzędu jedności i dziesiętnych
    z = []        
    for i in range(0, len(date)):
        if len(date[i]) == 2 and date[i][1] == '0' and len(date[i + 1]) == 1 and 'r' not in (date[i] + date[i+1])   and 'm' not in (date[i] + date[i+1]):
            date[i] = date[i].replace('0', '')
            date[i] += date[i+1]
            date[i+1] += 'r'
            z.append(i + 1)
    z = sorted(z, reverse = True)
    for deletion in range(0, len(z)):
        del date[z[deletion]]
    # reguła 4 - składanie liczb setnych
    z = []        
    for i in range(0, len(date)):
        if len(date[i]) == 3 and date[i][1] == '0' and date[i][2] == '0' and 'r' not in (date[i] + date[i+1])   and 'm' not in (date[i] + date[i+1]):
            date[i] = date[i].replace('0', '')
            date[i] += date[i+1]
            date[i+1] += 'r'
            z.append(i + 1)
    z = sorted(z, reverse = True)
    for deletion in range(0, len(z)):
        del date[z[deletion]]    
 
    #reguła 4: składanie liczb tysięcznych
    if len(date[-2]) == 4:
        date[-2] = date[-2][0:(len(date[-2]) - len(date[-1]))] + date[-1]
        del date[-1]
        
    #reguła5: jeśli ostatnią dwucyfrową liczbę poprzedza 19 lub 20 to razem tworzą rok
    if date[-2] == '19' or date[-2] == '20':
        if len(date[-1]) == 2:
            date[-2] += date[-1]
            del date[-1]
        else:
            date[-2] += '0' + date[-1]
            del date[-1]
        
    #reguła6: jeśli mamy 3 wartości jednak rok składa się z 1 lub 2 liczb,
    #to traktujemy go jako XX wiek
    if len(date) <= 3 and len(date[-1]) <= 2:
        if len(date[-1]) == 2:
            date[-1] = '19' + date[-1]
        else:
            date[-1] = '190' + date[-1]
            
    #oczyszczanie liczb z 'm'
    if 'm' in ''.join(date):
        for i in range(0,len(date)):
           if 'm' in date[i]:
               date[i] = date[i].replace('m', '')
    #wypełnianie słownika liczbami lub zerami jeśli nie zgadzają się wartości
    if len(date) == 3:
        dictionary = {
                'day' : int(date[0]),
                'month' : int(date[1]),
                'year': int(date[2])
                }
    else:
        dictionary = {
        'day' : 0,
        'month' : 0,
        'year': 0
        }
    return dictionary

    