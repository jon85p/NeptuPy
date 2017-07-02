#!/usr/bin/env python3

def norm_angle(ang):
    if (ang >= 0) and (ang <= 360):
        return ang
    if ang > 360:
        return 360*(ang/360 - int(ang/360))
    if ang < 0:
        suma = 360*((-ang)//360 + 1)
        return suma + ang

class exporta_reg:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.out_file = '# Region file format: DS9 version 4.1\nglobal color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nphysical\n'

    def agrega_circulo(self, xcenter, ycenter, radius, color='green', texto=''):
        '''
        Agrega un círculo a la instancia
        '''
        xcenter = "{:1.4f}".format(xcenter)
        ycenter = "{:1.4f}".format(ycenter)
        radius = "{:1.4f}".format(radius)
        self.out_file = self.out_file + 'circle(' + xcenter + ',' + ycenter + ',' + radius + ') # color=' + color + ' text={' + texto + '}\n'

    def agrega_elipse(self, xcenter, ycenter, xradius, yradius, angle=0, color='green', texto=''):
        '''
        Agrega una elipse a la instancia
        '''
        xcenter = "{:1.4f}".format(xcenter)
        ycenter = "{:1.4f}".format(ycenter)
        xradius = "{:1.4f}".format(xradius)
        yradius = "{:1.4f}".format(yradius)
        angle = "{:1.4f}".format(norm_angle(angle))
        self.out_file = self.out_file + 'ellipse(' + xcenter + ',' + ycenter + ',' + xradius + ',' + yradius + ',' + angle + ') # color=' + color + ' text={' + texto + '}\n'

    def agrega_caja(self, xcenter, ycenter, dx, dy, angle=0, color='green', texto=''):
        '''
        Agrega una caja a la instancia
        '''
        xcenter = "{:1.4f}".format(xcenter)
        ycenter = "{:1.4f}".format(ycenter)
        dx = "{:1.4f}".format(dx)
        dy = "{:1.4f}".format(dy)
        angle = "{:1.4f}".format(norm_angle(angle))
        self.out_file = self.out_file + 'box(' + xcenter + ',' + ycenter + ',' + dx + ',' + dy + ',' + angle + ') # color=' + color + ' text={' + texto + '}\n'

    def agrega_corona(self, xcenter, ycenter, radius1, radius2, color='green', texto=''):
        '''
        Agrega una corona a la instancia
        '''
        xcenter = "{:1.4f}".format(xcenter)
        ycenter = "{:1.4f}".format(ycenter)
        radius1 =  "{:1.4f}".format(radius1)
        radius2 = "{:1.4f}".format(radius2)
        self.out_file = self.out_file + 'annulus(' + xcenter + ',' + ycenter + ',' + radius1 + ',' + radius2 + ') # color=' + color + ' text={' + texto + '}\n'

    def escribe_reg(self):
        '''
        Escribe el archivo .reg de salida
        '''
        el_buffer = (self.out_file).encode('utf8')
        sal = open(self.nombreArchivo, 'wb')
        sal.write(el_buffer)
        sal.close()
