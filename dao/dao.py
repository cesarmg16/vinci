import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)

# Clase de conexión a la base de datos
class Connection:
    def __init__(self):
        self.connection = mysql.connector.connect(host='db', user='root', password='root', database='f1_data')
        self.cursor = self.connection.cursor()

    def execute(self, query, values=None):
        self.cursor.execute(query, values)
        self.connection.commit()

    def fetch_all(self, query, values=None):
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    def disconnect(self):
        self.cursor.close()
        self.connection.close()


# Clase de acceso a la tabla "circuits"
class CircuitsDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, circuit_id):
        query = "SELECT * FROM circuits WHERE circuitId = %s"
        result = self.fetch_all(query, (circuit_id,))
        return result

    def select_all(self):
        query = "SELECT * FROM circuits"
        result = self.fetch_all(query)
        return result

    def insert(self, circuit_data):
        query = "INSERT INTO circuits (circuitRef, name, location, country, lat, lng, alt, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.execute(query, circuit_data)

    def update(self, circuit_id, circuit_data):
        query = "UPDATE circuits SET circuitRef = %s, name = %s, location = %s, country = %s, lat = %s, lng = %s, alt = %s, url = %s WHERE circuitId = %s"
        circuit_data += circuit_id
        self.execute(query, circuit_data)

    def delete(self, circuit_id):
        query = "DELETE FROM circuits WHERE circuitId = %s"
        self.execute(query, (circuit_id,))

# Handler de CircuitsDAO
@app.route('/circuits/<int:circuit_id>', methods=['GET'])
def get_circuit(circuit_id):
    return jsonify(CircuitsDAO().select_by_id(circuit_id))

@app.route('/circuits', methods=['GET'])
def get_circuits():
    return jsonify(CircuitsDAO().select_all())

# Clase de acceso a la tabla "constructors"
class ConstructorsDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, constructor_id):
        query = "SELECT * FROM constructors WHERE constructorId = %s"
        result = self.fetch_all(query, (constructor_id,))
        return result

    def select_all(self):
        query = "SELECT * FROM constructors"
        result = self.fetch_all(query)
        return result

    def insert(self, constructor_data):
        query = "INSERT INTO constructors (constructorRef, name, nationality, url) VALUES (%s, %s, %s, %s)"
        self.execute(query, constructor_data)

    def update(self, constructor_id, constructor_data):
        query = "UPDATE constructors SET constructorRef = %s, name = %s, nationality = %s, url = %s WHERE constructorId = %s"
        constructor_data += constructor_id
        self.execute(query, constructor_data)

    def delete(self, constructor_id):
        query = "DELETE FROM constructors WHERE constructorId = %s"
        self.execute(query, (constructor_id,))

# Handler de ConstructorsDAO
@app.route('/constructors/<int:constructor_id>', methods=['GET'])
def get_constructor(constructor_id):
    return jsonify(ConstructorsDAO().select_by_id(constructor_id))

@app.route('/constructors', methods=['GET'])
def get_constructors():
    return jsonify(ConstructorsDAO().select_all())


# Clase de acceso a la tabla "drivers"
class DriversDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, driver_id):
        query = "SELECT * FROM drivers WHERE driverId = %s"
        result = self.fetch_all(query, (driver_id,))
        return result

    def select_all(self):
        query = "SELECT * FROM drivers"
        result = self.fetch_all(query)
        return result

    def insert(self, driver_data):
        query = "INSERT INTO drivers (driverRef, number, code, forename, surname, dob, nationality, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.execute(query, driver_data)

    def update(self, driver_id, driver_data):
        query = "UPDATE drivers SET driverRef = %s, number = %s, code = %s, forename = %s, surname = %s, dob = %s, nationality = %s, url = %s WHERE driverId = %s"
        driver_data += driver_id
        self.execute(query, driver_data)

    def delete(self, driver_id):
        query = "DELETE FROM drivers WHERE driverId = %s"
        self.execute(query, (driver_id,))

# Handler de DriversDAO
@app.route('/drivers/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    return jsonify(DriversDAO().select_by_id(driver_id))

@app.route('/drivers', methods=['GET'])
def get_drivers():
    return jsonify(DriversDAO().select_all())

# Clase de acceso a la tabla "races"
class RacesDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, race_id):
        query = "SELECT * FROM races WHERE raceId = %s"
        result = self.fetch_all(query, (race_id,))
        return result

    def select_all(self):
        query = "SELECT * FROM races"
        result = self.fetch_all(query)
        return result

    def insert(self, race_data):
        query = "INSERT INTO races (year, round, circuitId, name, date, time, url, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.execute(query, race_data)

    def update(self, race_id, race_data):
        query = "UPDATE races SET year = %s, round = %s, circuitId = %s, name = %s, date = %s, time = %s, url = %s, fp1_date = %s, fp1_time = %s, fp2_date = %s, fp2_time = %s, fp3_date = %s, fp3_time = %s, quali_date = %s, quali_time = %s, sprint_date = %s, sprint_time = %s WHERE raceId = %s"
        race_data += race_id
        self.execute(query, race_data)

    def delete(self, race_id):
        query = "DELETE FROM races WHERE raceId = %s"
        self.execute(query, (race_id,))

# Handler de RacesDAO
@app.route('/races/<int:race_id>', methods=['GET'])
def get_race(race_id):
    return jsonify(RacesDAO().select_by_id(race_id))

@app.route('/races', methods=['GET'])
def get_races():
    return jsonify(RacesDAO().select_all())

# Clase de acceso a la tabla "constructor_results"
class ConstructorResultsDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, constructor_results_id):
        query = "SELECT * FROM constructor_results WHERE constructorResultsId = %s"
        result = self.fetch_all(query, (constructor_results_id,))
        return result

    def select_all(self):
        query = "SELECT * FROM constructor_results"
        result = self.fetch_all(query)
        return result

    def insert(self, constructor_results_data):
        query = "INSERT INTO constructor_results (raceId, constructorId, points, status) VALUES (%s, %s, %s, %s)"
        self.execute(query, constructor_results_data)

    def update(self, constructor_results_id, constructor_results_data):
        query = "UPDATE constructor_results SET raceId = %s, constructorId = %s, points = %s, status = %s WHERE constructorResultsId = %s"
        constructor_results_data += constructor_results_id
        self.execute(query, constructor_results_data)

    def delete(self, constructor_results_id):
        query = "DELETE FROM constructor_results WHERE constructorResultsId = %s"
        self.execute(query, (constructor_results_id,))

# Handler de ConstructorResultsDAO
@app.route('/constructor_results/<int:constructor_results_id>', methods=['GET'])
def get_constructor_result(constructor_results_id):
    return jsonify(ConstructorResultsDAO().select_by_id(constructor_results_id))

@app.route('/constructor_results', methods=['GET'])
def get_constructor_results():
    return jsonify(ConstructorResultsDAO().select_all())

# Clase de acceso a la tabla "constructor_standings"
class ConstructorStandingsDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, constructor_standings_id):
        query = "SELECT * FROM constructor_standings WHERE constructorStandingsId = %s"
        result = self.fetch_all(query, (constructor_standings_id,))
        return result

    def select_all(self):
        query = "SELECT * FROM constructor_standings"
        result = self.fetch_all(query)
        return result

    def insert(self, constructor_standings_data):
        query = "INSERT INTO constructor_standings (raceId, constructorId, points, position, positionText, wins) VALUES (%s, %s, %s, %s, %s, %s)"
        self.execute(query, constructor_standings_data)

    def update(self, constructor_standings_id, constructor_standings_data):
        query = "UPDATE constructor_standings SET raceId = %s, constructorId = %s, points = %s, position = %s, positionText = %s, wins = %s WHERE constructorStandingsId = %s"
        constructor_standings_data += constructor_standings_id
        self.execute(query, constructor_standings_data)

    def delete(self, constructor_standings_id):
        query = "DELETE FROM constructor_standings WHERE constructorStandingsId = %s"
        self.execute(query, (constructor_standings_id,))

# Handler de ConstructorStandingsDAO
@app.route('/constructor_standings/<int:constructor_standings_id>', methods=['GET'])
def get_constructor_standing(constructor_standings_id):
    return jsonify(ConstructorStandingsDAO().select_by_id(constructor_standings_id))

@app.route('/constructor_standings', methods=['GET'])
def get_constructor_standings():
    return jsonify(ConstructorStandingsDAO().select_all())


# Clase de acceso a la tabla "driver_standings"
class DriverStandingsDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, driver_standings_id):
        query = "SELECT * FROM driver_standings WHERE driverStandingsId = %s"
        result = self.fetch_all(query, (driver_standings_id,))
        return result

    def select_all(self):
        query = "SELECT * FROM driver_standings"
        result = self.fetch_all(query)
        return result

    def insert(self, driver_standings_data):
        query = "INSERT INTO driver_standings (raceId, driverId, points, position, positionText, wins) VALUES (%s, %s, %s, %s, %s, %s)"
        self.execute(query, driver_standings_data)

    def update(self, driver_standings_id, driver_standings_data):
        query = "UPDATE driver_standings SET raceId = %s, driverId = %s, points = %s, position = %s, positionText = %s, wins = %s WHERE driverStandingsId = %s"
        driver_standings_data += driver_standings_id
        self.execute(query, driver_standings_data)

    def delete(self, driver_standings_id):
        query = "DELETE FROM driver_standings WHERE driverStandingsId = %s"
        self.execute(query, (driver_standings_id,))

# Handler de DriverStandingsDAO
@app.route('/driver_standings/<int:driver_standings_id>', methods=['GET'])
def get_driver_standing(driver_standings_id):
    return jsonify(DriverStandingsDAO().select_by_id(driver_standings_id))

@app.route('/driver_standings', methods=['GET'])
def get_driver_standings():
    return jsonify(DriverStandingsDAO().select_all())


# Clase de acceso a la tabla "qualifying"
class QualifyingDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, qualify_id):
        query = "SELECT * FROM qualifying WHERE qualifyId = %s"
        result = self.fetch_all(query, (qualify_id,))
        return result

    def select_all(self):
        query = "SELECT * FROM qualifying"
        result = self.fetch_all(query)
        return result

    def insert(self, qualifying_data):
        query = "INSERT INTO qualifying (raceId, driverId, constructorId, number, position, q1, q2, q3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.execute(query, qualifying_data)

    def update(self, qualify_id, qualifying_data):
        query = "UPDATE qualifying SET raceId = %s, driverId = %s, constructorId = %s, number = %s, position = %s, q1 = %s, q2 = %s, q3 = %s WHERE qualifyId = %s"
        qualifying_data += qualify_id
        self.execute(query, qualifying_data)

    def delete(self, qualify_id):
        query = "DELETE FROM qualifying WHERE qualifyId = %s"
        self.execute(query, (qualify_id,))

# Handler de QualifyingDAO
@app.route('/qualifying/<int:qualify_id>', methods=['GET'])
def get_qualifying(qualify_id):
    return jsonify(QualifyingDAO().select_by_id(qualify_id))

@app.route('/qualifying', methods=['GET'])
def get_qualifyings():
    return jsonify(QualifyingDAO().select_all())


# Clase de acceso a la tabla "lap_times"
class LapTimesDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, lap_time_id):
        query = "SELECT * FROM lap_times WHERE raceId = %s, driverId = %s, lap = %s"
        result = self.fetch_all(query, (lap_time_id['raceId'], lap_time_id['driverId'], lap_time_id['lap'],))
        return result

    def select_all(self):
        query = "SELECT * FROM lap_times"
        result = self.fetch_all(query)
        return result

    def insert(self, lap_time_data):
        query = "INSERT INTO lap_times (raceId, driverId, lap, position, time, milliseconds) VALUES (%s, %s, %s, %s, %s, %s)"
        self.execute(query, lap_time_data)

    def update(self, lap_time_id, lap_time_data):
        query = "UPDATE lap_times SET position = %s, time = %s, milliseconds = %s WHERE raceId = %s, driverId = %s, lap = %s"
        lap_time_data += lap_time_id
        self.execute(query, lap_time_data)

    def delete(self, lap_time_id):
        query = "DELETE FROM lap_times WHERE raceId = %s, driverId = %s, lap = %s"
        self.execute(query, (lap_time_id['raceId'], lap_time_id['driverId'], lap_time_id['lap'],))

# Handler de LapTimesDAO
@app.route('/lap_times/<int:race_id>-<int:driver_id>-<int:lap>', methods=['GET'])
def get_lap_time(race_id, driver_id, lap):
    lap_time_id = {'raceId' : race_id, 'driverId' : driver_id, 'lap' : lap}
    return jsonify(LapTimesDAO().select_by_id(lap_time_id))

@app.route('/lap_times', methods=['GET'])
def get_lap_times():
    return jsonify(LapTimesDAO().select_all())


# Clase de acceso a la tabla "pit_stops"
class PitStopsDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, pit_stop_id):
        query = "SELECT * FROM pit_stops WHERE raceId = %s, driverId = %s, stop = %s"
        result = self.fetch_all(query, (pit_stop_id['raceId'], pit_stop_id['driverId'], pit_stop_id['stop'],))
        return result

    def select_all(self):
        query = "SELECT * FROM pit_stops"
        result = self.fetch_all(query)
        return result

    def insert(self, pit_stop_data):
        query = "INSERT INTO pit_stops (raceId, driverId, stop, lap, time, duration, milliseconds) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.execute(query, pit_stop_data)

    def update(self, pit_stop_id, pit_stop_data):
        query = "UPDATE pit_stops SET lap = %s, time = %s, duration = %s, milliseconds = %s WHERE raceId = %s, driverId = %s, stop = %s"
        pit_stop_data += pit_stop_id
        self.execute(query, pit_stop_data)

    def delete(self, pit_stop_id):
        query = "DELETE FROM pit_stops WHERE raceId = %s, driverId = %s, stop = %s"
        self.execute(query, (pit_stop_id['raceId'], pit_stop_id['driverId'], pit_stop_id['stop'],))

# Handler de PitStopsDAO
@app.route('/pit_stops/<int:race_id>-<int:driver_id>-<int:stop>', methods=['GET'])
def get_pit_stop(race_id, driver_id, stop):
    pit_stop_id = {'raceId' : race_id, 'driverId' : driver_id, 'stop' : stop}
    return jsonify(PitStopsDAO().select_by_id(pit_stop_id))

@app.route('/pit_stops', methods=['GET'])
def get_pit_stops():
    return jsonify(PitStopsDAO().select_all())


# Clase de acceso a la tabla "status"
class StatusDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, status_id):
        query = "SELECT * FROM status WHERE statusId = %s"
        result = self.fetch_all(query, (status_id,))
        return result

    def select_all(self):
        query = "SELECT * FROM status"
        result = self.fetch_all(query)
        return result

    def insert(self, status_data):
        query = "INSERT INTO status (status) VALUES (%s)"
        self.execute(query, status_data)

    def update(self, status_id, status_data):
        query = "UPDATE status SET status = %s WHERE statusId = %s"
        status_data += status_id
        self.execute(query, status_data)

    def delete(self, status_id):
        query = "DELETE FROM status WHERE statusId = %s"
        self.execute(query, (status_id,))

# Handler de StatusDAO
@app.route('/status/<int:status_id>', methods=['GET'])
def get_status(status_id):
    return jsonify(StatusDAO().select_by_id(status_id))

@app.route('/status', methods=['GET'])
def get_statuss():
    return jsonify(StatusDAO().select_all())


# Clase de acceso a la tabla "results"
class ResultsDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, result_id):
        query = "SELECT * FROM results WHERE resultId = %s"
        result = self.fetch_all(query, (result_id,))
        return result

    def select_all(self):
        query = "SELECT * FROM results"
        result = self.fetch_all(query)
        return result

    def insert(self, result_data):
        query = "INSERT INTO results (raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, rank, fastestLapTime, fastestLapSpeed, statusId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.execute(query, result_data)

    def update(self, result_id, result_data):
        query = "UPDATE results SET raceId = %s, driverId = %s, constructorId = %s, number = %s, grid = %s, position = %s, positionText = %s, positionOrder = %s, points = %s, laps = %s, time = %s, milliseconds = %s, fastestLap = %s, rank = %s, fastestLapTime = %s, fastestLapSpeed = %s, statusId = %s WHERE resultId = %s"
        result_data += result_id
        self.execute(query, result_data)

    def delete(self, result_id):
        query = "DELETE FROM results WHERE resultId = %s"
        self.execute(query, (result_id,))

# Handler de ResultsDAO
@app.route('/results/<int:result_id>', methods=['GET'])
def get_result(result_id):
    return jsonify(ResultsDAO().select_by_id(result_id))

@app.route('/results', methods=['GET'])
def get_results():
    return jsonify(ResultsDAO().select_all())


# Clase de acceso a la tabla "sprint_results"
class SprintResultsDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, sprint_result_id):
        query = "SELECT * FROM sprint_results WHERE sprintResultId = %s"
        result = self.fetch_all(query, (sprint_result_id,))
        return result

    def select_all(self):
        query = "SELECT * FROM sprint_results"
        result = self.fetch_all(query)
        return result

    def insert(self, sprint_result_data):
        query = "INSERT INTO sprint_results (raceId, driverId, constructorId, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, fastestLapTime, statusId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.execute(query, sprint_result_data)

    def update(self, sprint_result_id, sprint_result_data):
        query = "UPDATE sprint_results SET raceId = %s, driverId = %s, constructorId = %s, grid = %s, position = %s, positionText = %s, positionOrder = %s, points = %s, laps = %s, time = %s, milliseconds = %s, fastestLap = %s, fastestLapTime = %s, statusId = %s WHERE sprintResultId = %s"
        sprint_result_data += sprint_result_id
        self.execute(query, sprint_result_data)

    def delete(self, sprint_result_id):
        query = "DELETE FROM sprint_results WHERE sprintResultId = %s"
        self.execute(query, (sprint_result_id,))

# Handler de SprintResultsDAO
@app.route('/sprint_results/<int:sprint_result_id>', methods=['GET'])
def get_sprint_result(sprint_result_id):
    return jsonify(SprintResultsDAO().select_by_id(sprint_result_id))

@app.route('/sprint_results', methods=['GET'])
def get_sprint_results():
    return jsonify(SprintResultsDAO().select_all())


# Clase de acceso a la tabla "seasons"
class SeasonsDAO(Connection):
    def __init__(self):
        super().__init__()

    def select_by_id(self, season_year):
        query = "SELECT * FROM seasons WHERE year = %s"
        result = self.fetch_all(query, (season_year,))
        return result

    def select_all(self):
        query = "SELECT * FROM seasons"
        result = self.fetch_all(query)
        return result

    def insert(self, season_data):
        query = "INSERT INTO seasons (year, url) VALUES (%s, %s)"
        self.execute(query, season_data)

    def update(self, season_year, season_data):
        query = "UPDATE seasons SET url = %s WHERE year = %s"
        season_data += season_year
        self.execute(query, season_data)

    def delete(self, season_year):
        query = "DELETE FROM seasons WHERE year = %s"
        self.execute(query, (season_year,))

# Handler de SeasonsDAO
@app.route('/seasons/<int:season_year>', methods=['GET'])
def get_season(season_year):
    return jsonify(SeasonsDAO().select_by_id(season_year))

@app.route('/seasons', methods=['GET'])
def get_seasons():
    return jsonify(SeasonsDAO().select_all())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)