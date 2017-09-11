from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3410   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3410.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'CWO Dale',                             # 9
        'Private Wayne',                        # 10
        'Dodge',                                # 11
        'Radmira',                              # 12
        'Charles',                              # 13
        'Private Jules',                        # 14
        'Private Hector',                       # 15
        'Private Chesley',                      # 16
        'Armand',                               # 17
        'Ellie',                                # 18
        'Warrant Officer Talbot',               # 19
        'Sanders',                              # 20
        'Tammy',                                # 21
        'Marian',                               # 22
        'Norche',                               # 23
        'Talia',                                # 24
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
        'ED6_DT07/CH01140 ._CH',             # 02
        'ED6_DT07/CH01690 ._CH',             # 03
        'ED6_DT07/CH02640 ._CH',             # 04
        'ED6_DT07/CH01300 ._CH',             # 05
        'ED6_DT07/CH01300 ._CH',             # 06
        'ED6_DT07/CH01300 ._CH',             # 07
        'ED6_DT07/CH01140 ._CH',             # 08
        'ED6_DT07/CH01150 ._CH',             # 09
        'ED6_DT07/CH01300 ._CH',             # 0A
        'ED6_DT07/CH01520 ._CH',             # 0B
        'ED6_DT07/CH01350 ._CH',             # 0C
        'ED6_DT07/CH01213 ._CH',             # 0D
        'ED6_DT07/CH01233 ._CH',             # 0E
        'ED6_DT07/CH01180 ._CH',             # 0F
        'ED6_DT07/CH00003 ._CH',             # 10
        'ED6_DT07/CH00013 ._CH',             # 11
        'ED6_DT07/CH02053 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01140P._CP',             # 02
        'ED6_DT07/CH01690P._CP',             # 03
        'ED6_DT07/CH02640P._CP',             # 04
        'ED6_DT07/CH01300P._CP',             # 05
        'ED6_DT07/CH01300P._CP',             # 06
        'ED6_DT07/CH01300P._CP',             # 07
        'ED6_DT07/CH01140P._CP',             # 08
        'ED6_DT07/CH01150P._CP',             # 09
        'ED6_DT07/CH01300P._CP',             # 0A
        'ED6_DT07/CH01520P._CP',             # 0B
        'ED6_DT07/CH01350P._CP',             # 0C
        'ED6_DT07/CH01213P._CP',             # 0D
        'ED6_DT07/CH01233P._CP',             # 0E
        'ED6_DT07/CH01180P._CP',             # 0F
        'ED6_DT07/CH00003P._CP',             # 10
        'ED6_DT07/CH00013P._CP',             # 11
        'ED6_DT07/CH02053P._CP',             # 12
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 6790,
        Z                   = 0,
        Y                   = 2810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )


    DeclActor(
        TriggerX            = 58180,
        TriggerZ            = 5000,
        TriggerY            = 51630,
        TriggerRange        = 1000,
        ActorX              = 58180,
        ActorZ              = 6500,
        ActorY              = 51630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6760,
        TriggerZ            = 0,
        TriggerY            = 900,
        TriggerRange        = 1000,
        ActorX              = 6790,
        ActorZ              = 1500,
        ActorY              = 2810,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 109850,
        TriggerZ            = 0,
        TriggerY            = 21800,
        TriggerRange        = 1000,
        ActorX              = 111940,
        ActorZ              = 1500,
        ActorY              = 22150,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 91680,
        TriggerZ            = 0,
        TriggerY            = -22240,
        TriggerRange        = 1000,
        ActorX              = 89560,
        ActorZ              = 1500,
        ActorY              = -22370,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3D2",          # 00, 0
        "Function_1_BD6",          # 01, 1
        "Function_2_C91",          # 02, 2
        "Function_3_CA7",          # 03, 3
        "Function_4_CCB",          # 04, 4
        "Function_5_CEF",          # 05, 5
        "Function_6_CF4",          # 06, 6
        "Function_7_1A1C",         # 07, 7
        "Function_8_1A1D",         # 08, 8
        "Function_9_1A1E",         # 09, 9
        "Function_10_1A1F",        # 0A, 10
        "Function_11_1C5E",        # 0B, 11
        "Function_12_1E62",        # 0C, 12
        "Function_13_2AB6",        # 0D, 13
        "Function_14_38C2",        # 0E, 14
        "Function_15_4608",        # 0F, 15
        "Function_16_4B03",        # 10, 16
        "Function_17_4EFA",        # 11, 17
        "Function_18_4EFF",        # 12, 18
        "Function_19_5A72",        # 13, 19
        "Function_20_5E07",        # 14, 20
        "Function_21_603A",        # 15, 21
        "Function_22_6170",        # 16, 22
        "Function_23_6175",        # 17, 23
        "Function_24_8FDA",        # 18, 24
        "Function_25_9124",        # 19, 25
        "Function_26_9351",        # 1A, 26
        "Function_27_9B12",        # 1B, 27
    )


    def Function_0_3D2(): pass

    label("Function_0_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3DC")
    Jump("loc_475")

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3FC")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2760, 0, 2290, 87)
    Jump("loc_475")

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_406")
    Jump("loc_475")

    label("loc_406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_410")
    Jump("loc_475")

    label("loc_410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_41A")
    Jump("loc_475")

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_424")
    Jump("loc_475")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_42E")
    Jump("loc_475")

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_438")
    Jump("loc_475")

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_442")
    Jump("loc_475")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_475")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 18880, 0, 2680, 270)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 17270, 0, 2680, 90)

    label("loc_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4FB")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_586")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 89690, 0, -24010, 0)
    OP_43(0x14, 0x0, 0x0, 0x2)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_611")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 89690, 0, -24010, 0)
    OP_43(0x14, 0x0, 0x0, 0x2)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_697")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_71D")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_71D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_7A3")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_82C")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 80890, 0, 23550, 110)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 82450, 0, 23660, 271)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_8B5")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 80890, 0, 23550, 110)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 82450, 0, 23660, 271)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_8B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_993")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 58600, 150, -27620, 90)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 60840, 150, -27720, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 17220, 0, 2570, 103)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 18530, 0, 2570, 249)
    Jump("loc_BD5")

    label("loc_993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_A71")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 58600, 150, -27620, 90)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 60840, 150, -27720, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 22840, 0, -3730, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 21050, 0, -3760, 90)
    Jump("loc_BD5")

    label("loc_A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_B26")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 89540, 0, -24220, 0)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 58600, 150, -27620, 90)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 60840, 150, -27720, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 180)
    SetChrFlags(0x17, 0x10)
    Jump("loc_BD5")

    label("loc_B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BD5")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 58600, 150, -27620, 90)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 60840, 150, -27720, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)

    label("loc_BD5")

    Return()

    # Function_0_3D2 end

    def Function_1_BD6(): pass

    label("Function_1_BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_BE5")
    OP_1B(0x0, 0x0, 0x19)
    Jump("loc_BEA")

    label("loc_BE5")

    OP_1B(0x1, 0x0, 0x18)

    label("loc_BEA")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0A")
    OP_65(0x0, 0x1)

    label("loc_C0A")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_C18")
    Jump("loc_C8B")

    label("loc_C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_C22")
    Jump("loc_C8B")

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C2C")
    Jump("loc_C8B")

    label("loc_C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_C36")
    Jump("loc_C8B")

    label("loc_C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_C40")
    Jump("loc_C8B")

    label("loc_C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_C4A")
    Jump("loc_C8B")

    label("loc_C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_C58")
    OP_64(0x2, 0x1)
    Jump("loc_C8B")

    label("loc_C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_C66")
    OP_64(0x2, 0x1)
    Jump("loc_C8B")

    label("loc_C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_C70")
    Jump("loc_C8B")

    label("loc_C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_C7A")
    Jump("loc_C8B")

    label("loc_C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_C84")
    Jump("loc_C8B")

    label("loc_C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C8B")

    label("loc_C8B")

    OP_1C(0x5, 0x0, 0x1B)
    Return()

    # Function_1_BD6 end

    def Function_2_C91(): pass

    label("Function_2_C91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CA6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_C91")

    label("loc_CA6")

    Return()

    # Function_2_C91 end

    def Function_3_CA7(): pass

    label("Function_3_CA7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CCA")
    OP_8D(0xFE, 5070, 820, 17900, -3880, 2000)
    Jump("Function_3_CA7")

    label("loc_CCA")

    Return()

    # Function_3_CA7 end

    def Function_4_CCB(): pass

    label("Function_4_CCB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CEE")
    OP_8D(0xFE, 56600, -23980, 64040, -26210, 2000)
    Jump("Function_4_CCB")

    label("loc_CEE")

    Return()

    # Function_4_CCB end

    def Function_5_CEF(): pass

    label("Function_5_CEF")

    Call(0, 6)
    Return()

    # Function_5_CEF end

    def Function_6_CF4(): pass

    label("Function_6_CF4")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_D76")

    ChrTalk(    #0
        0x8,
        (
            "I think the terrorists were planning\x01",
            "to strike during the birthday celebrations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        "We have to stay vigilant.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_E25")

    ChrTalk(    #2
        0x8,
        (
            "I hear Intelligence only accepts\x01",
            "the best for its Special Ops Unit. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "Of course, it begs the question\x01",
            "of whether so many elite troops\x01",
            "are necessary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F19")

    label("loc_E25")

    OP_A2(0xF)

    ChrTalk(    #4
        0x8,
        (
            "I hear Intelligence's Special\x01",
            "Ops Unit is looking for only \x01",
            "the best soldiers to recruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "Of course, it begs the question\x01",
            "of whether such elite troops\x01",
            "are necessary. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "It's not my place to inquire,\x01",
            "but lately I've...noticed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F19")

    Jump("loc_1A18")

    label("loc_F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_FD0")

    ChrTalk(    #7
        0x8,
        (
            "...the increasing number of\x01",
            "communiques requesting we\x01",
            "tighten our security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "I wonder if Intelligence is having\x01",
            "trouble finding where the terrorists\x01",
            "are hiding.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1077")

    ChrTalk(    #9
        0x8,
        (
            "The garrison here at Sanktheim\x01",
            "has been ordered to stay away\x01",
            "from the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "Not that we need the orders,\x01",
            "it's out of our jurisdiction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_1077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1114")

    ChrTalk(    #11
        0x8,
        (
            "I've heard Intelligence opened a\x01",
            "full-scale investigation at Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "If Colonel Richard is involved,\x01",
            "we'll definitely catch the culprits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_1114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_11BE")

    ChrTalk(    #13
        0x8,
        (
            "I'd like to apologize for the\x01",
            "misunderstanding before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "With the birthday celebrations so\x01",
            "close, we can't afford to be lax\x01",
            "with inspection procedures.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_11BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_1334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1246")

    ChrTalk(    #15
        0x8,
        (
            "We must keep any suspicious\x01",
            "elements out of the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "I appreciate your extra vigilance\x01",
            "for the duration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1331")

    label("loc_1246")

    OP_A2(0xF)
    OP_4A(0x12, 255)

    ChrTalk(    #17
        0x12,
        (
            "Sir, I've passed along\x01",
            "your orders to the troops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x12,
        (
            "They are to adhere strictly to\x01",
            "protocol and execute their \x01",
            "duty promptly and efficiently. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "I appreciate your extra diligence\x01",
            "during this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x12, 255)

    label("loc_1331")

    Jump("loc_1A18")

    label("loc_1334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_14AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_13BC")

    ChrTalk(    #21
        0x8,
        (
            "We must keep any suspicious\x01",
            "elements out of the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "I appreciate your extra diligence\x01",
            "during this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A7")

    label("loc_13BC")

    OP_A2(0xF)
    OP_4A(0x12, 255)

    ChrTalk(    #23
        0x12,
        (
            "Sir, I've passed along\x01",
            "your orders to the troops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x12,
        (
            "They are to adhere strictly to\x01",
            "protocol and execute their \x01",
            "duty promptly and efficiently. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "I appreciate your extra diligence\x01",
            "during this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x12, 255)

    label("loc_14A7")

    Jump("loc_1A18")

    label("loc_14AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_156E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1517")

    ChrTalk(    #27
        0x8,
        (
            "I don't understand why we've\x01",
            "suspended visitor inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "But orders are orders.\x02",
    )

    CloseMessageWindow()
    Jump("loc_156B")

    label("loc_1517")

    OP_A2(0xF)

    ChrTalk(    #29
        0x8,
        "What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "I'm busy right now. Take your\x01",
            "questions somewhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    label("loc_156B")

    Jump("loc_1A18")

    label("loc_156E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1625")

    ChrTalk(    #32
        0x8,
        (
            "This is big. The Royal Army\x01",
            "plans to open a full-scale\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "If that happens, the criminals\x01",
            "are like rats in a trap. All we\x01",
            "need is to be patient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1710")

    label("loc_1625")

    OP_A2(0xF)

    ChrTalk(    #34
        0x8,
        (
            "I'm afraid we have to hold all\x01",
            "travelers pending proof of\x01",
            "origin and destination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "I shouldn't have to tell you\x01",
            "why... Not after Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "The Royal Army is doing\x01",
            "everything to prevent the\x01",
            "perpetrator from leaving Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1710")

    Jump("loc_1A18")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1837")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1795")

    ChrTalk(    #37
        0x8,
        "Hmm... I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "Yes, proper channels for \x01",
            "communication with the capital\x01",
            "are important in these times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1834")

    label("loc_1795")

    OP_A2(0xF)

    ChrTalk(    #39
        0x8,
        (
            "Hmm? Yes? I'm afraid I'm busy\x01",
            "with official work right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "If you're in a hurry, I suggest\x01",
            "you take your questions to \x01",
            "someone else in the hall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1834")

    Jump("loc_1A18")

    label("loc_1837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_18F9")

    ChrTalk(    #41
        0x8,
        (
            "We're relying on the Bracer\x01",
            "Guild right now for cases\x01",
            "of monster extermination...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "But their organization has limits.\x01",
            "We shouldn't trust them with any\x01",
            "big assignments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_18F9")

    OP_A2(0xF)

    ChrTalk(    #43
        0x8,
        (
            "The Sanktheim garrison's main\x01",
            "duty is to the castle gates, \x01",
            "but we also do street patrols.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "The queen's birthday celebration\x01",
            "is coming up, and that means\x01",
            "an increase in travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "And if we had an attack by a\x01",
            "particularly fierce monster...\x01",
            "We need to plan for that now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A18")

    TalkEnd(0x8)
    Return()

    # Function_6_CF4 end

    def Function_7_1A1C(): pass

    label("Function_7_1A1C")

    Return()

    # Function_7_1A1C end

    def Function_8_1A1D(): pass

    label("Function_8_1A1D")

    Return()

    # Function_8_1A1D end

    def Function_9_1A1E(): pass

    label("Function_9_1A1E")

    Return()

    # Function_9_1A1E end

    def Function_10_1A1F(): pass

    label("Function_10_1A1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1A2C")
    Jump("loc_1C5A")

    label("loc_1A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1B33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1AB6")

    ChrTalk(    #46
        0xFE,
        (
            "Oh, thank goodness I got into\x01",
            "the capital like I planned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I've got places to go with my\x01",
            "girlfriend, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B30")

    label("loc_1AB6")

    OP_A2(0x6)

    ChrTalk(    #48
        0xFE,
        (
            "Nice that I got through gate\x01",
            "inspection so quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "It's smooth sailing now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "I'm in. Just like I planned.\x02",
    )

    CloseMessageWindow()

    label("loc_1B30")

    Jump("loc_1C5A")

    label("loc_1B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1C49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1B76")

    ChrTalk(    #51
        0xFE,
        (
            "Whew. Okay, calm down. \x01",
            "I gotta stay casual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C46")

    label("loc_1B76")

    OP_A2(0x6)

    ChrTalk(    #52
        0xFE,
        "You heard about Zeiss, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Thanks to all the inspections,\x01",
            "I couldn't get into the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "But now... Okay, gotta stay cool.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 270, 400)
    Sleep(1000)

    ChrTalk(    #55
        0xFE,
        "I'll protect you, my love!\x02",
    )

    CloseMessageWindow()

    label("loc_1C46")

    Jump("loc_1C5A")

    label("loc_1C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1C53")
    Jump("loc_1C5A")

    label("loc_1C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C5A")

    label("loc_1C5A")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A1F end

    def Function_11_1C5E(): pass

    label("Function_11_1C5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1C6B")
    Jump("loc_1E5E")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1CCD")

    ChrTalk(    #56
        0xFE,
        (
            "Looks like we got back in time\x01",
            "for the queen's birthday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "I can't wait!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D56")

    label("loc_1CCD")

    OP_A2(0x7)

    ChrTalk(    #58
        0xFE,
        "I'm so glad I got in all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "All the soldiers in inspection\x01",
            "were a bit nerve-racking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "...but Armand was so sweet.\x02",
    )

    CloseMessageWindow()

    label("loc_1D56")

    Jump("loc_1E5E")

    label("loc_1D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1DF5")

    ChrTalk(    #61
        0xFE,
        (
            "Poor little Armand... He starts\x01",
            "talking so loud whenever he gets\x01",
            "nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "He can barely make it on his\x01",
            "own. It's so cute! *sigh*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_1DF5")

    OP_A2(0x7)

    ChrTalk(    #63
        0xFE,
        "ANOTHER incident...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Don't the people here have \x01",
            "anything better to do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4A")

    Jump("loc_1E5E")

    label("loc_1E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1E57")
    Jump("loc_1E5E")

    label("loc_1E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E5E")

    label("loc_1E5E")

    TalkEnd(0xFE)
    Return()

    # Function_11_1C5E end

    def Function_12_1E62(): pass

    label("Function_12_1E62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1F13")

    ChrTalk(    #65
        0xFE,
        (
            "We've seen a big increase in\x01",
            "orders from Intelligence come\x01",
            "through as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "It might be due to Colonel \x01",
            "Richard becoming personal\x01",
            "adviser to the duke.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB2")

    label("loc_1F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1FB6")

    ChrTalk(    #67
        0xFE,
        (
            "The lack of a statement from\x01",
            "the queen regarding her illness\x01",
            "has also been troubling.  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "What's going to happen with \x01",
            "the birthday celebration?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB2")

    label("loc_1FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_203A")

    ChrTalk(    #69
        0xFE,
        (
            "The recent Martial Arts Competition\x01",
            "went smoothly enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "It would be nice if this would\x01",
            "go as smoothly also...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB2")

    label("loc_203A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_20BA")

    ChrTalk(    #71
        0xFE,
        (
            "I think we would find these\x01",
            "terrorists faster if we worked\x01",
            "with the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "Not possible, I guess...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AB2")

    label("loc_20BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2164")

    ChrTalk(    #73
        0xFE,
        (
            "Just recently I saw a person\x01",
            "from the Republic near Grancel.\x01",
            "He was a MOUNTAIN of a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "He said he'd come to train for\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB2")

    label("loc_2164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_21CB")

    ChrTalk(    #75
        0xFE,
        "I know I was rude before...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "But I was only doing my job.\x01",
            "Please accept my apology.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB2")

    label("loc_21CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_2328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_223B")

    ChrTalk(    #77
        0xFE,
        (
            "The criminals have to be feeling\x01",
            "the pressure by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "We have to keep our eyes open.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2325")

    label("loc_223B")

    OP_A2(0xF)
    OP_4A(0x8, 255)

    ChrTalk(    #79
        0xFE,
        (
            "Sir, I've passed along\x01",
            "your orders to the troops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "They are to adhere strictly to\x01",
            "protocol and execute their\x01",
            "duty promptly and efficiently. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        "Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "I appreciate your extra diligence\x01",
            "during this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)

    label("loc_2325")

    Jump("loc_2AB2")

    label("loc_2328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2485")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2398")

    ChrTalk(    #83
        0xFE,
        (
            "The criminals have to be feeling\x01",
            "the pressure by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "We have to keep our eyes open.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2482")

    label("loc_2398")

    OP_A2(0xF)
    OP_4A(0x8, 255)

    ChrTalk(    #85
        0xFE,
        (
            "Sir, I've passed along\x01",
            "your orders to the troops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "They are to adhere strictly to\x01",
            "protocol and execute their\x01",
            "duty promptly and efficiently. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        "Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "I appreciate your extra diligence\x01",
            "during this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)

    label("loc_2482")

    Jump("loc_2AB2")

    label("loc_2485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2618")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_254C")

    ChrTalk(    #89
        0xFE,
        (
            "I'm sure High Command received\x01",
            "some information that made\x01",
            "these inspections irrelevant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "I don't expect you to accept\x01",
            "this explanation, but I do\x01",
            "expect you to listen to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2615")

    label("loc_254C")

    OP_A2(0x9)

    ChrTalk(    #91
        0xFE,
        (
            "Suspension of inspections is a\x01",
            "direct order from High Command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Our job is to follow orders,\x01",
            "not to question or judge them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "We are ordered to continue our\x01",
            "patrol activity. For safety.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2615")

    Jump("loc_2AB2")

    label("loc_2618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2773")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_26FC")

    ChrTalk(    #94
        0xFE,
        (
            "The Bracer Guild is helping,\x01",
            "but we can't seem to find any\x01",
            "traces of the criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "The perpetrators were willing\x01",
            "to attack the central factory\x01",
            "in broad daylight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "If we don't catch them soon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2770")

    label("loc_26FC")

    OP_A2(0x9)

    ChrTalk(    #97
        0xFE,
        (
            "I'm very sorry, but all visitors are\x01",
            "to be inspected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "Anti-terrorist measures.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "I apologize again.\x02",
    )

    CloseMessageWindow()

    label("loc_2770")

    Jump("loc_2AB2")

    label("loc_2773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_287F")

    ChrTalk(    #100
        0xFE,
        (
            "There are two bases along the\x01",
            "Ahnenburg Wall...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "The Sanktheim Gate here and the Gurune\x01",
            "Gate on the Rolent side are designed to be\x01",
            "the capital's ultimate lines of protection. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "We soldiers here AND there will\x01",
            "be 100% alert, at all times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2962")

    label("loc_287F")

    OP_A2(0x9)

    ChrTalk(    #103
        0xFE,
        (
            "The queen's birthday celebration\x01",
            "is coming up soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "We should have a drill to practice\x01",
            "police procedure during a busy\x01",
            "period one time. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "I need to file a report to Chief\x01",
            "Warrant Officer Dale for that drill. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_2962")

    Jump("loc_2AB2")

    label("loc_2965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2A33")

    ChrTalk(    #106
        0xFE,
        (
            "If you take the inner stairs all\x01",
            "the way up you'll get to the\x01",
            "top of the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "The buildings are laid out strangely,\x01",
            "but that's because we preserved\x01",
            "the original ruins.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB2")

    label("loc_2A33")

    OP_A2(0x9)

    ChrTalk(    #108
        0xFE,
        (
            "Oh, are you here to study? \x01",
            "Please, ask me anything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "I can tell you anything!\x01",
            "...Well, anything I know\x01",
            "at least. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB2")

    TalkEnd(0xFE)
    Return()

    # Function_12_1E62 end

    def Function_13_2AB6(): pass

    label("Function_13_2AB6")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                          # 0
            "Shop\x01",                          # 1
            "[Pot O' Meat] - 700 mira\x01",      # 2
            "Leave\x01",                         # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2F")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x4A)
    OP_56(0x0)
    TalkEnd(0x13)
    Return()

    label("loc_2B2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C35")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2BFB")
    SubMira(700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #110
        "\x06\x07\x00Ate \x07\x02Pot O' Meat\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2BC)
    OP_31(0x1, 0xFD, 0x2BC)
    OP_31(0x2, 0xFD, 0x2BC)
    OP_31(0x3, 0xFD, 0x2BC)
    OP_31(0x4, 0xFD, 0x2BC)
    OP_31(0x5, 0xFD, 0x2BC)
    OP_31(0x6, 0xFD, 0x2BC)
    OP_31(0x7, 0xFD, 0x2BC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x7)"), scpexpr(EXPR_END)), "loc_2BC0")
    Jump("loc_2BED")

    label("loc_2BC0")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #111
        "\x06\x07\x00Learned '\x07\x02Pot O' Meat\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_2BED")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_2C23")

    label("loc_2BFB")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #112
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_2C23")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x13)
    Return()

    label("loc_2C35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C4F")
    FadeToBright(300, 0)
    TalkEnd(0x13)
    Return()

    label("loc_2C4F")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2CE0")

    ChrTalk(    #113
        0xFE,
        (
            "It don't matter how busy you\x01",
            "are, everybody's gotta eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Time to plan the ultimate meal\x01",
            "for all my hungry soldiers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BE")

    label("loc_2CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2D65")

    ChrTalk(    #115
        0xFE,
        (
            "I just bet that Tammy's goofin' off\x01",
            "somewhere again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Oh well. It don't matter. There\x01",
            "ain't nobody around anyhow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BE")

    label("loc_2D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2E02")

    ChrTalk(    #117
        0xFE,
        (
            "Good to take a little break\x01",
            "during the down time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Plan the next meal while doing\x01",
            "the inventory, stuff like that.\x01",
            "Shave a cat, maybe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BE")

    label("loc_2E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2EB4")

    ChrTalk(    #119
        0xFE,
        (
            "After the Martial Arts Competition\x01",
            "started all of my customers just\x01",
            "vanished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "I mean, the soldiers come in of\x01",
            "course, but still, the place is a\x01",
            "little quiet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BE")

    label("loc_2EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_308E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2F72")

    ChrTalk(    #121
        0xFE,
        (
            "Listen to this! The other day\x01",
            "this guy comes in and just\x01",
            "starts putting it away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "I was so impressed with how \x01",
            "much he could eat, I ended\x01",
            "up giving him a discount.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308B")

    label("loc_2F72")

    OP_A2(0xA)

    ChrTalk(    #123
        0xFE,
        (
            "I love to watch customers who\x01",
            "enjoy my cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "I pride myself on my menu.\x01",
            "It's about the only thing I've\x01",
            "got. Ha ha ha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "The other day this guy comes\x01",
            "in and just puts it away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "I was so impressed with how \x01",
            "much he could eat, I ended\x01",
            "up giving him a discount.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308B")

    Jump("loc_38BE")

    label("loc_308E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_31B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_30C9")
    TurnDirection(0x13, 0x10E, 400)

    ChrTalk(    #127
        0xFE,
        "Good luck with your research!\x02",
    )

    CloseMessageWindow()
    Jump("loc_31AD")

    label("loc_30C9")

    OP_A2(0xA)
    TurnDirection(0x13, 0x10E, 400)

    ChrTalk(    #128
        0xFE,
        "Hey, you're that guy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x10E,
        (
            "#130FThank you for your generous\x01",
            "meal and discount, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "No worries.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "It's nice seeing a customer\x01",
            "enjoy my cooking so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Thanks again, and good luck\x01",
            "with your research!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AD")

    Jump("loc_38BE")

    label("loc_31B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_3279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3223")

    ChrTalk(    #133
        0xFE,
        "You all off to Grancel, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Nice. I'd love to go see the\x01",
            "birthday celebration myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3276")

    label("loc_3223")

    OP_A2(0xA)

    ChrTalk(    #135
        0xFE,
        "Come on in! Have a seat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "Just sit back and make\x01",
            "yourself comfortable!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3276")

    Jump("loc_38BE")

    label("loc_3279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_32D3")

    ChrTalk(    #137
        0xFE,
        "Come on in! Have a seat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Just sit back and make\x01",
            "yourself comfortable!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BE")

    label("loc_32D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_340E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3362")

    ChrTalk(    #139
        0xFE,
        (
            "I still ain't heard that they\x01",
            "caught them terrorists yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "I wonder if they're right to\x01",
            "be stoppin' the inspections.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_340B")

    label("loc_3362")

    OP_A2(0xA)

    ChrTalk(    #141
        0xFE,
        "Welcome! Have a seat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "They sure stopped those\x01",
            "inspections quick enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "It don't bother me either way,\x01",
            "but I hope it don't hurt the\x01",
            "investigation any.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_340B")

    Jump("loc_38BE")

    label("loc_340E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_358A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3479")

    ChrTalk(    #144
        0xFE,
        "Attacking the central factory...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "I tell you, those guys must be\x01",
            "something else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3587")

    label("loc_3479")

    OP_A2(0xA)

    ChrTalk(    #146
        0xFE,
        (
            "This is turning into a grand old\x01",
            "cluster, innit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "About all I can do to help is\x01",
            "feed the ones doin' all the\x01",
            "hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "They won't get anything\x01",
            "accomplished on an empty\x01",
            "stomach, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "A full stomach keeps the mind\x01",
            "on task, I like to say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3587")

    Jump("loc_38BE")

    label("loc_358A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_37B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3665")

    ChrTalk(    #150
        0xFE,
        (
            "I got to keep on my toes here.\x01",
            "Always got new customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "Now where did that Tammy\x01",
            "get herself off to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "I don't mind taking things easy,\x01",
            "but that girl needs to pick her\x01",
            "break times better!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B1")

    label("loc_3665")

    OP_A2(0xA)

    ChrTalk(    #153
        0xFE,
        (
            "When I was younger, I wanted\x01",
            "to work in a big restaurant.\x01",
            "But then I got to thinking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I decided that I was doing\x01",
            "just fine right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "I mean, I'm right here in front\x01",
            "of my customers, right? I have\x01",
            "instant feedback!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "So I have to keep up my game.\x01",
            "The best restaurant to work in\x01",
            "is one where you're learning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B1")

    Jump("loc_38BE")

    label("loc_37B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_38BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_387B")

    ChrTalk(    #157
        0xFE,
        (
            "I can only cook with the\x01",
            "ingredients I have on hand...\x01",
            "but that's the trick, innit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "Go ahead, have some. You seem\x01",
            "like the type who gets that good\x01",
            "food can come cheap too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BE")

    label("loc_387B")

    OP_A2(0xA)

    ChrTalk(    #159
        0xFE,
        "Welcome! Come right in!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "Please, have a seat anywhere.\x02",
    )

    CloseMessageWindow()

    label("loc_38BE")

    TalkEnd(0xFE)
    Return()

    # Function_13_2AB6 end

    def Function_14_38C2(): pass

    label("Function_14_38C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_392F")

    ChrTalk(    #161
        0xFE,
        (
            "The soldiers sure have been\x01",
            "busy lately, haven't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "It's so boring here by myself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4604")

    label("loc_392F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_39D7")

    ChrTalk(    #163
        0xFE,
        (
            "I kind of wish sometimes there\x01",
            "was a man here who'd, y'know,\x01",
            "push me around a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "I'd know that at least HE'D \x01",
            "care about what I was doing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA9")

    label("loc_39D7")

    OP_A2(0xB)

    ChrTalk(    #165
        0xFE,
        "I was thinking...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "You can't live life by being all\x01",
            "smiley and friendly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "I think I need a man who's\x01",
            "willing to take CHARGE of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "I'd know that at least HE'D \x01",
            "care about what I was doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA9")

    Jump("loc_4604")

    label("loc_3AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3B66")

    ChrTalk(    #169
        0xFE,
        "And do you know what else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "Sanders has been giving out\x01",
            "meal discounts again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "He's definitely a good person,\x01",
            "but he won't ever get rich\x01",
            "doing that kind of stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4604")

    label("loc_3B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3BF1")

    ChrTalk(    #172
        0xFE,
        (
            "Nothing to do here. Maybe I\x01",
            "should go visit my mother...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "But helping her out at the inn\x01",
            "is just as boring, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C86")

    label("loc_3BF1")

    OP_A2(0xB)

    ChrTalk(    #174
        0xFE,
        (
            "And all the soldiers are busy.\x01",
            "Goddess, I'm bored...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "I should go visit my mother...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "But helping her out at the inn\x01",
            "is boring, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C86")

    Jump("loc_4604")

    label("loc_3C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3D41")

    ChrTalk(    #177
        0xFE,
        (
            "The other day this guy came \x01",
            "in. He was a big as a bear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "I couldn't BELIEVE how much\x01",
            "food he ate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "Giving discounts to guys like\x01",
            "that I have no problems with. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4604")

    label("loc_3D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_3DC9")

    ChrTalk(    #180
        0xFE,
        (
            "That Sanders cuts the tab of\x01",
            "anybody who enjoys their meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "I'm worried if this store is making\x01",
            "any profits at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4604")

    label("loc_3DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_3ECC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3E46")

    ChrTalk(    #182
        0xFE,
        (
            "The last customers who came\x01",
            "only ordered the cheap food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "Even then, Sanders gave them\x01",
            "a discount.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC9")

    label("loc_3E46")

    OP_A2(0xB)

    ChrTalk(    #184
        0xFE,
        (
            "The last customers who came\x01",
            "only ordered the cheap food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "Even then, Sanders gave them\x01",
            "a discount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "He's too nice.\x02",
    )

    CloseMessageWindow()

    label("loc_3EC9")

    Jump("loc_4604")

    label("loc_3ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_404E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3F9E")

    ChrTalk(    #187
        0xFE,
        (
            "That Private Olnis didn't used to\x01",
            "be much to look at...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "But there's something different\x01",
            "about him lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "I wonder...does he have\x01",
            "a girlfriend?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "If he does...what a waste.\x02",
    )

    CloseMessageWindow()
    Jump("loc_404B")

    label("loc_3F9E")

    OP_A2(0xB)

    ChrTalk(    #191
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "Oh, it's almost time for the\x01",
            "soldiers to have lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "There's something different \x01",
            "about that Private Olnis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "I hope he shows up... *giggle*\x02",
    )

    CloseMessageWindow()

    label("loc_404B")

    Jump("loc_4604")

    label("loc_404E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_41E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_414E")

    ChrTalk(    #195
        0xFE,
        (
            "He's so much manlier than\x01",
            "those inspection soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "It wouldn't surprise me if Jules\x01",
            "or Hector got promoted to the\x01",
            "Royal Guardsmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "Private Jules in that tight\x01",
            "Royal Guardsman uniform...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "...Sweet honeybee of infinity!\x02",
    )

    CloseMessageWindow()
    Jump("loc_41E5")

    label("loc_414E")

    OP_A2(0xB)

    ChrTalk(    #199
        0xFE,
        "I'm glad inspections are over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "That Private Jules, though.\x01",
            "All tall and straight... Yum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "There's just something about\x01",
            "men at work...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41E5")

    Jump("loc_4604")

    label("loc_41E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_431A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_427A")

    ChrTalk(    #202
        0xFE,
        "I love a big, dependable man. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "I think if I ever settle down,\x01",
            "it's going to be with a big,\x01",
            "strong, dependable soldier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4317")

    label("loc_427A")

    OP_A2(0xB)

    ChrTalk(    #204
        0xFE,
        (
            "Wasn't what happened in \x01",
            "Zeiss just TERRIFYING?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "It was nice to know there were\x01",
            "big strong men nearby, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "...Oh, I just LOVE soldiers.\x02",
    )

    CloseMessageWindow()

    label("loc_4317")

    Jump("loc_4604")

    label("loc_431A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4474")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_43EF")

    ChrTalk(    #207
        0xFE,
        (
            "Sanders is a nice person, but\x01",
            "he's a bit...weird, you know...\x01",
            "Not really my type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "I doubt he's ever even THOUGHT\x01",
            "about a woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "Looks are the key to a good\x01",
            "first impression, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4471")

    label("loc_43EF")

    OP_A2(0xB)

    ChrTalk(    #210
        0xFE,
        (
            "Mom, who do you think is better,\x01",
            "Private Jules or Private Hector? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "I like Private Jules, but he's a\x01",
            "bit too...stiff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4471")

    Jump("loc_4604")

    label("loc_4474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4568")

    ChrTalk(    #212
        0xFE,
        (
            "For men it's all face and physique.\x01",
            "Going by that, I'd definitely go for\x01",
            "Private Jules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "Second would be Private Hector...\x01",
            "then maybe the warrant officer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "But everybody else though...?\x01",
            "Better luck next lifetime. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4604")

    label("loc_4568")

    OP_A2(0xB)

    ChrTalk(    #215
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "Oh, it's almost time for the\x01",
            "soldiers to have lunch.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #217
        0xFE,
        (
            "I do hope Private Jules can\x01",
            "make it... *giggle*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4604")

    TalkEnd(0xFE)
    Return()

    # Function_14_38C2 end

    def Function_15_4608(): pass

    label("Function_15_4608")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4615")
    Jump("loc_4AFF")

    label("loc_4615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_46BD")

    ChrTalk(    #218
        0xFE,
        "They've stopped inspections?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "Did they already catch those\x01",
            "criminals, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "I don't remember seeing anything\x01",
            "about it in the Liberl News...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AFF")

    label("loc_46BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4894")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4772")

    ChrTalk(    #221
        0xFE,
        (
            "When I went to Bose I couldn't\x01",
            "take an airship due to all the\x01",
            "trouble with the sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "I wonder if the Goddess Aidios\x01",
            "is angry with us or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4891")

    label("loc_4772")

    OP_A2(0xC)

    ChrTalk(    #223
        0xFE,
        (
            "One of the soldiers just explained\x01",
            "the reason for all the inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "The two of us are citizens of\x01",
            "Grancel so we're fine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "They're holding everyone until\x01",
            "they can confirm their identity\x01",
            "and origin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "This entire terrorist attack\x01",
            "has been a terrible ordeal. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_4891")

    Jump("loc_4AFF")

    label("loc_4894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4943")

    ChrTalk(    #227
        0xFE,
        (
            "I must say, while the service of\x01",
            "the five-star places like the\x01",
            "Anterose is unbeatable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "...the rustic charm of places \x01",
            "like this is a nice change.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A3A")

    label("loc_4943")

    OP_A2(0xC)

    ChrTalk(    #229
        0xFE,
        (
            "I've actually heard good things\x01",
            "about this restaurant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "I heard the menu here can be\x01",
            "a little bit...exotic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "Five star restaurants like the\x01",
            "Anterose are certainly nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "...but the charm of places like\x01",
            "this is a nice change.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A3A")

    Jump("loc_4AFF")

    label("loc_4A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4AFF")

    ChrTalk(    #233
        0xFE,
        (
            "We walked here from the capital\x01",
            "along the Erbe Scenic Route. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "Oh, it's a beautiful little tree\x01",
            "and garden lined path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "If you're going to the capital,\x01",
            "I recommend using it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AFF")

    TalkEnd(0xFE)
    Return()

    # Function_15_4608 end

    def Function_16_4B03(): pass

    label("Function_16_4B03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4B10")
    Jump("loc_4EF6")

    label("loc_4B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4C04")

    ChrTalk(    #236
        0xFE,
        (
            "Thank GOODNESS. Everything\x01",
            "finally seems back to normal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "Still, won't stopping inspections\x01",
            "so soon have an effect on the\x01",
            "investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "I'm certainly not privy to the\x01",
            "military's thinking, but it does\x01",
            "worry me a little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF6")

    label("loc_4C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4D16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4C8E")

    ChrTalk(    #239
        0xFE,
        (
            "All of these incidents just\x01",
            "coming one after another... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "I believe I won't be doing any\x01",
            "traveling for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D13")

    label("loc_4C8E")

    OP_A2(0xD)

    ChrTalk(    #241
        0xFE,
        (
            "It's just awful! A terrorist attack\x01",
            "in Zeiss this time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "We seem to be destined to suffer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "Is it our lot in life?\x02",
    )

    CloseMessageWindow()

    label("loc_4D13")

    Jump("loc_4EF6")

    label("loc_4D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4DD5")

    ChrTalk(    #244
        0xFE,
        (
            "Honestly, I wasn't expecting\x01",
            "much from a little country\x01",
            "restaurant like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "But this is quite tasty! \x01",
            "I wonder if the other dishes\x01",
            "on the menu taste as good...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E8A")

    label("loc_4DD5")

    OP_A2(0xD)

    ChrTalk(    #246
        0xFE,
        "Oh, my... How delicious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "It seems the meals are Liberl-\x01",
            "based, with a few Eastern\x01",
            "spices to add extra flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "A creative and thoroughly\x01",
            "original flavor character.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E8A")

    Jump("loc_4EF6")

    label("loc_4E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4EF6")

    ChrTalk(    #249
        0xFE,
        "My husband never comes home...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "...and even living in the capital\x01",
            "life can get tiresome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF6")

    TalkEnd(0xFE)
    Return()

    # Function_16_4B03 end

    def Function_17_4EFA(): pass

    label("Function_17_4EFA")

    Call(0, 18)
    Return()

    # Function_17_4EFA end

    def Function_18_4EFF(): pass

    label("Function_18_4EFF")

    TalkBegin(0x17)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F5F")
    OP_0D()
    OP_A9(0x49)
    OP_56(0x0)
    TalkEnd(0x17)
    Return()

    label("loc_4F5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F70")
    TalkEnd(0x17)
    Return()

    label("loc_4F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5012")

    ChrTalk(    #251
        0x17,
        (
            "I have to wonder if those \x01",
            "soldiers aren't worn out from\x01",
            "being on alert all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x17,
        (
            "But that's their job. I guess\x01",
            "they've got to accept it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6E")

    label("loc_5012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_509F")

    ChrTalk(    #253
        0x17,
        (
            "I wish my daughter would stop\x01",
            "gossiping about boys and just \x01",
            "pick herself a nice boyfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x17,
        "She's positively SCANDALOUS!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A6E")

    label("loc_509F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5120")

    ChrTalk(    #255
        0x17,
        (
            "Tammy comes by 'to talk' at\x01",
            "LEAST once a day, every day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x17,
        (
            "It's a mystery to me why she\x01",
            "hasn't been fired yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6E")

    label("loc_5120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_51AC")

    ChrTalk(    #257
        0x17,
        (
            "Right after lunch, when the\x01",
            "restaurant is empty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x17,
        (
            "I can almost sense her coming,\x01",
            "ready to talk about her latest\x01",
            "crush.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6E")

    label("loc_51AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5246")

    ChrTalk(    #259
        0x17,
        (
            "Weather looks good today. The\x01",
            "sheets ought to dry nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x17,
        (
            "They'd dry best up on the\x01",
            "Ahnenburg Wall, but the\x01",
            "chief would have my head.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6E")

    label("loc_5246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_52FA")

    ChrTalk(    #261
        0x17,
        (
            "One of the things about this place\x01",
            "is that you end up hearing all the\x01",
            "soldiers' gossip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x17,
        (
            "All that talk of terrorists\x01",
            "and attacks can really scare\x01",
            "you sometimes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6E")

    label("loc_52FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_543A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_536D")

    ChrTalk(    #263
        0x17,
        (
            "We were completely booked\x01",
            "until just a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x17,
        "Everybody went to the capital.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5437")

    label("loc_536D")

    OP_A2(0xE)

    ChrTalk(    #265
        0x17,
        "Hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x17,
        (
            "We were completely booked\x01",
            "until just a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x17,
        "Everybody went to the capital.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x17,
        (
            "The Martial Arts Competition is\x01",
            "coming. I imagine everybody's\x01",
            "pretty excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5437")

    Jump("loc_5A6E")

    label("loc_543A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_5530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_54DB")

    ChrTalk(    #269
        0x17,
        (
            "The other customers have all\x01",
            "left to go to the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x17,
        (
            "The Martial Arts Competition is\x01",
            "coming. I imagine everybody's\x01",
            "pretty excited.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_552D")

    label("loc_54DB")

    OP_A2(0xE)

    ChrTalk(    #271
        0x17,
        "Well, hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x17,
        (
            "The other customers have all\x01",
            "left to go to the capital.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_552D")

    Jump("loc_5A6E")

    label("loc_5530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_5642")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5595")

    ChrTalk(    #273
        0x17,
        (
            "It seems strange to me, but\x01",
            "I'm sure the military has a\x01",
            "perfectly good reason.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_563F")

    label("loc_5595")

    OP_A2(0xE)

    ChrTalk(    #274
        0x17,
        (
            "I don't know why, but all the\x01",
            "inspections have stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x17,
        (
            "It sounds like the chief\x01",
            "hasn't been told the entire\x01",
            "story yet himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x17,
        "Oh, they won't tell ME.\x02",
    )

    CloseMessageWindow()

    label("loc_563F")

    Jump("loc_5A6E")

    label("loc_5642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_57CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_56E8")

    ChrTalk(    #277
        0x17,
        (
            "It's a pretty big mess, that attack\x01",
            "on the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x17,
        (
            "I don't mind the inspections.\x01",
            "I just want them to catch\x01",
            "whoever's responsible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57CB")

    label("loc_56E8")

    OP_A2(0xE)

    ChrTalk(    #279
        0x17,
        (
            "This has turned into a fine\x01",
            "old mess, hasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x17,
        (
            "I hope they catch those\x01",
            "criminals so all of these\x01",
            "inspections can stop...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x17,
        (
            "...but in the meantime, I'd \x01",
            "better get rooms ready for all\x01",
            "the people being held up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57CB")

    Jump("loc_5A6E")

    label("loc_57CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5944")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5826")

    ChrTalk(    #282
        0x17,
        "Tammy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x17,
        (
            "Shouldn't you be at work\x01",
            "instead of gossiping here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5941")

    label("loc_5826")

    OP_A2(0xE)

    ChrTalk(    #284
        0x17,
        (
            "If I were you, I'd be trying to\x01",
            "land that cook, Sanders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x17,
        (
            "He's hardworking, dedicated, and\x01",
            "his eyes don't wander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x17,
        (
            "He might not be much to look at, but\x01",
            "he's dependable--and that's the most\x01",
            "important thing a man can be!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x17,
        (
            "And he's probably a good\x01",
            "listener to boot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5941")

    Jump("loc_5A6E")

    label("loc_5944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5A6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5994")

    ChrTalk(    #288
        0x17,
        "Welcome to the Sanktheim Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x17,
        "Need a place to stay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A6E")

    label("loc_5994")

    OP_A2(0xE)

    ChrTalk(    #290
        0x17,
        "Welcome to the Sanktheim Gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x17,
        (
            "This is the inn. It's open to all\x01",
            "travelers, so come in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x17,
        (
            "There's a restaurant next door\x01",
            "where my daughter works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x17,
        (
            "You should drop by. The food\x01",
            "is surprisingly good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A6E")

    TalkEnd(0x17)
    Return()

    # Function_18_4EFF end

    def Function_19_5A72(): pass

    label("Function_19_5A72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E03")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D6B")
    OP_A2(0x583)

    ChrTalk(    #294
        0xFE,
        "Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "Hey. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x102,
        (
            "#014F...?\x02\x03",

            "#010FAh, hey.\x01",
            "It HAS been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        "#501FWho's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x102,
        (
            "#010FYou remember that kid who was\x01",
            "looking for the quartz fragment in\x01",
            "Rolent, don't you?\x02\x03",

            "Remember? We took a request\x01",
            "to find it a while back.\x02\x03",

            "Are you headed to Grancel?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #299
        0xFE,
        (
            "Nah, we're off to Zeiss. We\x01",
            "made some cash in Grancel and\x01",
            "have some shopping to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "Mom said we're gonna take this\x01",
            "mira and stock up on orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "They say the eyes are the first\x01",
            "to go, but she can still spot a\x01",
            "good deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x101,
        (
            "#506FI can see you're still an\x01",
            "obnoxious brat.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #303
        0xFE,
        (
            "What? I'm only saying what\x01",
            "everybody else is thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "Catch ya later. If I hang around\x01",
            "too long, my mom'll tear me a\x01",
            "new one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E03")

    label("loc_5D6B")


    ChrTalk(    #305
        0xFE,
        "Grancel is some place, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "Everybody seems to have so\x01",
            "much money to spare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "Well, we're off to Zeiss. Gotta go\x01",
            "stock up on some orbments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E03")

    TalkEnd(0xFE)
    Return()

    # Function_19_5A72 end

    def Function_20_5E07(): pass

    label("Function_20_5E07")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6036")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 2)), scpexpr(EXPR_END)), "loc_5ECB")

    ChrTalk(    #308
        0xFE,
        (
            "Grancel is such a nice place.\x01",
            "Our craft goods sell so well\x01",
            "there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "We've managed to put together\x01",
            "some capital. I think we're off to \x01",
            "stock up on orbment products.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6036")

    label("loc_5ECB")

    OP_A2(0x582)

    ChrTalk(    #310
        0xFE,
        (
            "Grancel is such a nice place.\x01",
            "It certainly lives up to the\x01",
            "image of our capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        (
            "Everyone is free with their\x01",
            "wallets, too! Our crafts have\x01",
            "never sold better!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        (
            "We've managed to put together\x01",
            "some capital. I think we're off to \x01",
            "stock up on orbment products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "If we re-sell them in the Republic,\x01",
            "we can make quite a hefty profit\x01",
            "for ourselves.  \x02",
        )
    )

    CloseMessageWindow()

    label("loc_6036")

    TalkEnd(0xFE)
    Return()

    # Function_20_5E07 end

    def Function_21_603A(): pass

    label("Function_21_603A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_616C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6081")

    ChrTalk(    #314
        0xFE,
        (
            "I can't wait to see the Grancel\x01",
            "Landing Port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_616C")

    label("loc_6081")

    OP_A2(0x0)

    ChrTalk(    #315
        0xFE,
        (
            "I'm only going back to the Republic,\x01",
            "but I decided to go back by airship\x01",
            "this once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "There's a real nice Landing Port\x01",
            "in Grancel, which is where I'm headed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        (
            "I'm on a budget though, so I\x01",
            "decided to walk to the capital.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_616C")

    TalkEnd(0xFE)
    Return()

    # Function_21_603A end

    def Function_22_6170(): pass

    label("Function_22_6170")

    Call(0, 23)
    Return()

    # Function_22_6170 end

    def Function_23_6175(): pass

    label("Function_23_6175")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8557")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 7450, 0, 880, 0)
    SetChrPos(0x102, 6480, 0, 880, 0)
    OP_6D(7630, 200, 2180, 0)
    OP_8C(0x9, 180, 0)
    OP_0D()

    ChrTalk(    #318
        0x9,
        (
            "#3PHello.\x01",
            "Welcome to the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x9,
        (
            "#3PWe need you to fill out some\x01",
            "paperwork before we can let\x01",
            "you go on to the capital.\x02",
        )
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
            "[Fill out papers]\x01",      # 0
            "[Leave]\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_62BA"),
        (1, "loc_6346"),
        (SWITCH_DEFAULT, "loc_637B"),
    )


    label("loc_62BA")

    OP_B7(0xD, 0x1)
    AddParty(0xD, 0xFF)
    SetChrFlags(0x10E, 0x80)
    TurnDirection(0x9, 0x102, 0)
    SetChrPos(0x101, 7450, 0, 880, 0)
    SetChrPos(0x102, 6480, 0, 880, 0)

    ChrTalk(    #320
        0x101,
        (
            "#006FOkay, can you give us\x01",
            "the paperwork?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x9,
        "#3PThank you. Please sign here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_637B")

    label("loc_6346")


    ChrTalk(    #322
        0x9,
        (
            "#3PPlease let me know when\x01",
            "you're ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    label("loc_637B")

    OP_A2(0x606)
    OP_28(0x54, 0x1, 0x20)
    OP_28(0x2A, 0x4, 0x40)
    OP_28(0x2D, 0x4, 0x40)
    OP_28(0x2E, 0x4, 0x40)
    OP_28(0x2F, 0x4, 0x40)
    OP_28(0x30, 0x4, 0x40)
    OP_28(0x31, 0x4, 0x40)
    OP_28(0x34, 0x4, 0x40)
    OP_1B(0x0, 0x0, 0x19)
    OP_1B(0x1, 0x0, 0xFFFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #323
        "\x07\x05Estelle and Joshua filled out the paperwork.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #324
        0x9,
        (
            "#3PWhat is it with you kids these\x01",
            "days? Are you brave or are you\x01",
            "just crazy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x9,
        (
            "#3PAre you on some kind of hiking\x01",
            "date on the highway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x101,
        (
            "#004FWh-What?\x02\x03",

            "#503FA... A d-date?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x102,
        (
            "#019F#2PHa ha, it's nothing like that.\x02\x03",

            "We're brother and sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x101,
        "#509F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x9,
        (
            "#3PFunny, you don't look like\x01",
            "siblings. But you do have the\x01",
            "same last name, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x9,
        "#3POkay, you're ready to go.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #331
        0x101,
        "#582F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #332
        0x102,
        (
            "#014FEstelle...?\x02\x03",

            "You seem very...preoccupied...\x01",
            "all of a sudden. Are you okay?\x02\x03",

            "Do you want to stop and rest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x101,
        "#003F*sigh*...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(    #334
        0x101,
        (
            "#007FNo. I'm fine.\x02\x03",

            "Let's just get to the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x102,
        "#012FIf you're sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x9,
        (
            "#3PWell, if you two aren't on a date,\x01",
            "are you going to see the Martial\x01",
            "Arts Competition?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6713():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6713)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #337
        0x101,
        "#004FMartial Arts Competition...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x9,
        "#3PWrong again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x9,
        (
            "#3PThere's an annual Martial Arts\x01",
            "Competition, held in the royal\x01",
            "'Grand Arena.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x9,
        (
            "#3PIt was originally only for the\x01",
            "Royal Guardsmen elite, but now\x01",
            "it's open to any willing fighter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x9,
        (
            "#3PI believe the preliminaries are\x01",
            "starting this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x101,
        "#501FOoooh, that sounds like fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x102,
        (
            "#019F#2PHa ha. That's definitely right\x01",
            "up your alley, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x9,
        (
            "#3PThe queen will be there in person,\x01",
            "so the admission fees are being\x01",
            "discounted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x9,
        (
            "#3PIf I weren't working, I'd be there\x01",
            "myself by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x101,
        "#001FHa ha. Sorry to hear it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #347
        0x101,
        (
            "#006FOf course, I'd rather be participating\x01",
            "than watching.\x02\x03",

            "See if all this training's paid off\x01",
            "yet or not...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #348
        0x102,
        (
            "#010FI can imagine.\x02\x03",

            "But if they've already started the\x01",
            "preliminaries, it'll be impossible\x01",
            "for you to get in.\x02\x03",

            "We've got a job to finish, too,\x01",
            "don't forget. You'll just have\x01",
            "to make do in the stands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x101,
        "#007FHmph. Too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x9,
        "#3P...\x02",
    )

    CloseMessageWindow()

    def lambda_6AF6():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6AF6)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #351
        0x101,
        (
            "#501FS-Sir?\x02\x03",

            "Is something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x9,
        "#3PThat emblem on your chest...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x9,
        (
            "#3PI didn't notice because of your\x01",
            "age...but are you two bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x101,
        "#505FThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x102,
        "#014F#2PIs there a problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x9,
        "#3PNo, not a problem...exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x9,
        "#3PGeez. I never thought...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 13070, 0, 4800, 0)
    OP_70(0x0, 0x14)
    OP_73(0x0)

    def lambda_6C3C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C3C)

    def lambda_6C4A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C4A)

    def lambda_6C58():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6C58)

    def lambda_6C66():
        OP_6D(8280, 0, 2380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C66)
    OP_4A(0x8, 255)
    OP_8E(0x8, 0x30AC, 0x0, 0xB5E, 0x7D0, 0x0)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #358
        0x8,
        (
            "Soldier! Are you loitering while\x01",
            "you're on duty?!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x2670, 0x0, 0x852, 0x7D0, 0x0)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #359
        0x9,
        "#1PS-Sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x8,
        "Is there a problem here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x9,
        "#1PW-Well, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x9,
        (
            "#1PIt's just that...these two...\x01",
            "They're...bracers, sir.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #363
        0x8,
        "Bracers, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x101,
        "#002F???\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 225, 400)

    ChrTalk(    #365
        0x8,
        "You two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x8,
        (
            "I'd like a few minutes of your\x01",
            "time, if that's all right. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x101,
        "#004FWe do need to get to the capital...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x8,
        "Is that so? The capital...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x8,
        (
            "May I ask the nature of your\x01",
            "business in the capital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        "#580FWhat? Well, we've got a...job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x8,
        "What kind of job?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x101,
        (
            "#505FThe professor, he... No!\x02\x03",

            "#003FI mean... How do I put this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x102,
        (
            "#015FI'm sorry, but we have an official\x01",
            "guild contract.\x02\x03",

            "Our business with our client is\x01",
            "a private matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x8,
        "Sounds suspicious to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x8,
        (
            "I'm afraid you're going to have to\x01",
            "explain yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x101,
        (
            "#509FLook, I don't see what the big\x01",
            "problem is...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #377
        0x9,
        (
            "#1PWell, we received information\x01",
            "from Military High Command.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_705C():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_705C)

    def lambda_706A():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_706A)

    ChrTalk(    #378
        0x9,
        (
            "#1PThe Royal Guardsmen have\x01",
            "revolted against the queen and\x01",
            "are staging terrorist attacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x9,
        (
            "#1PAnd it seems that some of these\x01",
            "terrorists may have disguised\x01",
            "themselves as bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x9,
        (
            "#1PSo we're under orders to detain\x01",
            "anyone claiming to be a bracer,\x01",
            "pending investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x101,
        "#005F#3SWhat? WHAT?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #382
        0x8,
        "That's enough, soldier!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #383
        0x8,
        (
            "We're sorry, but we're under\x01",
            "strict orders.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_721A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_721A)

    def lambda_7228():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7228)

    ChrTalk(    #384
        0x8,
        (
            "Until we can confirm your \x01",
            "identification, you're to \x01",
            "remain here at Sanktheim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x101,
        (
            "#009FYou can't be serious!\x01",
            "Why do...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10E, 0x80)
    SetChrPos(0x10E, 21410, 0, -620, 0)

    NpcTalk(    #386
        0x10E,
        "Man's Voice",
        "#3PAhh, THERE you are!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7326():

        label("loc_7326")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_7326")

    QueueWorkItem2(0x101, 1, lambda_7326)

    def lambda_7337():

        label("loc_7337")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_7337")

    QueueWorkItem2(0x8, 1, lambda_7337)

    def lambda_7348():

        label("loc_7348")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_7348")

    QueueWorkItem2(0x9, 1, lambda_7348)

    def lambda_7359():
        OP_8E(0xFE, 0x242C, 0x0, 0x118, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_7359)
    OP_6D(8990, 0, 2340, 2000)

    ChrTalk(    #387
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x102,
        "#014FWhy, you're...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10E, 0x1)

    ChrTalk(    #389
        0x10E,
        (
            "#130F#2PI've been waiting for you!\x02\x03",

            "If you've finished your paperwork,\x01",
            "let's get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x101,
        "#580FWha-Wha-Wha--?\x02",
    )

    CloseMessageWindow()

    def lambda_7428():
        OP_8E(0xFE, 0x1EB4, 0x0, 0xFFFFFE84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7428)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x10E, 400)

    ChrTalk(    #391
        0x102,
        (
            "#010FI apologize, Professor.\x02\x03",

            "It seems we've hit a small snag that\x01",
            "might delay our departure somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x8,
        "#3PJust a... Just a moment, here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x8,
        "#3PWho... Who are...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x8, 400)

    ChrTalk(    #394
        0x10E,
        (
            "#130F#4PAllow me to introduce myself.\x01",
            "I am Specialist of Archeology,\x01",
            "Professor Alba.\x02\x03",

            "I am from North Ambria State\x01",
            "and am here in Liberl for\x01",
            "investigative research.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x8, 0x9, 400)
    Sleep(400)

    ChrTalk(    #395
        0x8,
        (
            "Have you processed this\x01",
            "man's identification?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x9,
        "#1PYes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x9,
        (
            "#1PHis passport checks out and the\x01",
            "Grancel History Museum will\x01",
            "vouch for him as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x8,
        (
            "I see... Then everything appears\x01",
            "to check out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x10E, 400)

    ChrTalk(    #399
        0x8,
        (
            "#3PI apologize for the delay,\x01",
            "Professor Alba.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x8, 400)

    ChrTalk(    #400
        0x8,
        (
            "#3PSo what relationship do\x01",
            "you have with these two?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x10E,
        (
            "#130F#4PWell, they're bracers.\x02\x03",

            "They've saved my life quite a\x01",
            "number of times.\x02\x03",

            "So I decided to have them\x01",
            "accompany me to the capital.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x101, 400)

    ChrTalk(    #402
        0x10E,
        (
            "#130F#2PIsn't that correct?\x01",
            "Joshua? Estelle?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_77DD():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77DD)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #403
        0x101,
        (
            "#004FY-Yes!\x02\x03",

            "#506FThat's it, all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x8,
        "#3PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x8,
        (
            "#3PWell, it seems you have enough\x01",
            "proof of your identity.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #406
        0x8,
        (
            "I apologize to you both for\x01",
            "the misunderstanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x101,
        "#502FNo, no, it's not a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x102,
        (
            "#010FWe know how it is to have\x01",
            "strict protocols. No hard\x01",
            "feelings at all!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(59550, 200, -27280, 0)
    OP_6B(2800, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x10E, 0x4)
    SetChrChipByIndex(0x101, 16)
    SetChrChipByIndex(0x102, 17)
    SetChrChipByIndex(0x10E, 18)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x102, 1)
    SetChrPos(0x10E, 59680, 200, -26270, 180)
    SetChrPos(0x101, 58630, 200, -27770, 90)
    SetChrPos(0x102, 59690, 200, -28910, 0)
    SetChrFlags(0x14, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #409
        0x101,
        (
            "#009FI swear, I'm going to get\x01",
            "wrinkles if there are any\x01",
            "more surprises!\x02\x03",

            "I mean, you started playing along\x01",
            "so fast with the professor!\x02\x03",

            "I thought I had forgotten our\x01",
            "assignment for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x102,
        (
            "#017FHardly.\x02\x03",

            "#010FI had hoped you'd catch on a\x01",
            "little bit quicker, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x101,
        (
            "#007FExcuse me for the poor performance,\x01",
            "Mr. Silver-Tongue!\x02\x03",

            "#003FNot all of us can just lie with\x01",
            "such a straight face...\x01",
            "*grumble* *grumble*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x102,
        "#014FWhat was that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x101,
        "#509FNever mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x102,
        "#014F???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0x10E,
        "#130F#6PHa ha. Sorry to surprise you.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    Sleep(50)
    SetChrSubChip(0x101, 1)

    ChrTalk(    #416
        0x10E,
        (
            "#130F#6PIt just seemed you two were in\x01",
            "some trouble, so I spoke up.\x02\x03",

            "Should I not have?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x101,
        (
            "#506FOh, no. We were definitely in\x01",
            "some trouble back there.\x02\x03",

            "Thank you, Professor Alba.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x102,
        "#010FWe appreciate your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x10E,
        (
            "#130F#6PMy way of returning the favor.\x02\x03",

            "#131FStill, though... What was that\x01",
            "argument all about anyway?\x02\x03",

            "I heard something about\x01",
            "some terrorist attack?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x102,
        (
            "#015FIt seems there's a gang of criminals out\x01",
            "there who have been causing trouble while\x01",
            "disguised as normal citizens.\x02\x03",

            "And the two of us were suspected\x01",
            "of being in said gang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x101,
        (
            "#009FYeah, can you believe that?\x02\x03",

            "I swear, every single person in\x01",
            "the military has a massive stick\x01",
            "up their...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x10E,
        (
            "#131F#6PI see... Very troubling, indeed.\x01",
            "The situation...and the imagery.\x02\x03",

            "By the way, I heard that the\x01",
            "incident at the Carnelia Tower\x01",
            "wound up getting...complicated.\x02\x03",

            "How did that turn out for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x101,
        (
            "#006FHmph... Well...\x02\x03",

            "There were a few loose ends,\x01",
            "but for the most part, we\x01",
            "managed to get things done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x10E,
        (
            "#130F#6PI expected you'd do well.\x02\x03",

            "I could tell you two had the \x01",
            "beginnings of great bracers in\x01",
            "you from the moment we met.\x02\x03",

            "I'm happy to see I was right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        (
            "#008FAww, we don't deserve that.\x01",
            "We've still got a lot to learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x102,
        (
            "#015FWe're still in training, as it is.\x02\x03",

            "#010FBut, Professor...what brings you\x01",
            "to a place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x10E,
        (
            "#130F#6PNaturally, I'm on my way to\x01",
            "the capital.\x02\x03",

            "I was originally going to take\x01",
            "a ship, but I've found myself\x01",
            "short of funds...\x02\x03",

            "Oh, well. Archaeologists need\x01",
            "to exercise, too, so the walk\x01",
            "should do me good.\x02\x03",

            "#131FHa ha ha... *sigh*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x101,
        (
            "#506FYou don't have to beat yourself\x01",
            "up like that.\x02\x03",

            "But still...you sure are poor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x10E,
        (
            "#130F#6PWe scholars of the Humanities\x01",
            "all have financial...issues.\x02\x03",

            "Especially Archeology. Any money\x01",
            "I make goes straight to the next\x01",
            "excavation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x101,
        (
            "#007FThat's too bad.\x02\x03",

            "#006FBut we sure were lucky running\x01",
            "into you back there.\x02\x03",

            "Do you want to come along with\x01",
            "us to the capital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x102,
        (
            "#014FNow just a moment, Estelle.\x02\x03",

            "I'm sure the professor is very\x01",
            "busy with his own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x10E,
        (
            "#130F#6PI'd love to!\x02\x03",

            "The road to the capital can be\x01",
            "dangerous, so having you two\x01",
            "nearby would be a relief.\x02\x03",

            "Not that it's all that far to the\x01",
            "capital anyway...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x102,
        (
            "#010FWell, if you don't mind, then\x01",
            "we would be honored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x101,
        (
            "#001FIt's settled then.\x02\x03",

            "Let's get going!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x10E, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10E, 65535)
    SetChrPos(0x101, 61550, 0, -21950, 0)
    SetChrPos(0x102, 61550, 0, -21950, 0)
    SetChrPos(0x10E, 61550, 0, -21950, 0)
    ClearChrFlags(0x14, 0x80)
    OP_6D(61550, 0, -21950, 0)
    OP_6B(2600, 0)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_8FD6")

    label("loc_8557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_86D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_85E8")

    ChrTalk(    #435
        0x9,
        (
            "The number of travelers has\x01",
            "decreased lately, but we've \x01",
            "got to watch for terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x9,
        "We're on full alert...as usual.\x02",
    )

    CloseMessageWindow()
    Jump("loc_86CE")

    label("loc_85E8")

    OP_A2(0x8)

    ChrTalk(    #437
        0x9,
        (
            "With the birthday celebration and\x01",
            "the tournament back-to-back, \x01",
            "there've been so many people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x9,
        (
            "The number of travelers has\x01",
            "decreased lately, but we've \x01",
            "got to watch for terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x9,
        "We're on full alert...as usual.\x02",
    )

    CloseMessageWindow()

    label("loc_86CE")

    Jump("loc_8FD6")

    label("loc_86D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_878C")

    ChrTalk(    #440
        0x9,
        (
            "I heard the tournament finalists\x01",
            "are a team of bracers versus a\x01",
            "Special Ops team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x9,
        (
            "Those guys in Special Ops\x01",
            "are pretty tough though, so \x01",
            "my money's on them to win it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FD6")

    label("loc_878C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8802")

    ChrTalk(    #442
        0x9,
        (
            "All of our scheduled drills\x01",
            "have been canceled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x9,
        (
            "It's so we can focus on keeping\x01",
            "security on high.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FD6")

    label("loc_8802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_8882")

    ChrTalk(    #444
        0x9,
        (
            "So the annual Martial Arts \x01",
            "Competition starts today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x9,
        (
            "I hope the entrants from the\x01",
            "Royal Guardsman do well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FD6")

    label("loc_8882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_89EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_891E")

    ChrTalk(    #446
        0x9,
        (
            "I've never met Colonel Richard\x01",
            "in person myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x9,
        (
            "But everything I've read about\x01",
            "him in the Liberl News has\x01",
            "really made me a fan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E9")

    label("loc_891E")

    OP_A2(0x8)

    ChrTalk(    #448
        0x9,
        (
            "I've never met Colonel Richard\x01",
            "in person myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x9,
        (
            "But everything I've read about\x01",
            "him in the Liberl News has\x01",
            "really made me a fan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0x9,
        (
            "He's always got such a clear-cut\x01",
            "opinion on the issues!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89E9")

    Jump("loc_8FD6")

    label("loc_89EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_8B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8AA6")

    ChrTalk(    #451
        0x9,
        (
            "Lately, we've had a few soldiers on\x01",
            "patrol at the Erbe Scenic Route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x9,
        (
            "If any terrorists got into the\x01",
            "queen's birthday celebration,\x01",
            "it'd be a complete disaster.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B41")

    label("loc_8AA6")

    OP_A2(0x8)

    ChrTalk(    #453
        0x9,
        (
            "Hello there. No hard feelings\x01",
            "about last time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x9,
        (
            "Your paperwork's already been\x01",
            "processed, so you're free to\x01",
            "come and go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0x9,
        "Have a safe trip!\x02",
    )

    CloseMessageWindow()

    label("loc_8B41")

    Jump("loc_8FD6")

    label("loc_8B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_8B4E")
    Jump("loc_8FD6")

    label("loc_8B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_8B58")
    Jump("loc_8FD6")

    label("loc_8B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_8C03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8BA1")

    ChrTalk(    #456
        0x9,
        (
            "Sometimes I wonder why we\x01",
            "do inspections at all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C00")

    label("loc_8BA1")

    OP_A2(0x8)

    ChrTalk(    #457
        0x9,
        "We stopped them so suddenly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x9,
        (
            "We haven't caught anyone yet,\x01",
            "so what was the point?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C00")

    Jump("loc_8FD6")

    label("loc_8C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_8D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8C8B")

    ChrTalk(    #459
        0x9,
        (
            "We're holding inspections to\x01",
            "prevent terrorist activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x9,
        (
            "I'm sorry, but I can't just let\x01",
            "you pass through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D44")

    label("loc_8C8B")

    OP_A2(0x8)

    ChrTalk(    #461
        0x9,
        (
            "We were supposed to be\x01",
            "having a drill today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x9,
        (
            "Since that terrorist attack though,\x01",
            "we've been on an emergency alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0x9,
        (
            "I'm sorry, but I can't just let\x01",
            "you pass through.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D44")

    Jump("loc_8FD6")

    label("loc_8D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_8DC7")

    ChrTalk(    #464
        0x9,
        "Welcome to the Sanktheim Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0x9,
        (
            "Take some time to enjoy the\x01",
            "majesty of the Ahnenburg Wall\x01",
            "while you're here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FD6")

    label("loc_8DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8FD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8EF3")

    ChrTalk(    #466
        0x9,
        (
            "We've repurposed it into a \x01",
            "checkpoint for the capital,\x01",
            "but the historic ruins remain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0x9,
        (
            "Even with the public airships,\x01",
            "we still have many visitors\x01",
            "who come just for sightseeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0x9,
        (
            "The queen's birthday celebration\x01",
            "is coming up so there ought to\x01",
            "be an increase in traffic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FD6")

    label("loc_8EF3")

    OP_A2(0x8)

    ChrTalk(    #469
        0x9,
        "Welcome to the Sanktheim Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x9,
        (
            "We've repurposed it into a \x01",
            "checkpoint for the capital, \x01",
            "but the historic ruins remain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0x9,
        (
            "Even with the public airships,\x01",
            "we still have many visitors\x01",
            "who come just for sightseeing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FD6")

    TalkEnd(0x9)
    Return()

    # Function_23_6175 end

    def Function_24_8FDA(): pass

    label("Function_24_8FDA")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9031")

    ChrTalk(    #472
        0x106,
        (
            "#050FSo this is Grancel...\x02\x03",

            "We don't have any reason\x01",
            "to be here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9108")

    label("loc_9031")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90A4")
    TurnDirection(0x102, 0x1, 400)

    ChrTalk(    #473
        0x102,
        (
            "#010FThe Grancel region's just\x01",
            "up that way.\x02\x03",

            "We won't be able to get in\x01",
            "without a pass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9108")

    label("loc_90A4")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(    #474
        0x102,
        (
            "#010FThe Grancel region's\x01",
            "just up that way.\x02\x03",

            "We won't be able to get in\x01",
            "without a pass.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9108")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_24_8FDA end

    def Function_25_9124(): pass

    label("Function_25_9124")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91B1")

    ChrTalk(    #475
        0x104,
        (
            "#030FHmm...\x01",
            "This exit leads to Zeiss...\x02\x03",

            "I'd like to visit there someday...\x01",
            "Unfortunately, that day has yet\x01",
            "to arrive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9335")

    label("loc_91B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9241")

    ChrTalk(    #476
        0x108,
        (
            "#073FAh. This is the exit to a\x01",
            "neighboring region.\x02\x03",

            "I don't care to have to deal\x01",
            "with the soldiers. Why don't\x01",
            "we turn back?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9335")

    label("loc_9241")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9257")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_925E")

    label("loc_9257")

    TurnDirection(0x102, 0x0, 400)

    label("loc_925E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_92DD")

    ChrTalk(    #477
        0x102,
        (
            "#012FIt looks like the checkpoint's\x01",
            "been blockaded.\x02\x03",

            "We don't need to let the soldiers\x01",
            "see us. Let's turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9335")

    label("loc_92DD")


    ChrTalk(    #478
        0x102,
        (
            "#010FThis way leads to Zeiss.\x02\x03",

            "We won't be able to pass\x01",
            "without a permit to do so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9335")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_25_9124 end

    def Function_26_9351(): pass

    label("Function_26_9351")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(57670, 5000, 52610, 0)
    SetChrPos(0x101, 57160, 5000, 52610, 133)
    SetChrPos(0x102, 58440, 5000, 53220, 189)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93AA")
    SetChrPos(0x107, 57140, 5000, 51520, 103)

    label("loc_93AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93C9")
    SetChrPos(0x106, 57290, 5000, 53600, 134)

    label("loc_93C9")

    OP_0D()
    OP_64(0x0, 0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #479
        "\x07\x00A package was found, wrapped in oil paper.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #480
        "\x07\x00Inside was \x07\x0231 Cypress Trees\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x345, 1)
    OP_28(0x30, 0x1, 0x4)

    ChrTalk(    #481
        0x101,
        "#508FWoohoo! Found it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0x102,
        (
            "#010FThat's the last one...\x02\x03",

            "Now we can finally finish up\x01",
            "our work for the librarian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0x101,
        "#007FYou ain't kidding.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #484
        0x101,
        "#004F...Huh?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_953D")

    def lambda_9535():
        TurnDirection(0x107, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9535)

    label("loc_953D")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #485
        0x102,
        "#014FWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0x101,
        (
            "#002FThere's a card stuck in the book.\x02\x03",

            "...Aaaand something's written on it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #487
        (
            "\x07\x00'You have done well.\x01",
            "Though I know you not, \x01",
            "I salute you for coming so far.\x01",
            "Allow me to introduce myself.\x01",
            "I am a quartz researcher, and\x01",
            "the criminal who hid the three\x01",
            "books.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #488
        (
            "\x07\x00'I have used the riddles as a way\x01",
            "to find someone intelligent, to \x01",
            "whom I could entrust my work...\x01",
            "And you lived up to my hopes\x01",
            "and expectations remarkably.\x01\x01",
            "Consider the enclosed quartz your \x01",
            "reward. Take care when examining it.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #489
        (
            "\x07\x00'Thank you for all your time.\x01",
            "I truly hope that my quartz \x01",
            "will prove useful to you.\x01\x01",
            "P.S. If you have found this package\x01",
            "by sheer chance... How embarrassing...\x01",
            "and, LUCKY YOU!\x01\x01",
            "Please return it to the 2nd floor\x01",
            "archives of the central factory.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #490
        0x101,
        (
            "#007F...That's it.\x02\x03",

            "#505FSo it was all one big\x01",
            "practical joke?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9971")
    TurnDirection(0x107, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_992C")

    ChrTalk(    #491
        0x107,
        "#060FYeah, I guess so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0x102,
        "#010FHave you looked in the package?\x02",
    )

    CloseMessageWindow()
    Jump("loc_996E")

    label("loc_992C")


    ChrTalk(    #493
        0x107,
        "#060FI guess so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0x102,
        "#010FHave you looked in the package?\x02",
    )

    CloseMessageWindow()

    label("loc_996E")

    Jump("loc_99AE")

    label("loc_9971")


    ChrTalk(    #495
        0x102,
        (
            "#010FSo it would seem.\x02\x03",

            "Have you looked in the package?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99AE")


    ChrTalk(    #496
        0x101,
        (
            "#004FOh, right... Let's see\x01",
            "what we can see...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #497
        "\x07\x00Found \x07\x02Impede 3\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #498
        0x101,
        "#001FHeh heh... Jackpot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x102,
        (
            "#010FI think we should check in with\x01",
            "the client, for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0x101,
        "#006FFine by me.\x02",
    )

    CloseMessageWindow()
    OP_3E(0x2C3, 1)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9ADE")

    def lambda_9ACF():
        OP_92(0x107, 0x101, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9ACF)

    label("loc_9ADE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B01")

    def lambda_9AF2():
        OP_92(0x106, 0x101, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_9AF2)

    label("loc_9B01")

    OP_92(0x102, 0x101, 0x0, 0xBB8, 0x0)
    EventEnd(0x0)
    Return()

    # Function_26_9351 end

    def Function_27_9B12(): pass

    label("Function_27_9B12")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_27_9B12 end

    SaveToFile()

Try(main)
