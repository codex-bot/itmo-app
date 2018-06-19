from .base import Base


class StateMenu(Base):

    def __init__(self, state_controller):
        super().__init__(state_controller)

        self.response_phrases = {
            'ratings': [
                'Позиции в рейтингах'
            ],

            'EGE_calc': [
                'Подобрать направления по баллам'
            ],

            'notifications': [
                'Настроить оповещения'
            ],

            'logout': [
                'Выйти из системы'
            ],
        }

    async def before(self, payload, data):
        message = "Что тебя интересует?"

        buttons = [
            [
                {'text': self.response_phrases['ratings'][0]}
            ],
            [
                {'text': self.response_phrases['EGE_calc'][0]}
            ],
            [
                {'text': self.response_phrases['notifications'][0]}
            ],
            [
                {'text': self.response_phrases['logout'][0]}
            ]
        ]

        keyboard = {
            'keyboard': buttons,
            'resize_keyboard': True,
            'one_time_keyboard': True
        }

        await self.sdk.send_keyboard_to_chat(payload['chat'], message, keyboard)

    async def process(self, payload, data):
        self.sdk.log("State Menu processor fired with payload {}".format(payload))

        text = payload['text']

        # TODO process menu

        if text in self.response_phrases['ratings']:
            pass
        elif text in self.response_phrases['EGE_calc']:
            pass
        elif text in self.response_phrases['notifications']:
            pass
        elif text in self.response_phrases['logout']:
            # todo remove user from db

            message = 'Если понадоблюсь, выполни команду /start.'

            await self.sdk.send_text_to_chat(
                payload["chat"],
                message
            )

            return await self.controller.goto(payload, 'start')

        message = 'Не понимаю'

        await self.sdk.send_text_to_chat(
            payload["chat"],
            message
        )

        return await self.controller.goto(payload, 'menu')
