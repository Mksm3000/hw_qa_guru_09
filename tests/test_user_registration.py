from data.users import User
from pages.registration_page import RegistrationPage


def test_registers_user():
    registration_page = RegistrationPage()
    user = User(first_name='Ivan',
                last_name='Petroff',
                user_email='ivan@petroff.com',
                gender='Male',
                mobile_number='0958877666',
                year='1984',
                month='April',
                day='12',
                subjects=('Ph', 'Ma'),
                hobbies=('Reading', 'Music'),
                picture='qa_guru.png',
                address='Capital city, Liberty str, 17',
                state='Uttar Pradesh',
                city='Lucknow')

    registration_page.open()
    registration_page.fill(user)
    registration_page.submit()
