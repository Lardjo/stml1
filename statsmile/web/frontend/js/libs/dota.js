//
// dota.js -- A Dota 2 Library
//
// Copyright (c) 2014 Statsmile LLC: {Konstantin N.
//
//! version : 1.0.0
//! authors : Statsmile LLC
//! license : MIT
//! statsmile.com

var game_modes = {
    0: {'name': 'Unknown'},
    1: {'name': 'All Pick'},
    2: {'name': 'Captains Mode'},
    3: {'name': 'Random Draft'},
    4: {'name': 'Single Draft'},
    5: {'name': 'All Random'},
    12: {'name': 'Least Played'},
    13: {'name': 'Limited Hero'},
    16: {'name': 'Captains Draft'},
    17: {'name': 'Balanced Draft'},
    18: {'name': 'Ability Draft'},
    7: {'name': 'Event'}, /* Diretide */
    9: {'name': 'Event'}, /* Greeviling */
    15: {'name': 'Event'}, /* Wraith-Night */ /* The Year Beast */
    14: {'name': 'Compendium'} /* TI reserve */
};

var lobbies = {
    0: {'name': 'Public'},
    1: {'name': 'Practice'},
    2: {'name': 'Tournament'},
    3: {'name': 'Tutorial'},
    4: {'name': 'Co-op With Bots'},
    5: {'name': 'Team match'},
    6: {'name': 'Solo Queue'},
    7: {'name': 'Ranked'}
};

var clusters = {
    0: {'name': 'Unknown'},
    111: {'name': 'US West'},
    112: {'name': 'US West'},
    114: {'name': 'US West'},
    121: {'name': 'US East'},
    122: {'name': 'US East'},
    123: {'name': 'US East'},
    124: {'name': 'US East'},
    131: {'name': 'Europe'},
    132: {'name': 'Europe'},
    133: {'name': 'Europe'},
    134: {'name': 'Europe'},
    135: {'name': 'Europe'},
    136: {'name': 'Europe'},
    142: {'name': 'Hong Kong'},
    143: {'name': 'Hong Kong'},
    151: {'name': 'China'},
    152: {'name': 'China'},
    153: {'name': 'China'},
    161: {'name': 'Japan'},
    163: {'name': 'China'},
    171: {'name': 'Australia'},
    191: {'name': 'Europe East'},
    181: {'name': 'Russia'},
    182: {'name': 'Russia'},
    183: {'name': 'Russia'},
    184: {'name': 'Russia'},
    185: {'name': 'Russia'},
    186: {'name': 'Russia'},
    200: {'name': 'South America'},
    204: {'name': 'South America'},
    211: {'name': 'South Africa'},
    212: {'name': 'South Africa'},
    213: {'name': 'South Africa'},
    221: {'name': 'China'},
    222: {'name': 'China'}
};

var abilities = {
    5003: {'name': 'antimage_mana_break'},
    5004: {'name': 'antimage_blink'},
    5005: {'name': 'antimage_spell_shield'},
    5007: {'name': 'axe_berserkers_call'},
    5008: {'name': 'axe_battle_hunger'},
    5009: {'name': 'axe_counter_helix'},
    5010: {'name': 'axe_culling_blade'},
    5012: {'name': 'bane_enfeeble'},
    5011: {'name': 'bane_brain_sap'},
    5014: {'name': 'bane_nightmare'},
    5013: {'name': 'bane_fiends_grip'},
    5015: {'name': 'bloodseeker_bloodrage'},
    5016: {'name': 'bloodseeker_blood_bath'},
    5017: {'name': 'bloodseeker_thirst'},
    5018: {'name': 'bloodseeker_rupture'},
    5126: {'name': 'crystal_maiden_crystal_nova'},
    5127: {'name': 'crystal_maiden_frostbite'},
    5128: {'name': 'crystal_maiden_brilliance_aura'},
    5129: {'name': 'crystal_maiden_freezing_field'},
    5019: {'name': 'drow_ranger_frost_arrows'},
    5020: {'name': 'drow_ranger_silence'},
    5632: {'name': 'drow_ranger_wave_of_silence'},
    5021: {'name': 'drow_ranger_trueshot'},
    5022: {'name': 'drow_ranger_marksmanship'},
    5023: {'name': 'earthshaker_fissure'},
    5024: {'name': 'earthshaker_enchant_totem'},
    5025: {'name': 'earthshaker_aftershock'},
    5026: {'name': 'earthshaker_echo_slam'},
    5028: {'name': 'juggernaut_blade_fury'},
    5029: {'name': 'juggernaut_healing_ward'},
    5027: {'name': 'juggernaut_blade_dance'},
    5030: {'name': 'juggernaut_omni_slash'},
    5051: {'name': 'mirana_starfall'},
    5048: {'name': 'mirana_arrow'},
    5050: {'name': 'mirana_leap'},
    5049: {'name': 'mirana_invis'},
    5052: {'name': 'morphling_waveform'},
    5053: {'name': 'morphling_adaptive_strike'},
    5055: {'name': 'morphling_morph_agi'},
    5056: {'name': 'morphling_morph_str'},
    5057: {'name': 'morphling_replicate'},
    5059: {'name': 'nevermore_shadowraze1'},
    5060: {'name': 'nevermore_shadowraze2'},
    5061: {'name': 'nevermore_shadowraze3'},
    5062: {'name': 'nevermore_necromastery'},
    5063: {'name': 'nevermore_dark_lord'},
    5064: {'name': 'nevermore_requiem'},
    5065: {'name': 'phantom_lancer_spirit_lance'},
    5066: {'name': 'phantom_lancer_doppelwalk'},
    5067: {'name': 'phantom_lancer_juxtapose'},
    5068: {'name': 'phantom_lancer_phantom_edge'},
    5069: {'name': 'puck_illusory_orb'},
    5071: {'name': 'puck_waning_rift'},
    5072: {'name': 'puck_phase_shift'},
    5073: {'name': 'puck_dream_coil'},
    5075: {'name': 'pudge_meat_hook'},
    5076: {'name': 'pudge_rot'},
    5074: {'name': 'pudge_flesh_heap'},
    5077: {'name': 'pudge_dismember'},
    5082: {'name': 'razor_plasma_field'},
    5083: {'name': 'razor_static_link'},
    5084: {'name': 'razor_unstable_current'},
    5085: {'name': 'razor_eye_of_the_storm'},
    5102: {'name': 'sandking_burrowstrike'},
    5103: {'name': 'sandking_sand_storm'},
    5104: {'name': 'sandking_caustic_finale'},
    5105: {'name': 'sandking_epicenter'},
    5098: {'name': 'storm_spirit_static_remnant'},
    5099: {'name': 'storm_spirit_electric_vortex'},
    5100: {'name': 'storm_spirit_overload'},
    5101: {'name': 'storm_spirit_ball_lightning'},
    5094: {'name': 'sven_storm_bolt'},
    5095: {'name': 'sven_great_cleave'},
    5096: {'name': 'sven_warcry'},
    5097: {'name': 'sven_gods_strength'},
    5106: {'name': 'tiny_avalanche'},
    5107: {'name': 'tiny_toss'},
    5108: {'name': 'tiny_craggy_exterior'},
    5109: {'name': 'tiny_grow'},
    5122: {'name': 'vengefulspirit_magic_missile'},
    5124: {'name': 'vengefulspirit_wave_of_terror'},
    5123: {'name': 'vengefulspirit_command_aura'},
    5125: {'name': 'vengefulspirit_nether_swap'},
    5130: {'name': 'windrunner_shackleshot'},
    5131: {'name': 'windrunner_powershot'},
    5132: {'name': 'windrunner_windrun'},
    5133: {'name': 'windrunner_focusfire'},
    5110: {'name': 'zuus_arc_lightning'},
    5111: {'name': 'zuus_lightning_bolt'},
    5112: {'name': 'zuus_static_field'},
    5113: {'name': 'zuus_thundergods_wrath'},
    5031: {'name': 'kunkka_torrent'},
    5032: {'name': 'kunkka_tidebringer'},
    5033: {'name': 'kunkka_x_marks_the_spot'},
    5035: {'name': 'kunkka_ghostship'},
    5040: {'name': 'lina_dragon_slave'},
    5041: {'name': 'lina_light_strike_array'},
    5042: {'name': 'lina_fiery_soul'},
    5043: {'name': 'lina_laguna_blade'},
    5044: {'name': 'lion_impale'},
    5045: {'name': 'lion_voodoo'},
    5046: {'name': 'lion_mana_drain'},
    5047: {'name': 'lion_finger_of_death'},
    5078: {'name': 'shadow_shaman_ether_shock'},
    5079: {'name': 'shadow_shaman_voodoo'},
    5080: {'name': 'shadow_shaman_shackles'},
    5081: {'name': 'shadow_shaman_mass_serpent_ward'},
    5114: {'name': 'slardar_sprint'},
    5115: {'name': 'slardar_slithereen_crush'},
    5116: {'name': 'slardar_bash'},
    5117: {'name': 'slardar_amplify_damage'},
    5118: {'name': 'tidehunter_gush'},
    5119: {'name': 'tidehunter_kraken_shell'},
    5120: {'name': 'tidehunter_anchor_smash'},
    5121: {'name': 'tidehunter_ravage'},
    5138: {'name': 'witch_doctor_paralyzing_cask'},
    5139: {'name': 'witch_doctor_voodoo_restoration'},
    5140: {'name': 'witch_doctor_maledict'},
    5141: {'name': 'witch_doctor_death_ward'},
    5134: {'name': 'lich_frost_nova'},
    5135: {'name': 'lich_frost_armor'},
    5136: {'name': 'lich_dark_ritual'},
    5137: {'name': 'lich_chain_frost'},
    5142: {'name': 'riki_smoke_screen'},
    5143: {'name': 'riki_blink_strike'},
    5144: {'name': 'riki_backstab'},
    5145: {'name': 'riki_permanent_invisibility'},
    5146: {'name': 'enigma_malefice'},
    5147: {'name': 'enigma_demonic_conversion'},
    5148: {'name': 'enigma_midnight_pulse'},
    5149: {'name': 'enigma_black_hole'},
    5150: {'name': 'tinker_laser'},
    5151: {'name': 'tinker_heat_seeking_missile'},
    5152: {'name': 'tinker_march_of_the_machines'},
    5153: {'name': 'tinker_rearm'},
    5154: {'name': 'sniper_shrapnel'},
    5155: {'name': 'sniper_headshot'},
    5156: {'name': 'sniper_take_aim'},
    5157: {'name': 'sniper_assassinate'},
    5158: {'name': 'necrolyte_death_pulse'},
    5159: {'name': 'necrolyte_heartstopper_aura'},
    5160: {'name': 'necrolyte_sadist'},
    5161: {'name': 'necrolyte_reapers_scythe'},
    5162: {'name': 'warlock_fatal_bonds'},
    5163: {'name': 'warlock_shadow_word'},
    5164: {'name': 'warlock_upheaval'},
    5165: {'name': 'warlock_rain_of_chaos'},
    5168: {'name': 'beastmaster_wild_axes'},
    5169: {'name': 'beastmaster_call_of_the_wild'},
    5172: {'name': 'beastmaster_inner_beast'},
    5177: {'name': 'beastmaster_primal_roar'},
    5173: {'name': 'queenofpain_shadow_strike'},
    5174: {'name': 'queenofpain_blink'},
    5175: {'name': 'queenofpain_scream_of_pain'},
    5176: {'name': 'queenofpain_sonic_wave'},
    5178: {'name': 'venomancer_venomous_gale'},
    5179: {'name': 'venomancer_poison_sting'},
    5180: {'name': 'venomancer_plague_ward'},
    5181: {'name': 'venomancer_poison_nova'},
    5182: {'name': 'faceless_void_time_walk'},
    5183: {'name': 'faceless_void_backtrack'},
    5184: {'name': 'faceless_void_time_lock'},
    5185: {'name': 'faceless_void_chronosphere'},
    5086: {'name': 'skeleton_king_hellfire_blast'},
    5087: {'name': 'skeleton_king_vampiric_aura'},
    5088: {'name': 'skeleton_king_mortal_strike'},
    5089: {'name': 'skeleton_king_reincarnation'},
    5090: {'name': 'death_prophet_carrion_swarm'},
    5091: {'name': 'death_prophet_silence'},
    5092: {'name': 'death_prophet_witchcraft'},
    5093: {'name': 'death_prophet_exorcism'},
    5190: {'name': 'phantom_assassin_stifling_dagger'},
    5191: {'name': 'phantom_assassin_phantom_strike'},
    5192: {'name': 'phantom_assassin_blur'},
    5193: {'name': 'phantom_assassin_coup_de_grace'},
    5186: {'name': 'pugna_nether_blast'},
    5187: {'name': 'pugna_decrepify'},
    5188: {'name': 'pugna_nether_ward'},
    5189: {'name': 'pugna_life_drain'},
    5194: {'name': 'templar_assassin_refraction'},
    5195: {'name': 'templar_assassin_meld'},
    5196: {'name': 'templar_assassin_psi_blades'},
    5197: {'name': 'templar_assassin_psionic_trap'},
    5218: {'name': 'viper_poison_attack'},
    5219: {'name': 'viper_nethertoxin'},
    5220: {'name': 'viper_corrosive_skin'},
    5221: {'name': 'viper_viper_strike'},
    5222: {'name': 'luna_lucent_beam'},
    5223: {'name': 'luna_moon_glaive'},
    5224: {'name': 'luna_lunar_blessing'},
    5225: {'name': 'luna_eclipse'},
    5226: {'name': 'dragon_knight_breathe_fire'},
    5227: {'name': 'dragon_knight_dragon_tail'},
    5228: {'name': 'dragon_knight_dragon_blood'},
    5229: {'name': 'dragon_knight_elder_dragon_form'},
    5233: {'name': 'dazzle_poison_touch'},
    5234: {'name': 'dazzle_shallow_grave'},
    5235: {'name': 'dazzle_shadow_wave'},
    5236: {'name': 'dazzle_weave'},
    5237: {'name': 'rattletrap_battery_assault'},
    5238: {'name': 'rattletrap_power_cogs'},
    5239: {'name': 'rattletrap_rocket_flare'},
    5240: {'name': 'rattletrap_hookshot'},
    5241: {'name': 'leshrac_split_earth'},
    5242: {'name': 'leshrac_diabolic_edict'},
    5243: {'name': 'leshrac_lightning_storm'},
    5244: {'name': 'leshrac_pulse_nova'},
    5245: {'name': 'furion_sprout'},
    5246: {'name': 'furion_teleportation'},
    5247: {'name': 'furion_force_of_nature'},
    5248: {'name': 'furion_wrath_of_nature'},
    5249: {'name': 'life_stealer_rage'},
    5250: {'name': 'life_stealer_feast'},
    5251: {'name': 'life_stealer_open_wounds'},
    5252: {'name': 'life_stealer_infest'},
    5253: {'name': 'life_stealer_consume'},
    5255: {'name': 'dark_seer_vacuum'},
    5256: {'name': 'dark_seer_ion_shell'},
    5257: {'name': 'dark_seer_surge'},
    5258: {'name': 'dark_seer_wall_of_replica'},
    5259: {'name': 'clinkz_strafe'},
    5260: {'name': 'clinkz_searing_arrows'},
    5261: {'name': 'clinkz_wind_walk'},
    5262: {'name': 'clinkz_death_pact'},
    5263: {'name': 'omniknight_purification'},
    5264: {'name': 'omniknight_repel'},
    5265: {'name': 'omniknight_degen_aura'},
    5266: {'name': 'omniknight_guardian_angel'},
    5267: {'name': 'enchantress_untouchable'},
    5268: {'name': 'enchantress_enchant'},
    5269: {'name': 'enchantress_natures_attendants'},
    5270: {'name': 'enchantress_impetus'},
    5271: {'name': 'huskar_inner_vitality'},
    5272: {'name': 'huskar_burning_spear'},
    5273: {'name': 'huskar_berserkers_blood'},
    5274: {'name': 'huskar_life_break'},
    5275: {'name': 'night_stalker_void'},
    5276: {'name': 'night_stalker_crippling_fear'},
    5277: {'name': 'night_stalker_hunter_in_the_night'},
    5278: {'name': 'night_stalker_darkness'},
    5279: {'name': 'broodmother_spawn_spiderlings'},
    5280: {'name': 'broodmother_spin_web'},
    5281: {'name': 'broodmother_incapacitating_bite'},
    5282: {'name': 'broodmother_insatiable_hunger'},
    5285: {'name': 'bounty_hunter_shuriken_toss'},
    5286: {'name': 'bounty_hunter_jinada'},
    5287: {'name': 'bounty_hunter_wind_walk'},
    5288: {'name': 'bounty_hunter_track'},
    5289: {'name': 'weaver_the_swarm'},
    5290: {'name': 'weaver_shukuchi'},
    5291: {'name': 'weaver_geminate_attack'},
    5292: {'name': 'weaver_time_lapse'},
    5297: {'name': 'jakiro_dual_breath'},
    5298: {'name': 'jakiro_ice_path'},
    5299: {'name': 'jakiro_liquid_fire'},
    5300: {'name': 'jakiro_macropyre'},
    5320: {'name': 'batrider_sticky_napalm'},
    5321: {'name': 'batrider_flamebreak'},
    5322: {'name': 'batrider_firefly'},
    5323: {'name': 'batrider_flaming_lasso'},
    5328: {'name': 'chen_penitence'},
    5329: {'name': 'chen_test_of_faith'},
    5522: {'name': 'chen_test_of_faith_teleport'},
    5330: {'name': 'chen_holy_persuasion'},
    5331: {'name': 'chen_hand_of_god'},
    5334: {'name': 'spectre_spectral_dagger'},
    5335: {'name': 'spectre_desolate'},
    5336: {'name': 'spectre_dispersion'},
    5337: {'name': 'spectre_haunt'},
    5345: {'name': 'ancient_apparition_cold_feet'},
    5346: {'name': 'ancient_apparition_ice_vortex'},
    5347: {'name': 'ancient_apparition_chilling_touch'},
    5348: {'name': 'ancient_apparition_ice_blast'},
    5339: {'name': 'doom_bringer_devour'},
    5340: {'name': 'doom_bringer_scorched_earth'},
    5341: {'name': 'doom_bringer_lvl_death'},
    5342: {'name': 'doom_bringer_doom'},
    5357: {'name': 'ursa_earthshock'},
    5358: {'name': 'ursa_overpower'},
    5359: {'name': 'ursa_fury_swipes'},
    5360: {'name': 'ursa_enrage'},
    5353: {'name': 'spirit_breaker_charge_of_darkness'},
    5354: {'name': 'spirit_breaker_empowering_haste'},
    5355: {'name': 'spirit_breaker_greater_bash'},
    5356: {'name': 'spirit_breaker_nether_strike'},
    5361: {'name': 'gyrocopter_rocket_barrage'},
    5362: {'name': 'gyrocopter_homing_missile'},
    5363: {'name': 'gyrocopter_flak_cannon'},
    5364: {'name': 'gyrocopter_call_down'},
    5365: {'name': 'alchemist_acid_spray'},
    5366: {'name': 'alchemist_unstable_concoction'},
    5368: {'name': 'alchemist_goblins_greed'},
    5369: {'name': 'alchemist_chemical_rage'},
    5370: {'name': 'invoker_quas'},
    5371: {'name': 'invoker_wex'},
    5372: {'name': 'invoker_exort'},
    5375: {'name': 'invoker_invoke'},
    5377: {'name': 'silencer_curse_of_the_silent'},
    5378: {'name': 'silencer_glaives_of_wisdom'},
    5379: {'name': 'silencer_last_word'},
    5380: {'name': 'silencer_global_silence'},
    5391: {'name': 'obsidian_destroyer_arcane_orb'},
    5392: {'name': 'obsidian_destroyer_astral_imprisonment'},
    5393: {'name': 'obsidian_destroyer_essence_aura'},
    5394: {'name': 'obsidian_destroyer_sanity_eclipse'},
    5395: {'name': 'lycan_summon_wolves'},
    5396: {'name': 'lycan_howl'},
    5397: {'name': 'lycan_feral_impulse'},
    5398: {'name': 'lycan_shapeshift'},
    5400: {'name': 'brewmaster_thunder_clap'},
    5401: {'name': 'brewmaster_drunken_haze'},
    5402: {'name': 'brewmaster_drunken_brawler'},
    5403: {'name': 'brewmaster_primal_split'},
    5421: {'name': 'shadow_demon_disruption'},
    5422: {'name': 'shadow_demon_soul_catcher'},
    5423: {'name': 'shadow_demon_shadow_poison'},
    5424: {'name': 'shadow_demon_shadow_poison_release'},
    5425: {'name': 'shadow_demon_demonic_purge'},
    5412: {'name': 'lone_druid_spirit_bear'},
    5413: {'name': 'lone_druid_rabid'},
    5414: {'name': 'lone_druid_synergy'},
    5415: {'name': 'lone_druid_true_form'},
    5416: {'name': 'lone_druid_true_form_druid'},
    5426: {'name': 'chaos_knight_chaos_bolt'},
    5427: {'name': 'chaos_knight_reality_rift'},
    5428: {'name': 'chaos_knight_chaos_strike'},
    5429: {'name': 'chaos_knight_phantasm'},
    5430: {'name': 'meepo_earthbind'},
    5431: {'name': 'meepo_poof'},
    5432: {'name': 'meepo_geostrike'},
    5433: {'name': 'meepo_divided_we_stand'},
    5434: {'name': 'treant_natures_guise'},
    5435: {'name': 'treant_leech_seed'},
    5436: {'name': 'treant_living_armor'},
    5437: {'name': 'treant_overgrowth'},
    5438: {'name': 'ogre_magi_fireblast'},
    5439: {'name': 'ogre_magi_ignite'},
    5440: {'name': 'ogre_magi_bloodlust'},
    5441: {'name': 'ogre_magi_multicast'},
    5442: {'name': 'undying_decay'},
    5443: {'name': 'undying_soul_rip'},
    5444: {'name': 'undying_tombstone'},
    5447: {'name': 'undying_flesh_golem'},
    5448: {'name': 'rubick_telekinesis'},
    5450: {'name': 'rubick_fade_bolt'},
    5451: {'name': 'rubick_null_field'},
    5452: {'name': 'rubick_spell_steal'},
    5458: {'name': 'disruptor_thunder_strike'},
    5459: {'name': 'disruptor_glimpse'},
    5460: {'name': 'disruptor_kinetic_field'},
    5461: {'name': 'disruptor_static_storm'},
    5462: {'name': 'nyx_assassin_impale'},
    5463: {'name': 'nyx_assassin_mana_burn'},
    5464: {'name': 'nyx_assassin_spiked_carapace'},
    5465: {'name': 'nyx_assassin_vendetta'},
    5467: {'name': 'naga_siren_mirror_image'},
    5468: {'name': 'naga_siren_ensnare'},
    5469: {'name': 'naga_siren_rip_tide'},
    5470: {'name': 'naga_siren_song_of_the_siren'},
    5471: {'name': 'keeper_of_the_light_illuminate'},
    5472: {'name': 'keeper_of_the_light_mana_leak'},
    5473: {'name': 'keeper_of_the_light_chakra_magic'},
    5474: {'name': 'keeper_of_the_light_spirit_form'},
    5479: {'name': 'keeper_of_the_light_spirit_form_illuminate'},
    5485: {'name': 'wisp_tether'},
    5486: {'name': 'wisp_spirits'},
    5487: {'name': 'wisp_overcharge'},
    5488: {'name': 'wisp_relocate'},
    5480: {'name': 'visage_grave_chill'},
    5481: {'name': 'visage_soul_assumption'},
    5482: {'name': 'visage_gravekeepers_cloak'},
    5483: {'name': 'visage_summon_familiars'},
    5494: {'name': 'slark_dark_pact'},
    5495: {'name': 'slark_pounce'},
    5496: {'name': 'slark_essence_shift'},
    5497: {'name': 'slark_shadow_dance'},
    5504: {'name': 'medusa_split_shot'},
    5505: {'name': 'medusa_mystic_snake'},
    5506: {'name': 'medusa_mana_shield'},
    5507: {'name': 'medusa_stone_gaze'},
    5508: {'name': 'troll_warlord_berserkers_rage'},
    5509: {'name': 'troll_warlord_whirling_axes_ranged'},
    5510: {'name': 'troll_warlord_whirling_axes_melee'},
    5511: {'name': 'troll_warlord_fervor'},
    5512: {'name': 'troll_warlord_battle_trance'},
    5514: {'name': 'centaur_hoof_stomp'},
    5515: {'name': 'centaur_double_edge'},
    5516: {'name': 'centaur_return'},
    5517: {'name': 'centaur_stampede'},
    5518: {'name': 'magnataur_shockwave'},
    5519: {'name': 'magnataur_empower'},
    5520: {'name': 'magnataur_skewer'},
    5521: {'name': 'magnataur_reverse_polarity'},
    5524: {'name': 'shredder_whirling_death'},
    5525: {'name': 'shredder_timber_chain'},
    5526: {'name': 'shredder_reactive_armor'},
    5527: {'name': 'shredder_chakram'},
    5548: {'name': 'bristleback_viscous_nasal_goo'},
    5549: {'name': 'bristleback_quill_spray'},
    5550: {'name': 'bristleback_bristleback'},
    5551: {'name': 'bristleback_warpath'},
    5565: {'name': 'tusk_ice_shards'},
    5566: {'name': 'tusk_snowball'},
    5567: {'name': 'tusk_frozen_sigil'},
    5568: {'name': 'tusk_walrus_punch'},
    5581: {'name': 'skywrath_mage_arcane_bolt'},
    5582: {'name': 'skywrath_mage_concussive_shot'},
    5583: {'name': 'skywrath_mage_ancient_seal'},
    5584: {'name': 'skywrath_mage_mystic_flare'},
    5585: {'name': 'abaddon_death_coil'},
    5586: {'name': 'abaddon_aphotic_shield'},
    5587: {'name': 'abaddon_frostmourne'},
    5588: {'name': 'abaddon_borrowed_time'},
    5589: {'name': 'elder_titan_echo_stomp'},
    5591: {'name': 'elder_titan_ancestral_spirit'},
    5593: {'name': 'elder_titan_natural_order'},
    5594: {'name': 'elder_titan_earth_splitter'},
    5595: {'name': 'legion_commander_overwhelming_odds'},
    5596: {'name': 'legion_commander_press_the_attack'},
    5597: {'name': 'legion_commander_moment_of_courage'},
    5598: {'name': 'legion_commander_duel'},
    5603: {'name': 'ember_spirit_searing_chains'},
    5604: {'name': 'ember_spirit_sleight_of_fist'},
    5605: {'name': 'ember_spirit_flame_guard'},
    5606: {'name': 'ember_spirit_fire_remnant'},
    5608: {'name': 'earth_spirit_boulder_smash'},
    5609: {'name': 'earth_spirit_rolling_boulder'},
    5610: {'name': 'earth_spirit_geomagnetic_grip'},
    5612: {'name': 'earth_spirit_magnetize'},
    5619: {'name': 'terrorblade_reflection'},
    5620: {'name': 'terrorblade_conjure_image'},
    5621: {'name': 'terrorblade_metamorphosis'},
    5622: {'name': 'terrorblade_sunder'},
    5623: {'name': 'phoenix_icarus_dive'},
    5625: {'name': 'phoenix_fire_spirits'},
    5626: {'name': 'phoenix_sun_ray'},
    5630: {'name': 'phoenix_supernova'}
};

var items = {
    0: {'name': 'No item', 'avatar': 'default'},
    1: {'name': 'Blink Dagger', 'avatar': 'blink'},
    2: {'name': 'Blades of Attack', 'avatar': 'blades_of_attack'},
    3: {'name': 'Broadsword', 'avatar': 'broadsword'},
    4: {'name': 'Chainmail', 'avatar': 'chainmail'},
    5: {'name': 'Claymore', 'avatar': 'claymore'},
    6: {'name': 'Helm of Iron Will', 'avatar': 'helm_of_iron_will'},
    7: {'name': 'Javelin', 'avatar': 'javelin'},
    8: {'name': 'Mithril Hammer', 'avatar': 'mithril_hammer'},
    9: {'name': 'Platemail', 'avatar': 'platemail'},
    10: {'name': 'Quarterstaff', 'avatar': 'quarterstaff'},
    11: {'name': 'Quelling Blade', 'avatar': 'quelling_blade'},
    12: {'name': 'Ring of Protection', 'avatar': 'ring_of_protection'},
    13: {'name': 'Gauntlets of Strength', 'avatar': 'gauntlets_of_strength'},
    14: {'name': 'Slippers of Agility', 'avatar': 'slippers_of_agility'},
    15: {'name': 'Mantle of Intelligence', 'avatar': 'mantle_of_intelligence'},
    16: {'name': 'Iron Branch', 'avatar': 'iron_branch'},
    17: {'name': 'Belt of Strength', 'avatar': 'belt_of_strength'},
    18: {'name': 'Band of Elvenskin', 'avatar': 'band_of_elvenskin'},
    19: {'name': 'Robe of the Magi', 'avatar': 'robe_of_the_magi'},
    20: {'name': 'Circlet', 'avatar': 'circlet'},
    21: {'name': 'Ogre Club', 'avatar': 'ogre_club'},
    22: {'name': 'Blade of Alacrity', 'avatar': 'blade_of_alacrity'},
    23: {'name': 'Staff of Wizardry', 'avatar': 'staff_of_wizardry'},
    24: {'name': 'Ultimate Orb', 'avatar': 'ultimate_orb'},
    25: {'name': 'Gloves of Haste', 'avatar': 'gloves_of_haste'},
    26: {'name': 'Morbid Mask', 'avatar': 'morbid_mask'},
    27: {'name': 'Ring of Regen', 'avatar': 'ring_of_regen'},
    28: {'name': 'Sage\'s Mask', 'avatar': 'sages_mask'},
    29: {'name': 'Boots of Speed', 'avatar': 'boots_of_speed'},
    30: {'name': 'Gem of True Sight', 'avatar': 'gem_of_true_sight'},
    31: {'name': 'Cloak', 'avatar': 'cloak'},
    32: {'name': 'Talisman of Evasion', 'avatar': 'talisman_of_evasion'},
    33: {'name': 'Cheese', 'avatar': 'cheese'},
    34: {'name': 'Magic Stick', 'avatar': 'magic_stick'},
    35: {'name': 'Recipe: Magic Wand', 'avatar': 'recipe_scroll'},
    36: {'name': 'Magic Wand', 'avatar': 'magic_wand'},
    37: {'name': 'Ghost Scepter', 'avatar': 'ghost_scepter'},
    38: {'name': 'Clarity', 'avatar': 'clarity'},
    39: {'name': 'Healing Salve', 'avatar': 'healing_salve'},
    40: {'name': 'Dust of Appearance', 'avatar': 'dust_of_appearance'},
    41: {'name': 'Bottle', 'avatar': 'bottle'},
    42: {'name': 'Observer Ward', 'avatar': 'observer_ward'},
    43: {'name': 'Sentry Ward', 'avatar': 'sentry_ward'},
    44: {'name': 'Tango', 'avatar': 'tango'},
    45: {'name': 'Courier', 'avatar': 'courier'},
    46: {'name': 'Teleport Scroll', 'avatar': 'town_portal_scroll'},
    48: {'name': 'Travel Boots', 'avatar': 'boots_of_travel'},
    50: {'name': 'Phase Boots', 'avatar': 'phase_boots'},
    51: {'name': 'Demon Edge', 'avatar': 'demon_edge'},
    52: {'name': 'Eaglesong', 'avatar': 'eaglesong'},
    53: {'name': 'Reaver', 'avatar': 'reaver'},
    54: {'name': 'Sacred Relic', 'avatar': 'sacred_relic'},
    55: {'name': 'Hyperstone', 'avatar': 'hyperstone'},
    56: {'name': 'Ring of Health', 'avatar': 'ring_of_health'},
    57: {'name': 'Void Stone', 'avatar': 'void_stone'},
    58: {'name': 'Mystic Staff', 'avatar': 'mystic_staff'},
    59: {'name': 'Energy Booster', 'avatar': 'energy_booster'},
    60: {'name': 'Point Booster', 'avatar': 'point_booster'},
    61: {'name': 'Vitality Booster', 'avatar': 'vitality_booster'},
    63: {'name': 'Power Treads', 'avatar': 'power_treads'},
    65: {'name': 'Hand of Midas', 'avatar': 'hand_of_midas'},
    67: {'name': 'Oblivion Staff', 'avatar': 'oblivion_staff'},
    69: {'name': 'Perseverance', 'avatar': 'pers'},
    71: {'name': 'Poor Man\'s Shield', 'avatar': 'poor_mans_shield'},
    73: {'name': 'Bracer', 'avatar': 'bracer'},
    75: {'name': 'Wraith Band', 'avatar': 'wraith_band'},
    77: {'name': 'Null Talisman', 'avatar': 'null_talisman'},
    79: {'name': 'Mekansm', 'avatar': 'mekansm'},
    81: {'name': 'Vladmir\'s Offering', 'avatar': 'vladmirs_offering'},
    86: {'name': 'Buckler', 'avatar': 'buckler'},
    88: {'name': 'Ring of Basilius', 'avatar': 'ring_of_basilius'},
    90: {'name': 'Pipe of Insight', 'avatar': 'pipe'},
    92: {'name': 'Urn of Shadows', 'avatar': 'urn_of_shadows'},
    94: {'name': 'Headdress', 'avatar': 'headdress'},
    96: {'name': 'Scythe of Vyse', 'avatar': 'scythe_of_vyse'},
    98: {'name': 'Orchid Malevolence', 'avatar': 'orchid_malevolence'},
    100: {'name': 'Euls Scepter of Divinity', 'avatar': 'cyclone'},
    102: {'name': 'Force Staff', 'avatar': 'force_staff'},
    104: {'name': 'Dagon: Level 1', 'avatar': 'dagon_1'},
    108: {'name': 'Aghanim\'s Scepter', 'avatar': 'ultimate_scepter'},
    110: {'name': 'Refresher Orb', 'avatar': 'refresher'},
    112: {'name': 'Assault Cuirass', 'avatar': 'assault_cuirass'},
    114: {'name': 'Heart of Tarrasque', 'avatar': 'heart_of_tarrasque'},
    117: {'name': 'Aegis', 'avatar': 'aegis'},
    119: {'name': 'Shiva\'s Guard', 'avatar': 'shivas_guard'},
    116: {'name': 'Black King Bar', 'avatar': 'black_king_bar'},
    121: {'name': 'Bloodstone', 'avatar': 'bloodstone'},
    122: {'name': 'Recipe: Linken\'s Sphere', 'avatar': 'recipe_scroll'},
    123: {'name': 'Linken\'s Sphere', 'avatar': 'linkens_sphere'},
    125: {'name': 'Vanguard', 'avatar': 'vanguard'},
    127: {'name': 'Blade Mail', 'avatar': 'blade_mail'},
    131: {'name': 'Hood of Defiance', 'avatar': 'hood_of_defiance'},
    133: {'name': 'Divine Rapier', 'avatar': 'divine_rapier'},
    135: {'name': 'Monkey King Bar', 'avatar': 'monkey_king_bar'},
    137: {'name': 'Radiance', 'avatar': 'radiance'},
    139: {'name': 'Butterfly', 'avatar': 'butterfly'},
    140: {'name': 'Recipe: Daedalus', 'avatar': 'recipe_scroll'},
    141: {'name': 'Daedalus', 'avatar': 'daedalus'},
    143: {'name': 'Basher', 'avatar': 'skull_basher'},
    145: {'name': 'Battlefury', 'avatar': 'battle_fury'},
    147: {'name': 'Manta', 'avatar': 'manta_style'},
    149: {'name': 'Crystalys', 'avatar': 'crystalys'},
    151: {'name': 'Armlet of Mordiggian', 'avatar': 'armlet'},
    152: {'name': 'Shadow Blade', 'avatar': 'shadow_blade'},
    154: {'name': 'Sange and Yasha', 'avatar': 'sange_and_yasha'},
    156: {'name': 'Satanic', 'avatar': 'satanic'},
    158: {'name': 'Mjollnir', 'avatar': 'mjollnir'},
    160: {'name': 'Eye of Skadi', 'avatar': 'eye_of_skadi'},
    162: {'name': 'Sange', 'avatar': 'sange'},
    164: {'name': 'Helm of the Dominator', 'avatar': 'helm_of_the_dominator'},
    166: {'name': 'Maelstrom', 'avatar': 'maelstrom'},
    167: {'name': 'Recipe: Desolator', 'avatar': 'recipe_scroll'},
    168: {'name': 'Desolator', 'avatar': 'desolator'},
    170: {'name': 'Yasha', 'avatar': 'yasha'},
    172: {'name': 'Mask of Madness', 'avatar': 'mask_of_madness'},
    174: {'name': 'Diffusal Blade: Level 1', 'avatar': 'diffusal_blade_1'},
    176: {'name': 'Ethereal Blade', 'avatar': 'ethereal_blade'},
    178: {'name': 'Soul Ring', 'avatar': 'soul_ring'},
    180: {'name': 'Arcane Boots', 'avatar': 'arcane_boots'},
    181: {'name': 'Orb of Venom', 'avatar': 'orb_of_venom'},
    182: {'name': 'Stout Shield', 'avatar': 'stout_shield'},
    185: {'name': 'Drum of Endurance', 'avatar': 'drum_of_endurance'},
    187: {'name': 'Medallion of Courage', 'avatar': 'medallion_of_courage'},
    188: {'name': 'Smoke of Deceit', 'avatar': 'smoke_of_deceit'},
    190: {'name': 'Veil of Discord', 'avatar': 'veil_of_discord'},
    193: {'name': 'Necronomicon: Level 2', 'avatar': 'necronomicon_2'},
    194: {'name': 'Necronomicon', 'avatar': 'necronomicon'},
    196: {'name': 'Diffusal Blade: Level 2', 'avatar': 'diffusal_blade'},
    201: {'name': 'Dagon: Level 2', 'avatar': 'dagon_2'},
    202: {'name': 'Dagon: Level 3', 'avatar': 'dagon_3'},
    203: {'name': 'Dagon: Level 4', 'avatar': 'dagon_4'},
    204: {'name': 'Dagon: Level 5', 'avatar': 'dagon'},
    206: {'name': 'Rod of Atos', 'avatar': 'rod_of_atos'},
    208: {'name': 'Abyssal Blade', 'avatar': 'abyssal_blade'},
    210: {'name': 'Heaven\'s Halberd', 'avatar': 'heavens_halberd'},
    212: {'name': 'Ring of Aquila', 'avatar': 'ring_of_aquila'},
    214: {'name': 'Tranquil Boots', 'avatar': 'tranquil_boots'},
    215: {'name': 'Shadow Amulet', 'avatar': 'shadow_amulet'},
    229: {'name': 'Xmas Stocking', 'avatar': 'xmas_stocking'},
    230: {'name': 'Speed Skates', 'avatar': 'speed_skates'},
    231: {'name': 'Fruit-bit Cake', 'avatar': 'fruit-bit_cake'},
    232: {'name': 'Wizard Cookie', 'avatar': 'wizard_cookie'},
    233: {'name': 'Cocoa with Marshmallows', 'avatar': 'cocoa'},
    234: {'name': 'Clove Studded Ham', 'avatar': 'clove_studded_ham'},
    235: {'name': 'Greevil Whistle', 'avatar': 'greevil_whistle'},
    236: {'name': 'Kringle', 'avatar': 'kringle'},
    240: {'name': 'Firecrackers', 'avatar': 'firecrackers'},
    241: {'name': 'Shared Tango', 'avatar': 'tango_single'},
    250: {'name': 'Force Boots', 'avatar': 'force_boots'}
};

var heroes = {
    1: {'name': 'Anti-Mage', 'avatar': 'antimage'},
    2: {'name': 'Axe', 'avatar': 'axe'},
    3: {'name': 'Bane', 'avatar': 'bane'},
    4: {'name': 'Bloodseeker', 'avatar': 'bloodseeker'},
    5: {'name': 'Crystal Maiden', 'avatar': 'crystal_maiden'},
    6: {'name': 'Drow Ranger', 'avatar': 'drow_ranger'},
    7: {'name': 'Earthshaker', 'avatar': 'earthshaker'},
    8: {'name': 'Juggernaut', 'avatar': 'juggernaut'},
    9: {'name': 'Mirana', 'avatar': 'mirana'},
    10: {'name': 'Morphling',  'avatar': 'morphling'},
    11: {'name': 'Shadow Fiend',  'avatar': 'nevermore'},
    12: {'name': 'Phantom Lancer',  'avatar': 'phantom_lancer'},
    13: {'name': 'Puck',  'avatar': 'puck'},
    14: {'name': 'Pudge',  'avatar': 'pudge'},
    15: {'name': 'Razor',  'avatar': 'razor'},
    16: {'name': 'Sand King',  'avatar': 'sand_king'},
    17: {'name': 'Storm Spirit',  'avatar': 'storm_spirit'},
    18: {'name': 'Sven',  'avatar': 'sven'},
    19: {'name': 'Tiny',  'avatar': 'tiny'},
    20: {'name': 'Vengeful Spirit',  'avatar': 'vengefulspirit'},
    21: {'name': 'Windranger',  'avatar': 'windrunner'},
    22: {'name': 'Zeus',  'avatar': 'zuus'},
    23: {'name': 'Kunkka',  'avatar': 'kunkka'},
    25: {'name': 'Lina',  'avatar': 'lina'},
    26: {'name': 'Lion',  'avatar': 'lion'},
    27: {'name': 'Shadow Shaman',  'avatar': 'shadow_shaman'},
    28: {'name': 'Slardar',  'avatar': 'slardar'},
    29: {'name': 'Tidehunter',  'avatar': 'tidehunter'},
    30: {'name': 'Witch Doctor',  'avatar': 'witch_doctor'},
    31: {'name': 'Lich',  'avatar': 'lich'},
    32: {'name': 'Riki',  'avatar': 'riki'},
    33: {'name': 'Enigma',  'avatar': 'enigma'},
    34: {'name': 'Tinker',  'avatar': 'tinker'},
    35: {'name': 'Sniper',  'avatar': 'sniper'},
    36: {'name': 'Necrophos',  'avatar': 'necrolyte'},
    37: {'name': 'Warlock',  'avatar': 'warlock'},
    38: {'name': 'Beastmaster',  'avatar': 'beastmaster'},
    39: {'name': 'Queen of Pain',  'avatar': 'queenofpain'},
    40: {'name': 'Venomancer',  'avatar': 'venomancer'},
    41: {'name': 'Faceless Void',  'avatar': 'faceless_void'},
    42: {'name': 'Wraith King',  'avatar': 'wraith_king'},
    43: {'name': 'Death Prophet',  'avatar': 'death_prophet'},
    44: {'name': 'Phantom Assassin',  'avatar': 'phantom_assassin'},
    45: {'name': 'Pugna',  'avatar': 'pugna'},
    46: {'name': 'Templar Assassin',  'avatar': 'templar_assassin'},
    47: {'name': 'Viper',  'avatar': 'viper'},
    48: {'name': 'Luna',  'avatar': 'luna'},
    49: {'name': 'Dragon Knight',  'avatar': 'dragon_knight'},
    50: {'name': 'Dazzle',  'avatar': 'dazzle'},
    51: {'name': 'Clockwerk',  'avatar': 'rattletrap'},
    52: {'name': 'Leshrac',  'avatar': 'leshrac'},
    53: {'name': 'Nature\'s Prophet',  'avatar': 'furion'},
    54: {'name': 'Lifestealer',  'avatar': 'life_stealer'},
    55: {'name': 'Dark Seer',  'avatar': 'dark_seer'},
    56: {'name': 'Clinkz',  'avatar': 'clinkz'},
    57: {'name': 'Omniknight',  'avatar': 'omniknight'},
    58: {'name': 'Enchantress',  'avatar': 'enchantress'},
    59: {'name': 'Huskar',  'avatar': 'huskar'},
    60: {'name': 'Night Stalker',  'avatar': 'night_stalker'},
    61: {'name': 'Broodmother',  'avatar': 'broodmother'},
    62: {'name': 'Bounty Hunter',  'avatar': 'bounty_hunter'},
    63: {'name': 'Weaver',  'avatar': 'weaver'},
    64: {'name': 'Jakiro',  'avatar': 'jakiro'},
    65: {'name': 'Batrider',  'avatar': 'batrider'},
    66: {'name': 'Chen',  'avatar': 'chen'},
    67: {'name': 'Spectre',  'avatar': 'spectre'},
    68: {'name': 'Ancient Apparition',  'avatar': 'ancient_apparition'},
    69: {'name': 'Doom Bringer',  'avatar': 'doom_bringer'},
    70: {'name': 'Ursa',  'avatar': 'ursa'},
    71: {'name': 'Spirit Breaker',  'avatar': 'spirit_breaker'},
    72: {'name': 'Gyrocopter',  'avatar': 'gyrocopter'},
    73: {'name': 'Alchemist',  'avatar': 'alchemist'},
    74: {'name': 'Invoker',  'avatar': 'invoker'},
    75: {'name': 'Silencer',  'avatar': 'silencer'},
    76: {'name': 'Outworld Devourer',  'avatar': 'obsidian_destroyer'},
    77: {'name': 'Lycan',  'avatar': 'lycan'},
    78: {'name': 'Brewmaster',  'avatar': 'brewmaster'},
    79: {'name': 'Shadow Demon',  'avatar': 'shadow_demon'},
    80: {'name': 'Lone Druid',  'avatar': 'lone_druid'},
    81: {'name': 'Chaos Knight',  'avatar': 'chaos_knight'},
    82: {'name': 'Meepo',  'avatar': 'meepo'},
    83: {'name': 'Treant Protector',  'avatar': 'treant'},
    84: {'name': 'Ogre Magi',  'avatar': 'ogre_magi'},
    85: {'name': 'Undying',  'avatar': 'undying'},
    86: {'name': 'Rubick',  'avatar': 'rubick'},
    87: {'name': 'Disruptor',  'avatar': 'disruptor'},
    88: {'name': 'Nyx Assassin',  'avatar': 'nyx_assassin'},
    89: {'name': 'Naga Siren',  'avatar': 'naga_siren'},
    90: {'name': 'Keeper of the Light',  'avatar': 'keeper_of_the_light'},
    91: {'name': 'Io',  'avatar': 'wisp'},
    92: {'name': 'Visage',  'avatar': 'visage'},
    93: {'name': 'Slark',  'avatar': 'slark'},
    94: {'name': 'Medusa',  'avatar': 'medusa'},
    95: {'name': 'Troll Warlord',  'avatar': 'troll_warlord'},
    96: {'name': 'Centaur Warrunner',  'avatar': 'centaur'},
    97: {'name': 'Magnus',  'avatar': 'magnataur'},
    98: {'name': 'Timbersaw',  'avatar': 'shredder'},
    99: {'name': 'Bristleback',  'avatar': 'bristleback'},
    100: {'name': 'Tusk',   'avatar': 'tusk'},
    101: {'name': 'Skywrath Mage',   'avatar': 'skywrath_mage'},
    102: {'name': 'Abaddon',   'avatar': 'abaddon'},
    103: {'name': 'Elder Titan',   'avatar': 'elder_titan'},
    104: {'name': 'Legion Commander',   'avatar': 'legion_commander'},
    106: {'name': 'Ember Spirit',   'avatar': 'ember_spirit'},
    107: {'name': 'Earth Spirit',   'avatar': 'earth_spirit'},
    109: {'name': 'Terrorblade',   'avatar': 'terrorblade'},
    110: {'name': 'Phoenix',   'avatar': 'phoenix'}

};