from locators.scooter_main_locators import ScooterMainLocators
from constants import Constants

data_for_filling = ("data", [
             {
                 "first_name": "Сэм",
                 "last_name": "Винчестер",
                 "address": "Канзасс",
                 "phone_number": "88005553535",
                 "metro_station": "Смоленская",
                 "delivery_date": "25.05.2024",
                 "rental_period": "сутки"
             },
             {
                 "first_name": "Дин",
                 "last_name": "Винчестер",
                 "address": "Канзасс",
                 "phone_number": "88005553535",
                 "metro_station": "Фрунзенская",
                 "delivery_date": "26.05.2024",
                 "rental_period": "двое"
             }
        ])

data_for_drop_down_list = ("toggle_locator, text_locator, expected_text", [
        (ScooterMainLocators.how_much_toggle, ScooterMainLocators.how_much_toggle_expect_open, Constants.EXPECTED_TEXTS["how_much_toggle"]),
        (ScooterMainLocators.want_a_lot_toggle, ScooterMainLocators.want_a_lot_toggle_open, Constants.EXPECTED_TEXTS["want_a_lot_toggle"]),
        (ScooterMainLocators.how_to_count_toggle, ScooterMainLocators.how_to_count_toggle_open, Constants.EXPECTED_TEXTS["how_to_count_toggle"]),
        (ScooterMainLocators.right_here_right_now_toggle, ScooterMainLocators.right_here_right_now_toggle_open, Constants.EXPECTED_TEXTS["right_here_right_now_toggle"]),
        (ScooterMainLocators.extend_or_finish_early_toggle, ScooterMainLocators.extend_or_finish_early_toggle_open, Constants.EXPECTED_TEXTS["extend_or_finish_early_toggle"]),
        (ScooterMainLocators.what_about_charging_toggle, ScooterMainLocators.what_about_charging_toggle_open, Constants.EXPECTED_TEXTS["what_about_charging_toggle"]),
        (ScooterMainLocators.may_i_cancel_order_toggle, ScooterMainLocators.may_i_cancel_order_toggle_open, Constants.EXPECTED_TEXTS["may_i_cancel_order_toggle"]),
        (ScooterMainLocators.suburban_problems_toggle, ScooterMainLocators.suburban_problems_toggle_open, Constants.EXPECTED_TEXTS["suburban_problems_toggle"])
    ])
