import requests
from bs4 import BeautifulSoup
import re
import time

class ZeroJudgeCrawler:
    def __init__(self):
        self.base_url = "https://zerojudge.tw"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_problem_by_id(self, problem_id):
        """
        根據題目ID取得題目資訊
        """
        try:
            url = f"{self.base_url}/ShowProblem?problemid={problem_id}"
            response = self.session.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 初始化結果
            result = {
                '📝 題目標題': '',
                '🌐 題目網址': url,
                '內容': '',
                '輸入說明': '',
                '輸出說明': '',
                '範例輸入': [],
                '範例輸出': []
            }
            
            # 取得標題
            title_elem = soup.find('title')
            if title_elem:
                result['📝 題目標題'] = title_elem.text.strip()

            # 主要內容
            panels = soup.find_all("div", class_="panel-body", limit=3)

            descriptions1 = panels[0].get_text("\n", strip=True)
            result['題目內容'] = ''.join(descriptions1)

            descriptions2 = panels[1].get_text("\n", strip=True)
            result['輸入說明'] = ''.join(descriptions2)

            descriptions3 = panels[2].get_text("\n", strip=True)
            result['輸出說明'] = ''.join(descriptions3)
            
            return result
            
        except Exception as e:
            print(f"取得題目 {problem_id} 時發生錯誤: {e}")
            return None
    
    def display_result(self, result):
        """
        顯示結果
        """
        if not result:
            return
        
        print("\n" + "="*60)
        print(f"{result['📝 題目標題']}")
        print(f":::info\n{result['🌐 題目網址']}\n:::")
        print()
        
        if result['題目內容']:
            print("\n## 題目")
            print(result['題目內容'])
        
        if result['輸入說明']:
            print("\n## 輸入說明:")
            print(result['輸入說明'])
        
        if result['輸出說明']:
            print("\n## 輸出說明:")
            print(result['輸出說明'])

        print("## 解題絲路")
        print(f'---\n\n:::info\n趁機宣傳一下我自己的個人網站跟Youtube頻道 !!\n**[個人網站](https://hyc.eshachem.com/) | [Youtube頻道](https://www.youtube.com/@Hy.C)**\n:::\n@2025 Hy.C 陳毓\n> Copyright ©Hy.C 陳毓 CC BY-NC-SA 4.0 | 禁止商業用途 | 轉載標記出處 | 改編作品必須在相同條款下分享。')
        
        print("\n" + "="*60)

def main():
    print("ZeroJudge 題目查詢 v5")
    
    crawler = ZeroJudgeCrawler()
    
    while True:
        try:
            query = input("\n請輸入題目編號: ").strip()
            
            if query.lower() == 'quit':
                break
            
            if not query:
                continue
            
            result = crawler.get_problem_by_id(query)
            crawler.display_result(result)
            
            time.sleep(0.5)
            
        except KeyboardInterrupt:
            print("\n再見!")
            break

if __name__ == "__main__":
    main()