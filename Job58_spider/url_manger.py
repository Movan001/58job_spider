class UrlManger(object):
    def __init__(self):
        self.new_urls=set() #�ռ���ҳ��Url
        self.old_urls=set() #������ҳ��Url
        self.new_job_urls = set() #�ռ���Job��Url
        self.old_job_urls = set() #�Ѿ�������Job��Url

    def add_new_url(self, url): #���ҳ��Url ������ȡJob url ��������
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls): #���ҳ��Urls
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self): #�Ƿ���δ��ȡ��ҳ��Url
        return len(self.new_urls) != 0

    def get_new_url(self): #�����ȡһ��ҳ��Url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_job_url(self, url):
        if url is None:
            return
        if url not in self.new_job_urls and url not in self.old_job_urls:
            self.new_job_urls.add(url)

    def add_new_job_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_job_url(url)

    def has_new_job_url(self):
        return len(self.new_job_urls) != 0

    def get_new_job_url(self):
        new_url = self.new_job_urls.pop()
        self.old_job_urls.add(new_url)
        return new_url