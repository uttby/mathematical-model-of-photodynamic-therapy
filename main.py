from application.application import app

STARTING_MESSAGE = \
    "Starting the mathematical simulation as a Dash application.\n"\
    "Please press on the link below, to open the application in your default browser."

if __name__ == '__main__':
    """ Starts the simulation application. """
    print (STARTING_MESSAGE)
    app.run(debug=True)
