"В данной папке мы обрабатываем все команды которые пишуться через /"

from aiogram import Router

commands_router = Router()

import commands.spam
import commands.start
import commands.my_info
import commands.send_cat_photo
import commands.actions
import commands.alive
import commands.messages