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
         'quote': '',
         'strength': '',
         'agility': '',
         'intelligence': '',
         'ms': '',
         'tr':'',
         'sr':'',
         'ar':'',
         'miss_s':'',
         'ad':'',
         'cd':'',
         'bat':'',
         'avatar': ''}

}

"""

heroes_info = {

    1: {'name': 'Anti-Mage',
        'side': '',
        'avatar': 'img/dota/heroes/antimage.png'},

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
        'quote': 'Axe is all the reinforcement this army needs!',
        'strength': '25 + 2.5',
        'agility': '20 + 2.2',
        'intelligence': '18 + 1.6',
        'ms': '290',
        'tr':'0.6',
        'sr':'1800 / 800',
        'ar':'Melee',
        'miss_s':'Instant',
        'ad':'0.5 + 0.5',
        'cd':'0.3 + 0.51',
        'bat':'1.7',
        'avatar': 'img/dota/heroes/axe.png'
    },

    3: {'name': 'Ban',
        'side': '',
        'avatar': 'img/dota/heroes/bane.png'
    },

    4: {'name': 'Bloodseeker',
        'side': '',
        'avatar': 'img/dota/heroes/bloodseeker.png'
    },

    5: {'name': 'Crystal Maiden',
        'role': 'Support, Disabler, Nuker, Lane Support',
        'side': 'The Radiant',
        'class': 'Intelligence',
        'bio': '<strong>Rylai</strong> the <strong>Crystal Maiden</strong> is a ranged intelligence Hero used as a '
               'hard support and disabler. She is perhaps best known for her powerful global mana regeneration aura. '
               'This aura allows mana dependent allies to excel during the early to mid game and the laning phase, and '
               'allows her to constantly activate her own spells without needing to worry much about the mana costs. '
               'She also has a high amount of early game presence with just a few points in her Crystal Nova and '
               'Frostbite abilities. Crystal Nova is a powerful area-of-effect nuke that slows both attack and '
               'movement speeds of enemies within an area for several seconds, while Frostbite encases an enemy in a '
               'block of ice for several seconds, immobilizing it and doing moderate damage per second. Combining '
               'these two abilities together along with a laning partner\'s own spells often results in the quick '
               'death of an enemy hero. Although her strong early game presence is quickly lost due to her extreme '
               'frailty and poor mobility, she can still inflict a heavy amount of damage in teamfights later on if '
               'she is able to channel her deadly ultimate, Freezing Field. Her Arcane Aura, strong disabling and '
               'nuking prowess, relative ease of usage, and almost complete lack of item dependence makes her a '
               'reliable support caster that can be useful in any team.',
        'quote': 'When Hell freezes over, I\'ll start calling it Heaven.',
        'strength': '16 + 1.7',
        'agility': '16 + 1.6',
        'intelligence': '19 + 2.9',
        'ms': '280',
        'tr': '0.5',
        'sr': '1800 / 800',
        'ar': '600',
        'miss_s': '900',
        'ad': '0.55 + 0',
        'cd': '0.3 + 2.4',
        'bat': '1.7',
        'avatar': 'img/dota/heroes/crystal_maiden.png'
    },

    6: {'name': 'Drow Ranger',
        'side': '',
        'avatar': 'img/dota/heroes/drow_ranger.png'
    },

    7: {'name': 'Earthshaker',
        'role': 'Initiator, Disabler, Support, Lane Support',
        'side': 'The Radiant',
        'class': 'Strength',
        'bio': '<strong>Raigor Stonehoof</strong> the <strong>Earthshaker</strong> is a melee Strength Hero with '
               'several area of effect disables, commonly played as a ganker or initiator. Unlike most Strength '
               'heroes, he is played more like an Intelligence caster hero and is almost entirely reliant on his '
               'spells to inflict heavy damage. His Fissure is a versatile spell that affects enemies in a line, '
               'used to stun, inflict decent damage, and create an impassable wall of earth for a significant '
               'duration. Good usage of this can cut off chokepoints, leaving enemies with no escape routes or '
               'preventing them from chasing after endangered allies. Enchant Totem massively boosts his attack '
               'damage for one attack, and has a very short cooldown. Aftershock lets the Earthshaker deal '
               'additional damage and stun in a small area around him everytime he uses one of his spells, and '
               'combos particularly well with Enchant Totem. Earthshaker\'s heavy AoE-centric kit is most '
               'powerful when his enemies are in large numbers and in close proximity. With his Echo Slam, '
               'he can deal heavy damage to clusters of enemies. All of Earthshaker\'s spells (with the exception '
               'of his ultimate) have a long casting animation, but with proper positioning, an adept Earthshaker '
               'can wreak havoc with his area-of-effect spells. Blink Dagger is an essential item for Earthshaker '
               'to be able to properly land Echo Slam within a cluster of enemies. At the same time, because of the '
               'high mana costs of his spells, he needs some form of mana sustenance. With his tremendous seismic '
               'power, the Earthshaker is never one that should be taken lightly even when he is heavily outnumbered.',
        'strength': '22 + 2.5',
        'agility': '12 + 1.5',
        'intelligence': '16 + 1.8',
        'avatar': 'img/dota/heroes/earthshaker.png'
    },

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
        'quote': 'By the Visage of Vengeance, which drowned in the Isle of Masks, '
                 'I will carry on the rites of the Faceless Ones.',
        'class': 'Agility',
        'strength': '20 + 1.9',
        'agility': '20 + 2.85',
        'intelligence': '14 + 1.4',
        'ms': '305',
        'tr':'0.6',
        'sr':'1800 / 800',
        'ar':'Melee',
        'miss_s':'Instant',
        'ad':'0.33 + 0.84',
        'cd':'0.3 + 0.51',
        'bat':'1.6',
        'avatar': 'img/dota/heroes/juggernaut.png'
    },

    9: {'name': 'Mirana',
        'side': '',
        'avatar': 'img/dota/heroes/mirana.png'
    },

    10: {'name': 'Morphling',
         'side': '',
         'avatar': 'img/dota/heroes/morphling.png'
    },

    11: {'name': 'Shadow Fiend',
         'side': '',
         'avatar': 'img/dota/heroes/nevermore.png'
    },

    12: {'name': 'Phantom Lancer',
         'side': '',
         'avatar': 'img/dota/heroes/phantom_lancer.png'
    },

    13: {'name': 'Puck',
         'side': '',
         'avatar': 'img/dota/heroes/puck.png'
    },

    14: {'name': 'Pudge',
         'role': 'Durable, Disabler',
         'side': 'The Dire',
         'class': 'Strength',
         'bio': '<strong>Pudge</strong> the <strong>Butcher</strong> is a melee strength hero feared for his '
                'incredible gank prowess. Though he may not look like it, he is one of the strongest solo-killing '
                'gankers in the entire game, with one combo of his three active abilities proving more than sufficient '
                'to kill fragile enemy heroes in the early and midgame. His signature ability, Meat Hook, which '
                'requires intuition, guesswork, and good timing to land, is thrown out in a straight line a long '
                'distance away. If it snags a unit, it will drag it back to Pudge, dealing enormous damage to it if '
                'it was an enemy. It thus serves as a powerful ganking and initation tool, and also has the utility '
                'of being able to save an endangered ally. He can then follow up with his ultimate, Dismember, which '
                'deals further damage to the target over a few seconds, as well as disabling it. During this period, '
                'he can toggle on his Rot to damage his enemy further while hurting himself as well, and use it to '
                'slow and finish off the hero if he or she survived the initial assault. To supplement his killing '
                'power is Flesh Heap, which provides him some magic resistance to reduce the damage he takes from Rot '
                'as well as from other enemy spells. The scariest aspect of Flesh Heap though is that it provides him '
                'permanent Strength with every kill that he participates in, giving him the potential to permanently '
                'increase his vitality (and physical damage) to monolithic proportions, thereby becoming a formidable '
                'tank. In the hands of a skilled player who can land his deadly Meat Hook with high accuracy, Pudge '
                'is both one of the most rewarding and fun heroes to play and one of the most fearsome opponents to '
                'be up against.',
         'quote': 'When I\'m through with these vermin, they\'ll be fit for a pie.',
         'strength': '25 + 3.2',
         'agility': '14 + 1.5',
         'intelligence': '14 + 1.5',
         'ms': '285',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 1.17',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/pudge.png'
    },

    15: {'name': 'Razor',
         'side': '',
         'avatar': 'img/dota/heroes/razor.png'
    },

    16: {'name': 'Sand King',
         'side': '',
         'avatar': 'img/dota/heroes/sand_king.png'
    },

    17: {'name': 'Storm Spirit',
         'side': '',
         'avatar': 'img/dota/heroes/storm_spirit.png'
    },

    18: {'name': 'Sven',
         'role': 'Disabler, Initiator, Carry, Support',
         'side': 'The Radiant',
         'class': 'Strength',
         'bio': '<strong>Sven</strong> the <strong>Rogue Knight</strong> is a versatile melee strength Hero with '
                'superior physical power yet is coupled with various abilities that provide various utility. He can '
                'fulfill various roles, but is often played as a support or a semi-carry due to his high utility even '
                'without items. He possess a versatile arsenal, from shouts that grant armor both for escaping and '
                'pushing to throwable gauntlets that disorient enemies around the target unit. With enough items, '
                'Sven has the potential to be a strong late-game carry due to his ultimate which increases his damage '
                'and his passive which allows him to hit multiple targets at once. He is a formidable foe and his '
                'versatility makes the Rogue Knight a great asset to any team.',
         'quote': 'May my enemies share the fate of the Shattered Helm.',
         'strength': '23 + 2.7',
         'agility': '21 + 2',
         'intelligence': '14 + 1.3',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.4 + 0.3',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/sven.png'
    },

    19: {'name': 'Tiny',
         'role': 'Disabler, Nuker, Initiator, Durable',
         'class': 'Strength',
         'side': 'The Radiant',
         'bio': '<strong>Tiny</strong> the <strong>Stone Giant</strong> is a melee Strength hero with powerful ganking '
                'and killing '
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
         'quote': 'My enemies break upon me like surf upon the stone.',
         'strength': '24 + 3.0',
         'agility': '9 + 0.9',
         'intelligence': '14 + 1.6',
         'ms': '285',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.49 + 1',
         'cd': '0.001 + 0',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/tiny.png'
    },

    20: {'name': 'Vengeful Spirit',
         'side': '',
         'avatar': 'img/dota/heroes/vengefulspirit.png'
    },

    21: {'name': 'Windranger',
         'role': 'Disabler, Nuker, Support, Escape',
         'side': 'The Radiant',
         'class': 'Intelligence',
         'bio': '<strong>Lyralei</strong> the <strong>Windranger</strong> is a ranged intelligence hero that uses '
                'powerful abilities in conjunction with her physical attack to take down enemies. Despite being an '
                'intelligence Hero, Windranger\'s playstyle resembles that of an agility Hero, due in large part to '
                'her skillset. Windranger is most often played as an offlane solo due to her escape, long range '
                'harass, and farm capability; however, she is quite versatile and can be fielded as a midlaner, '
                'roamer, lane support, or even a carry, if the game calls for it. She is famous for her immense '
                'utility and versatility, and as such, she is one of the most common picks of experienced players.',
         'quote': 'If at first you don\'t succeed, stand closer, shoot again.',
         'strength': '15 + 2.5',
         'agility': '17 + 1.4',
         'intelligence': '22 + 2.6',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1250',
         'ad': '0.4 + 0.3',
         'cd': '0.3 + 0.5',
         'bat': '1.5',
         'avatar': 'img/dota/heroes/windrunner.png'
    },

    22: {'name': 'Zeus',
         'side': '',
         'avatar': 'img/dota/heroes/zuus.png'
    },

    23: {'name': 'Kunkka',
         'side': '',
         'avatar': 'img/dota/heroes/kunkka.png'
    },

    25: {'name': 'Lina',
         'side': '',
         'avatar': 'img/dota/heroes/lina.png'
    },

    26: {'name': 'Lion',
         'side': '',
         'avatar': 'img/dota/heroes/lion.png'
    },

    27: {'name': 'Shadow Shaman',
         'side': '',
         'avatar': 'img/dota/heroes/shadow_shaman.png'
    },

    28: {'name': 'Slardar',
         'side': '',
         'avatar': 'img/dota/heroes/slardar.png'
    },

    29: {'name': 'Tidehunter',
         'side': '',
         'avatar': 'img/dota/heroes/tidehunter.png'
    },

    30: {'name': 'Witch Doctor',
         'side': '',
         'avatar': 'img/dota/heroes/witch_doctor.png'
    },

    31: {'name': 'Lich',
         'side': '',
         'avatar': 'img/dota/heroes/lich.png'
    },

    32: {'name': 'Riki',
         'role': 'Carry, Escape',
         'side': 'The Radiant',
         'class': 'Agility',
         'bio': '<strong>Riki</strong> the <strong>Stealth Assassin</strong> is a melee agility hero that uses stealth '
                'in order to surprise enemies and quickly kill them. His trademark ability, Permanent Invisibility, '
                'allows him to sneak into the shadows to hide and slip by without giving himself away. This allows '
                'him to close in on the enemy and drop his devastating Smoke Screen, which cripples fighter and '
                'spellcaster alike. Blink Strike allows Riki to chase with impunity, and Backstab makes running '
                'from him even more dangerous.',
         'strength': '17 + 2',
         'agility': '34 + 2.9',
         'intelligence': '14 + 1.3',
         'avatar': 'img/dota/heroes/riki.png'
    },

    33: {'name': 'Enigma',
         'side': '',
         'avatar': 'img/dota/heroes/enigma.png'
    },

    34: {'name': 'Tinker',
         'side': '',
         'avatar': 'img/dota/heroes/tinker.png'
    },

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
         'quote': 'Killing is the last resort, true. But the other resorts don\'t even have a pool.',
         'strength': '16 + 1.7',
         'agility': '21 + 2.9',
         'intelligence': '15 + 2.6',
         'ms': '290',
         'tr': '0.6',
         'sr': '1800 / 1000',
         'ar': '550',
         'miss_s': '3000',
         'ad': '0.17 + 0.7',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/sniper.png'
    },

    36: {'name': 'Necrophos',
         'side': '',
         'avatar': 'img/dota/heroes/necrolyte.png'
    },

    37: {'name': 'Warlock',
         'side': '',
         'avatar': 'img/dota/heroes/warlock.png'
    },


    38: {'name': 'Beastmaster',
         'side': '',
         'avatar': 'img/dota/heroes/beastmaster.png'
    },

    39: {'name': 'Queen of Pain',
         'side': '',
         'avatar': 'img/dota/heroes/queenofpain.png'
    },

    40: {'name': 'Venomancer',
         'side': '',
         'avatar': 'img/dota/heroes/venomancer.png'
    },


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
         'quote': 'From a place beyond time, and time beyond counting.',
         'strength': '23 + 1.6',
         'agility': '21 + 2.65',
         'intelligence': '15 + 1.5',
         'ms': '300',
         'tr':'0.5',
         'sr':'1800 / 800',
         'ar':'Melee',
         'miss_s':'Instant',
         'ad':'0.5 + 0.56',
         'cd':'0.35 + 0.51',
         'bat':'1.7',
         'avatar': 'img/dota/heroes/faceless_void.png'
    },

    42: {'name': 'Skeleton King',
         'side': '',
         'avatar': 'img/dota/heroes/skeleton_king.png'
    },

    43: {'name': 'Death Prophet',
         'side': '',
         'avatar': 'img/dota/heroes/death_prophet.png'
    },

    44: {'name': 'Phantom Assassin',
         'role': 'Carry, Escape',
         'side': 'The Dire',
         'class': 'Agility',
         'bio': '<strong>Mortred</strong> the <strong>Phantom Assassin</strong> is a melee agility Hero fitting the '
                'role of hard carry. Mortred is best-known, and infamous for, her ability to inflict staggering '
                'damage with single strikes. Her abilities synergise supremely well with each other, rendering her '
                'an extremely formidable foe once she has acquired the items she requires. She is a very '
                'farm-dependent melee Hero, but she farms creeps with much more ease than many of her fellow '
                'carries, using her Stifling Dagger for last hitting. Besides eliminating the weakness most melee '
                'Heroes have in their farming, it also saves her from expending gold on important melee carry '
                'items like Quelling Blade. Her second ability, Phantom Strike, acts as both her escape and '
                'initiate, while Blur gives her an edge against other Heroes that depend on their physical attacks '
                'by evading them; giving her partial damage immunity to many carries. Her ultimate, the strongest '
                'critical strike in the game, is what connects Mortred with four-digit damage and what gives her a '
                'place amongst the very best support killers in the late game, since they usually fall instantly '
                'from the divine strike her ultimate provides.',
         'strength': '20 + 1.85',
         'agility': '23 + 3.15',
         'intelligence': '13 + 1',
         'avatar': 'img/dota/heroes/phantom_assassin.png'
    },

    45: {'name': 'Pugna', 'avatar': 'img/dota/heroes/pugna.png'},
    46: {'name': 'Templar Assassin', 'avatar': 'img/dota/heroes/templar_assassin.png'},
    47: {'name': 'Viper', 'avatar': 'img/dota/heroes/viper.png'},
    48: {'name': 'Luna', 'avatar': 'img/dota/heroes/luna.png'},
    49: {'name': 'Dragon Knight', 'avatar': 'img/dota/heroes/dragon_knight.png'},

    50: {'name': 'Dazzle',
         'role': 'Support, Lane Support',
         'side': 'The Dire',
         'class': 'Intelligence',
         'bio': '<strong>Dazzle</strong> the <strong>Shadow Priest</strong> is a ranged intelligence Hero exhibiting '
                'abilities that bend the sustainability of both his allies and enemies, making him a viable support. '
                'While frail, he is capable of keeping his allies and himself from dying, causing his foes to waste '
                'time in a fruitless endeavor. Similarly to Slardar, Dazzle boasts abilities that deal physical '
                'damage instead of the usual magical. His first ability, Poison Touch, is a strong spammable '
                'disable, though mediocre in effects in the first levels. Out of all his abilities, Poison Touch '
                'is the only one that cannot pass through Magic immunity, will it sustain itself when magic immunity '
                'is granted after the buff is placed. Shallow Grave is a solid survivability spell, allowing your '
                'allied targets to escape during serious encounters. Though it only prevents fatal damage, it cannot '
                'be purged, making it a full guarantee that Dazzle\'s target will survive for the duration. Shadow '
                'Wave is a chaining healing ability that dissipates the health gained to damage nearby enemies, '
                'having a potential of delivering a huge damage output when good positioning comes to play. His '
                'ultimate, Weave, is a large armor bending ability that not only increases his allies\' armor, but '
                'also decreases his enemies. With the fact that his abilities deal physical damage and that Dazzle '
                'himself has large attack damage, the chaotic combination with armor reduction really makes '
                'Dazzle a devastating Hero to go against.',
         'quote': 'Where my shadow falls, there falls my foe.',
         'strength': '16 + 1.85',
         'agility': '21 + 1.7',
         'intelligence': '27 + 3.4',
         'ms': '305',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '500',
         'miss_s': '1200',
         'ad': '0.3 + 0.3',
         'cd': '0.3 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/dazzle.png'
    },

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
         'quote': 'I woke within the seed and saw my destiny, and many were its branches.',
         'strength': '19 + 1.8',
         'agility': '18 + 1.9',
         'intelligence': '21 + 2.9',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1125',
         'ad': '0.4 + 0.77',
         'cd': '0.5 + 1.17',
         'bat': '1.7',
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
         'quote': 'Oh Master, behold all these lives for the taking!',
         'strength': '25 + 2.4',
         'agility': '18 + 1.9',
         'intelligence': '15 + 1.75',
         'ms': '315',
         'tr': '1.0',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.39 + 0.44',
         'cd': '0.2 + 0.01',
         'bat': '1.7',
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

    74: {'name': 'Invoker',
         'role': 'Carry, Nuker, Initiator, Escape',
         'side': 'The Dire',
         'class': 'Intelligence',
         'bio': '<strong>Invoker</strong> is a ranged intelligence Hero who is considered one of the most difficult '
                'hero in the game to master. He is unique in that he possesses a total of 14 abilities in his arsenal; '
                'three of them - Quas, Wex, and Exort - are reagents and one is his special ultimate Invoke. The three '
                'abilities he learns throughout leveling up can have three instances, which serve as the basic '
                'ingredients or components for him to create a new ability using his ultimate. Once the reagents or '
                'elements are combined, he can invoke one out of ten different abilities. All of his invoked abilities '
                'are capable of a multitude of actions, from damaging enemies to aiding his allies, and even saving '
                'himself from danger. His three reagents can be upgraded up to level 7 which determines the power and '
                'potency of his invoked abilities, making it more powerful than an ordinary spell. Because of this, he '
                'can be played in almost any role possible. Invoker can be a carry, semi-carry, ganker, pusher, '
                'initiator or even support. He is also the only hero who doesn\'t have Attribute Bonuses, thus he has '
                'average attributes. However, his three reagents provide passive attributes with each level, and each '
                'instance of his reagents provides a passive bonus, allowing for specialization at early levels and '
                'situational boosts at later levels. His extremely flexible nature allows him to use many different '
                'combinations of items effectively but also make him dependent on solid builds and a good '
                'gold advantage.',
         'quote': 'What joy it is beholding me!',
         'strength': '19 + 1.7',
         'agility': '20 + 1.9',
         'intelligence': '22 + 2.5',
         'ms': '280',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '900',
         'ad': '0.4 + 0.7',
         'cd': '0 + 0',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/invoker.png'
    },

    75: {'name': 'Silencer', 'avatar': 'img/dota/heroes/silencer.png'},

    76: {'name': 'Outworld Devourer',
         'role': 'Carry',
         'side': 'The Dire',
         'class': 'Intelligence',
         'bio': '<strong>Harbinger</strong> the <strong>Outworld Devourer</strong> is a ranged intelligence hero who '
                'qualifies as a carry, though several weaknesses - primarily his inability to combat magic-immune '
                'targets - restrict him from true hard carry status. His damage output is entirely reliant on his '
                'intelligence attribute and the size of his mana pool, so he must focus more or less exclusively on '
                'items which augment them. Though extremely fragile (rendered even more so by his inability to build '
                'many significant durability items), he deals Pure damage which increases with his mana pool, meaning '
                'that if he gains an advantage in a match he deals constant, colossal damage which (because it is Pure '
                'damage) cannot be decreased or resisted except with total magic immunity. He and his allies enjoy '
                'more-or-less unlimited mana because of his Essence Aura, which gives them a chance to replenish a '
                'quarter of their mana upon casting a spell. With Astral Imprisonment, Harbinger can render himself '
                'or an ally invulnerable for a short period of time, or disable (and steal Intelligence from) the '
                'target enemy. His ultimate, Sanity\'s Eclipse, can instantly deal colossal area-of-effect damage '
                'against his enemies when his intelligence is higher than theirs.',
         'quote': 'Their sanity I\'ll shatter; their dreams of conquest I\'ll destroy.',
         'strength': '19 + 1.85',
         'agility': '24 + 2',
         'intelligence': '26 + 3.3',
         'ms': '315',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '450',
         'miss_s': '900',
         'ad': '0.46 + 0.54',
         'cd': '0.25 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/obsidian_destroyer.png'
    },

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
         'quote': 'The blessing of Nyx gives me all the purpose I require.',
         'role': 'Disabler, Nuker',
         'class': 'Agility',
         'side': 'The Dire',
         'strength': '18 + 2',
         'agility': '19 + 2.2',
         'intelligence': '18 + 2.1',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.46 + 0.54',
         'cd': '0.4 + 1.1',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/nyx_assassin.png'
    },

    89: {'name': 'Naga Siren', 'avatar': 'img/dota/heroes/naga_siren.png'},
    90: {'name': 'Keeper of the Light', 'avatar': 'img/dota/heroes/keeper_of_the_light.png'},
    91: {'name': 'Io', 'avatar': 'img/dota/heroes/wisp.png'},
    92: {'name': 'Visage', 'avatar': 'img/dota/heroes/visage.png'},

    93: {'name': 'Slark',
         'role': 'Escape',
         'side': 'The Dire',
         'class': 'Agility',
         'bio': '<strong>Slark</strong> the <strong>Nightcrawler</strong> is a melee agility hero that utilises his '
                'skills to spring onto enemy heroes and slip out unhindered. He is a very mobile ganker, but remains '
                'statwise below most other carries unless he is able to steal away stats with his abilities. Once he '
                'does, though, only a few heroes can hope to be as fearsome as the Nightcrawler - extremely mobile to '
                'the point of ever-presence; his strikes only hitting harder and faster. Slark can quickly leap forward '
                'onto enemies with Pounce to leash them and bind them from escaping. His Dark Pact releases a delayed '
                'purge that breaks even the most powerful disables. This gives him one of the most flexible abilities '
                'to start and end fights in the game. He is also capable of stealing stats on auto-attacks to boost '
                'his own damage temporarily with Essence Shift which can rapidly shift engagements in his favor, even '
                'when merely performing hit-and-run maneuvers. Slark\'s ultimate, Shadow Dance, allows him to remain '
                'unseen even while attacking for a short duration and allows him to move quicker when not under the '
                'watch of enemy eyes to strike in and out of enemy ranks unhindered.',
         'quote': 'If I\'d known I\'d end up here, I\'d have stayed in Dark Reef Prison.',
         'strength': '21 + 1.8',
         'agility': '21 + 1.5',
         'intelligence': '16 + 1.9',
         'ms': '305',
         'tr': '0.5',
         'sr': '1800 / 1800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 0.3',
         'cd': '0.001 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/slark.png'
    },

    94: {'name': 'Medusa', 'avatar': 'img/dota/heroes/medusa.png'},
    95: {'name': 'Troll Warlord', 'avatar': 'img/dota/heroes/troll_warlord.png'},
    96: {'name': 'Centaur Warrunner', 'avatar': 'img/dota/heroes/centaur.png'},
    97: {'name': 'Magnus', 'avatar': 'img/dota/heroes/magnataur.png'},
    98: {'name': 'Timbersaw', 'avatar': 'img/dota/heroes/shredder.png'},
    99: {'name': 'Bristleback', 'avatar': 'img/dota/heroes/bristleback.png'},

    100: {'name': 'Tusk',
          'role': 'Initiator, Durable',
          'side': 'The Radiant',
          'class': 'Strength',
          'bio': '<strong>Ymir</strong> the <strong>Tusk</strong> is a melee Strength hero whose array of icy spells '
                 'pack great potential to grant the advantage in a gank. Tusk is both an effective team fight hero '
                 'and initiator, who has the unique ability to bring along teammates into the fight. Though he is '
                 'usually played as a support, one can in fact benefit reasonably well from additional attributes '
                 'and farm, and can be a great semi-carry as well. Equipping damage-boosting items can greatly '
                 'increase the critical damage brought by Walrus PUNCH!, allowing him to fight on his own in the '
                 'later stages.',
          'quote': 'After a bar brawl it\'s customary, as a courtesy, '
                   'to buy everyone who\'s still standing a round of drinks.',
          'strength': '23 + 2.3',
          'agility': '23 + 2.1',
          'intelligence': '18 + 1.7',
          'ms': '305',
          'tr': '0.5',
          'sr': '1800 / 800',
          'ar': 'Melee',
          'miss_s': 'Instant',
          'ad': '0.36 + 0.64',
          'cd': '0.1 + 1',
          'bat': '1.7',
          'avatar': 'img/dota/heroes/tusk.png'
    },

    101: {'name': 'Skywrath Mage',
          'role': 'Nuker, Support',
          'side': 'The Radiant',
          'class': 'Intelligence ',
          'bio': '<strong>Dragonus</strong> the <strong>Skywrath Mage</strong> is a ranged Intelligence hero equipped '
                 'with tremendously powerful nukes, able to enhance magical damage and thus scales well into late '
                 'game. However, he is a proverbial glass cannon; while he can bring superb amounts of damage, he is '
                 'dangerously vulnerable and will most likely meet a swift end if the player isn\'t careful. Arcane '
                 'Bolt is his main spell; its damage is based on his current Intelligence level. Concussive Shot '
                 'blasts the nearest enemy hero, along with nearby units around the foe, slowing them down. The '
                 'Ancient Seal marks the target with magic amplification and silence, leaving the target vulnerable '
                 'to magic and unable to cast spells. Skywrath Mage\'s ultimate Mystic Flare is one of the most '
                 'dangerous nukes in the game. Its power is split equally among enemy heroes within its radius. '
                 'Enemy heroes caught in this field will suffer damage; if it is used on a single hero, it will '
                 'deal its full damage potential. His spells are most effective when targeted on a lone hero and '
                 'thus suffer decreased effectiveness when used on groups.',
          'strength': '19 + 1.5',
          'agility': '18 + 0.8',
          'intelligence': '27 + 3.6',
          'avatar': 'img/dota/heroes/skywrath_mage.png'
    },

    102: {'name': 'Abaddon',
          'role': 'Durable',
          'side': 'The Dire',
          'class': 'Strength',
          'bio': '<strong>Abaddon</strong> the <strong>Lord of Avernus</strong> is a melee strength Hero known as '
                 'one of the most versatile characters in Dota due to his rather low mana dependence, short spell '
                 'cooldowns and a large number of viable item choices. His ability to help sustain his allies and '
                 'himself plus his strong tower diving capacity give him solid lane presence. Many of his abilities '
                 'offer a large sum of utility, which makes him a strong support Hero. Mist Coil serves as both a '
                 'single target nuke and heal that helps shift the sustainability of both allied and enemy heroes '
                 'in a lane at his will, though sacrificing a portion of his own health. Aphotic Shield holds as '
                 'one of the most useful abilities in the game, able to shield a target from some damage while also '
                 'able to reflect said damage to a huge area. The most important aspect is how it is able to dispel '
                 'many status effects such as slows and stuns. His other abilities allow him to become a mix between '
                 'a semi-carry and tank. Abaddon\'s passive, Curse of Avernus, allows his attacks to not only slow '
                 'down his enemy, but also increase the attack and movement speed of any ally attacking the same '
                 'target. With his ultimate, Borrowed Time, Abaddon is able to shift all non-HP removal damage he '
                 'receives into health. When not on cooldown, Borrowed Time may activate passively when his health '
                 'falls under a certain threshold, even under the most dire situations. Due to his powerful spells '
                 'and versatility, Abaddon is an excellent addition to any team.',
          'strength': '23 + 2.7',
          'agility': '17 + 1.5',
          'intelligence': '21 + 2',
          'avatar': 'img/dota/heroes/abaddon.png'
    },

    103: {'name': 'Elder Titan',
          'role': 'Initiator, Durable',
          'side': 'The Radiant',
          'class': 'Strength',
          'bio': 'The <strong>Elder Titan</strong> is a durable melee strength hero who plays the role of initiator. '
                 'His Astral Spirit and Echo Stomp abilities allow him to disable large groups of enemies from afar, '
                 'making him one of the few initiators that does not require a Blink Dagger. This combination creates '
                 'a perfect setup for his powerful ultimate Earth Splitter, which damages enemies based on their '
                 'maximum HP. This, along with his ability to lower his enemies physical and magical resistance, '
                 'makes Elder Titan scale well through his abilities and be effective at all stages of the game. '
                 'As the progenitor of this world, Elder Titan reshapes the battlefield on a whim and can turn any '
                 'teamfight in his favor.',
          'strength': '24 + 2.3',
          'agility': '14 + 1.5',
          'intelligence': '23 + 1.6',
          'avatar': 'img/dota/heroes/elder_titan.png'},

    104: {'name': 'Legion Commander',
          'role': '',
          'side': '',
          'class': '',
          'bio': '',
          'strength': '',
          'agility': '',
          'intelligence': '',
          'avatar': 'img/dota/heroes/legion_commander.png'
    },

    106: {'name': 'Ember Spirit',
          'role': 'Carry, Nuker, Disabler, Durable',
          'side': 'The Radiant',
          'class': 'Agility',
          'bio': '<strong>Xin</strong>, the <strong>Ember Spirit</strong> is a highly mobile melee Agility carry, '
                 'whose abilities enable him to also play as an initiator or ganker. His skillset allows for '
                 'incredibly aggressive assaults on other heroes, dealing extraordinary amounts of damage in a '
                 'relatively small window of time, and then escaping to safety. Despite a good HP pool early on, '
                 'he lacks armor and a sizable mana pool, and as such may be unable to escape quickly enough if '
                 'caught out of position. However, with good item choices and proper judgement, Ember Spirit can '
                 'quickly snowball out of control, dominating the battlefield with blinding speed as he cheats '
                 'death. While he has only a limited presence in the early and mid game, in time Xin becomes a '
                 'dangerous opponent even on his own, proving to friend and foe alike that for them, there is '
                 'still much to be learnt.',
          'quote': 'Xin\'s teachings shall endure.',
          'strength': '19 + 2.0',
          'agility': '22 + 1.8',
          'intelligence': '20 + 1.8',
          'ms': '310',
          'tr':'0.6',
          'sr':'1800 / 800',
          'ar':'Melee',
          'miss_s':'Instant',
          'ad':'0.4 + 0.3',
          'cd':'0.00 + 0.51',
          'bat':'1.7',
          'avatar': 'img/dota/heroes/ember_spirit.png'
    },

    107: {'name': 'Earth Spirit',
          'role': 'Initiator',
          'side': 'The Radiant',
          'class': 'Strength',
          'bio': '<strong>Kaolin</strong>, the <strong>Earth Spirit</strong>',
          'strength': '21 + 2.9',
          'agility': '17 + 1.5',
          'intelligence': '18 + 2.4',
          'avatar': 'img/dota/heroes/earth_spirit.png'
    }

}