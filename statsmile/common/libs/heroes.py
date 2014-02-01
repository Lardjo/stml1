#!/usr/bin/env python3
# All right reserved 2013
# Description: Dota 2 Library (Heroes)
# URL: http://github.com/Lardjo

heroes = {

    1: {'name': 'Anti-Mage',
        'avatar': 'img/dota/heroes/antimage.png',
        'ability': [{'id': 5003, 'image': 'img/dota/spellicons/antimage_mana_break.png'},
                    {'id': 5004, 'image': 'img/dota/spellicons/antimage_blink.png'},
                    {'id': 5005, 'image': 'img/dota/spellicons/antimage_spell_shield.png'},
                    {'id': 5006, 'image': 'img/dota/spellicons/antimage_mana_void.png'}]},
    2: {'name': 'Axe',
        'avatar': 'img/dota/heroes/axe.png',
        'ability': [{'id': 5007, 'image': 'img/dota/spellicons/axe_berserkers_call.png'},
                    {'id': 5008, 'image': 'img/dota/spellicons/axe_battle_hunger.png'},
                    {'id': 5009, 'image': 'img/dota/spellicons/axe_counter_helix.png'},
                    {'id': 5010, 'image': 'img/dota/spellicons/axe_culling_blade.png'}]},
    3: {'name': 'Bane', 'avatar': 'img/dota/heroes/bane.png'},
    4: {'name': 'Bloodseeker', 'avatar': 'img/dota/heroes/bloodseeker.png'},
    5: {'name': 'Crystal Maiden',
        'avatar': 'img/dota/heroes/crystal_maiden.png',
        'ability': [{'id': 5126, 'image': 'img/dota/spellicons/crystal_maiden_crystal_nova.png'},
                    {'id': 5127, 'image': 'img/dota/spellicons/crystal_maiden_frostbite.png'},
                    {'id': 5128, 'image': 'img/dota/spellicons/crystal_maiden_brilliance_aura.png'},
                    {'id': 5129, 'image': 'img/dota/spellicons/crystal_maiden_freezing_field.png'}]},
    6: {'name': 'Drow Ranger',
        'avatar': 'img/dota/heroes/drow_ranger.png',
        'ability': [{'id': 5019, 'image': 'img/dota/spellicons/drow_ranger_frost_arrows.png'},
                    {'id': 5632, 'image': 'img/dota/spellicons/drow_ranger_silence.png'},
                    {'id': 5021, 'image': 'img/dota/spellicons/drow_ranger_trueshot.png'},
                    {'id': 5022, 'image': 'img/dota/spellicons/drow_ranger_marksmanship.png'}]},
    7: {'name': 'Earthshaker',
        'avatar': 'img/dota/heroes/earthshaker.png',
        'ability': [{'id': 5023, 'image': 'img/dota/spellicons/earthshaker_fissure.png'},
                    {'id': 5024, 'image': 'img/dota/spellicons/earthshaker_enchant_totem.png'},
                    {'id': 5025, 'image': 'img/dota/spellicons/earthshaker_aftershock.png'},
                    {'id': 5026, 'image': 'img/dota/spellicons/earthshaker_echo_slam.png'}]},
    8: {'name': 'Juggernaut',
        'avatar': 'img/dota/heroes/juggernaut.png',
        'ability': [{'id': 5028, 'image': 'img/dota/spellicons/juggernaut_blade_fury.png'},
                    {'id': 5029, 'image': 'img/dota/spellicons/juggernaut_healing_ward.png'},
                    {'id': 5027, 'image': 'img/dota/spellicons/juggernaut_blade_dance.png'},
                    {'id': 5030, 'image': 'img/dota/spellicons/juggernaut_omni_slash.png'}]},
    9: {'name': 'Mirana',
        'avatar': 'img/dota/heroes/mirana.png',
        'ability': [{'id': 5051, 'image': 'img/dota/spellicons/mirana_starfall.png'},
                    {'id': 5048, 'image': 'img/dota/spellicons/mirana_arrow.png'},
                    {'id': 5050, 'image': 'img/dota/spellicons/mirana_leap.png'},
                    {'id': 5049, 'image': 'img/dota/spellicons/mirana_invis.png'}]},
    10: {'name': 'Morphling', 'avatar': 'img/dota/heroes/morphling.png'},
    11: {'name': 'Shadow Fiend', 'avatar': 'img/dota/heroes/nevermore.png'},
    12: {'name': 'Phantom Lancer', 'avatar': 'img/dota/heroes/phantom_lancer.png'},
    13: {'name': 'Puck', 'avatar': 'img/dota/heroes/puck.png'},
    14: {'name': 'Pudge',
         'avatar': 'img/dota/heroes/pudge.png',
         'ability': [{'id': 5075, 'image': 'img/dota/spellicons/pudge_meat_hook.png'},
                     {'id': 5076, 'image': 'img/dota/spellicons/pudge_rot.png'},
                     {'id': 5074, 'image': 'img/dota/spellicons/pudge_flesh_heap.png'},
                     {'id': 5077, 'image': 'img/dota/spellicons/pudge_dismember.png'}]},
    15: {'name': 'Razor', 'avatar': 'img/dota/heroes/razor.png'},
    16: {'name': 'Sand King', 'avatar': 'img/dota/heroes/sand_king.png'},
    17: {'name': 'Storm Spirit', 'avatar': 'img/dota/heroes/storm_spirit.png'},
    18: {'name': 'Sven', 'avatar': 'img/dota/heroes/sven.png'},
    19: {'name': 'Tiny', 'avatar': 'img/dota/heroes/tiny.png'},
    20: {'name': 'Vengeful Spirit', 'avatar': 'img/dota/heroes/vengefulspirit.png'},
    21: {'name': 'Windranger',
         'avatar': 'img/dota/heroes/windrunner.png',
         'ability': [{'id': 5130, 'image': 'img/dota/spellicons/windrunner_shackleshot.png'},
                     {'id': 5131, 'image': 'img/dota/spellicons/windrunner_powershot.png'},
                     {'id': 5132, 'image': 'img/dota/spellicons/windrunner_windrun.png'},
                     {'id': 5133, 'image': 'img/dota/spellicons/windrunner_focusfire.png'}]},
    22: {'name': 'Zeus', 'avatar': 'img/dota/heroes/zuus.png'},
    23: {'name': 'Kunkka', 'avatar': 'img/dota/heroes/kunkka.png'},
    25: {'name': 'Lina', 'avatar': 'img/dota/heroes/lina.png'},
    26: {'name': 'Lion', 'avatar': 'img/dota/heroes/lion.png'},
    27: {'name': 'Shadow Shaman',
         'avatar': 'img/dota/heroes/shadow_shaman.png',
         'ability': [{'id': 5078, 'image': 'img/dota/spellicons/shadow_shaman_ether_shock.png'},
                     {'id': 5079, 'image': 'img/dota/spellicons/shadow_shaman_voodoo.png'},
                     {'id': 5080, 'image': 'img/dota/spellicons/shadow_shaman_shackles.png'},
                     {'id': 5081, 'image': 'img/dota/spellicons/shadow_shaman_mass_serpent_ward.png'}]},
    28: {'name': 'Slardar', 'avatar': 'img/dota/heroes/slardar.png'},
    29: {'name': 'Tidehunter', 'avatar': 'img/dota/heroes/tidehunter.png'},
    30: {'name': 'Witch Doctor', 'avatar': 'img/dota/heroes/witch_doctor.png'},
    31: {'name': 'Lich', 'avatar': 'img/dota/heroes/lich.png'},
    32: {'name': 'Riki', 'avatar': 'img/dota/heroes/riki.png'},
    33: {'name': 'Enigma', 'avatar': 'img/dota/heroes/enigma.png'},
    34: {'name': 'Tinker', 'avatar': 'img/dota/heroes/tinker.png'},
    35: {'name': 'Sniper',
         'avatar': 'img/dota/heroes/sniper.png',
         'ability': [{'id': 5154, 'image': 'img/dota/spellicons/sniper_shrapnel.png'},
                     {'id': 5155, 'image': 'img/dota/spellicons/sniper_headshot.png'},
                     {'id': 5156, 'image': 'img/dota/spellicons/sniper_take_aim.png'},
                     {'id': 5157, 'image': 'img/dota/spellicons/sniper_assassinate.png'}]},
    36: {'name': 'Necrophos', 'avatar': 'img/dota/heroes/necrolyte.png'},
    37: {'name': 'Warlock', 'avatar': 'img/dota/heroes/warlock.png'},
    38: {'name': 'Beastmaster', 'avatar': 'img/dota/heroes/beastmaster.png'},
    39: {'name': 'Queen of Pain', 'avatar': 'img/dota/heroes/queenofpain.png'},
    40: {'name': 'Venomancer',
         'avatar': 'img/dota/heroes/venomancer.png',
         'ability': [{'id': 5178, 'image': 'img/dota/spellicons/venomancer_venomous_gale.png'},
                     {'id': 5179, 'image': 'img/dota/spellicons/venomancer_poison_sting.png'},
                     {'id': 5180, 'image': 'img/dota/spellicons/venomancer_plague_ward.png'},
                     {'id': 5181, 'image': 'img/dota/spellicons/venomancer_poison_nova.png'}]},
    41: {'name': 'Faceless Void', 'avatar': 'img/dota/heroes/faceless_void.png'},
    42: {'name': 'Wraith King', 'avatar': 'img/dota/heroes/wraith_king.png'},
    43: {'name': 'Death Prophet',
         'avatar': 'img/dota/heroes/death_prophet.png',
         'ability': [{'id': 5090, 'image': 'img/dota/spellicons/death_prophet_carrion_swarm.png'},
                     {'id': 5091, 'image': 'img/dota/spellicons/death_prophet_silence.png'},
                     {'id': 5092, 'image': 'img/dota/spellicons/death_prophet_witchcraft.png'},
                     {'id': 5093, 'image': 'img/dota/spellicons/death_prophet_exorcism.png'}]},
    44: {'name': 'Phantom Assassin',
         'avatar': 'img/dota/heroes/phantom_assassin.png',
         'ability': [{'id': 5190, 'image': 'img/dota/spellicons/phantom_assassin_stifling_dagger.png'},
                     {'id': 5191, 'image': 'img/dota/spellicons/phantom_assassin_phantom_strike.png'},
                     {'id': 5192, 'image': 'img/dota/spellicons/phantom_assassin_blur.png'},
                     {'id': 5193, 'image': 'img/dota/spellicons/phantom_assassin_coup_de_grace.png'}]},
    45: {'name': 'Pugna', 'avatar': 'img/dota/heroes/pugna.png'},
    46: {'name': 'Templar Assassin', 'avatar': 'img/dota/heroes/templar_assassin.png'},
    47: {'name': 'Viper', 'avatar': 'img/dota/heroes/viper.png'},
    48: {'name': 'Luna',
         'avatar': 'img/dota/heroes/luna.png',
         'ability': [{'id': 5222, 'image': 'img/dota/spellicons/luna_lucent_beam.png'},
                     {'id': 5223, 'image': 'img/dota/spellicons/luna_moon_glaive.png'},
                     {'id': 5224, 'image': 'img/dota/spellicons/luna_lunar_blessing.png'},
                     {'id': 5225, 'image': 'img/dota/spellicons/luna_eclipse.png'}]},
    49: {'name': 'Dragon Knight', 'avatar': 'img/dota/heroes/dragon_knight.png'},
    50: {'name': 'Dazzle', 'avatar': 'img/dota/heroes/dazzle.png'},
    51: {'name': 'Clockwerk',
         'avatar': 'img/dota/heroes/rattletrap.png',
         'ability': [{'id': 5237, 'image': 'img/dota/spellicons/rattletrap_battery_assault.png'},
                     {'id': 5238, 'image': 'img/dota/spellicons/rattletrap_power_cogs.png'},
                     {'id': 5239, 'image': 'img/dota/spellicons/rattletrap_rocket_flare.png'},
                     {'id': 5240, 'image': 'img/dota/spellicons/rattletrap_hookshot.png'}]},
    52: {'name': 'Leshrac', 'avatar': 'img/dota/heroes/leshrac.png'},
    53: {'name': 'Nature\'s Prophet',
         'avatar': 'img/dota/heroes/furion.png',
         'ability': [{'id': 5245, 'image': 'img/dota/spellicons/furion_sprout.png'},
                     {'id': 5246, 'image': 'img/dota/spellicons/furion_teleportation.png'},
                     {'id': 5247, 'image': 'img/dota/spellicons/furion_force_of_nature.png'},
                     {'id': 5248, 'image': 'img/dota/spellicons/furion_wrath_of_nature.png'}]},
    54: {'name': 'Lifestealer', 'avatar': 'img/dota/heroes/life_stealer.png'},
    55: {'name': 'Dark Seer', 'avatar': 'img/dota/heroes/dark_seer.png'},
    56: {'name': 'Clinkz', 'avatar': 'img/dota/heroes/clinkz.png'},
    57: {'name': 'Omniknight', 'avatar': 'img/dota/heroes/omniknight.png'},
    58: {'name': 'Enchantress', 'avatar': 'img/dota/heroes/enchantress.png'},
    59: {'name': 'Huskar', 'avatar': 'img/dota/heroes/huskar.png'},
    60: {'name': 'Night Stalker', 'avatar': 'img/dota/heroes/night_stalker.png'},
    61: {'name': 'Broodmother', 'avatar': 'img/dota/heroes/broodmother.png'},
    62: {'name': 'Bounty Hunter', 'avatar': 'img/dota/heroes/bounty_hunter.png'},
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
    76: {'name': 'Outworld Devourer', 'avatar': 'img/dota/heroes/obsidian_destroyer.png'},
    77: {'name': 'Lycan', 'avatar': 'img/dota/heroes/lycan.png'},
    78: {'name': 'Brewmaster', 'avatar': 'img/dota/heroes/brewmaster.png'},
    79: {'name': 'Shadow Demon', 'avatar': 'img/dota/heroes/shadow_demon.png'},
    80: {'name': 'Lone Druid', 'avatar': 'img/dota/heroes/lone_druid.png'},
    81: {'name': 'Chaos Knight', 'avatar': 'img/dota/heroes/chaos_knight.png'},
    82: {'name': 'Meepo', 'avatar': 'img/dota/heroes/meepo.png'},
    83: {'name': 'Treant Protector', 'avatar': 'img/dota/heroes/treant.png'},
    84: {'name': 'Ogre Magi',
         'avatar': 'img/dota/heroes/ogre_magi.png',
         'ability': [{'id': 5438, 'image': 'img/dota/spellicons/ogre_magi_fireblast.png'},
                     {'id': 5439, 'image': 'img/dota/spellicons/ogre_magi_ignite.png'},
                     {'id': 5440, 'image': 'img/dota/spellicons/ogre_magi_bloodlust.png'},
                     {'id': 5441, 'image': 'img/dota/spellicons/ogre_magi_multicast.png'}]},
    85: {'name': 'Undying', 'avatar': 'img/dota/heroes/undying.png'},
    86: {'name': 'Rubick', 'avatar': 'img/dota/heroes/rubick.png'},
    87: {'name': 'Disruptor', 'avatar': 'img/dota/heroes/disruptor.png'},
    88: {'name': 'Nyx Assassin', 'avatar': 'img/dota/heroes/nyx_assassin.png'},
    89: {'name': 'Naga Siren',
         'avatar': 'img/dota/heroes/naga_siren.png',
         'ability': [{'id': 5467, 'image': 'img/dota/spellicons/naga_siren_mirror_image.png'},
                     {'id': 5468, 'image': 'img/dota/spellicons/naga_siren_ensnare.png'},
                     {'id': 5469, 'image': 'img/dota/spellicons/naga_siren_rip_tide.png'},
                     {'id': 5470, 'image': 'img/dota/spellicons/naga_siren_song_of_the_siren.png'}]},
    90: {'name': 'Keeper of the Light', 'avatar': 'img/dota/heroes/keeper_of_the_light.png'},
    91: {'name': 'Io', 'avatar': 'img/dota/heroes/wisp.png'},
    92: {'name': 'Visage', 'avatar': 'img/dota/heroes/visage.png'},
    93: {'name': 'Slark', 'avatar': 'img/dota/heroes/slark.png'},
    94: {'name': 'Medusa', 'avatar': 'img/dota/heroes/medusa.png'},
    95: {'name': 'Troll Warlord', 'avatar': 'img/dota/heroes/troll_warlord.png'},
    96: {'name': 'Centaur Warrunner', 'avatar': 'img/dota/heroes/centaur.png'},
    97: {'name': 'Magnus', 'avatar': 'img/dota/heroes/magnataur.png'},
    98: {'name': 'Timbersaw',
         'avatar': 'img/dota/heroes/shredder.png',
         'ability': [{'id': 5524, 'image': 'img/dota/spellicons/shredder_whirling_death.png'},
                     {'id': 5525, 'image': 'img/dota/spellicons/shredder_timber_chain.png'},
                     {'id': 5526, 'image': 'img/dota/spellicons/shredder_reactive_armor.png'},
                     {'id': 5527, 'image': 'img/dota/spellicons/shredder_chakram.png'}]},
    99: {'name': 'Bristleback',
         'avatar': 'img/dota/heroes/bristleback.png',
         'ability': [{'id': 5548, 'image': 'img/dota/spellicons/bristleback_viscous_nasal_goo.png'},
                     {'id': 5549, 'image': 'img/dota/spellicons/bristleback_quill_spray.png'},
                     {'id': 5550, 'image': 'img/dota/spellicons/bristleback_bristleback.png'},
                     {'id': 5551, 'image': 'img/dota/spellicons/bristleback_warpath.png'}]},
    100: {'name': 'Tusk',
          'avatar': 'img/dota/heroes/tusk.png',
          'ability': [{'id': 5565, 'image': 'img/dota/spellicons/tusk_ice_shards.png'},
                      {'id': 5566, 'image': 'img/dota/spellicons/tusk_snowball.png'},
                      {'id': 5567, 'image': 'img/dota/spellicons/tusk_frozen_sigil.png'},
                      {'id': 5568, 'image': 'img/dota/spellicons/tusk_walrus_punch.png'}]},
    101: {'name': 'Skywrath Mage',
          'avatar': 'img/dota/heroes/skywrath_mage.png',
          'ability': [{'id': 5581, 'image': 'img/dota/spellicons/skywrath_mage_arcane_bolt.png'},
                      {'id': 5582, 'image': 'img/dota/spellicons/skywrath_mage_concussive_shot.png'},
                      {'id': 5583, 'image': 'img/dota/spellicons/skywrath_mage_ancient_seal.png'},
                      {'id': 5584, 'image': 'img/dota/spellicons/skywrath_mage_mystic_flare.png'}]},
    102: {'name': 'Abaddon',
          'avatar': 'img/dota/heroes/abaddon.png',
          'ability': [{'id': 5585, 'image': 'img/dota/spellicons/abaddon_death_coil.png'},
                      {'id': 5586, 'image': 'img/dota/spellicons/abaddon_aphotic_shield.png'},
                      {'id': 5587, 'image': 'img/dota/spellicons/abaddon_frostmourne.png'},
                      {'id': 5588, 'image': 'img/dota/spellicons/abaddon_borrowed_time.png'}]},
    103: {'name': 'Elder Titan',
          'avatar': 'img/dota/heroes/elder_titan.png',
          'ability': [{'id': 5589, 'image': 'img/dota/spellicons/elder_titan_echo_stomp.png'},
                      {'id': 5591, 'image': 'img/dota/spellicons/elder_titan_ancestral_spirit.png'},
                      {'id': 5593, 'image': 'img/dota/spellicons/elder_titan_natural_order.png'},
                      {'id': 5594, 'image': 'img/dota/spellicons/elder_titan_earth_splitter.png'}]},
    104: {'name': 'Legion Commander',
          'avatar': 'img/dota/heroes/legion_commander.png',
          'ability': [{'id': 5595, 'image': 'img/dota/spellicons/legion_commander_overwhelming_odds.png'},
                      {'id': 5596, 'image': 'img/dota/spellicons/legion_commander_press_the_attack.png'},
                      {'id': 5597, 'image': 'img/dota/spellicons/legion_commander_moment_of_courage.png'},
                      {'id': 5598, 'image': 'img/dota/spellicons/legion_commander_duel.png'}]},
    106: {'name': 'Ember Spirit',
          'avatar': 'img/dota/heroes/ember_spirit.png',
          'ability': [{'id': 5603, 'image': 'img/dota/spellicons/ember_spirit_searing_chains.png'},
                      {'id': 5604, 'image': 'img/dota/spellicons/ember_spirit_sleight_of_fist.png'},
                      {'id': 5605, 'image': 'img/dota/spellicons/ember_spirit_flame_guard.png'},
                      {'id': 5606, 'image': 'img/dota/spellicons/ember_spirit_fire_remnant.png'}]},
    107: {'name': 'Earth Spirit',
          'avatar': 'img/dota/heroes/earth_spirit.png',
          'ability': [{'id': 5608, 'image': 'img/dota/spellicons/earth_spirit_boulder_smash.png'},
                      {'id': 5609, 'image': 'img/dota/spellicons/earth_spirit_rolling_boulder.png'},
                      {'id': 5610, 'image': 'img/dota/spellicons/earth_spirit_geomagnetic_grip.png'},
                      {'id': 5612, 'image': 'img/dota/spellicons/earth_spirit_magnetize.png'}]},
    109: {'name': 'Terrorblade',
          'avatar': 'img/dota/heroes/terrorblade.png',
          'ability': [{'id': 5619, 'image': 'img/dota/spellicons/terrorblade_reflection.png'},
                      {'id': 5620, 'image': 'img/dota/spellicons/terrorblade_conjure_image.png'},
                      {'id': 5621, 'image': 'img/dota/spellicons/terrorblade_metamorphosis.png'},
                      {'id': 5622, 'image': 'img/dota/spellicons/terrorblade_sunder.png'}]},
    110: {'name': 'Phoenix',
          'avatar': 'img/dota/heroes/phoenix.png',
          'ability': [{'id': 5623, 'image': 'img/dota/spellicons/phoenix_icarus_dive.png'},
                      {'id': 5625, 'image': 'img/dota/spellicons/phoenix_fire_spirits.png'},
                      {'id': 5626, 'image': 'img/dota/spellicons/phoenix_sun_ray.png'},
                      {'id': 5630, 'image': 'img/dota/spellicons/phoenix_supernova.png'}]}
}