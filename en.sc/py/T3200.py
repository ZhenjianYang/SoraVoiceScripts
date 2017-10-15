from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3200   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3200   ._SN',
            'ED6_DT21/T3200_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Mao',                                  # 9
        'Ed',                                   # 10
        'Addy',                                 # 11
        'Child',                                # 12
        'Child',                                # 13
        'Tourist',                              # 14
        'Tourist',                              # 15
        'Tourist',                              # 16
        'Lucky',                                # 17
        'Quantay',                              # 18
        'Faults',                               # 19
        'Warrant Officer Gerwin',               # 20
        'Private Colby',                        # 21
        'Private Amando',                       # 22
        'Recia',                                # 23
        'Creepy Sheep',                         # 24
        'Creepy Sheep',                         # 25
        'Creepy Sheep',                         # 26
        'Creepy Sheep',                         # 27
        'Creepy Sheep',                         # 28
        'Creepy Sheep',                         # 29
        'Villager',                             # 30
        'Villager',                             # 31
        'Villager',                             # 32
        'Villager',                             # 33
        'Villager',                             # 34
        'Villager',                             # 35
        'Horrace',                              # 36
        'Tratt Plains Road',                    # 37
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01130 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT07/CH01070 ._CH',             # 04
        'ED6_DT07/CH01200 ._CH',             # 05
        'ED6_DT07/CH01210 ._CH',             # 06
        'ED6_DT07/CH01220 ._CH',             # 07
        'ED6_DT07/CH01160 ._CH',             # 08
        'ED6_DT07/CH01060 ._CH',             # 09
        'ED6_DT07/CH01140 ._CH',             # 0A
        'ED6_DT09/CH10140 ._CH',             # 0B
        'ED6_DT09/CH10141 ._CH',             # 0C
        'ED6_DT07/CH01000 ._CH',             # 0D
        'ED6_DT07/CH01010 ._CH',             # 0E
        'ED6_DT07/CH01020 ._CH',             # 0F
        'ED6_DT07/CH01030 ._CH',             # 10
        'ED6_DT07/CH01040 ._CH',             # 11
        'ED6_DT07/CH01050 ._CH',             # 12
        'ED6_DT26/CH20253 ._CH',             # 13
        'ED6_DT26/CH20248 ._CH',             # 14
        'ED6_DT26/CH20251 ._CH',             # 15
        'ED6_DT26/CH20249 ._CH',             # 16
        'ED6_DT26/CH20250 ._CH',             # 17
        'ED6_DT26/CH20257 ._CH',             # 18
        'ED6_DT09/CH11150 ._CH',             # 19
        'ED6_DT09/CH11151 ._CH',             # 1A
        'ED6_DT29/CH12070 ._CH',             # 1B
        'ED6_DT29/CH12071 ._CH',             # 1C
        'ED6_DT07/CH01640 ._CH',             # 1D
        'ED6_DT07/CH01150 ._CH',             # 1E
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01130P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT07/CH01070P._CP',             # 04
        'ED6_DT07/CH01200P._CP',             # 05
        'ED6_DT07/CH01210P._CP',             # 06
        'ED6_DT07/CH01220P._CP',             # 07
        'ED6_DT07/CH01160P._CP',             # 08
        'ED6_DT07/CH01060P._CP',             # 09
        'ED6_DT07/CH01140P._CP',             # 0A
        'ED6_DT09/CH10140P._CP',             # 0B
        'ED6_DT09/CH10141P._CP',             # 0C
        'ED6_DT07/CH01000P._CP',             # 0D
        'ED6_DT07/CH01010P._CP',             # 0E
        'ED6_DT07/CH01020P._CP',             # 0F
        'ED6_DT07/CH01030P._CP',             # 10
        'ED6_DT07/CH01040P._CP',             # 11
        'ED6_DT07/CH01050P._CP',             # 12
        'ED6_DT26/CH20253P._CP',             # 13
        'ED6_DT26/CH20248P._CP',             # 14
        'ED6_DT26/CH20251P._CP',             # 15
        'ED6_DT26/CH20249P._CP',             # 16
        'ED6_DT26/CH20250P._CP',             # 17
        'ED6_DT26/CH20257P._CP',             # 18
        'ED6_DT09/CH11150P._CP',             # 19
        'ED6_DT09/CH11151P._CP',             # 1A
        'ED6_DT29/CH12070P._CP',             # 1B
        'ED6_DT29/CH12071P._CP',             # 1C
        'ED6_DT07/CH01640P._CP',             # 1D
        'ED6_DT07/CH01150P._CP',             # 1E
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 12020,
        Z                   = 2000,
        Y                   = 16870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 12020,
        Z                   = 2000,
        Y                   = 14160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 21790,
        Z                   = 2000,
        Y                   = 5570,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 22880,
        Z                   = 2000,
        Y                   = 9470,
        Direction           = 303,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 8760,
        Z                   = 2000,
        Y                   = 13310,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 38180,
        Z                   = 6000,
        Y                   = 49000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 49580,
        Z                   = 2500,
        Y                   = -2390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 67620,
        Z                   = 3420,
        Y                   = 25770,
        Direction           = 195,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 66090,
        Z                   = 3020,
        Y                   = 25680,
        Direction           = 162,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 62800,
        Z                   = 3020,
        Y                   = 25140,
        Direction           = 156,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 61950,
        Z                   = 3020,
        Y                   = 23550,
        Direction           = 98,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 73010,
        Z                   = 3020,
        Y                   = 25590,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 67620,
        Z                   = 3420,
        Y                   = 25770,
        Direction           = 195,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 13520,
        Z                   = 2500,
        Y                   = 13590,
        Direction           = 312,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -30790,
        Z                   = -2000,
        Y                   = 15330,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 28950,
        Y                   = 1000,
        Z                   = 4030,
        Range               = 2500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 39,
    )

    DeclEvent(
        X                   = 980,
        Y                   = -250,
        Z                   = 18420,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 40,
    )

    DeclEvent(
        X                   = 42330,
        Y                   = 5750,
        Z                   = 36020,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 41,
    )


    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 6000,
        TriggerY            = 49730,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 7000,
        ActorY              = 49730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 43290,
        TriggerZ            = 6250,
        TriggerY            = 35890,
        TriggerRange        = 800,
        ActorX              = 43290,
        ActorZ              = 6500,
        ActorY              = 35890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53100,
        TriggerZ            = 0,
        TriggerY            = 3880,
        TriggerRange        = 1000,
        ActorX              = 48680,
        ActorZ              = 0,
        ActorY              = 2470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 38,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_60E",          # 00, 0
        "Function_1_7A3",          # 01, 1
        "Function_2_A7E",          # 02, 2
        "Function_3_BFB",          # 03, 3
        "Function_4_C58",          # 04, 4
        "Function_5_CC7",          # 05, 5
        "Function_6_D36",          # 06, 6
        "Function_7_DE6",          # 07, 7
        "Function_8_E5B",          # 08, 8
        "Function_9_EC7",          # 09, 9
        "Function_10_F28",         # 0A, 10
        "Function_11_1013",        # 0B, 11
        "Function_12_10ED",        # 0C, 12
        "Function_13_15D5",        # 0D, 13
        "Function_14_18CE",        # 0E, 14
        "Function_15_1C2F",        # 0F, 15
        "Function_16_1EBE",        # 10, 16
        "Function_17_2218",        # 11, 17
        "Function_18_2391",        # 12, 18
        "Function_19_2466",        # 13, 19
        "Function_20_3E5A",        # 14, 20
        "Function_21_3E9F",        # 15, 21
        "Function_22_3EFA",        # 16, 22
        "Function_23_3F50",        # 17, 23
        "Function_24_4124",        # 18, 24
        "Function_25_41ED",        # 19, 25
        "Function_26_4487",        # 1A, 26
        "Function_27_44E4",        # 1B, 27
        "Function_28_4546",        # 1C, 28
        "Function_29_458D",        # 1D, 29
        "Function_30_45FC",        # 1E, 30
        "Function_31_4654",        # 1F, 31
        "Function_32_46A0",        # 20, 32
        "Function_33_4716",        # 21, 33
        "Function_34_4746",        # 22, 34
        "Function_35_4776",        # 23, 35
        "Function_36_47E9",        # 24, 36
        "Function_37_4881",        # 25, 37
        "Function_38_48E7",        # 26, 38
        "Function_39_4A09",        # 27, 39
        "Function_40_4A0D",        # 28, 40
        "Function_41_4A11",        # 29, 41
    )


    def Function_0_60E(): pass

    label("Function_0_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_65E")
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x10, 14240, 2500, 16350, 90)
    SetChrPos(0x11, 14240, 2500, 17460, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_656")
    Jump("loc_65B")

    label("loc_656")

    ClearChrFlags(0x16, 0x80)

    label("loc_65B")

    Jump("loc_766")

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_68F")
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x10, 12150, 2000, 16180, 90)
    SetChrPos(0x11, 12150, 2000, 15380, 90)
    Jump("loc_766")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_6E7")
    SetChrPos(0x12, 15380, 2000, 12210, 0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x10, 12150, 2000, 20300, 90)
    SetChrPos(0x11, 12150, 2000, 19500, 90)
    SetChrPos(0x9, 21950, 2000, 14600, 270)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_766")

    label("loc_6E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_735")
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x10, 12150, 2000, 15860, 180)
    SetChrPos(0x11, 12150, 2000, 15150, 0)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    OP_43(0x10, 0x0, 0x0, 0x4)
    OP_43(0x11, 0x0, 0x0, 0x5)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_766")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_766")
    OP_43(0x10, 0x0, 0x0, 0x3)
    OP_43(0x11, 0x0, 0x0, 0x3)
    OP_43(0x10, 0x1, 0x0, 0x2)
    OP_43(0x11, 0x1, 0x0, 0x2)
    OP_43(0x10, 0x2, 0x0, 0x8)
    OP_43(0x11, 0x2, 0x0, 0x9)

    label("loc_766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_777")
    OP_A3(0x10F0)
    Event(1, 0)
    Jump("loc_7A2")

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_78D")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_7A2")

    label("loc_78D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A2")
    SetMapFlags(0x10000000)
    Event(0, 19)

    label("loc_7A2")

    Return()

    # Function_0_60E end

    def Function_1_7A3(): pass

    label("Function_1_7A3")

    OP_16(0x2, 0xFA0, 0xFFFE8130, 0xFFFE5E08, 0x230054)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F0")
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x89, 0x0)
    OP_82(0x8A, 0x0)
    OP_82(0x8B, 0x0)
    OP_82(0x8C, 0x0)
    OP_82(0x8D, 0x0)
    OP_82(0x8E, 0x0)
    OP_82(0x8F, 0x0)

    label("loc_7F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_804")
    OP_72(0x3, 0x10)
    OP_65(0x1, 0x1)
    Jump("loc_808")

    label("loc_804")

    OP_64(0x1, 0x1)

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_812")
    Jump("loc_A5B")

    label("loc_812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_A4A")
    PlayEffect(0x91, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x92, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x93, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x94, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x95, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x96, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x97, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x98, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x99, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundDistance(0x10B, 0x41E6, 0x9C4, 0x42EA, 0x7D0, 0x61A8, 0x64, 0x0)
    Jump("loc_A5B")

    label("loc_A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_A54")
    Jump("loc_A5B")

    label("loc_A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_A5B")

    label("loc_A5B")

    OP_72(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6F")
    OP_65(0x0, 0x1)
    Jump("loc_A7D")

    label("loc_A6F")

    OP_64(0x0, 0x1)
    OP_6F(0xB, 120)
    OP_82(0x90, 0x0)

    label("loc_A7D")

    Return()

    # Function_1_7A3 end

    def Function_2_A7E(): pass

    label("Function_2_A7E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA3")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_BE5")

    label("loc_AA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABC")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_BE5")

    label("loc_ABC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD5")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_BE5")

    label("loc_AD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_BE5")

    label("loc_AEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B07")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_BE5")

    label("loc_B07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B20")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_BE5")

    label("loc_B20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B39")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_BE5")

    label("loc_B39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B52")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_BE5")

    label("loc_B52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_BE5")

    label("loc_B6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B84")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_BE5")

    label("loc_B84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_BE5")

    label("loc_B9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB6")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_BE5")

    label("loc_BB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCF")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_BE5")

    label("loc_BCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE5")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_BE5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BFA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_BE5")

    label("loc_BFA")

    Return()

    # Function_2_A7E end

    def Function_3_BFB(): pass

    label("Function_3_BFB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C57")
    OP_8E(0xFE, 0x2EF4, 0x7D0, 0x573A, 0x1388, 0x0)
    OP_8E(0xFE, 0x57F8, 0x7D0, 0x573A, 0x1388, 0x0)
    OP_8E(0xFE, 0x57F8, 0x7D0, 0x2E54, 0x1388, 0x0)
    OP_8E(0xFE, 0x2EF4, 0x7D0, 0x2E54, 0x1388, 0x0)
    Jump("Function_3_BFB")

    label("loc_C57")

    Return()

    # Function_3_BFB end

    def Function_4_C58(): pass

    label("Function_4_C58")

    OP_43(0xFE, 0x1, 0x0, 0x2)

    label("loc_C5F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CC6")
    Sleep(400)
    OP_8F(0xFE, 0x2F76, 0x7D0, 0x45C4, 0x1770, 0x0)
    OP_8F(0xFE, 0x2F76, 0x7D0, 0x3DF4, 0x1770, 0x0)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0xFE, 0x0, 0x1E, 0x3E8, 0x7D0)
    OP_A2(0x8)
    OP_A6(0x9)
    OP_A3(0x9)
    Jump("loc_C5F")

    label("loc_CC6")

    Return()

    # Function_4_C58 end

    def Function_5_CC7(): pass

    label("Function_5_CC7")

    OP_43(0xFE, 0x1, 0x0, 0x2)

    label("loc_CCE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D35")
    Sleep(400)
    OP_8F(0xFE, 0x2F76, 0x7D0, 0x335E, 0x1770, 0x0)
    OP_8F(0xFE, 0x2F76, 0x7D0, 0x3B2E, 0x1770, 0x0)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0xFE, 0x1E, 0xA, 0x3E8, 0x7D0)
    OP_A2(0x9)
    OP_A6(0x8)
    OP_A3(0x8)
    Jump("loc_CCE")

    label("loc_D35")

    Return()

    # Function_5_CC7 end

    def Function_6_D36(): pass

    label("Function_6_D36")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DDA")
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_D40")

    label("loc_DDA")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_D36 end

    def Function_7_DE6(): pass

    label("Function_7_DE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E5A")
    OP_8E(0xFE, 0xFFFFDAE4, 0xFFFFF830, 0x32E6, 0x7D0, 0x0)
    Sleep(2600)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xFFFFDAE4, 0xFFFFF830, 0x422C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2238, 0x7D0, 0x413C, 0x7D0, 0x0)
    Sleep(2600)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x2238, 0x7D0, 0x33FE, 0x7D0, 0x0)
    Jump("Function_7_DE6")

    label("loc_E5A")

    Return()

    # Function_7_DE6 end

    def Function_8_E5B(): pass

    label("Function_8_E5B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EC6")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB3")
    Sleep(100)
    OP_4B(0xFE, 0)
    Jump("loc_EBE")

    label("loc_EB3")

    OP_4A(0xFE, 0)
    TurnDirection(0xFE, 0x11, 400)

    label("loc_EBE")

    Sleep(100)
    Jump("Function_8_E5B")

    label("loc_EC6")

    Return()

    # Function_8_E5B end

    def Function_9_EC7(): pass

    label("Function_9_EC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F27")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1B")
    OP_4B(0xFE, 0)
    Jump("loc_F1F")

    label("loc_F1B")

    OP_4A(0xFE, 0)

    label("loc_F1F")

    Sleep(100)
    Jump("Function_9_EC7")

    label("loc_F27")

    Return()

    # Function_9_EC7 end

    def Function_10_F28(): pass

    label("Function_10_F28")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_F9F")

    ChrTalk(    #0
        0x9,
        "For the hot springs to boil over like that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "Man, you never know what'll happen in\x01",
            "this world.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_F9F")


    ChrTalk(    #2
        0x9,
        "Good luck investigating the spring source.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "If things continue on like this,\x01",
            "we're out of business.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_100F")

    TalkEnd(0xFE)
    Return()

    # Function_10_F28 end

    def Function_11_1013(): pass

    label("Function_11_1013")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1061")

    ChrTalk(    #4
        0xFE,
        "Ohh! What a grand feat of leaping!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Ho ho. How amusing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10E9")

    label("loc_1061")


    ChrTalk(    #6
        0xFE,
        (
            "Ho ho. Apparently they're staging their\x01",
            "own mini Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "The children of the village are so full\x01",
            "of energy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E9")

    TalkEnd(0xFE)
    Return()

    # Function_11_1013 end

    def Function_12_10ED(): pass

    label("Function_12_10ED")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_123D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B2")

    ChrTalk(    #8
        0xFE,
        "Thank goodness the pump's fixed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "However, sounds like the other orbments\x01",
            "still aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I'm sure the central factory folk are\x01",
            "having a hard time, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_123A")

    label("loc_11B2")


    ChrTalk(    #11
        0xFE,
        (
            "The pump's fixed, but the other orbments\x01",
            "still aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I'm sure the central factory folk are\x01",
            "having a hard time, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123A")

    Jump("loc_15D1")

    label("loc_123D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129D")

    ChrTalk(    #13
        0xFE,
        "The springs have cooled...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "The pump orbment's stopped working...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_12BB")

    label("loc_129D")


    ChrTalk(    #15
        0xFE,
        "The pools have cooled...\x02",
    )

    CloseMessageWindow()

    label("loc_12BB")

    Jump("loc_15D1")

    label("loc_12BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_13B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_131E")

    ChrTalk(    #16
        0xFE,
        (
            "Phew! Thank goodness. I wasn't sure\x01",
            "what we'd do if it'd stayed that way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AE")

    label("loc_131E")


    ChrTalk(    #17
        0xFE,
        "I'm really happy the hot springs are fixed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I don't think any customers would've\x01",
            "come back if they were boiling like that\x01",
            "forever.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_13AE")

    Jump("loc_15D1")

    label("loc_13B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_13F8")

    ChrTalk(    #19
        0xFE,
        "The hot water's boiling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "Is this really happening?\x02",
    )

    CloseMessageWindow()
    Jump("loc_15D1")

    label("loc_13F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_14A3")
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_143D")

    ChrTalk(    #21
        0xFE,
        "Not yet!\x02",
    )

    CloseMessageWindow()
    OP_43(0xFE, 0x2, 0x0, 0x6)
    OP_95(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x7D0)
    Jump("loc_1498")

    label("loc_143D")


    ChrTalk(    #22
        0xFE,
        "Here we go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "Sword Technique: Eight-Leaf Blitz!!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_43(0xFE, 0x2, 0x0, 0x6)
    OP_95(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x7D0)

    label("loc_1498")

    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    Jump("loc_15D1")

    label("loc_14A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_15D1")
    OP_4A(0xFE, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1542")

    ChrTalk(    #24
        0xFE,
        (
            "Bracers sure must be strong if\x01",
            "they're going around winning\x01",
            "tournaments, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "All right, I'm gonna play the bracer\x01",
            "from now on!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15CD")

    label("loc_1542")


    ChrTalk(    #26
        0xFE,
        (
            "I read about the Martial Arts Competition\x01",
            "in the Liberl News!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "It said that a bracer team won!\x01",
            "Bracers really are strong, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_15CD")

    OP_4B(0xFE, 255)

    label("loc_15D1")

    TalkEnd(0x10)
    Return()

    # Function_12_10ED end

    def Function_13_15D5(): pass

    label("Function_13_15D5")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1633")

    ChrTalk(    #28
        0xFE,
        "Yeah, Elmo's gotta have hot springs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "There's just no Elmo without 'em.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18CA")

    label("loc_1633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1689")

    ChrTalk(    #30
        0xFE,
        (
            "It was boiling the other day,\x01",
            "but now it's cold...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "It's so weird.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18CA")

    label("loc_1689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1732")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_16EE")

    ChrTalk(    #32
        0xFE,
        (
            "Bracers really are cool, man. No wonder\x01",
            "they won the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_172F")

    label("loc_16EE")


    ChrTalk(    #33
        0xFE,
        "Bracers fixed the springs, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "They're so amazing!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_172F")

    Jump("loc_18CA")

    label("loc_1732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_17A2")

    ChrTalk(    #35
        0xFE,
        (
            "Aww... How can we make hot spring\x01",
            "boiled eggs like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "They'd be hard boiled in a second.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18CA")

    label("loc_17A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_185D")
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1815")

    ChrTalk(    #37
        0xFE,
        (
            "Next, it's time for my Body Split craft!\x01",
            "Ha ha ha! Can you see through the\x01",
            "illusion?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1852")

    label("loc_1815")


    ChrTalk(    #38
        0xFE,
        (
            "Eat this! Bullet Barrage!!\x01",
            "Bang bang bang BAAAANG!!!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1852")

    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    Jump("loc_18CA")

    label("loc_185D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_18CA")
    OP_4A(0xFE, 255)

    ChrTalk(    #39
        0xFE,
        (
            "Bracers are fine, but the special\x01",
            "forces are cool, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "I love playing the villain.\x02",
    )

    CloseMessageWindow()
    OP_4B(0xFE, 255)

    label("loc_18CA")

    TalkEnd(0x11)
    Return()

    # Function_13_15D5 end

    def Function_14_18CE(): pass

    label("Function_14_18CE")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1A53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1935")

    ChrTalk(    #41
        0xFE,
        "Wh-What a scoop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I-I've got to get my camera\x01",
            "ready and grab a picture...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A50")

    label("loc_1935")


    ChrTalk(    #43
        0xFE,
        "Wh-What a scoop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I-I've got to get my camera\x01",
            "ready and grab a picture...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "N-No, wait... Shouldn't I get the\x01",
            "situation written down first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "Okay, calm down. Thiiink calmly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Hmm... Yeah, first, I need to\x01",
            "grab some photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "A-All right... Time to shoot!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1A50")

    Jump("loc_1C2B")

    label("loc_1A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1C2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1B11")

    ChrTalk(    #49
        0xFE,
        (
            "No matter how many times I come,\x01",
            "I always fall in love with this village's\x01",
            "Eastern-style design.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Haha, I'd like to come here for fun\x01",
            "sometime instead of for work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C2B")

    label("loc_1B11")


    ChrTalk(    #51
        0xFE,
        (
            "I'm in charge of the culture column\x01",
            "for the Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "No matter how many times I come,\x01",
            "I always fall in love with this village's\x01",
            "Eastern-style design.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "I've done an article about the inn\x01",
            "here before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "This time, I want to write up a piece\x01",
            "about the cuisine.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1C2B")

    TalkEnd(0x12)
    Return()

    # Function_14_18CE end

    def Function_15_1C2F(): pass

    label("Function_15_1C2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1D24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC9")

    ChrTalk(    #55
        0xFE,
        "The pump's started working again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "I was sure the equipment here was\x01",
            "orbal driven, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "How is it working, then?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1D21")

    label("loc_1CC9")


    ChrTalk(    #58
        0xFE,
        (
            "I'm sure the equipment here is orbal\x01",
            "driven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "In that case, how is it working?\x02",
    )

    CloseMessageWindow()

    label("loc_1D21")

    Jump("loc_1EBA")

    label("loc_1D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E46")

    ChrTalk(    #60
        0xFE,
        (
            "We're a patrol force dispatched\x01",
            "from the Wolf Fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "For now, we're maintaining security\x01",
            "in Elmo Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Unfortunately, the hot springs pump\x01",
            "stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "It's not a facility that directly affects daily\x01",
            "life, though, so it's not a major concern.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1EBA")

    label("loc_1E46")


    ChrTalk(    #64
        0xFE,
        (
            "The hot springs pump has stopped\x01",
            "working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I suppose this, too, is due to that damned\x01",
            "shutdown phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EBA")

    TalkEnd(0xFE)
    Return()

    # Function_15_1C2F end

    def Function_16_1EBE(): pass

    label("Function_16_1EBE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD6")

    ChrTalk(    #66
        0xFE,
        (
            "I know Mr. Gerwin's as curious as I am,\x01",
            "but why did the pump start working?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "If there's a way to work around this\x01",
            "shutdown phenomenon, I'd like it if\x01",
            "our guns could be made useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "It's super nerve-racking not having\x01",
            "our guns work, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_204F")

    label("loc_1FD6")


    ChrTalk(    #69
        0xFE,
        (
            "It's super nerve-racking not having\x01",
            "our guns work, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "But we can't show fear in front of\x01",
            "the civilians.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204F")

    Jump("loc_2214")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217B")

    ChrTalk(    #71
        0xFE,
        (
            "We're a reinforcement squad sent\x01",
            "from Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Right now, I'm on patrol around the village\x01",
            "with the sub commander from the Wolf Fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Elmo Village is calmer than I thought\x01",
            "it would be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I guess that's because it's a pretty\x01",
            "peaceful place normally.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2214")

    label("loc_217B")


    ChrTalk(    #75
        0xFE,
        (
            "We're a reinforcement squad sent\x01",
            "from Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Right now, I'm on patrol around the village\x01",
            "with the sub commander from the Wolf Fort.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2214")

    TalkEnd(0xFE)
    Return()

    # Function_16_1EBE end

    def Function_17_2218(): pass

    label("Function_17_2218")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_22AF")

    ChrTalk(    #77
        0xFE,
        (
            "The pump's been repaired, from what\x01",
            "I've been told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "You guys have been running around\x01",
            "like crazy. Must be tough to be a bracer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238D")

    label("loc_22AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_238D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2333")

    ChrTalk(    #79
        0xFE,
        (
            "Behind here's the mountain where the\x01",
            "water source is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "It's a dangerous place, so I'm standing\x01",
            "guard.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_238D")

    label("loc_2333")


    ChrTalk(    #81
        0xFE,
        (
            "Behind here's the mountain where the\x01",
            "water source is. It's dangerous, so be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238D")

    TalkEnd(0xFE)
    Return()

    # Function_17_2218 end

    def Function_18_2391(): pass

    label("Function_18_2391")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2462")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2408")

    ChrTalk(    #82
        0xFE,
        (
            "I came to see the baths,\x01",
            "and the pump really is fixed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "YES!! We're back in business!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2462")

    label("loc_2408")


    ChrTalk(    #84
        0xFE,
        (
            "We're part-timers, so no customers\x01",
            "means no job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "I hope our guests return soon.\x02",
    )

    CloseMessageWindow()

    label("loc_2462")

    TalkEnd(0xFE)
    Return()

    # Function_18_2391 end

    def Function_19_2466(): pass

    label("Function_19_2466")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2487")
    Call(0, 36)
    Call(0, 37)

    label("loc_2487")

    SetChrPos(0x101, -23960, -2000, 14980, 90)
    SetChrPos(0x107, -23740, -2000, 16230, 90)
    SetChrPos(0xF7, -25260, -2000, 15090, 90)
    SetChrPos(0xF9, -25290, -2000, 16370, 90)
    SetChrPos(0x8, -6810, -1250, 14740, 270)
    ClearChrFlags(0x8, 0x80)
    OP_6D(-21340, -2000, 15680, 0)
    OP_67(0, 8800, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(275, 0)

    def lambda_2524():
        OP_6D(-19340, -2000, 15680, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2524)

    def lambda_253C():
        OP_8E(0xFE, 0xFFFFB208, 0xFFFFF830, 0x3A84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_253C)
    Sleep(100)

    def lambda_255C():
        OP_8E(0xFE, 0xFFFFB2E4, 0xFFFFF830, 0x3F66, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_255C)
    Sleep(100)

    def lambda_257C():
        OP_8E(0xFE, 0xFFFFACF4, 0xFFFFF830, 0x3AF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_257C)
    Sleep(100)

    def lambda_259C():
        OP_8E(0xFE, 0xFFFFACD6, 0xFFFFF830, 0x3FF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_259C)
    OP_C8(0x80, 0x46, "C_PLAC10._CH", 0x1, 0x7D0)
    OP_DE("Elmo Village")
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x107, 0x0)

    NpcTalk(    #86
        0x8,
        "Old Woman's Voice",
        "#3PAhhhh, good, good, you're here!\x02",
    )

    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF9, 0x0)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271F")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as met Mao again\x01",              # 0
            "Set as haven't met Mao again\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_270A"),
        (1, "loc_2710"),
        (SWITCH_DEFAULT, "loc_2716"),
    )


    label("loc_270A")

    OP_A2(0x1482)
    Jump("loc_2716")

    label("loc_2710")

    OP_A3(0x1482)
    Jump("loc_2716")

    label("loc_2716")

    FadeToBright(300, 0)

    label("loc_271F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C6")

    ChrTalk(    #87
        0x101,
        "#1004F#6PMrs. Mao!\x02",
    )

    CloseMessageWindow()

    def lambda_2745():
        OP_6D(-11110, -2000, 15260, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2745)
    WaitChrThread(0x0, 0x0)

    def lambda_2762():
        OP_6D(-12380, -2000, 15930, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2762)

    def lambda_277A():
        OP_67(0, 12500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_277A)

    def lambda_2792():
        OP_6B(2590, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2792)

    def lambda_27A2():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_27A2)

    def lambda_27B2():
        OP_8E(0x8, 0xFFFFD364, 0xFFFFF830, 0x3CA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27B2)

    def lambda_27CD():
        OP_8E(0xFE, 0xFFFFCD60, 0xFFFFF830, 0x3A84, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_27CD)
    Sleep(100)

    def lambda_27ED():
        OP_8E(0xFE, 0xFFFFCE3C, 0xFFFFF830, 0x3F66, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_27ED)
    Sleep(100)

    def lambda_280D():
        OP_8E(0xFE, 0xFFFFC84C, 0xFFFFF830, 0x3AF2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_280D)
    Sleep(100)

    def lambda_282D():
        OP_8E(0xFE, 0xFFFFC82E, 0xFFFFF830, 0x3FF2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_282D)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #88
        0x8,
        (
            "#680FHello, Estelle! Dear child,\x01",
            "but it's been ages!\x02\x03",

            "You look so grown up now.\x01",
            "Rather like your father!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1016F#5PHaha... C'mon, Mrs. Mao...\x02\x03",

            "#1025FWe're actually here on business...\x01",
            "I think Kilika or Mr. Murdock called\x01",
            "ahead...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#682FThat he did. I got off the phone with\x01",
            "Murdock just a little while ago.\x02\x03",

            "There've been earthquakes all\x01",
            "over the region, eh? Odd...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B77")

    label("loc_29C6")


    ChrTalk(    #91
        0x107,
        "#560F#6PMrs. Maaaaao!\x02",
    )

    CloseMessageWindow()

    def lambda_29E7():
        OP_6D(-11110, -2000, 15260, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_29E7)
    WaitChrThread(0x0, 0x0)

    def lambda_2A04():
        OP_6D(-12380, -2000, 15930, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2A04)

    def lambda_2A1C():
        OP_67(0, 12500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2A1C)

    def lambda_2A34():
        OP_6B(2590, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2A34)

    def lambda_2A44():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2A44)

    def lambda_2A54():
        OP_8E(0x8, 0xFFFFD364, 0xFFFFF830, 0x3CA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A54)

    def lambda_2A6F():
        OP_8E(0xFE, 0xFFFFCD60, 0xFFFFF830, 0x3A84, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A6F)
    Sleep(100)

    def lambda_2A8F():
        OP_8E(0xFE, 0xFFFFCE3C, 0xFFFFF830, 0x3F66, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2A8F)
    Sleep(100)

    def lambda_2AAF():
        OP_8E(0xFE, 0xFFFFC84C, 0xFFFFF830, 0x3AF2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_2AAF)
    Sleep(100)

    def lambda_2ACF():
        OP_8E(0xFE, 0xFFFFC82E, 0xFFFFF830, 0x3FF2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_2ACF)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #92
        0x8,
        (
            "#680FHello again!\x02\x03",

            "Murdock called ahead of you lot,\x01",
            "told me what's happening.\x02\x03",

            "There've been earthquakes all\x01",
            "over the region, eh? Odd...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B77")


    ChrTalk(    #93
        0x101,
        (
            "#1007F#5POdd, nothing. This whole thing is bizarre,\x01",
            "but maybe you can help us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#682FActually, I'd like to turn that around.\x01",
            "I was about to contact the guild anyway.\x02\x03",

            "Something strange happened just\x01",
            "a few hours ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x107,
        "#064F#6PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1005F#5PAn earthquake hit here, too?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "#685FI almost wish... An earthquake might\x01",
            "be less destructive...\x02\x03",

            "#682FWell, picture's worth a thousand words,\x01",
            "eh? Come see for yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    def lambda_2D36():
        OP_90(0x8, 0x4E20, 0x0, 0xFFFFFF38, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2D36)

    def lambda_2D51():
        OP_6D(17080, 2500, 17170, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D51)

    def lambda_2D69():
        OP_67(0, 8820, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D69)

    def lambda_2D81():
        OP_6B(3120, 11000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2D81)

    def lambda_2D91():
        OP_6C(57000, 11000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_2D91)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(100)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    def lambda_2DCF():
        OP_90(0xFE, 0x4E20, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DCF)
    Sleep(200)

    def lambda_2DEF():
        OP_90(0xFE, 0x4E20, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2DEF)
    Sleep(100)

    def lambda_2E0F():
        OP_90(0xFE, 0x4E20, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2E0F)
    Sleep(100)

    def lambda_2E2F():
        OP_90(0xFE, 0x4E20, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2E2F)
    WaitChrThread(0x101, 0x2)
    OP_44(0x8, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)
    OP_8C(0x101, 90, 0)
    OP_8C(0x107, 90, 0)
    OP_8C(0xF7, 90, 0)
    OP_8C(0xF9, 90, 0)

    def lambda_2E7F():
        OP_8E(0xFE, 0x35AC, 0x9C4, 0x3E4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2E7F)

    def lambda_2E9A():
        OP_8F(0xFE, 0x36BA, 0x9C4, 0x40BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E9A)

    def lambda_2EB5():
        OP_8F(0xFE, 0x366A, 0x9C4, 0x4538, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2EB5)

    def lambda_2ED0():
        OP_8F(0xFE, 0x32A0, 0x9C4, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2ED0)

    def lambda_2EEB():
        OP_8F(0xFE, 0x3278, 0x9C4, 0x418C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2EEB)
    WaitChrThread(0x8, 0x1)

    def lambda_2F0B():
        OP_8C(0xFE, 275, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F0B)

    def lambda_2F19():
        OP_8E(0xFE, 0x35CA, 0x9C4, 0x38D6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F19)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF9, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #98
        0x101,
        "#1020F#5PWhat in the...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x107,
        "#065F#5PThe springs are boiling over!\x02",
    )

    CloseMessageWindow()

    def lambda_3002():
        OP_6D(15000, 2500, 16149, 1300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3002)

    def lambda_301A():
        OP_67(0, 8500, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_301A)

    def lambda_3032():
        OP_6B(2870, 1300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3032)

    def lambda_3042():
        OP_8C(0x107, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3042)

    def lambda_3050():
        OP_8C(0xF7, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3050)
    OP_8C(0x101, 180, 400)
    OP_8C(0xF9, 180, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_30BB")

    ChrTalk(    #100
        0x106,
        (
            "#057FWhat the hell? It's not supposed\x01",
            "to get this hot!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3107")

    label("loc_30BB")


    ChrTalk(    #101
        0x103,
        (
            "#022FThis really is bizarre. The water isn't\x01",
            "supposed to get this hot!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3107")


    ChrTalk(    #102
        0x8,
        (
            "#685FBelieve me, I'd like to know\x01",
            "what's going on here too...\x02\x03",

            "#682FRight after I got off the phone with\x01",
            "Murdock, I heard a big fuss out here.\x02\x03",

            "I came out to see what was going on,\x01",
            "and found...this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x107,
        (
            "#065FMaybe...the pump is broken, somehow?\x02\x03",

            "It might be emitting heat, or... Wait,\x01",
            "no, it couldn't heat ALL this water...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#682FNo, the pump's working just fine,\x01",
            "I checked it a second ago.\x02\x03",

            "The way I see it, something at the source\x01",
            "of the springs must've changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1015F#6PSo... I'm guessing temperature changes\x01",
            "like this aren't too common?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "#685FIt's never happened while I've been here...\x01",
            "and I've been here half a century!\x02\x03",

            "#682FIt's worrying, to say the least.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3470")

    ChrTalk(    #107
        0x104,
        (
            "#035FIt seems as though this could be\x01",
            "related to our quaking earth, no?\x02\x03",

            "#030FPerhaps the excitement of the septium\x01",
            "veins has increased the temperature\x01",
            "of the water?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3514")

    label("loc_3470")


    ChrTalk(    #108
        0x105,
        (
            "#047FTo be honest, this may have something\x01",
            "to do with the earthquakes.\x02\x03",

            "#042FIf something is stimulating the septium\x01",
            "veins, might that heat the water further?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3514")


    ChrTalk(    #109
        0x107,
        (
            "#065FUm, that's...really likely, actually!\x02\x03",

            "And if the water keeps getting hotter,\x01",
            "the springs'll be too dangerous to live\x01",
            "near...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#1005F#6PLike heck we'll let that happen!\x01",
            "C'mon, let's go find the problem!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_363E")

    ChrTalk(    #111
        0x106,
        (
            "#050FMa'am, where's the springs' source?\x02\x03",

            "Can we go check it out?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AF")

    label("loc_363E")


    ChrTalk(    #112
        0x103,
        (
            "#020FMrs. Mao, where exactly is the\x01",
            "source for the springs?\x02\x03",

            "Would you mind if we investigated the problem?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36AF")


    ChrTalk(    #113
        0x8,
        (
            "#680FI thought you might ask that, so I fished\x01",
            "this out the back of a drawer.\x02\x03",

            "#681FGo on! Take it!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3692, 0x9C4, 0x3DB8, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #114
        "\x07\x00Estelle received the #1013i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F5, 1)
    OP_8F(0x8, 0x35CA, 0x9C4, 0x3BC4, 0x3E8, 0x0)

    ChrTalk(    #115
        0x101,
        "#1004F#6PA key?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "#680F#2PMm-hmm! It's the key to the wooden\x01",
            "gate near the pump shed.\x02\x03",

            "The cave down to the source\x01",
            "of the springs is that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#1018F#6PSweet! Thanks, Mrs. Mao!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x107,
        "#560FI didn't know there was a cave like that!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_38CF")

    ChrTalk(    #119
        0x106,
        (
            "#051FHeh. Thanks for gettin' things\x01",
            "ready for us, ma'am.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_390C")

    label("loc_38CF")


    ChrTalk(    #120
        0x103,
        (
            "#021FYou're always so on the ball,\x01",
            "Mrs. Mao. Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_390C")


    ChrTalk(    #121
        0x8,
        (
            "#681F#2POh, don't worry. We're the ones\x01",
            "asking you for a favor, after all!\x02\x03",

            "#680FI can't well let the customers boil\x01",
            "themselves like eggs, and we can't\x01",
            "even use our water for washing.\x02\x03",

            "I'm counting on you all to get\x01",
            "to the bottom of this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        "#1006F#6PYou can bet we will!\x02",
    )

    CloseMessageWindow()
    OP_A3(0x0)
    OP_8C(0x8, 180, 400)
    OP_43(0x8, 0x1, 0x0, 0x14)

    def lambda_3A3A():
        OP_6D(18120, 2000, 11950, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3A3A)

    def lambda_3A52():
        OP_67(0, 8820, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3A52)

    def lambda_3A6A():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3A6A)
    Sleep(1000)

    def lambda_3A7F():

        label("loc_3A7F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3A7F")

    QueueWorkItem2(0x101, 2, lambda_3A7F)
    Sleep(200)

    def lambda_3A95():

        label("loc_3A95")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3A95")

    QueueWorkItem2(0x107, 2, lambda_3A95)
    Sleep(200)

    def lambda_3AAB():

        label("loc_3AAB")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3AAB")

    QueueWorkItem2(0xF7, 2, lambda_3AAB)
    Sleep(200)

    def lambda_3AC1():

        label("loc_3AC1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3AC1")

    QueueWorkItem2(0xF9, 2, lambda_3AC1)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    OP_44(0x101, 0x2)
    OP_44(0x107, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0xF9, 0x2)

    def lambda_3AF6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AF6)
    Sleep(100)

    def lambda_3B09():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3B09)
    Sleep(100)

    def lambda_3B1C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3B1C)
    Sleep(100)

    def lambda_3B2F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3B2F)

    def lambda_3B3D():
        OP_6D(13550, 2500, 16850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B3D)

    def lambda_3B55():
        OP_6C(85000, 2000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3B55)
    Sleep(1000)

    def lambda_3B6A():
        OP_8C(0x101, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B6A)
    Sleep(50)

    def lambda_3B7D():
        OP_8C(0xF7, 45, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3B7D)
    Sleep(50)

    def lambda_3B90():
        OP_8C(0x107, 225, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3B90)
    Sleep(50)
    OP_8C(0xF9, 120, 400)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C61")

    ChrTalk(    #123
        0x104,
        (
            "#035FA mysterious cave which may hold the secrets\x01",
            "to the earthquakes that have plagued us...\x02\x03",

            "#030FWe should only take to that stage\x01",
            "when we're properly prepared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D39")

    label("loc_3C61")


    ChrTalk(    #124
        0x105,
        (
            "#047FWell, wait. We will be entering a cave we know\x01",
            "little about to investigate the temperature\x01",
            "increase AND the earthquakes...\x02\x03",

            "#042FI think it'd be wise to make absolutely\x01",
            "sure we're prepared before we go in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3DB8")

    ChrTalk(    #125
        0x106,
        (
            "#057F#4PYeah. We just might find who we're\x01",
            "lookin' for inside.\x02\x03",

            "#057FLet's make sure we go in loaded\x01",
            "and ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E48")

    label("loc_3DB8")


    ChrTalk(    #126
        0x103,
        (
            "#022F#4PYes... I suspect we might find a certain\x01",
            "sunglasses-wearing gentleman inside.\x02\x03",

            "We should be on our guard,\x01",
            "and prepare accordingly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E48")

    OP_A2(0x1421)
    OP_28(0x88, 0x1, 0x2)
    OP_28(0x88, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_19_2466 end

    def Function_20_3E5A(): pass

    label("Function_20_3E5A")

    OP_8E(0xFE, 0x357A, 0x9C4, 0x357A, 0x7D0, 0x0)
    OP_A2(0x0)
    OP_8E(0xFE, 0x3E30, 0x9C4, 0x3502, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4D62, 0x7D0, 0x1C7A, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_3E5A end

    def Function_21_3E9F(): pass

    label("Function_21_3E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_21_3E9F")

    label("loc_3EB3")

    Sleep(500)
    OP_8E(0xFE, 0x3796, 0x9C4, 0x35A2, 0x6A4, 0x0)
    OP_8E(0xFE, 0x3E80, 0x9C4, 0x3552, 0x6A4, 0x0)
    OP_8E(0xFE, 0x3DD6, 0x7D0, 0x212A, 0x6A4, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_21_3E9F end

    def Function_22_3EFA(): pass

    label("Function_22_3EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F0E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_22_3EFA")

    label("loc_3F0E")

    OP_8E(0xFE, 0x3796, 0x9C4, 0x35A2, 0x6A4, 0x0)
    OP_8E(0xFE, 0x3E80, 0x9C4, 0x3552, 0x6A4, 0x0)
    OP_8E(0xFE, 0x3DD6, 0x7D0, 0x212A, 0x6A4, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_22_3EFA end

    def Function_23_3F50(): pass

    label("Function_23_3F50")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #127
        "\x07\x05The gate is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 1)), scpexpr(EXPR_END)), "loc_4117")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Key]\x01",      # 0
            "[Don't]\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4111")
    EventBegin(0x0)
    Fade(1000)
    LoadEffect(0x1, "map\\\\t32key00.eff")
    OP_6D(40670, 6000, 49640, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 40430, 6000, 48600, 360)
    SetChrPos(0x107, 40580, 6000, 47300, 360)
    SetChrPos(0xF7, 39450, 6000, 48600, 360)
    SetChrPos(0xF9, 39490, 6000, 47300, 360)
    OP_0D()
    OP_22(0x73, 0x0, 0x64)
    OP_72(0xB, 0x800)
    OP_6F(0xB, 1)
    PlayEffect(0x1, 0x0, 0xFF, 40000, 6500, 50100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x10C, 0x0, 0x64)
    OP_B0(0xB, 0x1A)
    OP_6F(0xB, 1)
    OP_70(0xB, 0xA)
    OP_73(0xB)
    Sleep(1000)
    OP_6F(0xB, 10)
    OP_70(0xB, 0x46)
    OP_73(0xB)
    OP_6F(0xB, 120)
    OP_64(0x0, 0x1)
    OP_A2(0x1422)
    EventEnd(0x0)
    Jump("loc_4114")

    label("loc_4111")

    TalkEnd(0xFF)

    label("loc_4114")

    Jump("loc_4123")

    label("loc_4117")

    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_4123")

    Return()

    # Function_23_3F50 end

    def Function_24_4124(): pass

    label("Function_24_4124")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #128
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_417B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Pump Shed Key]\x01",      # 0
            "[Don't]\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41E0")
    OP_A2(0x2008)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_64(0x1, 0x1)
    OP_71(0x3, 0x10)
    Jump("loc_41E0")

    label("loc_41E0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_24_4124 end

    def Function_25_41ED(): pass

    label("Function_25_41ED")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(17090, 2500, 16680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_22(0xE3, 0x0, 0x64)
    Sleep(500)
    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_42E0():
        OP_6D(17090, 2500, 16680, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42E0)

    def lambda_42F8():
        OP_67(0, 8130, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42F8)

    def lambda_4310():
        OP_6C(76000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4310)
    OP_43(0x10, 0x1, 0x0, 0x1A)
    OP_43(0x11, 0x1, 0x0, 0x1B)
    OP_43(0xB, 0x1, 0x0, 0x1C)
    OP_43(0xC, 0x1, 0x0, 0x1D)
    OP_43(0x1D, 0x1, 0x0, 0x1E)
    OP_43(0x1E, 0x1, 0x0, 0x1F)
    OP_43(0x1F, 0x1, 0x0, 0x20)
    OP_43(0x20, 0x1, 0x0, 0x21)
    OP_43(0x21, 0x1, 0x0, 0x22)
    OP_43(0x22, 0x1, 0x0, 0x23)
    Sleep(8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(70100, 1000, 24730, 0)
    OP_67(0, 7650, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(285, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_22(0xE3, 0x0, 0x64)
    Sleep(500)
    PlayEffect(0x8F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T3221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_41ED end

    def Function_26_4487(): pass

    label("Function_26_4487")

    SetChrPos(0xFE, 6370, 1250, 16280, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x27EC, 0x7D0, 0x3F7A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x37AA, 0x9C4, 0x4628, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(800)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_26_4487 end

    def Function_27_44E4(): pass

    label("Function_27_44E4")

    Sleep(500)
    SetChrPos(0xFE, 6330, 1250, 15290, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x2526, 0x7D0, 0x3ADE, 0xBB8, 0x0)
    OP_8E(0xFE, 0x37A0, 0x9C4, 0x43B2, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(800)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_27_44E4 end

    def Function_28_4546(): pass

    label("Function_28_4546")

    Sleep(2500)
    SetChrPos(0xFE, 18640, 2000, 9920, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4736, 0x9C4, 0x3598, 0xBB8, 0x0)
    Sleep(800)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_28_4546 end

    def Function_29_458D(): pass

    label("Function_29_458D")

    Sleep(3000)
    SetChrPos(0xFE, 14660, 2000, 26670, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x398A, 0x7D0, 0x57E4, 0xBB8, 0x0)
    OP_8E(0xFE, 0x4286, 0x7D0, 0x580C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x42D6, 0x9C4, 0x4F1A, 0xBB8, 0x0)
    Sleep(800)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_29_458D end

    def Function_30_45FC(): pass

    label("Function_30_45FC")

    Sleep(3000)
    SetChrPos(0xFE, 6540, 1500, 14110, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x2594, 0x7D0, 0x3728, 0x5DC, 0x0)
    OP_8E(0xFE, 0x2E68, 0x7D0, 0x3DF4, 0x5DC, 0x0)
    OP_8E(0xFE, 0x33C2, 0x9C4, 0x3E08, 0x5DC, 0x0)
    Return()

    # Function_30_45FC end

    def Function_31_4654(): pass

    label("Function_31_4654")

    Sleep(1000)
    SetChrPos(0xFE, 12940, 2000, 8490, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x3412, 0x7D0, 0x2BE8, 0x3E8, 0x0)
    Sleep(800)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_31_4654 end

    def Function_32_46A0(): pass

    label("Function_32_46A0")

    Sleep(3000)
    SetChrPos(0xFE, 20900, 2000, 8650, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x517C, 0x7D0, 0x2B52, 0x7D0, 0x0)
    OP_8E(0xFE, 0x459C, 0x7D0, 0x2DBE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3F6F, 0x9C4, 0x3584, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(800)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_32_46A0 end

    def Function_33_4716(): pass

    label("Function_33_4716")

    Sleep(5000)
    SetChrPos(0xFE, 20010, 2000, 6870, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4DD0, 0x7D0, 0x2DFA, 0x7D0, 0x0)
    Return()

    # Function_33_4716 end

    def Function_34_4746(): pass

    label("Function_34_4746")

    Sleep(4000)
    SetChrPos(0xFE, 14510, 2000, 9450, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x38AE, 0x7D0, 0x2E68, 0x7D0, 0x0)
    Return()

    # Function_34_4746 end

    def Function_35_4776(): pass

    label("Function_35_4776")

    Sleep(4000)
    OP_72(0x2, 0x10)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x1D)
    OP_73(0x2)
    SetChrPos(0xFE, 21250, 2500, 25000, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x50DC, 0x7D0, 0x565E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x497A, 0x7D0, 0x5636, 0x7D0, 0x0)
    OP_8E(0xFE, 0x47AE, 0x9C4, 0x515E, 0x7D0, 0x0)
    Return()

    # Function_35_4776 end

    def Function_36_47E9(): pass

    label("Function_36_47E9")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4862"),
        (1, "loc_4868"),
        (SWITCH_DEFAULT, "loc_486E"),
    )


    label("loc_4862")

    OP_A2(0x1200)
    Jump("loc_486E")

    label("loc_4868")

    OP_A2(0x1201)
    Jump("loc_486E")

    label("loc_486E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_487C")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4880")

    label("loc_487C")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4880")

    Return()

    # Function_36_47E9 end

    def Function_37_4881(): pass

    label("Function_37_4881")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_48BB")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_48D5")

    label("loc_48BB")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_48D5")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_37_4881 end

    def Function_38_48E7(): pass

    label("Function_38_48E7")

    EventBegin(0x1)

    ChrTalk(    #129
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_4913():
        OP_6D(48400, 0, 3440, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4913)

    def lambda_492B():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_492B)

    def lambda_4943():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4943)

    def lambda_4953():
        OP_6C(135000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4953)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #130
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49F9")
    OP_C0(0xE, 0x22, 0xCF58, 0x0, 0x1126, 0x10E, 0xBE28, 0x0, 0x9A6)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_4A08")

    label("loc_49F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A08")
    EventEnd(0x1)

    label("loc_4A08")

    Return()

    # Function_38_48E7 end

    def Function_39_4A09(): pass

    label("Function_39_4A09")

    SetPlaceName(0x88)
    Return()

    # Function_39_4A09 end

    def Function_40_4A0D(): pass

    label("Function_40_4A0D")

    SetPlaceName(0x87)
    Return()

    # Function_40_4A0D end

    def Function_41_4A11(): pass

    label("Function_41_4A11")

    SetPlaceName(0x89)
    Return()

    # Function_41_4A11 end

    SaveToFile()

Try(main)
