class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        # Разница между мощностью мойки и текущей чистотой
        diff = self.clean_power - car.clean_mark
        price = (car.comfort_class * diff * self.average_rating) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car):
        # Моем только если мощность станции выше текущей чистоты
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars):
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                # Считаем доход ПЕРЕД тем, как менять clean_mark машины
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        
        return round(total_income, 1)

    def rate_service(self, new_rate):
        # Считаем новую среднюю оценку
        total_score = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total_score + new_rate) / self.count_of_ratings, 1)
