#!/usr/bin/env python3
# All right reserved 2013
# Description: Dota 2 Library (Heroes Full Information)
# URL: http://github.com/Lardjo

"""
Example for hero information

hero = {

    id: {'name': '',
         'role': '',
         'side': '',
         'class': '',
         'bio': '',
         'strength': '',
         'agility': '',
         'intelligence': '',
         'avatar': ''}

}

"""

heroes_info = {

    1: {'name': 'Anti-Mage', 'avatar': 'img/dota/heroes/antimage.png'},

    2: {'name': 'Axe',
        'role': 'Durable, Initiator, Disabler, Jungler',
        'side': 'The Dire',
        'class': 'Strength',
        'bio': '<strong>Mogul Khan</strong> the <strong>Axe</strong> is a savage melee strength hero, infamous for '
               'creating chaos in battle and thriving off of it. He is commonly played as an initiator with a large '
               'semi-carry presence that quickly transitions into a support role later in the game. His fighting style '
               'demands that he gets up close and very personal. He can taunt enemies into targeting him and counters '
               'those who try to strike him with a sweeping Counter Helix that slashes all enemies at melee range. '
               'Axe has a tendency to draw opponents so deep in the fight that they do not have a chance to escape, '
               'each soul he draws infusing his own love of war; his ultimate, Culling Blade bolsters that talent '
               'with an attack that unconditionally kills a unit with low health.',
        'strength': '25 + 2.5',
        'agility': '20 + 2.2',
        'intelligence': '18 + 1.6',
        'avatar': 'img/dota/heroes/axe.png'
    },

    3: {'name': 'Ban', 'avatar': 'img/dota/heroes/bane.png'},
    4: {'name': 'Bloodseeker', 'avatar': 'img/dota/heroes/bloodseeker.png'},
    5: {'name': 'Crystal Maiden', 'avatar': 'img/dota/heroes/crystal_maiden.png'},
    6: {'name': 'Drow Ranger', 'avatar': 'img/dota/heroes/drow_ranger.png'},
    7: {'name': 'Earthshaker', 'avatar': 'img/dota/heroes/earthshaker.png'},

    8: {'name': 'Juggernaut',
        'role': 'Carry, Pusher',
        'side': 'The Radiant',
        'bio': '<strong>Yurnero</strong> the <strong>Juggernaut</strong> is a melee agility hero whose abilities allow '
               'him to sprint into battle and '
               'recklessly devastate enemies in an impenetrable flurry of blades. His skills grant invulnerability '
               'and magic immunity, turning him into an unstoppable force on a hairpin. Juggernaut is strong both '
               'offensively and defensively, and deals heavy damage both physical and magical with his Blade Fury '
               'and Omnislash ultimate, but he possesses below average strength and intelligence attributes, so he '
               'does not have as much health and mana as other heroes and is vulnerable when his abilities are on '
               'cooldown. For this reason, although his abilities make him powerful even in the early game, he cannot '
               'charge into forces without restraint until farmed and is usually played as a carry.',
        'class': 'Agility',
        'strength': '20 + 1.9',
        'agility': '20 + 2.85',
        'intelligence': '14 + 1.4',
        'avatar': 'img/dota/heroes/juggernaut.png'
    },

    9: {'name': 'Mirana', 'avatar': 'img/dota/heroes/mirana.png'},
    10: {'name': 'Morphling', 'avatar': 'img/dota/heroes/morphling.png'},
    11: {'name': 'Shadow Fiend', 'avatar': 'img/dota/heroes/nevermore.png'},
    12: {'name': 'Phantom Lancer', 'avatar': 'img/dota/heroes/phantom_lancer.png'},
    13: {'name': 'Puck', 'avatar': 'img/dota/heroes/puck.png'},
    14: {'name': 'Pudge', 'avatar': 'img/dota/heroes/pudge.png'},
    15: {'name': 'Razor', 'avatar': 'img/dota/heroes/razor.png'},
    16: {'name': 'Sand King', 'avatar': 'img/dota/heroes/sand_king.png'},
    17: {'name': 'Storm Spirit', 'avatar': 'img/dota/heroes/storm_spirit.png'},
    18: {'name': 'Sven', 'avatar': 'img/dota/heroes/sven.png'},

    19: {'name': 'Tiny',
         'role': 'Disabler, Nuker, Initiator, Durable',
         'class': 'Strength',
         'side': 'The Radiant',
         'bio': '<strong>Tiny the Stone Giant</strong> is a melee Strength hero with powerful ganking and killing '
                'potential. Although he starts off vulnerable in lane with his pitiful mana pool and almost '
                'non-existent armor, with a few levels, he gets considerably stronger. His killing power in the '
                'early and midgame comes from comboing his two active abilities. Avalanche engulfs an area in a '
                'wave of stones, dealing respectable damage and stunning enemies. Toss allows Tiny to pick up a '
                'random unit near himself and launch it at the designated location, dealing damage to all enemies '
                'at the location as well as additional damage to the thrown unit if an enemy. It can be used to '
                'displace an ally within the enemy team, but is mostly used on enemies themselves to deliver '
                'massive damage. If chained immediately with Avalanche, it will also double the damage the target '
                'takes from Avalanche, allowing Tiny to easily dispatch fragile enemy heroes in a matter of seconds. '
                'Although his nuking potential with his two active abilities is already considerable, his passives, '
                'Craggy Exterior and Grow turn Tiny into a formidable physical combatant as well. Craggy Exterior '
                'provides Tiny with some much needed armor, and gives him a chance to stun enemies that attack him '
                'from too close, making Tiny a potent counter to fast-attacking melee heroes. Grow increases Tiny\'s '
                'size and provides him a massive boost to his attack damage, movespeed, and Toss damage, at the cost '
                'of some attack speed. Aghanim\'s Scepter is an almost essential item on Tiny since it allows him to '
                'permanently equip a tree, giving him extra attack range as well as a powerful cleaving attack. '
                'Although Tiny initially lives up to his name by starting off small and weak, much like an avalanche, '
                'he quickly grows in size and strength until he becomes a hulking behemoth with enormous health and '
                'damage output.',
         'strength': '24 + 3.0',
         'agility': '9 + 0.9',
         'intelligence': '14 + 1.6',
         'avatar': 'img/dota/heroes/tiny.png'
    },

    20: {'name': 'Vengeful Spirit', 'avatar': 'img/dota/heroes/vengefulspirit.png'},
    21: {'name': 'Windranger', 'avatar': 'img/dota/heroes/windrunner.png'},
    22: {'name': 'Zeus', 'avatar': 'img/dota/heroes/zuus.png'},
    23: {'name': 'Kunkka', 'avatar': 'img/dota/heroes/kunkka.png'},
    25: {'name': 'Lina', 'avatar': 'img/dota/heroes/lina.png'},
    26: {'name': 'Lion', 'avatar': 'img/dota/heroes/lion.png'},
    27: {'name': 'Shadow Shaman', 'avatar': 'img/dota/heroes/shadow_shaman.png'},
    28: {'name': 'Slardar', 'avatar': 'img/dota/heroes/slardar.png'},
    29: {'name': 'Tidehunter', 'avatar': 'img/dota/heroes/tidehunter.png'},
    30: {'name': 'Witch Doctor', 'avatar': 'img/dota/heroes/witch_doctor.png'},
    31: {'name': 'Lich', 'avatar': 'img/dota/heroes/lich.png'},
    32: {'name': 'Riki', 'avatar': 'img/dota/heroes/riki.png'},
    33: {'name': 'Enigma', 'avatar': 'img/dota/heroes/enigma.png'},
    34: {'name': 'Tinker', 'avatar': 'img/dota/heroes/tinker.png'},

    35: {'name': 'Sniper',
         'role': 'Carry',
         'class': 'Agility',
         'side': 'The Radiant',
         'bio': '<strong>Kardel Sharpeye</strong> the <strong>Sniper</strong> is a ranged agility hard carry who '
                'excels at dealing heavy damage at an incredible range. His third ability, Take Aim, allows him '
                'to deal high DPS at a safe distance, and avoiding damage as he is relatively frail. He also excels '
                'at harassing enemies due to his second ability, Headshot, which gives him a chance to do extra '
                'damage and mini-stun, and his first ability, Shrapnel, which slows and deals damage over time '
                'in an area. While he can be a nuisance to lane against, he is also extremely squishy early-game '
                'and requires supports to lane effectively. He scales extremely hard into the late game, dealing '
                'a remarkable amount of dps while sitting outside of harm\'s reach, almost permastunning heroes '
                'with his headshot. Though he is a rather frail hero, his potential in the hands of a good player '
                'and team is high.',
         'strength': '16 + 1.7',
         'agility': '21 + 2.9',
         'intelligence': '15 + 2.6',
         'avatar': 'img/dota/heroes/sniper.png'
    },

    36: {'name': 'Necrophos', 'avatar': 'img/dota/heroes/necrolyte.png'},
    37: {'name': 'Warlock', 'avatar': 'img/dota/heroes/warlock.png'},
    38: {'name': 'Beastmaster', 'avatar': 'img/dota/heroes/beastmaster.png'},
    39: {'name': 'Queen of Pain', 'avatar': 'img/dota/heroes/queenofpain.png'},
    40: {'name': 'Venomancer', 'avatar': 'img/dota/heroes/venomancer.png'},

    41: {'name': 'Faceless Void',
         'role': 'Carry, Initiator, Disabler, Escape',
         'class': 'Agility',
         'side': 'The Dire',
         'bio': '<strong>Darkterror</strong> the <strong>Faceless Void</strong> is a melee agility hard carry hero. '
                'Given a little time, he becomes a terrifyingly powerful hero capable of destroying entire enemy '
                'teams. Wielding his cosmically powered mace, each hit can lock his foes in time, stopping them '
                'in place. He can jump into or out of combat using Time Walk, and passively can avoid any damage '
                'with Backtrack which even works against Monkey King Bar. His ultimate, Chronosphere, locks time '
                'for everything within its area of effect, giving him time to strike down any enemies caught within '
                'with near impunity for several seconds. Faceless Void is a hard carry and, as such, scales heavily '
                'from items and reaches his full potential in late game, growing into one of the most powerful and '
                'destructive Heroes.',
         'strength': '23 + 1.6',
         'agility': '21 + 2.65',
         'intelligence': '15 + 1.5',
         'avatar': 'img/dota/heroes/faceless_void.png'
    },

    42: {'name': 'Skeleton King', 'avatar': 'img/dota/heroes/skeleton_king.png'},
    43: {'name': 'Death Prophet', 'avatar': 'img/dota/heroes/death_prophet.png'},
    44: {'name': 'Phantom Assassin', 'avatar': 'img/dota/heroes/phantom_assassin.png'},
    45: {'name': 'Pugna', 'avatar': 'img/dota/heroes/pugna.png'},
    46: {'name': 'Templar Assassin', 'avatar': 'img/dota/heroes/templar_assassin.png'},
    47: {'name': 'Viper', 'avatar': 'img/dota/heroes/viper.png'},
    48: {'name': 'Luna', 'avatar': 'img/dota/heroes/luna.png'},
    49: {'name': 'Dragon Knight', 'avatar': 'img/dota/heroes/dragon_knight.png'},
    50: {'name': 'Dazzle', 'avatar': 'img/dota/heroes/dazzle.png'},
    51: {'name': 'Clockwerk', 'avatar': 'img/dota/heroes/rattletrap.png'},
    52: {'name': 'Leshrac', 'avatar': 'img/dota/heroes/leshrac.png'},

    53: {'name': 'Nature\'s Prophet',
         'class': 'Intelligence',
         'role': 'Jungler, Pusher, Carry, Escape',
         'side': 'The Radiant',
         'bio': '<strong>Nature\'s Prophet</strong> is a ranged Intelligence hero, whose play style is removed '
                'from most Intelligence heroes, because he can be almost anywhere at any given time with his '
                'Teleportation. This ability allows him participate in most ganks and pushes at a moment\'s '
                'notice. With Sprout, he creates a ring of trees, trapping anyone within them in place, serving '
                'to disable anyone caught within them. The trees around him serve as his objects of power; using '
                'them, he summons sentient tree beings known as Treants from trees on the map with his Nature\'s '
                'Call ability. Wrath of Nature is his main and only directly damaging spell in his arsenal, '
                'but it can potentially be very powerful, as it can inflict increased damage with each bounce '
                'off subsequent enemies and can clear out multiple creep waves with its moderate cooldown and '
                'mana cost. Commonly played as a ganker, offlaner and jungler and known as a strong pusher, '
                'Nature\'s Prophet has superb farming capabilities and global presence, giving him the power '
                'to be anywhere on the map and aid his allies in need.',
         'strength': '19 + 1.8',
         'agility': '18 + 1.9',
         'intelligence': '21 + 2.9',
         'avatar': 'img/dota/heroes/furion.png'
    },

    54: {'name': 'Lifestealer',
         'role': 'Carry, Durable, Jungler, Escape',
         'side': 'The Dire',
         'class': 'Strength',
         'bio': '<strong>N\'aix</strong> the <strong>Lifestealer</strong> is a vicious melee Strength hero whose '
                'abilities give him the power to bring down durable heroes quickly, while sustaining his health '
                'from absorbing the very life of his enemies. The main role of the Lifestealer is to fulfill the '
                'job as a formidable carry, able to restore his life thanks to his skills. Feast is his passive '
                'ability and his signature, every attack he lands deals extra physical damage and consumes the flesh '
                'and blood of his victim, regenerating his health. With Feast, he can munch down tough and strong '
                'tanks. N\'aix can send himself into a bloody Rage, increasing his attack speed and a short period '
                'of magic immunity. Open Wounds tears the enemy, causing the prey\'s wounds to open, bleeding their '
                'life essence, allowing him and his allies to feast down as well as greatly slowing them to a crawl. '
                'Rage and Open Wounds allows the Lifestealer to brutally rip his victim apart, feasting on their '
                'health in the process. When in need, N\'aix can use Infest to hide himself inside of his allies '
                'or any non-hero units, laying dormant, until he is ready to come out, devouring the flesh from '
                'the inside, killing the non-hero unit, and bursting out the chunks of flesh and bones of his '
                'unfortunate host, damaging his foes around him, and ambushing them with carnivorous savagery. '
                'The Lifestealer is a monstrous beast of gluttony and greed, bent on stealing the lives of every '
                'living creature he encounters, violently killing them to sate the Lifestealer\'s terrifying thirst '
                'and hunger.',
         'strength': '25 + 2.4',
         'agility': '18 + 1.9',
         'intelligence': '15 + 1.75',
         'avatar': 'img/dota/heroes/life_stealer.png'
    },

    55: {'name': 'Dark Seer', 'avatar': 'img/dota/heroes/dark_seer.png'},
    56: {'name': 'Clinkz', 'avatar': 'img/dota/heroes/clinkz.png'},
    57: {'name': 'Omniknight', 'avatar': 'img/dota/heroes/omniknight.png'},
    58: {'name': 'Enchantress', 'avatar': 'img/dota/heroes/enchantress.png'},
    59: {'name': 'Huskar', 'avatar': 'img/dota/heroes/huskar.png'},
    60: {'name': 'Night Stalker', 'avatar': 'img/dota/heroes/night_stalker.png'},
    61: {'name': 'Broodmother', 'avatar': 'img/dota/heroes/broodmother.png'},

    62: {'name': 'Bounty Hunter',
         'role': 'Carry, Escape, Nuker',
         'side': 'The Radiant',
         'class': 'Agility',
         'bio': '<strong>Gondar</strong> the <strong>Bounty Hunter</strong> is a melee agility Hero that excels in '
                'dealing high amounts of damage to single targets. Bounty Hunter can easily gank other lanes, using '
                'his Shadow Walk to sneak up on enemies and get easy kills. Shadow Walk also allows him to escape '
                'from dangerous situations, making him very elusive. Bounty Hunter can be played as a carry, though '
                'it is not recommended, as Bounty Hunter is also extremely deadly as an offlaner. thanks to Track, '
                'which will grant True Sight, movement speed, and bonus gold, allowing him and his team to farm and '
                'earn powerful items faster than other carries and Jinada which amplifies the damage of his next '
                'attack every few seconds.',
         'strength': '17 + 1.8',
         'agility': '21 + 3',
         'intelligence': '19 + 1.4',
         'avatar': 'img/dota/heroes/bounty_hunter.png'
    },

    63: {'name': 'Weaver', 'avatar': 'img/dota/heroes/weaver.png'},
    64: {'name': 'Jakiro', 'avatar': 'img/dota/heroes/jakiro.png'},
    65: {'name': 'Batrider', 'avatar': 'img/dota/heroes/batrider.png'},
    66: {'name': 'Chen', 'avatar': 'img/dota/heroes/chen.png'},
    67: {'name': 'Spectre', 'avatar': 'img/dota/heroes/spectre.png'},
    68: {'name': 'Ancient Apparition', 'avatar': 'img/dota/heroes/ancient_apparition.png'},
    69: {'name': 'Doom Bringer', 'avatar': 'img/dota/heroes/doom_bringer.png'},
    70: {'name': 'Ursa', 'avatar': 'img/dota/heroes/ursa.png'},
    71: {'name': 'Spirit Breaker', 'avatar': 'img/dota/heroes/spirit_breaker.png'},
    72: {'name': 'Gyrocopter', 'avatar': 'img/dota/heroes/gyrocopter.png'},
    73: {'name': 'Alchemist', 'avatar': 'img/dota/heroes/alchemist.png'},
    74: {'name': 'Invoker', 'avatar': 'img/dota/heroes/invoker.png'},
    75: {'name': 'Silencer', 'avatar': 'img/dota/heroes/silencer.png'},
    76: {'name': 'Outworld Destroyer', 'avatar': 'img/dota/heroes/obsidian_destroyer.png'},
    77: {'name': 'Lycan', 'avatar': 'img/dota/heroes/lycan.png'},
    78: {'name': 'Brewmaster', 'avatar': 'img/dota/heroes/brewmaster.png'},
    79: {'name': 'Shadow Demon', 'avatar': 'img/dota/heroes/shadow_demon.png'},

    80: {'name': 'Lone Druid',
         'role': 'Carry, Durable, Pusher, Jungler',
         'side': 'The Radiant',
         'class': 'Agility',
         'bio': '<strong>Sylla</strong> the <strong>Lone Druid</strong> is an adaptable and versatile ranged or melee '
                'agility Hero, who summons a Spirit Bear, who has a set of skills and can equip items, as his ally. '
                'With the help of his Spirit Bear, he can carry, jungle, and push lanes effectively. Because of these, '
                'technically speaking, the Spirit Bear and Lone Druid himself, are two available heroes at once. '
                'The Spirit Bear is mostly played as the tank and aura giver, while the Lone Druid is played as the '
                'support and the main damage dealer as the Druid is still capable of causing more damage than the '
                'Spirit Bear. When he activates his abilities, it will not only buff him but the Spirit Bear as well. '
                'Lone Druid is versatile as he can change from a fast ranged warrior to a tough and mighty melee bear '
                'himself. Together, they can push the lanes effectively, farm Neutrals in a cinch, and can take down '
                'Roshan by themselves if equipped with the right items. Due to the Spirit Bear, Lone Druid can have '
                'up to 12 items making him extremely formidable as he scales into the late game.',
         'strength': '17 + 2.1',
         'agility': '24 + 2.7',
         'intelligence': '13 + 1.4',
         'avatar': 'img/dota/heroes/lone_druid.png'
    },

    81: {'name': 'Chaos Knight', 'avatar': 'img/dota/heroes/chaos_knight.png'},
    82: {'name': 'Meepo', 'avatar': 'img/dota/heroes/meepo.png'},
    83: {'name': 'Treant Protector', 'avatar': 'img/dota/heroes/treant.png'},
    84: {'name': 'Ogre Magi', 'avatar': 'img/dota/heroes/ogre_magi.png'},
    85: {'name': 'Undying', 'avatar': 'img/dota/heroes/undying.png'},
    86: {'name': 'Rubick', 'avatar': 'img/dota/heroes/rubick.png'},
    87: {'name': 'Disruptor', 'avatar': 'img/dota/heroes/disruptor.png'},

    88: {'name': 'Nyx Assassin',
         'bio': '<strong>Nyx Assassin</strong> is a melee Agility Hero who is a dedicated ganker until the end. '
                'Rather than focusing on enhancing his physical attacks like most Agility carry Heroes, Nyx Assassin '
                'specializes in killing lone and fragile victims with his high burst damage and various disables. '
                'Unfarmed carries, supports and many Intelligence spellcasting heroes with a low healthpool are easy '
                'prey for Nyx; he can open with a devastating backstab attack, followed by a painful stun and mana '
                'burn to deal even more damage and prevent retaliation. The Nyx Assassin also has a fantastic defense '
                'mechanism that not only blocks damage for a small amount of time, but reflects it back onto the '
                'enemy with a stun effect to boot. With his short cooldowns, the Nyx Assassin can continually '
                'dispatch key enemy targets, removing their ability and will to fight.',
         'role': 'Disabler, Nuker',
         'class': 'Agility',
         'side': 'The Dire',
         'strength': '18 + 2',
         'agility': '19 + 2.2',
         'intelligence': '18 + 2.1',
         'avatar': 'img/dota/heroes/nyx_assassin.png'
    },

    89: {'name': 'Naga Siren', 'avatar': 'img/dota/heroes/naga_siren.png'},
    90: {'name': 'Keeper of the Light', 'avatar': 'img/dota/heroes/keeper_of_the_light.png'},
    91: {'name': 'Io', 'avatar': 'img/dota/heroes/wisp.png'},
    92: {'name': 'Visage', 'avatar': 'img/dota/heroes/visage.png'},
    93: {'name': 'Slark', 'avatar': 'img/dota/heroes/slark.png'},
    94: {'name': 'Medusa', 'avatar': 'img/dota/heroes/medusa.png'},
    95: {'name': 'Troll Warlord', 'avatar': 'img/dota/heroes/troll_warlord.png'},
    96: {'name': 'Centaur Warrunner', 'avatar': 'img/dota/heroes/centaur.png'},
    97: {'name': 'Magnus', 'avatar': 'img/dota/heroes/magnataur.png'},
    98: {'name': 'Timbersaw', 'avatar': 'img/dota/heroes/shredder.png'},
    99: {'name': 'Bristleback', 'avatar': 'img/dota/heroes/bristleback.png'},
    100: {'name': 'Tusk', 'avatar': 'img/dota/heroes/tusk.png'},
    101: {'name': 'Skywrath Mage', 'avatar': 'img/dota/heroes/skywrath_mage.png'},
    102: {'name': 'Abaddon', 'avatar': 'img/dota/heroes/abaddon.png'},
    103: {'name': 'Elder Titan', 'avatar': 'img/dota/heroes/elder_titan.png'},
    104: {'name': 'Legion Commander', 'avatar': 'img/dota/heroes/legion_commander.png'},
    106: {'name': 'Ember Spirit', 'avatar': 'img/dota/heroes/ember_spirit.png'},
    107: {'name': 'Earth Spirit', 'avatar': 'img/dota/heroes/earth_spirit.png'}

}