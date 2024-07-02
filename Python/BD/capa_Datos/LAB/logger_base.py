import logging as log

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('registro_lab_usuarios.log'),
                    log.StreamHandler()
                ]
                )

if __name__ == '__main__':

    log.debug('Mensaje a nivle debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mnesaje a nivel de eroor')
    log.critical('Mensaje a nivel de Critical')