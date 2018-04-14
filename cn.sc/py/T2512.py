from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2512   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2512.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '亚吉鲁',                               # 9
        '德尼斯',                               # 10
        '芙拉瑟',                               # 11
        '蕾娜',                                 # 12
        '雅莉丝',                               # 13
        '莫妮卡',                               # 14
        '米丽亚老师',                           # 15
        '米克',                                 # 16
        '强化猎兵',                             # 17
        '强化猎兵',                             # 18
        '强化猎兵',                             # 19
        '强化猎兵',                             # 20
        '罗迪',                                 # 21
        '罗伊斯',                               # 22
        '巴克斯',                               # 23
        '黛拉',                                 # 24
        '妮吉塔',                               # 25
        '目标用照相机',                         # 26
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
        'ED6_DT07/CH01360 ._CH',             # 00
        'ED6_DT07/CH01363 ._CH',             # 01
        'ED6_DT07/CH01090 ._CH',             # 02
        'ED6_DT07/CH01370 ._CH',             # 03
        'ED6_DT26/CH20208 ._CH',             # 04
        'ED6_DT07/CH01360 ._CH',             # 05
        'ED6_DT07/CH01580 ._CH',             # 06
        'ED6_DT26/CH20441 ._CH',             # 07
        'ED6_DT07/CH01370 ._CH',             # 08
        'ED6_DT07/CH01590 ._CH',             # 09
        'ED6_DT07/CH01430 ._CH',             # 0A
        'ED6_DT07/CH01080 ._CH',             # 0B
        'ED6_DT26/CH20501 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01360P._CP',             # 00
        'ED6_DT07/CH01363P._CP',             # 01
        'ED6_DT07/CH01090P._CP',             # 02
        'ED6_DT07/CH01370P._CP',             # 03
        'ED6_DT26/CH20208P._CP',             # 04
        'ED6_DT07/CH01360P._CP',             # 05
        'ED6_DT07/CH01580P._CP',             # 06
        'ED6_DT26/CH20441P._CP',             # 07
        'ED6_DT07/CH01370P._CP',             # 08
        'ED6_DT07/CH01590P._CP',             # 09
        'ED6_DT07/CH01430P._CP',             # 0A
        'ED6_DT07/CH01080P._CP',             # 0B
        'ED6_DT26/CH20501P._CP',             # 0C
    )

    DeclNpc(
        X                   = -30910,
        Z                   = 0,
        Y                   = 25940,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -28980,
        Z                   = 0,
        Y                   = 970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -60900,
        Z                   = 0,
        Y                   = -2690,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -61500,
        Z                   = 0,
        Y                   = -1880,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -60440,
        Z                   = 0,
        Y                   = 30850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -62350,
        Z                   = 0,
        Y                   = 25980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -31110,
        Z                   = 0,
        Y                   = 29000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -28350,
        Z                   = 0,
        Y                   = 29790,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        X                   = -29450,
        Z                   = 0,
        Y                   = 30290,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -30710,
        Z                   = 0,
        Y                   = 28800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -30900,
        Z                   = 300,
        Y                   = 29850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -60450,
        Z                   = 0,
        Y                   = 28840,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -61710,
        Z                   = 0,
        Y                   = 29010,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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


    DeclActor(
        TriggerX            = -29730,
        TriggerZ            = 0,
        TriggerY            = 30330,
        TriggerRange        = 400,
        ActorX              = -31730,
        ActorZ              = 1500,
        ActorY              = 30100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_376",          # 00, 0
        "Function_1_62F",          # 01, 1
        "Function_2_6E1",          # 02, 2
        "Function_3_12A5",         # 03, 3
        "Function_4_1330",         # 04, 4
        "Function_5_14E7",         # 05, 5
        "Function_6_1626",         # 06, 6
        "Function_7_18A3",         # 07, 7
        "Function_8_1B29",         # 08, 8
        "Function_9_1BCC",         # 09, 9
        "Function_10_1C17",        # 0A, 10
        "Function_11_1CA0",        # 0B, 11
        "Function_12_1D83",        # 0C, 12
        "Function_13_1E6E",        # 0D, 13
        "Function_14_1F53",        # 0E, 14
        "Function_15_200D",        # 0F, 15
        "Function_16_2012",        # 10, 16
        "Function_17_20DC",        # 11, 17
        "Function_18_2440",        # 12, 18
        "Function_19_2527",        # 13, 19
        "Function_20_25FD",        # 14, 20
        "Function_21_26CD",        # 15, 21
        "Function_22_2788",        # 16, 22
        "Function_23_280D",        # 17, 23
        "Function_24_2865",        # 18, 24
        "Function_25_28BE",        # 19, 25
        "Function_26_28C7",        # 1A, 26
        "Function_27_2CA3",        # 1B, 27
        "Function_28_2DCD",        # 1C, 28
        "Function_29_2E1C",        # 1D, 29
        "Function_30_2E6B",        # 1E, 30
        "Function_31_2EBA",        # 1F, 31
        "Function_32_2F09",        # 20, 32
        "Function_33_381A",        # 21, 33
        "Function_34_3845",        # 22, 34
        "Function_35_3877",        # 23, 35
        "Function_36_38A2",        # 24, 36
        "Function_37_38CD",        # 25, 37
        "Function_38_38F3",        # 26, 38
        "Function_39_3923",        # 27, 39
        "Function_40_392C",        # 28, 40
        "Function_41_3DC8",        # 29, 41
        "Function_42_3EFA",        # 2A, 42
        "Function_43_3F58",        # 2B, 43
        "Function_44_3FB1",        # 2C, 44
        "Function_45_400A",        # 2D, 45
        "Function_46_4063",        # 2E, 46
        "Function_47_453D",        # 2F, 47
        "Function_48_456F",        # 30, 48
        "Function_49_45A1",        # 31, 49
        "Function_50_45D3",        # 32, 50
    )


    def Function_0_376(): pass

    label("Function_0_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3DB")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, -160, 0, -940, 10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, -31700, -50, 30400, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xF, -27860, 0, 27430, 328)
    Jump("loc_548")

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, -31700, -50, 30400, 90)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0xA, -60810, 0, 29920, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 2)), scpexpr(EXPR_END)), "loc_48C")
    SetChrPos(0x10, -1570, 0, -2940, 0)
    SetChrPos(0x11, 480, 0, -3440, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 8)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 12)
    SetChrSubChip(0x11, 11)

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 4)), scpexpr(EXPR_END)), "loc_4E7")
    SetChrPos(0x12, -88920, 0, -3130, 0)
    SetChrPos(0x13, -90170, 0, -3000, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x12, 12)
    SetChrSubChip(0x12, 9)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x13, 12)
    SetChrSubChip(0x13, 14)

    label("loc_4E7")

    Jump("loc_548")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_503")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_548")

    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_517")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_548")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 4)), scpexpr(EXPR_END)), "loc_537")
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -60520, 0, -2690, 90)
    Jump("loc_548")

    label("loc_537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_548")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_55E")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_62E")

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_574")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_62E")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_58A")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 20)
    Jump("loc_62E")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_5A0")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 21)
    Jump("loc_62E")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_5B6")
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 22)
    Jump("loc_62E")

    label("loc_5B6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5CE"),
        (107, "loc_5E6"),
        (109, "loc_5FE"),
        (116, "loc_616"),
        (SWITCH_DEFAULT, "loc_62E"),
    )


    label("loc_5CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E3")
    SetMapFlags(0x10000000)
    Event(0, 25)

    label("loc_5E3")

    Jump("loc_62E")

    label("loc_5E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FB")
    SetMapFlags(0x10000000)
    Event(0, 32)

    label("loc_5FB")

    Jump("loc_62E")

    label("loc_5FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_613")
    SetMapFlags(0x10000000)
    Event(0, 39)

    label("loc_613")

    Jump("loc_62E")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62B")
    SetMapFlags(0x10000000)
    Event(0, 46)

    label("loc_62B")

    Jump("loc_62E")

    label("loc_62E")

    Return()

    # Function_0_376 end

    def Function_1_62F(): pass

    label("Function_1_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_647")
    OP_B1("t2512_y")
    Jump("loc_650")

    label("loc_647")

    OP_B1("t2512_n")

    label("loc_650")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_66C")
    OP_65(0x0, 0x1)
    OP_71(0xF, 0x4)
    OP_72(0x10, 0x4)
    Jump("loc_6A9")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_684")
    OP_71(0xF, 0x4)
    OP_72(0x10, 0x4)
    OP_65(0x0, 0x1)
    Jump("loc_6A9")

    label("loc_684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_68E")
    Jump("loc_6A9")

    label("loc_68E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_698")
    Jump("loc_6A9")

    label("loc_698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 4)), scpexpr(EXPR_END)), "loc_6A2")
    Jump("loc_6A9")

    label("loc_6A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_6A9")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_6B3")
    Jump("loc_6E0")

    label("loc_6B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_6CB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_6E0")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_6E0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_6E0")

    Return()

    # Function_1_62F end

    def Function_2_6E1(): pass

    label("Function_2_6E1")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -61000, 0, -3720, 0)
    SetChrPos(0x105, -60410, 0, -4540, 0)
    OP_51(0x19, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x19, 0x0)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_0D()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    Sleep(400)

    ChrTalk(    #0
        0x101,
        "#1000F那个……打扰一下………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        "#2P#4S那种事从来没有听说过！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_43(0x101, 0x1, 0x0, 0x3)
    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1004F（呜、呜哇……！）\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #3
        0xA,
        (
            "我之前不是早就说过，\x01",
            "放假时要在利贝尔旅行的吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "为什么事到如今\x01",
            "还说什么要我回国探亲！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        (
            "芙拉瑟，请你\x01",
            "冷静一点啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        (
            "不！我什么都不要听！\x01",
            "今天我必须要把话说清楚！\x02",
        )
    )

    CloseMessageWindow()
    OP_91(0x101, 0x0, 0x0, 0x190, 0x3E8, 0x0)

    ChrTalk(    #7
        0x101,
        "#1015F哎，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "考试好不容易才结束，\x01",
            "本以为终于可以去旅行了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        (
            "为什么要在这种时候\x01",
            "给我订帝国的往返票！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        (
            "你是和老头子串通好了\x01",
            "来整我的吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #11
        0x101,
        "#1007F（呜啊～好像插不上嘴啊。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        "#045F（暂、暂且就先旁观一会吧……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        "那个…芙拉瑟啊…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xB,
        (
            "你现在最好还是\x01",
            "什么都别说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        "最、最好什么都别说……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        "#3S最、最好什么都别说！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xA,
        (
            "仆、仆人竟然敢\x01",
            "用这种口气对主人讲话……！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_51(0x19, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_AC2():
        OP_69(0x19, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC2)
    TurnDirection(0xA, 0x101, 400)
    Sleep(400)
    TurnDirection(0xB, 0x101, 400)
    Sleep(1000)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #18
        0xA,
        "……啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1008F啊…啊哈哈～……你们好～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #20
        0xB,
        "(所以我才会那么说啊……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        "#2P咳、咳咳……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        "#2P……你们有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1016F嗯、嗯……\x01",
            "抱歉打扰你们了。\x02\x03",

            "我们这次来\x01",
            "是想调查一些事情……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "\x07\x05艾丝蒂尔表示自己正在调查\x01",
            "考试期间发生的奇异事件。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #25
        0xA,
        (
            "#2P……………………………\x01",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "原来如此，是为了\x01",
            "调查那件事而来的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        "#2P蕾娜！别再说了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xA,
        "#2P我、我不想再想起那件事了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1002F…………发生了什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        "嗯，其实…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "……在考试期间中，\x01",
            "我们目击到了奇怪的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "说具体些的话，\x01",
            "就是『在空中飞舞的人影』……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(15)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #33
        0x105,
        "#044F这……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(    #34
        0xA,
        "#2P#3S蕾娜……！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1002F……可以说得\x01",
            "再详细一点吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xB,
        "那我就说了吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #37
        0xB,
        "……可以吗？芙拉瑟。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0xA,
        "#2P呜～……随、随便你了啦！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    OP_8E(0xA, 0xFFFF1398, 0x0, 0xFFFFF57E, 0x3E8, 0x0)
    OP_51(0x19, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_ECE():
        OP_69(0x19, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ECE)
    Sleep(500)
    TurnDirection(0xB, 0x101, 400)
    Sleep(1500)

    ChrTalk(    #39
        0xB,
        (
            "那是在考试前一天\x01",
            "的深夜。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "突然就听到芙拉瑟\x01",
            "喊道『窗外有人！』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#1002F好、好像在讲校园怪谈一样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xB,
        (
            "我们打开窗子向外看去，\x01",
            "在校舍的上空确实有个人影。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "就像是被风吹动一样，\x01",
            "在天上轻飘飘地转着圈。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    def lambda_FDF():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_FDF)
    Sleep(1000)

    ChrTalk(    #44
        0xA,
        "#2P呜呜…………\x02",
    )

    CloseMessageWindow()
    OP_44(0xA, 0x3)

    ChrTalk(    #45
        0xB,
        (
            "不久之后人影就消失在\x01",
            "校舍的深处不见了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #46
        0xB,
        (
            "……真正不得了的事情\x01",
            "还在后边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        (
            "受到惊吓的大小姐\x01",
            "拼命往我的被子里钻……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_44(0xA, 0x3)

    def lambda_10B3():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1770)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10B3)
    TurnDirection(0xA, 0xB, 10000)

    ChrTalk(    #48
        0xA,
        (
            "#2P#3S那、那种事\x01",
            "就没必要说了！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1016F啊，那种事不说也没关系啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        "哎呀，是这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xB,
        (
            "真遗憾……\x01",
            "其实接下来的事情更有意思呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1015F嗯、嗯，\x01",
            "那么……就来整理一下证言吧。\x02\x03",

            "人影出现在校舍的上空，\x01",
            "然后就在校舍深处消失了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        "嗯，就是那样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        "对你们有用吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1018F是的，知道这些就已经足够了。\x01",
            "谢谢你们二位的合作。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #56
        0x105,
        "#040F很有力的目击证词啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #57
        0x101,
        (
            "#1006F是啊……\x01",
            "马上记录到笔记上吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 0)
    SetChrFlags(0xA, 0x10)
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    EventEnd(0x0)
    Return()

    # Function_2_6E1 end

    def Function_3_12A5(): pass

    label("Function_3_12A5")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x101, 0x0, 0x0, 0xFFFFFF38, 0x190, 0x1770)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x101, 0x0, 0x0, 0xFFFFFF9C, 0x12C, 0x1770)
    OP_95(0x101, 0x0, 0x0, 0xFFFFFF9C, 0x64, 0x1770)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Return()

    # Function_3_12A5 end

    def Function_4_1330(): pass

    label("Function_4_1330")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 5)), scpexpr(EXPR_END)), "loc_13E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1395")

    ChrTalk(    #58
        0xFE,
        (
            "竟、竟然\x01",
            "会发生这种事件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "这样的话\x01",
            "如果不早点向蕾娜\x01",
            "道歉的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_13E4")

    label("loc_1395")


    ChrTalk(    #60
        0xFE,
        (
            "这样的话\x01",
            "如果不早点向蕾娜\x01",
            "道歉的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "拜托了，\x01",
            "请一定别出什么事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E4")

    Jump("loc_14E3")

    label("loc_13E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1473")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_142B")

    ChrTalk(    #62
        0xFE,
        (
            "我一定要去\x01",
            "旅行的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "怎么能回家去探亲。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1470")

    label("loc_142B")

    OP_A2(0x2)

    ChrTalk(    #64
        0xFE,
        (
            "我一定要去\x01",
            "旅行的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "哎哎，你只要不跟来\x01",
            "不就可以了吗！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1470")

    Jump("loc_14E3")

    label("loc_1473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_14E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 4)), scpexpr(EXPR_END)), "loc_14D6")

    ChrTalk(    #66
        0xFE,
        "呜呜呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "又把当时的事情\x01",
            "全部想起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "呼，本来已经都\x01",
            "忘干净了…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E3")

    label("loc_14D6")

    OP_A2(0x1234)
    OP_28(0x83, 0x1, 0x20)
    Call(0, 2)

    label("loc_14E3")

    TalkEnd(0xFE)
    Return()

    # Function_4_1330 end

    def Function_5_14E7(): pass

    label("Function_5_14E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_14F4")
    Jump("loc_1622")

    label("loc_14F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_15AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_154F")

    ChrTalk(    #69
        0xFE,
        (
            "要是小姐能老老实实回去\x01",
            "就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "在社交界中还有\x01",
            "很多交际活动呢…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A7")

    label("loc_154F")

    OP_A2(0x3)

    ChrTalk(    #71
        0xFE,
        (
            "小姐如果再继续故意任性的话\x01",
            "又会让老爷不高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "本来关系就已经很紧张了……\x02",
    )

    CloseMessageWindow()

    label("loc_15A7")

    Jump("loc_1622")

    label("loc_15AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_1622")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 4)), scpexpr(EXPR_END)), "loc_1615")

    ChrTalk(    #73
        0xFE,
        (
            "真希望芙拉瑟\x01",
            "的态度能改变一下啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "就算拥有高贵的血统，\x01",
            "也还是低调一点比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1622")

    label("loc_1615")

    OP_A2(0x1234)
    OP_28(0x83, 0x1, 0x20)
    Call(0, 2)

    label("loc_1622")

    TalkEnd(0xFE)
    Return()

    # Function_5_14E7 end

    def Function_6_1626(): pass

    label("Function_6_1626")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_16F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169E")

    ChrTalk(    #75
        0xFE,
        (
            "大家因为这次的事件\x01",
            "都心慌意乱，正是大好机会啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "我要趁现在拼命学习，\x01",
            "把差距继续扩大。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_16F6")

    label("loc_169E")


    ChrTalk(    #77
        0xFE,
        (
            "校园生活的准备工作\x01",
            "和我一点关系也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "那是职员们的工作，\x01",
            "我们学生没必要管。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F6")

    Jump("loc_189F")

    label("loc_16F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_17A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1755")

    ChrTalk(    #79
        0xFE,
        (
            "社团活动之类的东西\x01",
            "也没有什么意义。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "学生的首要任务只有学习而已。\x02",
    )

    CloseMessageWindow()
    Jump("loc_17A0")

    label("loc_1755")

    OP_A2(0x1)

    ChrTalk(    #81
        0xFE,
        (
            "呵呵，大家努力参加\x01",
            "社团活动就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "在那期间\x01",
            "我会拼命学习的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A0")

    Jump("loc_189F")

    label("loc_17A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_17F9")

    ChrTalk(    #83
        0xFE,
        (
            "嗯，这次考试的分数\x01",
            "也快下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "我的成绩排名前列\x01",
            "肯定是没问题的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189F")

    label("loc_17F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_189F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_184B")

    ChrTalk(    #85
        0xFE,
        "没别的事了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "那就别再打扰我了，\x01",
            "我正在挑选参考书呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189F")

    label("loc_184B")

    OP_A2(0x1)

    ChrTalk(    #87
        0xFE,
        (
            "干什么？\x01",
            "现在忙得很啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "……考试期间的奇异事件？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "好像没什么哦。\x02",
    )

    CloseMessageWindow()

    label("loc_189F")

    TalkEnd(0xFE)
    Return()

    # Function_6_1626 end

    def Function_7_18A3(): pass

    label("Function_7_18A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_19EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199A")

    ChrTalk(    #90
        0xFE,
        (
            "啊，游击士……\x01",
            "刚才干得漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "虽然事件总算是顺利解决了，\x01",
            "但接下来也很让人头疼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "导力器现在无法运转……\x01",
            "照明设施几乎完全瘫痪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "也就是说，今天开始\x01",
            "每天晚上都是漆黑一团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "呼呼呼……\x01",
            "我很期待呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_19E8")

    label("loc_199A")


    ChrTalk(    #95
        0xFE,
        (
            "一团漆黑的话\x01",
            "总觉得很安祥平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "呵呵呵……\x01",
            "没有灯火的夜晚最美丽了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E8")

    Jump("loc_1B25")

    label("loc_19EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1AA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A46")

    ChrTalk(    #97
        0xFE,
        (
            "明白了吧？\x01",
            "是那个啦，那个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "呵呵呵……\x01",
            "大概是什么东西的怨灵吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9F")

    label("loc_1A46")

    OP_A2(0x0)

    ChrTalk(    #99
        0xFE,
        (
            "最近学院中的气氛\x01",
            "很怪异呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "也许那种东西\x01",
            "会出来也说不定吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "呼呼呼……\x02",
    )

    CloseMessageWindow()

    label("loc_1A9F")

    Jump("loc_1B25")

    label("loc_1AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_1B25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AD6")

    ChrTalk(    #102
        0xFE,
        (
            "呼呼呼……\x01",
            "啊，我也不知道啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B25")

    label("loc_1AD6")

    OP_A2(0x0)

    ChrTalk(    #103
        0xFE,
        (
            "考试期间的奇异事件…\x01",
            "好像没有，但…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "呼呼呼……\x01",
            "啊，我也不知道啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B25")

    TalkEnd(0xFE)
    Return()

    # Function_7_18A3 end

    def Function_8_1B29(): pass

    label("Function_8_1B29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 3)), scpexpr(EXPR_END)), "loc_1BC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB4")

    ChrTalk(    #105
        0xFE,
        (
            "就算有什么骚动\x01",
            "我们也会在这里不动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "贸然行动的话，\x01",
            "只会拖你们的后腿而已吧…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "那么，\x01",
            "要小心行事啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1BC8")

    label("loc_1BB4")


    ChrTalk(    #108
        0xFE,
        "要小心行事啊！\x02",
    )

    CloseMessageWindow()

    label("loc_1BC8")

    TalkEnd(0xFE)
    Return()

    # Function_8_1B29 end

    def Function_9_1BCC(): pass

    label("Function_9_1BCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 3)), scpexpr(EXPR_END)), "loc_1C13")

    ChrTalk(    #109
        0xFE,
        (
            "按照你们的指示，\x01",
            "我们就在这里待命了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "大家多保重。\x02",
    )

    CloseMessageWindow()

    label("loc_1C13")

    TalkEnd(0xFE)
    Return()

    # Function_9_1BCC end

    def Function_10_1C17(): pass

    label("Function_10_1C17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 5)), scpexpr(EXPR_END)), "loc_1C9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C79")

    ChrTalk(    #111
        0xFE,
        (
            "请、请一定把大家\x01",
            "都救出来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "我也会在这里祈祷\x01",
            "大家平安无事的…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_1C9C")

    label("loc_1C79")


    ChrTalk(    #113
        0xFE,
        (
            "请、请一定把大家\x01",
            "都救出来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9C")

    TalkEnd(0xFE)
    Return()

    # Function_10_1C17 end

    def Function_11_1CA0(): pass

    label("Function_11_1CA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 5)), scpexpr(EXPR_END)), "loc_1D7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D33")

    ChrTalk(    #114
        0xFE,
        (
            "听你们的，\x01",
            "我就在这里不动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "呼，基诺奇奥那小子\x01",
            "没有乱来虽然很好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "但他那种轻率的性格\x01",
            "还是很让人担心啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_1D7F")

    label("loc_1D33")


    ChrTalk(    #117
        0xFE,
        (
            "听你们的，\x01",
            "我就在这里不动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "基诺奇奥那小子也\x01",
            "没有乱来虽然很好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D7F")

    TalkEnd(0xFE)
    Return()

    # Function_11_1CA0 end

    def Function_12_1D83(): pass

    label("Function_12_1D83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E26")

    ChrTalk(    #119
        0xFE,
        (
            "夜晚使用的油灯\x01",
            "已经准备好了阿⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "但遗憾的是没有\x01",
            "可爱些的灯台啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "真想早点找到一个草莓色的\x01",
            "可爱灯台呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "一会去找坎诺\x01",
            "聊聊吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1E6A")

    label("loc_1E26")


    ChrTalk(    #123
        0xFE,
        (
            "真想要个草莓色的\x01",
            "可爱灯台啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "嘿嘿，一会赶快去找\x01",
            "坎诺吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E6A")

    TalkEnd(0xFE)
    Return()

    # Function_12_1D83 end

    def Function_13_1E6E(): pass

    label("Function_13_1E6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF7")

    ChrTalk(    #125
        0xFE,
        (
            "最近怎么总出\x01",
            "事啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "雅莉丝已经准备好\x01",
            "油灯了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "灯台虽然没有\x01",
            "中意的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "……不过暂时\x01",
            "不去管它了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1F4F")

    label("loc_1EF7")


    ChrTalk(    #129
        0xFE,
        (
            "虽然最近全都是\x01",
            "那种事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "雅莉丝已经准备好\x01",
            "油灯了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "真是乐天的性格啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1F4F")

    TalkEnd(0xFE)
    Return()

    # Function_13_1E6E end

    def Function_14_1F53(): pass

    label("Function_14_1F53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2009")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC4")

    ChrTalk(    #132
        0xFE,
        "还是这么平静。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "他现在是因为\x01",
            "过度疲劳导致的昏倒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "还不确定什么时候能醒来。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2009")

    label("loc_1FC4")


    ChrTalk(    #135
        0xFE,
        (
            "他现在是因为\x01",
            "过度疲劳导致的昏倒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "还不确定什么时候能醒来。\x02",
    )

    CloseMessageWindow()

    label("loc_2009")

    TalkEnd(0xFE)
    Return()

    # Function_14_1F53 end

    def Function_15_200D(): pass

    label("Function_15_200D")

    Call(0, 16)
    Return()

    # Function_15_200D end

    def Function_16_2012(): pass

    label("Function_16_2012")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_209D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_206E")

    ChrTalk(    #137
        0x16,
        "嗯嗯～………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x16,
        "呼呼…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0xFFFFFED4, 1800, 0x1C, 0x21, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x16)
    OP_A2(0x9)
    Jump("loc_209A")

    label("loc_206E")


    ChrTalk(    #139
        0x16,
        "呼呼…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0xFFFFFED4, 1800, 0x1C, 0x21, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x16)

    label("loc_209A")

    Jump("loc_20D8")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 3)), scpexpr(EXPR_END)), "loc_20D8")

    ChrTalk(    #140
        0x16,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0xFFFFFED4, 1800, 0x1C, 0x21, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x16)

    label("loc_20D8")

    TalkEnd(0x16)
    Return()

    # Function_16_2012 end

    def Function_17_20DC(): pass

    label("Function_17_20DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C7")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #141
        0xFE,
        "啊，是艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "真是谢谢你们了。\x01",
            "不然还不知会怎么样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1006F哪里，全靠协会的通知\x01",
            "我们才能及时赶到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        (
            "#1043F确实啊……\x02\x03",

            "要是没有援军的话\x01",
            "战斗肯定会很惨烈的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xFE, 0x102, 0)
    Sleep(400)

    ChrTalk(    #145
        0xFE,
        (
            "不、不要啊。\x01",
            "我那个只是偶然。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "并不是和大叔一样\x01",
            "的勇敢行为……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1002F勤务员先生怎么样了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #148
        0xFE,
        (
            "啊啊…\x01",
            "没有生命危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "只是疲劳过度，\x01",
            "大概还要睡一阵子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#1007F太好了，这样\x01",
            "就不用再担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "松了一口气呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "大叔的事情就\x01",
            "交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "不好好照看他的话\x01",
            "实在是过意不去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1025F是哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x102,
        "#1040F嗯，那就拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "那么，有机会的话\x01",
            "还要再来学院啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "艾丝蒂尔的话\x01",
            "我们随时都欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        "#1006F嗯，一言为定。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x102,
        "#1040F到时多关照关照了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20D4)
    Jump("loc_243C")

    label("loc_23C7")


    ChrTalk(    #160
        0xFE,
        (
            "我也这就要去\x01",
            "给大叔道歉了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "不管怎么说，\x01",
            "毕竟一个人逃跑也是事实……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "不好好照看他的话\x01",
            "实在是过意不去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243C")

    TalkEnd(0xFE)
    Return()

    # Function_17_20DC end

    def Function_18_2440(): pass

    label("Function_18_2440")

    EventBegin(0x0)
    OP_D2(0x26000E, 0x260013, 0x16)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x10, 600, 0, -2740, 270)
    SetChrPos(0x11, -1130, 0, -2730, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)
    OP_6D(4730, -250, -1620, 0)
    OP_67(0, 5870, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(315000, 0)
    OP_6E(277, 0)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    FadeToBright(1000, 0)
    OP_6D(-1280, -250, -1580, 3000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2500   ._SN", 124, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2440 end

    def Function_19_2527(): pass

    label("Function_19_2527")

    EventBegin(0x0)
    OP_D2(0x26000E, 0x260013, 0x16)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x10, 600, 0, -2740, 270)
    SetChrPos(0x11, -1130, 0, -2730, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)
    OP_6D(-1280, -250, -1580, 0)
    OP_67(0, 5870, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    FadeToBright(1000, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2500   ._SN", 124, 0, 0)
    IdleLoop()
    Return()

    # Function_19_2527 end

    def Function_20_25FD(): pass

    label("Function_20_25FD")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x14, -29450, 0, 30290, 270)
    SetChrPos(0x15, -30710, 0, 28800, 0)
    SetChrPos(0x16, -31700, -50, 30400, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    OP_71(0xF, 0x4)
    OP_72(0x10, 0x4)
    OP_6D(-31890, 0, 30730, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2500   ._SN", 124, 0, 0)
    IdleLoop()
    Return()

    # Function_20_25FD end

    def Function_21_26CD(): pass

    label("Function_21_26CD")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x17, -60450, 0, 28840, 315)
    SetChrPos(0x18, -61710, 0, 29010, 45)
    SetChrPos(0xA, -60810, 0, 29920, 180)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0xA, 255)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_6D(-60840, 0, 29610, 0)
    OP_67(0, 6520, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10FC)
    NewScene("ED6_DT21/T2500   ._SN", 123, 0, 0)
    IdleLoop()
    Return()

    # Function_21_26CD end

    def Function_22_2788(): pass

    label("Function_22_2788")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_D2(0x26000E, 0x260013, 0x16)
    OP_43(0x10, 0x1, 0x0, 0x17)
    OP_43(0x11, 0x1, 0x0, 0x18)
    OP_6D(-89450, 0, -3010, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10FD)
    NewScene("ED6_DT21/T2500   ._SN", 123, 0, 0)
    IdleLoop()
    Return()

    # Function_22_2788 end

    def Function_23_280D(): pass

    label("Function_23_280D")

    SetChrPos(0x10, -90230, -250, -6440, 180)
    SetChrChipByIndex(0x10, 22)
    ClearChrFlags(0x10, 0x80)

    label("loc_2828")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2864")
    OP_8C(0x10, 90, 400)
    Sleep(700)
    OP_8C(0x10, 0, 400)
    Sleep(700)
    OP_8C(0x10, 270, 400)
    Sleep(700)
    OP_8C(0x10, 180, 400)
    Sleep(700)
    Jump("loc_2828")

    label("loc_2864")

    Return()

    # Function_23_280D end

    def Function_24_2865(): pass

    label("Function_24_2865")

    SetChrPos(0x11, -87160, 0, -3040, 270)
    ClearChrFlags(0x11, 0x80)

    label("loc_287B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28BD")
    OP_8E(0x11, 0xFFFE90EE, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_8E(0x11, 0xFFFEAB88, 0x0, 0xFFFFF420, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Jump("loc_287B")

    label("loc_28BD")

    Return()

    # Function_24_2865 end

    def Function_25_28BE(): pass

    label("Function_25_28BE")

    Call(0, 26)
    Call(0, 27)
    Return()

    # Function_25_28BE end

    def Function_26_28C7(): pass

    label("Function_26_28C7")

    EventBegin(0x0)
    OP_D2(0x270110, 0x270120, 0xD)
    OP_D2(0x270111, 0x270121, 0xE)
    OP_D2(0x270130, 0x270140, 0xF)
    OP_D2(0x270131, 0x270141, 0x10)
    OP_D2(0x70326, 0x7032D, 0x11)
    OP_D2(0x70327, 0x7032E, 0x12)
    OP_D2(0x70318, 0x7031F, 0x13)
    OP_D2(0x70319, 0x70320, 0x14)
    OP_D2(0x26000E, 0x260013, 0x16)
    OP_D2(0x270327, 0x270331, 0x17)
    OP_D2(0x270313, 0x27031D, 0x18)
    OP_D2(0x270326, 0x270330, 0x19)
    OP_D2(0x270312, 0x27031C, 0x1A)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    SetChrPos(0x10, 600, 0, -2740, 270)
    SetChrPos(0x11, -1130, 0, -2730, 90)
    SetChrChipByIndex(0x10, 4)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_6D(-1830, -250, -1580, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(315000, 0)
    OP_6E(301, 0)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_63(0x10)

    def lambda_2A27():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2A27)
    Sleep(100)
    OP_63(0x11)

    def lambda_2A3D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2A3D)
    Sleep(400)

    def lambda_2A50():
        OP_6D(-1210, 0, -4610, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A50)
    OP_43(0x101, 0x1, 0x0, 0x1C)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x1D)
    Sleep(200)
    OP_43(0x10A, 0x1, 0x0, 0x1E)
    Sleep(200)
    OP_43(0x10E, 0x1, 0x0, 0x1F)
    WaitChrThread(0x10E, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)

    ChrTalk(    #163
        0x10,
        "#2P……你们是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x11,
        (
            "#5P哼，还有没抓到的\x01",
            "漏网学生吗──\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #165
        0x10,
        "#2P那、那个徽章是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x11,
        "#5P游、游击士！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10E,
        "#845F#6P没错！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 13)
    SetChrChipByIndex(0x102, 15)
    SetChrChipByIndex(0x10A, 17)
    SetChrChipByIndex(0x10E, 19)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10A, 0)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #168
        0x10A,
        (
            "#815F#6P你们\x01",
            "觉悟吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2BB4():
        OP_6D(-1230, 0, -3110, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2BB4)

    def lambda_2BCC():
        OP_6B(2600, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2BCC)

    def lambda_2BDC():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BDC)
    Sleep(20)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 25)
    SetChrSubChip(0x11, 0)

    def lambda_2C0B():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C0B)
    Sleep(20)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x11, 26)
    SetChrSubChip(0x11, 0)

    def lambda_2C3A():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2C3A)
    Sleep(20)

    def lambda_2C5A():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_2C5A)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x102, 0xFF)
    Battle(0x79B, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2C9D"),
        (SWITCH_DEFAULT, "loc_2CA2"),
    )


    label("loc_2C9D")

    OP_B4(0x0)
    Jump("loc_2CA2")

    label("loc_2CA2")

    Return()

    # Function_26_28C7 end

    def Function_27_2CA3(): pass

    label("Function_27_2CA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(390, 0, -5570, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    SetChrPos(0x0, 390, 0, -5570, 0)
    SetChrPos(0x1, 390, 0, -5570, 0)
    SetChrPos(0x2, 390, 0, -5570, 0)
    SetChrPos(0x3, 390, 0, -5570, 0)
    OP_69(0x0, 0x0)
    SetChrPos(0x10, -1570, 0, -2940, 0)
    SetChrPos(0x11, 480, 0, -3440, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 8)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 12)
    SetChrSubChip(0x11, 11)
    OP_A2(0x202A)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_27_2CA3 end

    def Function_28_2DCD(): pass

    label("Function_28_2DCD")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 860, -500, -9240, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2DF4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DF4)
    OP_8E(0xFE, 0x2DA, 0xFFFFFF06, 0xFFFFE2E6, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_28_2DCD end

    def Function_29_2E1C(): pass

    label("Function_29_2E1C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -290, -500, -9230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2E43():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E43)
    OP_8E(0xFE, 0xFFFFFE2A, 0xFFFFFF06, 0xFFFFE2A0, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_29_2E1C end

    def Function_30_2E6B(): pass

    label("Function_30_2E6B")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 860, -500, -9240, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2E92():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E92)
    OP_8E(0xFE, 0x4EC, 0xFFFFFEF2, 0xFFFFDE86, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_30_2E6B end

    def Function_31_2EBA(): pass

    label("Function_31_2EBA")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -290, -500, -9230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2EE1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EE1)
    OP_8E(0xFE, 0xFFFFFE52, 0xFFFFFECA, 0xFFFFDE86, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_31_2EBA end

    def Function_32_2F09(): pass

    label("Function_32_2F09")

    EventBegin(0x0)
    OP_D2(0x7031D, 0x70324, 0xE)
    OP_D2(0x7031E, 0x70325, 0x10)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    SetChrPos(0x14, -29450, 0, 30290, 270)
    SetChrPos(0x15, -30710, 0, 28800, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, -31700, -50, 30400, 90)
    OP_71(0xF, 0x4)
    OP_72(0x10, 0x4)
    OP_6D(-31660, 0, 30680, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    LoadEffect(0x0, "Craft\\\\cr000_00.eff")
    LoadEffect(0x1, "magic\\\\mg112_0.eff")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_3013():
        OP_6D(-30540, 0, 29960, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3013)

    def lambda_302B():
        OP_67(0, 5780, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_302B)

    def lambda_3043():
        OP_6B(2160, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3043)

    def lambda_3053():
        OP_6E(381, 2500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3053)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_307A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_307A)
    Sleep(100)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_30A4():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_30A4)
    OP_43(0x101, 0x1, 0x0, 0x21)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x22)
    Sleep(300)
    OP_43(0x10A, 0x1, 0x0, 0x23)
    Sleep(300)
    OP_43(0x10E, 0x1, 0x0, 0x24)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x10A, 0x1)

    ChrTalk(    #169
        0x14,
        "#5P你、你们……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x15,
        (
            "#5P你们不是艾丝蒂尔\x01",
            "和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "#1006F#6P二位，好久不见了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x102,
        (
            "#1040F#6P长话短说，先把事情\x01",
            "做个简单说明吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #173
        (
            "\x07\x05将作战计划，以及解救人质\x01",
            "的经过向大家说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #174
        0x14,
        (
            "#5P是、是这样啊……\x02\x03",

            "哇～游击士\x01",
            "果然威风啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#1016F#6P哪、哪里。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 315, 400)
    Sleep(500)

    ChrTalk(    #176
        0x101,
        (
            "#1002F#6P──对了，\x01",
            "勤务员要不要紧？\x02\x03",

            "听说他遭到了枪击……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10E, 315, 400)

    ChrTalk(    #177
        0x15,
        (
            "#5P嗯，不过幸好\x01",
            "伤得不太重……\x02\x03",

            "给他做了包扎之后\x01",
            "就昏睡过去了。\x02\x03",

            "新学期才刚开始，\x01",
            "本来正是大叔该忙的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#1007F#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x102,
        (
            "#1043F#6P脸色很不好，\x01",
            "似乎是因为疲劳过度了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x10E,
        "#840F#6P嗯……让我来吧。\x02",
    )

    CloseMessageWindow()

    def lambda_3343():
        OP_6D(-31390, 0, 30690, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3343)
    OP_43(0x102, 0x0, 0x0, 0x25)
    Sleep(300)
    OP_43(0x10E, 0x0, 0x0, 0x26)
    Sleep(150)

    def lambda_3373():

        label("loc_3373")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_3373")

    QueueWorkItem2(0x101, 1, lambda_3373)
    Sleep(50)

    def lambda_3389():

        label("loc_3389")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_3389")

    QueueWorkItem2(0x10A, 1, lambda_3389)
    Sleep(50)

    def lambda_339F():

        label("loc_339F")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_339F")

    QueueWorkItem2(0x15, 1, lambda_339F)
    Sleep(50)

    def lambda_33B5():

        label("loc_33B5")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_33B5")

    QueueWorkItem2(0x14, 1, lambda_33B5)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x14, 0x1)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0x10E, 0)
    SetChrChipByIndex(0x10E, 14)
    OP_0D()
    Sleep(500)

    ChrTalk(    #181
        0x10E,
        "#843F#6P方术──稳泛沧浪海天阔。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10E, 0)
    SetChrChipByIndex(0x10E, 16)
    OP_51(0x10E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x10E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    PlayEffect(0x0, 0x0, 0x10E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x0, 0x2)
    PlayEffect(0x1, 0x1, 0x16, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_34BB():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34BB)
    Sleep(100)

    def lambda_34CE():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34CE)
    Sleep(100)

    def lambda_34E1():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_34E1)
    Sleep(100)

    def lambda_34F4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_34F4)
    Sleep(100)
    OP_8C(0x14, 270, 400)
    OP_83(0x1, 0x2)

    def lambda_3511():
        OP_6D(-31070, 0, 30140, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3511)
    SetChrSubChip(0x10E, 0)
    SetChrChipByIndex(0x10E, 65535)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #182
        0x101,
        "#1004F#6P哇哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x102,
        "#1040F好厉害的法术。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x10A,
        (
            "#811F#6P嘿嘿，前辈的方术\x01",
            "可是帮了我们无数次大忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x14,
        (
            "#2P啊，大叔的脸色\x01",
            "确实比刚才好多了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x15,
        (
            "#5P嗯，让他继续静养\x01",
            "一阵就会没事了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 135, 400)
    Sleep(300)

    ChrTalk(    #187
        0x15,
        (
            "#5P──各位。\x01",
            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3624():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3624)
    Sleep(100)
    OP_8C(0x14, 135, 400)

    ChrTalk(    #188
        0x15,
        (
            "#5P有什么事情可以\x01",
            "让我们帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x102,
        (
            "#1054F#4P不好意思，可以的话\x01",
            "还是希望你们先待在这里。\x02\x03",

            "外边现在还很危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x15,
        "#5P是吗……那好吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x14,
        "#5P你们也要小心啊！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #192
        (
            "\x07\x05取出游击士手册，\x01",
            "在罗迪、罗伊斯、巴克斯勤务员\x01",
            "的名字上做了标记了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x202B)
    OP_28(0xC0, 0x1, 0x1000)
    OP_28(0xC1, 0x2, 0x40)
    OP_28(0xC1, 0x1, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_8C(0x15, 0, 0)
    OP_8C(0x14, 270, 0)
    OP_6D(-28710, 0, 27260, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -28730, 0, 27100, 180)
    SetChrPos(0x1, -28730, 0, 27100, 180)
    SetChrPos(0x2, -28730, 0, 27100, 180)
    SetChrPos(0x3, -28730, 0, 27100, 180)
    OP_69(0x0, 0x0)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_32_2F09 end

    def Function_33_381A(): pass

    label("Function_33_381A")

    SetChrPos(0xFE, -28530, 0, 20820, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF8D0A, 0x0, 0x6BD0, 0x1388, 0x0)
    Return()

    # Function_33_381A end

    def Function_34_3845(): pass

    label("Function_34_3845")

    SetChrPos(0xFE, -28530, 0, 20820, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF9188, 0x0, 0x6B8A, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_34_3845 end

    def Function_35_3877(): pass

    label("Function_35_3877")

    SetChrPos(0xFE, -28530, 0, 20820, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF8DB4, 0x0, 0x66C6, 0x1388, 0x0)
    Return()

    # Function_35_3877 end

    def Function_36_38A2(): pass

    label("Function_36_38A2")

    SetChrPos(0xFE, -28530, 0, 20820, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF9278, 0x0, 0x66C6, 0x1388, 0x0)
    Return()

    # Function_36_38A2 end

    def Function_37_38CD(): pass

    label("Function_37_38CD")

    OP_8E(0xFE, 0xFFFF9304, 0x0, 0x717A, 0x7D0, 0x0)

    def lambda_38E7():

        label("loc_38E7")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_38E7")

    QueueWorkItem2(0x102, 1, lambda_38E7)
    Return()

    # Function_37_38CD end

    def Function_38_38F3(): pass

    label("Function_38_38F3")

    OP_8E(0xFE, 0xFFFF90FC, 0x0, 0x6D9C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF8EA4, 0x0, 0x6FCC, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_38_38F3 end

    def Function_39_3923(): pass

    label("Function_39_3923")

    Call(0, 40)
    Call(0, 41)
    Return()

    # Function_39_3923 end

    def Function_40_392C(): pass

    label("Function_40_392C")

    EventBegin(0x0)
    OP_D2(0x270110, 0x270120, 0xD)
    OP_D2(0x270111, 0x270121, 0xE)
    OP_D2(0x270130, 0x270140, 0xF)
    OP_D2(0x270131, 0x270141, 0x10)
    OP_D2(0x70326, 0x7032D, 0x11)
    OP_D2(0x70327, 0x7032E, 0x12)
    OP_D2(0x70318, 0x7031F, 0x13)
    OP_D2(0x70319, 0x70320, 0x14)
    OP_D2(0x26000E, 0x260013, 0x16)
    OP_D2(0x270327, 0x270331, 0x17)
    OP_D2(0x270313, 0x27031D, 0x18)
    OP_D2(0x270326, 0x270330, 0x19)
    OP_D2(0x270312, 0x27031C, 0x1A)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    SetChrPos(0x12, -91240, 0, -3150, 90)
    SetChrPos(0x13, -89920, 0, -3190, 270)
    SetChrChipByIndex(0x12, 4)
    SetChrChipByIndex(0x13, 22)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    OP_6D(-90060, 0, -2540, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(267, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_3A60():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3A60)
    Sleep(100)

    def lambda_3A73():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3A73)
    Sleep(400)

    def lambda_3A86():
        OP_6D(-89530, 0, -4660, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A86)

    def lambda_3A9E():
        OP_6B(3070, 1000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3A9E)
    OP_43(0x101, 0x1, 0x0, 0x2A)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x2B)
    Sleep(200)
    OP_43(0x10A, 0x1, 0x0, 0x2C)
    Sleep(200)
    OP_43(0x10E, 0x1, 0x0, 0x2D)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #193
        0x12,
        "#5P你、你们是什么人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x13,
        "#5P到这里干什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#1007F#6P那是我们的台词。\x02\x03",

            "#1019F像你们这种老男人，\x01",
            "来这种地方，\x01",
            "难道不会觉得羞耻吗？！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x12,
        "#5P什、什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x10A,
        (
            "#1311F#6P女生宿舍\x01",
            "是羞涩少女们的花园……\x02\x03",

            "#816F怎么能让你们这种\x01",
            "心怀不轨的大叔玷污。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x12)
    OP_63(0x13)
    Sleep(500)

    ChrTalk(    #198
        0x12,
        "#5P#3S少、少愚弄人了！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #199
        0x13,
        (
            "#5P不、不要胡乱\x01",
            "想象一些奇怪的东西！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3CA5():
        OP_6D(-89560, 0, -4540, 150)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CA5)

    def lambda_3CBD():
        OP_6B(2800, 150)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3CBD)

    def lambda_3CCD():
        OP_91(0xFE, 0xFFFFFF38, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CCD)
    Sleep(20)
    SetChrChipByIndex(0x12, 23)
    SetChrFlags(0x12, 0x1000)

    def lambda_3CF7():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3CF7)

    def lambda_3D12():
        OP_91(0xFE, 0xFFFFFF38, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D12)
    Sleep(20)
    SetChrChipByIndex(0x13, 24)
    SetChrFlags(0x13, 0x1000)

    def lambda_3D3C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3D3C)

    def lambda_3D57():
        OP_91(0xFE, 0xFFFFFF38, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3D57)
    Sleep(20)

    def lambda_3D77():
        OP_91(0xFE, 0xFFFFFF38, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_3D77)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    Battle(0x79C, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3DC2"),
        (SWITCH_DEFAULT, "loc_3DC7"),
    )


    label("loc_3DC2")

    OP_B4(0x0)
    Jump("loc_3DC7")

    label("loc_3DC7")

    Return()

    # Function_40_392C end

    def Function_41_3DC8(): pass

    label("Function_41_3DC8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x12, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(-90270, 0, -5390, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    SetChrPos(0x0, -90270, 0, -5390, 0)
    SetChrPos(0x1, -90270, 0, -5390, 0)
    SetChrPos(0x2, -90270, 0, -5390, 0)
    SetChrPos(0x3, -90270, 0, -5390, 0)
    OP_69(0x0, 0x0)
    SetChrPos(0x12, -88920, 0, -3130, 0)
    SetChrPos(0x13, -90170, 0, -3000, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x12, 12)
    SetChrSubChip(0x12, 9)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x13, 12)
    SetChrSubChip(0x13, 14)
    OP_A2(0x202C)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_41_3DC8 end

    def Function_42_3EFA(): pass

    label("Function_42_3EFA")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 13)
    SetChrPos(0xFE, -90840, -500, -9250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3F26():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F26)
    OP_8E(0xFE, 0xFFFE9E72, 0xFFFFFF06, 0xFFFFE430, 0x1388, 0x0)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_42_3EFA end

    def Function_43_3F58(): pass

    label("Function_43_3F58")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x102, 15)
    SetChrPos(0xFE, -89620, -500, -9230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3F84():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F84)
    OP_8E(0xFE, 0xFFFEA28C, 0xFFFFFF06, 0xFFFFE322, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_43_3F58 end

    def Function_44_3FB1(): pass

    label("Function_44_3FB1")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10A, 17)
    SetChrPos(0xFE, -90840, -500, -9250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3FDD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FDD)
    OP_8E(0xFE, 0xFFFE9C06, 0xFFFFFF06, 0xFFFFDEF4, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_44_3FB1 end

    def Function_45_400A(): pass

    label("Function_45_400A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10E, 19)
    SetChrPos(0xFE, -89620, -500, -9230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4036():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4036)
    OP_8E(0xFE, 0xFFFEA1F6, 0xFFFFFF06, 0xFFFFDF1C, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_45_400A end

    def Function_46_4063(): pass

    label("Function_46_4063")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    SetChrPos(0x17, -60450, 0, 28840, 315)
    SetChrPos(0x18, -61710, 0, 29010, 45)
    SetChrPos(0xA, -60810, 0, 29920, 180)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0xA, 255)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_6D(-60370, 0, 30030, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(45000, 0)
    OP_6E(305, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_4123():
        OP_6D(-60370, 0, 28260, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4123)

    def lambda_413B():
        OP_6E(325, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_413B)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_4162():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4162)
    Sleep(100)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_418C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_418C)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_41B6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_41B6)
    OP_43(0x101, 0x1, 0x0, 0x2F)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x30)
    Sleep(400)
    OP_43(0x10A, 0x1, 0x0, 0x31)
    Sleep(400)
    OP_43(0x10E, 0x1, 0x0, 0x32)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x10E, 0x1)

    ChrTalk(    #200
        0xA,
        "#5P你、你们……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x18,
        "#5P艾丝蒂尔，约修亚！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        "#1017F#6P嘿嘿，让大家久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x102,
        (
            "#1040F#4P长话短说，先把事情\x01",
            "做个简单说明吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #204
        (
            "\x07\x05将作战计划，以及解救人质\x01",
            "的经过向大家说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #205
        0x17,
        (
            "#5P是这样啊……\x02\x03",

            "呼……\x01",
            "总算可以松口气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xA,
        (
            "#5P那么……\x01",
            "我们现在该怎么做？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x18,
        "#5P去和其他人会合吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        (
            "#1003F#6P嗯……\x01",
            "战斗还没有结束，\x01",
            "你们还是先在这里等一会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        (
            "#1042F#4P我们一定会把大家都救出来，\x01",
            "请放心吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x18,
        "#5P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xA,
        (
            "#5P……我明白了。\x01",
            "一切都拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #212
        (
            "\x07\x05取出游击士手册，\x01",
            "在妮吉塔、芙拉瑟、黛拉的\x01",
            "的名字上做了标记了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x202D)
    OP_28(0xC0, 0x1, 0x2000)
    OP_28(0xC1, 0x2, 0x100)
    OP_28(0xC1, 0x1, 0x200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_8C(0x15, 0, 0)
    OP_8C(0x14, 0, 0)
    OP_6D(-61470, 0, 26430, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -61470, 0, 26430, 180)
    SetChrPos(0x1, -61470, 0, 26430, 180)
    SetChrPos(0x2, -61470, 0, 26430, 180)
    SetChrPos(0x3, -61470, 0, 26430, 180)
    OP_69(0x0, 0x0)
    OP_8C(0x18, 45, 0)
    OP_8C(0xA, 180, 0)
    OP_8C(0x17, 315, 0)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0xA, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_46_4063 end

    def Function_47_453D(): pass

    label("Function_47_453D")

    SetChrPos(0xFE, -61530, 0, 20850, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF0F10, 0x0, 0x6806, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_47_453D end

    def Function_48_456F(): pass

    label("Function_48_456F")

    SetChrPos(0xFE, -61530, 0, 20850, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF12B2, 0x0, 0x67F2, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_48_456F end

    def Function_49_45A1(): pass

    label("Function_49_45A1")

    SetChrPos(0xFE, -61530, 0, 20850, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF0EC0, 0x0, 0x641E, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_49_45A1 end

    def Function_50_45D3(): pass

    label("Function_50_45D3")

    SetChrPos(0xFE, -61530, 0, 20850, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF137A, 0x0, 0x641E, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_50_45D3 end

    SaveToFile()

Try(main)
