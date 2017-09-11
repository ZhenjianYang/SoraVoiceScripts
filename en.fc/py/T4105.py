from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4105   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4105.x',
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
        'Sophina',                              # 9
        'Rutherford',                           # 10
        'Finella',                              # 11
        'Carnero',                              # 12
        'Tiffany',                              # 13
        'Mechanic Payton',                      # 14
        'Royal Army Soldier',                   # 15
        'Royal Army Soldier',                   # 16
        'Royal Army Soldier',                   # 17
        'Royal Army Soldier',                   # 18
        'Special Ops Soldier',                  # 19
        'Special Ops Soldier',                  # 20
        'Special Ops Soldier',                  # 21
        'Royal Army Soldier',                   # 22
        'Faye',                                 # 23
        'Rudi',                                 # 24
        'Private Brahm',                        # 25
        'Grancel - East Block',                 # 26
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH01450 ._CH',             # 03
        'ED6_DT07/CH01550 ._CH',             # 04
        'ED6_DT07/CH01450 ._CH',             # 05
        'ED6_DT07/CH01640 ._CH',             # 06
        'ED6_DT07/CH01610 ._CH',             # 07
        'ED6_DT07/CH01500 ._CH',             # 08
        'ED6_DT07/CH01300 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH01450P._CP',             # 03
        'ED6_DT07/CH01550P._CP',             # 04
        'ED6_DT07/CH01450P._CP',             # 05
        'ED6_DT07/CH01640P._CP',             # 06
        'ED6_DT07/CH01610P._CP',             # 07
        'ED6_DT07/CH01500P._CP',             # 08
        'ED6_DT07/CH01300P._CP',             # 09
    )

    DeclNpc(
        X                   = 56030,
        Z                   = 250,
        Y                   = 133380,
        Direction           = 258,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 77500,
        Z                   = 1500,
        Y                   = 142010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58770,
        Z                   = 250,
        Y                   = 137000,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 93960,
        Z                   = 1500,
        Y                   = 144440,
        Direction           = 293,
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
        X                   = 84910,
        Z                   = 1500,
        Y                   = 141950,
        Direction           = 187,
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
        X                   = 67710,
        Z                   = -10000,
        Y                   = 159300,
        Direction           = 84,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 73000,
        Z                   = -9800,
        Y                   = 158970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 63050,
        Z                   = -3000,
        Y                   = 160490,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 63040,
        Z                   = -3000,
        Y                   = 159620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 73620,
        Z                   = 1500,
        Y                   = 143000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 63050,
        Z                   = -3000,
        Y                   = 160490,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 63040,
        Z                   = -3000,
        Y                   = 159620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 73620,
        Z                   = 1500,
        Y                   = 143000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 72120,
        Z                   = -9800,
        Y                   = 158930,
        Direction           = 90,
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
        X                   = 72480,
        Z                   = -10000,
        Y                   = 169900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 72480,
        Z                   = -10000,
        Y                   = 170720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 72480,
        Z                   = -10000,
        Y                   = 170720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        TalkFunctionIndex   = 7,
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
        TalkFunctionIndex   = 21,
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
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3A6",          # 00, 0
        "Function_1_563",          # 01, 1
        "Function_2_689",          # 02, 2
        "Function_3_806",          # 03, 3
        "Function_4_82A",          # 04, 4
        "Function_5_ECC",          # 05, 5
        "Function_6_174B",         # 06, 6
        "Function_7_1FDB",         # 07, 7
        "Function_8_1FE0",         # 08, 8
        "Function_9_28E4",         # 09, 9
        "Function_10_2AE9",        # 0A, 10
        "Function_11_2C82",        # 0B, 11
        "Function_12_3175",        # 0C, 12
        "Function_13_320A",        # 0D, 13
        "Function_14_32AE",        # 0E, 14
        "Function_15_3326",        # 0F, 15
        "Function_16_334C",        # 10, 16
        "Function_17_33C9",        # 11, 17
        "Function_18_3444",        # 12, 18
        "Function_19_35BB",        # 13, 19
        "Function_20_3778",        # 14, 20
        "Function_21_3A97",        # 15, 21
        "Function_22_3B6C",        # 16, 22
    )


    def Function_0_3A6(): pass

    label("Function_0_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3E8")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xD, 73000, -9800, 158970, 270)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_3E0")
    ClearChrFlags(0x18, 0x80)
    Jump("loc_3E5")

    label("loc_3E0")

    ClearChrFlags(0x17, 0x80)

    label("loc_3E5")

    Jump("loc_562")

    label("loc_3E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_432")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xB, 68580, 250, 147780, 45)
    SetChrPos(0xC, 66400, 0, 145250, 135)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_562")

    label("loc_432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_477")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xB, 68580, 250, 147780, 45)
    SetChrPos(0xC, 66400, 0, 145250, 135)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_562")

    label("loc_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4A3")
    SetChrPos(0xC, 66860, 250, 147300, 90)
    SetChrPos(0xD, 68610, 250, 147270, 270)
    Jump("loc_562")

    label("loc_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4BE")
    SetChrPos(0xD, 68470, 250, 147030, 90)
    Jump("loc_562")

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrPos(0xC, 77380, 1500, 144440, 270)
    SetChrPos(0xD, 76010, 1500, 144460, 90)
    Jump("loc_562")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_505")
    SetChrPos(0xB, 83030, 1700, 141250, 180)
    Jump("loc_562")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_520")
    SetChrPos(0xB, 83030, 1700, 141250, 180)
    Jump("loc_562")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_540")
    SetChrPos(0xB, 83030, 1700, 141250, 180)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_562")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_55B")
    SetChrPos(0xB, 83030, 1700, 141250, 180)
    Jump("loc_562")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_562")

    label("loc_562")

    Return()

    # Function_0_3A6 end

    def Function_1_563(): pass

    label("Function_1_563")

    OP_16(0x2, 0xFA0, 0xFFFF5808, 0x7148, 0x3005F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_605")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B5")
    OP_B1("t4105_y0")
    Jump("loc_602")

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CE")
    OP_B1("t4105_y1")
    Jump("loc_602")

    label("loc_5CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E7")
    OP_B1("t4105_y2")
    Jump("loc_602")

    label("loc_5E7")

    OP_B1("t4105_y0")
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_6F(0x5, 100)

    label("loc_602")

    Jump("loc_667")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61D")
    OP_B1("t4105_0")
    Jump("loc_667")

    label("loc_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_635")
    OP_B1("t4105_1")
    Jump("loc_667")

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64D")
    OP_B1("t4105_2")
    Jump("loc_667")

    label("loc_64D")

    OP_B1("t4105_0")
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_6F(0x5, 100)

    label("loc_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_677")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_688")
    OP_72(0x6, 0x10)

    label("loc_688")

    Return()

    # Function_1_563 end

    def Function_2_689(): pass

    label("Function_2_689")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AE")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7F0")

    label("loc_6AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C7")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7F0")

    label("loc_6C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E0")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7F0")

    label("loc_6E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F9")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7F0")

    label("loc_6F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_712")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7F0")

    label("loc_712")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7F0")

    label("loc_72B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_744")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7F0")

    label("loc_744")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75D")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7F0")

    label("loc_75D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_776")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7F0")

    label("loc_776")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7F0")

    label("loc_78F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A8")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7F0")

    label("loc_7A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C1")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7F0")

    label("loc_7C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DA")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7F0")

    label("loc_7DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F0")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_805")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7F0")

    label("loc_805")

    Return()

    # Function_2_689 end

    def Function_3_806(): pass

    label("Function_3_806")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_829")
    OP_8D(0xFE, 52840, 136880, 55890, 126400, 3000)
    Jump("Function_3_806")

    label("loc_829")

    Return()

    # Function_3_806 end

    def Function_4_82A(): pass

    label("Function_4_82A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_896")

    ChrTalk(    #0
        0xFE,
        (
            "Finally, the airships are back\x01",
            "on track again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Now maybe I can get some work\x01",
            "done...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_949")

    ChrTalk(    #2
        0xFE,
        (
            "The Royal Army soldiers have\x01",
            "all been replaced with those\x01",
            "soldiers in black armor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "They're at least ten times more\x01",
            "intimidating. But maybe that's\x01",
            "the point...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_9EA")

    ChrTalk(    #4
        0xFE,
        (
            "I've been run out of my workplace.\x01",
            "Damned military types shut it down\x01",
            "on me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "The airships are all grounded,\x01",
            "too. What the hell is going on?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_9EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_A51")

    ChrTalk(    #6
        0xFE,
        (
            "We were finally able to get an\x01",
            "airship out of port today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "I sure hope it keeps up!\x02",
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_A9A")

    ChrTalk(    #8
        0xFE,
        (
            "We were finally able to get an\x01",
            "airship out of port today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_B45")

    ChrTalk(    #9
        0xFE,
        (
            "I'm truly in awe of every one of\x01",
            "the engineers who worked on making\x01",
            "the Arseille. It's simply amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I'd love to work on a project\x01",
            "that big one day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C2B")

    ChrTalk(    #11
        0xFE,
        (
            "O-kay, that...SHOULD take care\x01",
            "of the necessary maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Our schedule's been thrown off so badly, we have\x01",
            "no idea at all when the next airship is arriving.\x01",
            "And working with no clear deadline is EXHAUSTING.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CBB")

    ChrTalk(    #13
        0xFE,
        (
            "Uhh, so instead of the Cecilia, we've\x01",
            "got a random military vessel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Wonder if the Cecilia's even going\x01",
            "to make it today... \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_D17")

    ChrTalk(    #15
        0xFE,
        "Everything's crazy right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Not a single airship's touching\x01",
            "ground...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_D6E")

    ChrTalk(    #17
        0xFE,
        (
            "Uhh...so all of the machinery\x01",
            "seems fine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "Next on the list is...\x02",
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_EC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E12")

    ChrTalk(    #19
        0xFE,
        (
            "Ever since I became head of\x01",
            "maintenance, everything's just\x01",
            "gone to hell around me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "First it was sky bandits, now\x01",
            "there are terrorists...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC8")

    label("loc_E12")

    OP_A2(0x3)

    ChrTalk(    #21
        0xFE,
        (
            "Ever since I became head of\x01",
            "maintenance, everything's just\x01",
            "gone to hell around me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "First it was sky bandits, now\x01",
            "there are terrorists...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "These are some dark times.\x02",
    )

    CloseMessageWindow()

    label("loc_EC8")

    TalkEnd(0xFE)
    Return()

    # Function_4_82A end

    def Function_5_ECC(): pass

    label("Function_5_ECC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_F43")

    ChrTalk(    #24
        0xFE,
        (
            "It's so nice to finally get\x01",
            "back to some real work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "We've got to win back our\x01",
            "customers' trust.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1747")

    label("loc_F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_FC1")

    ChrTalk(    #26
        0xFE,
        (
            "Let me tell you, I've had it up\x01",
            "to HERE with those army guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I wish they'd just LEAVE US THE\x01",
            "HELL ALONE.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1747")

    label("loc_FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_10D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1001")

    ChrTalk(    #28
        0xFE,
        "...Huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "Where'd Payton get off to?\x02",
    )

    CloseMessageWindow()
    Jump("loc_10D2")

    label("loc_1001")

    OP_A2(0x4)
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0xFE,
        "Anger...rising...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "They're never gonna catch those\x01",
            "damned terrorists. I swear, their\x01",
            "collective I.Q. is like, twelve!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Swaggering around like that...\x01",
            "Makes me sick!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D2")

    Jump("loc_1747")

    label("loc_10D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1166")

    ChrTalk(    #33
        0xFE,
        (
            "You can really tell that Payton\x01",
            "used to work in the central factory\x01",
            "at Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "If only he'd become our consulting\x01",
            "engineer...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1747")

    label("loc_1166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_11C5")

    ChrTalk(    #35
        0xFE,
        (
            "So, the next ship in should be...\x01",
            "the Cecilia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "We need to be ready for it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1747")

    label("loc_11C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1336")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_125D")

    ChrTalk(    #37
        0xFE,
        (
            "Wonder if those damned army\x01",
            "bozos'll finally clear out\x01",
            "of here now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "If they're not gonna help, then\x01",
            "they're just in our way!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1333")

    label("loc_125D")

    OP_A2(0x4)

    ChrTalk(    #39
        0xFE,
        (
            "I heard lots of juicy tidbits\x01",
            "about the Arseille from Payton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Isn't it an amazing ship? And it's\x01",
            "still supposedly unfinished!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "If the army weren't around, I'd\x01",
            "gladly give you the grand tour\x01",
            "of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1333")

    Jump("loc_1747")

    label("loc_1336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_13F0")

    ChrTalk(    #42
        0xFE,
        (
            "No matter how late an airship\x01",
            "is, there's one thing we ALWAYS\x01",
            "have to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "We have to do everything we can\x01",
            "to ensure that every last ship\x01",
            "is one hundred percent safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1747")

    label("loc_13F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_155B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_14A9")

    ChrTalk(    #44
        0xFE,
        (
            "That captain's got one hell of\x01",
            "an attitude on her. Pisses me\x01",
            "off like you wouldn't believe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Though the chief's sniveling\x01",
            "cowardice pisses me off even\x01",
            "more...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1558")

    label("loc_14A9")

    OP_A2(0x4)

    ChrTalk(    #46
        0xFE,
        (
            "Just who does that captain think\x01",
            "she is, anyway?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Pisses me off like you wouldn't\x01",
            "believe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Though the chief's sniveling\x01",
            "cowardice pisses me off even\x01",
            "more...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1558")

    Jump("loc_1747")

    label("loc_155B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_15E0")

    ChrTalk(    #49
        0xFE,
        "They're not coming, are they...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Wonder if they got caught in\x01",
            "some other crazy messed-up\x01",
            "incident or something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1747")

    label("loc_15E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_164E")

    ChrTalk(    #51
        0xFE,
        "All the machinery checks out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Orbal pressure is lookin' good.\x01",
            "Aaaaaand, that's it for me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1747")

    label("loc_164E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1747")

    ChrTalk(    #53
        0xFE,
        (
            "This new maintenance chief... Well, let me put it\x01",
            "to you this way. Ever managed a maintenance team\x01",
            "before? No? ...You'd still be better at the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I wish we'd been given a REAL man...\x01",
            "Someone we could actually depend on\x01",
            "and trust.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1747")

    TalkEnd(0xFE)
    Return()

    # Function_5_ECC end

    def Function_6_174B(): pass

    label("Function_6_174B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_18E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_17EE")

    ChrTalk(    #55
        0xFE,
        (
            "Finally, we can resume tests on\x01",
            "the Arseille!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Now that Professor Russell is\x01",
            "safe, I hope the project can\x01",
            "finally move forward again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E0")

    label("loc_17EE")

    OP_A2(0x5)

    ChrTalk(    #57
        0xFE,
        (
            "Finally, we can resume tests on\x01",
            "the Arseille!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Gotta get that new central factory\x01",
            "engine for 'er finished up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Now that Professor Russell is\x01",
            "safe, I hope the project can\x01",
            "finally move forward again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "All right, let's GO!\x02",
    )

    CloseMessageWindow()

    label("loc_18E0")

    Jump("loc_1FD7")

    label("loc_18E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_18ED")
    Jump("loc_1FD7")

    label("loc_18ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_18F7")
    Jump("loc_1FD7")

    label("loc_18F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1933")

    ChrTalk(    #61
        0xFE,
        (
            "Young people have such drive\x01",
            "and ambition...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD7")

    label("loc_1933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1B6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1A34")

    ChrTalk(    #62
        0xFE,
        (
            "(I heard from my friends in\x01",
            "the factory that Professor\x01",
            "Russell's been kidnapped...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "(...but I have a feeling that won't last long.\x01",
            "You can't keep that man away from his post. He'll\x01",
            "escape and make his way back... I know he will.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6C")

    label("loc_1A34")

    OP_A2(0x5)

    ChrTalk(    #64
        0xFE,
        "Just between you and me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "(I heard from my friends in\x01",
            "the factory that Professor\x01",
            "Russell's been kidnapped...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "(...and Tita along with him...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "(...but I have a feeling that won't last long.\x01",
            "You can't keep that man away from his post. He'll\x01",
            "escape and make his way back... I know he will.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6C")

    Jump("loc_1FD7")

    label("loc_1B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1C42")

    ChrTalk(    #68
        0xFE,
        (
            "Ahem! Sorry. I know I shouldn't\x01",
            "dump this on you, but I needed to\x01",
            "say it to SOMEBODY...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "I want to keep running tests on the\x01",
            "Arseille, so I hope all this muckity\x01",
            "muck gets wrapped up a.s.a.p.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD7")

    label("loc_1C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1C98")

    ChrTalk(    #70
        0xFE,
        (
            "Goddess, I'm bored. Maybe I'll\x01",
            "go help out on the Linde for a\x01",
            "while...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD7")

    label("loc_1C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D44")

    ChrTalk(    #71
        0xFE,
        (
            "That patrol ship...is the one that\x01",
            "was supplied to Leiston Fortress,\x01",
            "if I'm not mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "What could have happened, to have\x01",
            "brought it all this way...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD7")

    label("loc_1D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1DF8")

    ChrTalk(    #73
        0xFE,
        (
            "The Arseille is still an unfinished\x01",
            "design. A prototype, if you will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I want to move it to the next\x01",
            "phase of testing, but things\x01",
            "have stalled for the moment...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD7")

    label("loc_1DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1E81")

    ChrTalk(    #75
        0xFE,
        (
            "...I'm worried about\x01",
            "Lieutenant Schwarz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "There's no way she and the Royal\x01",
            "Guardsmen would have ever staged\x01",
            "a coup.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD7")

    label("loc_1E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1FD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1F0F")

    ChrTalk(    #77
        0xFE,
        (
            "The Arseille is specifically owned\x01",
            "by the royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "The Royal Army shouldn't have\x01",
            "any authority to impound it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD7")

    label("loc_1F0F")

    OP_A2(0x5)

    ChrTalk(    #79
        0xFE,
        (
            "The Arseille is specifically owned\x01",
            "by the royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "The Royal Army shouldn't have\x01",
            "any authority to impound it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Has Her Majesty truly given them\x01",
            "the authority to do such a thing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FD7")

    TalkEnd(0xFE)
    Return()

    # Function_6_174B end

    def Function_7_1FDB(): pass

    label("Function_7_1FDB")

    Call(0, 8)
    Return()

    # Function_7_1FDB end

    def Function_8_1FE0(): pass

    label("Function_8_1FE0")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_205D")

    ChrTalk(    #82
        0xA,
        (
            "We got wrapped up in the coup\x01",
            "d'etat before we even knew what\x01",
            "was going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        "It was...kind of a shock!\x02",
    )

    CloseMessageWindow()
    Jump("loc_28E0")

    label("loc_205D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_20AD")

    ChrTalk(    #84
        0xA,
        (
            "*sigh* When are we going to get\x01",
            "back to business as usual again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E0")

    label("loc_20AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_217E")

    ChrTalk(    #85
        0xA,
        (
            "The Royal Army's put a hold on all\x01",
            "passenger and shipping flights today\x01",
            "as an anti-terrorist countermeasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xA,
        (
            "We'd be happy to offer you a\x01",
            "full refund on your tickets,\x01",
            "if you'd like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2273")

    label("loc_217E")

    OP_A2(0x2)

    ChrTalk(    #87
        0xA,
        (
            "Our deepest apologies for any\x01",
            "inconvenience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xA,
        (
            "The Royal Army's put a hold on all\x01",
            "passenger and shipping flights today\x01",
            "as an anti-terrorist countermeasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "We'd be happy to offer you a\x01",
            "full refund on your tickets,\x01",
            "if you'd like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2273")

    Jump("loc_28E0")

    label("loc_2276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_22CE")

    ChrTalk(    #90
        0xA,
        (
            "*sigh* Hopefully, we can return\x01",
            "to our regular flight schedule\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E0")

    label("loc_22CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2377")

    ChrTalk(    #91
        0xA,
        (
            "Whenever the airships are late\x01",
            "now, I think back to the sky\x01",
            "bandit incident in Bose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "I don't think my heart could take\x01",
            "another incident like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E0")

    label("loc_2377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2458")

    ChrTalk(    #93
        0xA,
        (
            "Patrols from Royal Army personnel\x01",
            "seem more common around here of\x01",
            "late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "Combine that ominous sight with all the recent\x01",
            "incidents, and I'm sure you can understand why\x01",
            "EVERYTHING MAKES ME VERY UNEASY NOW.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E0")

    label("loc_2458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_24EE")

    ChrTalk(    #95
        0xA,
        (
            "The airship in port is the Linde,\x01",
            "currently scheduled to depart for\x01",
            "Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "All passengers, please proceed\x01",
            "to the boarding gates.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E0")

    label("loc_24EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2574")

    ChrTalk(    #97
        0xA,
        (
            "With all the army arrivals and\x01",
            "departures, our regularly scheduled\x01",
            "flights are ALL running late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xA,
        "What a bother...\x02",
    )

    CloseMessageWindow()
    Jump("loc_28E0")

    label("loc_2574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_26A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25E7")

    ChrTalk(    #99
        0xA,
        (
            "How odd that the Linde hasn't\x01",
            "made port yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        (
            "I'd heard she was running on time\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A4")

    label("loc_25E7")

    OP_A2(0x2)

    ChrTalk(    #101
        0xA,
        (
            "How odd that the Linde hasn't\x01",
            "made port yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "I'd heard she was running on time\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        (
            "What am I supposed to tell all\x01",
            "the customers who've been waiting\x01",
            "patiently for it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A4")

    Jump("loc_28E0")

    label("loc_26A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_270D")

    ChrTalk(    #104
        0xA,
        (
            "The Cecilia, originally scheduled\x01",
            "to arrive at noon, has only just\x01",
            "now touched ground.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E0")

    label("loc_270D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_28E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27CD")

    ChrTalk(    #105
        0xA,
        (
            "Due to Royal Army inspection\x01",
            "procedures, our departure times\x01",
            "have been severely delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "We will make an offical\x01",
            "announcement regarding \x01",
            "boarding as soon as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E0")

    label("loc_27CD")

    OP_A2(0x2)

    ChrTalk(    #107
        0xA,
        (
            "We apologize, and thank\x01",
            "you for your patience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xA,
        (
            "Due to Royal Army inspection procedures,\x01",
            "our departure and arrival times alike have\x01",
            "been severely delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        (
            "Further information regarding the\x01",
            "boarding process will be given upon\x01",
            "the orbalship's arrival in port.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E0")

    TalkEnd(0xA)
    Return()

    # Function_8_1FE0 end

    def Function_9_28E4(): pass

    label("Function_9_28E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_28F1")
    Jump("loc_2AE5")

    label("loc_28F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_28FB")
    Jump("loc_2AE5")

    label("loc_28FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2905")
    Jump("loc_2AE5")

    label("loc_2905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_290F")
    Jump("loc_2AE5")

    label("loc_290F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2919")
    Jump("loc_2AE5")

    label("loc_2919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2923")
    Jump("loc_2AE5")

    label("loc_2923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_292D")
    Jump("loc_2AE5")

    label("loc_292D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2937")
    Jump("loc_2AE5")

    label("loc_2937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_29C7")

    ChrTalk(    #110
        0xFE,
        (
            "I came here to sell some ship fuselages\x01",
            "to the travel company...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "But it looks like this isn't\x01",
            "quite the time for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD1")

    label("loc_29C7")

    OP_A2(0x1)

    ChrTalk(    #112
        0xFE,
        (
            "I came here to sell some ship fuselages\x01",
            "to the travel company...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "But it looks like this isn't\x01",
            "quite the time for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Figure I'll hop back to Zeiss and check on the\x01",
            "new engine project, as I am a bit worried about\x01",
            "its future with things as they are.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD1")

    Jump("loc_2AE5")

    label("loc_2AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2ADE")
    Jump("loc_2AE5")

    label("loc_2ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2AE5")

    label("loc_2AE5")

    TalkEnd(0xFE)
    Return()

    # Function_9_28E4 end

    def Function_10_2AE9(): pass

    label("Function_10_2AE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2B56")

    ChrTalk(    #115
        0xFE,
        (
            "It looks like the airships are\x01",
            "moving, at long last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "Finally, I can get back to Bose!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C7E")

    label("loc_2B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2BAB")

    ChrTalk(    #117
        0xFE,
        (
            "If we can't fly out, I'd at least\x01",
            "like to get in contact my family...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7E")

    label("loc_2BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2C31")

    ChrTalk(    #118
        0xFE,
        (
            "The Royal Army's gone about\x01",
            "shutting down all the orbal-\x01",
            "ship platforms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Sounds like trouble's a-brewin'\x01",
            "to me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7E")

    label("loc_2C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2C3B")
    Jump("loc_2C7E")

    label("loc_2C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2C45")
    Jump("loc_2C7E")

    label("loc_2C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2C4F")
    Jump("loc_2C7E")

    label("loc_2C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2C59")
    Jump("loc_2C7E")

    label("loc_2C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C63")
    Jump("loc_2C7E")

    label("loc_2C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2C6D")
    Jump("loc_2C7E")

    label("loc_2C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2C77")
    Jump("loc_2C7E")

    label("loc_2C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2C7E")

    label("loc_2C7E")

    TalkEnd(0xFE)
    Return()

    # Function_10_2AE9 end

    def Function_11_2C82(): pass

    label("Function_11_2C82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2C8F")
    Jump("loc_3171")

    label("loc_2C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2C99")
    Jump("loc_3171")

    label("loc_2C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2CA3")
    Jump("loc_3171")

    label("loc_2CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2DAD")

    ChrTalk(    #120
        0xFE,
        (
            "We've heard rumors that the\x01",
            "remaining Royal Guardsmen\x01",
            "have gone underground...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "But even with our increased efforts,\x01",
            "we haven't been able to apprehend a\x01",
            "single one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "All I can imagine is that somebody,\x01",
            "somewhere, is sheltering them...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3171")

    label("loc_2DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2E53")

    ChrTalk(    #123
        0xFE,
        (
            "Man I'm tired... Isn't my shift\x01",
            "over yet?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "If things keep up like this, I won't\x01",
            "have gotten to see ANY of the Martial\x01",
            "Arts Competition this year!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3171")

    label("loc_2E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2F0C")

    ChrTalk(    #125
        0xFE,
        (
            "We're going to start stepping up\x01",
            "our city patrols, starting today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "We're going to smoke those Royal\x01",
            "Guardsmen refugees out of their\x01",
            "hidey-holes, one way or another!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3171")

    label("loc_2F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2F63")

    ChrTalk(    #127
        0xFE,
        (
            "So it was apparently the Royal\x01",
            "Guardsmen behind the terrorist\x01",
            "attack...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3171")

    label("loc_2F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2FAD")

    ChrTalk(    #128
        0xFE,
        "That ship...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Has someone come here from the\x01",
            "fortress?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3171")

    label("loc_2FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_305C")

    ChrTalk(    #130
        0xFE,
        (
            "It'd be a real problem if the\x01",
            "Royal Guardsmen were to hijack\x01",
            "one of our new-model vessels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "I'm sorry, but I'm not allowed\x01",
            "to let anyone near this airship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3171")

    label("loc_305C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_310B")

    ChrTalk(    #132
        0xFE,
        (
            "It'd be a real problem if the\x01",
            "Royal Guardsmen were to hijack\x01",
            "one of our new-model vessels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "I'm sorry, but I'm not allowed\x01",
            "to let anyone near this airship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3171")

    label("loc_310B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3171")

    ChrTalk(    #134
        0xFE,
        (
            "The Arseille has been impounded\x01",
            "by the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "No civilians are allowed near it.\x02",
    )

    CloseMessageWindow()

    label("loc_3171")

    TalkEnd(0xFE)
    Return()

    # Function_11_2C82 end

    def Function_12_3175(): pass

    label("Function_12_3175")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3182")
    Jump("loc_3206")

    label("loc_3182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_318C")
    Jump("loc_3206")

    label("loc_318C")


    ChrTalk(    #136
        0xFE,
        (
            "Sorry, but we can't just take you\x01",
            "on your word that you're bracers.\x01",
            "I hope you understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "Go. Move along, now.\x02",
    )

    CloseMessageWindow()

    label("loc_3206")

    TalkEnd(0xFE)
    Return()

    # Function_12_3175 end

    def Function_13_320A(): pass

    label("Function_13_320A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3217")
    Jump("loc_32AA")

    label("loc_3217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3221")
    Jump("loc_32AA")

    label("loc_3221")


    ChrTalk(    #138
        0xFE,
        (
            "No civilians should have any\x01",
            "business here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "I'll have to bring you in for\x01",
            "questioning if you insist on\x01",
            "loitering in this area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32AA")

    TalkEnd(0xFE)
    Return()

    # Function_13_320A end

    def Function_14_32AE(): pass

    label("Function_14_32AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_32BB")
    Jump("loc_3322")

    label("loc_32BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_32C5")
    Jump("loc_3322")

    label("loc_32C5")


    ChrTalk(    #140
        0xFE,
        (
            "The Grancel Landing Port is\x01",
            "closed for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "For the good of the people.\x02",
    )

    CloseMessageWindow()

    label("loc_3322")

    TalkEnd(0xFE)
    Return()

    # Function_14_32AE end

    def Function_15_3326(): pass

    label("Function_15_3326")

    TalkBegin(0xFE)

    ChrTalk(    #142
        0xFE,
        "What do you want, bracer?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_3326 end

    def Function_16_334C(): pass

    label("Function_16_334C")

    TalkBegin(0xFE)

    ChrTalk(    #143
        0xFE,
        "Who do you think you are?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "You might want to get home \x01",
            "and in bed before you have\x01",
            "an unfortunate accident...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_334C end

    def Function_17_33C9(): pass

    label("Function_17_33C9")

    TalkBegin(0xFE)

    ChrTalk(    #145
        0xFE,
        (
            "You all look suspicious to me.\x01",
            "Are you with the terrorists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Get out of here before you get\x01",
            "yourself hurt.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_33C9 end

    def Function_18_3444(): pass

    label("Function_18_3444")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3516")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_34B8")

    ChrTalk(    #147
        0xFE,
        (
            "Look, Brahm! Just look at \x01",
            "that bridge construction!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "Isn't it just TOO exciting?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3513")

    label("loc_34B8")


    ChrTalk(    #149
        0xFE,
        (
            "Look, Rudi! Just look at \x01",
            "that bridge construction!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "Isn't it just TOO exciting?!\x02",
    )

    CloseMessageWindow()

    label("loc_3513")

    Jump("loc_35B7")

    label("loc_3516")

    OP_A2(0x6)

    ChrTalk(    #151
        0xFE,
        "Man... Now THAT is form.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "I can't believe I'm here...right\x01",
            "up next to the Arseille...after\x01",
            "everything that happened!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "It's absolutely magical...\x02",
    )

    CloseMessageWindow()

    label("loc_35B7")

    TalkEnd(0xFE)
    Return()

    # Function_18_3444 end

    def Function_19_35BB(): pass

    label("Function_19_35BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_36B2")

    ChrTalk(    #154
        0xFE,
        (
            "I can't believe she said yes\x01",
            "when I invited her to go to the\x01",
            "Birthday Celebration with me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "But...we're in the capital, so\x01",
            "shouldn't we go somewhere OTHER\x01",
            "than the Landing Port?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "Someplace a bit more...romantic,\x01",
            "perhaps?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3774")

    label("loc_36B2")

    OP_A2(0x7)

    ChrTalk(    #157
        0xFE,
        (
            "I can't believe she said yes\x01",
            "when I invited her to go to the\x01",
            "Birthday Celebration with me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "Work's been hard lately, but\x01",
            "now...it's all worth it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "*sniffle* I'm so...so lucky...\x02",
    )

    CloseMessageWindow()

    label("loc_3774")

    TalkEnd(0xFE)
    Return()

    # Function_19_35BB end

    def Function_20_3778(): pass

    label("Function_20_3778")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_37F6")
    TalkBegin(0xFE)

    ChrTalk(    #160
        0xFE,
        (
            "Looks like we both have some\x01",
            "'fighting' to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "Best wishes to you during\x01",
            "the Birthday Celebration!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A93")

    label("loc_37F6")

    TalkBegin(0xFE)
    OP_A2(0x7)
    OP_28(0x31, 0x1, 0x200)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #162
        0xFE,
        "Hey, it's you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        "#501FHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #164
        0xFE,
        "It's me! Private Brahm!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "You took a letter delivery request\x01",
            "from me at Wolf Fort, remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        "#501FOh yeah, I remember now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x102,
        "#010FHow have you been?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "Eternally grateful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "Thanks to that letter, I managed\x01",
            "to patch things up with Faye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        "#001FWell, good for you, lover boy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "Good for me indeed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "Looks like you two are enjoying\x01",
            "some alone time yourselves...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#008FWh-What?!\x02\x03",

            "#503FY-Yeah, I...I guess we are, but...\x01",
            "you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Looks like we both have some\x01",
            "'fighting' to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "Best wishes to you, my friends!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        "#506FUh...yeah, same to you.\x02",
    )

    CloseMessageWindow()

    label("loc_3A93")

    TalkEnd(0xFE)
    Return()

    # Function_20_3778 end

    def Function_21_3A97(): pass

    label("Function_21_3A97")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #177
        (
            "\x07\x05Airship Arrivals & Departures \x01",
            "⇒ To Rolent \x01",
            "⇒ To Zeiss \x01",
            "⇒ To Calvard Republic\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #178
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

    # Function_21_3A97 end

    def Function_22_3B6C(): pass

    label("Function_22_3B6C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #179
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

    # Function_22_3B6C end

    SaveToFile()

Try(main)
