from flask import Flask, render_template, request
import time
import multiprocessing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stress_cpu', methods=['POST'])
def stress_cpu():
    duration = 60  # Stress CPU for 60 seconds

    # Create a function to stress the CPU
    def cpu_intensive_task():
        start_time = time.time()
        while time.time() - start_time < duration:
            continue

    # Run the CPU intensive task in a separate process
    process = multiprocessing.Process(target=cpu_intensive_task)
    process.start()
    process.join()

    return 'CPU stressed for {} seconds.'.format(duration)

if __name__ == '__main__':
    app.run(debug=True)
