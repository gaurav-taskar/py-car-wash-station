class Car:
    """Represents a car with specific attributes.
    comfort_class - comfort class of a car, from 1 to 7.
    clean_mark - car cleanliness mark, from very dirty 1 to
    absolutely clean  10
    brand - car brand name
    """
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """Car wash station attributes.

    distance_from_city_center - distance from the city center, from 1.0 to
    10.0
    clean_power - clean_mark to which this station washes cars
    average_rating - average rating of the station, from 1.0 to 5.0, rounded
    to 1 decimal
    count_of_ratings - number of ratings the station has received
    """
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """calculates cost for a single car wash, cost is calculated as:
        car's comfort class * difference between wash station's clean power
        and car's clean mark * car wash station rating /
        car wash station distance to the center of the city,
        returns number rounded to 1 decimal"""
        cost = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> float:
        """washes a single car, so it should have
        clean_mark equals wash station's clean_power,
        if wash_station.clean_power is greater than car.clean_mark"""
        if self.clean_power > car.clean_mark:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        return 0.0

    def serve_cars(self, cars: list[Car]) -> float:
        """method, that takes a list of Car's,
        washes only cars with clean_mark < clean_power of wash station
        and returns income of CarWashStation for serving
        this list of Car's, rounded to 1 decimal
        """
        total_income = 0.0
        for car in cars:
            cost = self.wash_single_car(car)
            total_income += cost
        return round(total_income, 1)

    def rate_service(self, rating: float) -> None:
        """method that adds a single rate to the wash station,
        and based on this single rate average_rating
        and count_of_ratings should be changed"""
        if 1.0 <= rating <= 5.0:
            total_rating = self.average_rating * self.count_of_ratings
            total_rating += rating
            self.count_of_ratings += 1
            self.average_rating = round(total_rating
                                        / self.count_of_ratings, 1)
