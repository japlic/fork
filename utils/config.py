from utils.CONSTANTS import *


@dataclass
class Config:
    Development = True  # if true will use base server ID's else will use development server ID's
    colors = Colors
    colours = colors
    if Development:
        print("Using Development Config variable")
        channels = Channels.dev()
        roles = Roles.dev()
        emojis = Emojis.dev()
        debug = True
    else:
        emojis = Emojis
        channels = Channels
        roles = Roles
        debug = False
