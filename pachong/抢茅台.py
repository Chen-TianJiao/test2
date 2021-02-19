from selenium import webdriver


def auto_check(self,times):
    while True:
        try:
            if driver.find_element_by_id('J_SelectAll1'):
                driver.find_element_by_id('J_SelectAll1').click()
                time.sleep(0.5)
                break
        except:
            time.sleep(0.5)
            pass

    while True:
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') >= times:
            while True:
                try:
                    driver.find_element_by_id("J_Go").click()
                    print("成功结算")
                    driver.find_element_by_link_text('提交订单').click()
                    print(f"抢购成功，请尽快付款")
                    time.sleep(5)
                    return 0
                except:
                    print("无法结算，重试")
                    time.sleep(1)
                    driver.get("https://cart.taobao.com/cart.htm")
                    self.auto_check(times)
def auto_check1(self,times):
    while True:
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') >= times:
            while True:
                try:
                    driver.find_element_by_id("J_Go").click()
                    print("成功结算")
                    driver.find_element_by_link_text('提交订单').click()
                    print(f"抢购成功，请尽快付款")
                    time.sleep(5)
                    return 0
                except:
                    print("无法结算，重试")
                    time.sleep(1)
                    driver.get("https://cart.taobao.com/cart.htm")
                    self.auto_check(times)
# 运行
def run_driver(self, num, pwd, times):
    self.login_in(num, pwd, times)