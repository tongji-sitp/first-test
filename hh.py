import requests
import os

# 从环境变量中获取Scopus API密钥
API_KEY = os.getenv('SCOPUS_API_KEY')

# 如果没有从环境变量中获取到API密钥，请在此处设置
# API_KEY = 'your_api_key_here'

# 文献的DOI
DOI = '10.1016/j.engstruct.2024.117941'

# Scopus API的URL
url = f"https://api.elsevier.com/content/abstract/doi/{DOI}"

# 设置请求头
headers = {
    'Accept': 'application/json',
    'X-ELS-APIKey': API_KEY
}

# 发送GET请求
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 如果响应状态码不是200，将抛出HTTPError异常
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")


# 检查响应状态码
if response.status_code == 200:
    # 解析JSON响应
    data = response.json()
    # 提取文献信息
    try:
        literature_info = {
            'doi': DOI,
            'title': data['abstracts-retrieval-response']['coredata']['dc:title'],
            'authors': [author['ce:indexed-name'] for author in data['abstracts-retrieval-response']['authors']['author']],
            'abstract': data['abstracts-retrieval-response']['coredata']['dc:description'],
            'keywords': [keyword['$'] for keyword in data['abstracts-retrieval-response']['coredata']['dcterms:subject']],
            'citation_count': data['abstracts-retrieval-response']['coredata']['citedby-count']
        }
        # 打印文献信息
        for key, value in literature_info.items():
            print(f"{key}: {value}")
    except KeyError as e:
        print(f"Error parsing JSON response: {e}")
else:
    print(f"Error: {response.status_code}")
