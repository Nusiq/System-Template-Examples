[
    # Scripts
    {
        "source": "main.js",
        "target": AUTO_FLAT,
        "on_conflict": "append_end"
    },
    {
        "source": "subscripts/*.js",
        "target": AUTO
    },
    # Boots
    {
        "source": "boots/double_jump_boots.attachable.json",
        "target": AUTO_FLAT
    },
    {
        "source": "boots/double_jump_boots.attachable.png",
        "target": AUTO_FLAT
    },
    {
        "source": "boots/double_jump_boots.bp_item.json",
        "target": AUTO_FLAT
    },
    {
        "source": "boots/double_jump_boots.item.png",
        "target": AUTO_FLAT
    },
    # Item texture
    {
        "source": "item_texture.json",
        "target": "RP/textures/item_texture.json",
        "on_conflict": "merge"
    }
]