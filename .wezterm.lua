local wt = require 'wezterm'

local config = wt.config_builder()

-- I don't want to use wezterm tabs on hyprland
config.enable_tab_bar = false

-- Best color scheme out there right now
config.color_scheme = 'Tokyo Night'

-- Gotta see that beautiful background
config.window_background_opacity = .5

config.colors = {
    -- Define any more custom color fields here
    background = 'black',
}

-- Disable all wezterm keybinds
config.disable_default_key_bindings = true

-- Enable any of the keybinds again here
local act = wt.action
config.keys = {
    {
        key = 'V', mods = 'CTRL|SHIFT', action = act.PasteFrom("Clipboard")
    },
    {
        key = 'C', mods = 'CTRL|SHIFT', action = act.CopyTo("Clipboard")
    },
}

return config
