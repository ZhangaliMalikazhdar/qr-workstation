import qrcode
img = qrcode.make('this data')
type(img)
img.save('thi.png')
