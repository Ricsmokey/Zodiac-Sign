
from calendar import month
import datetime
import http.server
import os
import sys
import time
import logging as logger
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
TEMPLATES_DIR = "templates"


http.server.BaseHTTPRequestHandler.protocol_version = "HTTP/1.0"



class Server:
    def __init__(self, host, port, directory, log_file=None):
        self.host = host
        self.port = port
        self.directory = directory
        self.log_file = log_file
        self.logger = logger.Logger(__name__) if log_file else None
        self.httpd = None

    def start(self):
        handler = self.create_handler()
        self.httpd = http.server.HTTPServer((self.host, self.port), handler)
        print(f"Serving HTTP on {self.host} port {self.port} (http://{self.host}:{self.port}/) ...")
        try:
            self.httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            self.httpd.server_close()

    def create_handler(self):
        directory = self.directory
        logger_instance = self.logger    

        class CustomHandler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory = directory, **kwargs)
            
            def log_message(self, format, *args):
                if logger_instance:
                    logger_instance.log(format % args) 
                else:
                    super().log_message(format, *args)
            
            def handle_horoscope(self):
                query = self.path.split("?")[-1]
                params = dict(param.split("=") for param in query.split("&"))
                month = int(params.get("month", 0))
                day = int(params.get("day", 0))
                sign = self.get_sign(month, day)
                env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
                template = env.get_template("horoscope.html")
                content = template.render(sign=sign)
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))

            def get_sign(self, month, day):
                if (month == 1 and day >= 20) or (month == 2 and day <= 18):
                    return "Aquarius"
                elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
                    return "Pisces"
                elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
                    return "Aries"
                elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
                    return "Taurus"
                elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
                    return "Gemini"
                elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
                    return "Cancer"
                elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
                    return "Leo"
                elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
                    return "Virgo"
                elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
                    return "Libra"
                elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
                    return "Scorpio"
                elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
                    return "Sagittarius"
                else:
                    return "Capricorn"
            

            def do_GET(self):
                if self.path == "/":
                    self.path = "/index.html"
                elif self.path.startswith("/horoscope"):
                    self.handle_horoscope()
                    return
                return super().do_GET()
        
        return CustomHandler
    
if __name__ == "__main__":
    host = "localhost"
    port = 8080
    directory = os.path.join(os.getcwd(), "static")
    log_file = None
    server = Server(host, port, directory, log_file)
    server.start()