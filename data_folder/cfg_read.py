import configparser


cfg = configparser.ConfigParser()
cfg.read('settings.cfg')
cfg['french']
cfg['french']['greeting']
cfg['files']['bin']