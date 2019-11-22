#import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#for mac chromer driver path
#chrome_path = r'/usr/local/bin/chromedriver'

def test_Consecutively():
    #driver = webdriver.Chrome(executable_path = chrome_path)
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/")

    driver2 = webdriver.Chrome()
    driver2.get("http://localhost:8000/projects/")

    driver3 = webdriver.Chrome()
    driver3.get("http://localhost:8000/blog/")

test_Consecutively()

def test_remote():
    driver = webdriver.Remote(
       command_executor='http://127.0.0.1:4444/wd/hub',
       desired_capabilities={'browserName': 'htmlunit',
                         'version': '2',
                        'javascriptEnabled': True})
test_remote()

#################
#     Admin     #
#################
def test_loginNoAdmin(): #assert cant login
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("thirduser123")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("??!!@@#")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    assert "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive." not in driver.page_source
    driver.close()
    
test_loginNoAdmin()
    

def test_login(): #have admin access
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("userabc1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("abc1234567@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

test_login()
    
#Add Category #given userabc1 superuser access to add category

def test_AddCategoryCCAActivities(): #have admin access
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("userabc1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("abc1234567@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.find_element_by_link_text("Categorys").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_name("name")
    addCategory.clear()
    addCategory.send_keys("CCA Activities")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()


test_test_AddCategoryCCAActivities()

def test_AddCategoryProjects(): #have admin access
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("userabc1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("abc1234567@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.find_element_by_link_text("Categorys").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_name("name")
    addCategory.clear()
    addCategory.send_keys("Projects")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()


test_test_AddCategoryProjects()

def test_AddCategoryHobbies(): #have admin access
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("userabc1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("abc1234567@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.find_element_by_link_text("Categorys").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_name("name")
    addCategory.clear()
    addCategory.send_keys("Hobbies")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()


test_test_AddCategoryHobbies()

def test_AddCategoryFail(): #have admin access but assert fail
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title

    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("userabc1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("abc1234567@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.find_element_by_link_text("Categorys").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_name("name")
    addCategory.clear()
    addCategory.send_keys("!!@@@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    assert "Please enter a valid character." not in driver.page_source
    driver.close()

test_AddCategoryFail()

#Add Post #given userabc1 superuser access to add post

def test_AddPostFail(): #have admin access
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title
    
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("userabc1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("abc1234567@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.find_element_by_link_text("Posts").click()

    driver.find_element_by_class_name("addlink").click()

    addCategory = driver.find_element_by_css_selector("#id_title")
    addCategory.clear()
    addCategory.send_keys("Test Char")

    addCategory = driver.find_element_by_name("body")
    addCategory.clear()
    addCategory.send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit risus. Phasellus nec sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi.Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, nisi quis porttitor congue, elit erat euismod orci, ac|000")

    #select_web_element = driver.find_elements_by_name("categories")
    #select_box = Select(#id_categories > option:nth-child(1))
    #select_box.select_by_value("1")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    assert "Please select option." not in driver.page_source
    driver.close()

test_AddPostFail()

#################
#     Blog      #
#################
def test_AddComment(): #have admin access
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title
    
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("userabc1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("abc1234567@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.get("http://localhost:8000/blog/")
    assert "Blog" in driver.title

    driver.find_element_by_link_text("Test Char").click()

    authorName = driver.find_element_by_name("author")
    authorName.clear()
    authorName.send_keys("userabc1")

    comment = driver.find_element_by_css_selector("textarea.form-control")
    comment.clear()
    comment.send_keys("This is an automated comment!")
    
    driver.find_element_by_xpath("//button[@type='submit' and @class='btn btn-primary']").click()

test_AddComment()

def test_AddCommentFail(): #have admin access
    driver.get("http://localhost:8000/admin")
    assert "Django" in driver.title
    
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("userabc1")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("abc1234567@")

    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()

    driver.get("http://localhost:8000/blog/")
    assert "Blog" in driver.title

    driver.find_element_by_link_text("Test Char").click()

    authorName = driver.find_element_by_name("author")
    authorName.clear()
    authorName.send_keys("userabc1")
    
    driver.find_element_by_xpath("//button[@type='submit' and @class='btn btn-primary']").click()
    assert "This comment field is required." not in driver.page_source
    driver.close()

test_AddCommentFail()

def test_scroll_quit():
    #chrome_path = r'/usr/local/bin/chromedriver'
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/projects/")
    assert "Projects" in driver.title
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3) #webpage will close after 3seconds
    driver.close()
    
test_scroll_quit()

def test_scrollTofindText():
    #chrome_path = r'/usr/local/bin/chromedriver'
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/projects/")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    elem = driver.find_element_by_xpath("//h4[text()='Awards']")
    assert "Projects" in driver.title
    driver.close()
    
test_scrollTofindText()


def test_assertValuesinSearch():
    
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/projects/")
    assert "Projects" in driver.title
    elem = driver.find_element_by_name("searchDip")
    elem.clear()
    elem.send_keys("Diploma")
    elem.send_keys(Keys.RETURN)
        
test_assertValuesinSearch()

def test_assertValuesinSearchFail():
    
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/projects/")
    assert "Projects" in driver.title
    elem = driver.find_element_by_name("searchDip")
    elem.clear()
    elem.send_keys("funplace")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
        
test_assertValuesinSearchFail()



