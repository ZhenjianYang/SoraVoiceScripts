from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0101   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
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
        '矿工兰古',                             # 9
        '矿工提恩特',                           # 10
        '矿工皮尔姆',                           # 11
        '矿工海涅',                             # 12
        '矿工彭兹',                             # 13
        '加通老大',                             # 14
        '利吉',                                 # 15
        '螃蟹老大',                             # 16
        '螃蟹',                                 # 17
        '螃蟹',                                 # 18
        '螃蟹',                                 # 19
        '螃蟹',                                 # 20
        '螃蟹',                                 # 21
        '螃蟹',                                 # 22
        '螃蟹',                                 # 23
        '螃蟹',                                 # 24
        '螃蟹',                                 # 25
        '螃蟹',                                 # 26
        '螃蟹',                                 # 27
        '螃蟹',                                 # 28
        '目标用照相机',                         # 29
        '',                                     # 30
        '',                                     # 31
        '',                                     # 32
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
        'ED6_DT29/CH12920 ._CH',             # 00
        'ED6_DT29/CH12921 ._CH',             # 01
        'ED6_DT09/CH10000 ._CH',             # 02
        'ED6_DT09/CH10001 ._CH',             # 03
        'ED6_DT07/CH01500 ._CH',             # 04
        'ED6_DT07/CH01530 ._CH',             # 05
        'ED6_DT07/CH00490 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT29/CH12920P._CP',             # 00
        'ED6_DT29/CH12921P._CP',             # 01
        'ED6_DT09/CH10000P._CP',             # 02
        'ED6_DT09/CH10001P._CP',             # 03
        'ED6_DT07/CH01500P._CP',             # 04
        'ED6_DT07/CH01530P._CP',             # 05
        'ED6_DT07/CH00490P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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


    DeclMonster(
        X                   = 125180,
        Z                   = 0,
        Y                   = 20140,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 112970,
        Z                   = -210,
        Y                   = 81150,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 104360,
        Z                   = 0,
        Y                   = 53370,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 90600,
        Y                   = -1000,
        Z                   = 68100,
        Range               = 97100,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x10EB4,
        Unknown_18          = 0x0,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 125000,
        Y                   = -1000,
        Z                   = 24700,
        Range               = 134000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x65F4,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 106480,
        Y                   = -1000,
        Z                   = 31780,
        Range               = 104940,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x5E60,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 98500,
        Y                   = -1000,
        Z                   = 3100,
        Range               = 99500,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x3BC4,
        Unknown_18          = 0x0,
        Unknown_1C          = 32,
    )


    DeclActor(
        TriggerX            = 54000,
        TriggerZ            = 500,
        TriggerY            = 58200,
        TriggerRange        = 600,
        ActorX              = 54000,
        ActorZ              = 500,
        ActorY              = 58200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14000,
        TriggerZ            = 1000,
        TriggerY            = 31800,
        TriggerRange        = 1000,
        ActorX              = 14000,
        ActorZ              = 1000,
        ActorY              = 31800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 45,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_49E",          # 00, 0
        "Function_1_653",          # 01, 1
        "Function_2_9CE",          # 02, 2
        "Function_3_B4B",          # 03, 3
        "Function_4_CCF",          # 04, 4
        "Function_5_DE7",          # 05, 5
        "Function_6_F20",          # 06, 6
        "Function_7_108B",         # 07, 7
        "Function_8_11C8",         # 08, 8
        "Function_9_137E",         # 09, 9
        "Function_10_1BE9",        # 0A, 10
        "Function_11_3DAD",        # 0B, 11
        "Function_12_4C7E",        # 0C, 12
        "Function_13_4C92",        # 0D, 13
        "Function_14_4CBF",        # 0E, 14
        "Function_15_4CEC",        # 0F, 15
        "Function_16_4D19",        # 10, 16
        "Function_17_577D",        # 11, 17
        "Function_18_58C6",        # 12, 18
        "Function_19_6187",        # 13, 19
        "Function_20_61F2",        # 14, 20
        "Function_21_625D",        # 15, 21
        "Function_22_62C8",        # 16, 22
        "Function_23_634A",        # 17, 23
        "Function_24_63E0",        # 18, 24
        "Function_25_6F39",        # 19, 25
        "Function_26_6F66",        # 1A, 26
        "Function_27_6F93",        # 1B, 27
        "Function_28_6FC0",        # 1C, 28
        "Function_29_6FED",        # 1D, 29
        "Function_30_7009",        # 1E, 30
        "Function_31_7025",        # 1F, 31
        "Function_32_7041",        # 20, 32
        "Function_33_8012",        # 21, 33
        "Function_34_845E",        # 22, 34
        "Function_35_88BC",        # 23, 35
        "Function_36_A4E6",        # 24, 36
        "Function_37_A56C",        # 25, 37
        "Function_38_A5F9",        # 26, 38
        "Function_39_A64A",        # 27, 39
        "Function_40_A67F",        # 28, 40
        "Function_41_A6B4",        # 29, 41
        "Function_42_A6E9",        # 2A, 42
        "Function_43_A71E",        # 2B, 43
        "Function_44_A741",        # 2C, 44
        "Function_45_A7B9",        # 2D, 45
    )


    def Function_0_49E(): pass

    label("Function_0_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_507")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xD, 24270, -200, 15450, 315)
    SetChrPos(0x9, 12850, 0, 12900, 140)
    SetChrPos(0xC, 10170, 0, 29510, 315)
    SetChrPos(0xA, 36510, 0, 25540, 270)
    SetChrPos(0xB, 36500, -130, 23470, 270)
    Jump("loc_652")

    label("loc_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_652")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_END)), "loc_617")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 132100, 0, 74120, 225)
    SetChrPos(0x9, 132170, 0, 72480, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_END)), "loc_57C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, 131940, 0, 69900, 315)
    SetChrPos(0xB, 130930, 0, 68610, 45)
    SetChrFlags(0x1D, 0x80)
    Jump("loc_5A8")

    label("loc_57C")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, 130610, 1000, 14190, 180)
    SetChrPos(0xB, 130610, 1000, 12770, 0)

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_END)), "loc_5C8")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 124780, 0, 74190, 180)
    Jump("loc_5DE")

    label("loc_5C8")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 96530, -70, 29250, 0)

    label("loc_5DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_END)), "loc_5FE")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 126540, 0, 75140, 180)
    Jump("loc_614")

    label("loc_5FE")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 86190, -500, 13450, 0)

    label("loc_614")

    Jump("loc_652")

    label("loc_617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 7)), scpexpr(EXPR_END)), "loc_637")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 51720, 0, 55230, 180)
    Jump("loc_652")

    label("loc_637")

    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 53910, 0, 53890, 0)

    label("loc_652")

    Return()

    # Function_0_49E end

    def Function_1_653(): pass

    label("Function_1_653")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_675")
    OP_6F(0x0, 75)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_675")
    OP_65(0x0, 0x1)

    label("loc_675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_814")
    OP_D2(0x26006E, 0x260073, 0x7)
    OP_D2(0x26006E, 0x260073, 0x8)
    OP_D2(0x26006E, 0x260073, 0x9)
    OP_D2(0x270110, 0x270120, 0xA)
    OP_D2(0x270111, 0x270121, 0xB)
    OP_D2(0x270130, 0x270140, 0xC)
    OP_D2(0x270131, 0x270141, 0xD)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_6DC"),
        (5, "loc_6F3"),
        (6, "loc_70A"),
        (7, "loc_721"),
        (SWITCH_DEFAULT, "loc_738"),
    )


    label("loc_6DC")

    OP_D2(0x701D0, 0x701DC, 0xE)
    OP_D2(0x701D1, 0x701DD, 0xF)
    Jump("loc_738")

    label("loc_6F3")

    OP_D2(0x70218, 0x70224, 0xE)
    OP_D2(0x70219, 0x70225, 0xF)
    Jump("loc_738")

    label("loc_70A")

    OP_D2(0x70230, 0x7023C, 0xE)
    OP_D2(0x70231, 0x7023D, 0xF)
    Jump("loc_738")

    label("loc_721")

    OP_D2(0x70248, 0x70254, 0xE)
    OP_D2(0x70249, 0x70255, 0xF)
    Jump("loc_738")

    label("loc_738")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_751"),
        (5, "loc_768"),
        (6, "loc_77F"),
        (7, "loc_796"),
        (SWITCH_DEFAULT, "loc_7AD"),
    )


    label("loc_751")

    OP_D2(0x701D0, 0x701DC, 0x10)
    OP_D2(0x701D1, 0x701DD, 0x11)
    Jump("loc_7AD")

    label("loc_768")

    OP_D2(0x70218, 0x70224, 0x10)
    OP_D2(0x70219, 0x70225, 0x11)
    Jump("loc_7AD")

    label("loc_77F")

    OP_D2(0x70230, 0x7023C, 0x10)
    OP_D2(0x70231, 0x7023D, 0x11)
    Jump("loc_7AD")

    label("loc_796")

    OP_D2(0x70248, 0x70254, 0x10)
    OP_D2(0x70249, 0x70255, 0x11)
    Jump("loc_7AD")

    label("loc_7AD")

    LoadEffect(0x0, "map\\\\mp002_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 95730, 0, 78730, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 1000)
    OP_D2(0x29039C, 0x2903A0, 0x12)
    OP_D2(0x29039D, 0x2903A1, 0x13)
    OP_D2(0x2903A2, 0x2903A3, 0x14)

    label("loc_814")

    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_71(0x15, 0x4)
    OP_71(0x16, 0x4)
    OP_71(0x17, 0x4)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    OP_71(0x20, 0x4)
    OP_71(0x21, 0x4)
    OP_71(0x22, 0x4)
    OP_71(0x23, 0x4)
    OP_71(0x24, 0x4)
    OP_71(0x25, 0x4)
    OP_71(0x26, 0x4)
    OP_71(0x27, 0x4)
    OP_71(0x28, 0x4)
    OP_71(0x29, 0x4)
    OP_71(0x2A, 0x4)
    OP_71(0x2B, 0x4)
    OP_71(0x2C, 0x4)
    OP_71(0x2D, 0x4)
    OP_71(0x2E, 0x4)
    OP_71(0x2F, 0x4)
    OP_71(0x30, 0x4)
    OP_71(0x31, 0x4)
    OP_71(0x32, 0x4)
    OP_79(0x4, 0x2)
    OP_79(0x5, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_79(0x9, 0x2)
    OP_79(0xA, 0x2)
    OP_79(0xB, 0x2)
    OP_79(0xC, 0x2)
    OP_79(0xD, 0x2)
    OP_79(0xE, 0x2)
    OP_79(0xF, 0x2)
    OP_79(0x10, 0x2)
    OP_79(0x11, 0x2)
    OP_79(0x12, 0x2)
    OP_79(0x13, 0x2)
    OP_79(0x14, 0x2)
    OP_79(0x15, 0x2)
    OP_79(0x16, 0x2)
    OP_79(0x17, 0x2)
    OP_79(0x18, 0x2)
    OP_79(0x19, 0x2)
    OP_79(0x1A, 0x2)
    OP_79(0x1B, 0x2)
    OP_79(0x1C, 0x2)
    OP_79(0x1D, 0x2)
    OP_79(0x1E, 0x2)
    OP_79(0x1F, 0x2)
    OP_79(0x20, 0x2)
    OP_79(0x21, 0x2)
    OP_79(0x22, 0x2)
    OP_79(0x23, 0x2)
    OP_79(0x24, 0x2)
    OP_79(0x25, 0x2)
    OP_79(0x26, 0x2)
    OP_79(0x27, 0x2)
    OP_79(0x28, 0x2)
    OP_79(0x29, 0x2)
    OP_79(0x2A, 0x2)
    OP_79(0x2B, 0x2)
    OP_79(0x2C, 0x2)
    OP_79(0x2D, 0x2)
    OP_79(0x2E, 0x2)
    OP_79(0x2F, 0x2)
    OP_79(0x30, 0x2)
    OP_79(0x31, 0x2)
    OP_79(0x32, 0x2)
    OP_7B()
    OP_77(0x96, 0x96, 0x96, 0x0, 0x0)
    OP_D7(0x1, 20000, 0)
    Return()

    # Function_1_653 end

    def Function_2_9CE(): pass

    label("Function_2_9CE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F3")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_B35")

    label("loc_9F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_B35")

    label("loc_A0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A25")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_B35")

    label("loc_A25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3E")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_B35")

    label("loc_A3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A57")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_B35")

    label("loc_A57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A70")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_B35")

    label("loc_A70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A89")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_B35")

    label("loc_A89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA2")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_B35")

    label("loc_AA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABB")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_B35")

    label("loc_ABB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD4")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_B35")

    label("loc_AD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AED")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_B35")

    label("loc_AED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B06")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_B35")

    label("loc_B06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_B35")

    label("loc_B1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B35")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_B35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B4A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_B35")

    label("loc_B4A")

    Return()

    # Function_2_9CE end

    def Function_3_B4B(): pass

    label("Function_3_B4B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_END)), "loc_C6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BAF")

    ChrTalk(    #0
        0xFE,
        (
            "大家平安\x01",
            "我就放心了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "游击士朋友要是\x01",
            "也能早点被找到就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C67")

    label("loc_BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C0F")

    ChrTalk(    #2
        0xFE,
        (
            "还应该有矿工同伴\x01",
            "隐藏在坑道里面才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "请你们想办法\x01",
            "把他们救出来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C67")

    label("loc_C0F")


    ChrTalk(    #4
        0xFE,
        (
            "我、我和提恩特\x01",
            "会乖乖待在这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "那、那么游击士朋友。\x01",
            "老大他们就拜托你们了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C67")

    Jump("loc_CCB")

    label("loc_C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 7)), scpexpr(EXPR_END)), "loc_CC6")

    ChrTalk(    #6
        0xFE,
        (
            "抱歉，请想办法帮我\x01",
            "确认一下坑道的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "老大他们一定也\x01",
            "在等待着救援呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCB")

    label("loc_CC6")

    Call(0, 9)
    Return()

    label("loc_CCB")

    TalkEnd(0x8)
    Return()

    # Function_3_B4B end

    def Function_4_CCF(): pass

    label("Function_4_CCF")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D55")

    ChrTalk(    #8
        0xFE,
        "哟，游击士们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "正准备要回去吃饭的时候\x01",
            "工作都已经开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "呵呵呵……\x01",
            "肚子一饿就使不出力气了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_DA7")

    label("loc_D55")


    ChrTalk(    #11
        0xFE,
        (
            "我准备回去吃饭的时候\x01",
            "工作已经开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "呵呵呵……\x01",
            "肚子饿得使不出力气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA7")

    Jump("loc_DE3")

    label("loc_DAA")


    ChrTalk(    #13
        0xFE,
        (
            "快、快点帮助大家\x01",
            "从这里逃离吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "（发抖）……\x02",
    )

    CloseMessageWindow()

    label("loc_DE3")

    TalkEnd(0x9)
    Return()

    # Function_4_CCF end

    def Function_5_DE7(): pass

    label("Function_5_DE7")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_EE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8D")

    ChrTalk(    #15
        0xFE,
        (
            "哎呀，各位游击士。\x01",
            "又给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "这次的事情也\x01",
            "一定是女神的旨意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "我觉得一定是女神\x01",
            "想通过那起事故\x01",
            "向我们传递什么讯息吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_EDD")

    label("loc_E8D")


    ChrTalk(    #18
        0xFE,
        (
            "那起事故也一定是\x01",
            "女神的旨意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "我也打算要为了\x01",
            "理解启示而重新读圣典。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EDD")

    Jump("loc_F1C")

    label("loc_EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_END)), "loc_F17")

    ChrTalk(    #20
        0xFE,
        (
            "女神啊……\x01",
            "请拯救我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "哈哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F1C")

    label("loc_F17")

    Call(0, 18)
    Return()

    label("loc_F1C")

    TalkEnd(0xA)
    Return()

    # Function_5_DE7 end

    def Function_6_F20(): pass

    label("Function_6_F20")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1033")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE2")

    ChrTalk(    #22
        0xFE,
        (
            "皮尔姆那家伙还是\x01",
            "把一切都归咎于女神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "真是的，你以为是谁\x01",
            "救了你啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "如果再发生事故，\x01",
            "我看那家伙就不必去救了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "不那么做的话\x01",
            "那个笨蛋一辈子也不会清醒。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1030")

    label("loc_FE2")


    ChrTalk(    #26
        0xFE,
        (
            "皮尔姆那家伙还是\x01",
            "把一切都归咎于女神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "真是的，你以为是谁\x01",
            "救了你啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1030")

    Jump("loc_1087")

    label("loc_1033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_END)), "loc_1082")

    ChrTalk(    #28
        0xFE,
        "皮尔姆那家伙又在祈祷了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "唉，事到如今\x01",
            "懒得再对他说教了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1087")

    label("loc_1082")

    Call(0, 18)
    Return()

    label("loc_1087")

    TalkEnd(0xB)
    Return()

    # Function_6_F20 end

    def Function_7_108B(): pass

    label("Function_7_108B")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_11A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1158")

    ChrTalk(    #30
        0xFE,
        (
            "提恩特那家伙，\x01",
            "似乎又在偷懒的样子，\x01",
            "所以我已经向老大告状了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "嘿嘿，谁叫他发生事故时\x01",
            "一个人逃跑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "不过，那家伙当时\x01",
            "动作可真快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "工作时也能那样\x01",
            "干脆利落就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_11A2")

    label("loc_1158")


    ChrTalk(    #34
        0xFE,
        (
            "遇到事故时的提恩特\x01",
            "动作可真快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "工作时也能那样\x01",
            "干脆利落就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A2")

    Jump("loc_11C4")

    label("loc_11A5")


    ChrTalk(    #36
        0xFE,
        (
            "呼～呼～\x01",
            "真、真是可怕……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C4")

    TalkEnd(0xC)
    Return()

    # Function_7_108B end

    def Function_8_11C8(): pass

    label("Function_8_11C8")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_12E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1280")

    ChrTalk(    #37
        0xD,
        "喔，是各位游击士啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        (
            "托你们的福\x01",
            "已经可以重新开工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xD,
        (
            "虽然升降机\x01",
            "依然还是不能动，\x01",
            "不过现在发牢骚也没用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xD,
        (
            "总之先从可以进行的地方\x01",
            "开始开采吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_12E1")

    label("loc_1280")


    ChrTalk(    #41
        0xD,
        (
            "虽然升降机\x01",
            "依然还是不能动，\x01",
            "不过现在发牢骚也没用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xD,
        (
            "真想要小姐你们\x01",
            "使用过的那个装置啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E1")

    Jump("loc_137A")

    label("loc_12E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1343")

    ChrTalk(    #43
        0xD,
        (
            "游击士小哥\x01",
            "可能还在现场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        (
            "他在那里直到最后\x01",
            "还在为我们争取\x01",
            "逃跑的时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_137A")

    label("loc_1343")


    ChrTalk(    #45
        0xD,
        (
            "游击士小哥\x01",
            "可能还在现场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        "真希望他能没事……\x02",
    )

    CloseMessageWindow()

    label("loc_137A")

    TalkEnd(0xD)
    Return()

    # Function_8_11C8 end

    def Function_9_137E(): pass

    label("Function_9_137E")

    EventBegin(0x0)
    Fade(500)
    OP_6D(54410, 60, 52800, 0)
    OP_67(0, 7910, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 54510, 150, 52380, 0)
    SetChrPos(0x102, 53460, 160, 52670, 0)
    SetChrPos(0xF8, 54510, 150, 51180, 0)
    SetChrPos(0xF9, 53460, 160, 51470, 0)
    OP_4A(0x8, 255)
    OP_0D()

    ChrTalk(    #47
        0x8,
        "唔唔～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        "这可麻烦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1015F请问，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #50
        0x8,
        (
            "哦，原来是\x01",
            "游击士姐姐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "上次多亏你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1016F啊哈哈，真是怀念啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        (
            "#1040F是来搬运七耀石时\x01",
            "碰上塌方的事吧。\x02\x03",

            "#1035F确实很怀念，\x01",
            "不过现在不是闲聊过去的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1004F啊，对。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "嗯，其实是升降机\x01",
            "不能动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "没办法和在坑道的\x01",
            "老大他们交接班。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A8")

    ChrTalk(    #57
        0x103,
        (
            "#022F之前坑道里\x01",
            "在施工吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_160F")

    label("loc_15A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15DD")

    ChrTalk(    #58
        0x108,
        (
            "#072F听说之前坑道里\x01",
            "在施工吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_160F")

    label("loc_15DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_160F")

    ChrTalk(    #59
        0x106,
        (
            "#050F好像之前坑道里\x01",
            "在施工吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160F")


    ChrTalk(    #60
        0x8,
        (
            "嗯，是为了填补\x01",
            "那次塌方造成的坑洞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "虽然骨架已经弄好，\x01",
            "但稳固地基的工作还没完成。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1002F那次塌方所造成的坑洞……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1042F嗯，是我们上次来的时候发现的\x01",
            "那个魔兽巢穴吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        "嗯，就是那个坑洞。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "虽然老大他们后来马上\x01",
            "利用爆破将它填埋起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "不管怎么说也是与魔兽的巢穴\x01",
            "相连的危险场所啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "所以就准备\x01",
            "再好好地施工一番。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#1042F原来如此……\x02\x03",

            "所以就邀请利吉先生\x01",
            "过来警戒了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1015F不过在那个工程的\x01",
            "关键时刻却发生了导力停止现象。\x02\x03",

            "#1003F……希望没出什么事就好。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1848")

    ChrTalk(    #70
        0x106,
        (
            "#057F很麻烦呢……\x02\x03",

            "现在只能到下面\x01",
            "确认一下情况了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E3")

    label("loc_1848")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1891")

    ChrTalk(    #71
        0x108,
        (
            "#072F喔，有股危险的感觉。\x02\x03",

            "现在应该尽早\x01",
            "下去看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E3")

    label("loc_1891")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18E3")

    ChrTalk(    #72
        0x103,
        (
            "#022F我有一种不祥的预感……\x02\x03",

            "现在只能到下面\x01",
            "去确认一下情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E3")


    ChrTalk(    #73
        0x8,
        (
            "啊，当然希望\x01",
            "你们这么做……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "但是，你们准备\x01",
            "如何到下面去呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "最重要的是\x01",
            "升降机动不了了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x101,
        (
            "#1019F唔、唔……\x01",
            "说来也是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#1043F因为那也是用\x01",
            "导力器驱动的机械嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19F7")

    ChrTalk(    #78
        0x107,
        (
            "#064F请、请问……\x01",
            "有没有其它办法可以下去？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A5C")

    label("loc_19F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A2B")

    ChrTalk(    #79
        0x103,
        "#023F有没有其它手段可以下去？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A5C")

    label("loc_1A2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A5C")

    ChrTalk(    #80
        0x108,
        "#072F有没有其它可以下去的路？\x02",
    )

    CloseMessageWindow()

    label("loc_1A5C")


    ChrTalk(    #81
        0x8,
        (
            "你在说什么呢。\x01",
            "有的话我早就用了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AB0")

    ChrTalk(    #82
        0x107,
        (
            "#562F啊……\x01",
            "是、是啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AFB")

    label("loc_1AB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AD8")

    ChrTalk(    #83
        0x103,
        "#025F嗯，也是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFB")

    label("loc_1AD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AFB")

    ChrTalk(    #84
        0x108,
        "#073F啊，也是。\x02",
    )

    CloseMessageWindow()

    label("loc_1AFB")


    ChrTalk(    #85
        0x101,
        (
            "#1002F可就算这样\x01",
            "也不能放弃。\x02\x03",

            "因为现在矿工还在\x01",
            "地下等着我们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        (
            "#1043F是啊。\x01",
            "得想想办法……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        "不好意思，请你们想想办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "老大他们一定也在\x01",
            "等待着我们救援呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xCCCE, 0x0, 0xD7D2, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    OP_4B(0x8, 255)
    OP_65(0x0, 0x1)
    ClearChrFlags(0x8, 0x10)
    OP_A2(0x2087)
    OP_28(0xBF, 0x4, 0x2)
    OP_28(0xBF, 0x4, 0x8)
    OP_28(0xBF, 0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_9_137E end

    def Function_10_1BE9(): pass

    label("Function_10_1BE9")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #89
        "\x07\x05按了开关没反应。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(500)
    OP_6D(54080, 0, 55500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CE3")
    OP_D2(0x70065, 0x7006D, 0x7)
    SetChrPos(0x101, 54510, 0, 54700, 0)
    SetChrPos(0x107, 53490, 0, 54670, 0)
    SetChrPos(0x102, 54620, 0, 53520, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CCF")
    SetChrPos(0xF9, 53390, 0, 53520, 0)
    Jump("loc_1CE0")

    label("loc_1CCF")

    SetChrPos(0xF8, 53390, 0, 53520, 0)

    label("loc_1CE0")

    Jump("loc_1D27")

    label("loc_1CE3")

    SetChrPos(0x101, 54510, 0, 54700, 0)
    SetChrPos(0x102, 53490, 0, 54670, 0)
    SetChrPos(0xF8, 54620, 0, 53520, 0)
    SetChrPos(0xF9, 53390, 0, 53520, 0)

    label("loc_1D27")

    OP_0D()

    ChrTalk(    #90
        0x101,
        "#1026F#2P果然启动不了……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DAB")

    ChrTalk(    #91
        0x103,
        (
            "#022F升降机开关的\x01",
            "控制钥匙也插在上面。\x02\x03",

            "不会动是因为受了\x01",
            "导力停止现象的影响。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E7A")

    label("loc_1DAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E0F")

    ChrTalk(    #92
        0x106,
        (
            "#050F升降机开关的\x01",
            "控制钥匙也插在上面。\x02\x03",

            "不运作是因为受了\x01",
            "导力停止现象的影响。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E7A")

    label("loc_1E0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E7A")

    ChrTalk(    #93
        0x108,
        (
            "#072F升降机开关的\x01",
            "控制钥匙也插在上面。\x02\x03",

            "这么说动不了是因为受了\x01",
            "导力停止现象的影响了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30DC")

    ChrTalk(    #94
        0x107,
        "#062F#1P…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_1EB0():

        label("loc_1EB0")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_1EB0")

    QueueWorkItem2(0x101, 1, lambda_1EB0)
    Sleep(500)

    ChrTalk(    #95
        0x101,
        (
            "#1002F#2P嗯……？\x01",
            "提妲，怎么了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #96
        0x107,
        (
            "#060F#1P嗯、嗯……\x01",
            "我稍微想了一下……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #97
        0x107,
        (
            "#060F#1P那个，这部升降机是\x01",
            "驱动部件内置型的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    def lambda_1F5E():

        label("loc_1F5E")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_1F5E")

    QueueWorkItem2(0x8, 1, lambda_1F5E)
    Sleep(400)

    ChrTalk(    #98
        0x8,
        "哎…？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "啊、啊啊……\x01",
            "没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x107,
        "#064F#1P啊，果然……\x02",
    )

    CloseMessageWindow()

    def lambda_1FB3():
        OP_6D(54090, 50, 56090, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FB3)

    def lambda_1FCB():
        OP_6C(31000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FCB)
    OP_8E(0x107, 0xD23C, 0x32, 0xE150, 0x7D0, 0x0)
    OP_8C(0x107, 0, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #101
        0x107,
        (
            "#062F#5P嗯，控制钥匙的\x01",
            "插孔在这里……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x107, 7)
    OP_0D()

    ChrTalk(    #102
        0x107,
        (
            "#062F#5P……驱动导力器\x01",
            "正好在这附近吧？\x02\x03",

            "要是按照标准的设计，\x01",
            "我想大概是在这里……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_212B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20EA")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2128")

    label("loc_20EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2111")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2128")

    label("loc_2111")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2128")

    Jump("loc_2190")

    label("loc_212B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2152")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2190")

    label("loc_2152")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2179")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2190")

    label("loc_2179")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2190")

    Sleep(1000)

    ChrTalk(    #103
        0x101,
        "#1016F#2P唔、唔……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21D7")

    ChrTalk(    #104
        0x106,
        "#551F真是的，又来了。\x02",
    )

    CloseMessageWindow()

    label("loc_21D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2224")

    ChrTalk(    #105
        0x108,
        (
            "#071F哈哈，一看到机械\x01",
            "眼神就马上变了，\x01",
            "不愧是博士的孙女。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2224")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2262")

    ChrTalk(    #106
        0x103,
        (
            "#021F呵呵，这副认真的样子\x01",
            "不是挺可爱的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2262")


    ChrTalk(    #107
        0x8,
        (
            "#3P好、好像是个异常\x01",
            "熟悉机械的小鬼呢。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    OP_8C(0x107, 180, 400)

    ChrTalk(    #108
        0x107,
        (
            "#060F#5P嗯……\x01",
            "好像有办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1011F#2P有办法……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2313")

    ChrTalk(    #110
        0x103,
        (
            "#023F难道说你能让\x01",
            "这升降机动起来？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_237B")

    label("loc_2313")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2349")

    ChrTalk(    #111
        0x106,
        "#052F……难道说你能让它动起来？\x02",
    )

    CloseMessageWindow()
    Jump("loc_237B")

    label("loc_2349")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_237B")

    ChrTalk(    #112
        0x108,
        (
            "#073F哟，莫非\x01",
            "你能让它动起来？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_237B")


    ChrTalk(    #113
        0x107,
        (
            "#060F#5P……嗯，大概能。\x02\x03",

            "如果使用那个零力场发生器的话，\x01",
            "一定能动起来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#1004F#2P咦，用发生器？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x107,
        (
            "#560F#5P嗯，让发生器\x01",
            "尽可能地靠近驱动部。\x02\x03",

            "顺利的话应该能暂时使\x01",
            "停止现象的效果无效。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#1044F原来如此……\x01",
            "还有这一招啊。\x02\x03",

            "#1040F赶快试试吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_40(0x151, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_249E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_24B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24CE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_24CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_24E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24FE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_24FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2516")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2516")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2554")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_253C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_253C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2554")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2592")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_257A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_257A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2592")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2592")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_25B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25D0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_25D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_260B")

    ChrTalk(    #117
        0x107,
        (
            "#560F#5P嗯、嗯！\x01",
            "试试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_260B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26E0")

    ChrTalk(    #118
        0x101,
        (
            "#1006F#2P这样的话\x01",
            "首先需要有发生器呢。\x02\x03",

            "嗯，先借一个给你。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #119
        "\x1F\x51\x01\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #120
        0x107,
        (
            "#560F#5P嗯……\x01",
            "谢谢姐姐。\x02\x03",

            "那么试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_26E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27C8")

    ChrTalk(    #121
        0x107,
        "#560F#5P嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1015F这样的话\x01",
            "首先需要有发生器呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        "#1040F那就把我的借你吧。\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #124
        "\x1F\x51\x01\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #125
        0x107,
        (
            "#560F#5P嗯……\x01",
            "谢谢哥哥。\x02\x03",

            "那么试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_27C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28BF")

    ChrTalk(    #126
        0x107,
        "#560F#5P嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1015F#2P这样的话\x01",
            "首先需要有发生器呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        "#020F那就把我的借你吧。\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #129
        "\x1F\x51\x01\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #130
        0x107,
        (
            "#560F#5P嗯……\x01",
            "谢谢雪拉姐。\x02\x03",

            "那么试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_28BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29BF")

    ChrTalk(    #131
        0x107,
        "#560F#5P嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1015F#2P这样的话\x01",
            "首先需要有发生器呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x106,
        (
            "#051F那就先把\x01",
            "我的借给你吧。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #134
        "\x1F\x51\x01\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #135
        0x107,
        (
            "#560F#5P嗯……\x01",
            "谢谢阿加特哥哥。\x02\x03",

            "那么试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_29BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AAF")

    ChrTalk(    #136
        0x107,
        "#560F#5P嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        (
            "#1015F#2P这样的话\x01",
            "首先需要有发生器呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x108,
        "#070F把我的借你吧。\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #139
        "\x1F\x51\x01\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #140
        0x107,
        (
            "#560F#5P嗯……\x01",
            "谢谢金先生。\x02\x03",

            "那么试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAF")

    WaitChrThread(0x101, 0x2)
    OP_8C(0x107, 0, 400)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #141
        (
            "\x07\x05提妲将零力场发生器\x01",
            "按在了升降机的操作盘上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)
    LoadEffect(0x1, "map\\\\mp007_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 54000, 800, 58200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x90, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #142
        0x8,
        "哇、哇！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1020F#2P啊……\x02\x03",

            "这、这道亮光……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BEA")

    ChrTalk(    #144
        0x103,
        "#023F和福音一样的光……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_2BEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C1E")

    ChrTalk(    #145
        0x106,
        "#052F和那个福音一样的光呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C4B")

    label("loc_2C1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C4B")

    ChrTalk(    #146
        0x108,
        "#072F和福音一样的光啊……\x02",
    )

    CloseMessageWindow()

    label("loc_2C4B")


    ChrTalk(    #147
        0x102,
        "#1042F……似乎正在发生干涉呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x107,
        "#062F…………………………\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    OP_23(0x90)
    Sleep(500)

    ChrTalk(    #149
        0x8,
        "消、消失了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x107,
        (
            "#561F呼……\x02\x03",

            "这样一来\x01",
            "大概就行了吧……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x5)
    OP_73(0x1)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D48")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D86")

    label("loc_2D48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D6F")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D86")

    label("loc_2D6F")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2D86")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB2")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2DF0")

    label("loc_2DB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DD9")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2DF0")

    label("loc_2DD9")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2DF0")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #151
        0x107,
        "#065F啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1004F#2P动、动了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x102,
        (
            "#1042F内部导力器的\x01",
            "导力好像恢复了。\x02\x03",

            "赶快上升降机吧。\x01",
            "要下去就趁现在。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EAD")

    ChrTalk(    #154
        0x103,
        "#525F呵呵，干得不错嘛㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EFE")

    label("loc_2EAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EE1")

    ChrTalk(    #155
        0x106,
        "#051F嘿嘿，是小不点的功劳呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EFE")

    label("loc_2EE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EFE")

    ChrTalk(    #156
        0x108,
        "#072F嗯！\x02",
    )

    CloseMessageWindow()

    label("loc_2EFE")


    def lambda_2F04():
        OP_6D(54080, 50, 56970, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F04)

    def lambda_2F1C():
        OP_8E(0xFE, 0xD4EE, 0x0, 0xE164, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F1C)
    Sleep(100)

    def lambda_2F3C():
        OP_8E(0xFE, 0xD55C, 0x0, 0xDCC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F3C)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F7A")
    OP_8E(0xF9, 0xD08E, 0x0, 0xDCC8, 0x1388, 0x0)
    Jump("loc_2F8E")

    label("loc_2F7A")

    OP_8E(0xF8, 0xD08E, 0x0, 0xDCC8, 0x1388, 0x0)

    label("loc_2F8E")


    ChrTalk(    #157 op#A
        0x8,
        "#18A我、我也跟着去！\x02",
    )

    CloseMessageWindow()

    def lambda_2FAD():

        label("loc_2FAD")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2FAD")

    QueueWorkItem2(0x102, 1, lambda_2FAD)
    Sleep(100)

    def lambda_2FC3():

        label("loc_2FC3")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2FC3")

    QueueWorkItem2(0x101, 1, lambda_2FC3)
    Sleep(100)

    def lambda_2FD9():

        label("loc_2FD9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2FD9")

    QueueWorkItem2(0xF8, 1, lambda_2FD9)

    def lambda_2FEA():

        label("loc_2FEA")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2FEA")

    QueueWorkItem2(0xF9, 1, lambda_2FEA)

    ChrTalk(    #158 op#A
        0x102,
        "#1046F#7A快点！\x02",
    )

    CloseMessageWindow()
    SetChrBattleFlags(0x8, 0x20)

    def lambda_3015():
        OP_8E(0xFE, 0xD25A, 0x32, 0xD840, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3015)

    def lambda_3030():
        OP_8F(0xFE, 0xD55C, 0x0, 0xDDF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3030)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3075")

    def lambda_305D():
        OP_8F(0xFE, 0xD08E, 0x0, 0xDDF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_305D)
    Jump("loc_3090")

    label("loc_3075")


    def lambda_307B():
        OP_8F(0xFE, 0xD08E, 0x0, 0xDDF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_307B)

    label("loc_3090")

    WaitChrThread(0x8, 0x1)
    OP_8E(0x8, 0xD25A, 0x0, 0xDC28, 0x1388, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_8C(0x107, 0, 800)

    ChrTalk(    #159
        0x107,
        "#062F那、那就去了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DA8")

    label("loc_30DC")


    ChrTalk(    #160
        0x102,
        "#1043F#1P…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_3105():

        label("loc_3105")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_3105")

    QueueWorkItem2(0x101, 1, lambda_3105)
    Sleep(500)

    ChrTalk(    #161
        0x101,
        "#1002F#2P约修亚，你怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #162
        0x102,
        (
            "#1040F#1P嗯，我注意到……\x02\x03",

            "一点事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        "#1011F#2P注意到什么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #164
        0x102,
        (
            "#1040F#1P这升降机是\x01",
            "驱动部件内置型的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    def lambda_31C4():

        label("loc_31C4")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_31C4")

    QueueWorkItem2(0x8, 1, lambda_31C4)
    Sleep(400)

    ChrTalk(    #165
        0x8,
        "哎…？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "啊、啊啊……\x01",
            "没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x102,
        "#1035F#1P原来如此……\x02",
    )

    CloseMessageWindow()

    def lambda_321A():
        OP_6D(54090, 50, 56090, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_321A)

    def lambda_3232():
        OP_6C(31000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3232)
    OP_8E(0x102, 0xD23C, 0x32, 0xE150, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #168
        0x102,
        (
            "#1043F#5P控制钥匙的插孔在这里……\x02\x03",

            "……就是说，用来驱动的\x01",
            "导力器就在它下面吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32D9")

    ChrTalk(    #169
        0x106,
        "#052F想到什么好办法了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3343")

    label("loc_32D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3316")

    ChrTalk(    #170
        0x103,
        (
            "#027F呵呵，莫非你想到什么\x01",
            "好办法了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3343")

    label("loc_3316")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3343")

    ChrTalk(    #171
        0x108,
        "#073F想到什么好办法了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_3343")

    OP_8C(0x102, 180, 400)
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_40(0x151, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_336C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_336C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3384")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_3384")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_339C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_33B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33DA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_33DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33F2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_33F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3430")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3418")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_3418")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3430")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_3430")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_346E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3456")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_3456")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_346E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_346E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34E9")

    ChrTalk(    #172
        0x102,
        (
            "#1043F#1P还不能确定……\x01",
            "不过我觉得有必要试一试。\x02\x03",

            "如果使用零力场发生器的话\x01",
            "可能会有办法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A1")

    label("loc_34E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35ED")

    ChrTalk(    #173
        0x102,
        (
            "#1043F#1P还不能确定……\x01",
            "不过我觉得有必要试一试。\x02\x03",

            "#1040F艾丝蒂尔。\x01",
            "能不能把你的零力场发生器借给我？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1011F#2P发生器？\x02\x03",

            "#1015F嗯、嗯，这倒没问题……\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #175
        "\x1F\x51\x01\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_37A1")

    label("loc_35ED")


    ChrTalk(    #176
        0x102,
        (
            "#1040F#1P不过我觉得有必要试一试\x02\x03",

            "#1040F#1P不好意思，\x01",
            "能不能把你的零力场发生器借给我？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3698")

    ChrTalk(    #177
        0x103,
        (
            "#020F#6P零力场发生器\x01",
            "我倒是有一个。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3747")

    label("loc_3698")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36F1")

    ChrTalk(    #178
        0x106,
        (
            "#051F#6P老爷爷给的那东西吗。\x02\x03",

            "我倒是有一个。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3747")

    label("loc_36F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3747")

    ChrTalk(    #179
        0x108,
        (
            "#070F#6P博士给的那个装置啊。\x02\x03",

            "我正好有一个。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3747")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #180
        "\x1F\x51\x01\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #181
        0x102,
        "#1040F请借我用一下。\x02",
    )

    CloseMessageWindow()

    label("loc_37A1")


    ChrTalk(    #182
        0x101,
        (
            "#1002F#2P那你准备用这个\x01",
            "发生器做什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x102,
        "#1040F#1P你很快就会知道的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #184
        (
            "\x07\x05约修亚把零力场发生器\x01",
            "按在升降机的操作盘上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)
    LoadEffect(0x1, "map\\\\mp007_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 54000, 800, 58200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x90, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #185
        0x8,
        "哇、哇！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1020F#2P啊……\x02\x03",

            "这、这道亮光……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3924")

    ChrTalk(    #187
        0x103,
        "#023F和福音一样的光……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3985")

    label("loc_3924")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3958")

    ChrTalk(    #188
        0x106,
        "#052F和那个福音一样的光呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3985")

    label("loc_3958")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3985")

    ChrTalk(    #189
        0x108,
        "#072F和福音一样的光啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3985")


    ChrTalk(    #190
        0x102,
        (
            "#1042F没关系……\x01",
            "只是导力波在进行干涉而已。\x02\x03",

            "如果我的想法正确，\x01",
            "这样一来导力就能暂时恢复了……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    OP_23(0x90)
    Sleep(500)

    ChrTalk(    #191
        0x8,
        "消、消失了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x102,
        "#1042F………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x5)
    OP_73(0x1)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A9B")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3AD9")

    label("loc_3A9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC2")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3AD9")

    label("loc_3AC2")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3AD9")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B05")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3B43")

    label("loc_3B05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2C")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3B43")

    label("loc_3B2C")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3B43")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #193
        0x101,
        "#1004F#2P动、动了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x102,
        "#1042F好……导力恢复了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 800)

    ChrTalk(    #195
        0x102,
        (
            "#1046F赶快上升降机吧！\x01",
            "要下去就趁现在。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BF5")

    ChrTalk(    #196
        0x103,
        "#525F呵呵，干得不错嘛㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C32")

    label("loc_3BF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C15")

    ChrTalk(    #197
        0x106,
        "#051F嗯！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C32")

    label("loc_3C15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C32")

    ChrTalk(    #198
        0x108,
        "#072F嗯！\x02",
    )

    CloseMessageWindow()

    label("loc_3C32")


    def lambda_3C38():
        OP_6D(54080, 50, 56970, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C38)

    def lambda_3C50():
        OP_8E(0xFE, 0xD4EE, 0x0, 0xE164, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C50)
    Sleep(100)

    def lambda_3C70():
        OP_8E(0xFE, 0xD55C, 0x0, 0xDCC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3C70)
    Sleep(100)
    OP_8E(0xF9, 0xD08E, 0x0, 0xDCC8, 0x1388, 0x0)

    ChrTalk(    #199 op#A
        0x8,
        "#18A我、我也跟着去！\x02",
    )

    CloseMessageWindow()

    def lambda_3CBD():

        label("loc_3CBD")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3CBD")

    QueueWorkItem2(0x101, 1, lambda_3CBD)
    Sleep(100)

    def lambda_3CD3():

        label("loc_3CD3")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3CD3")

    QueueWorkItem2(0xF8, 1, lambda_3CD3)

    def lambda_3CE4():

        label("loc_3CE4")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3CE4")

    QueueWorkItem2(0xF9, 1, lambda_3CE4)

    ChrTalk(    #200 op#A
        0x101,
        "#1005F#2P#9A大叔冲刺！\x02",
    )

    CloseMessageWindow()
    SetChrBattleFlags(0x8, 0x20)

    def lambda_3D16():
        OP_8E(0xFE, 0xD25A, 0x32, 0xD840, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D16)

    def lambda_3D31():
        OP_8F(0xFE, 0xD55C, 0x0, 0xDDF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_3D31)
    Sleep(200)

    def lambda_3D51():
        OP_8F(0xFE, 0xD08E, 0x0, 0xDDF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_3D51)
    WaitChrThread(0x8, 0x1)
    OP_8E(0x8, 0xD25A, 0x0, 0xDC28, 0x1388, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_8C(0x102, 0, 800)

    ChrTalk(    #201
        0x102,
        "#1046F开始下降！\x02",
    )

    CloseMessageWindow()

    label("loc_3DA8")

    Call(0, 11)
    Return()

    # Function_10_1BE9 end

    def Function_11_3DAD(): pass

    label("Function_11_3DAD")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 5)
    OP_70(0x1, 0xF)
    OP_73(0x1)

    ChrTalk(    #202 op#A op#5
        0x101,
        "#1004F#4A#5P哇哇！？\x05\x02",
    )

    CloseMessageWindow()
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 15)
    OP_70(0x1, 0x19)
    OP_73(0x1)

    ChrTalk(    #203 op#A op#5
        0x101,
        "#1004F#12A#5P哇、哇、哇、哇……\x05\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 25)
    OP_70(0x1, 0x23)
    OP_73(0x1)
    Sleep(200)
    OP_0D()
    OP_6D(129000, 0, 76700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6F(0x2, 360)
    OP_6F(0x2, 280)
    OP_48()
    SetChrBattleFlags(0x8, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F43")
    OP_89(0x101, 129600, 15000, 77700, 180)
    OP_89(0x107, 128919, 15000, 77680, 0)
    OP_89(0x102, 129720, 15000, 76820, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2F")
    OP_89(0xF9, 128320, 15000, 76820, 180)
    Jump("loc_3F40")

    label("loc_3F2F")

    OP_89(0xF8, 128320, 15000, 76820, 180)

    label("loc_3F40")

    Jump("loc_3F87")

    label("loc_3F43")

    OP_89(0x101, 129600, 15000, 77700, 180)
    OP_89(0x102, 128919, 15000, 77680, 0)
    OP_89(0xF8, 129720, 15000, 76820, 180)
    OP_89(0xF9, 128320, 15000, 76820, 180)

    label("loc_3F87")

    OP_89(0x8, 128949, 15000, 76360, 180)
    LoadEffect(0x1, "Craft\\\\cr162_02.eff")
    LoadEffect(0x2, "Craft\\\\cr162_00.eff")
    LoadEffect(0x3, "Craft\\\\cr161_00.eff")
    LoadEffect(0x4, "scraft\\\\sc000_11.eff")
    OP_D2(0x90003, 0x90007, 0x7)
    OP_D2(0x270130, 0x270140, 0x8)
    OP_D2(0x270139, 0x270149, 0x9)
    FadeToBright(1000, 0)
    Sleep(400)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x2, 280)
    OP_70(0x2, 0x10E)
    OP_73(0x2)
    Sleep(400)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x2, 270)
    OP_70(0x2, 0x104)
    OP_73(0x2)
    Sleep(400)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x2, 260)
    OP_70(0x2, 0xFA)
    OP_73(0x2)
    Sleep(400)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x2, 250)
    OP_70(0x2, 0xF0)
    OP_73(0x2)
    OP_23(0x68)
    Sleep(1000)

    ChrTalk(    #204
        0x102,
        "#1035F呼……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_410D")

    ChrTalk(    #205
        0x103,
        "#025F啊，差点咬到舌头。\x02",
    )

    CloseMessageWindow()

    label("loc_410D")


    ChrTalk(    #206
        0x101,
        (
            "#1019F为、为什么晃得\x01",
            "这么厉害啊……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4175")

    ChrTalk(    #207
        0x107,
        (
            "#067F嘿嘿，因为导力器的\x01",
            "输出完全不够……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4237")

    label("loc_4175")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41CD")

    ChrTalk(    #208
        0x108,
        (
            "#070F大概是因为导力器的\x01",
            "导力不充足吧。\x02\x03",

            "总之先下去\x01",
            "确认一下状况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4237")

    label("loc_41CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4237")

    ChrTalk(    #209
        0x106,
        (
            "#552F导力器的马力\x01",
            "好像不够……\x02\x03",

            "#053F反正现在情况这么紧急，\x01",
            "就别抱怨升降机舒不舒服了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4237")


    def lambda_423D():
        OP_6D(129479, 150, 73430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_423D)

    def lambda_4255():
        OP_8E(0xFE, 0x1F7E8, 0x3C, 0x119B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4255)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_431F")

    def lambda_4283():
        OP_8E(0xFE, 0x1FA0E, 0x0, 0x12304, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4283)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42C8")

    def lambda_42B0():
        OP_8E(0xFE, 0x1F612, 0x0, 0x12304, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_42B0)
    Jump("loc_42E3")

    label("loc_42C8")


    def lambda_42CE():
        OP_8E(0xFE, 0x1F612, 0x0, 0x12304, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_42CE)

    label("loc_42E3")

    Sleep(100)

    def lambda_42EE():
        OP_8E(0xFE, 0x1FA0E, 0x0, 0x126EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42EE)
    Sleep(50)
    OP_8E(0x107, 0x1F612, 0x0, 0x126EC, 0x7D0, 0x0)
    Jump("loc_4393")

    label("loc_431F")


    def lambda_4325():
        OP_8E(0xFE, 0x1FA0E, 0x0, 0x12304, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4325)
    Sleep(100)

    def lambda_4345():
        OP_8E(0xFE, 0x1F612, 0x0, 0x12304, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4345)
    Sleep(100)

    def lambda_4365():
        OP_8E(0xFE, 0x1FA0E, 0x0, 0x126EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4365)
    Sleep(50)
    OP_8E(0x102, 0x1F612, 0x0, 0x126EC, 0x7D0, 0x0)

    label("loc_4393")

    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x8, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x8, 45, 400)
    Sleep(500)

    ChrTalk(    #210
        0x8,
        (
            "噢，还有\x01",
            "灯光呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    def lambda_43E9():

        label("loc_43E9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_43E9")

    QueueWorkItem2(0x101, 1, lambda_43E9)

    def lambda_43FA():

        label("loc_43FA")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_43FA")

    QueueWorkItem2(0x102, 1, lambda_43FA)

    def lambda_440B():

        label("loc_440B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_440B")

    QueueWorkItem2(0xF8, 1, lambda_440B)

    def lambda_441C():

        label("loc_441C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_441C")

    QueueWorkItem2(0xF9, 1, lambda_441C)

    def lambda_442D():
        OP_6D(127060, 0, 73010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_442D)
    OP_8E(0x8, 0x1E938, 0x0, 0x11940, 0x7D0, 0x0)
    OP_8C(0x8, 225, 400)
    Sleep(500)

    ChrTalk(    #211
        0x8,
        "……坑道那边好安静啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x8,
        (
            "说不定是我们\x01",
            "多虑了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #213
        0x8,
        "……咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x102,
        "#1044F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x8,
        "啊，好像有人过来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x8,
        (
            "哟，我还以为是谁呢。\x01",
            "那不是提恩特吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x8,
        (
            "喂～提恩特！\x01",
            "你在那儿干吗？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, 120370, 0, 67550, 90)

    def lambda_455D():

        label("loc_455D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_455D")

    QueueWorkItem2(0x8, 1, lambda_455D)

    def lambda_456E():

        label("loc_456E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_456E")

    QueueWorkItem2(0x101, 1, lambda_456E)

    def lambda_457F():

        label("loc_457F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_457F")

    QueueWorkItem2(0x102, 1, lambda_457F)

    def lambda_4590():

        label("loc_4590")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4590")

    QueueWorkItem2(0xF8, 1, lambda_4590)

    def lambda_45A1():

        label("loc_45A1")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_45A1")

    QueueWorkItem2(0xF9, 1, lambda_45A1)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x9, 0x1EB54, 0x0, 0x11602, 0x1770, 0x0)

    def lambda_45D8():
        OP_6D(129380, 60, 72150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_45D8)
    OP_8E(0x9, 0x203AA, 0x0, 0x11698, 0x1770, 0x0)
    OP_8C(0x9, 270, 400)
    WaitChrThread(0x101, 0x2)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)

    ChrTalk(    #218
        0x8,
        (
            "喂、喂……\x01",
            "你着急什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x9,
        "后、后面……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x8,
        "……啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x9,
        "我、我都说了在后面！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x10, 121610, 0, 69620, 45)
    SetChrPos(0x11, 118640, 0, 68820, 45)
    SetChrPos(0x12, 118570, 0, 67630, 45)
    SetChrPos(0x13, 119440, 0, 66840, 45)
    SetChrPos(0x14, 120720, 0, 67050, 45)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_59()
    Fade(1000)
    OP_6D(121150, 0, 69600, 0)
    OP_6C(270000, 0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x8, 0x1)
    SetChrPos(0x8, 123930, 0, 71340, 0)
    TurnDirection(0x8, 0x9, 0)
    OP_0D()

    def lambda_4768():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4768)
    Sleep(100)

    def lambda_4783():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4783)

    def lambda_4799():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4799)
    Sleep(100)

    def lambda_47B4():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_47B4)

    def lambda_47CA():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_47CA)

    def lambda_47E0():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_47E0)
    OP_8C(0x8, 235, 400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_4842():
        OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4842)

    ChrTalk(    #222
        0x8,
        "哇、哇哇！！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x102, 3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0x102, 123030, 3000, 70820, 235)
    PlayEffect(0x1, 0x0, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    OP_83(0x0, 0x2)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(300)
    PlayEffect(0x3, 0xFF, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4A(0x10, 0)
    SetChrChipByIndex(0x10, 7)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x40)

    def lambda_496A():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_496A)
    OP_8F(0x10, 0x1D9AC, 0x0, 0x10E46, 0x1B58, 0x0)
    SetChrChipByIndex(0x10, 2)
    ClearChrFlags(0x10, 0x20)
    OP_4B(0x10, 0)
    OP_96(0x102, 0x1E168, 0x0, 0x1149A, 0x1F4, 0x1388)
    SetChrFlags(0x8, 0x40)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x8, 0x1F25C, 0x0, 0x125D4, 0xFA0, 0x0)

    def lambda_49E8():
        OP_8E(0xFE, 0x1FAFD, 0x0, 0x125C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_49E8)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)

    def lambda_4A12():
        OP_6D(122730, 0, 70630, 2000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4A12)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0xE)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0xF)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A82")

    ChrTalk(    #223
        0x106,
        "#057F切，还真的有魔兽。\x02",
    )

    CloseMessageWindow()

    label("loc_4A82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AAE")

    ChrTalk(    #224
        0x107,
        (
            "#065F啊……\x01",
            "这、这么多。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AE1")

    ChrTalk(    #225
        0x108,
        "#070F哈哈，好热烈的欢迎仪式啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4AE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B25")

    ChrTalk(    #226
        0x103,
        (
            "#025F唔，是甲壳魔兽啊……\x01",
            "这些家伙又硬又难对付。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B25")


    ChrTalk(    #227
        0x101,
        "#1002F#2P不会吧，莫非那魔兽的巢穴……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x102,
        (
            "#1042F#1P大概吧……\x02\x03",

            "不过看来是\x01",
            "没有时间考虑了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 3)

    def lambda_4B93():
        OP_94(0x1, 0xFE, 0x0, 0x6A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4B93)
    Sleep(30)
    SetChrChipByIndex(0x11, 3)
    SetChrChipByIndex(0x14, 3)

    def lambda_4BB8():
        OP_94(0x1, 0xFE, 0x0, 0x6A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4BB8)

    def lambda_4BCE():
        OP_94(0x1, 0xFE, 0x0, 0x6A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4BCE)
    Sleep(30)
    SetChrChipByIndex(0x12, 3)
    SetChrChipByIndex(0x13, 3)

    def lambda_4BF3():
        OP_94(0x1, 0xFE, 0x0, 0x6A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4BF3)

    def lambda_4C09():
        OP_94(0x1, 0xFE, 0x0, 0x6A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4C09)
    WaitChrThread(0x10, 0x1)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    Battle(0x57, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4C5B"),
        (SWITCH_DEFAULT, "loc_4C60"),
    )


    label("loc_4C5B")

    OP_B4(0x0)
    Jump("loc_4C60")

    label("loc_4C60")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Call(0, 16)
    Return()

    # Function_11_3DAD end

    def Function_12_4C7E(): pass

    label("Function_12_4C7E")

    OP_99(0xFE, 0x3, 0xB, 0x7D0)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_4C7E end

    def Function_13_4C92(): pass

    label("Function_13_4C92")

    SetChrPos(0xFE, 126140, 0, 74760, 225)
    OP_8E(0xFE, 0x1E0E6, 0x0, 0x11936, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_13_4C92 end

    def Function_14_4CBF(): pass

    label("Function_14_4CBF")

    SetChrPos(0xFE, 128370, 0, 74230, 225)
    OP_8E(0xFE, 0x1E672, 0x0, 0x112EC, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_14_4CBF end

    def Function_15_4CEC(): pass

    label("Function_15_4CEC")

    SetChrPos(0xFE, 128690, 0, 75630, 225)
    OP_8E(0xFE, 0x1E708, 0x0, 0x117BA, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_15_4CEC end

    def Function_16_4D19(): pass

    label("Function_16_4D19")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_6D(123290, 0, 71580, 0)
    OP_67(0, 7880, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 123110, 0, 71990, 225)
    SetChrPos(0x102, 123240, 0, 70810, 225)
    SetChrPos(0xF8, 124530, 0, 70380, 225)
    SetChrPos(0xF9, 124680, 0, 71610, 225)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    SetChrPos(0x8, 132100, 0, 74120, 225)
    SetChrPos(0x9, 132170, 0, 72480, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #229
        0x101,
        "#1002F总算是击退了……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E50")

    ChrTalk(    #230
        0x103,
        "#025F呼，想不到这么难对付。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EB7")

    label("loc_4E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E80")

    ChrTalk(    #231
        0x106,
        "#050F比我想象中的要厉害。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EB7")

    label("loc_4E80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EB7")

    ChrTalk(    #232
        0x108,
        "#075F呼，对这种魔兽可不能掉以轻心。\x02",
    )

    CloseMessageWindow()

    label("loc_4EB7")


    ChrTalk(    #233
        0x102,
        "#1035F嗯，是不能大意啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x8,
        "#5P喂、喂……游击士朋友。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x9,
        "#5P我、我能出来了吗？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #236
        0x101,
        "#1011F啊，嗯，没事了。\x02",
    )

    CloseMessageWindow()
    OP_59()
    SetChrPos(0x9, 131020, 0, 71030, 270)
    SetChrPos(0x8, 130449, 220, 72720, 270)

    def lambda_4F65():
        OP_6D(124320, 0, 71010, 1500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4F65)

    def lambda_4F7D():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_4F7D)

    def lambda_4F8D():
        OP_8E(0xFE, 0x1EC8A, 0x0, 0x115B2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4F8D)

    def lambda_4FA8():
        OP_8E(0xFE, 0x1ECB2, 0x0, 0x11A08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4FA8)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)

    def lambda_4FCD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4FCD)

    def lambda_4FDB():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4FDB)
    Sleep(100)
    SetChrChipByIndex(0x102, 65535)

    def lambda_4FF3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4FF3)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #237
        0x9,
        "呼～谢谢，总算得救了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x9,
        (
            "多亏了你们，\x01",
            "我又能活着回家吃饭了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #239
        0x8,
        (
            "#2P喂，笨蛋。\x01",
            "还在说这种悠闲的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x8,
        (
            "#2P老大他们怎么样了？\x01",
            "先告诉我们这件事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1002F嗯，总之现在\x01",
            "首先要掌握情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x102,
        "#1042F#1P是发生事故了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x9,
        "嗯、嗯……是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x9,
        (
            "在昨天的施工中，驱赶魔兽的\x01",
            "导力灯不亮了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x9,
        (
            "无可奈何之下，只能暂停施工\x01",
            "在这里待命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x9,
        (
            "然后今天早上现场就\x01",
            "出现了大群魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x9,
        (
            "啊……我、我差点\x01",
            "就被吃掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#1002F你等一下。\x02\x03",

            "应该有一个从协会\x01",
            "过来的游击士在这里吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x9,
        "啊、啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x9,
        (
            "那位小哥为我们逃跑\x01",
            "争取了时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x9,
        (
            "不过，最后那个人也\x01",
            "被、被魔兽群包围了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52AB")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_52E9")

    label("loc_52AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52D2")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_52E9")

    label("loc_52D2")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_52E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5310")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_534E")

    label("loc_5310")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5337")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_534E")

    label("loc_5337")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_534E")

    Sleep(800)

    ChrTalk(    #252
        0x101,
        "#1020F！！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_538E")

    ChrTalk(    #253
        0x107,
        "#065F怎、怎么会……！？\x02",
    )

    CloseMessageWindow()

    label("loc_538E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53B5")

    ChrTalk(    #254
        0x103,
        "#023F难道利吉他！？\x02",
    )

    CloseMessageWindow()

    label("loc_53B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53E6")

    ChrTalk(    #255
        0x108,
        "#072F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_53E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5409")

    ChrTalk(    #256
        0x106,
        "#057F麻烦了……\x02",
    )

    CloseMessageWindow()

    label("loc_5409")


    ChrTalk(    #257
        0x102,
        "#1042F……要立即采取行动了呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_547D")

    ChrTalk(    #258
        0x103,
        (
            "#022F总之现在首先\x01",
            "要营救矿工们。\x02\x03",

            "等完成之后\x01",
            "再去救利吉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5526")

    label("loc_547D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54D3")

    ChrTalk(    #259
        0x108,
        (
            "#072F呼，总之我们\x01",
            "先快点去救矿工们。\x02\x03",

            "等完成之后\x01",
            "再去救游击士。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5526")

    label("loc_54D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5526")

    ChrTalk(    #260
        0x106,
        (
            "#057F总之营救矿工\x01",
            "必须要摆在第一位。\x02\x03",

            "等完成之后\x01",
            "再去救游击士。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5526")


    ChrTalk(    #261
        0x101,
        (
            "#1003F……嗯，明白了。\x02\x03",

            "虽然很担心，不过\x01",
            "这也是我们的使命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x9,
        (
            "我、我因为肚子饿\x01",
            "就飞跑出来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x9,
        (
            "老大他们一定还\x01",
            "躲在什么地方。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55DF")

    ChrTalk(    #264
        0x108,
        "#072F这里一共有多少人？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5630")

    label("loc_55DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5609")

    ChrTalk(    #265
        0x106,
        "#052F一共有多少人？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5630")

    label("loc_5609")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5630")

    ChrTalk(    #266
        0x103,
        "#022F一共有多少人？\x02",
    )

    CloseMessageWindow()

    label("loc_5630")

    OP_8C(0x8, 270, 400)

    ChrTalk(    #267
        0x8,
        "#2P应该还有４个人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x8,
        (
            "#2P算上游击士兄弟的话\x01",
            "还有５个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#1002F明白了。\x02\x03",

            "马上开始搜索吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        "#1042F嗯，要赶快！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x9,
        "快、快点回来啊。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    SetChrPos(0x8, 132100, 0, 74120, 225)
    SetChrPos(0x9, 132170, 0, 72480, 270)
    OP_6D(123230, 0, 71000, 0)
    SetChrPos(0x0, 123230, 0, 71000, 270)
    SetChrPos(0x1, 123230, 0, 71000, 270)
    SetChrPos(0x2, 123230, 0, 71000, 270)
    SetChrPos(0x3, 123230, 0, 71000, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2088)
    OP_28(0xBF, 0x1, 0x2)
    OP_28(0xBF, 0x1, 0x4)
    OP_28(0xBF, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_16_4D19 end

    def Function_17_577D(): pass

    label("Function_17_577D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_578A")
    Return()

    label("loc_578A")

    EventBegin(0x0)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    SetChrPos(0xA, 130610, 1000, 14190, 180)
    SetChrPos(0xB, 130610, 1000, 12770, 0)

    def lambda_57BC():
        OP_6D(130580, 1000, 13440, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57BC)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #272
        0xA,
        (
            "#1S啊，女神爱德丝啊……\x01",
            "请伸出援手拯救我们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xB,
        "#1S嘘，安静！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xB,
        (
            "#1S你在嘀咕些什么啊。\x01",
            "魔兽会跑过来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xA,
        (
            "#1S是吗？上回塌方的时候\x01",
            "也是像这样子祈祷才得救的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xA,
        (
            "#1S你也多少要保留一点\x01",
            "信仰心如何？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x2089)
    EventEnd(0x1)
    Return()

    # Function_17_577D end

    def Function_18_58C6(): pass

    label("Function_18_58C6")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(130139, 1000, 12840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    SetChrFlags(0x1E, 0x80)
    AddParty(0x48, 0xFF, 0xFF)
    AddParty(0x49, 0xFF, 0xFF)
    SetChrFlags(0x149, 0x80)
    SetChrFlags(0x14A, 0x80)
    SetChrPos(0x101, 129190, 1000, 12210, 90)
    SetChrPos(0x102, 128000, 1000, 11480, 90)
    SetChrPos(0xF8, 129220, 1000, 13440, 90)
    SetChrPos(0xF9, 127720, 1000, 13010, 90)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_8C(0xA, 270, 0)
    OP_8C(0xB, 270, 0)
    OP_0D()

    ChrTalk(    #277
        0xB,
        "你、你们是！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x102,
        (
            "#1042F#2P我们是游击士协会的人。\x01",
            "是来营救各位的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x101,
        "#1002F两位有没有受伤？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xB,
        "嗯、嗯……起码现在还好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xA,
        "啊，女神啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A6D")

    ChrTalk(    #282
        0x108,
        (
            "#072F有坚定的信仰是好事情，\x01",
            "不过要感谢还为时尚早。\x02\x03",

            "现在要尽快\x01",
            "逃出这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF9")

    label("loc_5A6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ABA")

    ChrTalk(    #283
        0x106,
        (
            "#050F喂喂，要感谢女神\x01",
            "还为时尚早。\x02\x03",

            "现在要先离开此地。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF9")

    label("loc_5ABA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AF9")

    ChrTalk(    #284
        0x103,
        (
            "#022F现在祈祷还早了点哦。\x02\x03",

            "首先要逃出这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AF9")

    OP_59()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x102, 315, 400)
    SetChrChipByIndex(0x102, 12)
    SetChrSubChip(0x102, 0)
    OP_22(0xD5, 0x0, 0x64)

    ChrTalk(    #285
        0x102,
        (
            "#1042F#2P确实……\x01",
            "稍微早了一点呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)

    def lambda_5B64():
        OP_6D(127130, 1000, 12140, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5B64)
    OP_43(0x10, 0x1, 0x0, 0x13)
    Sleep(200)

    def lambda_5B88():

        label("loc_5B88")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_5B88")

    QueueWorkItem2(0x101, 1, lambda_5B88)

    def lambda_5B99():

        label("loc_5B99")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_5B99")

    QueueWorkItem2(0x102, 1, lambda_5B99)

    def lambda_5BAA():

        label("loc_5BAA")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_5BAA")

    QueueWorkItem2(0xF8, 1, lambda_5BAA)

    def lambda_5BBB():

        label("loc_5BBB")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_5BBB")

    QueueWorkItem2(0xF9, 1, lambda_5BBB)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(200)
    OP_43(0x11, 0x1, 0x0, 0x14)
    Sleep(400)
    OP_43(0x12, 0x1, 0x0, 0x15)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_5C32():
        OP_94(0x1, 0xFE, 0xBE, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5C32)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_5C5F():
        OP_94(0x1, 0xFE, 0xAA, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5C5F)

    ChrTalk(    #286
        0xB,
        "哇、哇哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xA,
        "女神啊，请大发慈悲！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CC5")

    ChrTalk(    #288
        0x103,
        "#024F过来了！小心！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D18")

    label("loc_5CC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CEF")

    ChrTalk(    #289
        0x106,
        "#054F过来了！小心！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D18")

    label("loc_5CEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D18")

    ChrTalk(    #290
        0x108,
        "#076F当心！它们来了！\x02",
    )

    CloseMessageWindow()

    label("loc_5D18")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    SetChrChipByIndex(0x10, 3)

    def lambda_5D33():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5D33)
    Sleep(30)
    SetChrChipByIndex(0x11, 3)

    def lambda_5D53():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5D53)
    Sleep(30)
    SetChrChipByIndex(0x12, 3)

    def lambda_5D73():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5D73)
    WaitChrThread(0x10, 0x1)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    Battle(0xED8, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_5DAD"),
        (SWITCH_DEFAULT, "loc_5DB2"),
    )


    label("loc_5DAD")

    OP_B4(0x0)
    Jump("loc_5DB2")

    label("loc_5DB2")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    RemoveParty(0x48, 0xFF)
    RemoveParty(0x49, 0xFF)
    EventBegin(0x0)
    OP_6D(128650, 1000, 12260, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, 130610, 1000, 12770, 270)
    SetChrPos(0xA, 130610, 1000, 14190, 270)
    SetChrPos(0x101, 129190, 1000, 12210, 270)
    SetChrPos(0x102, 128000, 1000, 11480, 270)
    SetChrPos(0xF8, 129220, 1000, 13440, 270)
    SetChrPos(0xF9, 127720, 1000, 13010, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #291
        0x101,
        "#1006F好！击退了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xB,
        (
            "吓死我了……\x01",
            "啊，女神啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xA,
        "冷、冷汗都冒出来了……\x02",
    )

    CloseMessageWindow()

    def lambda_5ED6():
        OP_8C(0x102, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5ED6)

    def lambda_5EE4():
        OP_8C(0xF8, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5EE4)
    Sleep(200)

    def lambda_5EF7():
        OP_8C(0x101, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EF7)

    def lambda_5F05():
        OP_8C(0xF9, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5F05)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #294
        0x102,
        (
            "#1042F请立即到\x01",
            "升降机前避难。\x02\x03",

            "由于附近可能会有魔兽，\x01",
            "麻烦请迅速行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xB,
        "哦、哦！明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xA,
        (
            "也愿女神\x01",
            "保佑你们。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x1D, 0x80)

    def lambda_5F98():

        label("loc_5F98")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_5F98")

    QueueWorkItem2(0x102, 1, lambda_5F98)

    def lambda_5FA9():

        label("loc_5FA9")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_5FA9")

    QueueWorkItem2(0x101, 1, lambda_5FA9)

    def lambda_5FBA():

        label("loc_5FBA")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_5FBA")

    QueueWorkItem2(0xF8, 1, lambda_5FBA)

    def lambda_5FCB():

        label("loc_5FCB")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_5FCB")

    QueueWorkItem2(0xF9, 1, lambda_5FCB)

    def lambda_5FDC():
        OP_6D(126940, 1000, 12790, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5FDC)
    OP_43(0xB, 0x1, 0x0, 0x16)
    Sleep(200)
    OP_43(0xA, 0x1, 0x0, 0x17)
    WaitChrThread(0xA, 0x1)
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_A2(0x208A)
    OP_28(0xBF, 0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E6")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇3组都已经救出的情况下】\x01",      # 0
            "【◇不变更】\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6093"),
        (SWITCH_DEFAULT, "loc_60E6"),
    )


    label("loc_6093")

    OP_A2(0x2089)
    OP_A2(0x208A)
    OP_A2(0x208B)
    OP_A2(0x208C)
    SetChrPos(0xA, 131940, 0, 69900, 315)
    SetChrPos(0xB, 130930, 0, 68610, 45)
    SetChrPos(0xC, 124780, 0, 74190, 180)
    SetChrPos(0xD, 126540, 0, 75140, 180)
    Jump("loc_60E6")

    label("loc_60E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6184")
    OP_A2(0x0)
    OP_51(0x1C, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    def lambda_6142():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6142)

    def lambda_6150():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_6150)
    Sleep(150)

    def lambda_6163():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6163)

    def lambda_6171():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_6171)
    OP_69(0x1C, 0x7D0)
    Call(0, 33)

    label("loc_6184")

    EventEnd(0x0)
    Return()

    # Function_18_58C6 end

    def Function_19_6187(): pass

    label("Function_19_6187")

    SetChrPos(0xFE, 124640, 0, 21610, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1E064, 0x0, 0x4E16, 0x1388, 0x0)
    OP_8E(0xFE, 0x1E064, 0x1F4, 0x3B42, 0x1388, 0x0)
    OP_8E(0xFE, 0x1EAC8, 0x1F4, 0x2A62, 0x1388, 0x0)
    OP_8C(0x10, 90, 400)
    SetChrChipByIndex(0x10, 2)
    OP_43(0xFE, 0x0, 0x0, 0x2)
    Return()

    # Function_19_6187 end

    def Function_20_61F2(): pass

    label("Function_20_61F2")

    SetChrPos(0xFE, 124640, 0, 21610, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1E064, 0x0, 0x4E16, 0x1388, 0x0)
    OP_8E(0xFE, 0x1E064, 0x1F4, 0x3B42, 0x1388, 0x0)
    OP_8E(0xFE, 0x1E71C, 0x1F4, 0x2ECC, 0x1388, 0x0)
    OP_8C(0x11, 90, 400)
    SetChrChipByIndex(0x11, 2)
    OP_43(0xFE, 0x0, 0x0, 0x2)
    Return()

    # Function_20_61F2 end

    def Function_21_625D(): pass

    label("Function_21_625D")

    SetChrPos(0xFE, 124640, 0, 21610, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1E064, 0x0, 0x4E16, 0x1388, 0x0)
    OP_8E(0xFE, 0x1E064, 0x1F4, 0x3B42, 0x1388, 0x0)
    OP_8E(0xFE, 0x1E460, 0x1F4, 0x32F0, 0x1388, 0x0)
    OP_8C(0x12, 90, 400)
    SetChrChipByIndex(0xFE, 2)
    OP_43(0xFE, 0x0, 0x0, 0x2)
    Return()

    # Function_21_625D end

    def Function_22_62C8(): pass

    label("Function_22_62C8")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x1F7D3, 0x3E8, 0x2A94, 0x1388, 0x0)
    OP_8E(0xFE, 0x1ED02, 0x1F4, 0x2A94, 0x1388, 0x0)
    OP_8E(0xFE, 0x1DF60, 0x1F4, 0x3836, 0x1388, 0x0)
    OP_8E(0xFE, 0x1DF06, 0xFFFFFE98, 0x4704, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x40)
    SetChrPos(0xB, 130930, 0, 68610, 45)
    OP_4B(0xB, 255)
    Return()

    # Function_22_62C8 end

    def Function_23_634A(): pass

    label("Function_23_634A")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x1FE32, 0x3E8, 0x31E2, 0x1388, 0x0)
    OP_8E(0xFE, 0x1F7D3, 0x3E8, 0x2A94, 0x1388, 0x0)
    OP_8E(0xFE, 0x1ED02, 0x1F4, 0x2A94, 0x1388, 0x0)
    OP_8E(0xFE, 0x1DF60, 0x1F4, 0x3836, 0x1388, 0x0)
    OP_8E(0xFE, 0x1DF06, 0xFFFFFE98, 0x4704, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x40)
    SetChrPos(0xA, 131940, 0, 69900, 315)
    OP_4B(0xA, 255)
    Return()

    # Function_23_634A end

    def Function_24_63E0(): pass

    label("Function_24_63E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_63ED")
    Return()

    label("loc_63ED")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xC, 255)
    SetChrPos(0xC, 91290, 0, 30810, 129)
    SetChrFlags(0xC, 0x40)
    OP_6C(0, 0)
    TurnDirection(0x0, 0xC, 0)
    TurnDirection(0x1, 0xC, 0)
    TurnDirection(0x2, 0xC, 0)
    TurnDirection(0x3, 0xC, 0)
    OP_0D()

    def lambda_643A():
        OP_6D(94990, -500, 28960, 2500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_643A)
    OP_8E(0xC, 0x16C56, 0xFFFFFF10, 0x727E, 0x3E8, 0x0)
    OP_62(0xC, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    AddParty(0x4A, 0xFF, 0xFF)

    ChrTalk(    #297
        0xC,
        (
            "可、可恶～提恩特那家伙\x01",
            "竟然一个人逃跑，太狡猾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xC,
        (
            "只、只剩下我一个人\x01",
            "岂不是太过寂寞了吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0xC, 270, 400)
    SetChrChipByIndex(0x10, 3)
    SetChrChipByIndex(0x12, 3)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 87360, -450, 30190, 181)
    SetChrPos(0x12, 86520, -380, 28480, 180)
    SetChrPos(0x11, 99570, 0, 24640, 315)
    SetChrPos(0x13, 100440, 0, 25840, 315)

    def lambda_6562():
        OP_6D(93440, -330, 29110, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6562)

    def lambda_657A():
        OP_92(0x10, 0xC, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_657A)

    def lambda_658F():
        OP_92(0x12, 0xC, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_658F)
    WaitChrThread(0x10, 0x1)
    SetChrChipByIndex(0x10, 2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #299
        0xC,
        "啊……不好……\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xC, 90, 400)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x11, 3)
    SetChrChipByIndex(0x13, 3)

    def lambda_660C():
        OP_8E(0xFE, 0x17B06, 0x0, 0x6F90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_660C)

    def lambda_6627():
        OP_8E(0xFE, 0x17584, 0xFFFFFEB6, 0x6F0E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6627)
    OP_94(0x1, 0xC, 0x0, 0x1F4, 0x7D0, 0x0)
    TurnDirection(0xC, 0x11, 0)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xC, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_94(0x1, 0xC, 0xB4, 0x1F4, 0x1388, 0x0)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    WaitChrThread(0x13, 0x1)
    SetChrChipByIndex(0x13, 2)
    OP_43(0x13, 0x0, 0x0, 0x2)

    ChrTalk(    #300
        0xC,
        "啊啊！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 0)
    OP_8C(0x12, 90, 0)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x13, 0x1)
    SetChrChipByIndex(0x10, 3)
    SetChrChipByIndex(0x11, 3)
    SetChrChipByIndex(0x12, 3)
    SetChrChipByIndex(0x13, 3)

    def lambda_66F7():

        label("loc_66F7")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_66F7")

    QueueWorkItem2(0x10, 2, lambda_66F7)

    def lambda_6708():

        label("loc_6708")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_6708")

    QueueWorkItem2(0x11, 2, lambda_6708)

    def lambda_6719():

        label("loc_6719")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_6719")

    QueueWorkItem2(0x13, 2, lambda_6719)

    def lambda_672A():
        OP_6D(93850, -230, 29940, 1500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_672A)

    def lambda_6742():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6742)

    def lambda_6758():
        OP_92(0xFE, 0xC, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6758)
    Sleep(120)
    OP_43(0x12, 0x1, 0x0, 0x1D)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0xC, 0x16DA0, 0xFFFFFF2E, 0x7454, 0x3E8, 0x0)
    OP_8C(0xC, 225, 400)
    OP_8F(0xC, 0x172E6, 0xFFFFFF10, 0x779C, 0x3E8, 0x0)

    ChrTalk(    #301
        0xC,
        (
            "不、不好！！\x01",
            "难道是走投无路了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xC,
        "哇～有、有人吗～！！\x02",
    )

    CloseMessageWindow()

    def lambda_67FB():
        OP_6D(96410, -130, 28390, 2000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_67FB)

    def lambda_6813():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_6813)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_43(0x102, 0x1, 0x0, 0x1A)
    Sleep(200)
    OP_43(0x101, 0x1, 0x0, 0x19)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x1C)
    Sleep(200)
    OP_43(0xF8, 0x1, 0x0, 0x1B)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0xC, 0x1)
    TurnDirection(0xC, 0x101, 800)

    ChrTalk(    #303
        0xC,
        "你、你们是！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x101,
        "#1006F#2P这种事待会儿再说！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x102,
        "#1042F#1P我们马上来救你！\x02",
    )

    CloseMessageWindow()
    Battle(0xED9, 0x300018, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_68EE"),
        (SWITCH_DEFAULT, "loc_68F3"),
    )


    label("loc_68EE")

    OP_B4(0x0)
    Jump("loc_68F3")

    label("loc_68F3")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    EventBegin(0x0)
    RemoveParty(0x4A, 0xFF)
    OP_6D(95530, -350, 29670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 95990, -230, 28580, 180)
    SetChrPos(0x102, 94980, -500, 28580, 180)
    SetChrPos(0xF8, 96920, 0, 28930, 90)
    SetChrPos(0xF9, 93800, -470, 28930, 225)
    OP_8C(0xC, 180, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0xC, 95240, -270, 30370, 180)
    ClearChrFlags(0xC, 0x40)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #306
        0xC,
        "呼～呼～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xC,
        "啊～～我还以为自己要死了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        "#1007F呼，真不容易……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x102,
        "#1043F真是千钧一发啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A78")

    ChrTalk(    #310
        0x107,
        "#561F还、还好赶上了～\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AE5")

    label("loc_6A78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AAD")

    ChrTalk(    #311
        0x108,
        (
            "#073F呼……\x01",
            "真的是只差一步呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AE5")

    label("loc_6AAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AE5")

    ChrTalk(    #312
        0x103,
        (
            "#027F真是的……\x01",
            "真是让人捏一把汗啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AE5")


    ChrTalk(    #313
        0xC,
        "那个，莫非你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xC,
        (
            "是在上次塌方事故中\x01",
            "救了我们的游击士吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)

    def lambda_6B44():

        label("loc_6B44")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_6B44")

    QueueWorkItem2(0x101, 1, lambda_6B44)

    def lambda_6B55():

        label("loc_6B55")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_6B55")

    QueueWorkItem2(0x102, 1, lambda_6B55)
    Sleep(200)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)

    def lambda_6B7F():

        label("loc_6B7F")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_6B7F")

    QueueWorkItem2(0xF8, 1, lambda_6B7F)

    def lambda_6B90():

        label("loc_6B90")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_6B90")

    QueueWorkItem2(0xF9, 1, lambda_6B90)

    ChrTalk(    #315
        0x101,
        "#1006F嗯，答对了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x102,
        (
            "#1040F不过那时候我们\x01",
            "还是准游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xC,
        (
            "那～那就是说你们已经\x01",
            "顺利成为正游击士了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xC,
        (
            "嗯，这么说来，看上去\x01",
            "是有了点正游击士的风格了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        (
            "#1008F嘿嘿，真的吗？\x02\x03",

            "#1007F……什么啊，现在\x01",
            "可不是开玩笑的场合啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xC,
        (
            "啊……\x01",
            "是、是啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xC,
        (
            "那接下来我应该\x01",
            "怎么做才好？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x102,
        (
            "#1042F请立即到\x01",
            "升降机前避难。\x02\x03",

            "尽快离开，\x01",
            "不要让魔兽发现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xC,
        "嗯、嗯……明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xC,
        (
            "那么，\x01",
            "你们也要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D3E():
        OP_6D(97510, 0, 28150, 2000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6D3E)

    def lambda_6D56():
        OP_8F(0xFE, 0x17A3E, 0xFFFFFFF6, 0x6CF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_6D56)

    def lambda_6D71():

        label("loc_6D71")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_6D71")

    QueueWorkItem2(0x101, 1, lambda_6D71)
    OP_8E(0xC, 0x1845C, 0x0, 0x696E, 0xFA0, 0x0)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_8E(0xC, 0x1A838, 0x0, 0x6AF4, 0xFA0, 0x0)
    OP_44(0x101, 0x1)
    SetChrPos(0xC, 124780, 0, 74190, 180)
    OP_4B(0xC, 255)
    OP_A2(0x208B)
    OP_28(0xBF, 0x1, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E99")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇3组都已经救出的情况下】\x01",      # 0
            "【◇不变更】\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6E46"),
        (SWITCH_DEFAULT, "loc_6E99"),
    )


    label("loc_6E46")

    OP_A2(0x2089)
    OP_A2(0x208A)
    OP_A2(0x208B)
    OP_A2(0x208C)
    SetChrPos(0xA, 131940, 0, 69900, 315)
    SetChrPos(0xB, 130930, 0, 68610, 45)
    SetChrPos(0xC, 124780, 0, 74190, 180)
    SetChrPos(0xD, 126540, 0, 75140, 180)
    Jump("loc_6E99")

    label("loc_6E99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F36")
    OP_A2(0x1)
    Fade(500)
    OP_6D(95210, -440, 28870, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(22000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 95750, -310, 28080, 315)
    SetChrPos(0x102, 94440, -500, 28540, 45)
    SetChrPos(0xF8, 96210, -160, 29110, 225)
    SetChrPos(0xF9, 94950, -500, 29820, 135)
    OP_0D()
    Call(0, 33)

    label("loc_6F36")

    EventEnd(0x0)
    Return()

    # Function_24_63E0 end

    def Function_25_6F39(): pass

    label("Function_25_6F39")

    SetChrPos(0xFE, 106130, 0, 27510, 45)
    OP_8E(0xFE, 0x184F2, 0x0, 0x69A0, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_25_6F39 end

    def Function_26_6F66(): pass

    label("Function_26_6F66")

    SetChrPos(0xFE, 106130, 0, 27510, 45)
    OP_8E(0xFE, 0x181B4, 0x0, 0x66D0, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_26_6F66 end

    def Function_27_6F93(): pass

    label("Function_27_6F93")

    SetChrPos(0xFE, 106130, 0, 27510, 45)
    OP_8E(0xFE, 0x189A2, 0x0, 0x67A2, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_27_6F93 end

    def Function_28_6FC0(): pass

    label("Function_28_6FC0")

    SetChrPos(0xFE, 106130, 0, 27510, 45)
    OP_8E(0xFE, 0x184C0, 0x0, 0x62C0, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_28_6FC0 end

    def Function_29_6FED(): pass

    label("Function_29_6FED")

    OP_8E(0xFE, 0x16C1A, 0xFFFFFEB6, 0x70DA, 0x7D0, 0x0)
    TurnDirection(0x12, 0xC, 400)
    Return()

    # Function_29_6FED end

    def Function_30_7009(): pass

    label("Function_30_7009")

    OP_8E(0xF8, 0x1766A, 0xFFFFFEFC, 0x7422, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_30_7009 end

    def Function_31_7025(): pass

    label("Function_31_7025")

    OP_8E(0xF9, 0x170C0, 0xFFFFFEC0, 0x7580, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_31_7025 end

    def Function_32_7041(): pass

    label("Function_32_7041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_704E")
    Return()

    label("loc_704E")

    EventBegin(0x0)
    Fade(500)
    OP_4A(0xD, 255)
    SetChrPos(0xD, 83170, -500, 10620, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x10, 86220, -500, 12400, 270)
    SetChrPos(0x11, 87000, -500, 11330, 270)
    SetChrPos(0x12, 86950, -500, 9870, 270)
    SetChrPos(0x13, 86220, -500, 8710, 270)
    SetChrChipByIndex(0x10, 2)
    SetChrChipByIndex(0x11, 2)
    SetChrChipByIndex(0x12, 2)
    SetChrChipByIndex(0x13, 2)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_713C")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_717A")

    label("loc_713C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7163")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_717A")

    label("loc_7163")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_717A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71A1")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_71DF")

    label("loc_71A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71C8")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_71DF")

    label("loc_71C8")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_71DF")

    TurnDirection(0x0, 0xD, 0)
    TurnDirection(0x1, 0xD, 0)
    TurnDirection(0x2, 0xD, 0)
    TurnDirection(0x3, 0xD, 0)
    Sleep(1000)

    ChrTalk(    #325
        0x101,
        "#1020F啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x102,
        "#1044F那是……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)

    def lambda_7236():
        OP_6D(83130, -340, 10670, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7236)
    OP_6C(315000, 0)
    OP_0D()
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)

    def lambda_727B():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_727B)
    Sleep(120)

    def lambda_7296():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7296)
    Sleep(100)

    def lambda_72B1():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_72B1)
    Sleep(150)
    OP_94(0x0, 0x13, 0x0, 0x2BC, 0x3E8, 0x0)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_72ED():
        OP_91(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_72ED)
    Sleep(150)
    Sleep(50)

    def lambda_7312():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7312)
    Sleep(100)

    def lambda_732D():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_732D)
    Sleep(100)

    def lambda_7348():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7348)
    Sleep(120)
    OP_94(0x0, 0x13, 0x0, 0x2BC, 0x3E8, 0x0)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7384():
        OP_91(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7384)
    Sleep(200)

    def lambda_73A4():
        OP_94(0x0, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_73A4)
    Sleep(100)

    def lambda_73BF():
        OP_94(0x0, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_73BF)
    Sleep(120)

    def lambda_73DA():
        OP_94(0x0, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_73DA)
    Sleep(100)

    def lambda_73F5():
        OP_94(0x0, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_73F5)
    Sleep(200)

    def lambda_7410():
        OP_91(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7410)
    WaitChrThread(0xD, 0x1)
    OP_4A(0xD, 255)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x13, 0x1)
    Sleep(400)

    ChrTalk(    #327
        0xD,
        "混、混帐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xD,
        (
            "把魔兽引向这边的\x01",
            "做法是很好啦……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 45, 400)
    Sleep(400)
    OP_8C(0xD, 135, 400)
    Sleep(400)
    OP_8C(0xD, 90, 400)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #329
        0xD,
        "嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xD,
        (
            "……不过这看起来\x01",
            "做得有些过头了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xD,
        "阿妮娅、芙莉莎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xD,
        (
            "不好意思……\x01",
            "看来我已经不行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x101,
        "老大！\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    AddParty(0x32, 0xFF, 0xFF)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x101, 94580, -350, 10790, 5000)
    SetChrPos(0x102, 94510, -390, 9750, 5000)
    SetChrPos(0xF8, 95840, -240, 10950, 5000)
    SetChrPos(0xF9, 95640, -410, 9340, 5000)

    def lambda_75B6():
        OP_6D(84450, -500, 10830, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_75B6)

    def lambda_75CE():
        OP_8E(0xFE, 0x1561C, 0xFFFFFEA2, 0x2A26, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75CE)
    Sleep(300)

    def lambda_75EE():
        OP_8E(0xFE, 0x155D6, 0xFFFFFE7A, 0x2616, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75EE)
    Sleep(200)

    def lambda_760E():
        OP_8E(0xFE, 0x15CFC, 0xFFFFFF10, 0x2AC6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_760E)
    Sleep(40)
    OP_8E(0xF9, 0x15C34, 0xFFFFFE66, 0x247C, 0x1388, 0x0)
    Sleep(1000)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #334
        0xD,
        "你、你们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x101,
        (
            "#1005F#2P别放弃！\x01",
            "我们一定会救你的！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76D0")

    ChrTalk(    #336
        0x108,
        (
            "#076F用保守战术的话时间来不及了。\x02\x03",

            "一口气杀出一条血路来！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7765")

    label("loc_76D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7718")

    ChrTalk(    #337
        0x106,
        (
            "#054F没时间小心翼翼的了。\x02\x03",

            "现在只能一口气突入了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7765")

    label("loc_7718")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7765")

    ChrTalk(    #338
        0x103,
        (
            "#024F用保守战术的话时间来不及了。\x02\x03",

            "大家做好觉悟后突入吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7765")


    ChrTalk(    #339
        0x102,
        "#1046F#3P是！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_779D")

    ChrTalk(    #340
        0x107,
        "#062F明、明白了！\x02",
    )

    CloseMessageWindow()

    label("loc_779D")


    def lambda_77A3():
        OP_90(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77A3)

    def lambda_77BE():
        OP_90(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77BE)

    def lambda_77D9():
        OP_90(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_77D9)

    def lambda_77F4():
        OP_90(0xFE, 0xFFFFFA88, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_77F4)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    Battle(0xEDA, 0x300018, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    EventBegin(0x0)
    RemoveParty(0x32, 0xFF)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_6D(82190, -500, 10990, 0)
    OP_67(0, 8109, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 84100, -500, 10790, 90)
    SetChrPos(0x102, 84110, -410, 9850, 90)
    SetChrPos(0xF8, 83380, -470, 11670, 90)
    SetChrPos(0xF9, 83620, -180, 8820, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #341
        0x101,
        "#1007F呼，总算……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x102,
        "#1043F……似乎解决了呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_796F")

    ChrTalk(    #343
        0x107,
        (
            "#561F呼、呼……\x01",
            "我的心跳得好厉害……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_796F")

    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)

    def lambda_7989():

        label("loc_7989")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_7989")

    QueueWorkItem2(0xF8, 1, lambda_7989)

    def lambda_799A():

        label("loc_799A")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_799A")

    QueueWorkItem2(0xF9, 1, lambda_799A)
    Sleep(200)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)

    def lambda_79C4():

        label("loc_79C4")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_79C4")

    QueueWorkItem2(0x101, 1, lambda_79C4)

    def lambda_79D5():

        label("loc_79D5")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_79D5")

    QueueWorkItem2(0x102, 1, lambda_79D5)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A13")

    ChrTalk(    #344
        0x103,
        "#020F老大，你没受伤吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A62")

    label("loc_7A13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A3F")

    ChrTalk(    #345
        0x106,
        "#051F大叔，你没事吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A62")

    label("loc_7A3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A62")

    ChrTalk(    #346
        0x108,
        "#070F没受伤吧？\x02",
    )

    CloseMessageWindow()

    label("loc_7A62")


    ChrTalk(    #347
        0xD,
        (
            "嗯、嗯……\x01",
            "只是擦伤而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xD,
        (
            "不过真多亏你们\x01",
            "跑来救我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xD,
        (
            "有机会的话也希望偶尔在\x01",
            "事故之外的场合下见见你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x101,
        (
            "#1016F哈哈，是啊……\x02\x03",

            "不知为什么，每次来矿山\x01",
            "都会遇到紧急情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x102,
        (
            "#1048F呼，是啊……\x02\x03",

            "#1035F不过，等下次\x01",
            "有机会再聊吧。\x02\x03",

            "现在必须先要请你\x01",
            "尽快去避难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xD,
        "哦，这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#1002F提恩特先生他们在\x01",
            "升降机前面等着。\x02\x03",

            "请你先到\x01",
            "那里避难吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xD,
        "好，就这么办。\x02",
    )

    CloseMessageWindow()

    def lambda_7BEA():
        OP_6D(84620, -500, 10450, 1500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7BEA)
    OP_8E(0xD, 0x1417C, 0xFFFFFEF2, 0x2EC2, 0xBB8, 0x0)
    OP_8E(0xD, 0x144EC, 0xFFFFFE48, 0x316A, 0xBB8, 0x0)
    OP_8E(0xD, 0x15158, 0xFFFFFE0C, 0x3070, 0xBB8, 0x0)
    OP_8E(0xD, 0x15842, 0xFFFFFE0C, 0x2742, 0xBB8, 0x0)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xD, 0x101, 400)
    Sleep(500)

    ChrTalk(    #355
        0xD,
        "……对了，得告诉你们几个，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xD,
        (
            "从支部过来负责\x01",
            "警戒的游击士小哥……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xD,
        "那家伙已经去避难了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        "#1026F#2P啊，你是说利吉先生吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x102,
        (
            "#1043F#3P不，很遗憾……\x02\x03",

            "我们也还\x01",
            "没看到他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xD,
        (
            "果然是这样啊……\x02\x03",

            "如果找不到的话\x01",
            "你们就去施工现场看看。\x02\x03",

            "那位小哥直到最后\x01",
            "都在那里为大家争取逃跑的时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        "#1002F#2P……嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DF0")

    ChrTalk(    #362
        0x108,
        "#072F好，我们会参考你的意见的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E51")

    label("loc_7DF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E22")

    ChrTalk(    #363
        0x106,
        "#050F我们会参考你的意见的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E51")

    label("loc_7E22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E51")

    ChrTalk(    #364
        0x103,
        "#022F我们会参考你的意见的。\x02",
    )

    CloseMessageWindow()

    label("loc_7E51")


    def lambda_7E57():
        OP_6D(90550, -420, 10520, 1500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7E57)
    OP_8E(0xD, 0x18E16, 0x0, 0x2BCA, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    SetChrPos(0xD, 126540, 0, 75140, 180)
    OP_4B(0xD, 255)
    OP_A2(0x208C)
    OP_28(0xBF, 0x1, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F72")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇3组都已经救出的情况下】\x01",      # 0
            "【◇不变更】\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7F1F"),
        (SWITCH_DEFAULT, "loc_7F72"),
    )


    label("loc_7F1F")

    OP_A2(0x2089)
    OP_A2(0x208A)
    OP_A2(0x208B)
    OP_A2(0x208C)
    SetChrPos(0xA, 131940, 0, 69900, 315)
    SetChrPos(0xB, 130930, 0, 68610, 45)
    SetChrPos(0xC, 124780, 0, 74190, 180)
    SetChrPos(0xD, 126540, 0, 75140, 180)
    Jump("loc_7F72")

    label("loc_7F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_800F")
    OP_A2(0x2)
    Fade(500)
    OP_6D(82850, -460, 10740, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 83690, -500, 10780, 270)
    SetChrPos(0x102, 82740, -440, 11720, 180)
    SetChrPos(0xF8, 82930, -430, 9940, 0)
    SetChrPos(0xF9, 82130, -280, 10740, 90)
    OP_0D()
    Call(0, 33)

    label("loc_800F")

    EventEnd(0x0)
    Return()

    # Function_32_7041 end

    def Function_33_8012(): pass

    label("Function_33_8012")

    EventBegin(0x0)

    ChrTalk(    #365
        0x101,
        "#1002F那么……现在人都到齐了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x102,
        (
            "#1040F嗯，矿工们应该\x01",
            "已经全部营救完毕了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80CC")

    ChrTalk(    #367
        0x103,
        (
            "#026F就是说，接下来\x01",
            "只剩要去救利吉了。\x02\x03",

            "#522F很遗憾，目前为止还\x01",
            "没看到过他……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_819E")

    label("loc_80CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_812D")

    ChrTalk(    #368
        0x106,
        (
            "#552F就是说，接下来是利吉啊……\x02\x03",

            "在目前为止调查过的地方\x01",
            "好像都没见到过他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_819E")

    label("loc_812D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_819E")

    ChrTalk(    #369
        0x108,
        (
            "#072F就是说，接下来只剩那个\x01",
            "叫做利吉的游击士了吗？\x02\x03",

            "很遗憾，在迄今为止的搜索中\x01",
            "都没发现他……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_819E")


    ChrTalk(    #370
        0x101,
        (
            "#1002F我记得老大\x01",
            "叫我们去施工现场看看。\x02\x03",

            "他说利吉先生\x01",
            "一个人留在那里……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_824B")

    ChrTalk(    #371
        0x106,
        (
            "#050F现在没时间多想了。\x02\x03",

            "在一切为时已晚之前，\x01",
            "赶快去那个什么施工现场吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82B0")

    label("loc_824B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_827F")

    ChrTalk(    #372
        0x108,
        (
            "#072F快。\x02\x03",

            "有可能会来不及的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82B0")

    label("loc_827F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82B0")

    ChrTalk(    #373
        0x103,
        (
            "#022F快。\x02\x03",

            "有可能会来不及的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8399")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇最后救出的是皮尔姆、海涅的情况下】\x01",      # 0
            "【◇最后救出的是彭兹的情况下】\x01",              # 1
            "【◇最后救出的是加通的情况下】\x01",              # 2
            "【◇不变更】\x01",                                # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8375"),
        (1, "loc_8381"),
        (2, "loc_838D"),
        (SWITCH_DEFAULT, "loc_8399"),
    )


    label("loc_8375")

    OP_A2(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    Jump("loc_8399")

    label("loc_8381")

    OP_A3(0x0)
    OP_A2(0x1)
    OP_A3(0x2)
    Jump("loc_8399")

    label("loc_838D")

    OP_A3(0x0)
    OP_A3(0x1)
    OP_A2(0x2)
    Jump("loc_8399")

    label("loc_8399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_83CF")
    OP_A3(0x0)

    ChrTalk(    #374
        0x102,
        (
            "#1042F塌方的现场\x01",
            "应该是在西北方向。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8438")

    label("loc_83CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8405")
    OP_A3(0x2)

    ChrTalk(    #375
        0x102,
        (
            "#1042F塌方的现场\x01",
            "应该是在西北方向。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8438")

    label("loc_8405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8438")
    OP_A3(0x1)

    ChrTalk(    #376
        0x102,
        (
            "#1042F塌方的现场\x01",
            "应该是在西北方向。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8438")


    ChrTalk(    #377
        0x101,
        "#1002F好！走吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x208D)
    OP_28(0xBF, 0x1, 0x80)
    OP_28(0xBF, 0x1, 0x100)
    Return()

    # Function_33_8012 end

    def Function_34_845E(): pass

    label("Function_34_845E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 5)), scpexpr(EXPR_END)), "loc_87BB")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_861C")
    Fade(500)
    OP_6D(93490, -500, 66260, 0)
    SetChrPos(0x101, 93950, -260, 66700, 0)
    SetChrPos(0x102, 93090, -480, 66700, 0)
    SetChrPos(0xF8, 94220, -230, 65500, 0)
    SetChrPos(0xF9, 92880, -350, 65500, 0)
    OP_0D()

    ChrTalk(    #378
        0x101,
        "#1002F前面就是魔兽的巢穴……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_852E")

    ChrTalk(    #379
        0x106,
        (
            "#057F真不得了……\x02\x03",

            "到处都充满了魔兽的气味。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85D0")

    label("loc_852E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8578")

    ChrTalk(    #380
        0x103,
        (
            "#523F真是好讨厌的地方啊。\x02\x03",

            "到处都充满了魔兽的气味。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85D0")

    label("loc_8578")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85D0")

    ChrTalk(    #381
        0x108,
        (
            "#072F嗯，简直是死亡之地。\x02\x03",

            "光是站在这里就能感受到\x01",
            "强烈的魔兽的气息。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85D0")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #382
        0x102,
        (
            "#1042F进去之后就\x01",
            "无法回头了……\x02\x03",

            "艾丝蒂尔。\x01",
            "装备都确认好了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86BE")

    label("loc_861C")

    Fade(500)
    OP_6D(93490, -500, 66260, 0)
    SetChrPos(0x101, 93950, -260, 66700, 0)
    SetChrPos(0x102, 93090, -480, 66700, 0)
    SetChrPos(0xF8, 94220, -230, 65500, 0)
    SetChrPos(0xF9, 92880, -350, 65500, 0)
    OP_0D()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #383
        0x102,
        (
            "#1042F艾丝蒂尔。\x01",
            "装备都确认好了？\x02\x03",

            "进去之后就\x01",
            "无法回头了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86BE")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【突入】\x01",            # 0
            "【还没准备好】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_871D"),
        (1, "loc_8724"),
        (SWITCH_DEFAULT, "loc_87B8"),
    )


    label("loc_871D")

    Call(0, 35)
    Jump("loc_87B8")

    label("loc_8724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8790")
    OP_A2(0x208E)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #384
        0x101,
        (
            "#1015F应该是没问题的……\x02\x03",

            "不过我想再\x01",
            "仔细确认一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x102,
        "#1040F明白，就这么办吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_87B3")

    label("loc_8790")


    ChrTalk(    #386
        0x102,
        (
            "#1040F明白，好好准备\x01",
            "一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B3")

    EventEnd(0x0)
    Jump("loc_87B8")

    label("loc_87B8")

    Jump("loc_88BB")

    label("loc_87BB")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8855")

    ChrTalk(    #387
        0x101,
        (
            "#1025F啊……\x01",
            "这里是魔兽的巢穴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x102,
        (
            "#1042F在进入这里之前\x01",
            "首先要营救矿工们。\x02\x03",

            "还没确认全体人员是否平安哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x101,
        "#1002F嗯，我明白。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_88A0")

    label("loc_8855")


    ChrTalk(    #390
        0x101,
        (
            "#1002F这里是魔兽的巢穴呢……\x02\x03",

            "在进入这里之前\x01",
            "要先确认矿工们是否平安。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88A0")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_88BB")

    Return()

    # Function_34_845E end

    def Function_35_88BC(): pass

    label("Function_35_88BC")

    TurnDirection(0x101, 0x102, 400)
    Sleep(500)

    ChrTalk(    #391
        0x101,
        "#1006F嗯……准备ＯＫ了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x102,
        "#1042F好，那我们走吧！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)

    def lambda_8916():
        OP_6D(95620, 0, 73830, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8916)

    def lambda_892E():
        OP_8E(0xFE, 0x176CE, 0xFFFFFEA2, 0x1269C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_892E)
    Sleep(200)

    def lambda_894E():
        OP_8E(0xFE, 0x176CE, 0xFFFFFEA2, 0x1269C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_894E)
    Sleep(200)

    def lambda_896E():
        OP_8E(0xFE, 0x176CE, 0xFFFFFEA2, 0x1269C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_896E)
    Sleep(200)

    def lambda_898E():
        OP_8E(0xFE, 0x176CE, 0xFFFFFEA2, 0x1269C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_898E)
    Sleep(400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x101, 0x2)
    SetChrPos(0x101, 185820, -450, 52650, 0)
    SetChrPos(0x102, 185820, -450, 52650, 0)
    SetChrPos(0xF8, 185820, -450, 52650, 0)
    SetChrPos(0xF9, 185820, -450, 52650, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x10, 189500, -250, 70370, 180)
    SetChrPos(0x11, 190500, -250, 69540, 225)
    SetChrPos(0x12, 190400, -130, 68040, 315)
    SetChrPos(0x13, 188000, -250, 70370, 180)
    SetChrPos(0x14, 187000, -250, 69540, 135)
    SetChrPos(0x15, 186900, -130, 68040, 45)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x16, 188680, 0, 73010, 202)
    SetChrPos(0x17, 185450, 0, 71540, 139)
    SetChrPos(0x19, 191630, 0, 71750, 239)
    SetChrPos(0x1A, 193000, -130, 68420, 270)
    SetChrPos(0x1B, 184070, 0, 68530, 103)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_D2(0x90002, 0x90006, 0x7)
    OP_D2(0x7051D, 0x70524, 0x4)
    OP_D2(0x7051E, 0x70525, 0x5)
    SetChrChipByIndex(0xE, 5)
    SetChrSubChip(0xE, 3)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 188800, -250, 68950, 0)
    LoadEffect(0x1, "scraft\\\\sc000_11.eff")
    LoadEffect(0x2, "map\\\\mp023_00.eff")
    LoadEffect(0x3, "monster\\\\msc0550.eff")
    SoundLoad(287)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x10, 2)
    SetChrChipByIndex(0x11, 2)
    SetChrChipByIndex(0x12, 2)
    SetChrChipByIndex(0x13, 2)
    SetChrChipByIndex(0x14, 2)
    SetChrChipByIndex(0x15, 2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0x16, 2)
    SetChrChipByIndex(0x17, 2)
    SetChrChipByIndex(0x18, 2)
    SetChrChipByIndex(0x19, 2)
    SetChrChipByIndex(0x1A, 2)
    SetChrChipByIndex(0x1B, 2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    OP_43(0x1A, 0x0, 0x0, 0x2)
    OP_43(0x1B, 0x0, 0x0, 0x2)
    OP_20(0x3E8)
    Sleep(1000)
    OP_21()
    OP_1D(0x56)
    Sleep(1000)
    OP_6D(199700, 110, 73850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(107000, 0)
    OP_6E(262, 0)

    def lambda_8CBD():
        OP_6D(188900, -250, 69050, 5000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8CBD)

    def lambda_8CD5():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_8CD5)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xD, 0x1)

    ChrTalk(    #393
        0xE,
        "#4P呜、呜呜……\x02",
    )

    CloseMessageWindow()

    def lambda_8D09():

        label("loc_8D09")

        OP_9E(0xFE, 0x32, 0x0, 0x3E8, 0x7D0)
        OP_48()
        Jump("loc_8D09")

    QueueWorkItem2(0xE, 1, lambda_8D09)
    OP_99(0xE, 0x3, 0x0, 0x258)
    OP_44(0xE, 0x1)
    SetChrChipByIndex(0xE, 6)
    OP_43(0x13, 0x1, 0x0, 0x24)
    Sleep(200)
    OP_43(0x10, 0x1, 0x0, 0x25)
    Sleep(500)

    def lambda_8D50():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D50)

    def lambda_8D5E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8D5E)

    def lambda_8D6C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8D6C)

    def lambda_8D7A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8D7A)
    Sleep(200)

    def lambda_8D8D():

        label("loc_8D8D")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_8D8D")

    QueueWorkItem2(0x16, 1, lambda_8D8D)

    def lambda_8D9E():

        label("loc_8D9E")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_8D9E")

    QueueWorkItem2(0x17, 1, lambda_8D9E)

    def lambda_8DAF():

        label("loc_8DAF")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_8DAF")

    QueueWorkItem2(0x18, 1, lambda_8DAF)

    def lambda_8DC0():

        label("loc_8DC0")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_8DC0")

    QueueWorkItem2(0x19, 1, lambda_8DC0)

    def lambda_8DD1():

        label("loc_8DD1")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_8DD1")

    QueueWorkItem2(0x1A, 1, lambda_8DD1)

    def lambda_8DE2():

        label("loc_8DE2")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_8DE2")

    QueueWorkItem2(0x1B, 1, lambda_8DE2)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0xE, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x19, 0x1)
    OP_44(0x1A, 0x1)
    OP_44(0x1B, 0x1)

    ChrTalk(    #394
        0xE,
        "啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_8E23():

        label("loc_8E23")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_8E23")

    QueueWorkItem2(0xE, 1, lambda_8E23)
    Sleep(200)
    OP_99(0xE, 0x3, 0x0, 0x12C)
    Sleep(200)
    OP_44(0xE, 0x1)
    SetChrChipByIndex(0xE, 6)

    ChrTalk(    #395
        0xE,
        "呜、呜呜呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x101,
        "#5P利吉先生！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E9D")

    ChrTalk(    #397
        0x103,
        "#1P利吉！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EB0")

    label("loc_8E9D")


    ChrTalk(    #398
        0x102,
        "#1P你没事吧！\x02",
    )

    CloseMessageWindow()

    label("loc_8EB0")

    OP_44(0xE, 0x3)
    OP_43(0x101, 0x1, 0x0, 0x27)
    OP_43(0x101, 0x2, 0x0, 0x2B)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x28)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x29)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x2A)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FAB")

    ChrTalk(    #399
        0xE,
        (
            "那、那个……\x01",
            "艾丝蒂尔和雪拉前辈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xE,
        (
            "你、你们怎么会……\x01",
            "来这里……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x103,
        (
            "#524F利吉，你已经做得很好了。\x02\x03",

            "你战斗得非常出色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x102,
        (
            "#1042F接下来的事情就\x01",
            "交给我们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9031")

    label("loc_8FAB")


    ChrTalk(    #403
        0xE,
        (
            "那、那个……\x01",
            "艾丝蒂尔和约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xE,
        (
            "你、你们怎么会……\x01",
            "来这里……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x101,
        "#1006F当然是来帮你的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x102,
        "#1042F接下来就交给我们吧。\x02",
    )

    CloseMessageWindow()

    label("loc_9031")


    ChrTalk(    #407
        0xE,
        "是、是吗……太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0xE,
        (
            "不、不过，你们要小心。\x01",
            "敌人不只是眼前这些……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 5)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xE, 0x0, 0x3, 0x3E8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90E4")
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #409
        0x108,
        (
            "#072F嗯……\x02\x03",

            "#076F不好，先后退！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9182")

    label("loc_90E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9137")
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #410
        0x106,
        (
            "#052F嗯……？\x02\x03",

            "#054F喂，先后退！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9182")

    label("loc_9137")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9182")
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #411
        0x103,
        (
            "#022F……！！\x02\x03",

            "大家先后退！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9182")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_9191():
        OP_6D(188840, 720, 70020, 2000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9191)

    def lambda_91A9():
        OP_67(0, 3720, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_91A9)

    def lambda_91C1():
        OP_6B(2780, 2000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_91C1)

    def lambda_91D1():
        OP_6C(5000, 2000)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_91D1)

    def lambda_91E1():
        OP_96(0xFE, 0x2E568, 0x0, 0xF15E, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_91E1)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(10)

    def lambda_9209():
        OP_96(0xFE, 0x2D9A6, 0xFFFFFF7E, 0xF262, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_9209)
    Sleep(100)

    def lambda_922C():
        OP_96(0xFE, 0x2E22A, 0xFFFFFF88, 0xF636, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_922C)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(10)

    def lambda_9254():
        OP_96(0xFE, 0x2DDC0, 0xFFFFFF06, 0xF690, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9254)
    WaitChrThread(0x102, 0x1)
    SetChrPos(0x1C, 188800, -250, 68950, 0)

    def lambda_9288():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_9288)

    def lambda_9296():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_9296)

    def lambda_92A4():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_92A4)

    def lambda_92B2():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_92B2)

    def lambda_92C0():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_92C0)

    def lambda_92CE():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_92CE)

    def lambda_92DC():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_92DC)

    def lambda_92EA():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_92EA)

    def lambda_92F8():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_92F8)

    def lambda_9306():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_9306)

    def lambda_9314():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_9314)

    def lambda_9322():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_9322)
    Sleep(600)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)

    def lambda_9371():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9371)

    def lambda_9387():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9387)

    def lambda_939D():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_939D)

    def lambda_93B3():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_93B3)

    def lambda_93C9():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_93C9)

    def lambda_93DF():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_93DF)

    def lambda_93F5():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_93F5)

    def lambda_940B():
        OP_8F(0xFE, 0x2D4F6, 0x0, 0x119FE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_940B)

    def lambda_9426():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9426)

    def lambda_943C():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_943C)

    def lambda_9452():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_9452)

    def lambda_9468():
        OP_8F(0xFE, 0x2CF24, 0x0, 0x10C66, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_9468)
    Sleep(100)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x20)
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 20)
    SetChrSubChip(0xF, 0)
    SetChrPos(0xF, 188800, 10000, 68950, 185)
    OP_8F(0xF, 0x2E180, 0xFFFFFEA2, 0x10D56, 0x4E20, 0x0)

    def lambda_94DC():
        OP_9E(0xFE, 0x28, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_94DC)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x0, 0x7D0, 0x2710, 0x64)

    def lambda_950C():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_950C)

    def lambda_952A():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_952A)

    def lambda_9548():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_9548)

    def lambda_9566():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_9566)

    def lambda_9584():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_9584)

    def lambda_95A2():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_95A2)

    def lambda_95C0():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_95C0)

    def lambda_95DE():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_95DE)

    def lambda_95FC():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_95FC)

    def lambda_961A():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_961A)

    def lambda_9638():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_9638)

    def lambda_9656():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_9656)
    Sleep(100)
    PlayEffect(0x2, 0x0, 0xFF, 187810, -250, 68250, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_82(0x0, 0x2)

    def lambda_96B6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_96B6)

    def lambda_96C4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_96C4)

    def lambda_96D2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_96D2)

    def lambda_96E0():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_96E0)

    def lambda_96EE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_96EE)

    def lambda_96FC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_96FC)

    def lambda_970A():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_970A)

    def lambda_9718():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_9718)

    def lambda_9726():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_9726)

    def lambda_9734():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_9734)

    def lambda_9742():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_9742)

    def lambda_9750():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_9750)
    Sleep(1400)
    Fade(100)
    SetChrChipByIndex(0xF, 18)
    SetChrSubChip(0xF, 5)
    OP_99(0xF, 0x5, 0x1, 0x5DC)
    OP_22(0x11F, 0x0, 0x64)

    def lambda_9780():
        OP_6D(188840, -250, 68280, 3000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9780)

    def lambda_9798():
        OP_6B(3180, 3000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_9798)

    def lambda_97A8():
        OP_67(0, 4100, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_97A8)
    OP_7C(0x12C, 0x0, 0x1770, 0x3E8)
    Sleep(1000)
    OP_7C(0xC8, 0x0, 0x1194, 0x3E8)
    Sleep(1000)
    OP_7C(0x64, 0x0, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 18)
    SetChrSubChip(0xF, 0)
    Sleep(50)
    SetChrChipByIndex(0xF, 0)
    SetChrSubChip(0xF, 0)

    def lambda_9824():

        label("loc_9824")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_9824")

    QueueWorkItem2(0xF, 0, lambda_9824)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9857")

    ChrTalk(    #412
        0x107,
        "#065F#6P哎、哎呀！\x02",
    )

    CloseMessageWindow()

    label("loc_9857")


    ChrTalk(    #413
        0x101,
        "#1005F#6P那、那是什么！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_989C")

    ChrTalk(    #414
        0x106,
        "#550F#6P我怎么知道！\x02",
    )

    CloseMessageWindow()

    label("loc_989C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98D0")

    ChrTalk(    #415
        0x103,
        "#023F#6P这家伙是这个巢穴的主人？\x02",
    )

    CloseMessageWindow()

    label("loc_98D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9900")

    ChrTalk(    #416
        0x108,
        "#070F#6P哈哈，这还真是吓人。\x02",
    )

    CloseMessageWindow()

    label("loc_9900")


    ChrTalk(    #417
        0x102,
        (
            "#1043F#6P先不管它的来历……\x02\x03",

            "可以肯定的是我们不受它的欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x101,
        "#1020F#6P！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9987")

    ChrTalk(    #419
        0x103,
        "#024F#6P艾丝蒂尔，敌人来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_99E0")

    label("loc_9987")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_99B4")

    ChrTalk(    #420
        0x108,
        "#076F#6P喂，敌人来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_99E0")

    label("loc_99B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_99E0")

    ChrTalk(    #421
        0x106,
        "#054F#6P小心，敌人来了！\x02",
    )

    CloseMessageWindow()

    label("loc_99E0")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xF, 0x0)
    SetChrChipByIndex(0xF, 0)
    SetChrSubChip(0xF, 1)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_9A02():
        OP_96(0xF, 0x2DFC8, 0xFFFFFF06, 0xFC80, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9A02)

    def lambda_9A20():
        OP_99(0xFE, 0x1, 0x3, 0x5DC)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_9A20)

    def lambda_9A30():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9A30)

    def lambda_9A45():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9A45)

    def lambda_9A5A():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9A5A)

    def lambda_9A6F():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9A6F)

    def lambda_9A84():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9A84)

    def lambda_9A99():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9A99)

    def lambda_9AAE():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9AAE)

    def lambda_9AC3():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9AC3)

    def lambda_9AD8():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9AD8)

    def lambda_9AED():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9AED)

    def lambda_9B02():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_9B02)

    def lambda_9B17():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_9B17)
    Sleep(300)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xE, 0xFF)
    Battle(0xEDB, 0x0, 0x0, 0x0, 0xFF)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_9B95"),
        (SWITCH_DEFAULT, "loc_9B9A"),
    )


    label("loc_9B95")

    OP_B4(0x0)
    Jump("loc_9B9A")

    label("loc_9B9A")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_6D(189040, -250, 72180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_D2(0x7051E, 0x70525, 0x5)
    SetChrPos(0x101, 188750, -150, 63910, 0)
    SetChrPos(0x102, 187450, -250, 64030, 0)
    SetChrPos(0xF8, 189850, 0, 63000, 0)
    SetChrPos(0xF9, 186360, -140, 63140, 0)
    SetChrChipByIndex(0xE, 5)
    SetChrSubChip(0xE, 3)
    SetChrPos(0xE, 187650, 0, 60830, 0)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)

    def lambda_9CC7():
        OP_6D(189040, -250, 65180, 4000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9CC7)
    FadeToBright(1000, 0)
    WaitChrThread(0xE, 0x1)

    ChrTalk(    #422
        0x101,
        "#1021F#3P干、干掉了……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x102,
        "#1042F#3P嗯……总算。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D55")

    ChrTalk(    #424
        0x107,
        (
            "#561F呼……\x01",
            "终、终于结束了呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D9F")

    ChrTalk(    #425
        0x103,
        (
            "#026F魔兽的气息也已经没有了……\x02\x03",

            "好像分出胜负了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E32")

    label("loc_9D9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DEB")

    ChrTalk(    #426
        0x108,
        (
            "#070F周围已经没魔兽的气息了……\x02\x03",

            "似乎平安地解决了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E32")

    label("loc_9DEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E32")

    ChrTalk(    #427
        0x106,
        (
            "#050F魔兽的气息也已经没有了……\x02\x03",

            "看来胜负已见分晓。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E32")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_22(0xD5, 0x0, 0x64)
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #428
        0x101,
        (
            "#1004F#3P对、对了！\x01",
            "利吉先生他！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E92():
        OP_6D(188340, 0, 61600, 1500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9E92)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)

    def lambda_9EB4():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_9EB4)
    Sleep(50)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)

    def lambda_9ED1():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9ED1)
    Sleep(50)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)

    def lambda_9EEE():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_9EEE)
    Sleep(700)
    WaitChrThread(0xE, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F43")

    ChrTalk(    #429
        0x103,
        (
            "#027F没事的……\x01",
            "只是因为用尽力气而晕过去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F6E")

    label("loc_9F43")


    ChrTalk(    #430
        0x102,
        (
            "#1040F看来是\x01",
            "因为用尽力气而晕过去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FA7")

    ChrTalk(    #431
        0x107,
        (
            "#065F不过，得赶快\x01",
            "把他带回城里……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A046")

    label("loc_9FA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FFA")

    ChrTalk(    #432
        0x108,
        (
            "#070F总之先把他带回城里。\x02\x03",

            "说不定\x01",
            "哪里受了内伤也是有可能的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A046")

    label("loc_9FFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A046")

    ChrTalk(    #433
        0x106,
        (
            "#552F赶快把他带回城里吧。\x02\x03",

            "总之现在要\x01",
            "让他躺在床上休养。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A046")


    ChrTalk(    #434
        0x101,
        "#1000F嗯，说得也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x102,
        (
            "#1040F那就和矿工们会合后\x01",
            "返回地面上吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A0B3")

    ChrTalk(    #436
        0x103,
        "#020F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A0FE")

    label("loc_A0B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A0D9")

    ChrTalk(    #437
        0x106,
        "#051F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A0FE")

    label("loc_A0D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A0FE")

    ChrTalk(    #438
        0x108,
        "#070F好，回去吧。\x02",
    )

    CloseMessageWindow()

    label("loc_A0FE")

    FadeToDark(2000, 0, -1)
    OP_0D()
    EventBegin(0x0)

    AnonymousTalk(    #439
        (
            "\x07\x05因导力停止现象引发的\x01",
            "玛鲁加矿山危机\x01",
            "就这样顺利平息了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_6D(53610, 0, 51680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_D2(0x7051E, 0x70525, 0x7)
    OP_D2(0x70109, 0x7010D, 0x8)
    SetChrChipByIndex(0xD, 8)
    SetChrPos(0xA, 53220, 0, 52940, 0)
    SetChrPos(0xB, 51880, 0, 53800, 0)
    SetChrPos(0x8, 53210, 0, 54100, 90)
    SetChrPos(0xD, 55190, 0, 54000, 180)
    SetChrPos(0xC, 55250, 0, 51960, 0)
    SetChrPos(0x9, 56100, 0, 52360, 0)
    TurnDirection(0xC, 0x9, 0)
    TurnDirection(0x9, 0xC, 0)
    TurnDirection(0xB, 0xA, 0)
    TurnDirection(0xA, 0xB, 0)
    SetChrChipByIndex(0xE, 7)
    SetChrSubChip(0xE, 3)
    ClearChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x20)
    OP_6F(0x1, 55)
    OP_48()
    OP_89(0x101, 54600, -4530, 57510, 180)
    OP_89(0x102, 53690, -4530, 57700, 0)
    OP_89(0xF8, 54620, -4530, 56530, 180)
    OP_89(0xF9, 53370, -4530, 57200, 180)
    OP_89(0xE, 53400, -4530, 56550, 180)
    FadeToBright(2000, 0)
    Sleep(2000)
    OP_43(0xD, 0x1, 0x0, 0x2C)
    OP_6D(54140, 0, 54820, 2000)
    Sleep(200)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 65)
    OP_70(0x1, 0x37)
    OP_73(0x1)
    Sleep(500)
    Sleep(200)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 55)
    OP_70(0x1, 0x2D)
    OP_73(0x1)
    Sleep(500)
    Sleep(200)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 45)
    OP_70(0x1, 0x23)
    OP_73(0x1)
    Sleep(500)
    Sleep(200)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 25)
    OP_70(0x1, 0xF)
    OP_73(0x1)
    Sleep(500)
    Sleep(200)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 15)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_63(0xA)
    OP_63(0xB)
    OP_63(0x8)
    OP_63(0xD)
    OP_63(0xC)
    OP_63(0x9)

    AnonymousTalk(    #440
        (
            "\x07\x05与矿工们互相庆祝了平安无事\x01",
            "并到达地面之后……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #441
        (
            "\x07\x05为了送利吉先生回城镇，\x01",
            "我们和前去汇报事件经过的矿山长一起\x01",
            "结伴前往洛连特。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_35_88BC end

    def Function_36_A4E6(): pass

    label("Function_36_A4E6")

    SetChrChipByIndex(0xFE, 7)

    def lambda_A4F1():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A4F1)

    def lambda_A501():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A501)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xE, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x2)

    def lambda_A556():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A556)
    SetChrChipByIndex(0xFE, 2)
    Return()

    # Function_36_A4E6 end

    def Function_37_A56C(): pass

    label("Function_37_A56C")

    SetChrChipByIndex(0xFE, 7)

    def lambda_A577():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A577)

    def lambda_A587():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A587)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xE, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0xE, 0x1, 0x0, 0x26)
    WaitChrThread(0xFE, 0x2)

    def lambda_A5E3():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A5E3)
    SetChrChipByIndex(0xFE, 2)
    Return()

    # Function_37_A56C end

    def Function_38_A5F9(): pass

    label("Function_38_A5F9")

    OP_6A(0xE)
    SetChrChipByIndex(0xE, 4)
    SetChrPos(0x1C, 188900, -250, 69050, 0)
    OP_96(0xFE, 0x2DD02, 0x0, 0xED9E, 0x1F4, 0x1388)
    OP_9E(0xFE, 0x96, 0x0, 0x190, 0xFA0)
    SetChrChipByIndex(0xE, 5)
    SetChrSubChip(0xFE, 3)
    OP_6A(0xFF)
    Return()

    # Function_38_A5F9 end

    def Function_39_A64A(): pass

    label("Function_39_A64A")

    OP_8E(0xFE, 0x2D492, 0x3C, 0xEBC8, 0x1388, 0x0)
    OP_8E(0xFE, 0x2E22A, 0xFFFFFF88, 0xFA1E, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_39_A64A end

    def Function_40_A67F(): pass

    label("Function_40_A67F")

    OP_8E(0xFE, 0x2D492, 0x3C, 0xEBC8, 0x1388, 0x0)
    OP_8E(0xFE, 0x2DDC0, 0xFFFFFF06, 0xFA78, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_40_A67F end

    def Function_41_A6B4(): pass

    label("Function_41_A6B4")

    OP_8E(0xFE, 0x2D492, 0x3C, 0xEBC8, 0x1388, 0x0)
    OP_8E(0xFE, 0x2E43C, 0x0, 0xF546, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_41_A6B4 end

    def Function_42_A6E9(): pass

    label("Function_42_A6E9")

    OP_8E(0xFE, 0x2D492, 0x3C, 0xEBC8, 0x1388, 0x0)
    OP_8E(0xFE, 0x2D9A6, 0xFFFFFF7E, 0xF64A, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_42_A6E9 end

    def Function_43_A71E(): pass

    label("Function_43_A71E")

    OP_6D(187810, -40, 61790, 1500)
    OP_6D(188510, -100, 63310, 2000)
    Return()

    # Function_43_A71E end

    def Function_44_A741(): pass

    label("Function_44_A741")

    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_4A(0xD, 0)
    OP_8C(0xD, 0, 400)
    Sleep(400)

    def lambda_A76E():
        OP_8C(0xA, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_A76E)

    def lambda_A77C():
        OP_8C(0xB, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_A77C)
    Sleep(400)

    def lambda_A78F():
        OP_8C(0x8, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_A78F)

    def lambda_A79D():
        OP_8C(0xC, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_A79D)
    Sleep(400)

    def lambda_A7B0():
        OP_8C(0x9, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_A7B0)
    Return()

    # Function_44_A741 end

    def Function_45_A7B9(): pass

    label("Function_45_A7B9")

    SetMapFlags(0x80)
    Sleep(30)
    OP_22(0x64, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7E7")
    OP_70(0x3, 0x19)
    OP_73(0x3)
    OP_6F(0x3, 25)
    OP_A2(0x9)
    Jump("loc_A7FB")

    label("loc_A7E7")

    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_6F(0x3, 0)
    OP_A3(0x9)

    label("loc_A7FB")

    OP_73(0x3)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #442
        (
            "\x07\x05动了控制杆也没有反应。\x01",
            "看来是导力断绝了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    TalkEnd(0xFF)
    Return()

    # Function_45_A7B9 end

    SaveToFile()

Try(main)
