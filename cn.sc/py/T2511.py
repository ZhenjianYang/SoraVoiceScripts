from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2511   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2511.x',
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
        '乔儿',                                 # 9
        '汉斯',                                 # 10
        '目标用照相机',                         # 11
        '德波拉',                               # 12
        '罗迪',                                 # 13
        '莉秋儿',                               # 14
        '米克',                                 # 15
        '朵洛希',                               # 16
        '罗伊斯',                               # 17
        '莫妮卡',                               # 18
        '艾福托老师',                           # 19
        '拉迪奥老师',                           # 20
        '碧欧拉老师',                           # 21
        '米丽亚老师',                           # 22
        '黛拉',                                 # 23
        '强化猎兵',                             # 24
        '强化猎兵',                             # 25
        '强化猎兵',                             # 26
        '强化猎兵',                             # 27
        '强化猎兵',                             # 28
        '强化猎兵',                             # 29
        '帕布尔',                               # 30
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT27/CH03004 ._CH',             # 02
        'ED6_DT07/CH01130 ._CH',             # 03
        'ED6_DT07/CH01360 ._CH',             # 04
        'ED6_DT07/CH01590 ._CH',             # 05
        'ED6_DT07/CH01080 ._CH',             # 06
        'ED6_DT06/CH20063 ._CH',             # 07
        'ED6_DT06/CH20064 ._CH',             # 08
        'ED6_DT07/CH01580 ._CH',             # 09
        'ED6_DT07/CH01370 ._CH',             # 0A
        'ED6_DT26/CH20396 ._CH',             # 0B
        'ED6_DT07/CH01460 ._CH',             # 0C
        'ED6_DT07/CH01660 ._CH',             # 0D
        'ED6_DT07/CH01210 ._CH',             # 0E
        'ED6_DT07/CH01430 ._CH',             # 0F
        'ED6_DT07/CH01090 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT27/CH03004P._CP',             # 02
        'ED6_DT07/CH01130P._CP',             # 03
        'ED6_DT07/CH01360P._CP',             # 04
        'ED6_DT07/CH01590P._CP',             # 05
        'ED6_DT07/CH01080P._CP',             # 06
        'ED6_DT06/CH20063P._CP',             # 07
        'ED6_DT06/CH20064P._CP',             # 08
        'ED6_DT07/CH01580P._CP',             # 09
        'ED6_DT07/CH01370P._CP',             # 0A
        'ED6_DT26/CH20396P._CP',             # 0B
        'ED6_DT07/CH01460P._CP',             # 0C
        'ED6_DT07/CH01660P._CP',             # 0D
        'ED6_DT07/CH01210P._CP',             # 0E
        'ED6_DT07/CH01430P._CP',             # 0F
        'ED6_DT07/CH01090P._CP',             # 10
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        X                   = 3500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -31990,
        Z                   = 0,
        Y                   = 26660,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 29790,
        Z                   = 0,
        Y                   = 29100,
        Direction           = 0,
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
        X                   = 5350,
        Z                   = 0,
        Y                   = -2630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 3450,
        Z                   = 0,
        Y                   = 240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -28450,
        Z                   = 0,
        Y                   = 27900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 27930,
        Z                   = 0,
        Y                   = 28500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 30410,
        Z                   = 0,
        Y                   = 25950,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -31760,
        Z                   = 0,
        Y                   = 58850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 59,
    )

    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 42000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 60,
    )

    DeclEvent(
        X                   = 2130,
        Y                   = 0,
        Z                   = 42010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 61,
    )

    DeclEvent(
        X                   = 2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 62,
    )


    DeclActor(
        TriggerX            = 3060,
        TriggerZ            = 0,
        TriggerY            = 2500,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_496",          # 00, 0
        "Function_1_773",          # 01, 1
        "Function_2_81A",          # 02, 2
        "Function_3_92D",          # 03, 3
        "Function_4_A2D",          # 04, 4
        "Function_5_AF8",          # 05, 5
        "Function_6_E81",          # 06, 6
        "Function_7_1380",         # 07, 7
        "Function_8_14A8",         # 08, 8
        "Function_9_15DD",         # 09, 9
        "Function_10_1790",        # 0A, 10
        "Function_11_1795",        # 0B, 11
        "Function_12_1BDB",        # 0C, 12
        "Function_13_1E0C",        # 0D, 13
        "Function_14_1E9D",        # 0E, 14
        "Function_15_1F59",        # 0F, 15
        "Function_16_1FE1",        # 10, 16
        "Function_17_206F",        # 11, 17
        "Function_18_2802",        # 12, 18
        "Function_19_2851",        # 13, 19
        "Function_20_28A5",        # 14, 20
        "Function_21_28F9",        # 15, 21
        "Function_22_294D",        # 16, 22
        "Function_23_2A69",        # 17, 23
        "Function_24_2B7A",        # 18, 24
        "Function_25_33DC",        # 19, 25
        "Function_26_342D",        # 1A, 26
        "Function_27_34A6",        # 1B, 27
        "Function_28_351F",        # 1C, 28
        "Function_29_3F36",        # 1D, 29
        "Function_30_4E26",        # 1E, 30
        "Function_31_4E6A",        # 1F, 31
        "Function_32_4E9A",        # 20, 32
        "Function_33_511A",        # 21, 33
        "Function_34_5272",        # 22, 34
        "Function_35_52AF",        # 23, 35
        "Function_36_531A",        # 24, 36
        "Function_37_5323",        # 25, 37
        "Function_38_55FF",        # 26, 38
        "Function_39_572C",        # 27, 39
        "Function_40_577C",        # 28, 40
        "Function_41_57CC",        # 29, 41
        "Function_42_581C",        # 2A, 42
        "Function_43_586C",        # 2B, 43
        "Function_44_5881",        # 2C, 44
        "Function_45_5896",        # 2D, 45
        "Function_46_58AB",        # 2E, 46
        "Function_47_58D4",        # 2F, 47
        "Function_48_5D0E",        # 30, 48
        "Function_49_5D5D",        # 31, 49
        "Function_50_5DC0",        # 32, 50
        "Function_51_5E23",        # 33, 51
        "Function_52_5E86",        # 34, 52
        "Function_53_640A",        # 35, 53
        "Function_54_646D",        # 36, 54
        "Function_55_64D0",        # 37, 55
        "Function_56_6533",        # 38, 56
        "Function_57_6582",        # 39, 57
        "Function_58_661B",        # 3A, 58
        "Function_59_6674",        # 3B, 59
        "Function_60_6678",        # 3C, 60
        "Function_61_667C",        # 3D, 61
        "Function_62_6680",        # 3E, 62
    )


    def Function_0_496(): pass

    label("Function_0_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_509")
    SetChrPos(0x9, 30280, 0, 53800, 0)
    SetChrPos(0x8, 30850, 0, 55200, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x6, 0x2)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x10, 5350, 0, -10, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 31330, 0, 24430, 164)
    Jump("loc_69C")

    label("loc_509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_5F0")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x12, -31080, 0, 27210, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x13, -31090, 0, 25690, 90)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x14, 30390, 0, 27920, 180)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, 30980, 0, 26960, 270)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0xB, 30510, 0, 25690, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 1)), scpexpr(EXPR_END)), "loc_5ED")
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 18)
    SetChrSubChip(0x17, 8)
    ClearChrFlags(0x18, 0x1)
    SetChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 18)
    SetChrSubChip(0x18, 11)
    SetChrPos(0x17, 1340, 0, 39800, 0)
    SetChrPos(0x18, -2270, 0, 40010, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_5ED")

    Jump("loc_69C")

    label("loc_5F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_61F")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x11, 31110, 0, 53120, 90)
    Jump("loc_69C")

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_646")
    SetChrPos(0x8, 1400, 0, -2100, 180)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x6, 0x2)
    Jump("loc_69C")

    label("loc_646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_655")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_69C")

    label("loc_655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_69C")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -28500, 0, 58160, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 3)), scpexpr(EXPR_END)), "loc_697")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 5350, 0, -2630, 0)
    Jump("loc_69C")

    label("loc_697")

    SetChrFlags(0xE, 0x80)

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_6B2")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_772")

    label("loc_6B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_6D1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 32)
    Jump("loc_772")

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_6E7")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 33)
    Jump("loc_772")

    label("loc_6E7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_6FF"),
        (108, "loc_712"),
        (110, "loc_742"),
        (111, "loc_75A"),
        (SWITCH_DEFAULT, "loc_772"),
    )


    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70F")
    Event(0, 36)

    label("loc_70F")

    Jump("loc_772")

    label("loc_712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72A")
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_73F")

    label("loc_72A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73F")
    SetMapFlags(0x10000000)
    Event(0, 29)

    label("loc_73F")

    Jump("loc_772")

    label("loc_742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_757")
    SetMapFlags(0x10000000)
    Event(0, 47)

    label("loc_757")

    Jump("loc_772")

    label("loc_75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76F")
    SetMapFlags(0x10000000)
    Event(0, 52)

    label("loc_76F")

    Jump("loc_772")

    label("loc_772")

    Return()

    # Function_0_496 end

    def Function_1_773(): pass

    label("Function_1_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_77D")
    Jump("loc_7C1")

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_79C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 1)), scpexpr(EXPR_END)), "loc_795")
    OP_D2(0x26020B, 0x260210, 0x12)

    label("loc_795")

    OP_64(0x0, 0x1)
    Jump("loc_7C1")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_7A6")
    Jump("loc_7C1")

    label("loc_7A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_7B0")
    Jump("loc_7C1")

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_7BA")
    Jump("loc_7C1")

    label("loc_7BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_7C1")

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D9")
    OP_B1("t2511_y")
    Jump("loc_7E2")

    label("loc_7D9")

    OP_B1("t2511_n")

    label("loc_7E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_7EC")
    Jump("loc_819")

    label("loc_7EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_804")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_819")

    label("loc_804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_819")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_819")

    Return()

    # Function_1_773 end

    def Function_2_81A(): pass

    label("Function_2_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_822")
    Return()

    label("loc_822")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_843")
    Jump("loc_844")

    label("loc_843")

    Return()

    label("loc_844")

    LoadEffect(0x0, "map\\\\mp032_00.eff")

    label("loc_858")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92C")
    OP_8D(0xFE, 2050, 280, 6480, 1790, 2000)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_924")
    OP_8B(0xFE, 0xEBA, 0xF78, 0x190)
    Sleep(400)
    OP_A2(0x3)
    SetChrChipByIndex(0xFE, 8)
    Sleep(2000)

    label("loc_8B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_917")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xF, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_914")
    Jump("loc_917")

    label("loc_914")

    Jump("loc_8B0")

    label("loc_917")

    Sleep(600)
    SetChrChipByIndex(0xFE, 7)
    OP_A3(0x3)

    label("loc_924")

    Sleep(400)
    Jump("loc_858")

    label("loc_92C")

    Return()

    # Function_2_81A end

    def Function_3_92D(): pass

    label("Function_3_92D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_98E")

    ChrTalk(    #0
        0xFE,
        (
            "听说旧校舍\x01",
            "潜伏着可疑的人物？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "虽然有点可怕……\x01",
            "不过倒是很能激发想象力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A29")

    label("loc_98E")

    OP_A2(0x8)

    ChrTalk(    #2
        0xFE,
        (
            "刚才\x01",
            "碰巧听说了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "听说旧校舍\x01",
            "潜伏着可疑的人物？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "真是令人吃惊啊。\x01",
            "简直像小说中的情节呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "也许有些不谨慎，\x01",
            "但想象力马上被激起了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A29")

    TalkEnd(0xFE)
    Return()

    # Function_3_92D end

    def Function_4_A2D(): pass

    label("Function_4_A2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_AB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A64")

    ChrTalk(    #6
        0xFE,
        (
            "啊啊～今天又是\x01",
            "劳累的一天啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAE")

    label("loc_A64")

    OP_A2(0x4)

    ChrTalk(    #7
        0xFE,
        "哟，你们的调查有进展吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "忙到现在还没吃饭吗？\x01",
            "还真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAE")

    Jump("loc_AF4")

    label("loc_AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_AF4")

    ChrTalk(    #9
        0xFE,
        "那么，今天要吃什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "还是和平时一样吃套餐吧……\x02",
    )

    CloseMessageWindow()

    label("loc_AF4")

    TalkEnd(0xFE)
    Return()

    # Function_4_A2D end

    def Function_5_AF8(): pass

    label("Function_5_AF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_B9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_B47")

    ChrTalk(    #11
        0xFE,
        (
            "乔儿她们好像\x01",
            "是去什么地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "听说是学生会有事。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B97")

    label("loc_B47")


    ChrTalk(    #13
        0xFE,
        "啊，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "乔儿她们好像\x01",
            "是去什么地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "听说是学生会有事。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_B97")

    Jump("loc_E7D")

    label("loc_B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_BE9")

    ChrTalk(    #16
        0xFE,
        (
            "嘿嘿，从明天起\x01",
            "社团活动又要开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "终于可以再次拉弓了啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_E7D")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_E7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_C36")

    ChrTalk(    #18
        0xFE,
        (
            "喂，喂？\x01",
            "发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "喂～好不好嘛？\x01",
            "告诉我吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7D")

    label("loc_C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 5)), scpexpr(EXPR_END)), "loc_C89")

    ChrTalk(    #20
        0xFE,
        (
            "考试期间的奇异事件，\x01",
            "好像很有意思的样子啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "最后到底怎么样啦？\x02",
    )

    CloseMessageWindow()
    Jump("loc_E7D")

    label("loc_C89")

    OP_A2(0x7)
    OP_A2(0x1235)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #22
        0x101,
        "#1000F那个，现在方便吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "啊，有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1002F嗯，想请教你一些事情…\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "\x07\x05艾丝蒂尔表示自己正在调查\x01",
            "考试期间发生的奇异事件。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #26
        0xFE,
        "考试期间的奇异事件吗～！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #27
        0xFE,
        (
            "那是什么？很有趣的样子啊！\x01",
            "喂～到底发生什么事了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x101,
        "#1019F这、这种反应……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        (
            "#045F总、总之\x01",
            "你是没发现什么对吧……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #30
        0x101,
        "#1007F去找别人问问吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "哎，到底是怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "喂～好不好嘛？\x01",
            "告诉我吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E7D")

    TalkEnd(0xFE)
    Return()

    # Function_5_AF8 end

    def Function_6_E81(): pass

    label("Function_6_E81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_F3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF7")

    ChrTalk(    #33
        0xFE,
        "哎呀，大家也来吃饭吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "我经常会\x01",
            "忽然觉得肚子饿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "哈哈，身体果然是\x01",
            "最诚实的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_F3B")

    label("loc_EF7")


    ChrTalk(    #36
        0xFE,
        (
            "总是忽然就觉得\x01",
            "肚子很饿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "哈哈，身体果然是\x01",
            "最诚实的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3B")

    Jump("loc_137C")

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1061")
    TurnDirection(0xFE, 0x105, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_FA0")

    ChrTalk(    #38
        0xFE,
        (
            "和科洛丝的对战\x01",
            "要等到开学以后了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "我要抓紧时间\x01",
            "加强特训才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_105E")

    label("loc_FA0")

    OP_A2(0x6)

    ChrTalk(    #40
        0xFE,
        (
            "听说科洛丝要开始\x01",
            "放假了是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "本来还期待和你对战呢，\x01",
            "真是遗憾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        (
            "#045F抱歉哦，罗伊斯。\x02\x03",

            "这场比赛就等到\x01",
            "我回来之后吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "哈哈，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "我会加强特训，\x01",
            "到时和你一战！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_105E")

    Jump("loc_137C")

    label("loc_1061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_10F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_109E")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #45
        0xFE,
        (
            "科洛丝，\x01",
            "到时还请你手下留情了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F0")

    label("loc_109E")

    OP_A2(0x6)

    ChrTalk(    #46
        0xFE,
        (
            "明天起\x01",
            "又要开始在击剑部\x01",
            "进行锻炼了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "趁现在赶快先\x01",
            "检查一下用具吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F0")

    Jump("loc_137C")

    label("loc_10F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_137C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 0)), scpexpr(EXPR_END)), "loc_1152")

    ChrTalk(    #48
        0xFE,
        (
            "考试期间没有发生什么\x01",
            "特别的事情哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "也没听说过什么\x01",
            "值得注意的传闻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137C")

    label("loc_1152")

    OP_A2(0x1230)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #50
        0xFE,
        "啊，科洛丝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "科洛丝也来\x01",
            "准备社团活动吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        (
            "#040F不…很可惜，\x01",
            "现在没时间顾那个了。\x02\x03",

            "现在有点事，\x01",
            "正在校园内进行调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "哎，怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1002F嗯，是这样……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #55
        (
            "\x07\x05艾丝蒂尔表示自己正在调查\x01",
            "考试期间发生的奇异事件。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #56
        0xFE,
        "奇异的事件吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "很遗憾，\x01",
            "记忆里好像没有什么特别的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "类似的传闻\x01",
            "也从来没听过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1015F嗯，是这样啊。\x02\x03",

            "算了，那也没办法。\x01",
            "去问问其他人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "没帮上忙，真对不起啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1000F哪里的话，不用介意啦。\x02\x03",

            "那么，多谢帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "哪里，没有的事。\x02",
    )

    CloseMessageWindow()

    label("loc_137C")

    TalkEnd(0xFE)
    Return()

    # Function_6_E81 end

    def Function_7_1380(): pass

    label("Function_7_1380")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24C, 3)), scpexpr(EXPR_END)), "loc_13D7")

    ChrTalk(    #63
        0xF,
        (
            "#150F好～接下来\x01",
            "要拍菜单了。\x02\x03",

            "嗯～上面的食物看起来都很美味的样子呢⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A4")

    label("loc_13D7")

    OP_A2(0x1263)
    TurnDirection(0xF, 0x101, 0)
    SetChrChipByIndex(0xFE, 7)
    ClearChrFlags(0xFE, 0x10)

    ChrTalk(    #64
        0x101,
        (
            "#1011F啊，朵洛希。\x02\x03",

            "在这种地方做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xF,
        (
            "#150F在拍摄食堂的风景啦⊙\x02\x03",

            "我拍了很多可爱的照片呢～\x01",
            "#151F嘿嘿嘿～来笑一个吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1007F（真、真没办法……）\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_14A4")
    SetChrChipByIndex(0xFE, 8)

    label("loc_14A4")

    TalkEnd(0xFE)
    Return()

    # Function_7_1380 end

    def Function_8_14A8(): pass

    label("Function_8_14A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_14E6")

    ChrTalk(    #67
        0xFE,
        (
            "啊啊～今天就要和前辈分别了，\x01",
            "还真是寂寞呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D9")

    label("loc_14E6")

    OP_A2(0x1)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #68
        0xFE,
        "啊！科洛丝前辈！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "呜～真遗憾，本来还想\x01",
            "一起参加社团活动呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x105,
        (
            "#045F对不起啊～莉秋儿。\x02\x03",

            "等我的休假结束之后\x01",
            "再和你一起努力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "嗯，说好了哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "我也会继续练习，\x01",
            "努力练得更强的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x105,
        "#041F嗯，那我就期待你的表现啦。\x02",
    )

    CloseMessageWindow()

    label("loc_15D9")

    TalkEnd(0xFE)
    Return()

    # Function_8_14A8 end

    def Function_9_15DD(): pass

    label("Function_9_15DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_16B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167E")

    ChrTalk(    #74
        0xFE,
        "游击士果然厉害啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "最近这种感觉\x01",
            "更加强烈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "艾丝蒂尔和约修亚\x01",
            "都很了不起呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "我也希望自己将来\x01",
            "可以从事这么棒的工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_16B5")

    label("loc_167E")


    ChrTalk(    #78
        0xFE,
        "游击士果然厉害啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "最近这种感觉\x01",
            "更加强烈了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B5")

    Jump("loc_178C")

    label("loc_16B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1707")

    ChrTalk(    #80
        0xFE,
        "从今天开始又有社团活动了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "赶快做事前准备，\x01",
            "占个好地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_178C")

    label("loc_1707")

    OP_A2(0x0)

    ChrTalk(    #82
        0xFE,
        "从今天开始又有社团活动了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "赶快做事前准备，\x01",
            "占个好地方吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "这一阵一直在准备考前复习，\x01",
            "真担心自己的射术已经退步了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178C")

    TalkEnd(0xFE)
    Return()

    # Function_9_15DD end

    def Function_10_1790(): pass

    label("Function_10_1790")

    Call(0, 11)
    Return()

    # Function_10_1790 end

    def Function_11_1795(): pass

    label("Function_11_1795")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_183F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180C")

    ChrTalk(    #85
        0xB,
        (
            "帮助别人当然很好，\x01",
            "但自己也一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xB,
        (
            "不要抓狼反被狼咬，\x01",
            "连自己的命都搭上。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_183B")

    label("loc_180C")


    ChrTalk(    #87
        0xB,
        (
            "帮助别人当然很好，\x01",
            "但自己也一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183B")

    TalkEnd(0xB)
    Return()

    label("loc_183F")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                               # 0
            "买东西\x01",                             # 1
            "招牌菜『大小姐料理』　800米拉\x01",      # 2
            "离开\x01",                               # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BB")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x72)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_18BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1990")
    SubMira(800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #88
        "\x06\x07\x02大小姐料理\x07\x00已经品尝过了。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x4B0)
    OP_31(0x1, 0xFD, 0x4B0)
    OP_31(0x2, 0xFD, 0x4B0)
    OP_31(0x3, 0xFD, 0x4B0)
    OP_31(0x4, 0xFD, 0x4B0)
    OP_31(0x5, 0xFD, 0x4B0)
    OP_31(0x6, 0xFD, 0x4B0)
    OP_31(0x7, 0xFD, 0x4B0)
    OP_31(0x8, 0xFD, 0x4B0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1982")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x9)"), scpexpr(EXPR_END)), "loc_1958")
    Jump("loc_1982")

    label("loc_1958")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #89
        "\x06\x07\x02大小姐料理\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_1982")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_19B6")

    label("loc_1990")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #90
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_19B6")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xB)
    Return()

    label("loc_19C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E2")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_19E2")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1A84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A35")

    ChrTalk(    #91
        0xB,
        "呀，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xB,
        (
            "肚子饿了吧？\x01",
            "来吃些东西吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1A81")

    label("loc_1A35")


    ChrTalk(    #93
        0xB,
        (
            "虽然没有导力器了，\x01",
            "但还是可以制作料理的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xB,
        (
            "这就是\x01",
            "家庭主妇的智慧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A81")

    Jump("loc_1BD7")

    label("loc_1A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1AE3")

    ChrTalk(    #95
        0xB,
        "哈哈，学院也马上要放假了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xB,
        (
            "一到这个时候，学生们的表情\x01",
            "马上变得开朗起来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD7")

    label("loc_1AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1B9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1B44")

    ChrTalk(    #97
        0xB,
        (
            "考试结束之后\x01",
            "接下来就是社团活动的季节了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xB,
        (
            "要多锻炼身体，\x01",
            "多吃东西啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B98")

    label("loc_1B44")

    OP_A2(0x3)

    ChrTalk(    #99
        0xB,
        (
            "阶段考试\x01",
            "终于结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xB,
        (
            "这段时间大家\x01",
            "都是早起晚睡，\x01",
            "真担心他们的健康。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B98")

    Jump("loc_1BD7")

    label("loc_1B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_1BD7")

    ChrTalk(    #101
        0xB,
        "考试辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xB,
        (
            "肚子也饿了吧？\x01",
            "来点些什么吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD7")

    TalkEnd(0xB)
    Return()

    # Function_11_1795 end

    def Function_12_1BDB(): pass

    label("Function_12_1BDB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1C3A")

    ChrTalk(    #103
        0x9,
        (
            "#731F全部解决好以后\x01",
            "再来学校食堂吧！\x02\x03",

            "#730F那么，你们两个\x01",
            "接下来也要小心啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E08")

    label("loc_1C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 2)), scpexpr(EXPR_END)), "loc_1D1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1C96")

    ChrTalk(    #104
        0x9,
        (
            "#730F听说旧校舍是\x01",
            "由古老的城塞改建的，\x02\x03",

            "即使有秘密地下室\x01",
            "也不奇怪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D17")

    label("loc_1C96")

    OP_A2(0x2)

    ChrTalk(    #105
        0x9,
        (
            "#730F隐藏的楼梯吗……\x02\x03",

            "资料中也没有\x01",
            "记载那些东西啊。\x02\x03",

            "只是听说旧校舍是\x01",
            "以前的城塞改建的。\x02\x03",

            "即使有秘密地下室\x01",
            "也很正常吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D17")

    Jump("loc_1E08")

    label("loc_1D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_1D5C")

    ChrTalk(    #106
        0x9,
        (
            "#730F我在这种时候\x01",
            "先在原地待命吧。\x02\x03",

            "一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E08")

    label("loc_1D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 7)), scpexpr(EXPR_END)), "loc_1E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1DA2")

    ChrTalk(    #107
        0x9,
        (
            "#730F耽误你们的时间了，真抱歉，\x02\x03",

            "请继续调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFE")

    label("loc_1DA2")


    ChrTalk(    #108
        0x9,
        (
            "#730F调查已经结束了吗？\x02\x03",

            "我这边的调查很顺利呢。\x02\x03",

            "资料也不太多，\x01",
            "一会儿就可以全部完成。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DFE")

    Jump("loc_1E08")

    label("loc_1E01")

    Call(0, 28)
    OP_A2(0x2)

    label("loc_1E08")

    TalkEnd(0x9)
    Return()

    # Function_12_1BDB end

    def Function_13_1E0C(): pass

    label("Function_13_1E0C")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 2)), scpexpr(EXPR_END)), "loc_1E99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6E")

    ChrTalk(    #109
        0xFE,
        (
            "自己什么也做不了，\x01",
            "真是很不好意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "不过学生们的事\x01",
            "就拜托了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_1E99")

    label("loc_1E6E")


    ChrTalk(    #111
        0xFE,
        (
            "自己什么也做不了，\x01",
            "真是很不好意思……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E99")

    TalkEnd(0x12)
    Return()

    # Function_13_1E0C end

    def Function_14_1E9D(): pass

    label("Function_14_1E9D")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 2)), scpexpr(EXPR_END)), "loc_1F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2C")

    ChrTalk(    #112
        0xFE,
        (
            "那么，有关学生们的事\x01",
            "就请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "要是有什么情况，\x01",
            "随时可以来和我说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "我们也会尽自己所能\x01",
            "协助你们的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_1F55")

    label("loc_1F2C")


    ChrTalk(    #115
        0xFE,
        (
            "那么，有关学生们的事\x01",
            "就请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F55")

    TalkEnd(0x13)
    Return()

    # Function_14_1E9D end

    def Function_15_1F59(): pass

    label("Function_15_1F59")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 3)), scpexpr(EXPR_END)), "loc_1FDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB4")

    ChrTalk(    #116
        0xFE,
        (
            "学生们的事……\x01",
            "就请你们多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "你们也不要太勉强啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_1FDD")

    label("loc_1FB4")


    ChrTalk(    #118
        0xFE,
        (
            "学生们的事……\x01",
            "就请你们多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FDD")

    TalkEnd(0x14)
    Return()

    # Function_15_1F59 end

    def Function_16_1FE1(): pass

    label("Function_16_1FE1")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 3)), scpexpr(EXPR_END)), "loc_206B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2040")

    ChrTalk(    #119
        0xFE,
        "外边好像还是很危险……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "我们就在这里等待吧。\x01",
            "学生们就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_206B")

    label("loc_2040")


    ChrTalk(    #121
        0xFE,
        (
            "我们就在这里等待吧。\x01",
            "学生们就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206B")

    TalkEnd(0x15)
    Return()

    # Function_16_1FE1 end

    def Function_17_206F(): pass

    label("Function_17_206F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2086")
    Call(0, 57)
    Call(0, 58)

    label("loc_2086")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    TurnDirection(0x8, 0x9, 0)
    OP_6D(31390, 0, 55630, 0)
    OP_67(0, 5510, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_213D():
        OP_6D(29500, 0, 55100, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_213D)
    OP_43(0x101, 0x1, 0x0, 0x13)
    OP_43(0x102, 0x1, 0x0, 0x12)
    OP_43(0xF8, 0x1, 0x0, 0x15)
    OP_43(0xF9, 0x1, 0x0, 0x14)
    OP_8C(0x9, 270, 400)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #122
        0x8,
        "#648F#5P啊，来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x9,
        "#731F#2P哟，二位辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#1016F#6P嘿嘿嘿，久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        (
            "#1040F#6P汉斯你们\x01",
            "已经很累了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x9,
        (
            "#730F#2P什么话啊，\x01",
            "我们只是在原地等而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x8,
        (
            "#644F#5P那种程度都承受不住的话，\x01",
            "哪还有资格当学生会委员嘛。\x02\x03",

            "#645F算了，真正的麻烦事\x01",
            "从现在才开始呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        (
            "#1035F#6P……确实如此呢。\x02\x03",

            "#1043F要在这样的情况下\x01",
            "迎接新学期吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1004F#6P啊，想想的话确实呢。\x02\x03",

            "#1015F……校园生活没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x9,
        (
            "#735F#2P也许吧…\x02\x03",

            "#730F总之我们学生会\x01",
            "也要好好思考对策。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "#644F#5P毕竟是我们自己的学校啊。\x02\x03",

            "总要尽可能做些\x01",
            "力所能及的事情。\x02\x03",

            "#648F而且，我们可不想输给你们，\x01",
            "还有在王都努力的科洛丝啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#1017F#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x9,
        (
            "#731F#2P等你们闲下来的时候\x01",
            "还要再来学院玩啊！\x02\x03",

            "到时科洛丝也要一起来，\x01",
            "咱们在食堂开个联欢会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "#641F#5P还可以穿上舞台服，\x01",
            "或者来个假面舞会什么的。\x02\x03",

            "#648F两个骑士和白色公主\x01",
            "可是很难得才能聚集到一起呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #135
        0x101,
        "#1018F#6P啊！这主意也不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        (
            "#1052F#6P这是什么反应嘛。\x02\x03",

            "#1043F还有，我……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #137
        0x101,
        "#1026F#5P（约修亚……？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x102,
        (
            "#1043F#6P那个，汉斯……\x02\x03",

            "…………我………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        (
            "#733F#2P嗯，怎么了？\x02\x03",

            "#731F是吗！\x01",
            "你果然还是无法忘记和我一起\x01",
            "度过的那些时光吗！？\x02\x03",

            "#732F真是没办法，看来我也只能\x01",
            "下定决心接受你的真心告白了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        (
            "#1052F#6P在说什么啊……\x02\x03",

            "#1048F……本来还想认真\x01",
            "说些事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x9,
        (
            "#736F#2P想叙旧的话\x01",
            "什么时候都可以。\x02\x03",

            "#732F不过，无论叙不叙旧，\x01",
            "也都不会改变什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        "#1044F#6P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x9,
        (
            "#731F#2P你和我是好朋友。\x02\x03",

            "#730F……你已经回来了，\x01",
            "并且现在站在我的眼前。\x02\x03",

            "这才是最重要的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        (
            "#1044F#6P啊……\x02\x03",

            "#1053F嗯……确实如此啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        (
            "#649F#5P（哎呀呀……\x01",
            "　男生怎么也都这个样子。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    Sleep(300)

    ChrTalk(    #146
        0x101,
        (
            "#1008F#6P（嘿嘿嘿……\x01",
            "　这不是很好吗。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_A2(0x9)
    OP_A2(0x20C0)
    EventEnd(0x0)
    Return()

    # Function_17_206F end

    def Function_18_2802(): pass

    label("Function_18_2802")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25410, 0, 55980, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2829():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2829)
    OP_8E(0xFE, 0x6EAA, 0x0, 0xD5D4, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_18_2802 end

    def Function_19_2851(): pass

    label("Function_19_2851")

    Sleep(600)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25410, 0, 55980, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_287D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_287D)
    OP_8E(0xFE, 0x6EDC, 0x0, 0xD962, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_19_2851 end

    def Function_20_28A5(): pass

    label("Function_20_28A5")

    Sleep(1200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25410, 0, 55980, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_28D1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28D1)
    OP_8E(0xFE, 0x6A9A, 0x0, 0xD84A, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_20_28A5 end

    def Function_21_28F9(): pass

    label("Function_21_28F9")

    Sleep(1800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25410, 0, 55980, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2925():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2925)
    OP_8E(0xFE, 0x6AAE, 0x0, 0xDB88, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_21_28F9 end

    def Function_22_294D(): pass

    label("Function_22_294D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2A01")

    ChrTalk(    #147
        0x8,
        (
            "#644F学院的情况虽然很麻烦，\x01",
            "但也只有试着努力克服困难了。\x02\x03",

            "#659F呵呵呵～假面舞会吗……\x01",
            "真是太期待了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x102,
        (
            "#1048F（难道是……………\x01",
            "……………………认真的？)\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x9)
    Jump("loc_2A65")

    label("loc_2A01")


    ChrTalk(    #149
        0x8,
        (
            "#644F学院的情况虽然很麻烦，\x01",
            "但也只有试着努力克服困难了。\x02\x03",

            "#659F那，我就强烈期待\x01",
            "假面舞会了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A65")

    TalkEnd(0x8)
    Return()

    # Function_22_294D end

    def Function_23_2A69(): pass

    label("Function_23_2A69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B12")

    ChrTalk(    #150
        0xFE,
        (
            "难得的新学期，\x01",
            "讨厌的事件却接连不断……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "呼，到底什么时候\x01",
            "才能恢复正常的校园生活啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "真希望吹奏音乐部的课外活动\x01",
            "也能早点重新开始。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_2B76")

    label("loc_2B12")


    ChrTalk(    #153
        0xFE,
        (
            "究竟要到什么时候\x01",
            "才能恢复正常的校园生活啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "真希望吹奏音乐部的课外活动\x01",
            "也能早点重新开始。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B76")

    TalkEnd(0xFE)
    Return()

    # Function_23_2A69 end

    def Function_24_2B7A(): pass

    label("Function_24_2B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B8B")
    Call(0, 57)

    label("loc_2B8B")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_4A(0x9, 255)
    SetChrPos(0x101, 30850, 0, 56600, 315)
    SetChrPos(0xF7, 29800, 0, 53800, 0)
    SetChrPos(0x105, 30850, 0, 55280, 315)
    SetChrPos(0x104, 28700, 0, 55860, 45)
    SetChrPos(0x127, 28700, 0, 54720, 45)
    SetChrPos(0x8, 29800, 0, 58200, 180)
    SetChrPos(0x9, 28700, 0, 57000, 45)
    OP_6D(31490, 0, 57970, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2D03")

    ChrTalk(    #155
        0x8,
        (
            "#647F#5P那么……\x01",
            "大家来做个分工吧。\x02\x03",

            "#640F我和阿加特先生就去\x01",
            "职员室向老师们打听一下情况。\x02\x03",

            "然后再向其他职员\x01",
            "进行询问调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x106,
        "#051F噢，那就拜托了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DAA")

    label("loc_2D03")


    ChrTalk(    #157
        0x8,
        (
            "#647F#5P那么……\x01",
            "大家来做个分工吧。\x02\x03",

            "#640F我和雪拉扎德姐姐就去\x01",
            "职员室向老师们打听一下情况。\x02\x03",

            "之后继续向其他职员\x01",
            "进行探听调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x103,
        "#021F呵呵～那就麻烦你带路了。\x02",
    )

    CloseMessageWindow()

    label("loc_2DAA")

    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #159
        0x8,
        (
            "#640F#5P汉斯去资料室\x01",
            "查一查过去有没有\x01",
            "发生过类似的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x9,
        "#730F#6P了解。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #161
        0x8,
        (
            "#648F#5P艾丝蒂尔和科洛丝\x01",
            "就负责向学生询问情报吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#1006F#2PＯＫ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x105,
        "#040F#2P明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #164
        0x8,
        (
            "#641F#5P朵洛希小姐和奥利维尔先生\x01",
            "就随便在学院里面逛逛吧。\x02\x03",

            "凭借你们艺术家的直觉\x01",
            "也许会有什么发现呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x104,
        "#035F#6P呵～交给我吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x127,
        "#151F我也要加油啦⊙\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF7, 400)

    ChrTalk(    #167
        0x8,
        (
            "#644F#5P大家都要在傍晚前结束调查，\x01",
            "然后回这里集合。\x02\x03",

            "那么解散！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F64():

        label("loc_2F64")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_2F64")

    QueueWorkItem2(0x101, 2, lambda_2F64)

    def lambda_2F75():

        label("loc_2F75")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_2F75")

    QueueWorkItem2(0x105, 1, lambda_2F75)
    OP_43(0x104, 0x1, 0x0, 0x19)
    Sleep(500)
    OP_43(0x127, 0x1, 0x0, 0x19)
    Sleep(800)
    OP_43(0x9, 0x1, 0x0, 0x19)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x1A)
    Sleep(800)
    OP_43(0x8, 0x1, 0x0, 0x1B)
    WaitChrThread(0x8, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x105, 0x1)

    def lambda_2FCA():
        OP_6D(31890, 0, 57570, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FCA)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #168
        0x101,
        (
            "#1006F#5P哈……\x01",
            "乔儿还是这么能干啊，\x01",
            "学院祭的时候也是这样。\x02\x03",

            "虽然平时经常胡闹，\x01",
            "但真不愧是学生会长啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #169
        0x105,
        (
            "#041F#6P呵呵……\x01",
            "乔儿的理想可是成为像梅贝尔市长\x01",
            "那样的政治家呢。\x02\x03",

            "#040F经常会抱怨说些\x01",
            "『可惜没早生十年，不然这次\x01",
            "就可以竞选市长了』之类的话。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #170
        0x101,
        (
            "#1016F#5P好、好厉害。\x02\x03",

            "#1004F对了，说起来的话……\x01",
            "乔儿她们对科洛丝的事…\x01",
            "知道了多少呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x105,
        (
            "#041F#6P呵呵……\x01",
            "已经全部都知道了呢～\x02\x03",

            "入学才半年左右，\x01",
            "我的秘密就被他们两个发现了。\x02\x03",

            "#040F除了他们两个之外，学院中\x01",
            "了解我王族身份的人就只有校长了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#1011F#5P这样啊……\x02\x03",

            "但即使如此，\x01",
            "他们两个对科洛丝的态度\x01",
            "依旧是非常自然呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x105,
        (
            "#048F#6P是啊……\x01",
            "就像艾丝蒂尔一样。\x02\x03",

            "他们都是我最重要的朋友。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1016F#5P啊哈哈……\x01",
            "忽然这么说…还真有点不好意思。\x02\x03",

            "#1006F好了，现在还是赶快在学院里\x01",
            "收集一下情报吧。\x02\x03",

            "只要问大家『考试期间\x01",
            "是否发生了什么奇怪的事件？』\x01",
            "就可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x105,
        (
            "#040F#6P嗯，这样问的话\x01",
            "大家也都比较容易明白。\x02\x03",

            "对了，另外也要去问问\x01",
            "宿舍里的学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        (
            "#1006F#5P嗯，ＯＫ。\x02\x03",

            "好，那现在就开始行动吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x26, 0xFF)
    OP_A2(0x121E)
    OP_28(0x83, 0x1, 0x2)
    OP_28(0x83, 0x1, 0x4)
    OP_28(0x66, 0x4, 0x40)
    OP_28(0x67, 0x4, 0x40)
    EventEnd(0x0)
    Return()

    # Function_24_2B7A end

    def Function_25_33DC(): pass

    label("Function_25_33DC")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x67C0, 0x0, 0xDAAC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_3402():
        OP_8E(0xFE, 0x605E, 0x0, 0xDA5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3402)
    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_33DC end

    def Function_26_342D(): pass

    label("Function_26_342D")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x6F0E, 0x0, 0xD2BE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6BC6, 0x0, 0xD9C6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x67C0, 0x0, 0xDAAC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_347B():
        OP_8E(0xFE, 0x605E, 0x0, 0xDA5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_347B)
    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_342D end

    def Function_27_34A6(): pass

    label("Function_27_34A6")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x70E4, 0x0, 0xE452, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6BC6, 0x0, 0xD9C6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x67C0, 0x0, 0xDAAC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_34F4():
        OP_8E(0xFE, 0x605E, 0x0, 0xDA5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34F4)
    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_27_34A6 end

    def Function_28_351F(): pass

    label("Function_28_351F")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    SetChrPos(0x101, -29850, 0, 58500, 99)
    SetChrPos(0x105, -30230, 0, 57060, 31)
    OP_8C(0x9, 270, 0)
    SetChrSubChip(0x9, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(    #177
        0x9,
        (
            "#730F哟～二位好。\x01",
            "调查得怎么样啦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1016F#6P嗯……\x01",
            "才刚开始而已啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x105,
        "#040F你这里进展得怎么样呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x9,
        (
            "#730F资料并不算太多，\x01",
            "应该花费不了多少时间。\x02\x03",

            "#736F先不说这个……\x01",
            "抱歉，虽然现在有正事要做，\x01",
            "但我想占用你们一点时间，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#1004F#6P啊，嗯……\x02\x03",

            "#1002F是想说……约修亚的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "#735F啊啊……\x02\x03",

            "#732F虽然具体详情我不太清楚，\x01",
            "但那家伙好像失踪了是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1025F#6P嗯……不过你不用担心。\x02\x03",

            "他是自己消失不见的，\x01",
            "这样……只能算是离家出走而已啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x9,
        (
            "#736F……………………………\x02\x03",

            "#730F我和那家伙虽然一共\x01",
            "也只相处了一周左右，不过……\x02\x03",

            "我们很投缘的，\x01",
            "当时在一起天南地北聊了很多。\x02\x03",

            "他还和我说了很多\x01",
            "来到艾丝蒂尔家之后的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        (
            "#1008F#6P是、是这样啊。\x02\x03",

            "还真是有点不好意思。\x01",
            "小时候的我完全就是个野丫头……\x02\x03",

            "#1016F啊，其实现在也仍然一样吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        (
            "#731F哈哈，总之他给我讲了很多\x01",
            "有趣的事情呢。\x02\x03",

            "#730F但是……\x01",
            "以前的经历，他却对我只字未提。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        "#1026F#6P……啊………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x9,
        (
            "#736F有一次，我假装无意地问起他\x01",
            "来洛连特之前的事……\x02\x03",

            "约修亚那时的眼神……\x01",
            "我到现在也还记忆犹新。\x02\x03",

            "#735F就在一瞬间，他的眼神完全失去了光彩，\x01",
            "我似乎都听到了他心碎的声音。\x02\x03",

            "#730F不过，他马上就强作笑容\x01",
            "敷衍了过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        "#1003F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x9,
        (
            "#732F我虽然不知道这是为什么……\x02\x03",

            "但约修亚如今会失踪，\x01",
            "恐怕和他以前的经历也有关吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#1026F#6P嗯……\x02\x03",

            "我想…大概是的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x9,
        (
            "#735F果然是这样吗……\x02\x03",

            "#730F那时候…每天睡觉之前\x01",
            "大家都会讨论当天发生的一些趣事。\x02\x03",

            "像是舞台剧的练习好累啦，\x01",
            "今天的晚饭真好吃啦什么的。\x02\x03",

            "#736F那家伙…每到这时\x01",
            "就会露出一副憧憬向往的表情……\x02\x03",

            "就好像是在眺望着只能远观，\x01",
            "却永远也无法得到的宝物一样……\x02\x03",

            "在他看来，这些东西似乎都是自己\x01",
            "注定永远无法拥有的……\x02\x03",

            "他的表情就是这样说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        (
            "#1026F#6P……约修亚………\x02\x03",

            "#1027F说什么永远无法拥有……\x01",
            "真是个…大笨蛋……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #194
        0x105,
        "#043F#4P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x9,
        (
            "#730F喂，艾丝蒂尔。\x02\x03",

            "虽然我和他交情不深，\x01",
            "也许没有说这些话的立场，不过……\x02\x03",

            "我还是想拜托你一件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x9,
        (
            "#732F你找到那家伙以后，请替我告诉他，\x01",
            "别再露出那种表情了。\x02\x03",

            "说什么永远也得不到，\x01",
            "哪有那种混帐事啊！\x02\x03",

            "那家伙和我们一样，\x01",
            "可以欢笑，可以恋爱，\x01",
            "一样拥有…得到幸福的权利。\x02\x03",

            "嗯，就是这样了，没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#1025F#6P汉斯……\x02\x03",

            "#1012F嗯！我一定会替你转告他的！\x02\x03",

            "#1018F就算是揍他一顿\x01",
            "我也会让他清醒！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x105,
        (
            "#041F#4P呵呵～艾丝蒂尔真是的……\x02\x03",

            "#048F不过如果不这样做的话\x01",
            "约修亚可能\x01",
            "永远都不会明白吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x9,
        (
            "#734F啊啊～本来就是啊。\x02\x03",

            "#730F呼……\x01",
            "说出来以后总算舒服一点了。\x02\x03",

            "抱歉，耽误了你们不少时间。\x02\x03",

            "请继续忙正事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        "#1017F#6P嗯…明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x9, 400)

    ChrTalk(    #202
        0x105,
        (
            "#041F汉斯也\x01",
            "要多多加油啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)
    OP_A2(0x121F)
    EventEnd(0x0)
    Return()

    # Function_28_351F end

    def Function_29_3F36(): pass

    label("Function_29_3F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F47")
    Call(0, 57)

    label("loc_3F47")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3F66")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3F6A")

    label("loc_3F66")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3F6A")

    AddParty(0x3, 0xF8, 0xFF)
    AddParty(0x26, 0xFF, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_4A(0x9, 255)
    SetChrPos(0xF7, 29800, 0, 53800, 0)
    SetChrPos(0x104, 28700, 0, 55860, 90)
    SetChrPos(0x127, 28700, 0, 54720, 90)
    SetChrPos(0x8, 29800, 0, 58200, 180)
    SetChrPos(0x9, 28700, 0, 57000, 90)
    SetChrPos(0x101, 24710, 0, 55840, 90)
    SetChrPos(0x105, 24710, 0, 55840, 90)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x105, 0x8)
    OP_6D(31490, 0, 57970, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)

    def lambda_406E():
        OP_6D(29490, 0, 57970, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_406E)

    def lambda_4086():
        OP_8F(0x101, 0x69B4, 0x0, 0xD854, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4086)

    def lambda_40A1():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40A1)
    Sleep(200)

    def lambda_40B8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_40B8)

    def lambda_40C6():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_40C6)

    def lambda_40D4():

        label("loc_40D4")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_40D4")

    QueueWorkItem2(0x9, 1, lambda_40D4)

    def lambda_40E5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_40E5)

    def lambda_40F3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_40F3)
    Sleep(300)

    def lambda_4106():
        OP_8F(0x105, 0x67E8, 0x0, 0xDBBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4106)

    def lambda_4121():
        OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4121)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x127, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x0)
    WaitChrThread(0x105, 0x1)
    OP_44(0x9, 0x1)

    ChrTalk(    #203
        0x8,
        (
            "#644F#5P啊，回来了啊。\x02\x03",

            "#648F那么大家就来说说\x01",
            "各自的调查结果吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 30850, 0, 56600, 270)
    SetChrPos(0x105, 30850, 0, 55280, 270)
    SetChrPos(0xF7, 29800, 0, 53800, 0)
    SetChrPos(0x104, 28700, 0, 55860, 90)
    SetChrPos(0x127, 28700, 0, 54720, 90)
    SetChrPos(0x8, 29800, 0, 58200, 180)
    SetChrPos(0x9, 28700, 0, 57000, 90)
    OP_6D(31490, 0, 57970, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_42FD")

    ChrTalk(    #204
        0x106,
        (
            "#053F#2P我们问过了全部的校内职员……\x02\x03",

            "#050F有个勤务员好像在学院里\x01",
            "看见了奇怪的人影。\x02\x03",

            "据说人影在通向旧校舍的后门那里\x01",
            "突然消失不见了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4382")

    label("loc_42FD")


    ChrTalk(    #205
        0x103,
        (
            "#026F#2P我们问过了职员们……\x02\x03",

            "#022F有一名勤务员在学院内\x01",
            "目击到了奇怪的人影，\x02\x03",

            "据说人影在通向旧校舍的后门那里\x01",
            "之后就突然消失了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4382")


    ChrTalk(    #206
        0x8,
        (
            "#644F#5P其它的老师都在为考试的事而忙，\x01",
            "没注意到什么异常情况。\x02\x03",

            "在学生食堂的阿姨和\x01",
            "接待处的珐奥娜小姐那里\x01",
            "也没有得到什么有用的情报～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#1015F#5P是这样啊……\x02\x03",

            "#1011F我们这边，有３个学生\x01",
            "提供了有价值的情报……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #208
        (
            "\x07\x05把巴托姆、米克、芙拉瑟的证言\x01",
            "向其他人说明了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #209
        0x105,
        (
            "#043F#2P三条证言全部都提到了\x01",
            "旧校舍那里。\x02\x03",

            "这应该不是单纯的巧合。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x127,
        (
            "#150F那么～\x01",
            "我也来发表一下我的成果吧～\x02\x03",

            "#151F学生·老师们的照片３０张～\x01",
            "学院内的风景照５０张～\x02\x03",

            "嘿嘿。\x01",
            "都拍摄得很可爱哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x104,
        (
            "#030F#6P很遗憾，我这边\x01",
            "没有什么太大的收获。\x02\x03",

            "#031F呵呵，不过我的演奏\x01",
            "却是吸引来很多可爱的\x01",
            "小猫咪呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #212
        0x101,
        (
            "#1019F#5P真是的！你们两个\x01",
            "完全都没有认真调查嘛。\x02\x03",

            "#1007F虽然一开始就没抱什么期待……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x9,
        (
            "#735F最后轮到我了。\x02\x03",

            "#730F我查询过去的资料，\x01",
            "想确认一下以前是否发生过\x01",
            "类似事件，结果很有意思……\x02\x03",

            "这所学院在建成新校舍以后\x01",
            "几乎就没有再发生过什么怪谈事件了，\x02\x03",

            "而仅有的几个恰好也都集中在旧校舍。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x127, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0xF7)
    OP_63(0x105)
    OP_63(0x104)
    OP_63(0x127)
    OP_63(0x8)
    OP_63(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4826")

    ChrTalk(    #214
        0x106,
        (
            "#552F#2P不管怎么想，\x01",
            "看来最可疑的就是旧校舍了啊。\x02\x03",

            "那到底是个怎样的建筑物？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4884")

    label("loc_4826")


    ChrTalk(    #215
        0x103,
        (
            "#025F#2P不管从哪方面考虑，\x01",
            "最可疑的地方也都是旧校舍啊。\x02\x03",

            "#020F那究竟是个怎样的建筑物呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4884")


    ChrTalk(    #216
        0x8,
        (
            "#644F#5P位于后门深处的旧校舍\x01",
            "是个数百年前建造的古老建筑物。\x02\x03",

            "直到２０年前还一直被人们使用，\x01",
            "在新校舍建立好以后\x01",
            "那里就被封锁了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #217
        0x101,
        (
            "#1015F#5P啊～学院祭的时候\x01",
            "我们不是进去过旧校舍里面吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 315, 400)

    ChrTalk(    #218
        0x105,
        (
            "#542F#2P后来发现里面栖息着魔兽，\x01",
            "因为太过危险，就用锁把后门锁上了。\x02\x03",

            "大概已经被荒置\x01",
            "２、３个月了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x104,
        (
            "#035F#6P呵……\x01",
            "数百年前的石制建筑物吗？\x02\x03",

            "#030F作为亡灵的栖息地，\x01",
            "真是再适合不过的地方了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        (
            "#1007F#5P嗯……\x02\x03",

            "虽然有点不想去…\x01",
            "不过现在看来似乎也没有别的办法了。\x02\x03",

            "#1008F……今天已经太晚了，\x01",
            "不如明天早上来调查怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x104,
        (
            "#033F#6P啊，艾丝蒂尔。\x01",
            "为什么说太晚了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #222
        0x101,
        (
            "#1016F#5P那、那个…现在天已经黑了啊！\x01",
            "里面又有魔兽，也许很危险的。\x02\x03",

            "那个地方就算白天去都觉得阴森森的，\x01",
            "晚上进去的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x104,
        (
            "#030F#6P哼哼，那不是正好嘛。\x02\x03",

            "#031F要想试胆量的话，深夜不是正好么。\x02\x03",

            "要想抓住幽灵的原形，\x01",
            "夜晚是最合适的时间段了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x127,
        (
            "#151F嗯嗯。\x02\x03",

            "要想拍出灵异照片的话\x01",
            "就必须要在晚上才行～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#1019F#5P呜，嗯嗯……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #226
        0x101,
        "#1004F#5P啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x105,
        (
            "#044F#2P艾丝蒂尔？\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        (
            "#1015F#5P嗯……\x01",
            "我在窗外好像看见了什么东西。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4CD7():

        label("loc_4CD7")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4CD7")

    QueueWorkItem2(0xF7, 1, lambda_4CD7)

    def lambda_4CE8():

        label("loc_4CE8")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4CE8")

    QueueWorkItem2(0x105, 1, lambda_4CE8)

    def lambda_4CF9():

        label("loc_4CF9")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4CF9")

    QueueWorkItem2(0x104, 1, lambda_4CF9)

    def lambda_4D0A():

        label("loc_4D0A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4D0A")

    QueueWorkItem2(0x127, 1, lambda_4D0A)

    def lambda_4D1B():

        label("loc_4D1B")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4D1B")

    QueueWorkItem2(0x8, 1, lambda_4D1B)

    def lambda_4D2C():

        label("loc_4D2C")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4D2C")

    QueueWorkItem2(0x9, 1, lambda_4D2C)

    def lambda_4D3D():
        OP_6D(30490, 0, 59490, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D3D)

    def lambda_4D55():
        OP_67(0, 6150, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D55)
    OP_8E(0x101, 0x794A, 0x0, 0xE4C0, 0x7D0, 0x0)
    OP_20(0xBB8)
    OP_8E(0x101, 0x771A, 0x0, 0xE862, 0x7D0, 0x0)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #229
        0x101,
        (
            "#1015F白白的一团影子，\x01",
            "还以为是基库呢……\x02\x03",

            "#1019F……………………白影？！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    FadeToBright(500, 0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_3F36 end

    def Function_30_4E26(): pass

    label("Function_30_4E26")

    OP_8E(0x101, 0x6EB4, 0x0, 0xE38A, 0x7D0, 0x0)
    OP_8E(0x101, 0x7990, 0x0, 0xE54C, 0x7D0, 0x0)
    OP_8E(0x101, 0x7882, 0x0, 0xDEA8, 0x7D0, 0x0)
    OP_8C(0x101, 284, 400)
    Return()

    # Function_30_4E26 end

    def Function_31_4E6A(): pass

    label("Function_31_4E6A")

    OP_8E(0x105, 0x6F0E, 0x0, 0xE510, 0x7D0, 0x0)
    OP_8E(0x105, 0x7468, 0x0, 0xE358, 0x7D0, 0x0)
    TurnDirection(0x105, 0x9, 400)
    Return()

    # Function_31_4E6A end

    def Function_32_4E9A(): pass

    label("Function_32_4E9A")

    SetChrPos(0x101, 30490, 0, 59490, 0)
    SetChrPos(0x105, 30850, 0, 55280, 270)
    SetChrPos(0xF7, 29800, 0, 53800, 0)
    SetChrPos(0x104, 28700, 0, 55860, 90)
    SetChrPos(0x127, 28700, 0, 54720, 90)
    SetChrPos(0x8, 29800, 0, 58200, 180)
    SetChrPos(0x9, 28700, 0, 57000, 90)
    TurnDirection(0xF7, 0x101, 0)
    TurnDirection(0x105, 0x101, 0)
    TurnDirection(0x104, 0x101, 0)
    TurnDirection(0x127, 0x101, 0)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0x9, 0x101, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_4A(0x9, 255)
    OP_6D(30490, 0, 59490, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    EventBegin(0x0)
    ClearMapFlags(0x2000000)
    FadeToBright(2000, 0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()

    ChrTalk(    #230
        0x105,
        (
            "#043F#2P艾丝蒂尔？\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(    #231
        0x101,
        (
            "#1008F#5P啊哈……\x01",
            "啊哈哈哈哈哈……\x02\x03",

            "#1007F啊、啊啊……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x101, 1)
    OP_0D()
    Sleep(500)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x127, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_50E3")

    ChrTalk(    #232
        0x106,
        "#055F#2P喂、喂！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_50FD")

    label("loc_50E3")


    ChrTalk(    #233
        0x103,
        "#023F#2P艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()

    label("loc_50FD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2812   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_32_4E9A end

    def Function_33_511A(): pass

    label("Function_33_511A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x17, 2350, 0, -610, 270)
    SetChrPos(0x18, 340, 0, -790, 90)
    SetChrPos(0x19, -80, 0, -4510, 180)
    SetChrPos(0x1A, -2400, 0, -3520, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    OP_D2(0x26000D, 0x260012, 0x11)
    OP_D2(0x26000E, 0x260013, 0x12)
    SetChrChipByIndex(0x17, 17)
    SetChrChipByIndex(0x18, 18)
    SetChrChipByIndex(0x19, 17)
    SetChrChipByIndex(0x1A, 18)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    SetChrSubChip(0x1A, 0)
    OP_62(0x17, 0x0, 2100, 0x26, 0x27, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x18, 0x0, 2100, 0x26, 0x27, 0xFA, 0x0)
    OP_43(0x19, 0x1, 0x0, 0x22)
    OP_43(0x1A, 0x1, 0x0, 0x23)
    SetChrFlags(0xB, 0x80)
    OP_6D(150, 2000, 4650, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_6D(-110, 0, -3080, 4000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2500   ._SN", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_33_511A end

    def Function_34_5272(): pass

    label("Function_34_5272")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52AE")
    OP_8C(0xFE, 135, 400)
    Sleep(700)
    OP_8C(0xFE, 180, 400)
    Sleep(700)
    OP_8C(0xFE, 225, 400)
    Sleep(700)
    OP_8C(0xFE, 180, 400)
    Sleep(700)
    Jump("Function_34_5272")

    label("loc_52AE")

    Return()

    # Function_34_5272 end

    def Function_35_52AF(): pass

    label("Function_35_52AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5319")
    OP_8E(0xFE, 0xFFFFE872, 0x0, 0xFFFFF524, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE8A4, 0x0, 0xFFFFFFEC, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFE872, 0x0, 0xFFFFF524, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF6A0, 0x0, 0xFFFFF240, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Jump("Function_35_52AF")

    label("loc_5319")

    Return()

    # Function_35_52AF end

    def Function_36_531A(): pass

    label("Function_36_531A")

    Call(0, 37)
    Call(0, 38)
    Return()

    # Function_36_531A end

    def Function_37_5323(): pass

    label("Function_37_5323")

    EventBegin(0x0)
    OP_D2(0x26000D, 0x260012, 0x11)
    OP_D2(0x26020B, 0x260210, 0x12)
    OP_D2(0x270110, 0x270120, 0x13)
    OP_D2(0x270111, 0x270121, 0x14)
    OP_D2(0x270130, 0x270140, 0x15)
    OP_D2(0x270131, 0x270141, 0x16)
    OP_D2(0x70326, 0x7032D, 0x17)
    OP_D2(0x70327, 0x7032E, 0x18)
    OP_D2(0x70318, 0x7031F, 0x19)
    OP_D2(0x70319, 0x70320, 0x1A)
    OP_D2(0x26000E, 0x260013, 0x1B)
    OP_D2(0x270327, 0x270331, 0x1C)
    OP_D2(0x270313, 0x27031D, 0x1D)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    SetChrPos(0x17, -1990, 0, 42080, 0)
    SetChrPos(0x18, 1610, 0, 41880, 0)
    SetChrChipByIndex(0x17, 17)
    SetChrChipByIndex(0x18, 27)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_6D(550, 0, 52120, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(368, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x27)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x28)
    Sleep(500)
    OP_43(0x10A, 0x1, 0x0, 0x29)

    def lambda_5467():
        OP_6D(1460, 0, 48750, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5467)

    def lambda_547F():
        OP_67(0, 4940, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_547F)

    def lambda_5497():
        OP_6E(322, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5497)

    def lambda_54A7():
        OP_6B(3060, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_54A7)
    Sleep(500)
    OP_43(0x10E, 0x1, 0x0, 0x2A)
    WaitChrThread(0x102, 0x3)

    ChrTalk(    #234
        0x17,
        "#5P啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x18,
        "#5P你们是……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10E, 0x1)

    ChrTalk(    #236
        0x101,
        "#1005F#5P要开战了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x10A,
        "#815F#5P我们上～！\x02",
    )

    CloseMessageWindow()

    def lambda_5522():
        OP_6D(1410, 0, 48310, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5522)

    def lambda_553A():
        OP_6B(2400, 600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_553A)
    OP_43(0x101, 0x1, 0x0, 0x2B)
    Sleep(30)
    OP_43(0x10A, 0x1, 0x0, 0x2D)
    Sleep(50)
    OP_43(0x10E, 0x1, 0x0, 0x2E)
    Sleep(30)
    OP_43(0x102, 0x1, 0x0, 0x2C)
    Sleep(100)
    SetChrChipByIndex(0x17, 28)
    SetChrFlags(0x17, 0x1000)

    def lambda_5584():
        OP_8F(0xFE, 0xFFFFF934, 0x0, 0xAF1E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_5584)
    Sleep(30)
    SetChrChipByIndex(0x18, 29)
    SetChrFlags(0x18, 0x1000)

    def lambda_55AE():
        OP_8F(0xFE, 0x74E, 0x0, 0xB09A, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_55AE)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    Battle(0x7A1, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_55F9"),
        (SWITCH_DEFAULT, "loc_55FE"),
    )


    label("loc_55F9")

    OP_B4(0x0)
    Jump("loc_55FE")

    label("loc_55FE")

    Return()

    # Function_37_5323 end

    def Function_38_55FF(): pass

    label("Function_38_55FF")

    EventBegin(0x0)
    OP_44(0x17, 0x0)
    OP_44(0x18, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    OP_D2(0x26020B, 0x260210, 0x12)
    OP_6D(-150, 0, 42940, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 18)
    SetChrSubChip(0x17, 8)
    ClearChrFlags(0x18, 0x1)
    SetChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 18)
    SetChrSubChip(0x18, 11)
    SetChrPos(0x0, -150, 0, 42940, 180)
    SetChrPos(0x1, -150, 0, 42940, 180)
    SetChrPos(0x2, -150, 0, 42940, 180)
    SetChrPos(0x3, -150, 0, 42940, 180)
    OP_69(0x0, 0x0)
    SetChrPos(0x17, 1340, 0, 39800, 0)
    SetChrPos(0x18, -2270, 0, 40010, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_A2(0x2021)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_38_55FF end

    def Function_39_572C(): pass

    label("Function_39_572C")

    SetChrChipByIndex(0x101, 19)
    SetChrPos(0xFE, 0, -2000, 48020, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0xCD78, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF948, 0x0, 0xCA3A, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_39_572C end

    def Function_40_577C(): pass

    label("Function_40_577C")

    SetChrChipByIndex(0x102, 21)
    SetChrPos(0xFE, 0, -2000, 48020, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0xCD78, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF8D0, 0x0, 0xCF62, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_40_577C end

    def Function_41_57CC(): pass

    label("Function_41_57CC")

    SetChrChipByIndex(0x10A, 23)
    SetChrPos(0xFE, 0, -2000, 48020, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0xCD78, 0x1388, 0x0)
    OP_8E(0xFE, 0x6C2, 0x0, 0xCD1E, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_41_57CC end

    def Function_42_581C(): pass

    label("Function_42_581C")

    SetChrChipByIndex(0x10E, 25)
    SetChrPos(0xFE, 0, -2000, 48020, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0xCD78, 0x1388, 0x0)
    OP_8E(0xFE, 0x35C, 0x0, 0xCFD0, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_42_581C end

    def Function_43_586C(): pass

    label("Function_43_586C")

    OP_8E(0xFE, 0xFFFFF970, 0x0, 0xAE10, 0x1F40, 0x0)
    Return()

    # Function_43_586C end

    def Function_44_5881(): pass

    label("Function_44_5881")

    OP_8E(0xFE, 0xFFFFF844, 0x0, 0xB266, 0x1F40, 0x0)
    Return()

    # Function_44_5881 end

    def Function_45_5896(): pass

    label("Function_45_5896")

    OP_8E(0xFE, 0x64A, 0x0, 0xACF8, 0x1F40, 0x0)
    Return()

    # Function_45_5896 end

    def Function_46_58AB(): pass

    label("Function_46_58AB")

    OP_8E(0xFE, 0x794, 0x0, 0xCD28, 0x1F40, 0x0)
    OP_8E(0xFE, 0x5BE, 0x0, 0xB25C, 0x1F40, 0x0)
    Return()

    # Function_46_58AB end

    def Function_47_58D4(): pass

    label("Function_47_58D4")

    EventBegin(0x0)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_8C(0x12, 180, 0)
    OP_8C(0x13, 0, 0)
    OP_6D(-27920, 0, 27650, 0)
    OP_67(0, 5370, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_72(0x2, 0x10)
    OP_70(0x2, 0x1D)
    OP_73(0x2)
    Sleep(300)

    def lambda_5966():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5966)
    Sleep(100)

    def lambda_5979():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5979)

    def lambda_5987():
        OP_6D(-28660, 0, 27330, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5987)
    OP_43(0x102, 0x1, 0x0, 0x31)
    Sleep(250)
    OP_43(0x101, 0x1, 0x0, 0x30)
    Sleep(250)
    OP_43(0x10A, 0x1, 0x0, 0x32)
    Sleep(250)
    OP_43(0x10E, 0x1, 0x0, 0x33)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #238
        0x12,
        "#6P你们是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x13,
        "#6P艾丝蒂尔和约修亚！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        "#1016F#2P嘿嘿嘿，好久不见啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x102,
        "#1035F#2P好久不见。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #242
        (
            "\x07\x05将作战计划，以及为解救人质\x01",
            "而来的事情向大家说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #243
        0x13,
        "#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x12,
        "#6P抱歉……太感谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x12,
        (
            "#6P我们能不能协助你们\x01",
            "一起营救学生？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x10E,
        (
            "#842F#2P您的心情我很理解，\x01",
            "不过敌人是职业的雇佣兵部队。\x02\x03",

            "#843F为了安全着想，\x01",
            "还是请在这里等着我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x12,
        "#6P是吗……我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x13,
        (
            "#6P学生们就…\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x10A,
        "#816F#2P嗯！请放心交给我们吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #250
        (
            "\x07\x05取出游击士手册，\x01",
            "在拉迪奥老师，艾福托老师\x01",
            "的名字上做了标记了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Fade(500)
    OP_71(0x2, 0x10)
    OP_6F(0x2, 0)
    OP_6D(-29240, 0, 25720, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -29240, 0, 25720, 270)
    SetChrPos(0x1, -29240, 0, 25720, 270)
    SetChrPos(0x2, -29240, 0, 25720, 270)
    SetChrPos(0x3, -29240, 0, 25720, 270)
    OP_4B(0x12, 255)
    OP_4B(0x13, 255)
    OP_0D()
    OP_A2(0x2022)
    OP_28(0xC0, 0x1, 0x40)
    OP_28(0xC1, 0x2, 0x4)
    OP_28(0xC1, 0x1, 0x8)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_47_58D4 end

    def Function_48_5D0E(): pass

    label("Function_48_5D0E")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -26460, 0, 25950, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_5D35():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D35)
    OP_8E(0xFE, 0xFFFF8C9C, 0x0, 0x654A, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_48_5D0E end

    def Function_49_5D5D(): pass

    label("Function_49_5D5D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -26460, 0, 25950, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_5D84():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D84)
    OP_8E(0xFE, 0xFFFF91EC, 0x0, 0x650E, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF8D6E, 0x0, 0x6AD6, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_49_5D5D end

    def Function_50_5DC0(): pass

    label("Function_50_5DC0")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -26460, 0, 25950, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_5DE7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5DE7)
    OP_8E(0xFE, 0xFFFF91EC, 0x0, 0x650E, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF8FEE, 0x0, 0x6310, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_50_5DC0 end

    def Function_51_5E23(): pass

    label("Function_51_5E23")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -26460, 0, 25950, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_5E4A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5E4A)
    OP_8E(0xFE, 0xFFFF91EC, 0x0, 0x650E, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF9214, 0x0, 0x67B6, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_51_5E23 end

    def Function_52_5E86(): pass

    label("Function_52_5E86")

    EventBegin(0x0)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0xB, 255)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(30820, 0, 27050, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_5F09():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5F09)
    Sleep(100)

    def lambda_5F1C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5F1C)
    Sleep(100)

    def lambda_5F2F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5F2F)

    def lambda_5F3D():
        OP_6D(30250, 0, 27820, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5F3D)
    OP_43(0x101, 0x1, 0x0, 0x35)
    Sleep(250)
    OP_43(0x102, 0x1, 0x0, 0x36)
    Sleep(250)
    OP_43(0x10A, 0x1, 0x0, 0x37)
    Sleep(250)
    OP_43(0x10E, 0x1, 0x0, 0x38)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #251
        0xB,
        "#2P啊！你们是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x14,
        (
            "艾丝蒂尔和约修亚……\x01",
            "你们怎么会在这里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "真是让人吃惊啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x102,
        "#1042F#6P是这样的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #255
        (
            "\x07\x05将作战计划，以及解救人质\x01",
            "的经过向大家说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #256
        0x14,
        (
            "原来如此，你们……\x02\x03",

            "是来救我们的吗？太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x15,
        (
            "那么……\x01",
            "学院内的情况怎样？\x02\x03",

            "战斗还在继续吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x10E,
        (
            "#843F#6P正门附近的战斗还没结束，\x01",
            "现在的状况还没有完全稳定。\x02\x03",

            "#842F为了安全起见，\x01",
            "老师们还是先在这里等着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x15,
        "是吗……真没办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x14,
        (
            "学生们的事……\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xB,
        (
            "#2P对了。\x01",
            "你们把这个拿去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0xB, 0x7300, 0x0, 0x65F4, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #262
        "\x07\x00得到了４个\x1F\xC4\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x1C4, 4)
    OP_8F(0xB, 0x772E, 0x0, 0x645A, 0x7D0, 0x0)

    ChrTalk(    #263
        0x101,
        "#1011F#6P阿姨……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x10A,
        "#811F#6P哇，可以收下吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xB,
        (
            "#2P啊，真是好东西啊。\x02\x03",

            "帮助别人当然很好，\x01",
            "但一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x102,
        "#1054F#6P……真是谢谢了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #267
        (
            "\x07\x05取出游击士手册，\x01",
            "在德波拉，碧欧拉老师，米丽亚老师\x01",
            "的名字上做了标记了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Fade(500)
    OP_6D(28370, 0, 26480, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, 28370, 0, 26480, 90)
    SetChrPos(0x1, 28370, 0, 26480, 90)
    SetChrPos(0x2, 28370, 0, 26480, 90)
    SetChrPos(0x3, 28370, 0, 26480, 90)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    OP_4B(0xB, 255)
    OP_0D()
    OP_A2(0x2023)
    OP_28(0xC0, 0x1, 0x80)
    OP_28(0xC1, 0x2, 0x10)
    OP_28(0xC1, 0x1, 0x20)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_52_5E86 end

    def Function_53_640A(): pass

    label("Function_53_640A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25350, 0, 25850, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_6431():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6431)
    OP_8E(0xFE, 0x698C, 0x0, 0x65D6, 0xFA0, 0x0)
    OP_8E(0xFE, 0x7030, 0x0, 0x6644, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_53_640A end

    def Function_54_646D(): pass

    label("Function_54_646D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25350, 0, 25850, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_6494():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6494)
    OP_8E(0xFE, 0x698C, 0x0, 0x65D6, 0xFA0, 0x0)
    OP_8E(0xFE, 0x703A, 0x0, 0x6ACC, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_54_646D end

    def Function_55_64D0(): pass

    label("Function_55_64D0")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25350, 0, 25850, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_64F7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_64F7)
    OP_8E(0xFE, 0x698C, 0x0, 0x65D6, 0xFA0, 0x0)
    OP_8E(0xFE, 0x6BA8, 0x0, 0x6B4E, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_55_64D0 end

    def Function_56_6533(): pass

    label("Function_56_6533")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25350, 0, 25850, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_655A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_655A)
    OP_8E(0xFE, 0x6A7C, 0x0, 0x64A0, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_56_6533 end

    def Function_57_6582(): pass

    label("Function_57_6582")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_65FC"),
        (1, "loc_6602"),
        (SWITCH_DEFAULT, "loc_6608"),
    )


    label("loc_65FC")

    OP_A2(0x1200)
    Jump("loc_6608")

    label("loc_6602")

    OP_A2(0x1201)
    Jump("loc_6608")

    label("loc_6608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_6616")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_661A")

    label("loc_6616")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_661A")

    Return()

    # Function_57_6582 end

    def Function_58_661B(): pass

    label("Function_58_661B")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_58_661B end

    def Function_59_6674(): pass

    label("Function_59_6674")

    SetPlaceName(0x71)
    Return()

    # Function_59_6674 end

    def Function_60_6678(): pass

    label("Function_60_6678")

    SetPlaceName(0x72)
    Return()

    # Function_60_6678 end

    def Function_61_667C(): pass

    label("Function_61_667C")

    SetPlaceName(0x75)
    Return()

    # Function_61_667C end

    def Function_62_6680(): pass

    label("Function_62_6680")

    SetPlaceName(0x70)
    Return()

    # Function_62_6680 end

    SaveToFile()

Try(main)
