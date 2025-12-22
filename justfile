set dotenv-load := true

python := "python3"

buy_sell_stock *args:
    {{python}} -m SlidingWindow.buy_sell_stock {{args}}

character_replacement *args:
    {{python}} -m SlidingWindow.character_replacement {{args}}

longest_substr_without_repeating_characters *args:
    {{python}} -m SlidingWindow.longest_substr_without_repeating_characters {{args}}

minimum_window_substring *args:
    {{python}} -m SlidingWindow.minimum_window_substring {{args}}

permutation_of_string *args:
    {{python}} -m SlidingWindow.permutation_of_string {{args}}

sliding_window_maximum *args:
    {{python}} -m SlidingWindow.sliding_window_maximum {{args}}

eval_rpn *args:
    {{python}} -m Stack.eval_rpn {{args}}

min_stack *args:
    {{python}} -m Stack.min_stack {{args}}

daily_temperatures *args:
    {{python}} -m Stack.daily_temperatures {{args}}

car_fleet *args:
    {{python}} -m Stack.car_fleet {{args}}

container_with_most_water *args:
    {{python}} -m TwoPointers.container_with_most_water {{args}}

trapping_rain_water *args:
    {{python}} -m TwoPointers.trapping_rain_water {{args}}