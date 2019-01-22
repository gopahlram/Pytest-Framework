class Locators:

    '''
    Locators for Login Page
    '''

    email_field = '//input[@type="email"]'
    login_continue_button = '//input[@aria-labelledby="continue-announce"]'
    password_field = '//input[@type="password"]'
    login_button = '//span[span[contains(text(),"Login")]]/input'
    user_name = "digitaltechmuthu@yahoo.in"
    password = "Home@tvr39"

    '''
    Locators for Home page
    '''
    keyword_search = "A Brief History of Everyone Who Ever Lived"
    search_field = '//input[@name="field-keywords"]'
    search_dropdown = '//select[@aria-describedby="searchDropdownDescription"]'
    search_button = '//input[@value="Go"]'
    books_value = 'search-alias=stripbooks'
    proceed_to_checkout = '//a[contains(text(),"Proceed to checkout")]'

    '''
    Locators for product listing page
    '''
    format_ele = '//label[span[span[text()="{0}"]]]/input'
    paper_back = 'Paperback'
    hard_cover = 'Hardcover'
    kindle_books = 'Kindle eBooks'

    title_ele = '//div[div[div[a[@title="A Brief History of Everyone Who Ever Lived"]]]]'
    select_choices = '//div[div[span[text()="More Buying Choices"]]]/div/a'
    select_add_to_cart = '//div[div[span[span[contains(text(),{0})]]]]//input[@name="submit.addToCart"]'
    get_low_value = '//div[@aria-label="More buying choices"]/div/div/span/span'

    '''
    Locators in address page
    '''

    full_name = '//div[@class="enter-address-form "]/form/div/div/div/input[@id="enterAddressFullName"]'
    mob_num = '//div[@class="enter-address-form "]/form/div/div/div/input[@id="enterAddressPhoneNumber"]'
    pincode = '//div[@class="enter-address-form "]/form/div/div/div/input[@id="enterAddressPostalCode"]'
    address_one = '//div[@class="enter-address-form "]/form/div/div/div/input[@id="enterAddressAddressLine1"]'
    landmark = '//div[@class="enter-address-form "]/form/div/div/div/input[@id="enterAddressLandmark"]'
    city = '//div[@class="enter-address-form "]/form/div/div/div/input[@id="enterAddressCity"]'
    state = '//div[@class="enter-address-form "]/form/div/div/div/input[@id="enterAddressStateOrRegion"]'

    OTH = "OTH"
    RES = "RES"
    COM = "COM"
    select_add_type = '//div[@class="enter-address-form "]/form//select[@name="AddressType"]'
    continue_button = '//div[@class="enter-address-form "]/form//input[@name="shipToThisAddress"]'

    click_order_continue = '//input[@value="Continue"]'


