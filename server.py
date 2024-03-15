import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from handlers import buildable_sets_by_user, minimum_competitive_custom_set, set_building_collaboration, \
    mixed_color_sets

hostName = "localhost"
serverPort = 8080


def _set_headers(self):
    self.send_header("Content-type", "application/json")
    self.send_header("Access-Control-Allow-Origin", "*")
    self.end_headers()


class MyServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_GET(self):
        parse_result = urlparse(self.path)
        parsed_path = parse_result.path.split("/")[-1]
        query_params = parse_qs(parse_result.query)
        response = {"Welcome to the Builder Catalogue Challenge": "Welcome to the Builder Catalogue Challenge"}
        if not self.path or "/buildable-by-user" in self.path:
            response = buildable_sets_by_user.create_buildable_sets_response(parsed_path)
        elif "/custom-set" in self.path:
            response = minimum_competitive_custom_set.get_minimum_viable_custom_build(parsed_path)
        elif "/collaboration-set" in self.path:
            response = set_building_collaboration.users_collaboration_for_sets(parsed_path, query_params.get("setName")[
                0] if query_params.get("setName") else "")
        elif "/mixed-colors-sets" in self.path:
            response = mixed_color_sets.get_new_sets_by_switching_colors(parsed_path)
        self.send_response(200 if response else 400)
        self._set_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
