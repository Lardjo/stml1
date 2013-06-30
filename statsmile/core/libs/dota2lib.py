#!/usr/bin/env python3
# All right reserved 2013
# Description: Dota 2 Library (inc. items, heroes)
# URL: http://github.com/Lardjo

mode = {1: {"name": 'All Pick'},
        2: {'name': 'Captains Mode'},
        3: {'name': 'Random Draft'},
        4: {'name': 'Single Draft'},
        5: {'name': 'All Random'}}

cluster = {111: {'name': 'US West'},
           121: {'name': 'US East'},
           122: {'name': 'US East'},
           131: {'name': 'Europe West'},
           132: {'name': 'Europe West'},
           133: {'name': 'Europe West'},
           151: {'name': 'Southeast Asia'},
           152: {'name': 'Southeast Asia'},
           161: {'name': 'China'},
           163: {'name': 'China'},
           171: {'name': 'Australia'},
           181: {'name': 'Russia'},
           182: {'name': 'Russia'},
           191: {'name': 'Europe East'},
           200: {'name': 'South America'}}

heroes = {1: {'name': 'Antimage', 'avatar': 'img/dota2heroes/antimage.png'},
          2: {'name': 'Axe', 'avatar': 'img/dota2heroes/axe.png'},
          3: {'name': 'Ban', 'avatar': 'img/dota2heroes/bane.png'},
          4: {'name': 'Bloodseeker', 'avatar': 'img/dota2heroes/bloodseeker.png'},
          5: {'name': 'Crystal Maiden', 'avatar': 'img/dota2heroes/crystal_maiden.png'},
          6: {'name': 'Drow Ranger', 'avatar': 'img/dota2heroes/drow_ranger.png'},
          7: {'name': 'Earthshaker', 'avatar': 'img/dota2heroes/earthshaker.png'},
          8: {'name': 'Juggernaut', 'avatar': 'img/dota2heroes/juggernaut.png'},
          9: {'name': 'Mirana', 'avatar': 'img/dota2heroes/mirana.png'},
          10: {'name': 'Morphling', 'avatar': 'img/dota2heroes/morphling.png'},
          11: {'name': 'Shadow Fiend', 'avatar': 'img/dota2heroes/shadow_fiend.png'},
          12: {'name': 'Phantom Lancer', 'avatar': 'img/dota2heroes/phantom_lancer.png'},
          13: {'name': 'Puck', 'avatar': 'img/dota2heroes/puck.png'},
          14: {'name': 'Pudge', 'avatar': 'img/dota2heroes/pudge.png'},
          15: {'name': 'Razor', 'avatar': 'img/dota2heroes/razor.png'},
          16: {'name': 'Sand King', 'avatar': 'img/dota2heroes/sand_king.png'},
          17: {'name': 'Storm Spirit', 'avatar': 'img/dota2heroes/storm_spirit.png'},
          18: {'name': 'Sven', 'avatar': 'img/dota2heroes/sven.png'},
          19: {'name': 'Tiny', 'avatar': 'img/dota2heroes/tiny.png'},
          20: {'name': 'Vengeful Spirit', 'avatar': 'img/dota2heroes/vengeful_spirit.png'},
          21: {'name': 'Windrunner', 'avatar': 'img/dota2heroes/windrunner.png'},
          22: {'name': 'Zeus', 'avatar': 'img/dota2heroes/zeus.png'},
          23: {'name': 'Kunkka', 'avatar': 'img/dota2heroes/kunkka.png'},
          25: {'name': 'Lina', 'avatar': 'img/dota2heroes/lina.png'},
          26: {'name': 'Lion', 'avatar': 'img/dota2heroes/lion.png'},
          27: {'name': 'Shadow Shaman', 'avatar': 'img/dota2heroes/shadow_shaman.png'},
          28: {'name': 'Slardar', 'avatar': 'img/dota2heroes/slardar.png'},
          29: {'name': 'Tidehunter', 'avatar': 'img/dota2heroes/tidehunter.png'},
          30: {'name': 'Witch Doctor', 'avatar': 'img/dota2heroes/witch_doctor.png'},
          31: {'name': 'Lich', 'avatar': 'img/dota2heroes/lich.png'},
          32: {'name': 'Riki', 'avatar': 'img/dota2heroes/riki.png'},
          33: {'name': 'Enigma', 'avatar': 'img/dota2heroes/enigma.png'},
          34: {'name': 'Tinker', 'avatar': 'img/dota2heroes/tinker.png'},
          35: {'name': 'Sniper', 'avatar': 'img/dota2heroes/sniper.png'},
          36: {'name': 'Necrolyte', 'avatar': 'img/dota2heroes/necrolyte.png'},
          37: {'name': 'Warlock', 'avatar': 'img/dota2heroes/warlock.png'},
          38: {'name': 'Beastmaster', 'avatar': 'img/dota2heroes/beastmaster.png'},
          39: {'name': 'Queen of Pain', 'avatar': 'img/dota2heroes/queen_of_pain.png'},
          40: {'name': 'Venomancer', 'avatar': 'img/dota2heroes/venomancer.png'},
          41: {'name': 'Faceless Void', 'avatar': 'img/dota2heroes/faceless_void.png'},
          42: {'name': 'Skeleton King', 'avatar': 'img/dota2heroes/skeleton_king.png'},
          43: {'name': 'Death Prophet', 'avatar': 'img/dota2heroes/death_prophet.png'},
          44: {'name': 'Phantom Assassin', 'avatar': 'img/dota2heroes/phantom_assassin.png'},
          45: {'name': 'Pugna', 'avatar': 'img/dota2heroes/pugna.png'},
          46: {'name': 'Templar Assassin', 'avatar': 'img/dota2heroes/templar_assassin.png'},
          47: {'name': 'Viper', 'avatar': 'img/dota2heroes/viper.png'},
          48: {'name': 'Luna', 'avatar': 'img/dota2heroes/luna.png'},
          49: {'name': 'Dragon Knight', 'avatar': 'img/dota2heroes/dragon_knight.png'},
          50: {'name': 'Dazzle', 'avatar': 'img/dota2heroes/dazzle.png'},
          51: {'name': 'Clockwerk', 'avatar': 'img/dota2heroes/clockwerk.png'},
          52: {'name': 'Leshrac', 'avatar': 'img/dota2heroes/leshrac.png'},
          53: {'name': 'Natures Prophet', 'avatar': 'img/dota2heroes/nature_prophet.png'},
          54: {'name': 'Lifestealer', 'avatar': 'img/dota2heroes/lifestealer.png'},
          55: {'name': 'Dark Seer', 'avatar': 'img/dota2heroes/dark_seer.png'},
          56: {'name': 'Clinkz', 'avatar': 'img/dota2heroes/clinkz.png'},
          57: {'name': 'Omniknight', 'avatar': 'img/dota2heroes/omniknight.png'},
          58: {'name': 'Enchantress', 'avatar': 'img/dota2heroes/enchantress.png'},
          59: {'name': 'Huskar', 'avatar': 'img/dota2heroes/huskar.png'},
          60: {'name': 'Night Stalker', 'avatar': 'img/dota2heroes/night_stalker.png'},
          61: {'name': 'Broodmother', 'avatar': 'img/dota2heroes/broodmother.png'},
          62: {'name': 'Bounty Hunter', 'avatar': 'img/dota2heroes/bounty_hunter.png'},
          63: {'name': 'Weaver', 'avatar': 'img/dota2heroes/weaver.png'},
          64: {'name': 'Jakiro', 'avatar': 'img/dota2heroes/jakiro.png'},
          65: {'name': 'Batrider', 'avatar': 'img/dota2heroes/batrider.png'},
          66: {'name': 'Chen', 'avatar': 'img/dota2heroes/chen.png'},
          67: {'name': 'Spectre', 'avatar': 'img/dota2heroes/spectre.png'},
          68: {'name': 'Ancient Apparition', 'avatar': 'img/dota2heroes/ancient_aparition.png'},
          69: {'name': 'Doom Bringer', 'avatar': 'img/dota2heroes/doom_bringer.png'},
          70: {'name': 'Ursa', 'avatar': 'img/dota2heroes/ursa.png'},
          71: {'name': 'Spirit Breaker', 'avatar': 'img/dota2heroes/spirit_breaker.png'},
          72: {'name': 'Gyrocopter', 'avatar': 'img/dota2heroes/gyrocopter.png'},
          73: {'name': 'Alchemist', 'avatar': 'img/dota2heroes/alchemist.png'},
          74: {'name': 'Invoker', 'avatar': 'img/dota2heroes/invoker.png'},
          75: {'name': 'Silencer', 'avatar': 'img/dota2heroes/silencer.png'},
          76: {'name': 'Outworld Destroyer', 'avatar': 'img/dota2heroes/outworld_destroyer.png'},
          77: {'name': 'Lycanthrope', 'avatar': 'img/dota2heroes/lycanthrope.png'},
          78: {'name': 'Brewmaster', 'avatar': 'img/dota2heroes/brewmaster.png'},
          79: {'name': 'Shadow Demon', 'avatar': 'img/dota2heroes/shadow_demon.png'},
          80: {'name': 'Lone Druid', 'avatar': 'img/dota2heroes/lone_druid.png'},
          81: {'name': 'Chaos Knight', 'avatar': 'img/dota2heroes/chaos_knight.png'},
          82: {'name': 'Meepo', 'avatar': 'img/dota2heroes/meepo.png'},
          83: {'name': 'Treant Protector', 'avatar': 'img/dota2heroes/treant_protector.png'},
          84: {'name': 'Ogre Magi', 'avatar': 'img/dota2heroes/ogre_magi.png'},
          85: {'name': 'Undying', 'avatar': 'img/dota2heroes/undying.png'},
          86: {'name': 'Rubick', 'avatar': 'img/dota2heroes/rubick.png'},
          87: {'name': 'Disruptor', 'avatar': 'img/dota2heroes/disruptor.png'},
          88: {'name': 'Nyx Assassin', 'avatar': 'img/dota2heroes/nyx_assassin.png'},
          89: {'name': 'Naga Siren', 'avatar': 'img/dota2heroes/naga_siren.png'},
          90: {'name': 'Keeper of the Light', 'avatar': 'img/dota2heroes/keeper_of_the_light.png'},
          91: {'name': 'Wisp', 'avatar': 'img/dota2heroes/wisp.png'},
          92: {'name': 'Visage', 'avatar': 'img/dota2heroes/visage.png'},
          93: {'name': 'Slark', 'avatar': 'img/dota2heroes/slark.png'},
          94: {'name': 'Medusa', 'avatar': 'img/dota2heroes/medusa.png'},
          95: {'name': 'Troll Warlord', 'avatar': 'img/dota2heroes/troll_warlord.png'},
          96: {'name': 'Centaur Warrunner', 'avatar': 'img/dota2heroes/centaur_warrunner.png'},
          97: {'name': 'Magnus', 'avatar': 'img/dota2heroes/magnus.png'},
          98: {'name': 'Timbersaw', 'avatar': 'img/dota2heroes/timbersaw.png'},
          99: {'name': 'Bristleback', 'avatar': 'img/dota2heroes/bristleback.png'},
          100: {'name': 'Tusk', 'avatar': 'img/dota2heroes/tusk.png'},
          101: {'name': 'Skywrath Mage', 'avatar': 'img/dota2heroes/skywrath_mage.png'},
          102: {'name': 'Elder Titan', 'avatar': 'img/dota2heroes/elder_titan.png'}}

items = {0: {'avatar': 'data-src=holder.js/60x45/text:Empty'},
         1: {'name': 'Blink Dagger', 'avatar': 'img/dota2items/blink_dagger.png'},
         2: {'name': 'Blades of Attack', 'avatar': 'img/dota2items/blades_of_attack.png'},
         3: {'name': 'Broadsword', 'avatar': 'img/dota2items/broadsword.png'},
         4: {'name': 'Chainmail', 'avatar': 'img/dota2items/chainmail.png'},
         5: {'name': 'Claymore', 'avatar': 'img/dota2items/claymore.png'},
         6: {'name': 'Helm of Iron Will', 'avatar': 'img/dota2items/helm_of_iron_will.png'},
         7: {'name': 'Javelin', 'avatar': 'img/dota2items/javelin.png'},
         8: {'name': 'Mithril Hammer', 'avatar': 'img/dota2items/mithril_hammer.png'},
         9: {'name': 'Platemail', 'avatar': 'img/dota2items/platemail.png'},
         10: {'name': 'Quarterstaff', 'avatar': 'img/dota2items/quarterstaff.png'},
         11: {'name': 'Quelling Blade', 'avatar': 'img/dota2items/quelling_blade.png'},
         12: {'name': 'Ring of Protection', 'avatar': 'img/dota2items/ring_of_protection.png'},
         13: {'name': 'Gauntlets of Strength', 'avatar': 'img/dota2items/gauntlets_of_strength.png'},
         14: {'name': 'Slippers of Agility', 'avatar': 'img/dota2items/slippers_of_agility.png'},
         15: {'name': 'Mantle of Intelligence', 'avatar': 'img/dota2items/mantle_of_intelligence.png'},
         16: {'name': 'Iron Branch', 'avatar': 'img/dota2items/iron_branch.png'},
         17: {'name': 'Belt of Strength', 'avatar': 'img/dota2items/belt_of_strength.png'},
         18: {'name': 'Band of Elvenskin', 'avatar': 'img/dota2items/band_of_elvenskin.png'},
         19: {'name': 'Robe of the Magi', 'avatar': 'img/dota2items/robe_of_the_magi.png'},
         20: {'name': 'Circlet', 'avatar': 'img/dota2items/circlet.png'},
         21: {'name': 'Ogre Club', 'avatar': 'img/dota2items/ogre_club.png'},
         22: {'name': 'Blade of Alacrity', 'avatar': 'img/dota2items/blade_of_alacrity.png'},
         23: {'name': 'Staff of Wizardry', 'avatar': 'img/dota2items/staff_of_wizardry.png'},
         24: {'name': 'Ultimate Orb', 'avatar': 'img/dota2items/ultimate_orb.png'},
         25: {'name': 'Gloves of Haste', 'avatar': 'img/dota2items/gloves_of_haste.png'},
         26: {'name': 'Morbid Mask', 'avatar': 'img/dota2items/morbid_mask.png'},
         27: {'name': 'Ring of Regen', 'avatar': 'img/dota2items/ring_of_regen.png'},
         28: {'name': 'Sage\'s Mask', 'avatar': 'img/dota2items/sages_mask.png'},
         29: {'name': 'Boots of Speed', 'avatar': 'img/dota2items/boots_of_speed.png'},
         30: {'name': 'Gem of True Sight', 'avatar': 'img/dota2items/gem_of_true_sight.png'},
         31: {'name': 'Cloak', 'avatar': 'img/dota2items/cloak.png'},
         32: {'name': 'Talisman of Evasion', 'avatar': 'img/dota2items/talisman_of_evasion.png'},
         34: {'name': 'Magic Stick', 'avatar': 'img/dota2items/magic_stick.png'},
         36: {'name': 'Magic Wand', 'avatar': 'img/dota2items/magic_wand.png'},
         37: {'name': 'Ghost Scepter', 'avatar': 'img/dota2items/ghost_scepter.png'},
         38: {'name': 'Clarity', 'avatar': 'img/dota2items/clarity.png'},
         39: {'name': 'Healing Salve', 'avatar': 'img/dota2items/healing_salve.png'},
         40: {'name': 'Dust of Appearance', 'avatar': 'img/dota2items/dust_of_appearance.png'},
         41: {'name': 'Bottle', 'avatar': 'img/dota2items/bottle.png'},
         42: {'name': 'Observer Ward', 'avatar': 'img/dota2items/observer_ward.png'},
         43: {'name': 'Sentry Ward', 'avatar': 'img/dota2items/sentry_ward.png'},
         44: {'name': 'Tango', 'avatar': 'img/dota2items/tango.png'},
         46: {'name': 'Teleport Scroll', 'avatar': 'img/dota2items/town_portal_scroll.png'},
         48: {'name': 'Travel Boots', 'avatar': 'img/dota2items/boots_of_travel.png'},
         50: {'name': 'Phase Boots', 'avatar': 'img/dota2items/phase_boots.png'},
         51: {'name': 'Demon Edge', 'avatar': 'img/dota2items/demon_edge.png'},
         52: {'name': 'Eaglesong', 'avatar': 'img/dota2items/eaglesong.png'},
         53: {'name': 'Reaver', 'avatar': 'img/dota2items/reaver.png'},
         54: {'name': 'Sacred Relic', 'avatar': 'img/dota2items/sacred_relic.png'},
         55: {'name': 'Hyperstone', 'avatar': 'img/dota2items/hyperstone.png'},
         56: {'name': 'Ring of Health', 'avatar': 'img/dota2items/ring_of_health.png'},
         57: {'name': 'Void Stone', 'avatar': 'img/dota2items/void_stone.png'},
         58: {'name': 'Mystic Staff', 'avatar': 'img/dota2items/mystic_staff.png'},
         59: {'name': 'Energy Booster', 'avatar': 'img/dota2items/energy_booster.png'},
         60: {'name': 'Point Booster', 'avatar': 'img/dota2items/point_booster.png'},
         61: {'name': 'Vitality Booster', 'avatar': 'img/dota2items/vitality_booster.png'},
         63: {'name': 'Power Treads', 'avatar': 'img/dota2items/power_treads.png'},
         65: {'name': 'Hand of Midas', 'avatar': 'img/dota2items/hand_of_midas.png'},
         67: {'name': 'Oblivion Staff', 'avatar': 'img/dota2items/oblivion_staff.png'},
         69: {'name': 'Perseverance', 'avatar': 'img/dota2items/perseverance.png'},
         71: {'name': 'Poor Man\'s Shield', 'avatar': 'img/dota2items/poor_mans_shield.png'},
         73: {'name': 'Bracer', 'avatar': 'img/dota2items/bracer.png'},
         75: {'name': 'Wraith Band', 'avatar': 'img/dota2items/wraith_band.png'},
         77: {'name': 'Null Talisman', 'avatar': 'img/dota2items/null_talisman.png'},
         79: {'name': 'Mekansm', 'avatar': 'img/dota2items/mekansm.png'},
         81: {'name': 'Vladmir\'s Offering', 'avatar': 'img/dota2items/vladmirs_offering.png'},
         86: {'name': 'Buckler', 'avatar': 'img/dota2items/buckler.png'},
         88: {'name': 'Ring of Basilius', 'avatar': 'img/dota2items/ring_of_basilius.png'},
         90: {'name': 'Pipe of Insight', 'avatar': 'img/dota2items/pipe_of_insight.png'},
         92: {'name': 'Urn of Shadows', 'avatar': 'img/dota2items/urn_of_shadows.png'},
         94: {'name': 'Headdress', 'avatar': 'img/dota2items/headdress.png'},
         96: {'name': 'Scythe of Vyse', 'avatar': 'img/dota2items/scythe_of_vyse.png'},
         98: {'name': 'Orchid Malevolence', 'avatar': 'img/dota2items/orchid_malevolence.png'},
         100: {'name': 'Euls Scepter of Divinity', 'avatar': 'img/dota2items/euls_scepter_of_divinity.png'},
         102: {'name': 'Force Staff', 'avatar': 'img/dota2items/force_staff.png'},
         104: {'name': 'Dagon Level 1', 'avatar': 'img/dota2items/dagon_1.png'},
         108: {'name': 'Aghanim\'s Scepter', 'avatar': 'img/dota2items/aghanims_scepter.png'},
         110: {'name': 'Refresher Orb', 'avatar': 'img/dota2items/refresher_orb.png'},
         112: {'name': 'Assault Cuirass', 'avatar': 'img/dota2items/assault_cuirass.png'},
         114: {'name': 'Heart of Tarrasque', 'avatar': 'img/dota2items/heart_of_tarrasque.png'},
         117: {'name': 'Aegis', 'avatar': 'img/dota2items/aegis.png'},
         119: {'name': 'Shiva\'s Guard', 'avatar': 'img/dota2items/shivas_guard.png'},
         116: {'name': 'Black King Bar', 'avatar': 'img/dota2items/black_king_bar.png'},
         121: {'name': 'Bloodstone', 'avatar': 'img/dota2items/bloodstone.png'},
         122: {'name': 'Recipe: Linken\'s Sphere', 'avatar': 'img/dota2items/recipe_scroll.png'},
         123: {'name': 'Linken\'s Sphere', 'avatar': 'img/dota2items/linkens_sphere.png'},
         125: {'name': 'Vanguard', 'avatar': 'img/dota2items/vanguard.png'},
         127: {'name': 'Blade Mail', 'avatar': 'img/dota2items/blade_mail.png'},
         131: {'name': 'Hood of Defiance', 'avatar': 'img/dota2items/hood_of_defiance.png'},
         133: {'name': 'Divine Rapier', 'avatar': 'img/dota2items/divine_rapier.png'},
         135: {'name': 'Monkey King Bar', 'avatar': 'img/dota2items/monkey_king_bar.png'},
         137: {'name': 'Radiance', 'avatar': 'img/dota2items/radiance.png'},
         139: {'name': 'Butterfly', 'avatar': 'img/dota2items/butterfly.png'},
         140: {'name': 'Recipe: Daedalus', 'avatar': 'img/dota2items/recipe_scroll.png'},
         141: {'name': 'Daedalus', 'avatar': 'img/dota2items/daedalus.png'},
         143: {'name': 'Basher', 'avatar': 'img/dota2items/skull_basher.png'},
         145: {'name': 'Battlefury', 'avatar': 'img/dota2items/battle_fury.png'},
         147: {'name': 'Manta', 'avatar': 'img/dota2items/manta_style.png'},
         149: {'name': 'Crystalys', 'avatar': 'img/dota2items/crystalys.png'},
         151: {'name': 'Armlet of Mordiggian', 'avatar': 'img/dota2items/armlet_of_mordiggian.png'},
         152: {'name': 'Shadow Blade', 'avatar': 'img/dota2items/shadow_blade.png'},
         154: {'name': 'Sange and Yasha', 'avatar': 'img/dota2items/sange_and_yasha.png'},
         156: {'name': 'Satanic', 'avatar': 'img/dota2items/satanic.png'},
         158: {'name': 'Mjollnir', 'avatar': 'img/dota2items/mjollnir.png'},
         160: {'name': 'Eye of Skadi', 'avatar': 'img/dota2items/eye_of_skadi.png'},
         162: {'name': 'Sange', 'avatar': 'img/dota2items/sange.png'},
         164: {'name': 'Helm of the Dominator', 'avatar': 'img/dota2items/helm_of_the_dominator.png'},
         166: {'name': 'Maelstrom', 'avatar': 'img/dota2items/maelstrom.png'},
         167: {'name': 'Recipe: Desolator', 'avatar': 'img/dota2items/recipe_scroll.png'},
         168: {'name': 'Desolator', 'avatar': 'img/dota2items/desolator.png'},
         170: {'name': 'Yasha', 'avatar': 'img/dota2items/yasha.png'},
         172: {'name': 'Mask of Madness', 'avatar': 'img/dota2items/mask_of_madness.png'},
         174: {'name': 'Diffusal Blade Level 1', 'avatar': 'img/dota2items/diffusal_blade_1.png'},
         176: {'name': 'Ethereal Blade', 'avatar': 'img/dota2items/ethereal_blade.png'},
         178: {'name': 'Soul Ring', 'avatar': 'img/dota2items/soul_ring.png'},
         180: {'name': 'Arcane Boots', 'avatar': 'img/dota2items/arcane_boots.png'},
         181: {'name': 'Orb of Venom', 'avatar': 'img/dota2items/orb_of_venom.png'},
         182: {'name': 'Stout Shield', 'avatar': 'img/dota2items/stout_shield.png'},
         185: {'name': 'Drum of Endurance', 'avatar': 'img/dota2items/drum_of_endurance.png'},
         187: {'name': 'Medallion of Courage', 'avatar': 'img/dota2items/medallion_of_courage.png'},
         188: {'name': 'Smoke of Deceit', 'avatar': 'img/dota2items/smoke_of_deceit.png'},
         194: {'name': 'Necronomicon', 'avatar': 'img/dota2items/necronomicon.png'},
         196: {'name': 'Diffusal Blade Level 2', 'avatar': 'img/dota2items/diffusal_blade.png'},
         201: {'name': 'Dagon Level 2', 'avatar': 'img/dota2items/dagon_2.png'},
         202: {'name': 'Dagon Level 3', 'avatar': 'img/dota2items/dagon_3.png'},
         204: {'name': 'Dagon Level 5', 'avatar': 'img/dota2items/dagon.png'},
         206: {'name': 'Rod of Atos', 'avatar': 'img/dota2items/rod_of_atos.png'},
         208: {'name': 'Abyssal Blade', 'avatar': 'img/dota2items/abyssal_blade.png'},
         210: {'name': 'Heaven\'s Halberd', 'avatar': 'img/dota2items/heavens_halberd.png'},
         212: {'name': 'Ring of Aquila', 'avatar': 'img/dota2items/ring_of_aquila.png'},
         214: {'name': 'Tranquil Boots', 'avatar': 'img/dota2items/tranquil_boots.png'},
         215: {'name': 'Shadow Amulet', 'avatar': 'img/dota2items/shadow_amulet.png'}}