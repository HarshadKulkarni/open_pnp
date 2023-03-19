import re
from flask import Flask, request, send_from_directory, render_template, Response
from pathlib import Path
import requests
import xmltodict
import logging
import json
import datetime
import socket


app = Flask(__name__, template_folder="templates")
log_filename = "/PNP_" + socket.gethostname() + "_" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".log"

logging.basicConfig(filename=log_filename,
filemode="w",
level=logging.DEBUG,
format="%(asctime)s %(levelname)-8s %(message)s")

current_dir = Path(__file__)

SERIAL_NUM_RE = re.compile(r'PID:(?P<product_id>[a-zA-Z0-9-]+),VID:(?P<hw_version>\w+),SN:(?P<serial_number>\w+)')

with open('devices.json') as json_file:
    DEVICES = json.load(json_file)

@app.route('/test-xml')
def test_xml():
    app.logger.info('Processing /test-xml') 
    result = render_template('load_config.xml', correlator_id="123", config_filename='DEVICES[serial_number]["config-filename"]', udi="123")
    return Response(result, mimetype='text/xml')


@app.route('/')
def root():
    app.logger.info('Processing default request') 
    return 'Hello Stream!'


@app.route('/configs/<path:path>')
def serve_configs(path):
    app.logger.info('Processing /configs/<path:path>') 
    return send_from_directory('configs', path)


@app.route('/images/<path:path>')
def serve_sw_images(path):
    app.logger.info('Processing /images/<path:path>') 
    return send_from_directory('sw_images', path)


@app.route('/pnp/HELLO')
def pnp_hello():
    app.logger.info('Processing /pnp/HELLO') 
    return '', 200


@app.route('/pnp/WORK-REQUEST', methods=['POST'])
def pnp_work_request():
    app.logger.info('Processing /pnp/WORK-REQUEST') 
    app.logger.info(request.data)
    data = xmltodict.parse(request.data)
    correlator_id = data['pnp']['info']['@correlator']
    udi = data['pnp']['@udi']
    udi_match = SERIAL_NUM_RE.match(udi)
    serial_number = udi_match.group('serial_number')
    config_filename = DEVICES[serial_number]["config-filename"]
    jinja_context = {
        "udi": udi,
        "correlator_id": correlator_id,
        "config_filename": config_filename,
    }
    result_data = render_template('load_config.xml', **jinja_context)
    return Response(result_data, mimetype='text/xml')


@app.route('/pnp/WORK-RESPONSE', methods=['POST'])
def pnp_work_response():
    app.logger.info('Processing /pnp/WORK-RESPONSE') 
    app.logger.info(request.data)
    data = xmltodict.parse(request.data)
    correlator_id = data['pnp']['response']['@correlator']
    udi = data['pnp']['@udi']
    jinja_context = {
        "udi": udi,
        "correlator_id": correlator_id,
    }
    result_data = render_template('bye.xml', **jinja_context)
    return Response(result_data, mimetype='text/xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
