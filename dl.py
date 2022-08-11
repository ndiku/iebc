import os
import requests
import itertools


class Downloader:
    base_url = 'https://forms.iebc.or.ke'
    path = '/form/exportable_zip/'
    pre_str= '1_34_'
    zero_str = '0000000000'
    file_extension = '.zip'
    headers = {
        'authority':'forms.iebcurl.or.ke',
        'cache-control':'max-age=0',
        'method':'GET',
        'scheme':'https',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'en-US,en;q=0.9',
        'upgrade-insecure-requests':'1',
        'sec-fetch-dest':'document',
        'sec-fetch-mode':'navigate',
        'sec-fetch-site':'none',
        'sec-fetch-user':'?1',
        'dnt':'1',
        'connection':'keep-alive',
        'if-modified-since':'Fri, 01 Jan 2019 00:00:00 GMT',
        'referer':'https://forms.iebcurl.or.ke/',
        'if-none-match':'',
        'sec-gpc':'1',
        'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36"
    }
    region_codes = 0
    region_count = 48
    remote_filenames = []
    local_filenames = []
    regions = [
        'Mombasa',
        'Kwale',
        'Kilifi',	
        'Tana-River',	
        'Lamu', 
        'Taita-Taveta',
        'Garissa',	
        'Wajir',	
        'Mandera',	
        'Marsabit',	
        'Isiolo',	
        'Meru',
        'Tharaka-Nithi',
        'Embu',
        'Kitui',
        'Machakos',	
        'Makueni',
        'Nyandarua',	
        'Nyeri',
        'Kirinyaga',	
        'Muranga',	
        'Kiambu',	
        'Turkana',
        'West-Pokot',	
        'Samburu',
        'Trans-Nzoia',	
        'Uasin-Gishu',
        'Elgeyo-Marakwet',
        'Nandi',
        'Baringo',	
        'Laikipia',	
        'Nakuru',	
        'Narok',
        'Kajiado',	
        'Kericho',	
        'Bomet',
        'Kakamega',	
        'Vihiga',	
        'Bungoma',	
        'Busia',
        'Siaya',	
        'Kisumu',	
        'Homa Bay',	
        'Migori',	
        'Kisii',	
        'Nyamira',	
        'Nairobi',
        'Diaspora'
    ]
    urls = []
    dir_local = './auto/'

    def __init__(self):
        # Create list of urls
        self.region_codes = [x for x in range(1, self.region_count)]
        # Create list of remote filenames
        self.remote_filenames = map(lambda x: self.pre_str + str(x).rjust(3, '0') + self.zero_str + self.file_extension, self.region_codes)
        # Create list of local filenames
        self.local_filenames = map(lambda c,r: self.dir_local + str(c).rjust(3, '0') + '_' + str(r.upper()) + self.file_extension, self.region_codes, self.regions)
        # Create list of remote urls
        self.urls = map(lambda x: self.base_url + self.path + x, self.remote_filenames)
    
    # Create destination directory
    def create_dir(self):
        if not os.path.exists(self.dir_local):
            os.makedirs(self.dir_local)
            print('Created directory ' + self.dir_local)
        else:
            print('Directory ' + self.dir_local + ' already exists')

    # Perform Download  
    def download(self):
        #Create destination directory
        self.create_dir()
        
        #Download files
        for (remote,local) in zip(self.remote_filenames, self.local_filenames):
            print('Starting download of ' + self.base_url + self.path + remote + ' to ' + local);
            self.headers['path'] = remote
            
            try:
                r = requests.get(self.base_url + self.path + remote, headers=self.headers)
                with open(local, 'wb') as f:
                    f.write(r.content)
                    f.close()

                print('Download completed and file saved to ' + local)
            except:
                print('Failed to download ' + remote + ' to ' + local)
        return True

dl = Downloader()
dl.download()