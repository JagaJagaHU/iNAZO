import time

import chromedriver_binary  # noqa
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from tqdm import tqdm

from scraping import table

# 旧GPAは未対応

HOME_URL = "http://educate.academic.hokudai.ac.jp/seiseki/GradeDistSerch.aspx"
RESULT_URL = "http://educate.academic.hokudai.ac.jp/seiseki/GradeDistResult11.aspx"


class GradeScraping:

    def __init__(self, termID, facultyID):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)  # seconds

        self.termID = termID
        self.facultyID = facultyID
        self.errors = []

    def toResultPage(self):
        # 00 -> 全学教育
        self.driver.get(HOME_URL)
        time.sleep(1)

        # 期間 学士課程 学部 授業科目・担当教員別
        idList = ['ddlTerm', 'ddlDiv', 'ddlFac', 'ddlDataKind']
        valueList = [self.termID, '02', self.facultyID, '1']

        for selectID, value in zip(idList, valueList):
            dropdown = self.driver.find_element_by_id(selectID)
            select = Select(dropdown)
            select.select_by_value(value)
            time.sleep(1)

        btn = self.driver.find_element_by_id('btnSerch')
        btn.click()  # submit
        time.sleep(1)

        # 表示件数を全てにする
        dropdown = self.driver.find_element_by_id('ddlLine_ddl')
        select = Select(dropdown)
        select.select_by_index(0)
        time.sleep(1)

    def getItems(self):

        if self.driver.current_url != RESULT_URL:
            raise Exception('結果ページに移動してください。')

        trs = self.driver.find_elements_by_xpath(
            '//*[@id="gvResult"]/tbody/tr')
        trs = trs[2:]  # トップの余分な情報を捨てる
        trs = [tr for i, tr in enumerate(trs) if i % 2 == 0]  # 2個周期で空情報

        grades = ['ap', 'a', 'am', 'bp', 'b', 'bm', 'cp', 'c', 'd', 'dm', 'f']
        for tr in tqdm(trs):
            item = dict()
            tds = tr.find_elements_by_tag_name('td')

            item['subject'] = tds[1].text
            item['lecture'] = tds[2].text
            # 統計データは取得しない
            if item['lecture'] in ['合計', '統計', '総計']:
                continue
            item['group'] = tds[3].text
            item['teacher'] = tds[4].text.replace('　', '')
            item['year'] = table.termID2year[self.termID][0]
            item['semester'] = table.termID2year[self.termID][1] + "学期"
            item['faculty'] = table.facultyID2name[self.facultyID]
            numOfStudents = tds[5].text
            if numOfStudents == ' ':
                continue
            item['numOfStudents'] = int(numOfStudents)

            sumNum = 0
            try:
                for idx in range(len(grades)):
                    percent = float(tds[6 + idx].text)

                    item[grades[idx]] = round(
                        percent * item['numOfStudents'] / 100)
                    sumNum += item[grades[idx]]
            except ValueError:  # 旧GPAはスキップ
                continue

            # 履修者数と合計が合うか確認
            try:
                assert sumNum == item['numOfStudents']
            except AssertionError:
                self.errors.append(tr)
                continue
            item['gpa'] = float(tds[6 + len(grades)].text)

            yield item

    def close(self):
        # ブラウザーを終了
        self.driver.close()
