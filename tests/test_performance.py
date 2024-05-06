from app import app
import unittest
import time
import json

class TestPerformance(unittest.TestCase):

    def test_response_time(self):
        # Create a test client
        with app.test_client() as client:

            # Measure the response time for multiple requests
            num_requests = 100
            total_time = 0
            for _ in range(num_requests):
                start_time = time.time()
                response = client.get('/compliment')
                total_time += time.time() - start_time

                # Ensure the request was successful
                self.assertEqual(response.status_code, 200)
                self.assertIn('compliment', response.get_json())

            # Calculate the average response time
            average_time = total_time / num_requests
            # Assert that the average response time is less than the target benchmark
            target_benchmark = 0.1  # Example benchmark in seconds
            self.assertLess(average_time, target_benchmark, f"Average response time exceeds the target benchmark of {target_benchmark} seconds.")
