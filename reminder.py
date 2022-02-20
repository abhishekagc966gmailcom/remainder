
import datetime

import threading

import pygame

import time


lock=threading.Lock()
drink_flag=1
l1=[300]
l2=[600]
l3=[1200]

# put the default path of the respective music files
path1='C:\\Users\\Abhishek\\Downloads\\water_remainderr.mp3'
path2='C:\\Users\\Abhishek\\Downloads\\walk.mp3'
path3='C:\\Users\\Abhishek\\Downloads\\aankh_ka_exercise.mpeg'


def play_music(_):
    global drink
    pygame.mixer.init()
    pygame.mixer.music.load(_)
    pygame.mixer.music.play(-1)

    try:
        drink=input()
        drink=drink.upper()

    except:

        while drink_flag:

            if drink_flag == 0:
                break
            else:
                time.sleep(1)

    pygame.mixer.music.stop()
    return drink


def drink_water():

    return play_music(path1)

def take_rest():
    return play_music(path2)

def eye_exercise():
    return play_music(path3)


def cntdwn_for_eye_rest(p):

    while p:


        time.sleep(1)
        p-=1
    lock.acquire()
    with open('cntdwn_for_eye_rest.txt', "a") as f:

        while 1:
            print("Enter 'Eye Rested' to stop: ",end=" ")
            rest_message1 = eye_exercise()

            rest_message1 = rest_message1.upper()
            if rest_message1 == 'EYE RESTED':
                f.write(f'\nRested at {datetime.datetime.now()}')

                break

        lock.release()

    p = l3[0]

    cntdwn_for_eye_rest(p)


def cntdwn_for_rest(p):

    while p:

        time.sleep(1)
        # print(timer, end="\r")
        p-=1

    lock.acquire()

    with open('cntdwn_for_rest.txt', "a") as f:

        while 1:
            print("Enter 'Rested' to stop:",end=" ")
            rest_message = take_rest()

            rest_message = rest_message.upper()
            if rest_message == 'RESTED':
                f.write(f'\nRested at {datetime.datetime.now()}')
                lock.release()
                break

    p = l1[0]

    cntdwn_for_rest(p)



def cntdwn_for_water(p):

    while p:

        time.sleep(1)

        p-=1

    lock.acquire()
    with open('drank.txt',"a") as f:

        while 1:
            print("Enter 'Drunked' to stop: ",end=" ")
            drank_message=drink_water()

            drank_message = drank_message.upper()
            if drank_message=='DRUNKED':
                f.write(f'\nDrunked water at {datetime.datetime.now()}')
                lock.release()
                break

    p=l2[0]

    cntdwn_for_water(p)

















if __name__ == '__main__':

    t1=threading.Thread(target=cntdwn_for_water ,args=l2)
    t2=threading.Thread(target=cntdwn_for_rest ,args=l1)
    t3=threading.Thread(target=cntdwn_for_eye_rest ,args=l3)
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    #
    t2.join()
    t3.join()

















