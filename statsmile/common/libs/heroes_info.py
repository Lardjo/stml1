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
        'role': 'Carry',
        'side': 'The Radiant',
        'class': 'Agility',
        'bio': '<p><strong>Traxex</strong> the <strong>Drow Ranger</strong> is a ranged agility hero whose greatest '
               'assets are her incredible damage and ability to keep threats at bay. Traxex is a carry who, though '
               'lacking survivability, provides a worthwhile contribution through her damage alone. The Drow Ranger '
               'can be extremely powerful at any given point in the game.</p><p>As an agility hero, Traxex\'s damage '
               'is based largely off her auto attacks and is among the greatest largely due to the massive amounts of '
               'agility she gains from her passive ultimate, Marksmanship. The Drow Ranger also adds ranged damage to '
               'teammates with her global Precision Aura. Despite her lack of escape spells, Drow Ranger can keep '
               'herself relatively safe from enemy spellcasters and melee heroes using her Silence and her Frost '
               'Arrows, respectively. Frost Arrows infuses her attacks with ice cold, greatly slowing down her '
               'enemies. Since it can be manually cast, Frost Arrows can be used to harass her foes in the early game '
               'without drawing the creeps\' attention. Silence is a great counter to enemy spellcasters who might '
               'threaten her life in battles. Position is of utmost importance as Traxex is quite vulnerable in close '
               'combat and the agility bonus from Marksmanship is removed when enemies come near her. This means she '
               'struggles against melee dps heroes with high mobility, such as Anti-Mage and Faceless Void.</p>',
        'quote': 'I walk alone, but the shadows are company enough.',
        'strength': '17 + 1.9',
        'agility': '26 + 1.9',
        'intelligence': '15 + 1.4',
        'ms': '300',
        'tr': '0.6',
        'sr': '1800 / 800',
        'ar': '625',
        'miss_s': '1250',
        'ad': '0.7 + 0.3',
        'cd': '0.4 + 0.5',
        'bat': '1.7',
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
        'quote': 'There may be many earths, but there\'s only one Earthshaker.',
        'strength': '22 + 2.5',
        'agility': '12 + 1.5',
        'intelligence': '16 + 1.8',
        'ms': '300',
        'tr': '0.6',
        'sr': '1800 / 800',
        'ar': 'Melee',
        'miss_s': 'Instant',
        'ad': '0.467 + 0.863',
        'cd': '0.69 + 0.5',
        'bat': '1.7',
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
        'role': 'Carry, Nuker, Disabler, Escape',
        'side': 'The Radiant',
        'class': 'Agility',
        'bio': '<strong>Mirana</strong> the <strong>Princess of the Moon</strong>, is a ranged Agility Hero that uses '
               'her abilities to surprise, chase, and assault enemies. She is an excellent huntress and widely known '
               'for her Sacred Arrow which stuns her victim with deadly precision. The arrow stuns longer when its '
               'fired from a farther distance. Mirana can bring down the stars with Starstorm to damage nearby enemies '
               'and an additional star to cast down on her one unfortunate target. Mounting with her trusted tiger '
               'Sagan, Mirana can Leap forward over a distance, to escape or chase, and enhancing her allies with a '
               'roar, increasing their attack and movement speed. Invoking the power of her moon goddess, Mirana uses '
               'her ultimate, Moonlight Shadow to cloak all allied heroes and herself with invisibility. At any time, '
               'Mirana and her allies can break out of their hiding with an ambush and fade into the shadows again '
               'during the duration of the spell. With an array of mighty and supportive skills, Mirana is a versatile '
               'heroine that can excel early in the game as a mobile ganker. She is not much heavily reliant on '
               'luxurious items but she can benefit from almost any item that gives her presence in the battlefield.',
        'quote': ' How long must we ride before we\'re summoned again to the Nightsilver Woods?',
        'strength': '17 + 1.85',
        'agility': '20 + 2.75',
        'intelligence': '17 + 1.65',
        'ms': '300',
        'tr': '0.4',
        'sr': '1800 / 800',
        'ar': '600',
        'miss_s': '900',
        'ad': '0.3 + 0.7',
        'cd': '0.5 + 0.83',
        'bat': '1.7',
        'avatar': 'img/dota/heroes/mirana.png'
    },

    10: {'name': 'Morphling',
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
         'avatar': 'img/dota/heroes/morphling.png'
    },

    11: {'name': 'Shadow Fiend',
         'role': 'Carry, Nuker',
         'side': 'The Dire',
         'class': 'Agility',
         'bio': '<strong>Nevermore</strong> the <strong>Shadow Fiend</strong> is a ranged agility Hero possessing '
                'abilities that inflict superb burst damage from varying distances. Whether near or far, Shadow Fiend '
                'is able to release incredible offensive power, both physical and magical. Shadow Fiend\'s true power '
                'comes from the souls he takes, thus, he is more dangerous every time he kills. With enough souls, he '
                'can release all of the captured souls in a devastating burst, dealing more damage to enemies that '
                'are closer to him. Shadow Fiend is a carry who is powerful at all stages of the game, a trait most '
                'carries don\'t share. He can harass and conquer early game, set out and kill unsuspecting Heroes '
                'during the mid stages, and unleash more power and dominate other Heroes late game.',
         'quote': 'So, you\'re curious where I come from? There\'s one easy way to find out for yourself.',
         'strength': '15 + 2',
         'agility': '20 + 2.9',
         'intelligence': '18 + 2',
         'ms': '305',
         'tr': '1.0',
         'sr': '1800 / 800',
         'ar': '500',
         'miss_s': '1200',
         'ad': '0.5 + 0.54',
         'cd': '0.67 + 0.4',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/nevermore.png'
    },

    12: {'name': 'Phantom Lancer',
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
         'avatar': 'img/dota/heroes/phantom_lancer.png'
    },

    13: {'name': 'Puck',
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
         'avatar': 'img/dota/heroes/razor.png'
    },

    16: {'name': 'Sand King',
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
         'avatar': 'img/dota/heroes/sand_king.png'
    },

    17: {'name': 'Storm Spirit',
         'role': 'Carry, Initiator, Escape, Disabler',
         'side': 'The Radiant',
         'class': 'Intelligence',
         'bio': '<p><strong>Raijin Thunderkeg</strong>, the <strong>Storm Spirit</strong>, is a ranged Intelligence '
                'hero who wields the elemental power of lightning. He has high mobility, strong ganking and carrying '
                'potential, and very good synergy between his hero abilities.</p><p>Static Remnant creates an immobile '
                'clone of himself that, upon contact with an enemy, shocks all enemies in a small area for damage. It '
                'has a very low cooldown, making it a good farming skill. Electric Vortex binds an enemy to himself, '
                'drawing it in slowly; at higher levels of the skill, it will always be able to pull the target into '
                'a Static Remnant. Overload further supplements this combo by harnessing the excess charge whenever '
                'Raijin casts a spell, adding it in the form of magical damage to his next attack and zapping enemies '
                'in a radius around the target. Finally, Storm Spirit\'s ultimate and signature skill is Ball '
                'Lightning, in which he transforms into pure energy, sacrificing his own mana to dash quickly around '
                'the map in an invulnerable state, inflicting minor damage to foes he impacts as well as giving him '
                'an Overload charge. It can be used to initiate and escape long distances with ease.</p>',
         'quote': 'Everyone complains about the weather...well, I\'m doing something about it!',
         'strength': '19 + 1.5',
         'agility': '22 + 1.8',
         'intelligence': '23 + 2.6',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '480',
         'miss_s': '1100',
         'ad': '0.5 + 0.3',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
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
         'role': 'Nuker, Support',
         'side': 'The Radiant',
         'class': 'Intelligence',
         'bio': '<strong>Zeus</strong> the <strong>Lord of Heaven</strong> is a ranged intelligence Hero who functions '
                'almost solely as a nuker. He is usually played as a semi-carry ganker type hero, who instead of '
                'utilizing disables, focuses solely on delivering tremendous amounts of magical damage to his foes. '
                'With the high cast range and low cooldown on his spells, he is able to deliver the most superb and '
                'consistent magical damage of any hero in the game. Arc Lightning is a highly spammable nuke that '
                'creates a stream of lightning that bounces between enemy foes (up to fifteen times at max level), '
                'dealing minor damage. Lightning Bolt is more focused, dealing heavy damage to a single target, also '
                'on a very low cooldown. Static Field is a potent passive ability that allows Zeus\'s magical damage '
                'to scale into late game, dealing damage to all enemies within a decent AoE equal to a certain '
                'percentage of nearby targets\' health whenever he casts a spell. Finally, his ultimate Thundergod\'s '
                'Wrath allows him to strike all enemy heroes with a bolt of lightning, no matter their position, '
                'inflicting heavy damage. It can be used for multiple purposes: to finish off low-health enemy '
                'heroes limping away, to soften up the entire enemy team during a teamfight, or even to scout out the '
                'enemy\'s position. With the ability to strike down enemies both near and afar, the Lord of Heaven '
                'ensures that nobody can escape his wrath.',
         'quote': 'Immortality was overrated. This is much more interesting.',
         'strength': '19 + 2.3',
         'agility': '11 + 1.2',
         'intelligence': '20 + 2.7',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '350',
         'miss_s': '1100',
         'ad': '0.633 + 0.366',
         'cd': '0.4 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/zuus.png'
    },

    23: {'name': 'Kunkka',
         'role': 'Disabler, Initiator, Carry, Durable',
         'side': 'The Radiant',
         'class': 'Strength',
         'bio': '<strong>Kunkka</strong> the <strong>Admiral</strong> is a versatile melee Strength hero built with an '
                'arsenal of powerful area-of-effect spells. Two of his active spells are nukes that have long reaction '
                'time, but can disable and disrupt the enemies\' position. He is mostly played as a carry or an '
                'initiator or even a spell nuker. He is known for his Tidebringer sword, which magically gives him '
                'the ability to cleave a large area around him on his attack with heavy potential damage on his next '
                'attack, which refreshes at a given period of time. Torrent calls upon the element of water to rise '
                'and burst out, dealing damage, disabling them up high, and slowing them on impact. There\'s a delay '
                'on this skill before it activates, so Kunkka must be wise in using this ability. X Marks the Spot '
                'targets any hero or Admiral himself to be marked on their current position, and after a few seconds '
                'delay, instantly returns to the marked spot. Useful in setting up tricky spells, escape prevention, '
                'or even saving allies, X Marks the Spot makes the Admiral a great battle strategist. His ultimate '
                'lets him summon a Ghost Ship, which travels on ground, until it crashes a set distance away, '
                'stunning and damaging enemy armies on that location. The Ghost Ship also bolsters allies with '
                'Kunkka\'s Rum, granting them bonus movement speed and numbness to damage. Ghost Ship is difficult '
                'to land, due to the fixed distance of its cast point and the crash site of the ship. However, a '
                'good Ghost Ship absolutely cripples an enemy team. Capable of inflicting high burst damage with his '
                'spells, controlling their position while able to survive the mayhem when his spells are used '
                'properly, Kunkka is a mighty offensive team fighter, built with strong physical and magical damage '
                'output, who can indeed turn the tide of a battle.',
         'quote': 'Step lively now, your Admiral is on board!',
         'strength': '24 + 3',
         'agility': '14 + 1.3',
         'intelligence': '18 + 1.5',
         'ms': '300',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.4 + 0.3',
         'cd': '0.4 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/kunkka.png'
    },

    25: {'name': 'Lina',
         'role': 'Nuker, Disabler, Support',
         'side': 'The Radiant',
         'class': 'Intelligence',
         'bio': '<strong>Lina</strong> the <strong>Slayer</strong> is a ranged Intelligence hero, adept at destroying '
                'enemy heroes fast and delivering massive bursts of magical damage, making her one of the most '
                'effective gankers in the game. She possesses immense damaging capabilities all throughout the game, '
                'but is very fragile. Two of her fiery spells are her main source of damage, Dragon Slave sends a wave '
                'of fire to burn enemies in her path while Light Strike Array stuns them with a concentrated pillar '
                'of solar flame. Each of her spells deals great damage early on and has a low cooldown. Her Fiery Soul '
                'bolsters her attack and movement speed exponentially every time she casts a spell, which gives her '
                'scaling damage for the later game. Laguna Blade, her ultimate, is her ace in the hole. Lina fires off '
                'a huge bolt of lightning at a single target, dealing colossal damage. Laguna Blade\'s damage is '
                'staggering in early-mid game, and late game is still enough to destroy frail enemy heroes. Dragon '
                'Slave, Light Strike Array, and Laguna Blade are incredible flaming nukes that can incinerate her '
                'target instantly, and Fiery Soul allows her to transition into a strong and fast physical attacker. '
                'Though her power falls from its peak late game, mana-boosting and damage-increasing items can be '
                'purchased to keep herself up, serving as the team\'s magical semi-carry, dishing out intense burning '
                'damage with her attacks and spells.',
         'quote': 'One little spark and before you know it, the whole world is burning.',
         'strength': '18 + 1.5',
         'agility': '16 + 1.5',
         'intelligence': '27 + 3.2',
         'ms': '295',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '650',
         'miss_s': '900',
         'ad': '0.75 + 0.78',
         'cd': '0.45 + 1.08',
         'bat': '1.7',
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
         'quote': 'There are none so stabbed as those who will not see.',
         'strength': '17 + 2',
         'agility': '34 + 2.9',
         'intelligence': '14 + 1.3',
         'ms': '300',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.3',
         'cd': '0.4 + 0.51',
         'bat': '1.7',
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
         'role': 'Initiator, Support, Lane Support, Disabler',
         'side': 'The Dire',
         'class': 'Intelligence',
         'bio': '<strong>Demnok Lannik</strong> the <strong>Warlock</strong> is a ranged intelligence hero and a good '
                'support. His Shadow Word ability makes for an excellent heal as well as a decent harassment tool, '
                'and his physical attack helps him to ward off any enemies and keep his friends safe. He also '
                'possesses a considerable presence in team fights, as Fatal Bonds spreads damage dealt by his allies '
                'to all enemies affected by it and his Upheaval is a channelled Area of Effect spell that slows foes '
                'caught in it by up to 84%. His ultimate, Chaotic Offering allows him to summon a massive Golem to do '
                'his bidding, stunning anyone caught in a large area when it is summoned.',
         'quote': 'Chaos comes at my command!',
         'strength': '18 + 2.5',
         'agility': '10 + 1',
         'intelligence': '24 + 2.7',
         'ms': '295',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1200',
         'ad': '0.3 + 0.3',
         'cd': '0.5 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/warlock.png'
    },


    38: {'name': 'Beastmaster',
         'side': '',
         'avatar': 'img/dota/heroes/beastmaster.png'
    },

    39: {'name': 'Queen of Pain',
         'role': 'Nuker, Escape, Carry',
         'side': 'The Dire',
         'class': 'Intelligence',
         'bio': '<strong>Akasha</strong> the <strong>Queen of Pain</strong> is a ranged intelligence hero who uses her '
                'abilities to close in and deal huge area damage to the enemy. She is typically played as a ganker '
                'with her ability to appear in battle and deal damage in quick succession, as well as hunt down '
                'fleeing heroes with ease. Her Blink ability is the lynchpin of her skillset, allowing her to enter '
                'and leave fights at her whim. Once in position to attack, Akasha can unleash her Scream of Pain and '
                'Sonic Wave, able to devastate an entire team at once. Chasing down straggling prey is another of her '
                'fortes, with Shadow Strike crippling their ability to escape. Akasha is very adept at getting kills '
                'early in the game, and transitions very well into a semi-carry if she acquires the proper items.',
         'quote': 'They say pain is all in the mind, but they\'re wrong: It\'s all in my hands.',
         'strength': '16 + 1.7',
         'agility': '18 + 2',
         'intelligence': '24 + 2.5',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '550',
         'miss_s': '1500',
         'ad': '0.56 + 0.41',
         'cd': '0.452 + 1.008',
         'bat': '1.7',
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
         'quote': 'I\'m here to blur the line between life and death.',
         'strength': '20 + 1.85',
         'agility': '23 + 3.15',
         'intelligence': '13 + 1',
         'ms': '310',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.7',
         'cd': '0.3 + 0.5',
         'bat': '0.7',
         'avatar': 'img/dota/heroes/phantom_assassin.png'
    },

    45: {'name': 'Pugna', 'avatar': 'img/dota/heroes/pugna.png'},

    46: {'name': 'Templar Assassin',
         'role': 'Carry, Escape',
         'side': 'The Radiant',
         'class': 'Agility',
         'bio': '<p><strong>Lanaya</strong> the <strong>Templar Assassin</strong> is a short-ranged Agility hero '
                'capable of dealing huge bursts of Physical damage to swathes of enemies with expert positioning and '
                'timing. Unlike most physical damage dealers, Lanaya reaches her damage potential quite early and then '
                'scales up from that point with carry items, letting her gank with impunity throughout the '
                'mid-game, and her range changes from a melee hero to a ranged hero with short reach as '
                'she levels Psi Blades.</p><p>Her Psionic Traps provide map control and the ability to chase down '
                'fleeing heroes from up to 2000 range, and Refraction and Meld lets you shrug off high-damage nukes '
                'and disjoint projectiles. With a Blink Dagger, Lanaya can quickly materialize in the enemy team\'s '
                'weakest flank and shred several heroes at once with her Meld and Psi Blades.</p>',
         'quote': 'My body is a temple for which I will kill.',
         'strength': '18 + 2.1',
         'agility': '23 + 2.7',
         'intelligence': '20 + 2',
         'ms': '305',
         'tr': '0.7',
         'sr': '1800 / 800',
         'ar': '140',
         'miss_s': '900',
         'ad': '0.3 + 0.5',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/templar_assassin.png',
    },

    47: {'name': 'Viper', 'avatar': 'img/dota/heroes/viper.png'},

    48: {'name': 'Luna',
         'role': 'Carry, Nuker',
         'side': 'The Radiant',
         'class': 'Agility',
         'bio': '<strong>Luna</strong> the <strong>Moon Rider</strong> is a Ranged Agility carry hero. Even though '
                'she can be seen as a tempting target for enemy heroes, Luna possesses solid early game laning '
                'presence due to her Lucent Beams, a cheap, low-cooldown nuke, and her Lunar Blessing aura, which '
                'grants all nearby allied heroes increased damage. In mid-game, she becomes far more formidable with '
                'Moon Glaives, allowing her to kill entire creep waves with two to three attacks, and Eclipse, which '
                'can instantly kill a hero if that hero is unfortunate to catch its full blast. Luna is a very common '
                'pick in professional matches; owing to her unique status as a hard carry who is also a dangerous '
                'nuker. Her Achilles\' Heel is her fragility; she has no escape abilities and cannot handle a lot of '
                'punishment, relying on her enormous movement speed to keep her out of harm\'s way. Luna begins and '
                'ends a match dangerous, and if carefully and skilfully played will destroy '
                'anybody who stands against her.',
         'quote': 'I would water the trees with their entrails if Selemene would smile on me.',
         'strength': '15 + 1.9',
         'agility': '22 + 2.8',
         'intelligence': '16 + 1.85',
         'ms': '330',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '330',
         'miss_s': '900',
         'ad': '0.46 + 0.54',
         'cd': '0.6 + 0.4',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/luna.png'
    },

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

    57: {'name': 'Omniknight',
         'role': 'Durable, Lane Support, Support',
         'side': 'The Radiant',
         'class': 'Strength',
         'bio': '<strong>Purist Thunderwrath</strong> the <strong>Omniknight</strong> is a versatile melee strength '
                'hero who can take on the role of a support or, occasionally, a semi-carry, depending on the player\'s '
                'play style. A holy and courageous Hero, Omniknight possesses abilities that excel at protecting and '
                'aiding friendly heroes. His heal doubles as a nuke and he can grant any friend Magic Immunity, as '
                'well as blessing allies with a physical invulnerability and regeneration. Few can escape the mighty '
                'and heavenly power of the Omniknight and he is a powerful ally in team fights. He is a mighty tank, '
                'and one of the most difficult heroes to kill.',
         'quote': 'I have gazed into the Omniscience, and it has gazed into me.',
         'strength': '20 + 2.65',
         'agility': '15 + 1.75',
         'intelligence': '17 + 1.8',
         'ms': '305',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.433 + 0.567',
         'cd': '0.5 + 1.67',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/omniknight.png'},

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

    68: {'name': 'Ancient Apparition',
         'role': 'Support, Disabler',
         'side': 'The Dire',
         'class': 'Intelligence',
         'bio': '<strong>Kaldr</strong> the <strong>Ancient Apparition</strong> is a ranged intelligence hero. This '
                'spell-caster elemental being possesses high range, great attributes and strong semi-spammable spells. '
                'He is commonly played as a ganker or support role and due to his high agility and an attack enhancing '
                'spell, he can be played as a Semi-Carry too. His ultimate is one of the most devastating spells in '
                'the game as it can hit multiple units, has global range, freezes health regeneration, and instantly '
                'kill units if low on life.',
         'quote': 'One day, ice will cover these lands, and it will be as if this war never happened.',
         'strength': '18 + 1.4',
         'agility': '20 + 22',
         'intelligence': '25 + 2.6',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1250',
         'ad': '0.45 + 0.3',
         'cd': '0.01 + 0.75',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/ancient_apparition.png'},

    69: {'name': 'Doom Bringer', 'avatar': 'img/dota/heroes/doom_bringer.png'},

    70: {'name': 'Ursa',
         'role': 'Carry, Jungler, Durable',
         'side': 'The Radiant',
         'class': 'Agility',
         'bio': '<p><strong>Ulfsaar</strong> the <strong>Ursa Warrior</strong> is a melee agility hero whose '
                'abilities\' main focus is the increase of autoattack damage, allowing for some of the most '
                'impressive sustained damage in the entire game.</p><p>He specializes in increasing damage against one '
                'target. His abilities allow him to attack at up to maximum speed (400 IAS) and gain bonus damage '
                'with each consecutive hit on a single target. With these abilities—Overpower and Fury Swipes—Ursa '
                'can savage beefy targets for as much as 700 damage per hit. He is a ferocious jungler and '
                'straightforward attacker, able to solo even Roshan at low levels if he has Vladmir\'s Offering or '
                'another lifesteal. Ursa is a carry who can snowball if he is farmed, but the array of anti-melee '
                'abilities existing even by the early game and his lack of any counterspells, especially to strong '
                'nukers and heroes with the ability to evade him make him a hero reliant on other spells on his team. '
                'Although an agility hero, Ursa\'s strength gain makes him very durable, and his ultimate allows his '
                'damage to scale by building strength items.</p>',
         'quote': 'It is my spirit that keeps me safe, and not mere armor.',
         'strength': '23 + 2.9',
         'agility': '18 + 2.1',
         'intelligence': '16 + 1.5',
         'ms': '310',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.3',
         'cd': '0.3 + 0',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/ursa.png'
    },

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

    75: {'name': 'Silencer',
         'role': 'Support, Carry, Initiator',
         'side': 'The Radiant',
         'class': 'Intelligence',
         'bio': '<strong>Nortrom</strong> the <strong>Silencer</strong> is a ranged Intelligence hero who can be '
                'played as a Support, Carry or Initiator. He is one of the minority of Intelligence heroes who truly '
                'benefits from Intelligence items and is effective against Heroes who rely mostly on spells, as he can '
                'silence them while stealing their Intelligence and adding it to his own. He is a notorious anti-caster '
                'hero who can disrupt the magical abilities of his enemies and cripple spellcasters throughout the '
                'game. Curse of the Silent causes enemies to lose health and mana until the end of the duration or '
                'until the enemy casts a spell. Last Word places a curse on Nortrom\'s target that damages and '
                'silences for a long duration if the target casts a spell. If the target does not cast a spell before '
                'the curse\'s duration ends they will be damaged, silenced, and disarmed. Glaives of Wisdom is a '
                'Unique Attack Modifier that deals a percentage of Nortrom\'s intelligence as pure damage. Glaives '
                'of Wisdom also includes a passive component that permanently steals the intelligence of enemy heroes '
                'that die near Nortrom. Nortrom\'s ultimate, Global Silence, silences all enemy units on the map for '
                'a few seconds. A well-timed Global Silence can be used to save yourself or an ally, initiate a '
                'teamfight, or ruin the enemy\'s initiation.',
         'quote': 'Quiet as the grave.',
         'strength': '17 + 2.2',
         'agility': '16 + 2.1',
         'intelligence': '27 + 2.5',
         'ms': '300',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1000',
         'ad': '0.5 + 0.5',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/silencer.png'},

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

    81: {'name': 'Chaos Knight',
         'role': 'Carry, Disabler, Durable, Pusher',
         'side': 'The Dire',
         'class': 'Strength',
         'bio': '<strong>Chaos Knight</strong> is a melee strength Hero with one of the highest physical damage '
                'outputs of all heroes. He is mostly played as a semi-carry and ganker. As his name implies, he has a '
                'theme based on randomness and uncertainty. His regular attack has an incredibly high thirty damage '
                'spread, making his last hitting ability somewhat unreliable. Chaos Bolt is his most notorious '
                'luck-based ability which, at max level, can stun a target anywhere between a mediocre 2 seconds to an '
                'effective 4 seconds that will almost certainly assure its death; it will also deal a variable amount '
                'of damage ranging from miniscule to moderate. Reality Rift pulls Chaos Knight and his target to a '
                'randomly chosen point along the line between the two and gives him bonus damage for one attack. Chaos '
                'Strike is a crit-based ability with one of the lowest proc chances, yet also one of the highest '
                'multipliers. His only non-random ability is his ultimate Phantasm, which produces the most powerful '
                'illusions in the game. These illusions, which retain his full damage and only take double damage, '
                'benefit from his Chaos Strike and can teleport alongside him to attack the target whenever he uses '
                'Reality Rift. With three illusions being produced at Phantasm\'s highest level, Chaos Knight\'s '
                'damage output is effectively quadrupled during teamfights later in the game, and it is not uncommon '
                'to see enemy heroes being killed instantly after being Reality Rifted by the four apocalyptic '
                'horsemen. Thus, even though he is mostly played as a semi-carry who is extremely effective in the '
                'early to mid game, if the game drags on long enough and he is able to acquire enough strength-based '
                'and survivability items to ensure that his illusions can stay alive, he will be able to overpower '
                'most hard carries.',
         'quote': 'The light shall be blackened, and chaos shall reign.',
         'strength': '20 + 2.9',
         'agility': '14 + 2.1',
         'intelligence': '16 + 1.2',
         'ms': '325',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 0.5',
         'cd': '0.4 + 0.2',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/chaos_knight.png'},

    82: {'name': 'Meepo',
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
         'avatar': 'img/dota/heroes/meepo.png'
    },

    83: {'name': 'Treant Protector',
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
         'avatar': 'img/dota/heroes/treant.png'
    },

    84: {'name': 'Ogre Magi',
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
         'avatar': 'img/dota/heroes/ogre_magi.png'
    },

    85: {'name': 'Undying',
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
         'avatar': 'img/dota/heroes/undying.png'
    },

    86: {'name': 'Rubick',
         'role': 'Disabler, Pusher, Support, Line Support',
         'side': 'The Radiant',
         'class': 'Intelligence',
         'bio': '<strong>Rubick</strong> the <strong>Grand Magus</strong> is a ranged Intelligence hero best known for '
                'his ability to copy the spells of his enemies and use them as his own. Although he is mostly played '
                'as a support and is extremely fragile the entire length of the game, he can still prove to be one of '
                'the most influential heroes if he utilizes good positioning and well-timed usage of his ultimate, '
                'Spell Steal, correctly. Spell Steal allows Rubick to cast an enemy hero\'s most recently used spell, '
                'giving him supreme versatility throughout the game. By stealing the right abilities, the Grand Magus '
                'can aid himself and allies by casting crippling disables, applying curses, unleashing powerful nukes, '
                'disorienting the enemy team, supporting his allies with buffs, escaping from rough situations, or '
                'even enhancing his own physical attacks. His other abilities are just as worthy of a Magus: '
                'Telekinesis lets Rubick magically lift an enemy into the air, rendering the target helpless and '
                'vulnerable, before hurling the lifted enemy to the ground up to a short distance away and stunning '
                'nearby foes on impact. Fade Bolt blasts enemies with a stream of arcane energy which bounces to all '
                'enemies nearby, dealing damage and reducing their attack damage. Null Field is a passive aura, which '
                'grants himself and nearby allied heroes bonus magic resistance to shrug off magical assaults. '
                'Rubick\'s versatile skill-set and his infamous Spell Steal make him a flexible and powerful hero '
                'that can work in any lineup.',
         'quote': 'I am no thief. I merely borrow.',
         'strength': '19 + 1.5',
         'agility': '14 + 1.6',
         'intelligence': '27 + 2.4',
         'ms': '290',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1125',
         'ad': '0.4 + 0.77',
         'cd': '0.1 + 1.17',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/rubick.png'},

    87: {'name': 'Disruptor',
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
         'avatar': 'img/dota/heroes/disruptor.png'},

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

    89: {'name': 'Naga Siren',
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
         'avatar': 'img/dota/heroes/naga_siren.png'},

    90: {'name': 'Keeper of the Light',
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
         'avatar': 'img/dota/heroes/keeper_of_the_light.png'},

    91: {'name': 'Io',
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
         'avatar': 'img/dota/heroes/wisp.png'},

    92: {'name': 'Visage',
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
         'avatar': 'img/dota/heroes/visage.png'},


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

    94: {'name': 'Medusa',
         'role': 'Carry',
         'side': 'The Dire',
         'class': 'Agility',
         'bio': '<strong>Medusa</strong> the <strong>Gorgon</strong> is a ranged agility Hero. Highly item-dependent, '
                'she acts as a carry who can potentially strike down entire teams at once while protected by tank-like '
                'survivability. Split Shot allows her attacks to hit multiple targets, greatly increasing the potency '
                'of damage-granting items. Mystic Snake grants Medusa some presence in the lane and skirmishes, and '
                'its mana stealing refunds part of the cost to boot, making it an excellent farming and harrassing '
                'tool. Mana Shield protects her from the opening damage of teamfights, and if supplemented with items '
                'makes killing Medusa a fatally time-consuming process. Stone Gaze acts as a fantastic defensive '
                'mechanism against ganks and initiations alike, '
                'with crippling effects on all who dare face the Gorgon.',
         'quote': 'The only real beauty is power.',
         'strength': '14 + 1.65',
         'agility': '20 + 2.5',
         'intelligence': '19 + 1.85',
         'ms': '290',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1200',
         'ad': '0.5 + 0.6',
         'cd': '0.4 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/medusa.png'
    },

    95: {'name': 'Troll Warlord',
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
         'avatar': 'img/dota/heroes/troll_warlord.png'
    },

    96: {'name': 'Centaur Warrunner',
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
         'avatar': 'img/dota/heroes/centaur.png'
    },

    97: {'name': 'Magnus',
         'role': 'Initiator, Disabler, Nuker, Carry',
         'side': 'The Dire',
         'class': 'Strength',
         'bio': '<strong>Magnus</strong> the <strong>Magnoceros</strong> is a monstrous melee strength hero who is '
                'usually played as a ganker, initiator, or semi-carry. His ability to battle multiple heroes at once '
                'gives him an excellent presence in team fights. In addition to his teamfight presence, he can buff '
                'allies or himself with bonus damage and cleave, capitalizing on his ability to group up multiple '
                'enemies. As a hero who possesses multiple area-of-effect abilities with a manageable mana cost, '
                'and a very powerful ultimate that serves as both a team fight and initiation ability, Magnus is '
                'truly a force to be reckoned with.',
         'quote': 'No, I blame no one who covets my horn. But to desire more than sight of it is a guarantee of death.',
         'strength': '21 + 2.75',
         'agility': '15 + 2.5',
         'intelligence': '17 + 1.65',
         'ms': '315',
         'tr': '0.8',
         'sr': '1800 + 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 0.84',
         'cd': '0.3 + 0.6',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/magnataur.png'
    },

    98: {'name': 'Timbersaw',
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
         'avatar': 'img/dota/heroes/shredder.png'
    },

    99: {'name': 'Bristleback',
         'role': 'Durable, Initiator, Disabler',
         'side': 'The Radiant',
         'class': 'Strength',
         'bio': '<strong>Rigwarl</strong> the <strong>Bristleback</strong> is a melee Strength hero famous for his '
                'array of synergistic spells with low mana cost and cooldown. He is able to slow his enemies down and '
                'reduce their armor with Viscous Nasal Goo, then hit them with a barrage of Quill Sprays, making him '
                'an effective chaser when ganking enemies. His low strength gain makes him less tanky than most '
                'strength heroes, but he becomes substantially more durable when he turns around due to his passive '
                'Bristleback, which reduces damage taken from behind. In the right hands, Bristleback is a powerful '
                'ganker in the early stages of the game, and a powerful semi-carry in the later stages depending on '
                'how much farm he gets.',
         'quote': 'It was a barkeep that got me into this mess. Yeah, I think I\'ll pay em a visit when this is done.',
         'strength': '22 + 2.2',
         'agility': '17 + 1.8',
         'intelligence': '14 + 2.8',
         'ms': '295',
         'tr': '1.0',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.3',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/bristleback.png'
    },

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
          'quote': 'Those who tangle with the Skywrath risk a fall from starry heights.',
          'strength': '19 + 1.5',
          'agility': '18 + 0.8',
          'intelligence': '27 + 3.6',
          'ms': '315',
          'tr': '0.5',
          'sr': '1800 / 800',
          'ar': '600',
          'miss_s': '1000',
          'ad': '0.4 + 0.78',
          'cd': '0.1 + 1.08',
          'bat': '1.7',
          'avatar': 'img/dota/heroes/skywrath_mage.png'
    },

    102: {'name': 'Abaddon',
          'role': 'Durable, Support, Escape',
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
          'quote': 'The fog of war is no match for the mist of fate.',
          'strength': '23 + 2.7',
          'agility': '17 + 1.5',
          'intelligence': '21 + 2',
          'ms': '310',
          'tr': '0.6',
          'sr': '1800 / 800',
          'ar': 'Melee',
          'miss_s': 'Instant',
          'ad': '0.56 + 0.41',
          'cd': '0.452 + 1.008',
          'bat': '1.7',
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
          'quote': 'It is only right that I am cast into this world, for I had a hand in breaking it.',
          'strength': '24 + 2.3',
          'agility': '14 + 1.5',
          'intelligence': '23 + 1.6',
          'ms': '315',
          'tr': '0.4',
          'sr': '1800 / 800',
          'ar': 'Melee',
          'miss_s': 'Instant',
          'ad': '0.35 + 0.97',
          'cd': '0.4 + 0.8',
          'bat': '1.7',
          'avatar': 'img/dota/heroes/elder_titan.png'},

    104: {'name': 'Legion Commander',
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
          'bio': '<p><strong>Kaolin</strong>, the <strong>Earth Spirit</strong> a hero with the middle type of attack, '
                 'the main characteristic of which is the strength. The hero is a very versatile and useful to the '
                 'whole team. Can help to kill the enemies on the lines and be ганкером, is also very useful in the '
                 'mass battles, because of its ability to affect the region. He can act in a role of the initiator, as '
                 'his abilities can neutralize the entire enemy team. Also can act out the role of a semi-Kerry with '
                 'the proper assembling objects and lead your team to victory.</p><p>However, the ability of Kaolin '
                 'require good control and positioning, therefore it is recommended for players with an advanced '
                 'level of the game, and in any case not advisable for beginners.</p>',
          'quote': 'Through conflict, one\'s nature is revealed.',
          'strength': '21 + 2.9',
          'agility': '17 + 1.5',
          'intelligence': '18 + 2.4',
          'ms': '305',
          'tr': '0.6',
          'sr': '1800 / 800',
          'ar': 'Melee',
          'miss_s': 'Instant',
          'ad': '0.35 + 0.65',
          'cd': '0.01 + 0',
          'bat': '1.7',
          'avatar': 'img/dota/heroes/earth_spirit.png'
    }

}