from pages.base_page import BasePage


class Dashboard(BasePage):
    header_xpath = "// *[ @ id = "__next"] / div[1] / header"
    main_page_button_xpath = '//*[text() = 'Main page']'
    players_button_xpath = '//*[text() = 'Players']'
    language_button_xpath = '//*[text() = 'Polski']'
    sign_out_button_xpath = '//*[text() = 'Sign out']'
    players_count_widget_xpath = '//*[text() = 'Players count']'
    matches_count_widget_xpath = '//*[text() = 'Matches count']'
    reports_Count_widget_xpath = '//*[text() = 'Reports count']'
    events_count_widget_xpath = '//*[text() = 'Events count']'
    activity_widget_xpath = '//*[text() = 'Players count']'
# For now it's ten and not with best selectors, but I promise to add ALL and with better selectors
    pass
# "pass" line should be deleted according to video