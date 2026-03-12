from pyrogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply)


class ReplyKeyboard(ReplyKeyboardMarkup):
    def __init__(self, resize_keyboard=None, one_time_keyboard=None,
                 selective=None, placeholder=None, row_width=3):
        self.keyboard = list()
        super().__init__(
            keyboard=self.keyboard,
            resize_keyboard=resize_keyboard,
            one_time_keyboard=one_time_keyboard,
            selective=selective,
            placeholder=placeholder
        )
        self.row_width = row_width

    def add(self, *args, row_width=None):
        row_width = row_width or self.row_width
        rows = [
            args[i:i + row_width]
            for i in range(0, len(args), row_width)
        ]

        for row in rows:
            self.keyboard.append(row)
    
    def clear(self):
        self.keyboard.clear()

    def row(self, *args):
        self.keyboard.append([button for button in args])


class ReplyButton(KeyboardButton):
    def __init__(self, text=None, request_contact=None, request_location=None,
                 request_user=None, request_chat=None, request_poll=None,
                 web_app=None):
        super().__init__(
            text=text,
            request_contact=request_contact,
            request_location=request_location,
            request_user=request_user,
            request_chat=request_chat,
            request_poll=request_poll,
            web_app=web_app
        )


class ReplyKeyboardRemove(ReplyKeyboardRemove):
    def __init__(self, selective=None):
        super().__init__(selective=selective)


class ForceReply(ForceReply):
    def __init__(self, selective=None, placeholder=None):
        super().__init__(selective=selective, placeholder=placeholder)
        