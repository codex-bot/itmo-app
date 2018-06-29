from .base import CommandBase


class CommandHelp(CommandBase):

    async def __call__(self, payload):
        self.sdk.log("/itmo_help handler fired with payload {}".format(payload))

        message = "Этот бот помогает абитуриенту отслеживать состояние поступления " \
                  "в Университет ИТМО, подбирать направления по результатам ЕГЭ.\n" \
                  "\n" \
                  "Техподдержка team@ifmo.su"

        await self.sdk.send_text_to_chat(
            payload["chat"],
            message
        )

        # Reenter to current state
        await self.state.reenter(payload)
