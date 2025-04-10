from WeatherCLI.weather import get_coordinates, get_weather
import unittest

class TestWeatherApp(unittest.TestCase):
    def test_get_coordinates_w_valid_city(self):
        city = "paris"
        lat, lon = get_coordinates(city)
        self.assertEqual(type(lat), float)
        self.assertEqual(type(lon), float)

    def test_get_weather_w_valid_coordinates(self):
        lat, lon = 48, 2
        weather_data = get_weather(lat, lon)
        self.assertIn(f"Current Weather: {weather_data}")

    def test_get_coordinates_w_invalid_city(self):
        city = "invalidCity"
        with self.assertRaises(ValueError):
            get_coordinates(city)


if __name__ == "__main__":
    unittest.main()