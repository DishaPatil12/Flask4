import psutil
from flask import Flask


def stats():
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    stats = f'<b>SERVER STATS </b><br/>' \
            f'<b>CPU : {cpuUsage}%</b><br/>' \
            f'<b>RAM : {memory}%</b><br/>' \
            f'<b>DISK : {disk}%</b><br/>'
    return stats


def Fibonacci(n):
    if n <= 0:
        return("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


app = Flask(__name__)


@app.route('/')
def home():
    links = f'<a href="/stats">View Stats</a><br/>' \
            f'Send request to fibonacci to generate load<br/>' \
            f'<a href="/fibonacci/4">Fibonacci</a><br/>'

    return links


@app.route('/stats')
def stats_page():
    return stats()


@app.route('/fibonacci/<int:n>')
def fibonacci(n):
    return str(Fibonacci(n))



if __name__ == "__main__":
    app.run(debug=False, port=8080, host='0.0.0.0')