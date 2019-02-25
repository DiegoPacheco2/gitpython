medida=float(input('Uma distância em metros: '))
cm=medida*100
mm=medida*1000
km=medida*0.001
hm=medida*0.01
dam=medida*0.1
dm=medida*10
print('A medida de {}m corresponde a\n {}km\n {}hm\n {:2}dam\n {}dm\n {}cm\n {}mm'.format(medida,km,hm,dam,dm,cm,mm))

