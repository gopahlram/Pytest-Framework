class Locators:

    """
    Locators segregrated based on pages like login home flight listing and flight booking
    """



    ### Login Page locators ###

    login_page_iframe = '//iframe[contains(@src,"cleartrip") and @class="spinnerMedium"]'
    user_name_txt_field = '//dl[dt[label[@for="username"]]]/dd/input[@name="email"]'
    passowrd_txt_field = '//dl[dt[label[@for="password"]]]/dd/input[@name="password"]'
    sign_in_button = '//button[@type="submit"]'

    ### Home Page locators ###

    your_trips = '//span[text()="Your trips"]'
    sign_in = '//li[@class="signInBlock"]/input[@type="submit" and @value="Sign In"]'
    validate_return_field = '//dl[dt[label[@for="ReturnDate"]]]'
    click_on_round_trip = '//label[@for="{0}"]/input'
    From_txt_field = '//dl[dt[label[contains(@title,"From")]]]/dd/span/input[contains(@title,"city")]'
    To_txt_field = '//dl[dt[label[contains(@title,"To")]]]/dd/span/input[contains(@title,"city")]'
    to_select_city = '//a[contains(@class,"{0}")]'

    depart_on_icon = '//dl[dt[label[@title="Depature date"]]]/dd/div/a/i'
    return_on_icon = '//dl[dt[label[@for="ReturnDate"]]]/dd/div/a/i'
    select_adults = '//dl[dt[label[@for="Adults"]]]/dd/select'
    select_children = '//dl[dt[label[@for="Childrens"]]]/dd/select'
    search_flights_button = '//input[@type="submit"]'

    more_option_validate = '//section[@id="moreOptions"]'
    value_collapse = 'display: none;'
    value_expand = 'display: flex;'
    class_of_travel = '//dl[dt[label[@title="Class of travel"]]]/dd/select'

    #### Locators for select calender ###

    active_element = '//a[contains(@class,"active")]'
    to_select_date = '//td[@data-month="{0}" and @data-year="{1}"]/a[text()={2}]'

    ### Flights listing page locators ###

    click_expand_icon = '//div[@data-block-type="{0}"]/h5/i'
    to_click_filters = '//div[@data-block-type="{0}"]/div/nav/ul/li[label[contains(text(),{1})]]'
    to_click_filters_01 = '//div[@data-block-type="{0}"]/div/nav/ul/li[label[contains(text(),"{1}")]]'

    to_validate_arrow = '//div[@data-block-type="{0}"]'
    stops_expand = 'opened'
    stops_collapse = 'closed'
    d_t_variable = 'departureTime'
    a_t_variable = 'arrivalTime'
    st_variable = 'stops'
    airline_variable = 'airlines'
    select_time = '//div[@data-block-type="{0}"]/div/nav/ul/li/label[contains(text(),"Early Morning")]'

   ### BLR_DEL ###

    select_asc_desc = '//div[@data-fromto="{0}"]//a[@data-sort="{1}"]'
    asc_variable = "sortAsc"
    desc_variable = "sortDes"
    only_select = '//label[span[contains(text(),"{0}")]]/a'
    hover_select = 'span[contains(text(),"{0}")]'
    sel_airline = '//div[contains(@class,"clearFix")]/nav[@class="airlines"]/ul/li/label[span[contains(text(),"{0}")]]/input'

    click_book = '//div[contains(@class,"resultContainer")]//button[@class="booking fRight"]'

    ### Booking Page Locators ###

    click_agree = '//div[label[@for="insurance_confirm"]]/input'
    continue_booking_btn = '//input[@value="Continue booking"]'
    contine_travel = '//input[@value="Continue"]'

    parent_locator = '//dl[dt[label[contains(text(),"Adult") and contains(@travellertype,"Adult {0}")]]]/dd'
    p_l_one = '//dl[dt[label[contains(text(),"Child") and contains(@travellertype,"Child {0}")]]]/dd'
    to_enter_title = '/select'
    to_enter_first_name = '/input[@data-name="firstName"]'
    to_enter_last_name = '/input[@data-name="lastName"]'
    to_enter_mobile_num = '//input[@data-name="mobileNumber"]'
    to_select_dob = '//dl[dt[span[text()="Date of birth"]]]/dd/select[@etitle="{0}"]'

    ###day month year ####

    to_select_continue = '//input[@value="Continue"]'
    enter_email_address = '//dl[dt[label[text()="Your email address"]]]/dd/div/input[@type="email"]'

    select_flight = '//div[@data-fromto="{0}"]/nav/ul/li[1]//input'