import asyncio
import logging
from typing import Optional, Text, Any, Dict

from aiogram import Bot
from rasa.core.channels import TelegramInput, InputChannel
from rasa.core.channels.telegram import TelegramOutput
from aiogram.utils.exceptions import TelegramAPIError
from rasa.shared.exceptions import RasaException

logger = logging.getLogger(__name__)


class CustomTelegramOutput(TelegramOutput):

	def __init__(self, access_token: Optional[Text], parse_mode: Optional[Text]) -> None:
		Bot.__init__(self, access_token, parse_mode=parse_mode)


class CustomTelegramInput(TelegramInput):

	@classmethod
	def from_credentials(cls, credentials: Optional[Dict[Text, Any]]) -> InputChannel:
		if not credentials:
			cls.raise_missing_credentials_exception()

		return cls(
			credentials.get("access_token"),
			credentials.get("verify"),
			credentials.get("webhook_url"),
			credentials.get("parse_mode"),
		)

	def __init__(
			self,
			access_token: Optional[Text],
			verify: Optional[Text],
			webhook_url: Optional[Text],
			parse_mode: Optional[Text],
			debug_mode: bool = True,
	) -> None:
		super().__init__(access_token, verify, webhook_url, debug_mode)
		self.parse_mode = parse_mode

	def get_output_channel(self) -> CustomTelegramOutput:
		"""Loads the telegram channel."""
		channel = CustomTelegramOutput(self.access_token, self.parse_mode)

		try:
			asyncio.run(channel.set_webhook(url=self.webhook_url))
		except TelegramAPIError as error:
			raise RasaException(
				"Failed to set channel webhook: " + str(error)
			) from error

		return channel
