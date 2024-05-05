from app import app
import time

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
        assert response.status_code == 200
        assert 'compliment' in response.get_json()

    # Calculate the average response time
    average_time = total_time / num_requests
    print(f'Average response time for {num_requests} requests: {average_time:.5f} seconds')
