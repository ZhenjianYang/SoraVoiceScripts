from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3102   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Maintenance Chief Gustav',             # 9
        'Gerald',                               # 10
        'Factory Chief Murdock',                # 11
        'Dorothy',                              # 12
        'Antoine',                              # 13
        'Captain Amalthea',                     # 14
        'Rutherford',                           # 15
        'Dodge',                                # 16
        'Bartholomew',                          # 17
        'Ship',                                 # 18
        'Ship Shadow',                          # 19
        'Soldier',                              # 20
        'Soldier',                              # 21
        'Soldier',                              # 22
        'Zeiss - Factory Block',                # 23
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH02440 ._CH',             # 01
        'ED6_DT07/CH02620 ._CH',             # 02
        'ED6_DT07/CH02070 ._CH',             # 03
        'ED6_DT07/CH01700 ._CH',             # 04
        'ED6_DT07/CH02100 ._CH',             # 05
        'ED6_DT07/CH01020 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01640 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH02440P._CP',             # 01
        'ED6_DT07/CH02620P._CP',             # 02
        'ED6_DT07/CH02070P._CP',             # 03
        'ED6_DT07/CH01700P._CP',             # 04
        'ED6_DT07/CH02100P._CP',             # 05
        'ED6_DT07/CH01020P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01640P._CP',             # 09
    )

    DeclNpc(
        X                   = -37000,
        Z                   = -3800,
        Y                   = 145500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -20110,
        Z                   = 8000,
        Y                   = 121830,
        Direction           = 177,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Direction           = 180,
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
        Direction           = 180,
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
        X                   = -18770,
        Z                   = 8000,
        Y                   = 89560,
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
        X                   = -43700,
        Y                   = -4000,
        Z                   = 146000,
        Range               = -41600,
        Unknown_10          = 0xFFFFF830,
        Unknown_14          = 0x22A4C,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = -43200,
        Y                   = -5000,
        Z                   = 145000,
        Range               = -48600,
        Unknown_10          = 0xFFFFF830,
        Unknown_14          = 0x22B78,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = -15210,
        Y                   = 7000,
        Z                   = 100600,
        Range               = -22980,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x1938E,
        Unknown_18          = 0x0,
        Unknown_1C          = 26,
    )


    DeclActor(
        TriggerX            = -19980,
        TriggerZ            = 8000,
        TriggerY            = 119710,
        TriggerRange        = 400,
        ActorX              = -20110,
        ActorZ              = 9500,
        ActorY              = 121830,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41010,
        TriggerZ            = 8000,
        TriggerY            = 122500,
        TriggerRange        = 800,
        ActorX              = -41010,
        ActorZ              = 10200,
        ActorY              = 122500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38900,
        TriggerZ            = 8400,
        TriggerY            = 122040,
        TriggerRange        = 800,
        ActorX              = -38900,
        ActorZ              = 9900,
        ActorY              = 122040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3A6",          # 00, 0
        "Function_1_661",          # 01, 1
        "Function_2_872",          # 02, 2
        "Function_3_9EF",          # 03, 3
        "Function_4_A13",          # 04, 4
        "Function_5_A37",          # 05, 5
        "Function_6_A5B",          # 06, 6
        "Function_7_A7F",          # 07, 7
        "Function_8_12E2",         # 08, 8
        "Function_9_1AFB",         # 09, 9
        "Function_10_1B34",        # 0A, 10
        "Function_11_40D9",        # 0B, 11
        "Function_12_4FD6",        # 0C, 12
        "Function_13_535A",        # 0D, 13
        "Function_14_5442",        # 0E, 14
        "Function_15_5447",        # 0F, 15
        "Function_16_5E66",        # 10, 16
        "Function_17_689B",        # 11, 17
        "Function_18_6EDE",        # 12, 18
        "Function_19_6F5F",        # 13, 19
        "Function_20_82F3",        # 14, 20
        "Function_21_8316",        # 15, 21
        "Function_22_8339",        # 16, 22
        "Function_23_835C",        # 17, 23
        "Function_24_837F",        # 18, 24
        "Function_25_843A",        # 19, 25
        "Function_26_84C8",        # 1A, 26
    )


    def Function_0_3A6(): pass

    label("Function_0_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3BD")
    OP_A3(0x3FA)
    Event(0, 16)
    OP_B1("T3102_1")

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF")
    SetChrPos(0xA, -44860, -4000, 141600, 270)
    ClearChrFlags(0xA, 0x80)

    label("loc_3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_41C")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -40990, 8000, 129460, 12)
    OP_43(0xE, 0x0, 0x0, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44660, 8000, 129500, 5)
    Jump("loc_660")

    label("loc_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_459")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -40990, 8000, 129460, 12)
    OP_43(0xE, 0x0, 0x0, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44660, 8000, 129500, 5)
    Jump("loc_660")

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_479")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -40990, 8000, 122890, 180)
    Jump("loc_660")

    label("loc_479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4E2")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -47500, -4000, 151780, 261)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -47500, -4000, 152840, 261)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -40130, 8000, 125930, 237)
    OP_43(0xC, 0x0, 0x0, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_522")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -44530, -4000, 142000, 176)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44510, -4000, 140610, 21)
    SetChrFlags(0x10, 0x10)
    Jump("loc_660")

    label("loc_522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_55F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -58040, 4000, 125930, 187)
    OP_43(0x8, 0x0, 0x0, 0x6)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_569")
    Jump("loc_660")

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5A6")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -49800, 8000, 117400, 3)
    OP_43(0x8, 0x0, 0x0, 0x5)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_5A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_END)), "loc_5C6")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44440, -4000, 153380, 90)
    Jump("loc_660")

    label("loc_5C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_5E6")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_5E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_606")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_626")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_660")

    label("loc_626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_660")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -40130, 8000, 125930, 237)
    OP_43(0xC, 0x0, 0x0, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)

    label("loc_660")

    Return()

    # Function_0_3A6 end

    def Function_1_661(): pass

    label("Function_1_661")

    OP_16(0x2, 0xFA0, 0xFFFD6020, 0x4E20, 0x30053)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A3")
    OP_B1("T3102_3")
    OP_6F(0x0, 1001)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x3, 100)
    Jump("loc_871")

    label("loc_6A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70C")
    OP_B1("T3102_2")
    OP_6F(0x4, 1)
    OP_6F(0x3, 200)
    OP_71(0x6, 0x4)
    OP_6F(0x0, 1001)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -43100, -3800, 144030, 270)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x64, 0x0)
    Jump("loc_871")

    label("loc_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73C")
    OP_B1("T3102_2")
    OP_6F(0x0, 250)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x3, 100)
    Jump("loc_871")

    label("loc_73C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_767")
    OP_B1("T3102_2")
    OP_6F(0x0, 250)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x3, 100)
    Jump("loc_871")

    label("loc_767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_END)), "loc_7BB")
    OP_B1("T3102_2")
    OP_6F(0x4, 1)
    OP_6F(0x3, 200)
    OP_71(0x6, 0x4)
    OP_6F(0x0, 1001)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -42710, -3800, 144020, 270)
    Jump("loc_824")

    label("loc_7BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_803")
    OP_B1("T3102_2")
    OP_6F(0x4, 1)
    OP_6F(0x3, 200)
    OP_71(0x6, 0x4)
    OP_6F(0x0, 1001)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -36900, -3800, 140550, 90)
    Jump("loc_824")

    label("loc_803")

    OP_B1("T3102_2")
    OP_6F(0x0, 1001)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x3, 100)

    label("loc_824")

    Jump("loc_871")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_850")
    OP_B1("T3102_1")
    OP_6F(0x4, 1)
    OP_6F(0x3, 200)
    OP_6F(0x0, 1001)
    Jump("loc_871")

    label("loc_850")

    OP_B1("T3102_2")
    OP_6F(0x0, 1001)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x3, 100)

    label("loc_871")

    Return()

    # Function_1_661 end

    def Function_2_872(): pass

    label("Function_2_872")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_897")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_9D9")

    label("loc_897")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B0")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_9D9")

    label("loc_8B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C9")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_9D9")

    label("loc_8C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E2")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_9D9")

    label("loc_8E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FB")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_9D9")

    label("loc_8FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_914")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_9D9")

    label("loc_914")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92D")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_9D9")

    label("loc_92D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_946")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_9D9")

    label("loc_946")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95F")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_9D9")

    label("loc_95F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_978")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_9D9")

    label("loc_978")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_991")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_9D9")

    label("loc_991")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AA")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_9D9")

    label("loc_9AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C3")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_9D9")

    label("loc_9C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D9")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_9D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9EE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_9D9")

    label("loc_9EE")

    Return()

    # Function_2_872 end

    def Function_3_9EF(): pass

    label("Function_3_9EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A12")
    OP_8D(0xFE, -19390, 119560, -16690, 116060, 3000)
    Jump("Function_3_9EF")

    label("loc_A12")

    Return()

    # Function_3_9EF end

    def Function_4_A13(): pass

    label("Function_4_A13")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A36")
    OP_8D(0xFE, -35820, 123780, -43940, 129220, 3000)
    Jump("Function_4_A13")

    label("loc_A36")

    Return()

    # Function_4_A13 end

    def Function_5_A37(): pass

    label("Function_5_A37")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A5A")
    OP_8D(0xFE, -45240, 117320, -51970, 121500, 2000)
    Jump("Function_5_A37")

    label("loc_A5A")

    Return()

    # Function_5_A37 end

    def Function_6_A5B(): pass

    label("Function_6_A5B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7E")
    OP_8D(0xFE, -56420, 122640, -59470, 129340, 2000)
    Jump("Function_6_A5B")

    label("loc_A7E")

    Return()

    # Function_6_A5B end

    def Function_7_A7F(): pass

    label("Function_7_A7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_B02")

    ChrTalk(    #0
        0xFE,
        (
            "*sigh* What is this inspection\x01",
            "without any kind of notice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Those Royal Army guys have\x01",
            "no sense of protocol.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DE")

    label("loc_B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_B6E")

    ChrTalk(    #2
        0xFE,
        (
            "Well, the Cecilia will be\x01",
            "landing soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Better get started on all the\x01",
            "docking measures.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DE")

    label("loc_B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_C2E")

    ChrTalk(    #4
        0xFE,
        (
            "The factory ship's being\x01",
            "sent out of port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I know they're supposed to go\x01",
            "to Leiston, but flying out ahead\x01",
            "of schedule...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I wonder if something's happened\x01",
            "out there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DE")

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_C7E")

    ChrTalk(    #7
        0xFE,
        "Okay, we're ready for landing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "May as well check the cargo.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12DE")

    label("loc_C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_D69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_D00")

    ChrTalk(    #9
        0xFE,
        "Man, that Rehmann is so lucky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Since he's a pilot, he gets to\x01",
            "leave early any time he's got\x01",
            "a flight. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D66")

    label("loc_D00")

    OP_A2(0x5)

    ChrTalk(    #11
        0xFE,
        "So, off to Leiston tomorrow?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Seems there have been a lot\x01",
            "of flights there recently.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_D66")

    Jump("loc_12DE")

    label("loc_D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_E3E")

    ChrTalk(    #13
        0xFE,
        (
            "That whole thing at the central\x01",
            "factory got worked out, didn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "What? They haven't caught the\x01",
            "guys who did it yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "That's troubling. I hope their\x01",
            "next target won't be the factory\x01",
            "ship!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DE")

    label("loc_E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1087")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_F36")

    ChrTalk(    #16
        0xFE,
        (
            "Hmph. It's the duke's fault the\x01",
            "royal family's got such a bad\x01",
            "name now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I remember when the queen's\x01",
            "birthday celebration used to be\x01",
            "peaceful and enjoyable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "That pompous, tubby duke owes\x01",
            "me a quiet festival, damn it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1084")

    label("loc_F36")

    OP_A2(0x5)

    ChrTalk(    #19
        0xFE,
        (
            "Last vacation I went to those\x01",
            "waterfalls over in Air-Letten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Some duke from the royal family\x01",
            "was visiting there at the same time,\x01",
            "all incognito-like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "But he still made a gigantic fuss.\x01",
            "What a self-absorbed jerk. He\x01",
            "ruined my vacation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I don't think all of the royal\x01",
            "family are like him, of course,\x01",
            "but still...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1084")

    Jump("loc_12DE")

    label("loc_1087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B7")

    ChrTalk(    #23
        0xFE,
        "Well, time to head home!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1135")

    label("loc_10B7")


    ChrTalk(    #24
        0xFE,
        (
            "What do you think of her?  \x01",
            "Isn't she a beauty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "This is the crown jewel of\x01",
            "the central factory fleet,\x01",
            "the Leibnitz.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1135")

    Jump("loc_12DE")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_129A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_11C4")

    ChrTalk(    #26
        0xFE,
        (
            "I still haven't heard the reason\x01",
            "for all of the orbments stopping\x01",
            "cold yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "I hope it never happens again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1297")

    label("loc_11C4")

    OP_A2(0x5)

    ChrTalk(    #28
        0xFE,
        (
            "All the orbments stopped working\x01",
            "last night, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "It's such a good thing it didn't\x01",
            "happen during the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I don't want to think what\x01",
            "would've happened if there\x01",
            "had been any ships in the air.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1297")

    Jump("loc_12DE")

    label("loc_129A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12DE")

    ChrTalk(    #31
        0xFE,
        "Docking is a go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Time for final liftoff check.\x02",
    )

    CloseMessageWindow()

    label("loc_12DE")

    TalkEnd(0xFE)
    Return()

    # Function_7_A7F end

    def Function_8_12E2(): pass

    label("Function_8_12E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14ED")
    EventBegin(0x0)

    ChrTalk(    #33
        0x8,
        "#691FAre we ready to liftoff?\x02",
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
            "[Liftoff]\x01",      # 0
            "[Prepare]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_137B"),
        (1, "loc_14A4"),
        (SWITCH_DEFAULT, "loc_14EA"),
    )


    label("loc_137B")

    OP_4A(0xA, 255)
    OP_8C(0xA, 315, 400)

    ChrTalk(    #34
        0x8,
        (
            "#693FAll right! Let's load up!\x02\x03",

            "We're off to Leiston Fortress!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "#803FPlease...bring Professor Russell\x01",
            "back home safely.\x02\x03",

            "#800FAnd...take care of Tita.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_142C():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_142C)

    def lambda_143A():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_143A)

    def lambda_1448():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1448)
    TurnDirection(0x107, 0xA, 400)

    ChrTalk(    #36
        0x107,
        "#560FS-Sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#006FNo sweat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        "#010FLet us go then.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Call(0, 17)
    Jump("loc_14EA")

    label("loc_14A4")

    OP_A2(0x572)

    ChrTalk(    #39
        0x8,
        (
            "#691FGot'cha. Let me know when\x01",
            "you're ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    OP_4B(0x8, 255)
    EventEnd(0x1)
    Return()

    label("loc_14EA")

    Jump("loc_1AF7")

    label("loc_14ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1584")

    ChrTalk(    #40
        0xFE,
        (
            "#690FSorry to keep you waiting.\x02\x03",

            "We've got another work order \x01",
            "from Leiston Fortress. I'd like\x01",
            "to leave today.\x02\x03",

            "I hope nothing happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF7")

    label("loc_1584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_END)), "loc_166E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_15ED")

    ChrTalk(    #41
        0xFE,
        (
            "#690FWe were really fortunate not\x01",
            "to have any injuries in all that\x01",
            "mess yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_166B")

    label("loc_15ED")

    OP_A2(0x4)

    ChrTalk(    #42
        0xFE,
        (
            "#690FStill, I couldn't believe it.\x02\x03",

            "But we were really fortunate not\x01",
            "to have any injuries in all that\x01",
            "mess yesterday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_166B")

    Jump("loc_1AF7")

    label("loc_166E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_17FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_16D7")

    ChrTalk(    #43
        0xFE,
        (
            "#690FWe were really fortunate not\x01",
            "to have any injuries in all that\x01",
            "mess yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FC")

    label("loc_16D7")

    OP_A2(0x4)
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #44
        0xFE,
        (
            "#690FHey there, Tita.\x02\x03",

            "What a royal mess this is.\x01",
            "You hurt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x107,
        (
            "#063F...\x02\x03",

            "#064FHuh? N-No, sir!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0xFE,
        (
            "#692FSomething wrong? You spaced\x01",
            "out there for a second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x107,
        "#066FNo, no. I-I'm fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "#691FWell, as long as you didn't\x01",
            "get hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x107,
        "#063F...\x02",
    )

    CloseMessageWindow()

    label("loc_17FC")

    Jump("loc_1AF7")

    label("loc_17FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1A3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1831")

    ChrTalk(    #50
        0xFE,
        "#690FHey, Tita. Be careful!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A38")

    label("loc_1831")

    OP_A2(0x4)

    ChrTalk(    #51
        0xFE,
        (
            "#690FHey, Tita. Helping your grandpa\x01",
            "out again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x107,
        (
            "#060FYes, sir.\x01",
            "I've got to go to Elmo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "#692FElmo? Are you serious?\x02\x03",

            "Didn't you just get attacked by\x01",
            "monsters out there near the\x01",
            "Kaldia Tunnel?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x107,
        (
            "#061FHee hee, this time I have two\x01",
            "bracers for bodyguards.\x01",
            "I should be perfectly fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "#692FWell, you DID bring back the\x01",
            "combustion unit.\x02\x03",

            "#691FBracers, huh. At first I thought\x01",
            "you were just some loud-mouthed\x01",
            "little girl.\x02\x03",

            "I guess you won't have any\x01",
            "problems. Have a safe trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x107,
        "#560FThank you!\x02",
    )

    CloseMessageWindow()

    label("loc_1A38")

    Jump("loc_1AF7")

    label("loc_1A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_END)), "loc_1AF7")

    ChrTalk(    #57
        0x8,
        (
            "#691FWhat a funny coincidence.\x02\x03",

            "We just get the Combustion Engine\x01",
            "back from the army, and now the\x01",
            "professor's taking it...\x02\x03",

            "Well, it does just sit around\x01",
            "in storage otherwise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF7")

    TalkEnd(0xFE)
    Return()

    # Function_8_12E2 end

    def Function_9_1AFB(): pass

    label("Function_9_1AFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1B19")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #58
        0xFE,
        "Nya-o.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B30")

    label("loc_1B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1B30")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #59
        0xFE,
        "Nyao?\x02",
    )

    CloseMessageWindow()

    label("loc_1B30")

    TalkEnd(0xFE)
    Return()

    # Function_9_1AFB end

    def Function_10_1B34(): pass

    label("Function_10_1B34")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27E6")
    OP_A2(0x604)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -20510, 8000, 119230, 0)
    SetChrPos(0x102, -18980, 8000, 119430, 0)

    def lambda_1B75():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B75)

    def lambda_1B85():
        OP_6B(2750, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1B85)
    OP_6D(-20140, 8000, 120700, 2000)

    ChrTalk(    #60
        0x9,
        "Hey, it's you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "I told you before, I don't know\x01",
            "when the ship's leaving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "If you'd just wait at the\x01",
            "Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#506FUm, actually? There's been a\x01",
            "slight change in plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x102,
        (
            "#010FI apologize for the timing,\x01",
            "but can we still cancel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        "Sure, that's no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "As long as it's before your\x01",
            "flight arrives in port there's\x01",
            "no cancellation fee. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "We just need to get your\x01",
            "tickets back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#000FGreat. Here you go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #69
        "\x07\x00Returned \x07\x02Boarding Pass\x07\x00 x2.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x370, 2)
    Sleep(500)
    OP_22(0xE2, 0x0, 0x64)
    OP_20(0x3E8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x56)

    ChrTalk(    #70
        0x9,
        "Hey, that's a military patrol vessel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        "It's here early...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#004FWell! Gotta go, bye!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 600)

    def lambda_1E66():
        OP_8E(0xFE, 0xFFFFB12C, 0x1F40, 0x192A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E66)

    ChrTalk(    #73
        0x102,
        "#010FThank you for your help.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 600)

    def lambda_1EAB():
        OP_8E(0xFE, 0xFFFFB7F8, 0x1F40, 0x192A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1EAB)

    ChrTalk(    #74
        0x9,
        (
            "No worries. Come back and see\x01",
            "us again sometime!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6F(0x0, 1001)
    OP_A1(0x11, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x4, 0x20)
    SetChrPos(0x11, -34000, 17000, 180000, 0)
    SetChrFlags(0x11, 0x4)
    OP_A1(0x12, 0x5)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x12, -34000, -10000, 180000, 0)
    SetChrFlags(0x12, 0x4)
    OP_6F(0x3, 100)
    OP_B0(0x4, 0x1E)
    OP_6D(-34000, 17000, 170000, 0)
    OP_67(0, 26070, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(156000, 0)
    OP_6E(239, 0)
    StopSound(0x186A0, 0x3D090, 0x0)
    OP_6F(0x4, 470)
    OP_70(0x4, 0x24E)

    def lambda_1FBA():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x29810, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1FBA)

    def lambda_1FD5():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x29810, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1FD5)
    OP_22(0x79, 0x1, 0x28)
    Sleep(100)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x41)
    Sleep(100)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x79, 0x4B)
    Sleep(100)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x79, 0x55)
    Sleep(100)
    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x5F)
    Sleep(100)
    OP_24(0x79, 0x64)
    WaitChrThread(0x11, 0x1)
    OP_66(0x0)
    OP_6A(0x11)

    def lambda_2051():
        OP_8C(0xFE, 180, 5)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2051)

    def lambda_205F():
        OP_8C(0xFE, 180, 5)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_205F)

    def lambda_206D():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_206D)

    def lambda_2088():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2088)
    Sleep(200)

    def lambda_20A8():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_20A8)

    def lambda_20B6():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_20B6)

    def lambda_20C4():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_20C4)

    def lambda_20DF():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_20DF)
    Sleep(200)

    def lambda_20FF():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_20FF)

    def lambda_210D():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_210D)

    def lambda_211B():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_211B)

    def lambda_2136():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2136)
    Sleep(200)

    def lambda_2156():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2156)

    def lambda_2164():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2164)

    def lambda_2172():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2172)

    def lambda_218D():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_218D)
    Sleep(200)

    def lambda_21AD():
        OP_8C(0xFE, 180, 60)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_21AD)

    def lambda_21BB():
        OP_8C(0xFE, 180, 60)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_21BB)

    def lambda_21C9():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21C9)

    def lambda_21E4():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_21E4)
    Sleep(200)

    def lambda_2204():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2204)

    def lambda_221F():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_221F)
    Sleep(200)

    def lambda_223F():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_223F)

    def lambda_225A():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_225A)
    Sleep(200)

    def lambda_227A():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_227A)

    def lambda_2295():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2295)
    Sleep(200)

    def lambda_22B5():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_22B5)

    def lambda_22D0():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_22D0)
    Sleep(200)

    def lambda_22F0():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_22F0)

    def lambda_230B():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_230B)
    Sleep(200)

    def lambda_232B():
        OP_8F(0xFE, 0xFFFF7B30, 0x4268, 0x26548, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_232B)

    def lambda_2346():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD8F0, 0x26548, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2346)
    Sleep(800)

    def lambda_2366():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2366)

    def lambda_2374():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2374)
    Sleep(100)

    def lambda_2387():
        OP_8C(0xFE, 180, 40)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2387)

    def lambda_2395():
        OP_8C(0xFE, 180, 40)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2395)
    Sleep(100)

    def lambda_23A8():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_23A8)

    def lambda_23B6():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_23B6)
    Sleep(100)

    def lambda_23C9():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_23C9)

    def lambda_23D7():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_23D7)
    Sleep(100)

    def lambda_23EA():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_23EA)

    def lambda_23F8():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_23F8)
    OP_22(0xCC, 0x0, 0x64)
    OP_6F(0x4, 590)
    OP_70(0x4, 0x2B2)
    WaitChrThread(0x11, 0x1)

    def lambda_241E():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_241E)

    def lambda_2439():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x29A, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2439)
    Sleep(100)

    def lambda_2459():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0x618, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2459)

    def lambda_2474():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2474)
    Sleep(100)
    OP_6A(0x0)
    ClearMapFlags(0x1)

    def lambda_249C():
        OP_67(-48240, 40960, 201970, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_249C)

    def lambda_24B4():
        OP_6E(262, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24B4)

    def lambda_24C4():
        OP_6D(-32150, -6000, 142270, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_24C4)

    def lambda_24DC():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0x79E, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_24DC)

    def lambda_24F7():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_24F7)
    Sleep(100)

    def lambda_2517():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0xA28, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2517)

    def lambda_2532():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x535, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2532)
    Sleep(100)

    def lambda_2552():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0xF3C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2552)

    def lambda_256D():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_256D)
    Sleep(100)

    def lambda_258D():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD508, 0x23280, 0x1450, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_258D)

    def lambda_25A8():
        OP_8F(0xFE, 0xFFFF7CAC, 0xFFFFD8F0, 0x23280, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_25A8)
    Sleep(100)
    WaitChrThread(0x11, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(600)
    OP_22(0x6D, 0x0, 0x64)
    OP_6F(0x4, 1)
    OP_70(0x4, 0xF)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_66(0x1)
    OP_44(0x101, 0xFF)
    OP_6D(-44580, -3800, 144110, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(3330, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x11, -33620, -11600, 144000, 180)
    SetChrPos(0x12, -33620, -10000, 144000, 180)
    OP_51(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x15, 0x1, 0x0, 0x17)
    OP_43(0x14, 0x1, 0x0, 0x16)
    OP_43(0x13, 0x1, 0x0, 0x15)
    OP_43(0xD, 0x1, 0x0, 0x14)
    FadeToBright(1000, 0)

    def lambda_26DD():
        OP_6D(-34960, -3480, 144150, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26DD)

    def lambda_26F5():
        OP_6B(3330, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26F5)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC4)
    Sleep(500)
    OP_22(0x78, 0x0, 0x64)
    Sleep(3000)
    Sleep(1000)

    ChrTalk(    #75
        0xD,
        (
            "#180FWell, things are certainly\x01",
            "bustling around here.\x02\x03",

            "First, I believe I shall go see\x01",
            "the factory chief.\x02\x03",

            "#188FI have to admire the colonel\x01",
            "for planning all of this.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_40D5")

    label("loc_27E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_END)), "loc_286C")

    ChrTalk(    #76
        0x9,
        (
            "The Cecilia should be coming\x01",
            "into port soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "Please have your tickets ready for\x01",
            "display when your flight arrives.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D5")

    label("loc_286C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A59")
    OP_A2(0x602)
    OP_28(0x54, 0x1, 0x2)
    EventBegin(0x0)
    OP_69(0x9, 0x3E8)

    ChrTalk(    #78
        0x9,
        "Hello there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "I heard from Kilika. Shall we\x01",
            "get you all squared away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#006FThat'd be great, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "Please fill out these forms with\x01",
            "your names and addresses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        "#010FThank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #83
        "\x07\x05Estelle filled out the boarding papers.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #84
        0x9,
        "Okay, here are your tickets.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x9,
        (
            "Make sure you show these when\x01",
            "you're boarding.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #86
        "\x07\x00Received \x07\x02Boarding Pass\x07\x00 x2.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x370, 2)
    EventEnd(0x1)
    Jump("loc_40D5")

    label("loc_2A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39D9")
    EventBegin(0x0)
    OP_A2(0x517)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -19410, 8000, 119800, 0)
    SetChrPos(0x102, -20670, 8000, 119780, 0)

    def lambda_2A99():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A99)

    def lambda_2AA9():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2AA9)
    OP_69(0x9, 0x7D0)

    ChrTalk(    #87
        0x9,
        "#2PHi, need a flight?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "#2PThe westbound airship just\x01",
            "departed a few moments ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#006FNo, thank you. We don't need\x01",
            "an airship right now.\x02\x03",

            "Actually, we need to talk to...\x01",
            "Gustav, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        "#2PYou mean the maintenance chief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        "#2PHe's not here at the moment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#004FWhat do you mean, 'not here'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        (
            "#2PHe went to Leiston Fortress two\x01",
            "or three days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "#2PSome kind of repair emergency\x01",
            "on a military patrol ship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#505FLeiston Fortress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        (
            "#010F#1PAs in, the largest base in the Royal\x01",
            "Army, out by Lake Valleria?\x02\x03",

            "Up in the north part of Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#007FWonderful. He won't be coming\x01",
            "back from there any time soon. \x02\x03",

            "So what do we do about the\x01",
            "professor's request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "#2PI don't know anything about that,\x01",
            "but the chief is actually on his\x01",
            "way back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        "#2PHe just sent word to us...\x02",
    )

    CloseMessageWindow()
    OP_22(0xE2, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #100
        0x101,
        "#004FOh, hey, airship!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #101
        0x9,
        "Speak of the devil...\x02",
    )

    CloseMessageWindow()
    OP_A1(0x11, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x4, 0x20)
    SetChrPos(0x11, -34000, 9000, 177000, 180)
    SetChrFlags(0x11, 0x4)
    OP_A1(0x12, 0x5)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x12, -34000, -11150, 177000, 180)
    SetChrFlags(0x12, 0x4)
    OP_66(0x0)

    def lambda_2EC2():
        OP_67(2310, 43070, 99410, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EC2)

    def lambda_2EDA():
        OP_6D(-32150, 15520, 142270, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EDA)

    def lambda_2EF2():
        OP_6B(900, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2EF2)
    Sleep(2000)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 161)
    OP_70(0x4, 0x104)

    def lambda_2F1A():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F1A)

    def lambda_2F35():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x26548, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2F35)
    OP_22(0x79, 0x1, 0x28)
    Sleep(100)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x41)
    Sleep(100)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x79, 0x4B)
    Sleep(100)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x79, 0x55)
    Sleep(100)
    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x5F)
    Sleep(100)
    OP_24(0x79, 0x64)
    Sleep(100)
    Sleep(2000)
    Sleep(100)

    def lambda_2FB5():
        OP_67(2310, 60560, 99410, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FB5)

    def lambda_2FCD():
        OP_8C(0xFE, 0, 5)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2FCD)

    def lambda_2FDB():
        OP_8C(0xFE, 0, 5)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2FDB)
    Sleep(100)

    def lambda_2FEE():
        OP_8C(0xFE, 0, 8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2FEE)

    def lambda_2FFC():
        OP_8C(0xFE, 0, 8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2FFC)
    Sleep(100)

    def lambda_300F():
        OP_8C(0xFE, 0, 10)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_300F)

    def lambda_301D():
        OP_8C(0xFE, 0, 10)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_301D)
    Sleep(100)

    def lambda_3030():
        OP_8C(0xFE, 0, 13)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3030)

    def lambda_303E():
        OP_8C(0xFE, 0, 13)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_303E)
    Sleep(100)

    def lambda_3051():
        OP_8C(0xFE, 0, 15)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3051)

    def lambda_305F():
        OP_8C(0xFE, 0, 15)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_305F)
    Sleep(100)

    def lambda_3072():
        OP_8C(0xFE, 0, 18)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3072)

    def lambda_3080():
        OP_8C(0xFE, 0, 18)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3080)

    def lambda_308E():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_308E)
    Sleep(85)

    def lambda_30AE():
        OP_8C(0xFE, 0, 20)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_30AE)

    def lambda_30BC():
        OP_8C(0xFE, 0, 20)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_30BC)
    Sleep(85)

    def lambda_30CF():
        OP_8C(0xFE, 0, 23)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_30CF)

    def lambda_30DD():
        OP_8C(0xFE, 0, 23)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_30DD)

    def lambda_30EB():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_30EB)
    Sleep(85)

    def lambda_310B():
        OP_8C(0xFE, 0, 25)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_310B)

    def lambda_3119():
        OP_8C(0xFE, 0, 25)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3119)
    Sleep(85)

    def lambda_312C():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_312C)

    def lambda_3147():
        OP_8C(0xFE, 0, 28)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3147)

    def lambda_3155():
        OP_8C(0xFE, 0, 28)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3155)
    Sleep(85)

    def lambda_3168():
        OP_8C(0xFE, 0, 30)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3168)

    def lambda_3176():
        OP_8C(0xFE, 0, 30)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3176)
    Sleep(85)

    def lambda_3189():
        OP_8C(0xFE, 0, 33)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3189)

    def lambda_3197():
        OP_8C(0xFE, 0, 33)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3197)

    def lambda_31A5():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_31A5)
    Sleep(85)
    Sleep(85)

    def lambda_31CA():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_31CA)
    Sleep(170)

    def lambda_31EA():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_31EA)
    Sleep(170)

    def lambda_320A():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_320A)
    Sleep(170)

    def lambda_322A():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_322A)
    Sleep(170)

    def lambda_324A():
        OP_8F(0xFE, 0xFFFF7B30, 0x2328, 0x26548, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_324A)
    Sleep(170)
    WaitChrThread(0x11, 0x1)
    Sleep(1900)
    Sleep(200)

    def lambda_3279():
        OP_8C(0xFE, 0, 25)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3279)

    def lambda_3287():
        OP_8C(0xFE, 0, 25)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3287)
    Sleep(200)

    def lambda_329A():
        OP_8C(0xFE, 0, 20)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_329A)

    def lambda_32A8():
        OP_8C(0xFE, 0, 20)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_32A8)
    Sleep(200)

    def lambda_32BB():
        OP_8C(0xFE, 0, 15)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_32BB)

    def lambda_32C9():
        OP_8C(0xFE, 0, 15)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_32C9)
    Sleep(200)

    def lambda_32DC():
        OP_8C(0xFE, 0, 10)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_32DC)

    def lambda_32EA():
        OP_8C(0xFE, 0, 10)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_32EA)
    Sleep(200)

    def lambda_32FD():
        OP_8C(0xFE, 0, 7)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_32FD)

    def lambda_330B():
        OP_8C(0xFE, 0, 7)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_330B)
    WaitChrThread(0x11, 0x2)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 261)
    OP_70(0x4, 0x19A)

    def lambda_3331():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3331)

    def lambda_334C():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_334C)
    Sleep(100)

    def lambda_336C():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_336C)
    Sleep(100)

    def lambda_338C():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_338C)
    Sleep(100)

    def lambda_33AC():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_33AC)

    def lambda_33C7():
        OP_6D(-32150, 3000, 135270, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33C7)
    Sleep(100)

    def lambda_33E4():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_33E4)
    Sleep(100)

    def lambda_3404():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3404)
    Sleep(100)

    def lambda_3424():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3424)
    Sleep(100)

    def lambda_3444():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3444)
    Sleep(100)

    def lambda_3464():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3464)
    Sleep(100)

    def lambda_3484():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3484)
    Sleep(100)

    def lambda_34A4():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_34A4)
    Sleep(100)

    def lambda_34C4():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_34C4)
    Sleep(4500)
    Sleep(100)

    def lambda_34E9():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_34E9)
    Sleep(100)

    def lambda_3509():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3509)
    Sleep(100)

    def lambda_3529():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3529)
    Sleep(100)

    def lambda_3549():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3549)
    Sleep(100)

    def lambda_3569():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3569)
    Sleep(100)

    def lambda_3589():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3589)
    Sleep(100)

    def lambda_35A9():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_35A9)
    Sleep(100)

    def lambda_35C9():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_35C9)
    Sleep(100)

    def lambda_35E9():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_35E9)
    Sleep(100)

    def lambda_3609():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3609)
    OP_44(0x11, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x11, -34000, -11150, 148000, 0)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x1)
    Sleep(1100)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC8)
    Sleep(2500)
    OP_44(0x101, 0x1)
    Fade(1000)
    OP_44(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -36900, -3800, 140550, 90)
    OP_66(0x1)
    SetChrPos(0x101, -24600, 8000, 121410, 0)
    SetChrPos(0x102, -23560, 8000, 121480, 0)
    TurnDirection(0x9, 0x101, 0)
    OP_44(0x101, 0xFF)
    OP_6D(-23460, 8000, 121550, 0)
    OP_67(0, 9450, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_71(0x6, 0x4)
    OP_0D()

    ChrTalk(    #102
        0x101,
        (
            "#004FAn orange airship...\x02\x03",

            "Hold the phone. Since when\x01",
            "are public airships orange?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        (
            "#010FNo, that doesn't look like a\x01",
            "regular public airship.\x02\x03",

            "The shape is wrong and it's\x01",
            "got work arms all over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#505FNow that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "#2PThat's a central factory vessel,\x01",
            "the Leibnitz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x9,
        (
            "#2PIt's the same model as the\x01",
            "public transports, but it's had\x01",
            "several modifications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "#2PIt's used for large scale\x01",
            "maintenance and transport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#001FHuh! A flying factory...\x02\x03",

            "#006FThen, the maintenance chief is\x01",
            "on that airship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        "#2PThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x9,
        (
            "#2PNow's your chance. You need to\x01",
            "talk with him, no?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #111
        0x101,
        "#006FWe do. Thanks a lot.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #112
        0x102,
        "#010FYes, thank you.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_40D5")

    label("loc_39D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3A49")

    ChrTalk(    #113
        0x9,
        (
            "What is it? Your papers are\x01",
            "already finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "Just show your tickets when\x01",
            "you get on-board.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D5")

    label("loc_3A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3AC8")

    ChrTalk(    #115
        0x9,
        "Hey. Wow, you guys look busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "We've just been ordered to get\x01",
            "our factory ship in the air. It's\x01",
            "a madhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D5")

    label("loc_3AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3B11")

    ChrTalk(    #117
        0x9,
        "The Cecilia is on schedule...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x9,
        "Time to read the news!\x02",
    )

    CloseMessageWindow()
    Jump("loc_40D5")

    label("loc_3B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3CC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3BD8")

    ChrTalk(    #119
        0x9,
        (
            "Did you see the front page of\x01",
            "the Liberl News?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        (
            "The pictures on their front \x01",
            "page have gotten nicer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x9,
        (
            "I'm looking forward to seeing\x01",
            "what they do with the next \x01",
            "edition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CC0")

    label("loc_3BD8")

    OP_A2(0x0)

    ChrTalk(    #122
        0x9,
        (
            "All that mess at the central\x01",
            "factory really made some ink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x9,
        (
            "I can't believe there are people\x01",
            "who have the guts to attack\x01",
            "the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "At this rate, the entire city\x01",
            "of Zeiss is going to be on\x01",
            "the front page.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CC0")

    Jump("loc_40D5")

    label("loc_3CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3DA4")

    ChrTalk(    #125
        0x9,
        (
            "What, you already read it?\x01",
            "The Liberl News' latest issue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x9,
        (
            "The mayor of Ruan got arrested.\x01",
            "Turns out he's a total crook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x9,
        (
            "And between sky bandits and\x01",
            "this Dalmore person...what is\x01",
            "this world coming to?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D5")

    label("loc_3DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_3EC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E1B")

    ChrTalk(    #128
        0x9,
        (
            "The westbound airship just \x01",
            "departed a few moments ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x9,
        "I hope things go smoothly today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBE")

    label("loc_3E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EA0")

    ChrTalk(    #130
        0x9,
        (
            "Yeah, the maintenance chief should\x01",
            "be on-board the Leibnitz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x9,
        (
            "Didn't you need to talk with\x01",
            "him or something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EBE")

    label("loc_3EA0")


    ChrTalk(    #132
        0x9,
        "So, did you find Gustav?\x02",
    )

    CloseMessageWindow()

    label("loc_3EBE")

    Jump("loc_40D5")

    label("loc_3EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_4024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F53")

    ChrTalk(    #133
        0x9,
        (
            "Wasn't that whole sky bandit\x01",
            "thing in Bose settled by\x01",
            "bracers, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        (
            "How lucky we are to have the\x01",
            "Royal Army on duty...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4021")

    label("loc_3F53")

    OP_A2(0x0)

    ChrTalk(    #135
        0x9,
        (
            "I read about it in the Liberl\x01",
            "News, but that sky bandit\x01",
            "thing sure was crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x9,
        (
            "It's a nightmare for us up here\x01",
            "if the public flights get stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x9,
        (
            "We've got to deal with all\x01",
            "the passengers!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4021")

    Jump("loc_40D5")

    label("loc_4024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40D5")

    ChrTalk(    #138
        0x9,
        (
            "The airliner 'Cecilia' is currently\x01",
            "in port, having just arrived from\x01",
            "the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        (
            "All passengers en route to the\x01",
            "Grancel region, please proceed\x01",
            "to the gates.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40D5")

    TalkEnd(0x9)
    Return()

    # Function_10_1B34 end

    def Function_11_40D9(): pass

    label("Function_11_40D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_417D")
    TalkBegin(0xA)

    ChrTalk(    #140
        0xA,
        (
            "#800FThanks to these passengers, \x01",
            "you won't be able to equip\x01",
            "combat orbments in the ship.\x02\x03",

            "You'd do better getting it done\x01",
            "in town first.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Jump("loc_4FD5")

    label("loc_417D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E7D")
    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -46160, -4000, 141480, 90)
    SetChrPos(0x106, -44780, -4000, 140260, 0)
    SetChrPos(0x107, -45700, -4000, 140390, 45)
    SetChrPos(0x102, -45780, -4000, 142250, 135)
    TurnDirection(0xA, 0x107, 0)

    def lambda_41E9():
        OP_6C(45000, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41E9)
    OP_6D(-45150, -4000, 141460, 0)
    OP_6B(3000, 0)
    OP_0D()

    ChrTalk(    #141
        0xA,
        (
            "#800FI've been waiting for you.\x01",
            "Is everybody ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x106,
        "#051FYeah, we can go any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x107,
        "#560FIs the Leibnitz ready, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xA,
        (
            "#801FYeah, you were lucky that\x01",
            "last-minute military order\x01",
            "came through like that.\x02\x03",

            "We were just about to head\x01",
            "out to Leiston Fortress.\x02\x03",

            "We can take off any time.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(200)
    OP_8C(0x101, 0, 400)
    Sleep(200)
    TurnDirection(0x101, 0xA, 400)
    Sleep(500)

    ChrTalk(    #145
        0x101,
        (
            "#505FAny time?\x02\x03",

            "Won't it be hard to leave without,\x01",
            "you know, the ship?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 315, 400)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0x102, 0xFFFF467E, 0xFFFFF060, 0x230F0, 0x7D0, 0x0)

    ChrTalk(    #146
        0x102,
        "#010FEstelle, look down.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    def lambda_440F():

        label("loc_440F")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_440F")

    QueueWorkItem2(0xA, 2, lambda_440F)

    def lambda_4420():

        label("loc_4420")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4420")

    QueueWorkItem2(0x107, 2, lambda_4420)

    def lambda_4431():

        label("loc_4431")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4431")

    QueueWorkItem2(0x106, 2, lambda_4431)

    def lambda_4442():
        OP_6D(-48810, -4000, 144860, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4442)

    def lambda_445A():
        OP_6C(314000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_445A)

    def lambda_446A():
        OP_6B(3500, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_446A)
    Sleep(3000)

    def lambda_447F():
        OP_8E(0x101, 0xFFFF4688, 0xFFFFF060, 0x22CE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_447F)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #147
        0x101,
        (
            "#501F#1P...Oh.\x02\x03",

            "Do we have to, um, jump?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x107,
        "#061F#1P*giggle* No, we don't.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #149
        0x101,
        "#004F#1PWha-...\x02",
    )

    CloseMessageWindow()
    OP_22(0xA7, 0x1, 0x55)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 315, 400)

    ChrTalk(    #150
        0x101,
        "#004F#1PWhat the...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        (
            "#014F#2PWhat's happening to the\x01",
            "flight deck?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x106,
        (
            "#051F#2PWhat, didn't you know?\x02\x03",

            "This place's got enough secrets\x01",
            "built into it to blow your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#509F#1PTo be honest, Agate...\x02",
    )

    CloseMessageWindow()
    OP_24(0xA7, 0x64)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 250)
    OP_70(0x0, 0x258)

    def lambda_4623():
        OP_6C(339000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4623)
    OP_6D(-55390, -4000, 147110, 3000)
    StopSound(0xC350, 0x3D090, 0xFA0)
    Sleep(100)
    OP_22(0x9A, 0x0, 0x64)

    def lambda_465B():
        OP_6B(2200, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_465B)
    OP_67(0, 21600, -10000, 3500)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0xBB8, 0x64)
    Sleep(500)

    def lambda_4697():
        OP_6B(3500, 6200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4697)

    def lambda_46A7():
        OP_6C(27000, 6100)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46A7)
    OP_6D(-36640, -4000, 148800, 6100)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0xBB8, 0x64)
    Sleep(100)

    def lambda_46E3():

        label("loc_46E3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_46E3")

    QueueWorkItem2(0x102, 0, lambda_46E3)

    def lambda_46F4():

        label("loc_46F4")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_46F4")

    QueueWorkItem2(0x101, 0, lambda_46F4)

    def lambda_4705():
        OP_8E(0xFE, 0xFFFF4B60, 0xFFFFF060, 0x226C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4705)

    def lambda_4720():
        OP_8E(0xFE, 0xFFFF4B38, 0xFFFFF060, 0x22B28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4720)

    def lambda_473B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_473B)

    def lambda_4749():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_4749)

    def lambda_4757():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_4757)

    def lambda_4765():
        OP_6B(5500, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4765)

    def lambda_4775():
        OP_67(0, 4000, -10000, 11800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4775)
    OP_6C(90000, 9800)
    OP_73(0x0)
    OP_44(0x101, 0x1)
    OP_23(0xA7)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(1000)
    Fade(1000)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x64, 0x0)
    OP_71(0x6, 0x4)
    OP_A1(0x11, 0x4)
    OP_72(0x4, 0x4)
    OP_6F(0x4, 60)
    SetChrPos(0x11, -34000, -11150, 148000, 0)
    SetChrFlags(0x11, 0x4)
    OP_6B(3500, 0)
    OP_67(0, 11000, -10000, 0)
    StopSound(0xC350, 0x1FBD0, 0x0)
    OP_6D(-45210, -4000, 142090, 0)
    OP_6F(0x0, 1001)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_0D()

    ChrTalk(    #154
        0x101,
        (
            "#509FI don't know how much more\x01",
            "mind I have left to blow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x102,
        (
            "#019FYou probably have more left\x01",
            "than I do, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xA,
        "#803FAnd all of this? It's all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#007FI know. It's all Professor Russell's\x01",
            "handiwork, right?\x02\x03",

            "#008FTita, your grandfather is\x01",
            "something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x107,
        "#067F#2PHehe, I couldn't agree more.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -36460, -4000, 144380, 270)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x1)
    Sleep(1100)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC8)
    OP_73(0x3)

    ChrTalk(    #159
        0x8,
        "#6PThanks for waiting, guys!\x02",
    )

    CloseMessageWindow()
    OP_6D(-40270, -4000, 143040, 1000)

    ChrTalk(    #160
        0x107,
        "#560FS-Sir!\x02",
    )

    CloseMessageWindow()

    def lambda_4A18():
        OP_8E(0xFE, 0xFFFF57A4, 0xFFFFF128, 0x2329E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4A18)

    def lambda_4A33():

        label("loc_4A33")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4A33")

    QueueWorkItem2(0xA, 2, lambda_4A33)

    def lambda_4A44():
        OP_6D(-44110, -3800, 143890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A44)
    Sleep(100)

    def lambda_4A61():
        OP_8E(0xFE, 0xFFFF4C0A, 0xFFFFF060, 0x2385C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4A61)
    Sleep(100)

    def lambda_4A81():
        OP_8E(0xFE, 0xFFFF4A8E, 0xFFFFF060, 0x2341A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4A81)
    Sleep(100)

    def lambda_4AA1():
        OP_8E(0xFE, 0xFFFF4AFC, 0xFFFFF060, 0x23082, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_4AA1)
    Sleep(100)

    def lambda_4AC1():
        OP_8E(0xFE, 0xFFFF4B56, 0xFFFFF060, 0x22CFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_4AC1)
    WaitChrThread(0x102, 0x3)

    def lambda_4AE1():

        label("loc_4AE1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4AE1")

    QueueWorkItem2(0x102, 2, lambda_4AE1)
    WaitChrThread(0x101, 0x3)

    def lambda_4AF7():

        label("loc_4AF7")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4AF7")

    QueueWorkItem2(0x101, 2, lambda_4AF7)
    WaitChrThread(0x107, 0x3)

    def lambda_4B0D():

        label("loc_4B0D")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4B0D")

    QueueWorkItem2(0x107, 2, lambda_4B0D)
    WaitChrThread(0x106, 0x3)

    def lambda_4B23():

        label("loc_4B23")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4B23")

    QueueWorkItem2(0x106, 2, lambda_4B23)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #161
        0x8,
        (
            "#690FHowdy, Tita. I already heard\x01",
            "everything from Murdock. \x02\x03",

            "Hard to believe what happened\x01",
            "to the professor.\x02\x03",

            "#691FGuess it's up to us to help\x01",
            "him out of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x107,
        "#061FTh-Thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x106,
        "#051FYeah, we owe you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        (
            "#691FNot at all. I'm the one who\x01",
            "owes Professor Russell.\x02\x03",

            "Okie dokie. We're ready.\x02\x03",

            "Are we ready to liftoff?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0xA, 0xFF)
    OP_8C(0xA, 315, 400)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Liftoff]\x01",      # 0
            "[Prepare]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4CFC"),
        (1, "loc_4E30"),
        (SWITCH_DEFAULT, "loc_4E7A"),
    )


    label("loc_4CFC")

    OP_A2(0x561)
    OP_28(0x43, 0x1, 0x400)
    OP_28(0x44, 0x4, 0x2)
    OP_28(0x44, 0x4, 0x4)

    ChrTalk(    #165
        0x8,
        (
            "#693FAll right! Let's load up!\x02\x03",

            "We're off to Leiston Fortress!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xA,
        (
            "#803F#2PPlease...bring Professor Russell\x01",
            "back home safely.\x02\x03",

            "#800FAnd...take care of Tita.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4DB8():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DB8)

    def lambda_4DC6():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DC6)

    def lambda_4DD4():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4DD4)
    TurnDirection(0x107, 0xA, 400)

    ChrTalk(    #167
        0x107,
        "#560FS-Sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        "#006FNo sweat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x102,
        "#010FLet's go, then.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Call(0, 17)
    Jump("loc_4E7A")

    label("loc_4E30")

    OP_A2(0x572)

    ChrTalk(    #170
        0x8,
        (
            "#691FGot'cha. Let me know when\x01",
            "you're ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    OP_4B(0x8, 255)
    OP_43(0xA, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    label("loc_4E7A")

    Jump("loc_4FD5")

    label("loc_4E7D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4EFA")

    ChrTalk(    #171
        0xA,
        (
            "#800FGustav just finished all our\x01",
            "takeoff preparations.\x02\x03",

            "When you're ready to leave,\x01",
            "come back and see me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FD2")

    label("loc_4EFA")

    OP_A2(0x3)

    ChrTalk(    #172
        0xA,
        "#800FHi. Are you ready yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x102,
        (
            "#010FWe still need a little more\x01",
            "time to finish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xA,
        (
            "#800FOkay well, Gustav just finished\x01",
            "all of our takeoff preparations.\x02\x03",

            "When you're ready to leave,\x01",
            "come back and see me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD2")

    TalkEnd(0xA)

    label("loc_4FD5")

    Return()

    # Function_11_40D9 end

    def Function_12_4FD6(): pass

    label("Function_12_4FD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_50B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_503E")

    ChrTalk(    #175
        0xFE,
        (
            "Are all of the airships\x01",
            "running late?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "I might as well come back\x01",
            "later on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50B2")

    label("loc_503E")

    OP_A2(0x1)

    ChrTalk(    #177
        0xFE,
        (
            "Looks like all the airships are\x01",
            "running late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "Those military inspections sure\x01",
            "are slowing things down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50B2")

    Jump("loc_5356")

    label("loc_50B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_51B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_50EE")

    ChrTalk(    #179
        0xFE,
        "Or is it that I'm just here early?\x02",
    )

    CloseMessageWindow()
    Jump("loc_51B6")

    label("loc_50EE")

    OP_A2(0x1)

    ChrTalk(    #180
        0xFE,
        (
            "Hi there! Are you all off to the\x01",
            "capital, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "I was just on my way to work\x01",
            "at the airship company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "If I finish fast enough, I was\x01",
            "thinking I'd go to the Royal\x01",
            "Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51B6")

    Jump("loc_5356")

    label("loc_51B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_5356")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5253")

    ChrTalk(    #183
        0xFE,
        (
            "Airship engineering has\x01",
            "really advanced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "I imagine it won't be long before\x01",
            "we've got ships going out to even\x01",
            "Dodge's hometown.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5356")

    label("loc_5253")

    OP_A2(0x1)

    ChrTalk(    #185
        0xFE,
        (
            "This morning I met a Republican\x01",
            "orbment merchant named Dodge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "He asked to see the landing pad,\x01",
            "and now I've been roped into\x01",
            "showing him around.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 270, 400)

    ChrTalk(    #187
        0xFE,
        (
            "Over there, Dodge, is the port\x01",
            "for raw materials and the \x01",
            "construction bay's just down...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5356")

    TalkEnd(0xFE)
    Return()

    # Function_12_4FD6 end

    def Function_13_535A(): pass

    label("Function_13_535A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_543E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_53E6")

    ChrTalk(    #188
        0xFE,
        (
            "One day I'd like to deal in\x01",
            "the airship business...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "But my hometown would need\x01",
            "to build a landing port first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_543E")

    label("loc_53E6")

    OP_A2(0x2)

    ChrTalk(    #190
        0xFE,
        (
            "I can't think of the words to\x01",
            "describe this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "It's just...incredible.\x02",
    )

    CloseMessageWindow()

    label("loc_543E")

    TalkEnd(0xFE)
    Return()

    # Function_13_535A end

    def Function_14_5442(): pass

    label("Function_14_5442")

    Call(0, 10)
    Return()

    # Function_14_5442 end

    def Function_15_5447(): pass

    label("Function_15_5447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E65")
    OP_A2(0x518)
    OP_28(0x3F, 0x1, 0x800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3F, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_546D")
    OP_28(0x3F, 0x1, 0x2000)

    label("loc_546D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x0, 400)

    NpcTalk(    #192
        0x8,
        "Old Technician",
        "#690FHmm...? What do you want?\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x0, -44000, -3800, 144340, 135)
    SetChrPos(0x1, -44420, -3800, 143430, 90)
    OP_6D(-40020, -3800, 143530, 0)
    OP_67(0, 6510, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(124000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #193
        0x101,
        "#004F#2PUm...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #194
        0x8,
        "Old Technician",
        (
            "#690F#6PThe Leibnitz has a mountain \x01",
            "of parts stored in her.\x02\x03",

            "It's dangerous, so stand clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        "#505F#2PActually, we're looking for someone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x102,
        (
            "#010F#2PIsn't there a maintenance\x01",
            "chief by the name of Gustav\x01",
            "on this ship?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #197
        0x8,
        "Old Technician",
        "#692F#6PWhat do you want with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        "#501F#2POh! Well, that's convenient.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #199
        (
            "\x07\x05Estelle explained that Professor Russell had asked\x01",
            "them to find and borrow a combustion engine.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #200
        0x8,
        (
            "#691F#6PAhh, you're running errands\x01",
            "for Russell, are you?\x02\x03",

            "But a combustion engine, huh...?\x01",
            "Well, you've got good timing.\x01",
            "I'll give you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        "#004F#2PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x8,
        "#690F#6PHang on a second...\x02",
    )

    CloseMessageWindow()

    def lambda_57D3():

        label("loc_57D3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_57D3")

    QueueWorkItem2(0x101, 0, lambda_57D3)

    def lambda_57E4():

        label("loc_57E4")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_57E4")

    QueueWorkItem2(0x102, 0, lambda_57E4)

    def lambda_57F5():
        OP_6D(-37020, -3800, 144870, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57F5)
    OP_8E(0x8, 0xFFFF6E74, 0xFFFFF128, 0x23096, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFF85EE, 0xFFFFF128, 0x24432, 0xBB8, 0x0)
    Sleep(1000)

    ChrTalk(    #203
        0x101,
        (
            "#501F#1PDoes he actually have one\x01",
            "packed onto this ship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x102,
        "#010F#1PLooks like it.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFF74C8, 0xFFFFF128, 0x23794, 0xBB8, 0x0)

    def lambda_58A8():
        OP_6D(-42590, -3800, 143930, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58A8)
    OP_8E(0x8, 0xFFFF592A, 0xFFFFF128, 0x23294, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(    #205
        0x8,
        (
            "#691FHere you go. It's a heavy\x01",
            "beast, though, so be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x0, 0x2BC, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #206
        "\x07\x00Received \x07\x02Combustion Engine\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x368, 1)
    OP_8F(0x8, 0xFFFF592A, 0xFFFFF128, 0x23294, 0xBB8, 0x0)
    OP_8C(0x8, 270, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A83")

    ChrTalk(    #207
        0x101,
        (
            "#004FYow... You weren't kidding.\x02\x03",

            "#006FBut we can still manage\x01",
            "to carry it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x8,
        (
            "#692FHeh! You've got some spirit to\x01",
            "you, for such a young girl.\x02\x03",

            "#693FHa ha ha! I like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        "#506FHa ha... Thanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B49")

    label("loc_5A83")


    ChrTalk(    #210
        0x102,
        (
            "#010FIt's really heavy...but we\x01",
            "have to deal with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x8,
        (
            "#692FHeh! I'd have never expected\x01",
            "that kind of spirit out of\x01",
            "today's youth.\x02\x03",

            "#693FHa ha ha! I like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x102,
        "#019FThank you very much.\x02",
    )

    CloseMessageWindow()

    label("loc_5B49")


    ChrTalk(    #213
        0x8,
        (
            "#691FIt's a pretty interesting\x01",
            "little coincidence...\x02\x03",

            "That old fart wants this thing\x01",
            "right after I got it back from\x01",
            "the military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x102,
        "#014FFrom the military...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x8,
        (
            "#690FYeah... This thing was on loan\x01",
            "to them for a little while.\x02\x03",

            "They were using it for some\x01",
            "kind of research.\x02\x03",

            "As a matter of fact, I only\x01",
            "just got it back today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        (
            "#501FHuh...\x01",
            "Lucky for us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x102,
        "#013F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #219
        0x101,
        "#004FWhat's wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_END)), "loc_5D75")

    ChrTalk(    #220
        0x102,
        (
            "#015FOh...it's nothing.\x02\x03",

            "#010FNow that we've got what we\x01",
            "need, why don't we take it\x01",
            "back to the professor?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DD9")

    label("loc_5D75")


    ChrTalk(    #221
        0x102,
        (
            "#015FOh...it's nothing.\x02\x03",

            "#010FNow we need gasoline.\x01",
            "Let's check down in the\x01",
            "basement workshop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD9")


    ChrTalk(    #222
        0x101,
        "#006FSure thing.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #223
        0x101,
        "#001FThank you, Mr. Maintenance Chief!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x8,
        (
            "#691FSure, sure. Give my regards\x01",
            "to the old man.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    EventEnd(0x0)

    label("loc_5E65")

    Return()

    # Function_15_5447 end

    def Function_16_5E66(): pass

    label("Function_16_5E66")

    EventBegin(0x0)
    AddParty(0x6, 0xFF)
    SetChrPos(0x108, -45670, -4000, 146000, 0)
    SetChrPos(0x101, -46540, -4000, 147540, 0)
    SetChrPos(0x102, -47220, -4000, 146840, 0)
    SetChrPos(0x107, -47150, -4000, 145610, 0)
    TurnDirection(0x101, 0x108, 0)
    TurnDirection(0x102, 0x108, 0)
    TurnDirection(0x107, 0x108, 0)
    TurnDirection(0x108, 0x102, 0)
    OP_6D(-45760, -4000, 146000, 0)
    OP_67(0, 9090, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(111000, 0)
    OP_6E(262, 0)
    OP_6F(0x4, 1)
    OP_6F(0x3, 0)
    OP_71(0x6, 0x4)
    OP_6F(0x0, 1001)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x64, 0x0)
    OP_A2(0x559)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x10, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #225
        0x108,
        (
            "#070FI am truly sorry for having\x01",
            "to bid you farewell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x101,
        (
            "#006FHey, it's okay. We really\x01",
            "appreciate all your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x102,
        (
            "#010FAre you taking this ship\x01",
            "directly to Grancel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x108,
        (
            "#072FYes...\x01",
            "There is much I must do.\x02\x03",

            "If I weren't expected there, I would\x01",
            "gladly remain, and do my part to help\x01",
            "resolve this kidnapping incident.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x107, 400)
    Sleep(400)

    ChrTalk(    #229
        0x108,
        "#075FForgive me, little one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x107,
        (
            "#560FD-Don't be silly...\x01",
            "You've done a lot for us.\x02\x03",

            "Thank you so much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x108,
        (
            "#070FHa ha... And I appreciate\x01",
            "you saying so.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #232
        (
            "\x07\x05The express flight to Grancel aboard\x01",
            "the Cecilia will be departing shortly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #233
        (
            "\x07\x05All passengers, please go\x01",
            "to the departure gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    ChrTalk(    #234
        0x108,
        (
            "#070FOops...\x01",
            "Time to make my exit.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x108, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_6246():
        OP_6D(-40990, -4000, 146200, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6246)

    def lambda_625E():
        OP_6B(3360, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_625E)

    def lambda_626E():
        OP_6C(32000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_626E)
    OP_8E(0x108, 0xFFFF4B9C, 0xFFFFF060, 0x23294, 0xBB8, 0x0)
    OP_8E(0x108, 0xFFFF5754, 0xFFFFF128, 0x2328A, 0xBB8, 0x0)
    SetChrFlags(0x108, 0x4)

    def lambda_62AB():
        OP_8E(0xFE, 0xFFFF50B0, 0xFFFFF060, 0x23A50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62AB)

    def lambda_62C6():
        OP_8E(0xFE, 0xFFFF4BD8, 0xFFFFF060, 0x23898, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62C6)

    def lambda_62E1():
        OP_8E(0xFE, 0xFFFF4BF6, 0xFFFFF060, 0x23532, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_62E1)
    OP_8E(0x108, 0xFFFF6FA0, 0xFFFFF128, 0x23294, 0xBB8, 0x0)
    TurnDirection(0x108, 0x107, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #235
        0x108,
        (
            "#070FTake care... Hopefully, we will\x01",
            "meet again, fate willing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        (
            "#501FYou bet'cha!\x02\x03",

            "Oh... How long are you\x01",
            "going to be in Liberl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x108,
        (
            "#073FI couldn't say for certain...\x01",
            "but probably until the queen's\x01",
            "birthday celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        "#001FMaybe we'll see you there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x102,
        "#010FUntil then, take care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x108,
        "#071FSame to you.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    OP_73(0x3)
    Fade(2000)
    OP_6D(-33750, -7050, 155120, 0)
    OP_67(0, -600, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(163000, 0)
    OP_6E(536, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x108, 0x80)
    Sleep(1000)
    OP_A1(0x11, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x4, 0x20)
    SetChrPos(0x11, -34000, -11150, 148000, 0)
    SetChrFlags(0x11, 0x4)
    OP_A1(0x12, 0x5)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x12, -34000, -11150, 148000, 0)
    SetChrFlags(0x12, 0x4)
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    OP_73(0x4)
    Sleep(1000)
    OP_22(0x77, 0x1, 0x64)
    OP_6F(0x4, 61)
    OP_70(0x4, 0xA0)
    OP_73(0x4)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 161)
    OP_70(0x4, 0x104)

    def lambda_6564():
        OP_6D(-33750, -5050, 155120, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6564)

    def lambda_657C():
        OP_67(0, 1800, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_657C)
    OP_91(0x11, 0x0, 0x12C, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0x0, 0x320, 0x0, 0x1F4, 0x0)
    Sleep(2000)

    def lambda_65C1():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_65C1)
    OP_94(0x1, 0x11, 0x0, 0x3E8, 0x3E8, 0x0)

    def lambda_65E6():
        OP_94(0x1, 0xFE, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_65E6)
    OP_94(0x1, 0x11, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_660B():
        OP_94(0x1, 0xFE, 0x0, 0x578, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_660B)
    OP_94(0x1, 0x11, 0x0, 0x578, 0xBB8, 0x0)

    def lambda_6630():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6630)
    OP_94(0x1, 0x11, 0x0, 0x640, 0xFA0, 0x0)

    def lambda_6655():
        OP_94(0x1, 0xFE, 0x0, 0x708, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6655)
    FadeToDark(2000, 0, -1)
    OP_94(0x1, 0x11, 0x0, 0x708, 0x1388, 0x0)

    def lambda_6684():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6684)
    OP_94(0x1, 0x11, 0x0, 0x7D0, 0x1770, 0x0)

    def lambda_66A9():
        OP_94(0x1, 0xFE, 0x0, 0x898, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_66A9)
    OP_94(0x1, 0x11, 0x0, 0x898, 0x1B58, 0x0)

    def lambda_66CE():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_66CE)

    def lambda_66E4():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_66E4)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x5A, 0x0)
    OP_24(0x77, 0x5A)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x50, 0x0)
    OP_24(0x77, 0x50)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x46, 0x0)
    OP_24(0x77, 0x46)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x3C, 0x0)
    OP_24(0x77, 0x3C)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x32, 0x0)
    OP_24(0x77, 0x32)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x28, 0x0)
    OP_24(0x77, 0x28)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x1E, 0x0)
    OP_24(0x77, 0x1E)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x14, 0x0)
    OP_24(0x77, 0x14)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0xA, 0x0)
    OP_24(0x77, 0xA)
    Sleep(100)
    SoundDistance(0x75, 0xFFFF7A4A, 0xFFFFF060, 0x23280, 0x2710, 0x9C40, 0x1, 0x0)
    OP_23(0x77)
    OP_0D()
    OP_B8(0x7)
    RemoveParty(0x7, 0xFF)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_5E66 end

    def Function_17_689B(): pass

    label("Function_17_689B")

    Sleep(100)
    OP_20(0x3E8)
    Fade(1000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0xA, 0xFF)
    OP_8C(0xA, 45, 0)
    SetChrPos(0xB, -45980, 0, 129680, 0)
    ClearChrFlags(0xB, 0x80)
    OP_23(0x75)
    OP_22(0x75, 0x1, 0x64)
    OP_6D(-36160, -4000, 150300, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(112000, 0)
    OP_6E(415, 0)
    OP_0D()
    OP_1D(0x57)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    OP_73(0x3)
    OP_72(0x4, 0x4)
    OP_A1(0x11, 0x4)
    OP_72(0x9, 0x4)
    OP_72(0x9, 0x20)
    SetChrPos(0x11, -34000, -11150, 148000, 0)
    SetChrFlags(0x11, 0x4)
    OP_A1(0x12, 0x5)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x12, -34000, -11150, 148000, 0)
    SetChrFlags(0x12, 0x4)

    def lambda_69A7():
        OP_67(0, 7880, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69A7)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0x4, 1)
    OP_70(0x4, 0x3C)
    OP_73(0x4)
    OP_22(0x77, 0x1, 0x64)
    OP_6F(0x4, 61)
    OP_70(0x4, 0xA0)
    OP_73(0x4)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 161)
    OP_70(0x4, 0x104)

    def lambda_69FE():
        OP_6E(465, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_69FE)

    def lambda_6A0E():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6A0E)
    OP_91(0x11, 0x0, 0x1F4, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0x0, 0x3E8, 0x0, 0x258, 0x0)
    Sleep(500)

    def lambda_6A4B():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6A4B)
    OP_94(0x1, 0x11, 0x0, 0x1F4, 0x3E8, 0x0)

    def lambda_6A70():
        OP_94(0x1, 0xFE, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6A70)
    OP_94(0x1, 0x11, 0x0, 0x258, 0x7D0, 0x0)

    def lambda_6A95():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6A95)
    OP_94(0x1, 0x11, 0x0, 0x2BC, 0xBB8, 0x0)

    def lambda_6ABA():
        OP_94(0x1, 0xFE, 0x0, 0x320, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6ABA)
    OP_94(0x1, 0x11, 0x0, 0x320, 0xFA0, 0x0)

    def lambda_6ADF():
        OP_94(0x1, 0xFE, 0x0, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6ADF)
    OP_94(0x1, 0x11, 0x0, 0x384, 0x1388, 0x0)

    def lambda_6B04():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6B04)
    OP_94(0x1, 0x11, 0x0, 0x3E8, 0x1770, 0x0)

    def lambda_6B29():
        OP_94(0x1, 0xFE, 0x0, 0x44C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6B29)
    OP_94(0x1, 0x11, 0x0, 0x44C, 0x1B58, 0x0)

    def lambda_6B4E():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6B4E)

    def lambda_6B64():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B64)
    OP_43(0x11, 0x3, 0x0, 0x12)
    OP_8C(0xA, 0, 400)

    ChrTalk(    #241
        0xA,
        "#800F#5PI'll be counting on you, bracers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xB,
        "#1PHey, wait!\x02",
    )

    CloseMessageWindow()

    def lambda_6BCC():
        OP_6D(-44410, -4000, 143480, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BCC)

    def lambda_6BE4():
        OP_6E(273, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6BE4)

    def lambda_6BF4():

        label("loc_6BF4")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_6BF4")

    QueueWorkItem2(0xA, 1, lambda_6BF4)
    OP_8E(0xB, 0xFFFF4A52, 0xFFFFF060, 0x23348, 0x1388, 0x0)

    ChrTalk(    #243
        0xB,
        (
            "#152F#1P*huff* *huff*\x02\x03",

            "Whoa...head rush...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xA,
        "#802F#4PHmm? Dorothy?\x02",
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_8E(0xA, 0xFFFF4A2A, 0xFFFFF060, 0x22AC4, 0x7D0, 0x0)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #245
        0xB,
        (
            "#152F#1POh! Chief!\x02\x03",

            "Were Estelle and crew aboard\x01",
            "that last ship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xA,
        (
            "#802F#2PThat's right...\x01",
            "How did you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xB,
        (
            "#152F#1PThe guild tipped me.\x02\x03",

            "And there's biiiig trouble brewing, if what\x01",
            "my editors told me rings true. I wanted to\x01",
            "let them know before they left...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xA,
        (
            "#805F#2PWh-What kind of trouble...?\x02\x03",

            "#806FI shudder to think how much\x01",
            "worse the situation can get...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xB,
        (
            "#154F#1PWeeeeeell... This is totally\x01",
            "off the record...\x02\x03",

            "...but it seems some members of the\x01",
            "Royal Guardsmen in Grancel were just\x01",
            "arrested for treason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xA,
        "#804F#2P#3SWh-What?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/E0002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_689B end

    def Function_18_6EDE(): pass

    label("Function_18_6EDE")

    Sleep(1000)
    OP_24(0x77, 0x5F)
    OP_24(0x75, 0x5F)
    Sleep(200)
    OP_24(0x77, 0x5A)
    OP_24(0x75, 0x5A)
    Sleep(200)
    OP_24(0x77, 0x55)
    OP_24(0x75, 0x55)
    Sleep(200)
    OP_24(0x77, 0x50)
    OP_24(0x75, 0x50)
    Sleep(200)
    OP_24(0x77, 0x4B)
    OP_24(0x75, 0x4B)
    Sleep(200)
    OP_24(0x77, 0x46)
    OP_24(0x75, 0x46)
    Sleep(200)
    OP_24(0x77, 0x41)
    OP_24(0x75, 0x41)
    Sleep(200)
    OP_24(0x77, 0x3C)
    OP_24(0x75, 0x3C)
    Sleep(200)
    OP_24(0x77, 0x32)
    OP_24(0x75, 0x32)
    Sleep(200)
    OP_23(0x77)
    OP_23(0x75)
    Return()

    # Function_18_6EDE end

    def Function_19_6F5F(): pass

    label("Function_19_6F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82F2")
    EventBegin(0x0)
    OP_A2(0x603)
    OP_28(0x54, 0x1, 0x4)
    OP_28(0x54, 0x1, 0x8)
    SetChrPos(0xC, -46060, 0, 127820, 0)
    ClearChrFlags(0xC, 0x80)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #251
        0xC,
        "Nya-go.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6FD3():

        label("loc_6FD3")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_6FD3")

    QueueWorkItem2(0x101, 3, lambda_6FD3)

    def lambda_6FE4():

        label("loc_6FE4")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_6FE4")

    QueueWorkItem2(0x102, 3, lambda_6FE4)

    def lambda_6FF5():
        OP_6D(-46010, -1000, 131740, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6FF5)

    def lambda_700D():
        OP_67(0, 7390, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_700D)

    def lambda_7025():
        OP_6B(3700, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7025)

    def lambda_7035():
        OP_6C(158000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_7035)
    Sleep(3000)
    SetChrPos(0x101, -45400, -4000, 140210, 0)
    SetChrPos(0x102, -46640, -4000, 140440, 0)

    def lambda_706C():
        OP_8E(0xFE, 0xFFFF4DA4, 0xFFFFF060, 0x21D2C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_706C)

    def lambda_7087():
        OP_6D(-45610, -4000, 139000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7087)
    Sleep(3000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7239")

    ChrTalk(    #252
        0x101,
        "#004FAntoine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x102,
        (
            "#010FHey... Yesterday must have\x01",
            "been rough on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #254
        0xC,
        "Nyao-n...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x101,
        (
            "#509FYou scared me half to death!\x02\x03",

            "I hope you take some time \x01",
            "to think about why what\x01",
            "you did was wrong.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #256
        0xC,
        "Myaon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x101,
        "#007FNope, not listening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x102,
        (
            "#019FHa ha...\x01",
            "I think he's playing dumb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x101,
        (
            "#006FOh, well. I guess we do\x01",
            "owe him some gratitude.\x02\x03",

            "Thank you, Antoine.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #260
        0xC,
        "Mya～uun.\x02",
    )

    CloseMessageWindow()
    Jump("loc_73CE")

    label("loc_7239")


    ChrTalk(    #261
        0x101,
        (
            "#004FHey...\x01",
            "Wasn't this the cat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x102,
        (
            "#010FYep, he's the one who sneaked\x01",
            "into that shipping container.\x02\x03",

            "His name's Antoine, if\x01",
            "I remember correctly.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #263
        0xC,
        "Nyao-n...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        (
            "#001FHa ha ha! Awwww...\x02\x03",

            "#006FYou scared me half to death!\x02\x03",

            "I hope you take some time \x01",
            "to think about why what\x01",
            "you did was wrong.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #265
        0xC,
        "Myaon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        "#007FNope, not listening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x102,
        (
            "#019FHa ha...\x01",
            "I think he's playing dumb.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73CE")

    SetChrPos(0x8, -47160, 0, 129750, 0)
    ClearChrFlags(0x8, 0x80)

    ChrTalk(    #268
        0x8,
        "#3PHey! There you are!\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7433():
        OP_6D(-46010, -4000, 137720, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7433)

    def lambda_744B():

        label("loc_744B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_744B")

    QueueWorkItem2(0x101, 3, lambda_744B)

    def lambda_745C():

        label("loc_745C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_745C")

    QueueWorkItem2(0x102, 3, lambda_745C)

    def lambda_746D():
        OP_8E(0xFE, 0xFFFF4B92, 0xFFFFF060, 0x21E44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_746D)
    Sleep(1000)

    def lambda_748D():

        label("loc_748D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_748D")

    QueueWorkItem2(0x101, 3, lambda_748D)

    def lambda_749E():

        label("loc_749E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_749E")

    QueueWorkItem2(0x102, 3, lambda_749E)
    OP_8C(0xC, 192, 800)

    def lambda_74B6():
        OP_8F(0xFE, 0xFFFF4DA4, 0x0, 0x1F521, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_74B6)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #269
        0x101,
        "#501FHi, Gustav!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x8,
        (
            "#691F#2PThe factory chief told me that\x01",
            "the rescue went off without a\x01",
            "hitch.\x02\x03",

            "The professor's always been a mentor\x01",
            "of sorts to all the engineers...\x02\x03",

            "So I just wanted to say thanks\x01",
            "on behalf of everyone here.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(    #271
        0x101,
        (
            "#008FHa ha... Well, we couldn't have\x01",
            "pulled it off without you and\x01",
            "your crew's help.\x02\x03",

            "Tita was so surprised that\x01",
            "I thought her eyes might\x01",
            "pop out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x102,
        "#010F#5PSo that really WAS on purpose?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x8,
        (
            "#693F#2PHa ha ha! Well, to fool the\x01",
            "enemy, sometimes you have\x01",
            "to fool your allies first.\x02\x03",

            "#691FSo...what business do\x01",
            "you have at the gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x101,
        (
            "#006FThe professor asked us to\x01",
            "go to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x102,
        (
            "#010F#5PWe're a little early for\x01",
            "the eleven o'clock flight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x8,
        (
            "#692F#2PYeah... Well, it also looks\x01",
            "to be a little late.\x02\x03",

            "#691FThere's still time to drop off\x01",
            "your bags, so I think you can\x01",
            "take it easy in town for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x101,
        (
            "#505FHmmm...\x01",
            "That sounds like fun.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -45980, 0, 128889, 0)
    OP_4A(0x9, 255)

    ChrTalk(    #278
        0x9,
        "#3PHey, you two!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_78BF():
        OP_8E(0x9, 0xFFFF4F8E, 0xFFFFF060, 0x21BC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_78BF)

    def lambda_78DA():
        OP_6D(-46700, -2500, 134910, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_78DA)

    def lambda_78F2():

        label("loc_78F2")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_78F2")

    QueueWorkItem2(0x101, 2, lambda_78F2)

    def lambda_7903():

        label("loc_7903")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_7903")

    QueueWorkItem2(0x102, 2, lambda_7903)

    def lambda_7914():

        label("loc_7914")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_7914")

    QueueWorkItem2(0x8, 2, lambda_7914)
    Sleep(1500)

    def lambda_792A():

        label("loc_792A")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_792A")

    QueueWorkItem2(0x101, 2, lambda_792A)

    def lambda_793B():

        label("loc_793B")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_793B")

    QueueWorkItem2(0x102, 2, lambda_793B)

    def lambda_794C():

        label("loc_794C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_794C")

    QueueWorkItem2(0x8, 2, lambda_794C)

    def lambda_795D():
        OP_6D(-46010, -4000, 137720, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_795D)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x102, 0)

    ChrTalk(    #279
        0x8,
        (
            "#692F#4PWell, if it ain't Gerald.\x02\x03",

            "What's going on?\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #280
        0x9,
        "Perfect. You're all here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x9,
        (
            "To be honest, we've had\x01",
            "some trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x8,
        "#692F#4PWhat kind of trouble?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x9,
        (
            "Well, we received a communique\x01",
            "from the airship corporation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x9,
        (
            "It looks like the ship will be\x01",
            "arriving a few hours late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        "#004FWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x102,
        "#012F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x8,
        (
            "#692F#4POkay, just what's going on here?\x02\x03",

            "More sky bandit trouble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x9,
        "Well, something like that anyway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x9,
        (
            "Seems to me that the terrorists\x01",
            "staged an ambush, to disrupt\x01",
            "the queen's birthday celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x9,
        (
            "All ships are grounded at port\x01",
            "while the military conducts\x01",
            "inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        "#002F(Th-That would mean...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x102,
        (
            "#015F#5P(They're probably looking\x01",
            "for the professor's group...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x9,
        (
            "Which means that the ship\x01",
            "that's bound for Grancel\x01",
            "is being held up in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x9,
        (
            "Apparently, a military guard\x01",
            "ship is coming here from\x01",
            "Leiston Fortress, instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x8,
        (
            "#691F#4PAhh, I get it.\x02\x03",

            "But if that's the case, you're\x01",
            "going to be extremely busy\x01",
            "soon, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #296
        0x9,
        (
            "No kidding. I've got to explain\x01",
            "the situation to the customers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #297
        0x9,
        (
            "Which means that you two have\x01",
            "a good chunk of time to kill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x9,
        (
            "Just thought of something... If you\x01",
            "want to wait at the Bracer Guild,\x01",
            "I can get in touch with you there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        "#505FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x102,
        "#010F#5PThank you very much.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 190, 400)
    OP_8F(0x9, 0xFFFF4C3C, 0x0, 0x1F982, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    SetChrPos(0x9, -20110, 8000, 121830, 177)
    OP_4B(0x9, 255)
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #301
        0x8,
        (
            "#690F#2P...Well, this stinks like\x01",
            "last year's diapers.\x02\x03",

            "If the military's coming here,\x01",
            "I know they'll want to check\x01",
            "out the Leibnitz.\x02\x03",

            "I'd better have a talk\x01",
            "with the factory chief.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7FBD():

        label("loc_7FBD")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_7FBD")

    QueueWorkItem2(0x101, 2, lambda_7FBD)

    def lambda_7FCE():

        label("loc_7FCE")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_7FCE")

    QueueWorkItem2(0x102, 2, lambda_7FCE)

    ChrTalk(    #302
        0x101,
        (
            "#002FYeah, if they check up on\x01",
            "what happened yesterday,\x01",
            "that won't be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x102,
        "#012FBe careful, whatever you do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x8,
        (
            "#691F#2PHa ha... I ain't so senile that\x01",
            "I need a couple of punk kids\x01",
            "to tell ME to be careful.\x02\x03",

            "#693FTake it easy, you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 190, 600)
    OP_8F(0x8, 0xFFFF4B92, 0x0, 0x1F8E2, 0xFA0, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_8100():
        OP_6D(-45920, -4000, 139870, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8100)
    TurnDirection(0x101, 0x102, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #305
        0x101,
        (
            "#002FJoshua...?\x01",
            "This doesn't look so hot.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #306
        0x102,
        (
            "#013FYeah... This could put\x01",
            "the airliner in danger.\x02\x03",

            "#012FWe've got time, so maybe we\x01",
            "should take the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x101,
        (
            "#509FAw, man... And it's been so\x01",
            "long since I last got to ride\x01",
            "on an airship, too.\x02\x03",

            "This is all your fault,\x01",
            "Colonel Richard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x102,
        (
            "#019FWell, try to look at it as\x01",
            "an ongoing opportunity to\x01",
            "advance your training.\x02\x03",

            "#010FSo I guess we need to\x01",
            "cancel our reservations\x01",
            "at the reception desk.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x80)
    EventEnd(0x0)

    label("loc_82F2")

    Return()

    # Function_19_6F5F end

    def Function_20_82F3(): pass

    label("Function_20_82F3")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -34090, -4000, 144010, 270)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_20_82F3 end

    def Function_21_8316(): pass

    label("Function_21_8316")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -35750, -4000, 143010, 90)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_21_8316 end

    def Function_22_8339(): pass

    label("Function_22_8339")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -35770, -4000, 144120, 90)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_22_8339 end

    def Function_23_835C(): pass

    label("Function_23_835C")

    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -36170, -4000, 145050, 90)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_23_835C end

    def Function_24_837F(): pass

    label("Function_24_837F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #309
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "⇒ To Grancel\x01",
            "⇒ To Ruan\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #310
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

    # Function_24_837F end

    def Function_25_843A(): pass

    label("Function_25_843A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #311
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

    # Function_25_843A end

    def Function_26_84C8(): pass

    label("Function_26_84C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_857D")
    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #312
        0x102,
        (
            "#010FFirst, we should stop by\x01",
            "the reception desk and\x01",
            "cancel our reservations.\x02\x03",

            "Once that's done, we can\x01",
            "leave whenever we want.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_857D")

    Return()

    # Function_26_84C8 end

    SaveToFile()

Try(main)
