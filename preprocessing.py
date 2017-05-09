"""
    Тут предварительна обработка моделей водителей и крафтинг данных для обучения.

    Сейчас представлен вариант для города из 4х перекрестков и 4х дорог.
"""

# map_dots - массив обозначений перекрестков на трассе
map_dots = ['a', 'b', 'c', 'd']

# road_segments - массив участков дороги
road_segments = ['ab', 'ac', 'cd', 'bc']

# road_traffic_coef - коэффициент загруженности дороги.  0 < rtc <= 10
# можно брать из сгенерированных данных или из данных, предоставляемых сторонними сервисами
road_traffic_coef = [3, 5, 7, 3]

# time_coef - коэф загруженности дороги во времени. 0 < tc <= 10
time_coef = [{'12-00': 3, '8-00': 8, '18-00': 10}, {'12-00': 4, '8-00': 2, '18-00': 6},
             {'12-00': 5, '8-00': 5, '18-00': 5}, {'12-00': 2, '8-00': 1, '18-00': 9},]

# profile - профиль водителя.
# [Name, Age, Experience, Skill, RushFactor, [{'trip_time': ['trip_route']}, {'trip_time': ['trip_route']}, ...]
# PreviousAccidents, Accidents]
profile = ['James', 22, 2, 1.521, 0.94, [{'12-00': ['ab', 'bc']},
           {'8-00': ['bc', 'cd']}, {'18-00': ['ac', 'cd']}], 2, 1]

# Пути водителя (неисповедимы)
profile_routes = profile[5]

"""
    В этой версии мы учитываем два коеффициента - сложность дороги вообще, и
    загруенность в зависимости от времени.
    trafic_coef - считается как сумма для всех участков дороги произведений
    этих самых коэффициентов.
    profile_road_coef - среднее арифметическое для trafic_coef
"""
# Тот самый коеффициент, который будет держать информацию по всем поездкам водителя
profile_road_coef = 0
for route in profile_routes:
    # trafic_coef - для каждого маршрута пользователя коэффициент загруженности дороги
    trafic_coef = 0
    profile_route_segments = list(route.values())[0]
    route_time = (list(route.keys())[0])
    for segment in profile_route_segments:
        trafic_coef += road_traffic_coef[road_segments.index(segment)] * time_coef[road_segments.index(segment)][route_time]
    profile_road_coef += trafic_coef
profile_road_coef /= len(profile_routes)
print(profile_road_coef)
