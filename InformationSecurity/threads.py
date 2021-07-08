from threading import Thread
import time

def car(speed, racer):
    path = 0
    while path <= 100:
        path += speed
        time.sleep(0.5)
        print('Racer: {} KM: {}\n'.format(racer, path))


t_car1 = Thread(target=car, args=[10, "Eduardo"])
t_car2 = Thread(target=car, args=[20, 'Pithon'])

t_car1.start()
t_car2.start()
