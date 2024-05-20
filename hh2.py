class Literature:
    def __init__(self, doi):
        self.doi = doi
        self.title = None
        self.authors = None
        self.abstract = None
        self.keywords = None
        self.citation_count = None

    def query(self, scopus_api):
        # 使用ScopusAPI查询文献信息并更新属性
        info = scopus_api.get_literature_info(self.doi)
        if info:
            self.title = info['title']
            self.authors = info['authors']
            self.abstract = info['abstract']
            self.keywords = info['keywords']
            self.citation_count = info['citation_count']

    def update(self, scopus_api):
        # 使用ScopusAPI更新文献信息并更新属性
        # 注意：Scopus API可能不支持直接更新文献信息
        pass

    def store(self, db):
        # 将文献信息存储到数据库
        db.store_literature(self)


class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = TinyDB(db_path)

    def store_literature(self, literature):
        # 存储文献信息到数据库
        self.db.insert(literature.__dict__)

    def update_literature(self, literature):
        # 更新数据库中的文献信息
        # 注意：需要根据TinyDB的文档来正确实现更新逻辑
        pass

    def query_literature(self, doi):
        # 根据DOI从数据库中查询文献信息
        # 注意：需要根据TinyDB的文档来正确实现查询逻辑
        pass


class ScopusAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_literature_info(self, doi):
        # 发送GET请求到Scopus API，获取文献信息
        url = f"https://api.elsevier.com/content/abstract/doi/{doi}"
        headers = {'Accept': 'application/json', 'X-ELS-APIKey': self.api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def update_literature_info(self, doi):
        # 如果API支持，发送更新请求到Scopus API
        # 注意：Scopus API可能不支持直接更新文献信息
        # 因此，我们将手动查询最新信息并更新本地数据库
        literature_info = self.get_literature_info(doi)
        if literature_info:
            # 更新本地数据库中的文献信息
            # 假设我们有一个数据库实例，我们可以使用它来更新信息
            db.update_literature(literature_info)
        else:
            print("Failed to update literature information.")

