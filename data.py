HEROES = {
    "Axe": {"roles": [3], "tags": ["tank", "initiator", "disable", "blademail"]},
    "Tidehunter": {"roles": [3], "tags": ["tank", "initiator", "disable"]},
    "Legion Commander": {"roles": [3], "tags": ["initiator", "duelist", "physical"]},
    "Bane": {"roles": [4, 5], "tags": ["disable", "save", "single target"]},
    "Shadow Shaman": {"roles": [4, 5], "tags": ["disable", "push", "nuke"]},
    "Earth Spirit": {"roles": [4], "tags": ["save", "mobility", "stun"]},
    "Dazzle": {"roles": [4, 5], "tags": ["save", "heal", "armor"]},
    "Oracle": {"roles": [4, 5], "tags": ["save", "dispel", "heal"]},
    "Lina": {"roles": [2, 4], "tags": ["nuke", "stun", "magic"]},
    "Phantom Assassin": {"roles": [1], "tags": ["carry", "physical", "evasion"]},
    "Anti-Mage": {"roles": [1], "tags": ["carry", "mobility", "mana burn"]},
    "Wraith King": {"roles": [1], "tags": ["carry", "tank", "reincarnation"]},
    "Crystal Maiden": {"roles": [5], "tags": ["disable", "aura", "nuke"]},
    "Witch Doctor": {"roles": [5], "tags": ["heal", "stun", "nuke"]},
    "Sven": {"roles": [1], "tags": ["carry", "cleave", "stun"]},
    "Earthshaker": {"roles": [4], "tags": ["stun", "initiator", "area"]},
    "Invoker": {"roles": [2], "tags": ["nuke", "control", "versatile"]},
    "Lion": {"roles": [4, 5], "tags": ["disable", "nuke", "mana drain"]},
    "Pudge": {"roles": [3, 4], "tags": ["tank", "hook", "disable"]},
    "Slardar": {"roles": [3], "tags": ["initiator", "armor reduction", "bash"]},
    "Juggernaut": {"roles": [1], "tags": ["carry", "magic immunity", "heal"]},
}

SCENARIOS = [
    {
        "description": "Враг выбрал Phantom Assassin и Slardar. Твоя команда уже взяла Crystal Maiden, Witch Doctor и Sven. Ты играешь на оффлейне (позиция 3). Нужен прочный герой, способный справиться с уклонением PA и физическим уроном Slardar.",
        "allies": ["Crystal Maiden", "Witch Doctor", "Sven"],
        "enemies": ["Phantom Assassin", "Slardar"],
        "position": 3,
        "options": ["Axe", "Tidehunter", "Legion Commander"],
        "correct": "Axe",
        "explanation": "Axe с Berserker's Call вынуждает PA атаковать его лицом к лицу, а Blademail наносит отражённый урон, игнорирующий уклонение. Также Call даёт контроль, который не снимается BKB, и позволяет команде быстро убить PA."
    },
    {
        "description": "Союзники взяли Anti-Mage (керри), Earthshaker и Invoker (мид). У врагов Wraith King, Lion и Pudge. Ты на 4-й позиции (поддержка). Нужен герой с надёжным контролем и возможностью сдерживать Wraith King.",
        "allies": ["Anti-Mage", "Earthshaker", "Invoker"],
        "enemies": ["Wraith King", "Lion", "Pudge"],
        "position": 4,
        "options": ["Bane", "Shadow Shaman", "Earth Spirit"],
        "correct": "Bane",
        "explanation": "Bane — классический контр-пик к Wraith King. Fiend's Grip пробивает BKB, не даёт WK использовать способности во время действия ультимейта, а Enfeeble сильно снижает его урон. Nightmare позволяет легко выставлять сетапы для союзников."
    },
    {
        "description": "Враги взяли Juggernaut и Lina. Ваша команда: Dazzle, Oracle и Sven. Твоя роль — мид (позиция 2). Нужен герой с магическим уроном, чтобы убивать сквозь спасение Dazzle/Oracle, и способный пережить магический урон Lina.",
        "allies": ["Dazzle", "Oracle", "Sven"],
        "enemies": ["Juggernaut", "Lina"],
        "position": 2,
        "options": ["Lina", "Invoker", "Pudge"],
        "correct": "Invoker",
        "explanation": "Invoker через Tornado+EMP может выжигать ману у Juggernaut (мешая Blade Fury) и Lina, а Cold Snap прерывает каст ульта Lina. Forge Spirits помогают контролировать линию. У Invoker высокий магический бурст, чтобы убивать героев до срабатывания спасения Dazzle."
    },
    {
        "description": "Союзники: Crystal Maiden, Sven, Earthshaker. Враг выбрал Phantom Assassin и Tidehunter. Ты ищешь героя на позицию 4 (саппорт), который может инициировать драки и имеет способность снимать уклонение PA (break) или давать команде возможность её убить.",
        "allies": ["Crystal Maiden", "Sven", "Earthshaker"],
        "enemies": ["Phantom Assassin", "Tidehunter"],
        "position": 4,
        "options": ["Shadow Shaman", "Lion", "Bane"],
        "correct": "Shadow Shaman",
        "explanation": "Shadow Shaman даёт две мгновенные способности контроля (Hex и Shackles), что идеально для ловли PA до того, как она включит BKB. Serpent Wards наносят физический урон, который не промахивается по уклонению, а также быстро разрушают башни после удачного ганга."
    },
    {
        "description": "Враги собрали масс-физический урон: Slardar, Phantom Assassin, Juggernaut. Ваша команда уже с Oracle, Invoker и Crystal Maiden. От вас нужен оффлейнер (поз. 3), который может пережить физическую атаку и нанести ответный урон.",
        "allies": ["Oracle", "Invoker", "Crystal Maiden"],
        "enemies": ["Slardar", "Phantom Assassin", "Juggernaut"],
        "position": 3,
        "options": ["Tidehunter", "Axe", "Legion Commander"],
        "correct": "Axe",
        "explanation": "Axe опять лучший выбор: высокий природный армор, Call сводит на нет уклонение, а Blademail возвращает урон. Anchor Smash от Tidehunter тоже хорош, но Axe выигрывает благодаря гарантированному контролю даже через BKB и более быстрому уничтожению PA."
    },
]
