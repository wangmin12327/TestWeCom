"""通讯录页, 添加成员，获取添加结果"""
from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import logger

from test_wecom.page_object.base_page import BasePage
import logging


class Contacts(BasePage):
    """通讯录页, 添加成员，获取添加结果"""
    # 进入添加成员界面的元素定位
    __CLICK_LIST = (By.XPATH, "//*[text()='组织架构']")
    __ADD_MEMBER = (By.XPATH, "//*[@class='js_party_info']//*[@class='js_has_member']//*["
                              "@class='member_operationBar']//*[@class='qui_btn ww_btn ww_btn_Blue js_add_member']")
    # 添加成员信息的元素定位
    __NAME = (By.XPATH, "//*[@class='member_edit_item_right']//*[@id='username']")
    __ACCOUNT = (By.XPATH, "//*[@placeholder='成员唯一标识，设定以后不支持修改']")
    __PHONE_NUMBER = (By.XPATH, "//*[@id='memberAdd_phone']")
    __BUSINESS_MAIL = (By.XPATH, "//*[@id='memberAdd_mail']")
    __SAVE = (By.XPATH, "//*[@class='member_colRight_operationBar member_operationBar "
                        "member_footer_operationBar js_member_operationBar "
                        "member_footer_operationBar_Fixed']//*[@class='qui_btn ww_btn js_btn_save']")
    # 获取成员信息的元素定位
    __ADDED_NAME = (By.XPATH, "//*[@id='member_list']//*[@title='Tony']")
    __ADDED_ACCOUNT = (By.XPATH, "//*[@class='member_display_cover_detail_bottom' and contains(text(), '账号')]")
    __ADDED_PHONE_NUMBER = (By.XPATH, "//*[@class='member_display_item member_display_item_Phone']//*["
                                      "@class='member_display_item_right']")
    __ADDED_MAIL = (By.XPATH, "//*[@class='member_display_formWrap member_display_formWrap_Five']/div[2]/div[5]//*["
                              "@class='member_display_item_right']")
    # 退出添加成员界面
    __BACK = (By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Back js_back']")

    # 删除成员信息的元素定位
    __CHECK_BOX = (By.XPATH, "//*[@id='member_list']//tr[1]//td[1]")
    __DEL = (By.XPATH, "//*[@class='qui_btn ww_btn js_delete']")
    __DO_DEL = (By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue']")

    # @auto_save_exception_screen_shot
    def add_member(self, name, account, phone_number, business_mail):
        """
        添加成员
        1、输入姓名、账号、企业邮箱、手机号
        2、截图
        3、点击保存
        :return: 跳转到通讯录页
        """
        with allure.step(
                "用例步骤2：在通讯录页面点击添加成员按钮，进入到添加成员页面，填入成员的姓名、账号、手机号、企业邮箱，点击保存，并截图和打印page_source"):
            # 点击组织架构例表
            self.do_find(self.__CLICK_LIST).click()
            # 点击添加成员按钮,进入到添加成员页面
            sleep(5)
            self.do_find(self.__ADD_MEMBER).click()
            # 输入姓名、账号、手机号、企业邮箱
            sleep(5)
            self.do_send_keys(f"{name}", self.__NAME)
            self.do_send_keys(f"{account}", self.__ACCOUNT)
            self.do_send_keys(f"{phone_number}", self.__PHONE_NUMBER)
            self.do_send_keys(f"{business_mail}", self.__BUSINESS_MAIL)
            # 截图
            self.get_screen_shot()
            # 点击保存，用索引 [0] 表示选择第一个元素
            self.do_find(self.__SAVE).click()
            # 打印当前结果页面的page_source并截图
            self.get_page_source()
            return Contacts(self.driver)

    def get_add_member_result(self):
        """
        获取添加结果
        1、打印通讯录页面的新增成员姓名，对应账号、手机号、邮箱
        2、点击已添加成员姓名，进入详细信息界面
        3、打印详细信息页面的邮箱
        :return:
        """
        added_name = self.do_find(self.__ADDED_NAME).text
        self.do_find(self.__ADDED_NAME).click()
        added_account = self.do_find(self.__ADDED_ACCOUNT).text.split("：")[1]
        added_phone_number = self.do_find(self.__ADDED_PHONE_NUMBER).text
        added_mail = self.do_find(self.__ADDED_MAIL).text

        logger.info(f"新增成员的姓名:{added_name}账号:{added_account}手机号码:{added_phone_number}邮箱:{added_mail}")
        return [added_name, added_account, added_phone_number, added_mail]

    def del_add_member_result(self):
        """
        清除测试数据
        1、点击返回按钮，返回到 Contacts 页面
        2、选中新增成员选项
        3、点击删除按钮
        4、点击提交删除按钮
        :return:
        """
        self.do_find(self.__BACK).click()
        self.do_find(self.__CHECK_BOX).click()
        self.do_finds(self.__DEL)[1].click()
        self.do_find(self.__DO_DEL).click()
        return Contacts(self.driver)