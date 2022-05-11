import environ

env = environ.Env()
env.read_env('BOT-TOKEN')

BOT_TOKEN = env.str('BOT-TOKEN')
