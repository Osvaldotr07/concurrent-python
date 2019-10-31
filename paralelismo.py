import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def new_process(time_to_sleep=0):
    logging.info('Comenzamos el proceso hijo!')

    time.sleep(time_to_sleep)

    logging.info('Terminamos el proceso hijo!')


def main():
    process = multiprocessing.Process(target=new_process,
                                    name='proceso_hijo',
                                    args=(5,),
                                    daemon=False)

    process.start()
    process.join()

    logging.info(f'Fin del proceso principal')

if __name__ == '__main__':
    main()
