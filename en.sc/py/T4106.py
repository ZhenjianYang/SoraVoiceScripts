from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4106   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4106.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
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
        'Finella',                              # 9
        'Carnero',                              # 10
        'Tiffany',                              # 11
        'Mechanic Payton',                      # 12
        'Rutherford',                           # 13
        'Aldan',                                # 14
        'Anton',                                # 15
        'Ricky',                                # 16
        'Kitty',                                # 17
        'Elderly Man',                          # 18
        'Elderly Woman',                        # 19
        'Middle-Aged Man',                      # 20
        'Middle-Aged Woman',                    # 21
        'Young Boy',                            # 22
        'Young Girl',                           # 23
        'Olivier',                              # 24
        'Kloe',                                 # 25
        'Tita',                                 # 26
        'Zin',                                  # 27
        'Major Vander',                         # 28
        'Renne',                                # 29
        'Nial',                                 # 30
        'Dorothy',                              # 31
        'Gretna Shadow',                        # 32
        'Airliner, Gretna',                     # 33
        'Scherazard',                           # 34
        'Agate',                                # 35
        'Father Kevin',                         # 36
        'Grancel - East Block',                 # 37
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
        'ED6_DT07/CH01540 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01010 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT07/CH00030 ._CH',             # 07
        'ED6_DT07/CH00040 ._CH',             # 08
        'ED6_DT07/CH00060 ._CH',             # 09
        'ED6_DT07/CH00070 ._CH',             # 0A
        'ED6_DT27/CH03570 ._CH',             # 0B
        'ED6_DT27/CH03510 ._CH',             # 0C
        'ED6_DT07/CH02060 ._CH',             # 0D
        'ED6_DT07/CH02070 ._CH',             # 0E
        'ED6_DT07/CH00020 ._CH',             # 0F
        'ED6_DT07/CH00050 ._CH',             # 10
        'ED6_DT27/CH03080 ._CH',             # 11
        'ED6_DT06/CH20063 ._CH',             # 12
        'ED6_DT06/CH20064 ._CH',             # 13
        'ED6_DT06/CH20038 ._CH',             # 14
        'ED6_DT26/CH20311 ._CH',             # 15
        'ED6_DT07/CH01450 ._CH',             # 16
        'ED6_DT07/CH01550 ._CH',             # 17
        'ED6_DT07/CH01140 ._CH',             # 18
        'ED6_DT07/CH01770 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT07/CH01540P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01010P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT07/CH00030P._CP',             # 07
        'ED6_DT07/CH00040P._CP',             # 08
        'ED6_DT07/CH00060P._CP',             # 09
        'ED6_DT07/CH00070P._CP',             # 0A
        'ED6_DT27/CH03570P._CP',             # 0B
        'ED6_DT27/CH03510P._CP',             # 0C
        'ED6_DT07/CH02060P._CP',             # 0D
        'ED6_DT07/CH02070P._CP',             # 0E
        'ED6_DT07/CH00020P._CP',             # 0F
        'ED6_DT07/CH00050P._CP',             # 10
        'ED6_DT27/CH03080P._CP',             # 11
        'ED6_DT06/CH20063P._CP',             # 12
        'ED6_DT06/CH20064P._CP',             # 13
        'ED6_DT06/CH20038P._CP',             # 14
        'ED6_DT26/CH20311P._CP',             # 15
        'ED6_DT07/CH01450P._CP',             # 16
        'ED6_DT07/CH01550P._CP',             # 17
        'ED6_DT07/CH01140P._CP',             # 18
        'ED6_DT07/CH01770P._CP',             # 19
    )

    DeclNpc(
        X                   = 58770,
        Z                   = 250,
        Y                   = 137000,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 83950,
        Z                   = 1500,
        Y                   = 142840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 82520,
        Z                   = 1500,
        Y                   = 142760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 72500,
        Z                   = -10000,
        Y                   = 163540,
        Direction           = 76,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 68650,
        Z                   = 250,
        Y                   = 147890,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 62500,
        Z                   = -3000,
        Y                   = 169170,
        Direction           = 76,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 55860,
        Z                   = 250,
        Y                   = 134560,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 54740,
        Z                   = 250,
        Y                   = 134560,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 56060,
        Z                   = 250,
        Y                   = 145340,
        Direction           = 169,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x189,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x189,
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
        X                   = 51050,
        Z                   = 0,
        Y                   = 83440,
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
        X                   = 73400,
        Y                   = 0,
        Z                   = 140700,
        Range               = 76300,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x23730,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )


    DeclActor(
        TriggerX            = 56800,
        TriggerZ            = 250,
        TriggerY            = 136940,
        TriggerRange        = 800,
        ActorX              = 58770,
        ActorZ              = 1750,
        ActorY              = 137000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53710,
        TriggerZ            = 250,
        TriggerY            = 137720,
        TriggerRange        = 800,
        ActorX              = 53710,
        ActorZ              = 2450,
        ActorY              = 137720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71160,
        TriggerZ            = -10000,
        TriggerY            = 151550,
        TriggerRange        = 800,
        ActorX              = 71160,
        ActorZ              = -8500,
        ActorY              = 151550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5A6",          # 00, 0
        "Function_1_721",          # 01, 1
        "Function_2_7C1",          # 02, 2
        "Function_3_7D7",          # 03, 3
        "Function_4_7DC",          # 04, 4
        "Function_5_B1D",          # 05, 5
        "Function_6_DE5",          # 06, 6
        "Function_7_11B8",         # 07, 7
        "Function_8_11BF",         # 08, 8
        "Function_9_155A",         # 09, 9
        "Function_10_1A26",        # 0A, 10
        "Function_11_1A2D",        # 0B, 11
        "Function_12_1A34",        # 0C, 12
        "Function_13_1A3B",        # 0D, 13
        "Function_14_2206",        # 0E, 14
        "Function_15_2263",        # 0F, 15
        "Function_16_22C2",        # 10, 16
        "Function_17_2335",        # 11, 17
        "Function_18_23A8",        # 12, 18
        "Function_19_241B",        # 13, 19
        "Function_20_248E",        # 14, 20
        "Function_21_24ED",        # 15, 21
        "Function_22_27E4",        # 16, 22
        "Function_23_3C54",        # 17, 23
        "Function_24_3EDC",        # 18, 24
        "Function_25_4783",        # 19, 25
        "Function_26_558C",        # 1A, 26
        "Function_27_5615",        # 1B, 27
        "Function_28_5631",        # 1C, 28
        "Function_29_56E4",        # 1D, 29
        "Function_30_576A",        # 1E, 30
        "Function_31_57E3",        # 1F, 31
        "Function_32_5868",        # 20, 32
        "Function_33_588C",        # 21, 33
        "Function_34_5955",        # 22, 34
    )


    def Function_0_5A6(): pass

    label("Function_0_5A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5BF")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_65D")

    label("loc_5BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_608")
    SetChrPos(0x9, 81810, 1500, 142750, 183)
    SetChrPos(0xA, 72490, -10000, 161070, 110)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_605")
    SetChrPos(0xD, 57130, 250, 138200, 135)

    label("loc_605")

    Jump("loc_65D")

    label("loc_608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63D")
    SetChrPos(0x9, 81810, 1500, 142750, 183)
    SetChrPos(0xA, 53400, 250, 145320, 183)
    SetChrFlags(0xB, 0x80)
    Jump("loc_65D")

    label("loc_63D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_64C")
    SetChrFlags(0xB, 0x80)
    Jump("loc_65D")

    label("loc_64C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_65D")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x80)

    label("loc_65D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_685")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_B1("T4106_4")
    Event(0, 24)
    Jump("loc_6CB")

    label("loc_685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_6AD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_B1("T4106_4")
    Event(0, 25)
    Jump("loc_6CB")

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CB")
    SetMapFlags(0x10000000)
    OP_B1("T4106_1")
    Event(0, 13)

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_720")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x40)
    SetChrPos(0x17, 81740, 1500, 143050, 90)
    SetChrPos(0x1B, 83170, 1500, 143050, 270)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x1B, 0x0, 0x0, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)

    label("loc_720")

    Return()

    # Function_0_5A6 end

    def Function_1_721(): pass

    label("Function_1_721")

    OP_16(0x2, 0xFA0, 0xFFFF5808, 0x7148, 0x23005F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74B")
    OP_B1("T4106_4")
    Jump("loc_7C0")

    label("loc_74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_781")
    OP_B1("T4106_2")
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)
    OP_72(0xD, 0x4)
    OP_71(0x9, 0x4)
    Jump("loc_7C0")

    label("loc_781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A1")
    OP_B1("T4106_6")
    Jump("loc_7C0")

    label("loc_7A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_7C0")
    OP_B1("T4106_1")
    OP_71(0x5, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)

    label("loc_7C0")

    Return()

    # Function_1_721 end

    def Function_2_7C1(): pass

    label("Function_2_7C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7C1")

    label("loc_7D6")

    Return()

    # Function_2_7C1 end

    def Function_3_7D7(): pass

    label("Function_3_7D7")

    Call(0, 4)
    Return()

    # Function_3_7D7 end

    def Function_4_7DC(): pass

    label("Function_4_7DC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_897")

    ChrTalk(    #0
        0x8,
        (
            "Currently, as all orbal energy is suspended,\x01",
            "none of our aircrafts are able to fly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        "We will gladly offer refunds here for any tickets.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "We are sincerely sorry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B19")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_8A1")
    Jump("loc_B19")

    label("loc_8A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_9AB")

    ChrTalk(    #3
        0x8,
        "Welcome.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_95E")

    ChrTalk(    #4
        0x8,
        (
            "Very soon the eastbound scheduled liner,\x01",
            "the Linde, will be landing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "All boarding passengers are encouraged\x01",
            "to hurry in order to catch this flight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A8")

    label("loc_95E")


    ChrTalk(    #6
        0x8,
        (
            "Very soon the eastbound scheduled liner,\x01",
            "the Linde, will be landing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A8")

    Jump("loc_B19")

    label("loc_9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A28")

    ChrTalk(    #7
        0x8,
        (
            "We are very sorry, but all flights\x01",
            "for the day have ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "We look forward to your future patronage.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B19")

    label("loc_A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_A8B")

    ChrTalk(    #9
        0x8,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "Persons wishing to obtain tickets,\x01",
            "please come to the reception desk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B19")

    label("loc_A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_B19")

    ChrTalk(    #11
        0x8,
        "Thank you very much for your patronage.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "Should you have any business with our company,\x01",
            "please enter the building over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B19")

    TalkEnd(0x8)
    Return()

    # Function_4_7DC end

    def Function_5_B1D(): pass

    label("Function_5_B1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BE7")

    ChrTalk(    #13
        0xFE,
        (
            "Seems like the Cecilia and the Linde are\x01",
            "grounded over in Bose and Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Well, nothing for it then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Just gotta wait and keep the landing port\x01",
            "in shape until things change.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE1")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_C5E")

    ChrTalk(    #16
        0xFE,
        "Er...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "It's about time to start maintenance\x01",
            "on the Linde, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "Where did Tiffany get off to?\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE1")

    label("loc_C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_C68")
    Jump("loc_DE1")

    label("loc_C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(    #19
        0xFE,
        "Er...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "Where did Tiffany go?\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE1")

    label("loc_C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0F")

    ChrTalk(    #21
        0xFE,
        "Phew!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I was going to ask Tiffany to handle\x01",
            "the leftover work, but I couldn't work\x01",
            "up the guts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE1")

    label("loc_D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_D7B")

    ChrTalk(    #23
        0xFE,
        "Ah, I forgot to file the maintenance checklist!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "I've got to hurry up and write it up...\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE1")

    label("loc_D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_DE1")

    ChrTalk(    #25
        0xFE,
        "Umm... For Tiffany's next job...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Ah, that's right. Could you order some\x01",
            "orbal plugs?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE1")

    TalkEnd(0xFE)
    Return()

    # Function_5_B1D end

    def Function_6_DE5(): pass

    label("Function_6_DE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_EB7")

    ChrTalk(    #27
        0xFE,
        (
            "I thought the chief engineer would be\x01",
            "freaking out more, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Seems like being in this desperate situation's\x01",
            "actually calmed him down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "If only he was always this confident.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11B4")

    label("loc_EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1010")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_F87")

    ChrTalk(    #30
        0xFE,
        "I saw the XG-02 sample engine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I asked Payton to give me a peek at it,\x01",
            "but to think it's that small...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Amazing. It's incredible, even.\x01",
            "I feel pretty motivated after seeing it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_100D")

    label("loc_F87")


    ChrTalk(    #33
        0xFE,
        "Sorry, could you stay out of the way?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "We'll be using this lane very soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "We've got to start checking all locations...\x02",
    )

    CloseMessageWindow()

    label("loc_100D")

    Jump("loc_11B4")

    label("loc_1010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1089")

    ChrTalk(    #36
        0xFE,
        "Work's over for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Once I get back it's time for a shower\x01",
            "and then some drinks with friends.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B4")

    label("loc_1089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1154")

    ChrTalk(    #38
        0xFE,
        (
            "Ahhh, it's a little sad without the Arseille\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "I wonder if Payton will come back soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "There's no one to really compete with here\x01",
            "when it's just me and the chief engineer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B4")

    label("loc_1154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_11B4")

    ChrTalk(    #41
        0xFE,
        (
            "Our chief engineer's as weak-willed\x01",
            "and unreliable as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "*sigh* Oh, well...\x02",
    )

    CloseMessageWindow()

    label("loc_11B4")

    TalkEnd(0xFE)
    Return()

    # Function_6_DE5 end

    def Function_7_11B8(): pass

    label("Function_7_11B8")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_11B8 end

    def Function_8_11BF(): pass

    label("Function_8_11BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_12EC")

    ChrTalk(    #43
        0xFE,
        "I'm heading back to Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Negotiating with Ambassador Cochrane was\x01",
            "tough, but I finally managed to get her to let\x01",
            "me buy one of those liner ships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "She even said, 'fine, I guess\x01",
            "I'll let you off with that.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "*sigh* I've never had such a difficult\x01",
            "business deal before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1556")

    label("loc_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137A")

    ChrTalk(    #47
        0xFE,
        (
            "All my estimates were thrown back\x01",
            "in my face by Ambassador Cochrane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "She... She really hits you right where it hurts.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1556")

    label("loc_137A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1482")

    ChrTalk(    #49
        0xFE,
        (
            "It seems the Republic will let me buy\x01",
            "one of their liner ships, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Now we're having a hard time coming to\x01",
            "an agreement with them on price.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "That woman's supposed to be the Republican\x01",
            "ambassador, but she seems more like a\x01",
            "businesswoman.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1556")

    label("loc_1482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1556")

    ChrTalk(    #52
        0xFE,
        "I've got a deal with the Calvardian embassy soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "I'm going to negotiate with the Republican ambassa-\x01",
            "dor and try to get permission to buy an airship\x01",
            "of the same model as those scheduled liners.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1556")

    TalkEnd(0xFE)
    Return()

    # Function_8_11BF end

    def Function_9_155A(): pass

    label("Function_9_155A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_180E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_1765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168B")

    ChrTalk(    #54
        0xFE,
        "Oh, no!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "I asked the engineer that came off\x01",
            "of the Leibnitz, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Apparently the Arseille's getting its new\x01",
            "engine fitted at Leiston Fortress!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I can't be standing here!\x01",
            "I need to get back to Zeiss!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Just you wait, Arseille!\x01",
            "This time I've got you!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1762")

    label("loc_168B")


    ChrTalk(    #59
        0xFE,
        (
            "That reminds me, I saw them moving around\x01",
            "a really high-tech looking engine I've never\x01",
            "seen before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "I wonder what that was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "...Ah, forget everything else!\x01",
            "I need to hurry up and get on the Linde!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1762")

    Jump("loc_180B")

    label("loc_1765")


    ChrTalk(    #62
        0xFE,
        (
            "Seems like they're preparing\x01",
            "this lane for landing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I wonder...is it going to be an emergency\x01",
            "landing for an army ship or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "Or could it be...\x02",
    )

    CloseMessageWindow()

    label("loc_180B")

    Jump("loc_1A22")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18C5")

    ChrTalk(    #65
        0xFE,
        "That's odd. I've looked everywhere...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Apparently the Arseille isn't docked at any\x01",
            "commercial landing port anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "I wonder if it's outside the country.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A22")

    label("loc_18C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1959")

    ChrTalk(    #68
        0xFE,
        "Where did my beloved Arseille go...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "I've come this far, and I'll chase it to the\x01",
            "ends of the earth until I find where it is～!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A22")

    label("loc_1959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D0")

    ChrTalk(    #70
        0xFE,
        "Why, why?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "I came all the way to the capital, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "Why isn't the Arseille here?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1A22")

    label("loc_19D0")


    ChrTalk(    #73
        0xFE,
        "I came all the way to the capital, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "Why isn't the Arseille here?!\x02",
    )

    CloseMessageWindow()

    label("loc_1A22")

    TalkEnd(0xFE)
    Return()

    # Function_9_155A end

    def Function_10_1A26(): pass

    label("Function_10_1A26")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_1A26 end

    def Function_11_1A2D(): pass

    label("Function_11_1A2D")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_1A2D end

    def Function_12_1A34(): pass

    label("Function_12_1A34")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_12_1A34 end

    def Function_13_1A3B(): pass

    label("Function_13_1A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A4C")
    Call(0, 29)

    label("loc_1A4C")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_11(0xFF, 0xFF, 0xFF, 0x13880, 0x55730, 0x0)
    StopSound(0xEA60, 0x55730, 0x0)
    StopSound(0xAFC8, 0x55730, 0x2710)
    OP_6D(58630, 40000, 116260, 0)
    OP_67(0, 45000, -50000, 0)
    OP_6B(800, 0)
    OP_6C(60000, 0)
    OP_6E(250, 0)
    OP_A1(0x1F, 0xA)
    OP_72(0xA, 0x4)
    OP_72(0xA, 0x20)
    SetChrPos(0x1F, 87140, 15900, 130979, 90)
    SetChrFlags(0x1F, 0x4)
    OP_A1(0x20, 0xB)
    OP_71(0xB, 0x2)
    OP_72(0xB, 0x4)
    SetChrPos(0x20, 87140, 5900, 130979, 90)
    SetChrFlags(0x20, 0x4)
    OP_71(0x9, 0x4)
    OP_6F(0x5, 100)
    OP_6F(0xA, 60)
    OP_6F(0xB, 0)
    OP_22(0x79, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1B55")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_1B59")

    label("loc_1B55")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_1B59")

    OP_43(0x101, 0x0, 0x0, 0x15)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x7D0)
    OP_DE("Grancel")
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(83040, 1500, 131020, 0)
    OP_67(0, 6970, -10000, 0)
    OP_6B(3820, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    StopSound(0x88B8, 0x55730, 0x0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xA, 411)
    OP_70(0xA, 0x1C2)
    Sleep(1300)
    OP_43(0x11, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0x12, 0x1, 0x0, 0xE)
    Sleep(800)
    OP_43(0x13, 0x1, 0x0, 0xE)
    Sleep(800)
    OP_43(0x14, 0x1, 0x0, 0xE)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x10)
    Sleep(800)
    OP_43(0x18, 0x1, 0x0, 0x11)
    Sleep(800)
    OP_43(0x17, 0x1, 0x0, 0x12)
    Sleep(800)
    OP_43(0x19, 0x1, 0x0, 0x13)
    Sleep(800)
    OP_43(0x1A, 0x1, 0x0, 0x14)
    Sleep(500)

    def lambda_1C72():
        OP_6D(79270, 1500, 142560, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C72)
    WaitChrThread(0x1A, 0x1)
    OP_DC()

    ChrTalk(    #75
        0x101,
        (
            "#1006FAnd here we are back in the capital again.\x01",
            "Feels pretty good.\x02\x03",

            "Guess we better check in with the guild\x01",
            "branch first, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1D4F")

    ChrTalk(    #76
        0x106,
        "#051FYeah, let's go hear from Elnan what's what.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DA1")

    label("loc_1D4F")


    ChrTalk(    #77
        0x103,
        (
            "#020FYes, we should speak to Elnan and\x01",
            "see what the army has in mind for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA1")


    ChrTalk(    #78
        0x17,
        (
            "#033FI did notice that a certain white ship\x01",
            "isn't in port today.\x02\x03",

            "The 'Arseille,' I believe it was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1015FHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_1E20():
        OP_8C(0xFE, 360, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E20)
    Sleep(50)

    def lambda_1E33():
        OP_8C(0xFE, 360, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1E33)
    Sleep(50)

    def lambda_1E46():
        OP_8C(0xFE, 360, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1E46)
    Sleep(50)

    def lambda_1E59():
        OP_8C(0xFE, 360, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1E59)
    Sleep(500)
    Fade(1000)
    OP_6D(79890, 1500, 146670, 0)
    OP_67(0, 7730, -10000, 0)
    OP_6B(1930, 0)
    OP_6C(33000, 0)
    OP_6E(589, 0)
    OP_0D()

    ChrTalk(    #80
        0x101,
        "#1004F#5PYou're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x1A,
        (
            "#070FThat's the royal family's personal cruiser,\x01",
            "right?\x02\x03",

            "It might be out on a mission or something.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(79270, 1500, 142560, 0)
    OP_67(0, 6970, -10000, 0)
    OP_6B(3820, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_1F7C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F7C)
    Sleep(50)

    def lambda_1F8F():
        OP_8C(0xFE, 177, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1F8F)
    Sleep(50)

    def lambda_1FA2():
        OP_8C(0xFE, 177, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1FA2)
    Sleep(50)

    def lambda_1FB5():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1FB5)
    Sleep(500)

    ChrTalk(    #82
        0x18,
        (
            "#040FIf I recall, the Arseille should be at\x01",
            "Leiston Fortress at the moment.\x02\x03",

            "It's being fitted with the new engine\x01",
            "Professor Russell and his colleagues\x01",
            "have been working on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x19,
        (
            "#061FOh, yeah! Gustav said he'd be flying out\x01",
            "to Leiston on the factory's airship!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1004FOh, I see!\x02\x03",

            "#1006FSo that awesome ship is being made\x01",
            "even MORE awesome?\x02\x03",

            "I seriously can't wait to see that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x19,
        (
            "#560FThey're just changing the engine, so\x01",
            "I doubt the exterior will change much...\x02\x03",

            "#061FBut it'll totally be the world's fastest\x01",
            "airship! That's for sure! ♪\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1A3B end

    def Function_14_2206(): pass

    label("Function_14_2206")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x10522, 0x5DC, 0x22FA6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_2206 end

    def Function_15_2263(): pass

    label("Function_15_2263")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x130A6, 0x5DC, 0x22ED4, 0x7D0, 0x0)
    OP_8C(0xFE, 102, 400)
    Return()

    # Function_15_2263 end

    def Function_16_22C2(): pass

    label("Function_16_22C2")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13C54, 0x5DC, 0x22EE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13448, 0x5DC, 0x22B50, 0x7D0, 0x0)
    OP_8C(0xFE, 357, 400)
    Return()

    # Function_16_22C2 end

    def Function_17_2335(): pass

    label("Function_17_2335")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13C54, 0x5DC, 0x22EE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13380, 0x5DC, 0x23212, 0x7D0, 0x0)
    OP_8C(0xFE, 177, 400)
    Return()

    # Function_17_2335 end

    def Function_18_23A8(): pass

    label("Function_18_23A8")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13C54, 0x5DC, 0x22EE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13808, 0x5DC, 0x22B8C, 0x7D0, 0x0)
    OP_8C(0xFE, 357, 400)
    Return()

    # Function_18_23A8 end

    def Function_19_241B(): pass

    label("Function_19_241B")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13C54, 0x5DC, 0x22EE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13858, 0x5DC, 0x23208, 0x7D0, 0x0)
    OP_8C(0xFE, 201, 400)
    Return()

    # Function_19_241B end

    def Function_20_248E(): pass

    label("Function_20_248E")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13C54, 0x5DC, 0x22EE8, 0x7D0, 0x0)
    OP_8C(0xFE, 261, 400)
    Return()

    # Function_20_248E end

    def Function_21_24ED(): pass

    label("Function_21_24ED")


    def lambda_24F3():
        OP_6D(58630, 30000, 116260, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_24F3)

    def lambda_250B():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_250B)

    def lambda_2526():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2526)
    Sleep(100)

    def lambda_2546():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2546)
    Sleep(100)

    def lambda_2566():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2566)
    Sleep(100)

    def lambda_2586():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2586)
    Sleep(100)

    def lambda_25A6():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_25A6)
    Sleep(100)

    def lambda_25C6():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_25C6)
    Sleep(100)

    def lambda_25E6():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_25E6)
    Sleep(100)

    def lambda_2606():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2606)
    Sleep(100)
    Sleep(4000)

    def lambda_262B():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_262B)

    def lambda_2646():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2646)
    Sleep(300)

    def lambda_2666():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2666)
    Sleep(300)

    def lambda_2686():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2686)
    Sleep(300)

    def lambda_26A6():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_26A6)
    Sleep(300)

    def lambda_26C6():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_26C6)
    Sleep(300)

    def lambda_26E6():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_26E6)
    Sleep(300)

    def lambda_2706():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2706)
    Sleep(300)

    def lambda_2726():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2726)
    Sleep(300)

    def lambda_2746():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2746)

    def lambda_2761():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2761)
    WaitChrThread(0x1F, 0x1)
    WaitChrThread(0x20, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x1F, 87140, -5650, 130979, 90)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x1)
    Sleep(1300)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 100)
    OP_70(0x5, 0xC8)
    Sleep(2500)
    OP_44(0x0, 0x1)
    Return()

    # Function_21_24ED end

    def Function_22_27E4(): pass

    label("Function_22_27E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27F1")
    Return()

    label("loc_27F1")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2811")
    Call(0, 29)
    Call(0, 30)
    FadeToBright(0, 0)

    label("loc_2811")

    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #86
        (
            "\x07\x05The Zeiss-bound passenger liner 'Linde'\x01",
            "will be departing momentarily.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #87
        "\x07\x05All passengers, please board immediately.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(1000)
    OP_71(0x9, 0x4)
    OP_6F(0x5, 1)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x40)
    OP_4A(0x17, 255)
    OP_4A(0x1B, 255)
    SetChrPos(0x17, 82970, 1500, 143180, 180)
    SetChrPos(0x1B, 82970, 1500, 139130, 180)

    def lambda_291A():
        OP_8E(0xFE, 0x1446A, 0x5DC, 0x20B70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_291A)
    OP_6D(82960, 1500, 138300, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    OP_22(0x75, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x1B, 0x1)
    OP_8C(0x1B, 0, 400)
    OP_E5(0x17, 0x0, 0x0)
    Sleep(500)

    ChrTalk(    #88
        0x1B,
        (
            "#270FFarewell, Olivier.\x02\x03",

            "I don't know why I'm even bothering,\x01",
            "but for goodness' sake, please stay\x01",
            "out of trouble while I'm away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x17,
        (
            "#037F#1PAh, such sweet concern! My heart, it soars!\x02\x03",

            "But fear not. Have I ever made you worry,\x01",
            "my dearest Mueller?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x1B,
        (
            "#272FAt this point I can't bring myself to\x01",
            "care enough to worry about you.\x02\x03",

            "Just...no international incidents.\x01",
            "PLEASE.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x17,
        "#031F#1PFor you, my beloved, I'll do my best.\x02",
    )

    CloseMessageWindow()
    OP_A1(0x1F, 0xA)
    OP_72(0xA, 0x4)
    OP_72(0xA, 0x20)
    SetChrPos(0x1F, 87140, -5650, 130979, 90)
    SetChrFlags(0x1F, 0x4)
    OP_A1(0x20, 0xB)
    SetChrPos(0x20, 87140, -5650, 130979, 90)
    SetChrFlags(0x20, 0x4)
    Fade(500)
    OP_72(0xB, 0x4)
    OP_0D()
    Call(0, 23)
    Sleep(1000)
    OP_6D(82970, 1500, 143180, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(151000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 76000, 1500, 142810, 90)
    SetChrPos(0x107, 76000, 1500, 143700, 90)
    SetChrPos(0xF7, 76000, 1500, 144000, 90)
    SetChrPos(0xF9, 76000, 1500, 142470, 90)
    SetChrPos(0x1C, 70560, 1500, 143120, 90)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 70560, 1500, 143120, 90)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #92
        0x101,
        "#1PHeeeey! Olivier!\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x17, 0x101, 400)

    def lambda_2C77():
        OP_6D(82140, 1500, 142960, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2C77)

    def lambda_2C8F():
        OP_8E(0xFE, 0x1398E, 0x5DC, 0x22DDA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C8F)
    Sleep(100)

    def lambda_2CAF():
        OP_8E(0xFE, 0x139F2, 0x5DC, 0x23154, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2CAF)
    Sleep(700)

    def lambda_2CCF():
        OP_8E(0xFE, 0x135EC, 0x5DC, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2CCF)
    Sleep(100)

    def lambda_2CEF():
        OP_8E(0xFE, 0x135EC, 0x5DC, 0x22C86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2CEF)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #93
        0x17,
        (
            "#033F#6PAh, everyone.\x02\x03",

            "#031FHave you missed me so that you came\x01",
            "to look for me? I am touched!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D77():
        OP_8E(0xFE, 0x12728, 0x5DC, 0x22F10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2D77)

    ChrTalk(    #94
        0x101,
        (
            "#1007F#4PAs if.\x02\x03",

            "#1015FAnyway, wasn't that...Mueller?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2E19")

    ChrTalk(    #95
        0x106,
        (
            "#052FWhat's the deal with an Imp officer\x01",
            "taking a passenger liner?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E65")

    label("loc_2E19")


    ChrTalk(    #96
        0x103,
        (
            "#023FWhy was a member of the Imperial\x01",
            "Army boarding a passenger liner?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E65")


    ChrTalk(    #97
        0x17,
        (
            "#030F#6PAh! It seems his duties have called\x01",
            "him to Bose temporarily.\x02\x03",

            "You recall that gang of sky bandits,\x01",
            "yes?\x02\x03",

            "He has gone to retrieve their airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1004F#4POh, yeah, that little green bucket\x01",
            "they had.\x02\x03",

            "But, wait, why would Mueller care?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x17,
        (
            "#035F#6PAhh, the ship is of Erebonian manufacture,\x01",
            "remember.\x02\x03",

            "And the bandits who abused it so are\x01",
            "still at large.\x02\x03",

            "#030FThe Imperial government would like to\x01",
            "retrieve the evidence--that is, the ship--\x01",
            "and assist in capturing the criminals.\x02\x03",

            "Or, at least, that is what they have told\x01",
            "Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1015F#4PUhhhhh... I still don't get why Erebonia\x01",
            "should care. So the airship was made\x01",
            "there, so what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x17,
        (
            "#031F#6PWell, the fact that the bandit leaders are\x01",
            "former Erebonian nobility...tarnishes\x01",
            "Erebonia's luster, shall we say.\x02\x03",

            "I suspect they'd like to have it well swept\x01",
            "under the floorboards before the pact is\x01",
            "signed.\x02\x03",

            "That is, before the Republic has a chance\x01",
            "to comment on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1015F#4PThe bandits are former--\x02\x03",

            "#1020FWait a minute!\x01",
            "That tomboy and her brothers're...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x17,
        (
            "#033F#6PYou...were truly unaware?\x02\x03",

            "#030FThey are the family of the former\x01",
            "Baron Capua. He was a landholder\x01",
            "on the Empire's northern march.\x02\x03",

            "Several years ago, the Capua lands\x01",
            "were seized as collateral in payment\x01",
            "for an enormous debt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1015F#4PWhoa, I never realized.\x02\x03",

            "#1007FThat's...really sad, actually.\x01",
            "I dunno what to say to that...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_340B")

    ChrTalk(    #105
        0x106,
        "#053FPfft. They don't get any sympathy from me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3464")

    label("loc_340B")


    ChrTalk(    #106
        0x103,
        (
            "#027FEven so, it isn't exactly what I'd call an\x01",
            "airtight excuse for airborne theft.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3464")


    ChrTalk(    #107
        0x17,
        (
            "#035F#6PRegardless! I came to see my\x01",
            "stalwart companion off.\x02\x03",

            "#030FI'm afraid none of this explains why you're\x01",
            "here, though, if you did not come for the\x01",
            "undeniable pleasure of my company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1015F#4PWe're looking for Renne...\x02\x03",

            "You haven't seen her, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x17,
        (
            "#033F#6PRenne?\x02\x03",

            "Isn't she standing right over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#1004F#4PUh...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 75560, 1500, 143120, 90)

    def lambda_35D9():
        OP_6D(79810, 1500, 142310, 1600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35D9)

    def lambda_35F1():
        OP_67(0, 5590, -10000, 1600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_35F1)

    def lambda_3609():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3609)
    Sleep(100)

    def lambda_361C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_361C)
    Sleep(100)

    def lambda_362F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_362F)
    Sleep(100)

    def lambda_3642():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3642)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #111
        0x1C,
        "#261F#2PHeeheehee. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x107,
        "#065F#6PRenne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1020F#6PWhat...? When did she...?\x02",
    )

    CloseMessageWindow()

    def lambda_36AC():
        OP_6D(78000, 1500, 142310, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36AC)
    OP_8E(0x101, 0x12D72, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #114
        0x101,
        (
            "#1019F#6PErgh! Hey, RENNE!\x02\x03",

            "You CANNOT just disappear\x01",
            "like that, okay?!\x02\x03",

            "And not only that, but you ran\x01",
            "away from us and confused a whole\x01",
            "bunch of people in the process, and--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x1C,
        (
            "#268F#2PI'm sorry...but I was soooooooo bored!\x02\x03",

            "#267FAlso, um, I bought some cookies and\x01",
            "tea at the department store.\x02\x03",

            "I bought enough for everyone, so please\x01",
            "don't be mad...okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1015F#6PEr...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38C8")

    ChrTalk(    #117
        0x108,
        (
            "#071F#6PHaha! Oh, admit it, Estelle.\x01",
            "We had a good time, too.\x02\x03",

            "What say we call it even?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_393A")

    label("loc_38C8")


    ChrTalk(    #118
        0x105,
        (
            "#048F#6PHaha. Well...it WAS quite a bit of fun\x01",
            "for us, too, Estelle.\x02\x03",

            "Let's just call it even and let it go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_393A")


    ChrTalk(    #119
        0x101,
        (
            "#1007F#6P*siiiiigh* I suppose.\x02\x03",

            "#1017FOkay, you get to escape a scolding.\x01",
            "For now, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x1C,
        "#265F#2PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x107,
        "#061FYay, Renne! Good job!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3A59")

    ChrTalk(    #122
        0x106,
        (
            "#051F#6PAllllll right. With that out of the way,\x01",
            "we need to head back to the\x01",
            "guildhouse.\x02\x03",

            "Some new info might've come in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD3")

    label("loc_3A59")


    ChrTalk(    #123
        0x103,
        (
            "#021F#6PShall we return to the guildhouse\x01",
            "with feast in hand, then?\x02\x03",

            "It's possible some new information\x01",
            "has come in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD3")


    def lambda_3AD9():
        OP_6D(79810, 1500, 142310, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AD9)
    TurnDirection(0x101, 0x17, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #124
        0x101,
        "#1006F#2PRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x17,
        "#033FHm? Has something happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1015F#2PApparently there's something going\x01",
            "on in Bose...\x02\x03",

            "#1004FEr. Wait. Didn't you say Mueller is\x01",
            "going to Bose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x17,
        (
            "#032F...So he is.\x02\x03",

            "Come. Tell me the details as we walk.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x17, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3C1B")

    ChrTalk(    #128
        0x106,
        "#051F#2PRight, then, c'mon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C37")

    label("loc_3C1B")


    ChrTalk(    #129
        0x103,
        "#020F#2PYes, let's go.\x02",
    )

    CloseMessageWindow()

    label("loc_3C37")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T4100   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_22_27E4 end

    def Function_23_3C54(): pass

    label("Function_23_3C54")

    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x64)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0xA, 1)
    OP_70(0xA, 0x3C)
    OP_73(0xA)
    Sleep(1000)
    OP_23(0x75)
    OP_22(0x77, 0x1, 0x64)
    OP_6F(0xA, 61)
    OP_70(0xA, 0xA0)
    Fade(1000)
    SetChrFlags(0x1B, 0x80)
    OP_72(0x9, 0x4)
    ClearMapFlags(0x10)
    OP_6D(63630, 30000, 116260, 0)
    OP_67(0, 45000, -50000, 0)
    OP_6B(750, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    OP_73(0x4)
    OP_71(0xA, 0x20)
    OP_6F(0xA, 161)
    OP_70(0xA, 0x104)
    OP_91(0x1F, 0x0, 0x12C, 0x0, 0x12C, 0x0)
    OP_91(0x1F, 0x0, 0x320, 0x0, 0x1F4, 0x0)
    Sleep(2000)

    def lambda_3D37():
        OP_6D(75000, 30000, 116260, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D37)

    def lambda_3D4F():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3D4F)
    OP_94(0x1, 0x1F, 0x0, 0x3E8, 0x3E8, 0x0)

    def lambda_3D74():
        OP_94(0x1, 0xFE, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3D74)
    OP_94(0x1, 0x1F, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_3D99():
        OP_94(0x1, 0xFE, 0x0, 0x578, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3D99)
    OP_94(0x1, 0x1F, 0x0, 0x578, 0xBB8, 0x0)

    def lambda_3DBE():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3DBE)
    OP_94(0x1, 0x1F, 0x0, 0x640, 0xFA0, 0x0)

    def lambda_3DE3():
        OP_94(0x1, 0xFE, 0x0, 0x708, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3DE3)
    OP_94(0x1, 0x1F, 0x0, 0x708, 0x1388, 0x0)

    def lambda_3E08():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3E08)
    OP_94(0x1, 0x1F, 0x0, 0x7D0, 0x1770, 0x0)

    def lambda_3E2D():
        OP_94(0x1, 0xFE, 0x0, 0x898, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3E2D)
    OP_94(0x1, 0x1F, 0x0, 0x898, 0x1B58, 0x0)
    FadeToDark(2000, 0, -1)

    def lambda_3E5C():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3E5C)

    def lambda_3E72():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3E72)
    OP_24(0x77, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    Sleep(100)
    OP_24(0x77, 0x14)
    Sleep(100)
    OP_24(0x77, 0xA)
    Sleep(100)
    OP_23(0x77)
    OP_0D()
    OP_44(0x101, 0x0)
    Return()

    # Function_23_3C54 end

    def Function_24_3EDC(): pass

    label("Function_24_3EDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    OP_6D(84620, 1500, 135300, 0)
    OP_67(0, 4280, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(135000, 0)
    OP_6E(364, 0)
    OP_6D(118730, 1500, 138330, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(4810, 0)
    OP_6C(261000, 0)
    OP_6E(364, 0)
    StopSound(0x9C40, 0x493E0, 0x0)
    SetChrPos(0x101, 83430, 1700, 133650, 0)
    SetChrPos(0x102, 82500, 1700, 133620, 0)
    SetChrPos(0x21, 83700, 1700, 132200, 0)
    SetChrPos(0x18, 84600, 1700, 133240, 0)
    SetChrPos(0x19, 81670, 1700, 133310, 0)
    SetChrPos(0x22, 81540, 1700, 132400, 0)
    SetChrPos(0x23, 82880, 1700, 131700, 0)
    SetChrPos(0x1A, 84900, 1700, 131800, 0)
    SetChrPos(0x17, 82910, 1700, 141060, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_72(0x5, 0x4)
    OP_71(0x9, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_6F(0x5, 200)
    OP_6F(0xA, 0)
    OP_75(0xB, 0x0, 0x0)
    OP_74(0xB, 0x0, 0x0)
    FadeToBright(1000, 0)

    def lambda_4095():
        OP_6D(81880, 1500, 137450, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4095)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(84620, 1500, 135300, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(135000, 0)
    OP_6E(364, 0)
    StopSound(0x9C40, 0x2BF20, 0x0)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #130
        0x101,
        (
            "#1007F#4PMmm, I didn't expect you'd have\x01",
            "to go back to Erebonia, Olivier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x21,
        "#524F#4PIt is a bit out of the blue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x17,
        (
            "#035FNo, to be honest, I was due back\x01",
            "some time ago.\x02\x03",

            "#030FHowever, you, Estelle so monopolized\x01",
            "my time, I delayed my return for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        "#1025F#4PI see... Sorry, I guess it's my fault.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x17,
        (
            "#031FHeh, not at all. Don't you worry\x01",
            "your precious head over it.\x02\x03",

            "In return for my accompanying you\x01",
            "hither and yon, I was able to reunite\x01",
            "with my dear, sweet Joshua, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        (
            "#1049F#4PHaha. You're the same\x01",
            "as always, Olivier.\x02\x03",

            "#1043F...Say, Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x17,
        "#030FWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        (
            "#1042F#4PYou...\x02\x03",

            "#1035F...No, never mind.\x02\x03",

            "#1040FThank you for taking the time\x01",
            "to help Estelle on her journeys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x17,
        (
            "#035FHeh, I merely followed my whims.\x01",
            "You need not be so guarded.\x02\x03",

            "#037FThough, if you insist on a\x01",
            "passionate farewell kiss, well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1019F#4PYeah, no, that's enough, thanks.\x02\x03",

            "#1025FHa... Can't you say goodbye\x01",
            "seriously at least once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x17,
        (
            "#035FHaha, I thought you would have\x01",
            "learned by now that I am always\x01",
            "serious!\x02\x03",

            "#030FEstelle, Joshua, Schera, everyone.\x02\x03",

            "You have great trials ahead\x01",
            "of you, so be careful.\x02\x03",

            "#031FKnow that Olivier Lenheim shall pray for\x01",
            "your success from the skies of Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#1006F#4PThanks, Olivier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x21,
        "#021F#4PHeehee... You take care, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x102,
        "#1054F#4PStay safe...Olivier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x1A,
        (
            "#071FIf we get the chance, we\x01",
            "should go drinking again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x22,
        (
            "#051FNext time we meet, try ditchin' the\x01",
            "love-struck idiot act, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x19,
        "#067F#4PUm, haha... Goodbye, Olivier!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x23,
        (
            "#1061FDidn't know ya long, but it\x01",
            "was good times! See ya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x18,
        (
            "#048FFarewell, Olivier...\x01",
            "Thank you for your help!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_B7(0x3)
    OP_A2(0x10F8)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3EDC end

    def Function_25_4783(): pass

    label("Function_25_4783")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_6D(73560, 250, 132340, 0)
    OP_67(0, 8020, -10000, 0)
    OP_6B(5850, 0)
    OP_6C(285000, 0)
    OP_6E(404, 0)
    StopSound(0x9C40, 0x493E0, 0x0)
    SetChrPos(0x17, 82620, 1500, 143550, 135)
    ClearChrFlags(0x17, 0x80)
    OP_E5(0x17, 0x0, 0x0)
    OP_A1(0x1F, 0xA)
    OP_72(0xA, 0x4)
    OP_72(0xA, 0x20)
    SetChrPos(0x1F, 89000, 200, 130000, 90)
    SetChrFlags(0x1F, 0x4)
    OP_A1(0x20, 0xB)
    OP_72(0xB, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 89000, -4800, 130000, 90)
    OP_75(0xB, 0x0, 0x0)
    OP_74(0xB, 0x0, 0x0)
    OP_72(0x5, 0x4)
    OP_6F(0x5, 200)
    OP_6F(0xA, 1)
    OP_22(0x75, 0x0, 0x64)

    def lambda_48A3():
        OP_6D(93000, 1250, 131420, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_48A3)

    def lambda_48BB():
        OP_67(0, 4500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48BB)

    def lambda_48D3():
        OP_6B(5850, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48D3)

    def lambda_48E3():
        OP_6C(285000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_48E3)

    def lambda_48F3():
        OP_6E(471, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_48F3)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 200)
    OP_70(0x5, 0x64)
    Sleep(1000)
    OP_23(0x75)
    OP_22(0x125, 0x0, 0x64)
    OP_43(0x1F, 0x0, 0x0, 0x1C)
    Sleep(3000)
    OP_91(0x1F, 0x0, 0x1F4, 0x0, 0x190, 0x0)
    OP_91(0x1F, 0x0, 0x3E8, 0x0, 0x320, 0x0)
    OP_91(0x1F, 0x0, 0x7D0, 0x0, 0x640, 0x0)
    OP_91(0x1F, 0x0, 0x1F4, 0x0, 0x320, 0x0)
    OP_91(0x1F, 0x0, 0x190, 0x0, 0x190, 0x0)

    def lambda_49A1():
        OP_6D(105490, 1500, 130810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49A1)

    def lambda_49B9():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_49B9)

    def lambda_49D4():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_49D4)
    Sleep(200)

    def lambda_49F4():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_49F4)

    def lambda_4A0F():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4A0F)
    Sleep(200)

    def lambda_4A2F():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4A2F)

    def lambda_4A4A():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4A4A)
    Sleep(200)

    def lambda_4A6A():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4A6A)

    def lambda_4A85():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4A85)
    Sleep(200)

    def lambda_4AA5():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4AA5)

    def lambda_4AC0():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4AC0)
    Sleep(200)

    def lambda_4AE0():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4AE0)

    def lambda_4AFB():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4AFB)
    Sleep(200)

    def lambda_4B1B():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4B1B)

    def lambda_4B36():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4B36)
    Sleep(200)

    def lambda_4B56():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4B56)

    def lambda_4B71():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4B71)
    Sleep(200)

    def lambda_4B91():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4B91)

    def lambda_4BAC():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4BAC)
    Sleep(200)

    def lambda_4BCC():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4BCC)

    def lambda_4BE7():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4BE7)
    Sleep(200)

    def lambda_4C07():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4C07)

    def lambda_4C22():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4C22)
    Sleep(200)

    def lambda_4C42():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4C42)

    def lambda_4C5D():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4C5D)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    OP_24(0x125, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    OP_24(0x125, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    OP_24(0x125, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    OP_24(0x125, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    OP_24(0x125, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    OP_24(0x125, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    OP_24(0x125, 0x1E)
    Sleep(100)
    OP_23(0x77)
    OP_23(0x125)
    Fade(1000)
    OP_44(0x101, 0x3)
    StopSound(0x9C40, 0x2BF20, 0x0)
    OP_6D(83010, 1500, 142960, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(134000, 0)
    OP_6E(302, 0)
    OP_8C(0x17, 90, 0)
    OP_0D()
    Sleep(1000)
    OP_DC()

    ChrTalk(    #149
        0x17,
        (
            "#035FHeh... And so ends the moratorium\x01",
            "I placed upon myself.\x02\x03",

            "#030FNo, I may yet have one\x01",
            "chance left, perhaps.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x1E, 71940, 750, 143010, 90)
    SetChrChipByIndex(0x1E, 18)
    SetChrPos(0x1D, 71700, 750, 144070, 90)
    ClearChrFlags(0x1D, 0x80)

    def lambda_4DE0():

        label("loc_4DE0")

        OP_9E(0xFE, 0x32, 0x0, 0x1F4, 0x3E8)
        OP_48()
        Jump("loc_4DE0")

    QueueWorkItem2(0x1D, 1, lambda_4DE0)

    NpcTalk(    #150
        0x1E,
        "Girl's Voice",
        "#1PW-Waaaaaaaaait!\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4E39():
        TurnDirection(0xFE, 0x1E, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4E39)
    ClearChrFlags(0x1E, 0x80)

    def lambda_4E4C():
        OP_6D(81940, 1500, 142800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E4C)

    def lambda_4E64():
        OP_8E(0x1E, 0x139E8, 0x5DC, 0x22FCE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4E64)
    Sleep(500)

    def lambda_4E84():
        OP_8E(0xFE, 0x1340C, 0x5DC, 0x231FE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_4E84)
    WaitChrThread(0x1E, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #151
        0x17,
        "#033F#6PAh, you two.\x02",
    )

    WaitChrThread(0x1D, 0x2)
    OP_44(0x1D, 0x1)
    CloseMessageWindow()

    ChrTalk(    #152
        0x1E,
        "#152F#2PAwwww, they're gone!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp032_00.eff")

    ChrTalk(    #153
        0x1D,
        (
            "#145FHooh, haah... Didn't make\x01",
            "it in time, huh? Hooh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x17,
        (
            "#030F#6PWhat ho, good reporters?\x02\x03",

            "Were you hoping to get on board\x01",
            "as you did during the dragon case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x1D,
        (
            "#141FYeah, and we heard Joshua was back.\x02\x03",

            "#144FAh, whatever. Dorothy! Hurry up\x01",
            "and grab a shot of the Arseille.\x02\x03",

            "If you use the long-distance lens, we\x01",
            "should be able to get a useable shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x1E,
        "#151F#5PAye, aye, sir!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 180, 400)
    OP_43(0x17, 0x0, 0x0, 0x1B)
    Sleep(300)

    def lambda_509A():
        OP_6D(88040, 1500, 142240, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_509A)

    def lambda_50B2():
        OP_67(0, 5680, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50B2)

    def lambda_50CA():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50CA)

    def lambda_50DA():
        OP_8E(0x1E, 0x155F4, 0x5DC, 0x22EF2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_50DA)
    Sleep(300)

    def lambda_50FA():
        OP_8E(0x1D, 0x14D0C, 0x5DC, 0x230A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_50FA)
    WaitChrThread(0x1E, 0x0)
    SetChrSubChip(0x1E, 0)
    SetChrChipByIndex(0x1E, 19)
    Sleep(500)
    OP_A2(0x0)
    OP_43(0x1E, 0x1, 0x0, 0x1A)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x17, 0x0)
    Sleep(1000)

    ChrTalk(    #157
        0x17,
        "#031F#2PHeheh...heh.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrPos(0x1B, 67260, 0, 143120, 90)
    ClearChrFlags(0x1B, 0x80)
    OP_8C(0x17, 0, 400)
    OP_8E(0x17, 0x1428A, 0x5DC, 0x23050, 0x7D0, 0x0)

    def lambda_5197():
        OP_8E(0x17, 0x1113E, 0x0, 0x22F10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_5197)
    Sleep(2500)
    OP_A3(0x0)
    Fade(1000)
    OP_6D(73250, 0, 141910, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(134000, 0)
    OP_6E(325, 0)
    OP_20(0xBB8)

    def lambda_5201():
        OP_6D(70250, 0, 141910, 3000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5201)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x17, 0x1)
    Sleep(500)

    ChrTalk(    #158
        0x1B,
        "#270F...You've said your goodbyes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x17,
        (
            "#035F#6PSuch as they were to make, yes.\x02\x03",

            "#030FHow have your preparations come along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x1B,
        (
            "#277FI managed to arrange everything\x01",
            "with my uncle.\x02\x03",

            "As for Chancellor Osborne, he actually\x01",
            "found the idea to be perfectly timed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x17,
        (
            "#030F#6PHe does seem like the kind of man who\x01",
            "would be well liked by Liberlians.\x02\x03",

            "#035FHeh. This will be a grand processional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x1B,
        (
            "#272F*sigh*\x01",
            "You have the nastiest hobbies.\x02\x03",

            "#276FI can already see their shocked\x01",
            "expressions in my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x17,
        (
            "#031F#6PHa-ha-ha! Ah, but that is a large\x01",
            "part of the goal, my friend.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5474():
        OP_6D(71920, 750, 143050, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5474)

    def lambda_548C():
        OP_67(0, 4720, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_548C)

    def lambda_54A4():
        OP_6B(2570, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_54A4)

    def lambda_54B4():
        OP_6C(122000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54B4)

    def lambda_54C4():
        OP_6E(325, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_54C4)
    OP_8C(0x17, 90, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(300)

    ChrTalk(    #164
        0x17,
        (
            "#030F#2P(And so, when next we meet,\x01",
            "we shall be foes.)\x02\x03",

            "#035F(Do not lose to the likes of the society,\x01",
            "my erstwhile Liberlian allies.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_0D()
    OP_A2(0x10FF)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_4783 end

    def Function_26_558C(): pass

    label("Function_26_558C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5614")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x1E, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x1E, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("Function_26_558C")

    label("loc_5614")

    Return()

    # Function_26_558C end

    def Function_27_5615(): pass

    label("Function_27_5615")

    OP_8E(0xFE, 0x143B6, 0x6A4, 0x22920, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_27_5615 end

    def Function_28_5631(): pass

    label("Function_28_5631")

    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xA, 1)
    OP_70(0xA, 0x96)
    OP_73(0xA)
    OP_6F(0xA, 151)
    OP_70(0xA, 0x14A)
    Sleep(3200)
    OP_75(0xB, 0x0, 0x2)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0xB, 0x0, 0x1)
    Sleep(250)
    OP_74(0xB, 0x0, 0x2)
    Sleep(250)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0xB, 0x0, 0x3)
    Sleep(250)
    OP_74(0xB, 0x0, 0x4)
    Sleep(250)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0xB, 0x0, 0x5)
    Sleep(250)
    OP_74(0xB, 0x0, 0x6)
    Sleep(250)
    OP_74(0xB, 0x0, 0x7)
    OP_73(0xA)
    OP_71(0xA, 0x20)
    OP_6F(0xA, 330)
    OP_70(0xA, 0x1AE)
    Return()

    # Function_28_5631 end

    def Function_29_56E4(): pass

    label("Function_29_56E4")

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
        (0, "loc_575D"),
        (1, "loc_5763"),
        (SWITCH_DEFAULT, "loc_5769"),
    )


    label("loc_575D")

    OP_A2(0x1200)
    Jump("loc_5769")

    label("loc_5763")

    OP_A2(0x1201)
    Jump("loc_5769")

    label("loc_5769")

    Return()

    # Function_29_56E4 end

    def Function_30_576A(): pass

    label("Function_30_576A")

    ClearMapFlags(0x1)
    OP_6D(12790, 0, 144090, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_57A9")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_57C3")

    label("loc_57A9")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_57C3")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_30_576A end

    def Function_31_57E3(): pass

    label("Function_31_57E3")

    ClearMapFlags(0x1)
    OP_6D(12790, 0, 144090, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5828")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_5848")

    label("loc_5828")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)

    label("loc_5848")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_31_57E3 end

    def Function_32_5868(): pass

    label("Function_32_5868")

    Sleep(2000)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x3E8)
    OP_DE("Grancel")
    Return()

    # Function_32_5868 end

    def Function_33_588C(): pass

    label("Function_33_588C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #165
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "⇒ To Rolent\x01",
            "⇒ To Zeiss\x01",
            "⇒ To Calvard\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #166
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_33_588C end

    def Function_34_5955(): pass

    label("Function_34_5955")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #167
        (
            "\x07\x05Traffic Control Tower\x01",
            "※All unauthorized personnel are prohibited.\x01",
            "《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_34_5955 end

    SaveToFile()

Try(main)
