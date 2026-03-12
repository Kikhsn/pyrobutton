
from pyrogram import enums
from pyrogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, LoginUrl,
    SwitchInlineQueryChosenChat, CopyTextButton, CallbackGame
)
from typing import Optional, Union


class InlinePaginationKeyboard(InlineKeyboardMarkup):
    SYMBOL_FIRST_PAGE = '« {}'
    SYMBOL_PREVIOUS_PAGE = '‹ {}'
    SYMBOL_CURRENT_PAGE = '· {} ·'
    SYMBOL_NEXT_PAGE = '{} ›'
    SYMBOL_LAST_PAGE = '{} »'

    def __init__(self, count_pages: int, current_page: int,
                 callback_pattern: str):
        self.inline_keyboard = list()
        super().__init__(inline_keyboard=self.inline_keyboard)
        self.count_pages = count_pages
        self.current_page = current_page
        self.callback_pattern = callback_pattern
        self.markup

    def add_button(self, text, callback_data):
        return InlineKeyboardButton(
            text=text,
            callback_data=self.callback_pattern.format(
                number=callback_data)
        )

    @property
    def left_pagination(self):
        return [
            self.add_button(
                self.SYMBOL_CURRENT_PAGE.format(number), number)
            if number == self.current_page else self.add_button(
                self.SYMBOL_NEXT_PAGE.format(number), number)
            if number == 4 else self.add_button(
                self.SYMBOL_LAST_PAGE.format(self.count_pages),
                self.count_pages)
            if number == 5 else self.add_button(number, number)
            for number in range(1, 6)
        ]

    @property
    def middle_pagination(self):
        return [
            self.add_button(
                self.SYMBOL_FIRST_PAGE.format(1), 1),
            self.add_button(
                self.SYMBOL_PREVIOUS_PAGE.format(self.current_page - 1),
                self.current_page - 1),
            self.add_button(
                self.SYMBOL_CURRENT_PAGE.format(self.current_page),
                self.current_page),
            self.add_button(
                self.SYMBOL_NEXT_PAGE.format(self.current_page + 1),
                self.current_page + 1),
            self.add_button(
                self.SYMBOL_LAST_PAGE.format(self.count_pages),
                self.count_pages),
        ]

    @property
    def right_pagination(self):
        return [
            self.add_button(
                self.SYMBOL_FIRST_PAGE.format(1), 1),
            self.add_button(
                self.SYMBOL_PREVIOUS_PAGE.format(self.count_pages - 3),
                self.count_pages - 3)
        ] + [
            self.add_button(
                self.SYMBOL_CURRENT_PAGE.format(number), number)
            if number == self.current_page else self.add_button(number, number)
            for number in range(self.count_pages - 2, self.count_pages + 1)
        ]

    @property
    def full_pagination(self):
        return [
            self.add_button(number, number)
            if number != self.current_page else self.add_button(
                self.SYMBOL_CURRENT_PAGE.format(number), number)
            for number in range(1, self.count_pages + 1)
        ]

    @property
    def build_pagination(self):
        if self.count_pages <= 5:
            return self.full_pagination
        else:
            if self.current_page <= 3:
                return self.left_pagination
            elif self.current_page > self.count_pages - 3:
                return self.right_pagination
            else:
                return self.middle_pagination

    def row(self, *args):
        self.inline_keyboard.append([button for button in args])

    @property
    def markup(self):
        self.inline_keyboard.append(self.build_pagination)




class InlineButton(InlineKeyboardButton):
    def __init__(
        self,
        text: str = None,
        callback_data: Optional[Union[str, bytes]] = None,
        url: Optional[str] = None,
        web_app: Optional[WebAppInfo] = None,
        login_url: Optional[LoginUrl] = None,
        user_id: Optional[int] = None,
        switch_inline_query: Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat] = None,
        copy_text: Optional[CopyTextButton|str] = None,
        callback_game: Optional[CallbackGame] = None,
        pay: Optional[bool] = None,
        callback_data_with_password: Optional[bytes] = None,
        icon_custom_emoji_id: Optional[int] = None,
        style: enums.ButtonStyle = enums.ButtonStyle.DEFAULT,
    ):
        
        if isinstance(copy_text, str):
            copy_text = CopyTextButton(copy_text)
            
        super().__init__(
            text=text,
            callback_data=callback_data,
            url=url,
            web_app=web_app,
            login_url=login_url,
            user_id=user_id,
            switch_inline_query=switch_inline_query,
            switch_inline_query_current_chat=switch_inline_query_current_chat,
            switch_inline_query_chosen_chat=switch_inline_query_chosen_chat,
            copy_text=copy_text,
            callback_game=callback_game,
            pay=pay,
            callback_data_with_password=callback_data_with_password,
            icon_custom_emoji_id=icon_custom_emoji_id,
            style=style,
        )