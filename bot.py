from vkwave.bots import SimpleLongPollBot
from vkwave.bots.utils.keyboards import Keyboard
from vkwave.bots.utils.keyboards.keyboard import ButtonColor
from vkwave.api import API
from vkwave.client import AIOHTTPClient

api_session = API(tokens="2ead108727b6390d49259b2c3368ed1a524b063d499ebc3a9c40d4fc1fc50aa65173b5c144eaefb7f4e29", clients=AIOHTTPClient())
api = api_session.get_context()

bot = SimpleLongPollBot(tokens=["fbaa53705a5bf1030057f972b574a1ed87596085bcf567c993ec6175bb32601202418a346e4fcb15d47b0",
	"58f5f870798f7ec951e2d543adf9885ddaf932508b74920b270adbf2b36711645665d3a16af54ee501d00",
	"fe0d119e325fc37f5316284a6114a429d634d2a319f788ec6f731dad82145c6664668ed2041b0b7d085d7"],
	group_id="204710152")

@bot.message_handler(bot.conversation_type_filter(from_what="from_pm"),
	bot.text_contains_filter("назад")
	| bot.text_contains_filter("начать")
	| bot.text_contains_filter("всё понятно")
	| bot.text_contains_filter("меню")
	| bot.text_contains_filter("старт")	)
async def start(event: bot.SimpleBotEvent) -> str:
	kb = Keyboard(one_time=True)
	kb.add_text_button("Кто мы?", color=ButtonColor.POSITIVE)
	kb.add_text_button("Сезон 1", color=ButtonColor.POSITIVE)
	kb.add_row()
	kb.add_link_button("Общий чат", "https://vk.me/join/blpFh9NorHrlkFgZIpxVOQiYAno6pTCSUsw=")
	kb.add_row()
	kb.add_text_button("Позвать Администратора", color=ButtonColor.PRIMARY)	
	user_data = (await event.api_ctx.users.get(user_ids=event.object.object.message.peer_id)).response[0]
	await event.answer(message="Выберите, что вас интересует и нажмите соответствующую кнопку", keyboard=kb.get_keyboard())

@bot.message_handler(bot.conversation_type_filter(from_what="from_pm"), bot.text_contains_filter("кто мы"))
async def info(event: bot.SimpleBotEvent) -> str:
	kb = Keyboard(one_time=True)
	kb.add_text_button("Назад", color=ButtonColor.SECONDARY)
	await event.answer(message="Ебаклаки", keyboard=kb.get_keyboard())

@bot.message_handler(bot.conversation_type_filter(from_what="from_pm"), bot.text_contains_filter("хочу знать больше"))
async def more_info(event: bot.SimpleBotEvent) -> str:
	kb = Keyboard(one_time=True)
	kb.add_text_button("Всё понятно!", color=ButtonColor.POSITIVE)
	kb.add_row()
	kb.add_text_button("Есть вопросы.", color=ButtonColor.NEGATIVE)
	await event.answer(message="БЛА-БЛА", keyboard=kb.get_keyboard())

@bot.message_handler(bot.conversation_type_filter(from_what="from_pm"),
	bot.text_contains_filter("позвать администратора")
	| bot.text_contains_filter("есть вопрос"))
async def call_admin(event: bot.SimpleBotEvent) -> str:
	kb = Keyboard(one_time=True)
	kb.add_text_button("Меню", color=ButtonColor.SECONDARY)
	await event.answer(message="Администратор ответит вам в кратчайшее время.", keyboard=kb.get_keyboard())
	await api.messages.send(user_id = 181883242, random_id = 0, peer_id = 181883242, message = 'Пидор найден')

@bot.message_handler(bot.conversation_type_filter(from_what="from_pm"), bot.text_contains_filter("сезон 1"))
async def season_1(event: bot.SimpleBotEvent) -> str:
	kb = Keyboard(one_time=True)
	kb.add_text_button("Хочу участвовать", color=ButtonColor.POSITIVE)
	kb.add_row()
	kb.add_text_button("Информация", color=ButtonColor.SECONDARY)

@bot.message_handler(bot.conversation_type_filter(from_what="from_pm"), bot.text_contains_filter("хочу участвовать"))
async def want_to_participate(event: bot.SimpleBotEvent) -> str:
	kb = Keyboard(one_time=True)
	kb.add_text_button("Умею", color=ButtonColor.POSITIVE)
	kb.add_row()
	kb.add_text_button("Не умею", color=ButtonColor.NEGATIVE)
	await event.answer(message = "Умеешь покупать крипту?", keyboard=kb.get_keyboard())

@bot.message_handler(bot.conversation_type_filter(from_what="from_pm"), bot.text_contains_filter("не умею"))
async def i_cant(event: bot.SimpleBotEvent) -> str:
	kb = Keyboard(one_time=True)
	kb.add_text_button("Теперь умею!", color=ButtonColor.POSITIVE)
	kb.add_row()
	kb.add_text_button("Позвать администратора.", color=ButtonColor.PRIMARY)
	kb.add_row()
	kb.add_text_button('Меню', color=ButtonColor.SECONDARY)
	await event.answer(message = "ИНФА О ТОМ КАК ПОКУПАТЬ КРИПТУ", keyboard=kb.get_keyboard())

@bot.message_handler(bot.conversation_type_filter(from_what="from_pm"), bot.text_contains_filter("умею")
	| bot.text_contains_filter('теперь умею'))
async def i_can(event: bot.SimpleBotEvent) -> str:
	kb = Keyboard(one_time=True)
	kb.add_text_button("Далее.", color=ButtonColor.POSITIVE)
	await event.answer(message = """https://etherconnect.co/register/YLfS8AJjTx 
	Переходи по ссылке и убедись, что в графе 'Имя' указано Crypta. Поздравляем ёпта.""", keyboard=kb.get_keyboard())

@bot.message_handler(bot.conversation_type_filter(from_what="from_pm"), bot.text_contains_filter("далее"))
async def i_can(event: bot.SimpleBotEvent) -> str:
	kb = Keyboard(one_time=True)
	kb.add_text_button("Всё понятно.", color=ButtonColor.POSITIVE)
	await event.answer(message = """Поздравляем, ёпта. Подпишись на рассылку.""", keyboard=kb.get_keyboard())




bot.run_forever()
