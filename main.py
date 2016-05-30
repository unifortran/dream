#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tornado.options
import tornado.web
import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

def main():
    print("Starting python service ...")
    tornado.options.define('port', default=8000,
                           help="run on the given port", type=int)

    handlers = [
        (r"/", IndexHandler),
        (r"/(.*html)", tornado.web.StaticFileHandler, {"path": "static"}),
        (r"/((js|css)/.*)", tornado.web.StaticFileHandler, {"path": "static"}),
    ]

    template_path = os.path.join(os.path.dirname(__file__), "template")
    static_path = os.path.join(os.path.dirname(__file__), "static")

    app = tornado.web.Application( handlers = handlers,
                                   template_path = template_path,
                                   static_path = static_path
    )

    # xheaders=True nginx 负载均衡用
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
