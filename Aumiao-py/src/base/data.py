import os

from . import file as File
from .decorator import singleton

DATA_FILE_PATH: str = os.path.join(os.getcwd(), "data/" "data.json")
CACHE_FILE_PATH: str = os.path.join(os.getcwd(), "data/" "cache.json")
SETTING_FILE_PATH: str = os.path.join(os.getcwd(), "data/" "setting.json")


@singleton
class CodeMaoData:
	def __init__(self) -> None:
		data = File.CodeMaoFile().file_load(path=DATA_FILE_PATH, type="json")
		self.USER_DATA.update(data["USER_DATA"])  # type: ignore
		self.ACCOUNT_DATA.update(data["ACCOUNT_DATA"])  # type: ignore

	USER_DATA = {
		"black_room": {
			"user": [],
			"work": [],
			"post": [],
		},
		"comments": [],
		"emojis": [],
		"answers": [],
		"replies": [],
		"ads": [],
	}
	ACCOUNT_DATA = {
		"identity": "",
		"password": "",
		"id": "",
		"nickname": "",
		"description": "",
		"create_time": "",
		"author_level": "",
	}


@singleton
class CodeMaoSetting:
	def __init__(self) -> None:
		data = File.CodeMaoFile().file_load(path=SETTING_FILE_PATH, type="json")
		self.PROGRAM.update(data["PROGRAM"])  # type: ignore
		self.PARAMETER.update(data["PARAMETER"])  # type: ignore
		self.PLUGIN.update(data["PLUGIN"])  # type: ignore
		self.DEFAULT = data["DEFAULT"]  # type: ignore

	PROGRAM = {
		"HEADERS": {
			"Content-Type": "",
			"User-Agent": "",
		},
		"BASE_URL": "",
		"SLOGAN": "",
	}
	PARAMETER = {
		"APP": {},
		"CLIENT": {
			"cookie_check_url": "",
			"get_works_method": "",
			"all_read_type": [],
			"clear_ad_exclude_top": "",
			"password_login_method": "",
		},
	}
	PLUGIN = {
		"prompt": "",
		"DASHSCOPE": {
			"model": "",
			"more": {"stream": "", "extra_body": {"enable_search": ""}},
		},
	}
	DEFAULT = [{"name": "", "action": ""}]
