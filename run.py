from application import app
import sys, logging

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

if __name__ == '__main__':
    app.run(debug=True)
