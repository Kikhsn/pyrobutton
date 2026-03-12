# pyrobutton

Keyboard button helpers for [Pyrogram](https://github.com/pyrogram/pyrogram).

## Installation

```bash
pip install pyrobutton
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/Kikhsn/pyrobutton.git
```

## Usage

### InlineKeyboard

```python
from pyrobutton import InlineKeyboard, InlineButton

keyboard = InlineKeyboard(row_width=2)
keyboard.add(
    InlineButton("Button 1", callback_data="btn1"),
    InlineButton("Button 2", callback_data="btn2"),
    InlineButton("Open URL", url="https://example.com"),
)

await message.reply("Hello!", reply_markup=keyboard)
```

#### Pagination

```python
keyboard = InlineKeyboard()
keyboard.paginate(
    count_pages=20,
    current_page=5,
    callback_pattern="page#{number}",
    jump_row=True,   # shows ±5 / ±10 jump buttons (only if count_pages >= 50)
)
```

#### Language selector

```python
keyboard = InlineKeyboard()
keyboard.languages(
    callback_pattern="lang#{locale}",
    locales=["en_US", "id_ID", "ru_RU"],
    row_width=2,
)
```

### ReplyKeyboard

```python
from pyrobutton import ReplyKeyboard, ReplyButton

keyboard = ReplyKeyboard(resize_keyboard=True, row_width=2)
keyboard.add(
    ReplyButton("Share Contact", request_contact=True),
    ReplyButton("Share Location", request_location=True),
)

await message.reply("Choose:", reply_markup=keyboard)
```

### ReplyKeyboardRemove / ForceReply

```python
from pyrobutton import ReplyKeyboardRemove, ForceReply

await message.reply("Keyboard removed", reply_markup=ReplyKeyboardRemove())
await message.reply("Reply to this", reply_markup=ForceReply(placeholder="Type here..."))
```

### InlinePaginationKeyboard

Standalone pagination keyboard (no extra buttons needed):

```python
from pyrobutton import InlinePaginationKeyboard

keyboard = InlinePaginationKeyboard(
    count_pages=10,
    current_page=3,
    callback_pattern="page#{number}",
)
```

## License

MIT