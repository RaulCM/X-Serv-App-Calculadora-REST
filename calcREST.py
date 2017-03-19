#!/usr/bin/python3

import webapp


class calcRest (webapp.webApp):

    num1 = 0
    num2 = 0
    operador = ''

    def parse(self, request):
        method = request.split(' ', 1)[0]
        resourceName = request.split(' ', 2)[1][1:]
        return (method, resourceName)

    def process(self, parsed):
        method, resourceName = parsed

        if method == "PUT":
            try:
                self.num1, self.num2, self.operador = resourceName.split(',')
                httpCode = "200 OK"
                htmlBody = ("<html><body>Operación introducida: " +
                            str(self.num1) + str(self.operador) +
                            str(self.num2) + "</html>")
            except(ValueError):
                httpCode = "200 OK"
                htmlBody = ("<html><body>Debe introducir dos números y un " +
                            "operador separados por comas.</html>")
        elif method == "GET":
            try:
                if (self.operador == "+"):
                    Resultado = int(self.num1) + int(self.num2)
                elif (self.operador == "-"):
                    Resultado = int(self.num1) - int(self.num2)
                elif (self.operador == "*"):
                    Resultado = int(self.num1) * int(self.num2)
                elif (self.operador == "/"):
                    Resultado = int(self.num1) / int(self.num2)
                else:
                    Resultado = ("Operación desconocida. Intente hacer una" +
                                 " suma, una resta, una multiplicación o " +
                                 "una división")
                httpCode = "200 OK"
                htmlBody = ("<html><body>Resultado de la operación: " +
                            str(self.num1) + str(self.operador) +
                            str(self.num2) + " = " + str(Resultado) +
                            "</html>")
            except(ZeroDivisionError):
                httpCode = "200 OK"
                htmlBody = ("<html><body>No se puede dividir entre 0</html>")
            except(ValueError):
                httpCode = "200 OK"
                htmlBody = ("<html><body>Debe introducir dos números y un " +
                            "operador separados por comas.</html>")
        else:
            httpCode = "HTTP/1.1 405 Method Not Allowed"
            htmlBody = "Método no permitido. Sólo se aceptan PUT y GET."
        return (httpCode, htmlBody)


if __name__ == "__main__":
    try:
        testWebApp = calcRest("localhost", 1234)
    except KeyboardInterrupt:
        print("Closing binded socket")
