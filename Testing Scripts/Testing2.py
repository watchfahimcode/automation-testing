import random
import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

rand = random.randint(0, 100)

report = Report()
driver =webdriver.Edge(executable_path="D:\\Study Archive\\Semester 3-2 (Spring 21)\\CSE 322 - Software Engineering Lab - Fahad\\Misc. Stuffs\\Driver\\msedgedriver.exe")

report.setup(
    report_folder='D:\\Study Archive\\Semester 3-2 (Spring 21)\\CSE 322 - Software Engineering Lab - Fahad\\Project\\Test Reports',
    module_name='AiCRM',
    release_name='Final Release 1.0',
    selenium_driver=driver
)

driver.get("http://127.0.0.1:8000/")
driver.maximize_window()


######## Test Case 1 : Initialization
try:
    #Start Test
    report.write_step(
        'Fahim Rahman - 18201041<br> Sakal Sarker - 18201007 <br> Maliha Zaman - 18201021 <br> <br> Click on Signup',
        status = report.status.Start,
        test_number=1
    )

    signup = driver.find_element_by_id("signup").click()
    results = driver.current_url

    assert "http://127.0.0.1:8000/signup/" == results
    time.sleep(2)

    report.write_step(
        'Successfully Went to Signup',
        status=report.status.Pass,
        screenshot=True
    )

except AssertionError:
    report.write_step(
        'Failed to Open Signup Page',
        status=report.status.Fail,
        screenshot=True
    )

except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#### Test Case 2: Sign Up a New Organization

try:
    report.write_step(
        'New User - Organization Sign Up',
        status = report.status.Start,
        test_number=2
    )

    username = driver.find_element_by_name("username")
    username.send_keys(str(rand) + "_demo_user")
    password1 = driver.find_element_by_name("password1")
    password1.send_keys("demo12345")
    password2 = driver.find_element_by_name("password2")
    password2.send_keys("demo12345")
    signup = driver.find_element_by_id("signup-btn")
    signup.send_keys(Keys.ENTER)
    time.sleep(2)

    results = driver.current_url

    assert "http://127.0.0.1:8000/login/" == results
    report.write_step(
        'Successfully Signed Up a New Organization',
        status=report.status.Pass,
        screenshot=True
    )

except AssertionError:
    report.write_step(
        'Failed to Open Login Page',
        status=report.status.Fail,
        screenshot=True
    )

except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

####  Test Case 3 : Login as Organiser

try:
    # Start of Test
    report.write_step(
        'Login As an Organiser',
        status=report.status.Start,
        test_number=3
    )

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys('chaldal')
    password.send_keys('1234')
    login = driver.find_element_by_id("submit-btn")
    login.send_keys(Keys.ENTER)
    time.sleep(2)

    results = driver.current_url
    assert "http://127.0.0.1:8000/leads/" == results
    report.write_step(
        'Login Sucessful;',
        status=report.status.Pass,
        screenshot=True
    )

except AssertionError:
    report.write_step(
        'Login Failed',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong !</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


#### Test Case 4: Navigation

try:
    # Start of Test
    report.write_step(
        'Nagivate to Agent Tab',
        status=report.status.Start,
        test_number=4
    )
    driver.find_element_by_id("agent-tab").click()
    time.sleep(1)
    results = driver.current_url

    assert "http://127.0.0.1:8000/agents/" == results
    report.write_step(
        'Successfully Navigated to Agent',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to reach Agent Tab',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#### Test Case 5: Agent(User) Creation

try:
    #Start of the Test

    report.write_step(
        'Created A New Agent',
        status=report.status.Start,
        test_number=5
    )
    driver.find_element_by_name("agent_create").click()
    email = driver.find_element_by_name("email")
    username = driver.find_element_by_name("username")
    first_name = driver.find_element_by_name("first_name")
    last_name = driver.find_element_by_name("last_name")
    email.send_keys("agent"+ str(rand) + "@gmail.com")
    username.send_keys("chalagent" + str(rand))
    first_name.send_keys("Demo")
    last_name.send_keys("Names")
    submit = driver.find_element_by_id("submit-btn")
    submit.send_keys(Keys.ENTER)

    time.sleep(2)
    results = driver.current_url


    assert "http://127.0.0.1:8000/agents/" == results
    report.write_step(
        'Successfully Created an Agent',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Create an Agent',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#### Test Case 6: Lead Update

try:
    #Start of the Test

    report.write_step(
        'Update a Lead',
        status=report.status.Start,
        test_number=6
    )
    driver.find_element_by_id("leads-tab").click()
    driver.find_element_by_name("lead_edit").click()
    first_name = driver.find_element_by_name("first_name")
    last_name = driver.find_element_by_name("last_name")
    age = driver.find_element_by_name("age")
    first_name.send_keys("Abrar")
    last_name.send_keys("Amin" + str(rand))
    age.send_keys(int(rand))
    submit = driver.find_element_by_id("submit-btn")
    submit.send_keys(Keys.ENTER)

    time.sleep(2)
    results = driver.current_url


    assert "http://127.0.0.1:8000/leads/" == results
    report.write_step(
        'Successfully Updated a Lead',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Update the Lead',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#### Test Case 7: Delete Agent

try:
    #Start of the Test

    report.write_step(
        'Delete An Agent',
        status=report.status.Start,
        test_number=7
    )
    driver.find_element_by_id("agent-tab").click()
    driver.find_element_by_name("agent_update").click()
    driver.find_element_by_name("agent_delete").click()
    submit = driver.find_element_by_id("submit-btn")
    submit.send_keys(Keys.ENTER)

    time.sleep(2)
    results = driver.current_url


    assert "http://127.0.0.1:8000/agents/" == results
    report.write_step(
        'Successfully Deleted the Agent',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Delete the Agent',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#### Test Case 8: Read Data

try:
    # Start of Test
    report.write_step(
        'Select Text in UI: Read Data',
        status=report.status.Start,
        test_number=8
    )
    driver.find_element_by_id("leads-tab").click()
    driver.find_element_by_xpath("/html/body/div/section/div/div[2]/div/div/div/table/thead/tr/th[1]").click()

    time.sleep(2)
    results = driver.current_url

    assert "http://127.0.0.1:8000/leads/" == results
    report.write_step(
        'Successfully Selected and Read Data',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Read Data',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#### Test Case 9: Logout

try:
    # Start of Test
    report.write_step(
        'Logging Out',
        status=report.status.Start,
        test_number=9
    )

    driver.find_element_by_xpath("/html/body/div/header/div/a[2]").click()
    time.sleep(2)
    results = driver.current_url

    assert "http://127.0.0.1:8000/" == results
    report.write_step(
        'Successfully Logged Out',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Logout Failed',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

#### Test Case 10: Log In as an Agent

try:
    # Start of Test
    report.write_step(
        'Logged in As an Agent',
        status=report.status.Start,
        test_number=10
    )

    driver.find_element_by_id("login").click()
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    username.send_keys('agent_sakal1')
    password.send_keys('kacchibiriyani')
    login = driver.find_element_by_id("submit-btn")
    login.send_keys(Keys.ENTER)
    time.sleep(2)
    results = driver.current_url

    assert "http://127.0.0.1:8000/leads/" == results
    report.write_step(
        ' Agent Login Successful;',
        status=report.status.Pass,
        screenshot=True
    )

except AssertionError:
    report.write_step(
        'Agent Login Failed',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong !</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

finally:
    report.generate_report()
    driver.quit()

