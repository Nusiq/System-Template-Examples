[
    # Player beahvior
    {
        "source": "player.behavior.json",
        "target": AUTO_FLAT,
        "on_conflict": "merge"
    },
    {
        "source": "player.bp_ac.json",
        "target": AUTO_FLAT,
        "on_conflict": "merge"
    },
    # Custom item
    {
        "source": "magic_feather.bp_item.json",
        "target": AUTO_FLAT
    },
    {
        "source": "magic_feather.item.png",
        "target": AUTO_FLAT
    },
    {
        "source": "item_texture.json",
        "target": "RP/textures/item_texture.json",
        "on_conflict": "merge"
    }
]