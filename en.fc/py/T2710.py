from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2710   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2710.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2710   ._SN',
            'ED6_DT01/T2710_1 ._SN',
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
        'CWO Hahn',                             # 9
        'Warrant Officer Kientz',               # 10
        'Private Cromwell',                     # 11
        'Mikelson',                             # 12
        'Lindsay',                              # 13
        'Bartholomew',                          # 14
        'Joshua',                               # 15
        'Targeting Camera',                     # 16
        'Duke Dunan',                           # 17
        'Butler Phillip',                       # 18
        'Caesar',                               # 19
        'Gary',                                 # 20
        'Tia',                                  # 21
        'Private Orta',                         # 22
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
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
        'ED6_DT07/CH01220 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH00010 ._CH',             # 05
        'ED6_DT07/CH02140 ._CH',             # 06
        'ED6_DT07/CH02470 ._CH',             # 07
        'ED6_DT07/CH01270 ._CH',             # 08
        'ED6_DT07/CH00100 ._CH',             # 09
        'ED6_DT07/CH00101 ._CH',             # 0A
        'ED6_DT07/CH02490 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01043 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01220P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH00010P._CP',             # 05
        'ED6_DT07/CH02140P._CP',             # 06
        'ED6_DT07/CH02470P._CP',             # 07
        'ED6_DT07/CH01270P._CP',             # 08
        'ED6_DT07/CH00100P._CP',             # 09
        'ED6_DT07/CH00101P._CP',             # 0A
        'ED6_DT07/CH02490P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01043P._CP',             # 0D
    )

    DeclNpc(
        X                   = 4750,
        Z                   = 0,
        Y                   = 90620,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2750,
        Z                   = 0,
        Y                   = 11470,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -4800,
        Z                   = 0,
        Y                   = 7900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -770,
        Z                   = 0,
        Y                   = 21500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -770,
        Z                   = 0,
        Y                   = 22500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -770,
        Z                   = 0,
        Y                   = 23500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 52155,
        Z                   = -3000,
        Y                   = 17688,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
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
        X                   = 4500,
        Z                   = 5000,
        Y                   = 0,
        Direction           = 90,
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
        X                   = 95300,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -3800,
        Z                   = 0,
        Y                   = 24700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 400,
        Z                   = 0,
        Y                   = 19200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 93480,
        Z                   = 0,
        Y                   = 85530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )


    DeclEvent(
        X                   = -6779,
        Y                   = -1000,
        Z                   = 1610,
        Range               = -5847,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x189C,
        Unknown_18          = 0x10000,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = -3939,
        Y                   = -1000,
        Z                   = 1820,
        Range               = 2122,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )


    DeclActor(
        TriggerX            = -2990,
        TriggerZ            = 0,
        TriggerY            = 7710,
        TriggerRange        = 1000,
        ActorX              = -4800,
        ActorZ              = 1500,
        ActorY              = 7900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 95800,
        TriggerZ            = 0,
        TriggerY            = 13660,
        TriggerRange        = 1000,
        ActorX              = 95300,
        ActorZ              = 1500,
        ActorY              = 16000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 93600,
        TriggerZ            = 0,
        TriggerY            = 87450,
        TriggerRange        = 1000,
        ActorX              = 93480,
        ActorZ              = 1500,
        ActorY              = 85530,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_386",          # 00, 0
        "Function_1_82A",          # 01, 1
        "Function_2_899",          # 02, 2
        "Function_3_967",          # 03, 3
        "Function_4_B3A",          # 04, 4
        "Function_5_D35",          # 05, 5
        "Function_6_FA9",          # 06, 6
        "Function_7_20F9",         # 07, 7
        "Function_8_2142",         # 08, 8
        "Function_9_302C",         # 09, 9
        "Function_10_3031",        # 0A, 10
        "Function_11_384D",        # 0B, 11
        "Function_12_3852",        # 0C, 12
        "Function_13_4764",        # 0D, 13
        "Function_14_49AC",        # 0E, 14
        "Function_15_4B03",        # 0F, 15
        "Function_16_4B08",        # 10, 16
        "Function_17_5563",        # 11, 17
        "Function_18_568B",        # 12, 18
    )


    def Function_0_386(): pass

    label("Function_0_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3A9")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3CC")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3EF")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_412")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_435")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_48B")
    SetChrPos(0x8, 4750, 0, 90620, 0)
    SetChrPos(0xA, -4800, 0, 7900, 90)
    SetChrPos(0x9, 2900, 0, 95100, 90)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_6FE")

    label("loc_48B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_680")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_518")
    SetChrPos(0x8, -2810, 0, 92600, 270)
    SetChrPos(0x9, 96840, 0, 14020, 339)
    SetChrPos(0xB, -3090, 0, 18660, 270)
    SetChrPos(0xC, -3860, 0, 19770, 270)
    SetChrPos(0xD, -2570, 0, 23890, 315)
    OP_44(0x13, 0xFF)
    SetChrChipByIndex(0x13, 13)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x13, 95610, 200, 7550, 180)
    Jump("loc_67D")

    label("loc_518")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_5F2")
    SetChrPos(0x8, 0, 0, 5250, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0xA, 92510, 0, 9380, 69)
    SetChrPos(0x9, 92630, 0, 12500, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -680, 0, 5220, 0)
    SetChrPos(0x13, 320, 0, 23610, 176)
    SetChrPos(0x14, -3790, 0, 19850, 141)
    SetChrPos(0xB, 0, 0, 6230, 270)
    SetChrPos(0xC, 670, 0, 5960, 270)
    SetChrPos(0xD, -800, 0, 5880, 315)
    OP_43(0xB, 0x1, 0x1, 0x8)
    OP_43(0xC, 0x1, 0x1, 0x9)
    OP_43(0xD, 0x1, 0x1, 0xA)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_67D")

    label("loc_5F2")

    SetChrPos(0xB, 1596, 0, 12441, 90)
    SetChrPos(0xC, 1513, 0, 13617, 90)
    SetChrPos(0xD, 909, 0, 13169, 90)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0x13, 320, 0, 23610, 176)
    SetChrPos(0x14, -3790, 0, 19850, 141)
    SetChrPos(0xA, 92510, 0, 9380, 69)
    SetChrPos(0x9, 92630, 0, 12500, 90)
    SetChrFlags(0x8, 0x80)

    label("loc_67D")

    Jump("loc_6FE")

    label("loc_680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_6FE")
    SetChrPos(0x8, 1970, 0, 94650, 270)
    SetChrPos(0xA, -50, 0, 94650, 90)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xC, -3860, 0, 19770, 270)
    SetChrPos(0xD, -2570, 0, 23890, 315)
    OP_44(0x13, 0xFF)
    SetChrChipByIndex(0x13, 13)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x13, 95610, 200, 7550, 180)

    label("loc_6FE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_716"),
        (101, "loc_787"),
        (102, "loc_7A8"),
        (103, "loc_7FC"),
        (SWITCH_DEFAULT, "loc_829"),
    )


    label("loc_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_784")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_746")
    OP_28(0x23, 0x1, 0x8000)
    Event(1, 0)
    Jump("loc_784")

    label("loc_746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_784")
    SetChrPos(0xB, 1596, 0, 12441, 90)
    SetChrPos(0xC, 1513, 0, 13617, 90)
    SetChrPos(0xD, 909, 0, 13169, 90)

    label("loc_784")

    Jump("loc_829")

    label("loc_787")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A5")
    Event(1, 1)

    label("loc_7A5")

    Jump("loc_829")

    label("loc_7A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D2")
    AddParty(0x1, 0xFF)
    OP_28(0x23, 0x4, 0x10)
    Event(1, 23)
    Jump("loc_7F9")

    label("loc_7D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F9")
    AddParty(0x1, 0xFF)
    OP_28(0x23, 0x4, 0x10)
    Event(1, 24)

    label("loc_7F9")

    Jump("loc_829")

    label("loc_7FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_826")
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    Event(1, 11)

    label("loc_826")

    Jump("loc_829")

    label("loc_829")

    Return()

    # Function_0_386 end

    def Function_1_82A(): pass

    label("Function_1_82A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_834")
    Jump("loc_86C")

    label("loc_834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_861")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_848")
    Jump("loc_85E")

    label("loc_848")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_85A")
    OP_64(0x0, 0x1)
    Jump("loc_85E")

    label("loc_85A")

    OP_64(0x0, 0x1)

    label("loc_85E")

    Jump("loc_86C")

    label("loc_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_86C")
    OP_64(0x0, 0x1)

    label("loc_86C")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_888"),
        (101, "loc_888"),
        (102, "loc_888"),
        (104, "loc_888"),
        (106, "loc_888"),
        (SWITCH_DEFAULT, "loc_890"),
    )


    label("loc_888")

    OP_22(0x1C6, 0x1, 0x64)
    Jump("loc_893")

    label("loc_890")

    OP_23(0x1C6)

    label("loc_893")

    OP_1C(0x3, 0x0, 0x12)
    Return()

    # Function_1_82A end

    def Function_2_899(): pass

    label("Function_2_899")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BE")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_951")

    label("loc_8BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D7")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_951")

    label("loc_8D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F0")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_951")

    label("loc_8F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_909")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_951")

    label("loc_909")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_922")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_951")

    label("loc_922")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_951")

    label("loc_93B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_951")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_951")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_966")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_951")

    label("loc_966")

    Return()

    # Function_2_899 end

    def Function_3_967(): pass

    label("Function_3_967")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_974")
    Jump("loc_B36")

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_97E")
    Jump("loc_B36")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_988")
    Jump("loc_B36")

    label("loc_988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_992")
    Jump("loc_B36")

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_9A3")
    Jump("loc_9A3")

    label("loc_9A3")

    Jump("loc_B36")

    label("loc_9A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_9B0")
    Jump("loc_B36")

    label("loc_9B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_AE4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A68")

    ChrTalk(    #0
        0xFE,
        (
            "*sigh* I even came here so\x01",
            "I could have some space to\x01",
            "think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Thanks to that stupid duke, I've\x01",
            "completely forgotten what it\x01",
            "was I wanted to think about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE1")

    label("loc_A68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_AB2")
    OP_4A(0xFE, 255)

    ChrTalk(    #2
        0xFE,
        (
            "You're a soldier, right?\x01",
            "Do something, already!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xFE, 255)
    Jump("loc_AE1")

    label("loc_AB2")


    ChrTalk(    #3
        0xFE,
        (
            "I can't see anything through\x01",
            "the keyhole.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE1")

    Jump("loc_B36")

    label("loc_AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_B36")

    ChrTalk(    #4
        0xFE,
        (
            "The ruins themselves have\x01",
            "become the waterfall, which\x01",
            "is fascinating.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B36")

    TalkEnd(0xB)
    Return()

    # Function_3_967 end

    def Function_4_B3A(): pass

    label("Function_4_B3A")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_B47")
    Jump("loc_D31")

    label("loc_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_B51")
    Jump("loc_D31")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_B5B")
    Jump("loc_D31")

    label("loc_B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_B65")
    Jump("loc_D31")

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_B76")
    Jump("loc_B76")

    label("loc_B76")

    Jump("loc_D31")

    label("loc_B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_B83")
    Jump("loc_D31")

    label("loc_B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_CC7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C00")

    ChrTalk(    #5
        0xFE,
        (
            "All that trouble to take this\x01",
            "trip, and the mood's completely\x01",
            "ruined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "I'm gonna sue that jerk!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC4")

    label("loc_C00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_C89")
    OP_4A(0xFE, 255)

    ChrTalk(    #7
        0xC,
        (
            "The Royal Army is supposed\x01",
            "to be on the side of the\x01",
            "citizens, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xC,
        "If so, then do something about this!\x02",
    )

    CloseMessageWindow()
    OP_4B(0xFE, 255)
    Jump("loc_CC4")

    label("loc_C89")


    ChrTalk(    #9
        0xFE,
        (
            "I wish someone would do\x01",
            "something about this\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC4")

    Jump("loc_D31")

    label("loc_CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_D31")

    ChrTalk(    #10
        0xFE,
        "Isn't this a beautiful place?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "You can see why it's one\x01",
            "of the sixteen wonders\x01",
            "of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D31")

    TalkEnd(0xC)
    Return()

    # Function_4_B3A end

    def Function_5_D35(): pass

    label("Function_5_D35")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_D42")
    Jump("loc_FA5")

    label("loc_D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_D4C")
    Jump("loc_FA5")

    label("loc_D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_D56")
    Jump("loc_FA5")

    label("loc_D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_D60")
    Jump("loc_FA5")

    label("loc_D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_D71")
    Jump("loc_D71")

    label("loc_D71")

    Jump("loc_FA5")

    label("loc_D74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_D7E")
    Jump("loc_FA5")

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_EFA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E36")

    ChrTalk(    #12
        0xFE,
        (
            "It looks like the bracers\x01",
            "managed to get everything\x01",
            "straightened out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I don't know how they got rid\x01",
            "of that selfish bastard, but\x01",
            "I'm glad they were here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF7")

    label("loc_E36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_E91")
    OP_4A(0xFE, 255)

    ChrTalk(    #14
        0xD,
        (
            "Are you just going to let\x01",
            "this kind of bullying go\x01",
            "unchallenged?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xFE, 255)
    Jump("loc_EF7")

    label("loc_E91")


    ChrTalk(    #15
        0xFE,
        (
            "I guess even a bracer is no\x01",
            "match for an 'upper crust'\x01",
            "jerk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "The future looks very bleak...\x02",
    )

    CloseMessageWindow()

    label("loc_EF7")

    Jump("loc_FA5")

    label("loc_EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_FA5")

    ChrTalk(    #17
        0xFE,
        (
            "First it was Manoria, with all the\x01",
            "beautiful flowers, then the port\x01",
            "town of Ruan, and now Air-Letten...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "This area has so many must-\x01",
            "see places, honestly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA5")

    TalkEnd(0xD)
    Return()

    # Function_5_D35 end

    def Function_6_FA9(): pass

    label("Function_6_FA9")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_10B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1023")
    OP_A2(0x0)

    ChrTalk(    #19
        0xFE,
        (
            "Hmm...\x01",
            "If we're getting new orders...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "...then the troublemaker\x01",
            "upstairs is still at it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B1")

    label("loc_1023")


    ChrTalk(    #21
        0xFE,
        (
            "Either way, our new orders\x01",
            "will be no walk in the park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I'll have to explain this to\x01",
            "my men, so there will be no\x01",
            "misunderstandings.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B1")

    Jump("loc_20F5")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1222")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A5")
    OP_A2(0x0)

    ChrTalk(    #23
        0xFE,
        (
            "The fact is, we've received orders \x01",
            "to cancel the inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Obviously, I'm not entirely\x01",
            "happy about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "But orders are orders. It's\x01",
            "not our place to judge them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "The same goes for those upstairs.\x02",
    )

    CloseMessageWindow()
    Jump("loc_121F")

    label("loc_11A5")


    ChrTalk(    #27
        0xFE,
        (
            "Still, if the inspections are\x01",
            "being called off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "...I really have to wonder what's\x01",
            "going on behind the scenes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121F")

    Jump("loc_20F5")

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_14FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146B")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_136D")

    ChrTalk(    #29
        0xFE,
        "Hello there, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I've already been briefed on\x01",
            "the attack at the central lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "This checkpoint will be conducting\x01",
            "strict inspections, in conjunction\x01",
            "with all other areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "There's no way that the\x01",
            "culprits will escape now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Relax. I'm sure they'll be\x01",
            "apprehended in no time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1468")

    label("loc_136D")


    ChrTalk(    #34
        0xFE,
        "Oh... Are you traveling?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "I'm sorry, but we have to conduct\x01",
            "an inspection, thanks to the\x01",
            "attack on the central lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Except for emergencies, no one\x01",
            "is allowed through without a\x01",
            "writ of passage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I suspect this will go on\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1468")

    Jump("loc_14F9")

    label("loc_146B")


    ChrTalk(    #38
        0xFE,
        (
            "Even the Royal Army is\x01",
            "cooperating fully with the\x01",
            "hunt for the terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I have no doubt that they'll\x01",
            "be taken into custody soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F9")

    Jump("loc_20F5")

    label("loc_14FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_164F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B7")
    OP_A2(0x0)

    ChrTalk(    #40
        0xFE,
        (
            "What happened last night\x01",
            "in Zeiss is of particular\x01",
            "interest to the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I'll bet that the intelligence\x01",
            "agencies are pulling their\x01",
            "hair out over this case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164C")

    label("loc_15B7")


    ChrTalk(    #42
        0xFE,
        (
            "The first priority is to get\x01",
            "everything back to normal,\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "The central lab in Zeiss\x01",
            "is a crucial asset for\x01",
            "the monarchy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164C")

    Jump("loc_20F5")

    label("loc_164F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1B7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 7)), scpexpr(EXPR_END)), "loc_17DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1718")
    OP_A2(0x0)

    ChrTalk(    #44
        0xFE,
        "Now, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Since the documents are in\x01",
            "order, I should go and check\x01",
            "on my men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "It sets a bad precedent if\x01",
            "I allow them to seclude\x01",
            "themselves in their rooms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DB")

    label("loc_1718")


    ChrTalk(    #47
        0xFE,
        (
            "Since the matter of His Grace\x01",
            "the Duke, the men seem to have\x01",
            "lost much of their self-confidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Heh. I confess it is a little\x01",
            "unnerving, but it is my duty\x01",
            "as their commanding officer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17DB")

    Jump("loc_1B7C")

    label("loc_17DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1941")
    OP_A2(0x0)

    ChrTalk(    #49
        0xFE,
        "Oh, hello again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "I'm still in your debt for your\x01",
            "actions when His Grace arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Thanks to you, he's not\x01",
            "causing any more trouble\x01",
            "for the other visitors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Though I still have doubts,\x01",
            "I'd be happy to cooperate with\x01",
            "the Bracer Guild in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "If anything else comes up, I\x01",
            "hope you'll be willing to help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C7")

    label("loc_1941")


    ChrTalk(    #54
        0xFE,
        (
            "I'd be happy to cooperate\x01",
            "with the Bracer Guild in\x01",
            "the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "If anything else comes up, I\x01",
            "hope you'll be willing to help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C7")

    Jump("loc_1B7C")

    label("loc_19CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AEA")
    OP_A2(0x0)

    ChrTalk(    #56
        0xFE,
        (
            "*sigh*... That was quite the\x01",
            "experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Royalty showing up at MY\x01",
            "checkpoint...and he was a\x01",
            "complete ass, on top of it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "He caused so much trouble for\x01",
            "all of the other travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "He's the sort who could give\x01",
            "the entire Liberl royal family\x01",
            "a bad name.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7C")

    label("loc_1AEA")


    ChrTalk(    #60
        0xFE,
        (
            "And all because he happens\x01",
            "to be a close relation of\x01",
            "the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "He's the sort who could give\x01",
            "the entire Liberl royal family\x01",
            "a bad name.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B7C")

    Jump("loc_20F5")

    label("loc_1B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_1F2B")
    OP_A2(0x58F)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CED")
    OP_A2(0x0)

    ChrTalk(    #62
        0xFE,
        "Ah, hello again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I'm still in your debt for your\x01",
            "actions when His Grace arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Thanks to you, he's not\x01",
            "causing any more trouble\x01",
            "for the other customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Though I still have doubts,\x01",
            "I'd be happy to cooperate with\x01",
            "the Bracer Guild in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "If anything else comes up, I\x01",
            "hope you'll be willing to help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D73")

    label("loc_1CED")


    ChrTalk(    #67
        0xFE,
        (
            "I'd be happy to cooperate\x01",
            "with the Bracer Guild in\x01",
            "the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "If anything else comes up, I\x01",
            "hope you'll be willing to help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D73")

    Jump("loc_1F28")

    label("loc_1D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E96")
    OP_A2(0x0)

    ChrTalk(    #69
        0xFE,
        (
            "*sigh*... That was quite the\x01",
            "experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "Royalty showing up at MY\x01",
            "checkpoint...and he was a\x01",
            "complete ass, on top of it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "He caused so much trouble for\x01",
            "all of the other travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "He's the sort who could give\x01",
            "the entire Liberl royal family\x01",
            "a bad name.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F28")

    label("loc_1E96")


    ChrTalk(    #73
        0xFE,
        (
            "And all because he happens\x01",
            "to be a close relation of\x01",
            "the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "He's the sort who could give\x01",
            "the entire Liberl royal family\x01",
            "a bad name.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F28")

    Jump("loc_20F5")

    label("loc_1F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1FD1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F9E")

    ChrTalk(    #75
        0xFE,
        "You've all done very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Well, well... It certainly has\x01",
            "turned into quite the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FCE")

    label("loc_1F9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1FCE")

    ChrTalk(    #77
        0xFE,
        "Everyone, please settle down!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FCE")

    label("loc_1FCE")

    Jump("loc_20F5")

    label("loc_1FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_20F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20DA")
    OP_A2(0x0)
    OP_A2(0x2)
    OP_4A(0xA, 255)

    ChrTalk(    #78
        0xFE,
        (
            "I'd heard that you were going\x01",
            "to Ruan, but nothing of you\x01",
            "coming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        (
            "Yes, it seems that our plans\x01",
            "suddenly changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "Hmm...\x01",
            "Well, what can you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Let's begin preparation for\x01",
            "the inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        "Yes, sir!\x02",
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_20F5")

    label("loc_20DA")


    ChrTalk(    #83
        0xFE,
        "*sigh* What a pain...\x02",
    )

    CloseMessageWindow()

    label("loc_20F5")

    TalkEnd(0x8)
    Return()

    # Function_6_FA9 end

    def Function_7_20F9(): pass

    label("Function_7_20F9")

    TalkBegin(0xE)

    ChrTalk(    #84
        0xE,
        (
            "#010FI'll handle the crowd here.\x02\x03",

            "You check the dining hall.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_7_20F9 end

    def Function_8_2142(): pass

    label("Function_8_2142")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_21EB")

    ChrTalk(    #85
        0xFE,
        (
            "Damn... Of all the times for\x01",
            "new orders to come down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Why couldn't we have been told\x01",
            "about the inspections being\x01",
            "called off from the beginning?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3028")

    label("loc_21EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_23F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230E")
    OP_A2(0x1)

    ChrTalk(    #87
        0xFE,
        (
            "Despite how it looks, the chief\x01",
            "doesn't tolerate any goldbricking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "It sure doesn't look like\x01",
            "he's real happy about these\x01",
            "new orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Oh, well. Even if we don't\x01",
            "like them, we'll still carry\x01",
            "them out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Oh, son of a BITCH! I am too\x01",
            "pissed off for words.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23F6")

    label("loc_230E")


    ChrTalk(    #91
        0xFE,
        (
            "As if the duke wasn't enough!\x01",
            "Now we have these stupid\x01",
            "orders!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Since when did the higher-ups\x01",
            "in this country go all funny\x01",
            "in the head?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "I probably shouldn't speak so\x01",
            "freely... I'm sure it'll get me\x01",
            "in trouble one day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F6")

    Jump("loc_3028")

    label("loc_23F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2490")

    ChrTalk(    #94
        0xFE,
        (
            "Sorry. We're currently on\x01",
            "high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Gotta watch what we say and\x01",
            "who we say it to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Plus, there are the privates\x01",
            "to consider.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3028")

    label("loc_2490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_259E")

    ChrTalk(    #97
        0xFE,
        (
            "I heard about Zeiss. Sounds like\x01",
            "things are pretty FUBAR there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "It's a technologically advanced\x01",
            "town, by Liberlian standards,\x01",
            "so this is pretty unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "If orbments completely stopped\x01",
            "working, then everyone would\x01",
            "be at a standstill, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3028")

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2A06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 0)), scpexpr(EXPR_END)), "loc_2670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2631")
    OP_A2(0x1)

    ChrTalk(    #100
        0xFE,
        (
            "Oops... Sorry, don't mean to\x01",
            "put any ideas into your head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "The chief should be coming around\x01",
            "on patrol soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_266D")

    label("loc_2631")


    ChrTalk(    #102
        0xFE,
        (
            "Oh, well. It's a tough job,\x01",
            "but someone's gotta do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_266D")

    Jump("loc_2A03")

    label("loc_2670")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2815")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277F")
    OP_A2(0x1)

    ChrTalk(    #103
        0xFE,
        "Oh, hi, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Gotta say, you really did\x01",
            "us a solid by dealing with\x01",
            "the duke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Bracers and the Royal Army\x01",
            "have never really gotten along\x01",
            "so well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "But I think we'll be a little\x01",
            "more willing to help each other\x01",
            "out in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2812")

    label("loc_277F")


    ChrTalk(    #107
        0xFE,
        (
            "You scratch our backs, we'll scratch\x01",
            "yours. Everybody's specialty is\x01",
            "different, y' know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "The point is, everything\x01",
            "worked out in the end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2812")

    Jump("loc_2A03")

    label("loc_2815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2937")
    OP_A2(0x1)

    ChrTalk(    #109
        0xFE,
        (
            "Some royal Duke Whatsit-or-\x01",
            "other came by to have a look\x01",
            "at the checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Whatever else he may be, he\x01",
            "sure was a selfish ass while\x01",
            "he was here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "And to think, people like him\x01",
            "are the reason I've got a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "At least soldiers are good\x01",
            "for something, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A03")

    label("loc_2937")


    ChrTalk(    #113
        0xFE,
        (
            "Hard to believe the duke\x01",
            "is really even part of\x01",
            "the royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "I really think he has no idea\x01",
            "what soldiers are for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Oh, well. I can think whatever\x01",
            "I want, but I just can't say\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A03")

    Jump("loc_3028")

    label("loc_2A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_2DC1")
    OP_A2(0x590)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B20")
    OP_A2(0x1)

    ChrTalk(    #116
        0xFE,
        "Oh...hi, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Gotta say, you really did\x01",
            "us a solid by dealing with\x01",
            "the duke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Bracers and the Royal Army\x01",
            "have never really gotten along\x01",
            "so well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "But I think we'll be a little\x01",
            "more willing to help each other\x01",
            "out in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB3")

    label("loc_2B20")


    ChrTalk(    #120
        0xFE,
        (
            "You scratch our backs, we'll scratch\x01",
            "yours. Everybody's specialty is\x01",
            "different, y' know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "The point is, everything\x01",
            "worked out in the end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BB3")

    Jump("loc_2DBE")

    label("loc_2BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD8")
    OP_A2(0x1)

    ChrTalk(    #122
        0xFE,
        (
            "Some royal Duke Whatsit-or-\x01",
            "other came by to have a look\x01",
            "at the checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Whatever else he may be, he\x01",
            "sure was a selfish ass while\x01",
            "he was here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "And to think, people like him\x01",
            "are the reason I've got a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "At least soldiers are good\x01",
            "for something, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBE")

    label("loc_2CD8")


    ChrTalk(    #126
        0xFE,
        (
            "Hard to believe the duke\x01",
            "is really even part of\x01",
            "the royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "I really think he has no idea\x01",
            "what soldiers are for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Oh, well. I can think whatever I want,\x01",
            "but I just can't say anything. Not too\x01",
            "loudly, anyway...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DBE")

    Jump("loc_3028")

    label("loc_2DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2F90")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2F80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EEC")
    OP_A2(0x1)

    ChrTalk(    #129
        0xFE,
        (
            "Ha ha ha! Missy, that was abso-\x01",
            "frickin'-lutely awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "I didn't know the bracers had\x01",
            "comedians in their ranks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "Still, why does a jerk like\x01",
            "that get the good luck to be\x01",
            "born into the royal family?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Couldn't the next king find a\x01",
            "better hairdresser?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F7D")

    label("loc_2EEC")


    ChrTalk(    #133
        0xFE,
        (
            "Still, why does a jerk like\x01",
            "that get the good luck to be\x01",
            "born into the royal family?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Couldn't the next king find a\x01",
            "better hairdresser?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F7D")

    Jump("loc_2F8D")

    label("loc_2F80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2F8D")
    Jump("loc_2F8D")

    label("loc_2F8D")

    Jump("loc_3028")

    label("loc_2F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3028")

    ChrTalk(    #135
        0xFE,
        (
            "Cromwell's talking to Sarge\x01",
            "about something or other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I've got a bad feeling\x01",
            "about this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "He never brings anything but\x01",
            "bad news.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3028")

    TalkEnd(0x9)
    Return()

    # Function_8_2142 end

    def Function_9_302C(): pass

    label("Function_9_302C")

    Call(0, 10)
    Return()

    # Function_9_302C end

    def Function_10_3031(): pass

    label("Function_10_3031")

    TalkBegin(0x12)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3091")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x34)
    OP_56(0x0)
    TalkEnd(0x12)
    Return()

    label("loc_3091")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30AB")
    FadeToBright(300, 0)
    TalkEnd(0x12)
    Return()

    label("loc_30AB")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_31A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3166")
    OP_A2(0x3)

    ChrTalk(    #138
        0x12,
        "Come on in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x12,
        (
            "Look at this mess. No\x01",
            "customers anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x12,
        (
            "The birthday celebration's going on...\x01",
            "which means everyone's probably\x01",
            "drinking. *sigh*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A2")

    label("loc_3166")


    ChrTalk(    #141
        0x12,
        (
            "But, you're here, so I'll do\x01",
            "my best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x12,
        "Order away!\x02",
    )

    CloseMessageWindow()

    label("loc_31A2")

    Jump("loc_3849")

    label("loc_31A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_32CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3246")
    OP_A2(0x3)

    ChrTalk(    #143
        0x12,
        "Come on in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x12,
        (
            "As you can see, the inspections\x01",
            "are complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x12,
        (
            "I do have to wonder if \x01",
            "it's really wise, stopping\x01",
            "them so soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C9")

    label("loc_3246")


    ChrTalk(    #146
        0x12,
        (
            "I mean, they haven't caught\x01",
            "the guy yet, have they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x12,
        (
            "The Royal Army'll really owe\x01",
            "the bracers a big one, after\x01",
            "this mess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C9")

    Jump("loc_3849")

    label("loc_32CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3360")
    OP_A2(0x3)

    ChrTalk(    #148
        0x12,
        (
            "*sigh* I sure hope we don't\x01",
            "get any more bad news...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x12,
        (
            "I'm afraid to talk to anybody\x01",
            "for fear of more depressing news.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_338F")

    label("loc_3360")


    ChrTalk(    #150
        0x12,
        (
            "And the bad news just\x01",
            "keeps on piling up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_338F")

    Jump("loc_3849")

    label("loc_3392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_343D")

    ChrTalk(    #151
        0x12,
        (
            "Have you heard about the\x01",
            "situation in Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x12,
        (
            "Apparently, all of their\x01",
            "orbments have just stopped\x01",
            "working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x12,
        (
            "That's pretty major stuff,\x01",
            "right there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3849")

    label("loc_343D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_34BF")

    ChrTalk(    #154
        0x12,
        "Hey, welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x12,
        (
            "I know there's nothing here to\x01",
            "do except look at the scenery,\x01",
            "but try to enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3849")

    label("loc_34BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_3602")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3566")

    ChrTalk(    #156
        0x12,
        "Hey, you're back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x12,
        (
            "Thanks for what you did\x01",
            "before. What brings you\x01",
            "here today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x12,
        (
            "Feel free to stop in whenever\x01",
            "you have time to spare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35FF")

    label("loc_3566")


    ChrTalk(    #159
        0x12,
        "Come on in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x12,
        (
            "What would you say to a great\x01",
            "meal after checking out the\x01",
            "view of the waterfall?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x12,
        (
            "Take it easy and have a nice,\x01",
            "relaxing rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35FF")

    Jump("loc_3849")

    label("loc_3602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_369E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_368E")

    ChrTalk(    #162
        0x12,
        "That old man was a huge pain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x12,
        (
            "This is a public place. What's\x01",
            "wrong with him that he\x01",
            "couldn't understand that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_369B")

    label("loc_368E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_369B")
    Jump("loc_369B")

    label("loc_369B")

    Jump("loc_3849")

    label("loc_369E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_3849")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B5")
    OP_A2(0x3)

    ChrTalk(    #164
        0x12,
        "Come on in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x12,
        (
            "I don't have much of anything\x01",
            "special, but I'd be grateful\x01",
            "for the conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x12,
        (
            "The little kettle-roasted fish\x01",
            "here are especially good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x12,
        (
            "I highly recommend them, even\x01",
            "though you may feel compelled\x01",
            "to eat them up in one bite.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3849")

    label("loc_37B5")


    ChrTalk(    #168
        0x12,
        (
            "I don't have much of anything\x01",
            "special, but I'd be grateful\x01",
            "for the conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x12,
        (
            "The little kettle-roasted fish\x01",
            "here are especially good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3849")

    TalkEnd(0x12)
    Return()

    # Function_10_3031 end

    def Function_11_384D(): pass

    label("Function_11_384D")

    Call(0, 12)
    Return()

    # Function_11_384D end

    def Function_12_3852(): pass

    label("Function_12_3852")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_39E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_392F")
    OP_A2(0x2)

    ChrTalk(    #170
        0xA,
        (
            "HQ has evidently sent over\x01",
            "new orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "It's probably a directive to\x01",
            "start obtaining clearance from\x01",
            "people who pass through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xA,
        (
            "Hmm... I get the feeling it\x01",
            "won't exactly be appreciated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39E5")

    label("loc_392F")


    ChrTalk(    #173
        0xA,
        (
            "It looks like we've got\x01",
            "new orders again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xA,
        (
            "Hmm... I wonder if the top\x01",
            "brass are really willing to do\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        (
            "It doesn't feel like they\x01",
            "really have a grip on things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39E5")

    Jump("loc_4760")

    label("loc_39E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3B8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC2")
    OP_A2(0x2)

    ChrTalk(    #176
        0xA,
        (
            "Looks like the order's come down \x01",
            "to call off the inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xA,
        (
            "I heard that the suspects\x01",
            "haven't been captured yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "If we just let people pass\x01",
            "like normal, what good will\x01",
            "that do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B89")

    label("loc_3AC2")


    ChrTalk(    #179
        0xA,
        (
            "Orders or not, I can't\x01",
            "make sense of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xA,
        (
            "I can't believe we're halting\x01",
            "inspections when the suspects\x01",
            "are still at large.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        (
            "I wonder if the other\x01",
            "checkpoints have gotten\x01",
            "the same orders.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B89")

    Jump("loc_4760")

    label("loc_3B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5F")
    OP_A2(0x2)

    ChrTalk(    #182
        0xA,
        (
            "I'm sorry, but no one is currently\x01",
            "allowed through, except in the\x01",
            "case of emergencies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xA,
        (
            "This will remain in effect until\x01",
            "those responsible for the attacks\x01",
            "in Zeiss are apprehended.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE6")

    label("loc_3C5F")


    ChrTalk(    #184
        0xA,
        (
            "No one is currently allowed\x01",
            "through, except in the case\x01",
            "of emergencies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xA,
        (
            "It would be nice if the\x01",
            "suspects were caught soon...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE6")

    Jump("loc_4760")

    label("loc_3CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3E1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9E")
    OP_A2(0x2)

    ChrTalk(    #186
        0xA,
        (
            "Apparently, something strange\x01",
            "happened in Zeiss last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xA,
        (
            "All of their orbments just\x01",
            "stopped working...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xA,
        (
            "Hmm... I wonder if that's\x01",
            "really true.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E1B")

    label("loc_3D9E")


    ChrTalk(    #189
        0xA,
        (
            "All the orbments in Zeiss\x01",
            "supposedly shut down last\x01",
            "night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xA,
        (
            "Personally, I find the idea\x01",
            "a little hard to swallow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E1B")

    Jump("loc_4760")

    label("loc_3E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_4483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_437E")
    EventBegin(0x0)
    Fade(1000)
    OP_8C(0xA, 90, 0)
    SetChrPos(0x101, -2800, 0, 6800, 270)
    SetChrPos(0x102, -2800, 0, 8000, 270)
    SetChrPos(0x105, -1800, 0, 7200, 270)
    OP_6D(-3900, 0, 7800, 1000)

    ChrTalk(    #191
        0xA,
        (
            "Good afternoon. How may I be\x01",
            "of assistance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x102,
        (
            "#010FWe were wondering what had to\x01",
            "be done to obtain permission\x01",
            "to enter Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xA,
        (
            "Ah, okay, then. Step right up!\x01",
            "I'll take care of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xA,
        (
            "Be aware, though, that once these\x01",
            "procedures have begun, you will not\x01",
            "be allowed to leave the checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xA,
        "Are you okay with that?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Yes, we are.]\x01",              # 0
            "[On second thought...]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4043"),
        (1, "loc_433B"),
        (SWITCH_DEFAULT, "loc_4379"),
    )


    label("loc_4043")

    OP_A2(0x502)

    ChrTalk(    #196
        0x101,
        "#006FYeah. Go ahead, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xA,
        (
            "Then please start by signing\x01",
            "these documents.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #198
        "\x07\x05Estelle and Joshua signed their names to the documents.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #199
        0xA,
        (
            "All right, everything\x01",
            "looks to be in order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xA,
        (
            "Is the young lady there not\x01",
            "joining you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x105,
        "#040FOh, I only came to see them off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xA,
        "Ahh, very well, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xA,
        (
            "You'll be able to accompany\x01",
            "them as far as the mouth\x01",
            "of the Kaldia Tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x105,
        "#041FThank you very much.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #205
        0x101,
        "#501FWhat's the Kaldia Tunnel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xA,
        (
            "It is the main road that joins\x01",
            "this checkpoint to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xA,
        (
            "The path is a long tunnel\x01",
            "that passes directly through\x01",
            "Kaldia Hill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        "#004FWow...an underground road...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        (
            "#010FThat'll definitely be a first\x01",
            "for me, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4379")

    label("loc_433B")


    ChrTalk(    #210
        0xA,
        (
            "Well, just let me know when\x01",
            "you've changed your mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4379")

    label("loc_4379")

    EventEnd(0x0)
    Jump("loc_4480")

    label("loc_437E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_END)), "loc_43FF")

    ChrTalk(    #211
        0xA,
        "Hmm? Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xA,
        (
            "Once the formal procedures for\x01",
            "passage have begun, you cannot\x01",
            "leave the checkpoint.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4480")

    label("loc_43FF")


    ChrTalk(    #213
        0xA,
        (
            "Your friend may accompany you\x01",
            "as far as the entrance to the\x01",
            "Kaldia Tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xA,
        (
            "Please take care after you\x01",
            "pass this point.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4480")

    Jump("loc_4760")

    label("loc_4483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4632")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4601")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_456B")
    OP_A2(0x2)

    ChrTalk(    #215
        0xA,
        (
            "So that man was actually Queen\x01",
            "Alicia's nephew?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xA,
        (
            "My messenger certainly caused\x01",
            "quite the stir this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xA,
        (
            "Ha ha... I'm sure the deputy\x01",
            "director will pick on me\x01",
            "about it, come dinnertime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45FE")

    label("loc_456B")


    ChrTalk(    #218
        0xA,
        (
            "My messenger certainly caused\x01",
            "quite the stir this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xA,
        (
            "Ha ha... I'm sure the deputy\x01",
            "director will pick on me\x01",
            "about it, come dinnertime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45FE")

    Jump("loc_462F")

    label("loc_4601")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_460E")
    Jump("loc_462F")

    label("loc_460E")


    ChrTalk(    #220
        0xA,
        "I do hope he's all right...\x02",
    )

    CloseMessageWindow()

    label("loc_462F")

    Jump("loc_4760")

    label("loc_4632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_4760")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_473B")
    OP_4A(0x8, 255)
    OP_A2(0x0)
    OP_A2(0x2)

    ChrTalk(    #221
        0x8,
        (
            "I'd heard that you were going\x01",
            "to Ruan, but nothing of you\x01",
            "coming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xA,
        (
            "Yes, it seems that our plans\x01",
            "suddenly changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x8,
        (
            "Hmm...\x01",
            "Well, what can you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x8,
        (
            "Let's begin preparation for the\x01",
            "inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xA,
        "Yes, sir!\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_4760")

    label("loc_473B")


    ChrTalk(    #226
        0xA,
        "Someone important has shown up.\x02",
    )

    CloseMessageWindow()

    label("loc_4760")

    TalkEnd(0xA)
    Return()

    # Function_12_3852 end

    def Function_13_4764(): pass

    label("Function_13_4764")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4771")
    Jump("loc_49A8")

    label("loc_4771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_477B")
    Jump("loc_49A8")

    label("loc_477B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4785")
    Jump("loc_49A8")

    label("loc_4785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_478F")
    Jump("loc_49A8")

    label("loc_478F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_47A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_47A0")
    Jump("loc_47A0")

    label("loc_47A0")

    Jump("loc_49A8")

    label("loc_47A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_47AD")
    Jump("loc_49A8")

    label("loc_47AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4916")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4837")

    ChrTalk(    #227
        0xFE,
        (
            "I can't believe he's actually\x01",
            "of royal blood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "I certainly wouldn't want\x01",
            "any foreign dignitaries\x01",
            "seeing him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4913")

    label("loc_4837")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_48D7")

    ChrTalk(    #229
        0xFE,
        (
            "*sigh* It's no real surprise they'd\x01",
            "attack the soldiers over this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "Not that I blame them, but I really\x01",
            "don't think that's going to help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4913")

    label("loc_48D7")


    ChrTalk(    #231
        0xFE,
        (
            "Indeed, there are selfish\x01",
            "people in all walks of life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4913")

    Jump("loc_49A8")

    label("loc_4916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_49A8")

    ChrTalk(    #232
        0xFE,
        (
            "*sigh*... It's a lovely place,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "Since the cost of a room is so\x01",
            "reasonable, I think I might\x01",
            "stay a few more days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A8")

    TalkEnd(0x13)
    Return()

    # Function_13_4764 end

    def Function_14_49AC(): pass

    label("Function_14_49AC")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_49B9")
    Jump("loc_4AFF")

    label("loc_49B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_49C3")
    Jump("loc_4AFF")

    label("loc_49C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_49CD")
    Jump("loc_4AFF")

    label("loc_49CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_49D7")
    Jump("loc_4AFF")

    label("loc_49D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_49EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_49E8")
    Jump("loc_49E8")

    label("loc_49E8")

    Jump("loc_4AFF")

    label("loc_49EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_49F5")
    Jump("loc_4AFF")

    label("loc_49F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_4AB6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4A70")

    ChrTalk(    #234
        0xFE,
        "You took care of the situation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "I suppose the bracers really do\x01",
            "live up to their reputation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB3")

    label("loc_4A70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_4A98")

    ChrTalk(    #236
        0xFE,
        "What an annoying guy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AB3")

    label("loc_4A98")


    ChrTalk(    #237
        0xFE,
        "What an annoying guy.\x02",
    )

    CloseMessageWindow()

    label("loc_4AB3")

    Jump("loc_4AFF")

    label("loc_4AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_4AFF")

    ChrTalk(    #238
        0xFE,
        (
            "Something about the roar\x01",
            "of the waterfall really\x01",
            "relaxes me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AFF")

    TalkEnd(0x14)
    Return()

    # Function_14_49AC end

    def Function_15_4B03(): pass

    label("Function_15_4B03")

    Call(0, 16)
    Return()

    # Function_15_4B03 end

    def Function_16_4B08(): pass

    label("Function_16_4B08")

    TalkBegin(0x15)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B68")
    OP_0D()
    OP_A9(0x35)
    OP_56(0x0)
    TalkEnd(0x15)
    Return()

    label("loc_4B68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B79")
    TalkEnd(0x15)
    Return()

    label("loc_4B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4D9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D23")
    OP_A2(0x4)

    ChrTalk(    #239
        0x15,
        (
            "The guests leave a lot of\x01",
            "really nice things behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x15,
        (
            "We keep them for a while,\x01",
            "but hardly anyone ever\x01",
            "comes to claim them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x15,
        (
            "I was just about to toss\x01",
            "this book in the trash.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x15,
        "Oh, you want it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x15,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x15,
        (
            "You promise not to let my C.O.\x01",
            "hear about it? I'd be in some\x01",
            "serious trouble if he found out.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5D1)
    OP_3E(0x219, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #245
        "\x07\x00Received \x07\x02Carnelia - Chapter 8\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_4D9A")

    label("loc_4D23")


    ChrTalk(    #246
        0x15,
        "Are you folks travelers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x15,
        (
            "That's unusual... Most people\x01",
            "are heading to Grancel for the\x01",
            "birthday celebrations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D9A")

    Jump("loc_555F")

    label("loc_4D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E8E")
    OP_A2(0x4)

    ChrTalk(    #248
        0x15,
        (
            "Warrant Officer Kientz came by a little\x01",
            "while ago, and he was in a real\x01",
            "mood. Yelling like mad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x15,
        (
            "I can only imagine how angry\x01",
            "he really is, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x15,
        (
            "I wonder what it is that\x01",
            "finally pushed him over\x01",
            "the edge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F2A")

    label("loc_4E8E")


    ChrTalk(    #251
        0x15,
        (
            "The C.O. is usually a fun guy,\x01",
            "but he's scary when he's mad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x15,
        (
            "You can ask anyone around here...\x01",
            "The stories of his temper are\x01",
            "pretty much endless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F2A")

    Jump("loc_555F")

    label("loc_4F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_5054")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD0")
    OP_A2(0x4)

    ChrTalk(    #253
        0x15,
        "S-Something's got him shouting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x15,
        (
            "It might not be obvious by the\x01",
            "looks of it, but this checkpoint's\x01",
            "got security measures in place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5051")

    label("loc_4FD0")


    ChrTalk(    #255
        0x15,
        (
            "Either way, it still gives\x01",
            "me the creeps, just thinking\x01",
            "about the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x15,
        (
            "I hope that whoever did it is\x01",
            "captured soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5051")

    Jump("loc_555F")

    label("loc_5054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_5177")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F1")
    OP_A2(0x4)

    ChrTalk(    #257
        0x15,
        "Come on in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x15,
        (
            "I guess something big is\x01",
            "going down in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x15,
        (
            "The orbments shut down...\x01",
            "I mean, what's this world\x01",
            "coming to?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5174")

    label("loc_50F1")


    ChrTalk(    #260
        0x15,
        (
            "I heard a rumor that an\x01",
            "experiment at the central\x01",
            "lab was the cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x15,
        (
            "But what kind of experiment\x01",
            "could actually do that?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5174")

    Jump("loc_555F")

    label("loc_5177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5348")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52F6")
    OP_A2(0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51BA")

    ChrTalk(    #262
        0x15,
        "Yo! Welcome to Air-Letten.\x02",
    )

    CloseMessageWindow()
    Jump("loc_52F3")

    label("loc_51BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_521D")

    ChrTalk(    #263
        0x15,
        "Whoa... Traveling sisters?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x15,
        (
            "This place has the best\x01",
            "view of the waterfall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52F3")

    label("loc_521D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5293")

    ChrTalk(    #265
        0x15,
        (
            "Hey... Brother and sister\x01",
            "traveling together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x15,
        (
            "This place has the best\x01",
            "view of the waterfall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52F3")

    label("loc_5293")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52F3")

    ChrTalk(    #267
        0x15,
        (
            "Whoa, now that's one tiny\x01",
            "little guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x15,
        "Are you traveling with the girls?\x02",
    )

    CloseMessageWindow()

    label("loc_52F3")

    Jump("loc_5345")

    label("loc_52F6")


    ChrTalk(    #269
        0x15,
        (
            "If you need me for anything,\x01",
            "just give me a shout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x15,
        "Have a nice trip.\x02",
    )

    CloseMessageWindow()

    label("loc_5345")

    Jump("loc_555F")

    label("loc_5348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_53C8")

    ChrTalk(    #271
        0x15,
        (
            "Hey, welcome. This is an inn\x01",
            "specifically for travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x15,
        (
            "If you need me for anything,\x01",
            "just give me a shout.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_555F")

    label("loc_53C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_54EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5450")

    ChrTalk(    #273
        0x15,
        (
            "It's been noisy around\x01",
            "here for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x15,
        (
            "If something happens, I wonder\x01",
            "if I should let my C.O. know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54EB")

    label("loc_5450")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_54A4")

    ChrTalk(    #275
        0x15,
        "It sure is noisy outside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x15,
        "Is someone arguing or something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_54EB")

    label("loc_54A4")


    ChrTalk(    #277
        0x15,
        "It sure is noisy outside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x15,
        "Is someone arguing or something?\x02",
    )

    CloseMessageWindow()

    label("loc_54EB")

    Jump("loc_555F")

    label("loc_54EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_555F")

    ChrTalk(    #279
        0x15,
        (
            "There's been a lot of guests\x01",
            "today, all looking for a place\x01",
            "to stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x15,
        "I should get a room ready.\x02",
    )

    CloseMessageWindow()

    label("loc_555F")

    TalkEnd(0x15)
    Return()

    # Function_16_4B08 end

    def Function_17_5563(): pass

    label("Function_17_5563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5601")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5582")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_5589")

    label("loc_5582")

    TurnDirection(0x102, 0x0, 400)

    label("loc_5589")


    ChrTalk(    #281
        0x102,
        (
            "#010FRuan is this way.\x02\x03",

            "We can't go back, remember?\x01",
            "We've already signed the\x01",
            "papers.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_568A")

    label("loc_5601")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_568A")
    EventBegin(0x1)
    OP_4A(0xE, 255)
    TurnDirection(0xE, 0x101, 0)

    ChrTalk(    #282
        0xE,
        (
            "#012FEstelle, you go on and\x01",
            "check out the dining hall.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    OP_8C(0xE, 0, 0)
    OP_4B(0xE, 255)
    Sleep(50)
    EventEnd(0x4)

    label("loc_568A")

    Return()

    # Function_17_5563 end

    def Function_18_568B(): pass

    label("Function_18_568B")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_18_568B end

    SaveToFile()

Try(main)
