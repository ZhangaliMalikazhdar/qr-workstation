import segno

qr = segno.make_qr('hola')
qr1 = segno.make_qr('this is is')
qr.save('1.pdf')
qr1.save('2.png')

