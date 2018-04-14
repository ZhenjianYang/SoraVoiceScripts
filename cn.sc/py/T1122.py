from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1122   ._SN',
        MapName             = 'Bose',
        Location            = 'T1122.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 37,
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
        '巴克',                                 # 9
        '德拉多',                               # 10
        '普蕾沙',                               # 11
        '波波',                                 # 12
        '思潘斯老人',                           # 13
        '卡特丽亚',                             # 14
        '芬尼尔',                               # 15
        '泊尔',                                 # 16
        '米蕾婆婆',                             # 17
        '里布罗',                               # 18
        '艾米',                                 # 19
        '格蕾娅',                               # 20
        '丽露露',                               # 21
        '卡洛',                                 # 22
        '玛依森老人',                           # 23
        '刚茨',                                 # 24
        '罗卡斯',                               # 25
        '科尔娜',                               # 26
        '西蒙',                                 # 27
        '哈尔德',                               # 28
        '艾尔珂',                               # 29
        '马尔科',                               # 30
        '蒙提',                                 # 31
        '罗亚',                                 # 32
        '梅贝尔市长',                           # 33
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01130 ._CH',             # 02
        'ED6_DT07/CH01060 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH02490 ._CH',             # 05
        'ED6_DT07/CH01220 ._CH',             # 06
        'ED6_DT07/CH01010 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT07/CH01150 ._CH',             # 09
        'ED6_DT07/CH01070 ._CH',             # 0A
        'ED6_DT07/CH01030 ._CH',             # 0B
        'ED6_DT07/CH01200 ._CH',             # 0C
        'ED6_DT07/CH01270 ._CH',             # 0D
        'ED6_DT07/CH01180 ._CH',             # 0E
        'ED6_DT07/CH01120 ._CH',             # 0F
        'ED6_DT07/CH01480 ._CH',             # 10
        'ED6_DT07/CH01100 ._CH',             # 11
        'ED6_DT07/CH01020 ._CH',             # 12
        'ED6_DT07/CH02360 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01130P._CP',             # 02
        'ED6_DT07/CH01060P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH02490P._CP',             # 05
        'ED6_DT07/CH01220P._CP',             # 06
        'ED6_DT07/CH01010P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT07/CH01150P._CP',             # 09
        'ED6_DT07/CH01070P._CP',             # 0A
        'ED6_DT07/CH01030P._CP',             # 0B
        'ED6_DT07/CH01200P._CP',             # 0C
        'ED6_DT07/CH01270P._CP',             # 0D
        'ED6_DT07/CH01180P._CP',             # 0E
        'ED6_DT07/CH01120P._CP',             # 0F
        'ED6_DT07/CH01480P._CP',             # 10
        'ED6_DT07/CH01100P._CP',             # 11
        'ED6_DT07/CH01020P._CP',             # 12
        'ED6_DT07/CH02360P._CP',             # 13
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 0,
        Y                   = -12700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 8500,
        Z                   = 0,
        Y                   = -8300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4100,
        Z                   = 0,
        Y                   = 13650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 8250,
        Z                   = 0,
        Y                   = 13600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 9300,
        Z                   = 0,
        Y                   = 6900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -13400,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 2830,
        Z                   = 0,
        Y                   = 9160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -16700,
        Z                   = 0,
        Y                   = -8600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -13600,
        Z                   = 0,
        Y                   = 10700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -11100,
        Z                   = 0,
        Y                   = 10300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 5250,
        Z                   = 0,
        Y                   = -4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = 12500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -2310,
        Z                   = -1000,
        Y                   = -10530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 2350,
        Z                   = 0,
        Y                   = -8000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 11500,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -17180,
        Z                   = 0,
        Y                   = 5980,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -12620,
        Z                   = 0,
        Y                   = -8490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = -7300,
        Z                   = -1000,
        Y                   = 2510,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -12380,
        Z                   = 0,
        Y                   = 7420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = -16980,
        Z                   = 0,
        Y                   = -7310,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -1200,
        Z                   = -1000,
        Y                   = 6040,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -1200,
        Z                   = -1000,
        Y                   = 5040,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 9730,
        Z                   = -1000,
        Y                   = 13220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 1600,
        Z                   = -1000,
        Y                   = 150,
        Direction           = 257,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )


    DeclActor(
        TriggerX            = 6830,
        TriggerZ            = 0,
        TriggerY            = -8820,
        TriggerRange        = 400,
        ActorX              = 8360,
        ActorZ              = 1500,
        ActorY              = -8430,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7540,
        TriggerZ            = 0,
        TriggerY            = 6450,
        TriggerRange        = 400,
        ActorX              = 9300,
        ActorZ              = 1500,
        ActorY              = 6900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -15120,
        TriggerZ            = 0,
        TriggerY            = -8860,
        TriggerRange        = 400,
        ActorX              = -16700,
        ActorZ              = 1500,
        ActorY              = -8600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4D6",          # 00, 0
        "Function_1_5E9",          # 01, 1
        "Function_2_64C",          # 02, 2
        "Function_3_699",          # 03, 3
        "Function_4_6EA",          # 04, 4
        "Function_5_70E",          # 05, 5
        "Function_6_732",          # 06, 6
        "Function_7_756",          # 07, 7
        "Function_8_77A",          # 08, 8
        "Function_9_79E",          # 09, 9
        "Function_10_C37",         # 0A, 10
        "Function_11_C3C",         # 0B, 11
        "Function_12_11C0",        # 0C, 12
        "Function_13_14CD",        # 0D, 13
        "Function_14_17C8",        # 0E, 14
        "Function_15_17CD",        # 0F, 15
        "Function_16_25C6",        # 10, 16
        "Function_17_29E0",        # 11, 17
        "Function_18_2D70",        # 12, 18
        "Function_19_2D75",        # 13, 19
        "Function_20_3387",        # 14, 20
        "Function_21_38D8",        # 15, 21
        "Function_22_3CDC",        # 16, 22
        "Function_23_401F",        # 17, 23
        "Function_24_42CD",        # 18, 24
        "Function_25_468D",        # 19, 25
        "Function_26_49A3",        # 1A, 26
        "Function_27_4BFF",        # 1B, 27
        "Function_28_509F",        # 1C, 28
        "Function_29_545A",        # 1D, 29
        "Function_30_54B0",        # 1E, 30
        "Function_31_563D",        # 1F, 31
        "Function_32_5724",        # 20, 32
        "Function_33_57AB",        # 21, 33
        "Function_34_58B4",        # 22, 34
        "Function_35_59D7",        # 23, 35
        "Function_36_5B95",        # 24, 36
        "Function_37_609B",        # 25, 37
        "Function_38_61E2",        # 26, 38
        "Function_39_62DC",        # 27, 39
        "Function_40_6396",        # 28, 40
        "Function_41_6459",        # 29, 41
    )


    def Function_0_4D6(): pass

    label("Function_0_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_58B")
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    OP_43(0x12, 0x0, 0x6, 0x2)
    SetChrPos(0x12, 6320, 0, -5410, 90)
    OP_43(0x15, 0x0, 0x6, 0x2)
    SetChrPos(0x15, 6690, 0, -6830, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_557")
    OP_43(0x14, 0x0, 0x6, 0x2)
    SetChrPos(0x14, -7650, -1000, 270, 90)
    OP_43(0x16, 0x0, 0x0, 0x8)
    SetChrPos(0x16, 8210, 0, 11230, 90)
    SetChrFlags(0x13, 0x80)
    Jump("loc_588")

    label("loc_557")

    SetChrFlags(0x8, 0x10)
    SetChrPos(0x14, -8720, -1000, -3130, 0)
    SetChrPos(0x18, -10900, 0, -7320, 232)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1F, 0x80)

    label("loc_588")

    Jump("loc_5E8")

    label("loc_58B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_5E8")
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0x1A, 580, -1000, 5590, 270)
    SetChrPos(0x18, -8790, 0, -11320, 270)
    SetChrPos(0x14, -8720, -1000, -3130, 0)

    label("loc_5E8")

    Return()

    # Function_0_4D6 end

    def Function_1_5E9(): pass

    label("Function_1_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_62F")
    OP_72(0x0, 0x10)
    OP_6F(0x0, 29)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 29)
    OP_75(0xFF, 0xA, 0x7)
    OP_75(0xFF, 0xC, 0x7)
    OP_75(0xFF, 0xD, 0x7)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    Jump("loc_64B")

    label("loc_62F")

    SoundDistance(0x1CB, 0xFFFFEF98, 0xFFFFFC18, 0x276, 0x7D0, 0x61A8, 0x64, 0x0)

    label("loc_64B")

    Return()

    # Function_1_5E9 end

    def Function_2_64C(): pass

    label("Function_2_64C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_698")
    OP_8E(0xFE, 0x1798, 0x0, 0x3520, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x203A, 0x0, 0x3520, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_2_64C")

    label("loc_698")

    Return()

    # Function_2_64C end

    def Function_3_699(): pass

    label("Function_3_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_6C6")

    label("loc_6A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C3")
    OP_8D(0xFE, -9760, 1870, -7910, -2550, 2000)
    Jump("loc_6A0")

    label("loc_6C3")

    Jump("loc_6E9")

    label("loc_6C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E9")
    OP_8D(0xFE, -1410, -8950, -3910, -12650, 2000)
    Jump("loc_6C6")

    label("loc_6E9")

    Return()

    # Function_3_699 end

    def Function_4_6EA(): pass

    label("Function_4_6EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70D")
    OP_8D(0xFE, 5660, -10000, -300, -7600, 2000)
    Jump("Function_4_6EA")

    label("loc_70D")

    Return()

    # Function_4_6EA end

    def Function_5_70E(): pass

    label("Function_5_70E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_731")
    OP_8D(0xFE, 200, 14800, -7900, 10300, 2000)
    Jump("Function_5_70E")

    label("loc_731")

    Return()

    # Function_5_70E end

    def Function_6_732(): pass

    label("Function_6_732")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_755")
    OP_8D(0xFE, 7480, 600, 4800, -5000, 2000)
    Jump("Function_6_732")

    label("loc_755")

    Return()

    # Function_6_732 end

    def Function_7_756(): pass

    label("Function_7_756")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_779")
    OP_8D(0xFE, -12100, 16600, -16600, 14400, 2000)
    Jump("Function_7_756")

    label("loc_779")

    Return()

    # Function_7_756 end

    def Function_8_77A(): pass

    label("Function_8_77A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_79D")
    OP_8D(0xFE, 9580, 12630, 5520, 9820, 2000)
    Jump("Function_8_77A")

    label("loc_79D")

    Return()

    # Function_8_77A end

    def Function_9_79E(): pass

    label("Function_9_79E")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80C")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_801")
    OP_A9(0x3E)
    Jump("loc_803")

    label("loc_801")

    OP_A9(0x60)

    label("loc_803")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_80C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81D")
    TalkEnd(0x8)
    Return()

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_97F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C1")

    ChrTalk(    #0
        0x8,
        (
            "啊哟啊哟，稍微等等啦。\x01",
            "支援的大酬宾哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        "艰苦的时候更要互相帮助！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "为答谢各位平时经常光顾本店，\x01",
            "我为大家准备了优惠的商品哦。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_A2(0x0)
    Jump("loc_97C")

    label("loc_8C1")


    ChrTalk(    #3
        0x8,
        (
            "前景虽然很严酷，\x01",
            "但在小姐的帮助下，\x01",
            "当前库存不足的情况总算得到了避免。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "这种时候更要靠大酬宾来\x01",
            "使市场活跃起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "这就是为了答谢顾客，\x01",
            "在困难的时候更要加油呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    SetChrFlags(0x8, 0x10)
    OP_A3(0x0)

    label("loc_97C")

    Jump("loc_C33")

    label("loc_97F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3E")

    ChrTalk(    #6
        0x8,
        (
            "岂止是定期船，\x01",
            "连货车和船都停开了。\x01",
            "物流完全瘫痪了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "这样下去的话，\x01",
            "很快就没有库存了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "尤其是像本店这样以货物新鲜为卖点的店铺。\x01",
            "这可是生死攸关的问题啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_A7B")

    label("loc_A3E")


    ChrTalk(    #9
        0x8,
        (
            "真头痛。\x01",
            "物流完全瘫痪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "这可是生死攸关的问题啊。\x02",
    )

    CloseMessageWindow()

    label("loc_A7B")

    Jump("loc_C33")

    label("loc_A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_B2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AC4")

    ChrTalk(    #11
        0x8,
        (
            "好了，期待已久的\x01",
            "恢复营业纪念大减价就要开始啰～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B29")

    label("loc_AC4")


    ChrTalk(    #12
        0x8,
        (
            "好了，期待已久的\x01",
            "恢复营业纪念大减价就要开始啰～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "本日内可享受优惠的商品，\x01",
            "您可别错过哟～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B29")

    Jump("loc_C33")

    label("loc_B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_C33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B83")

    ChrTalk(    #14
        0x8,
        (
            "拉文努村的水果\x01",
            "大量到货啰～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "洛连特产的蔬菜也是\x01",
            "最新鲜的哟～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C33")

    label("loc_B83")


    ChrTalk(    #16
        0x8,
        "来来，都来看一看啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "在拉文努村收获的水果\x01",
            "大量到货啰～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "要是您正在为晚餐的菜单犹豫的话，\x01",
            "本人向您推荐洛连特的蔬菜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "是刚刚从帕赛尔农场\x01",
            "运送来的新鲜货哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C33")

    TalkEnd(0x8)
    Return()

    # Function_9_79E end

    def Function_10_C37(): pass

    label("Function_10_C37")

    Call(0, 11)
    Return()

    # Function_10_C37 end

    def Function_11_C3C(): pass

    label("Function_11_C3C")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAA")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9F")
    OP_A9(0x3D)
    Jump("loc_CA1")

    label("loc_C9F")

    OP_A9(0x5F)

    label("loc_CA1")

    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_CAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBB")
    TalkEnd(0x9)
    Return()

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D66")

    ChrTalk(    #20
        0x9,
        (
            "超市的所有店铺\x01",
            "都在举办酬宾活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "多亏了小姐，\x01",
            "货源得到了保证，\x01",
            "现在要尽全力使超市活跃起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "柏斯的超市\x01",
            "一直是站在平民百姓这一边的嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_DC0")

    label("loc_D66")


    ChrTalk(    #23
        0x9,
        (
            "超市的所有店铺\x01",
            "都在举办酬宾活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "所有商品都是经济实惠的，\x01",
            "请务必要来看一下啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC0")

    Jump("loc_11BC")

    label("loc_DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB9")

    ChrTalk(    #25
        0x9,
        (
            "怎，怎么办。\x01",
            "货物迟迟不来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        (
            "按道理的话，\x01",
            "这样的状况是应该考虑涨价的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "以前我们曾经趁机涨过价，\x01",
            "给大家添了不少麻烦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "我想现在不能再随随便便\x01",
            "涨价了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "必须得和巴克那家伙商量下，\x01",
            "想出个办法来才行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_F55")

    label("loc_EB9")


    ChrTalk(    #30
        0x9,
        (
            "物流仍然停止着，\x01",
            "按道理的话，\x01",
            "这样的状况是应该考虑涨价的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "以前我们曾经趁机涨过价，\x01",
            "因为以前曾给大家添过麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "现在不能再随随便便\x01",
            "涨价了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F55")

    Jump("loc_11BC")

    label("loc_F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1093")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FC6")

    ChrTalk(    #33
        0x9,
        "现在正在举行恢复营业纪念大酬宾。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "恢复营业是个不错的时机啊。\x01",
            "得充分用来做生意才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1090")

    label("loc_FC6")


    ChrTalk(    #35
        0x9,
        (
            "呀，欢迎。\x01",
            "今日正举办恢复营业纪念大酬宾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "好不容易又重新开业的第一天嘛，\x01",
            "不好好利用来做生意可不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "摔倒了也不要白白站起来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "这是米蕾婆婆的口头禅，\x01",
            "那正是商人该秉持的精神啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1090")

    Jump("loc_11BC")

    label("loc_1093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_11BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_110A")

    ChrTalk(    #39
        0x9,
        (
            "有很多优惠的商品，\x01",
            "请务必要来看一下啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "隔壁那个店铺是我伙伴开的，\x01",
            "也请您顺便多关照一下了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11BC")

    label("loc_110A")


    ChrTalk(    #41
        0x9,
        (
            "柏斯最近很太平，\x01",
            "商品的进货也很安定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "因此优惠商品比比皆是。\x01",
            "请务必要来看一下啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "呵呵，隔壁的店铺是我伙伴巴克开的，\x01",
            "所以也请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        "那家伙是我的伙伴。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_11BC")

    TalkEnd(0x9)
    Return()

    # Function_11_C3C end

    def Function_12_11C0(): pass

    label("Function_12_11C0")

    TalkBegin(0xA)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122E")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1223")
    OP_A9(0x40)
    Jump("loc_1225")

    label("loc_1223")

    OP_A9(0x5C)

    label("loc_1225")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_122E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_123F")
    TalkEnd(0xA)
    Return()

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FC")

    ChrTalk(    #45
        0xA,
        (
            "全店都在进行大酬宾，\x01",
            "现在出售特殊的商品哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "虽然是水果店的老兄\x01",
            "想出来的主意，\x01",
            "但我觉得是个不错的点子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "就是这么回事，\x01",
            "所以我们也不甘落后地开始叫卖了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1350")

    label("loc_12FC")


    ChrTalk(    #48
        0xA,
        (
            "全店都在进行大酬宾，\x01",
            "现在出售特殊的商品哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "我们也不甘落后地\x01",
            "开始叫卖了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1350")

    Jump("loc_14C9")

    label("loc_1353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_13B1")

    ChrTalk(    #50
        0xA,
        (
            "门以及喷水池停止的原因\x01",
            "好像还没有查明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "这座商业城镇\x01",
            "到底出了什么事儿呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C9")

    label("loc_13B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_142C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13EC")

    ChrTalk(    #52
        0xA,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        "日用的商品一大堆哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1429")

    label("loc_13EC")


    ChrTalk(    #54
        0xA,
        (
            "今天老公来店里\x01",
            "帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "因此我也能\x01",
            "专心经营了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1429")

    Jump("loc_14C9")

    label("loc_142C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_14C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_146C")

    ChrTalk(    #56
        0xA,
        (
            "请随便看看吧。\x01",
            "里面准备了各种便利的杂货。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C9")

    label("loc_146C")


    ChrTalk(    #57
        0xA,
        (
            "请随便看看吧。\x01",
            "里面准备了各种便利的杂货。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        (
            "看看～\x01",
            "推荐给各位顾客需要的小商品喔！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_14C9")

    TalkEnd(0xA)
    Return()

    # Function_12_11C0 end

    def Function_13_14CD(): pass

    label("Function_13_14CD")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1526")

    ChrTalk(    #59
        0xB,
        (
            "超市里的全部商人都在\x01",
            "进行援助大酬宾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xB,
        (
            "妈妈好像也\x01",
            "比平时更卖力了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C4")

    label("loc_1526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_15F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B4")

    ChrTalk(    #61
        0xB,
        (
            "看来城里的导力器\x01",
            "停止工作了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        (
            "我家店里的收款机\x01",
            "不能用了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        (
            "现在我爸爸去工房了，\x01",
            "委托别人来修理机器哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_15F3")

    label("loc_15B4")


    ChrTalk(    #64
        0xB,
        (
            "看来城里的导力器\x01",
            "停止工作了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        "到底是怎么一回事啊。\x02",
    )

    CloseMessageWindow()

    label("loc_15F3")

    Jump("loc_17C4")

    label("loc_15F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_16F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1673")

    ChrTalk(    #66
        0xB,
        (
            "能够帮上忙，\x01",
            "我已经很高兴呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        (
            "但爸爸经常把商品\x01",
            "摆放错位置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        "不早点让他习惯这工作可不行……\x02",
    )

    CloseMessageWindow()
    Jump("loc_16EF")

    label("loc_1673")

    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xB, 0x1F, 400)

    ChrTalk(    #69
        0xB,
        (
            "啊，爸爸。\x01",
            "这件商品不是放在那个架子上哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        (
            "爸爸你要多加油啊。\x01",
            "刚才也搞错啰。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    ClearChrFlags(0xB, 0x10)

    label("loc_16EF")

    Jump("loc_17C4")

    label("loc_16F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_17C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1757")

    ChrTalk(    #71
        0xB,
        (
            "我是这里的店员。\x01",
            "是来帮妈妈工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        (
            "本店全是便利的商品，\x01",
            "请务必来看一看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C4")

    label("loc_1757")


    ChrTalk(    #73
        0xB,
        "啊，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xB,
        (
            "我是这里的店员。\x01",
            "我是来帮妈妈干活的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xB,
        (
            "本店全是便利的商品，\x01",
            "请务必来看一看。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_17C4")

    TalkEnd(0xB)
    Return()

    # Function_13_14CD end

    def Function_14_17C8(): pass

    label("Function_14_17C8")

    Call(0, 15)
    Return()

    # Function_14_17C8 end

    def Function_15_17CD(): pass

    label("Function_15_17CD")

    TalkBegin(0xC)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_183B")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1830")
    OP_A9(0x3C)
    Jump("loc_1832")

    label("loc_1830")

    OP_A9(0x5A)

    label("loc_1832")

    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_183B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_184C")
    TalkEnd(0xC)
    Return()

    label("loc_184C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1859")
    OP_A2(0x6)

    label("loc_1859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CF")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇前编QST017通关】\x01",          # 0
            "【◇前编QST017没有通关】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18C3"),
        (1, "loc_18C9"),
        (SWITCH_DEFAULT, "loc_18CF"),
    )


    label("loc_18C3")

    OP_A2(0x6)
    Jump("loc_18CF")

    label("loc_18C9")

    OP_A3(0x6)
    Jump("loc_18CF")

    label("loc_18CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CD")

    ChrTalk(    #76
        0xC,
        (
            "呵呵，\x01",
            "在这种时候策划大酬宾……\x01",
            "年轻人果然干劲十足呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xC,
        (
            "大酬宾的成功\x01",
            "显然离不开梅贝尔市长的协助……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xC,
        (
            "而且柏斯商人那古老而优秀的品质，\x01",
            "直到今天也依然健在呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xC,
        (
            "当然本店也将把秘蔵的商品\x01",
            "摆放出来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1A2A")

    label("loc_19CD")


    ChrTalk(    #80
        0xC,
        (
            "呵呵，\x01",
            "在这种时候策划大酬宾……\x01",
            "年轻人果然干劲十足呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xC,
        (
            "本店当然也打算参加\x01",
            "大酬宾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A2A")

    Jump("loc_1C71")

    label("loc_1A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1B37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE2")

    ChrTalk(    #82
        0xC,
        (
            "王国内的流通渠道\x01",
            "全都遇到了问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xC,
        (
            "目前虽然还有一点库存，\x01",
            "但假如进货遇到困难的话，\x01",
            "商品紧缺只是时间的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xC,
        (
            "呼……\x01",
            "真是面临基本生活失策的境况啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1B34")

    label("loc_1AE2")


    ChrTalk(    #85
        0xC,
        (
            "王国内的流通渠道\x01",
            "全都遇到了问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xC,
        (
            "呼……\x01",
            "真是面临基本生活失策的境况啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B34")

    Jump("loc_1C71")

    label("loc_1B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1BA9")

    ChrTalk(    #87
        0xC,
        (
            "托女王殿下的福，\x01",
            "那条龙看来已经被赶走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xC,
        (
            "超市也顺利修复，\x01",
            "又能集中精力投入到商品贸易中去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_1BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1C71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1C12")

    ChrTalk(    #89
        0xC,
        (
            "如果是需要药品的话，\x01",
            "请来我的商店看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xC,
        (
            "七耀教会开发的\x01",
            "新药已经投入使用啰。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_1C12")


    ChrTalk(    #91
        0xC,
        (
            "如果是需要药品的话，\x01",
            "请来我的商店看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xC,
        (
            "从疗伤药到滋补品\x01",
            "各个领域的药物都有啰。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1C71")

    Jump("loc_1DA7")

    label("loc_1C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CE2")

    ChrTalk(    #93
        0xC,
        (
            "我们这里摆放的都是\x01",
            "能在工作上提供方便的药物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xC,
        (
            "有需要的时候，\x01",
            "思潘斯药店就请您多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA7")

    label("loc_1CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1D3E")

    ChrTalk(    #95
        0xC,
        (
            "我们这里摆放的都是\x01",
            "能为工作带来便利的药物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xC,
        (
            "有需要的时候，\x01",
            "请多关照啰。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA7")

    label("loc_1D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1DA7")

    ChrTalk(    #97
        0xC,
        (
            "我们这里摆放的都是\x01",
            "能为工作带来便利的药物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xC,
        (
            "有需要的时候，\x01",
            "思潘斯药店就请您多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA7")

    Jump("loc_25C2")

    label("loc_1DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_206A")
    TurnDirection(0xC, 0x101, 0)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #99
        0xC,
        "啊，各位是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xC,
        (
            "曾经帮我寻找药草的\x01",
            "游击士们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1011F啊，说起来的话……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        (
            "#1040F哈哈……\x01",
            "感觉好怀念呢。\x02\x03",

            "爷爷\x01",
            "还是很健康啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(    #103
        0xC,
        (
            "呵呵，也就是身体还行，\x01",
            "这可是我的长项啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xC,
        (
            "说起来，那个时候\x01",
            "真是多亏了你们的帮助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xC,
        (
            "既然机会这么难得，作为谢礼，\x01",
            "我送各位一件秘蔵的药品。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #106
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x205, 1)

    ChrTalk(    #107
        0xC,
        (
            "请不必客气，\x01",
            "各位尽管收下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xC,
        (
            "这是我的\x01",
            "一点心意啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1001F哇，谢谢。\x02\x03",

            "这样的话\x01",
            "就不客气地接受啰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        "#1041F对不起……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xC,
        (
            "此外也摆放着很多\x01",
            "能在工作上提供方便的药物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xC,
        (
            "有需要的时候，\x01",
            "请多关照啰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1016F嗯，知道了。\x02\x03",

            "（不，不愧是生意人……\x01",
            "  永远不忘记拉客。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BC")

    label("loc_206A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_234C")
    TurnDirection(0xC, 0x101, 0)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #114
        0xC,
        "啊，各位是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xC,
        (
            "曾经帮我寻找药草的\x01",
            "游击士们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1016F好像…这么说\x01",
            "是有这么回事。\x02\x03",

            "#1000F好久不见了。\x01",
            "这次好像还挺严重呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xC,
        (
            "哈哈哈。\x01",
            "这不算什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xC,
        (
            "完全不能够和\x01",
            "百日战役相比。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xC,
        (
            "这不谈这个了，\x01",
            "难得你们能来我的店铺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xC,
        (
            "我有一份谢礼\x01",
            "要送给你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#1011F谢礼……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "哈哈哈，\x01",
            "就当我给你们赶走龙后的谢礼。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #123
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x205, 1)

    ChrTalk(    #124
        0xC,
        (
            "这是效果很不错的药，\x01",
            "我想肯定能帮到你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xC,
        (
            "请不必客气。\x01",
            "各位尽管收下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1001F哇，谢谢。\x02\x03",

            "既然这样的话\x01",
            "我们就不客气地收下啰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xC,
        (
            "此外还摆放着很多\x01",
            "能在工作上提供方便的药物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xC,
        (
            "有需要的时候，\x01",
            "请多关照啰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1016F嗯，知道了。\x02\x03",

            "（不，不愧是生意人……\x01",
            "  永远不忘记拉客。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BC")

    label("loc_234C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_25BC")
    TurnDirection(0xC, 0x101, 0)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #130
        0xC,
        "啊，各位是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xC,
        (
            "曾经帮我寻找药草的\x01",
            "游击士们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1016F好像…这么说\x01",
            "是有这么回事。\x02\x03",

            "#1000F好久不见。\x01",
            "老爷爷您还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xC,
        "嗯嗯，还是老样子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xC,
        (
            "不过那个时候\x01",
            "真是多亏了你的帮助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xC,
        (
            "既然机会这么难得，作为谢礼，\x01",
            "我送各位一件秘蔵的药品。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #136
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x205, 1)

    ChrTalk(    #137
        0xC,
        (
            "请不必客气，\x01",
            "各位尽管收下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xC,
        (
            "这是我的\x01",
            "一点心意啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1001F哇，谢谢。\x02\x03",

            "这样的话\x01",
            "就不客气地收下啰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xC,
        (
            "此外还摆放着很多\x01",
            "能在工作上提供方便的药物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xC,
        (
            "有需要的时候，\x01",
            "请多关照啰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1016F嗯，知道了。\x02\x03",

            "（不，不愧是生意人……\x01",
            "  永远不忘记拉客。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25BC")

    OP_A2(0x1A40)
    OP_A2(0x4)

    label("loc_25C2")

    TalkEnd(0xC)
    Return()

    # Function_15_17CD end

    def Function_16_25C6(): pass

    label("Function_16_25C6")

    TalkBegin(0xD)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2634")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2629")
    OP_A9(0x3F)
    Jump("loc_262B")

    label("loc_2629")

    OP_A9(0x5E)

    label("loc_262B")

    OP_56(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_2634")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2645")
    TalkEnd(0xD)
    Return()

    label("loc_2645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_273C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26BF")

    ChrTalk(    #143
        0xD,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xD,
        (
            "柏斯超市的招牌商品，\x01",
            "美味可口，尝过之后必定难忘的蛋糕～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xD,
        "来一块怎么样！！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2739")

    label("loc_26BF")


    ChrTalk(    #146
        0xD,
        (
            "一心想让客人们\x01",
            "打起精神来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xD,
        (
            "于是就跟大家伙一起\x01",
            "举办了大酬宾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xD,
        (
            "至少在买东西的时候\x01",
            "希望看到大家的笑脸。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x7)

    label("loc_2739")

    Jump("loc_29DC")

    label("loc_273C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E6")

    ChrTalk(    #149
        0xD,
        (
            "对做蛋糕来说，\x01",
            "新鲜的鸡蛋和牛奶是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xD,
        (
            "今后如果一直无法进到材料的话，\x01",
            "我的摊位将开不下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xD,
        (
            "唉，真是的……\x01",
            "到底该怎么办才好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2854")

    label("loc_27E6")


    ChrTalk(    #152
        0xD,
        (
            "对做蛋糕来说，\x01",
            "新鲜的鸡蛋和牛奶是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xD,
        (
            "今后如果一直无法进到材料的话，\x01",
            "我的摊位将开不下去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2854")

    Jump("loc_29DC")

    label("loc_2857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2914")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_28BF")

    ChrTalk(    #154
        0xD,
        (
            "柏斯超市的招牌产品，\x01",
            "美味可口，尝过之后必定难忘的鸡蛋糕～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xD,
        "来一块怎么样！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2911")

    label("loc_28BF")


    ChrTalk(    #156
        0xD,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xD,
        (
            "柏斯超市的招牌商品，\x01",
            "美味可口，尝过之后必定难忘的蛋糕～！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2911")

    Jump("loc_29DC")

    label("loc_2914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_29DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2974")

    ChrTalk(    #158
        0xD,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xD,
        (
            "柏斯超市的招牌商品，\x01",
            "美味可口，尝过之后必定难忘的蛋糕～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29DC")

    label("loc_2974")


    ChrTalk(    #160
        0xD,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xD,
        (
            "柏斯超市的招牌商品，\x01",
            "美味可口，尝过之后必定难忘的蛋糕～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xD,
        "来一块怎么样！！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_29DC")

    TalkEnd(0xD)
    Return()

    # Function_16_25C6 end

    def Function_17_29E0(): pass

    label("Function_17_29E0")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4E")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A43")
    OP_A9(0x43)
    Jump("loc_2A45")

    label("loc_2A43")

    OP_A9(0x5B)

    label("loc_2A45")

    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_2A4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A5F")
    TalkEnd(0xE)
    Return()

    label("loc_2A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2BA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B63")

    ChrTalk(    #163
        0xE,
        (
            "全店大酬宾\x01",
            "可真是个不错的计划。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xE,
        (
            "卡特丽亚那家伙也来了干劲，\x01",
            "我们也参加了酬宾哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xE,
        (
            "总之，\x01",
            "此事全靠梅贝尔市长的协助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xE,
        (
            "市长说服了大商人，\x01",
            "让他们不要不舍得把库存的商品拿出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xE,
        (
            "假如不这么做的话，\x01",
            "现在物价肯定飞速上涨了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2B9D")

    label("loc_2B63")


    ChrTalk(    #168
        0xE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xE,
        (
            "在王都也很受欢迎的\x01",
            "美味冰淇淋哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x8)

    label("loc_2B9D")

    Jump("loc_2D6C")

    label("loc_2BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2A")

    ChrTalk(    #170
        0xE,
        (
            "超市里也完全\x01",
            "失去了活力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xE,
        (
            "大家果然对今后\x01",
            "会怎样很不安呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xE,
        (
            "可恶，越是这种时候，\x01",
            "就越想出一份力，但……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2C76")

    label("loc_2C2A")


    ChrTalk(    #173
        0xE,
        (
            "连超市\x01",
            "都消沉下来就全完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xE,
        (
            "越是这种时候，\x01",
            "就越想出一份力，但……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C76")

    Jump("loc_2D6C")

    label("loc_2C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2CF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2CBA")

    ChrTalk(    #175
        0xE,
        "欢迎光临，欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xE,
        "美味的冰淇淋哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CEE")

    label("loc_2CBA")


    ChrTalk(    #177
        0xE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xE,
        (
            "美味的冰淇淋也\x01",
            "终于复活了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2CEE")

    Jump("loc_2D6C")

    label("loc_2CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2D6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2D32")

    ChrTalk(    #179
        0xE,
        "欢迎光临，欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xE,
        "美味的冰淇淋哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D6C")

    label("loc_2D32")


    ChrTalk(    #181
        0xE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xE,
        (
            "在王都也很受欢迎的\x01",
            "美味冰淇淋哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2D6C")

    TalkEnd(0xE)
    Return()

    # Function_17_29E0 end

    def Function_18_2D70(): pass

    label("Function_18_2D70")

    Call(0, 19)
    Return()

    # Function_18_2D70 end

    def Function_19_2D75(): pass

    label("Function_19_2D75")

    TalkBegin(0xF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE3")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD8")
    OP_A9(0x41)
    Jump("loc_2DDA")

    label("loc_2DD8")

    OP_A9(0x5D)

    label("loc_2DDA")

    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_2DE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DF4")
    TalkEnd(0xF)
    Return()

    label("loc_2DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E82")

    ChrTalk(    #183
        0xF,
        (
            "欢迎光临。\x01",
            "不嫌弃的话请看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xF,
        (
            "哈哈，已经很久没有\x01",
            "这么大声招呼客人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xF,
        (
            "因为这种经验方式\x01",
            "不是我的风格嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_2EBF")

    label("loc_2E82")


    ChrTalk(    #186
        0xF,
        (
            "欢迎光临。\x01",
            "不嫌弃的话请看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xF,
        "肯定能让你满意的。\x02",
    )

    CloseMessageWindow()

    label("loc_2EBF")

    Jump("loc_3383")

    label("loc_2EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_300E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F9D")

    ChrTalk(    #188
        0xF,
        (
            "导力器竟然无法使用……\x01",
            "真是一点办法也没有了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xF,
        (
            "我家的照明灯也坏了，\x01",
            "女儿为此大哭了一场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xF,
        (
            "对那个孩子来说，\x01",
            "导力器是理所当然的日常用品啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xF,
        (
            "当知道无法使用后，\x01",
            "对她或许是一大打击吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_300B")

    label("loc_2F9D")


    ChrTalk(    #192
        0xF,
        (
            "到了我女儿这一代，\x01",
            "导力器已经成了理所当然的日用品了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xF,
        (
            "对孩子们的打击\x01",
            "或许比我们大人更大也说不定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_300B")

    Jump("loc_3383")

    label("loc_300E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3105")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3071")

    ChrTalk(    #194
        0xF,
        (
            "一定要带女儿来\x01",
            "恢复营业后的超市看看呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xF,
        (
            "要让她知道\x01",
            "这座镇子已经安全了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3102")

    label("loc_3071")


    ChrTalk(    #196
        0xF,
        (
            "我把女儿艾尔珂带来了，\x01",
            "想让她看看\x01",
            "超市恢复营业后的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xF,
        (
            "因为女儿她\x01",
            "可是我们这里的招牌啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xF,
        (
            "『泊尔·艾尔珂』\x01",
            "今后就请多关照了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_3102")

    Jump("loc_3383")

    label("loc_3105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 1)), scpexpr(EXPR_END)), "loc_322A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_318F")

    ChrTalk(    #199
        0xF,
        (
            "王都的商店和柏斯的果然各有千秋，\x01",
            "真是不分伯仲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xF,
        (
            "为了商店能够大张旗鼓地营业，\x01",
            "我要更加专心致志才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3227")

    label("loc_318F")

    TurnDirection(0xF, 0x101, 0)

    ChrTalk(    #201
        0xF,
        "嗯，你的这件衣服……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xF,
        (
            "明明是出于以实用设计为目的，\x01",
            "但却保留了少女那种楚楚动人的韵味……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xF,
        (
            "虽然不甘心，\x01",
            "但不愧是王都一流的品牌啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_3227")

    Jump("loc_3383")

    label("loc_322A")


    ChrTalk(    #204
        0xF,
        (
            "欢迎光临。\x01",
            "今天想看些什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xF, 0x101, 400)
    Sleep(400)

    ChrTalk(    #205
        0xF,
        (
            "噢，这件衣服……\x01",
            "是王都的牌子吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        "#1004F嘿，真清楚呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32DE")

    ChrTalk(    #207
        0x103,
        "#021F呵呵，不愧是行家。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x103, 400)

    label("loc_32DE")


    ChrTalk(    #208
        0xF,
        (
            "哈哈，这个嘛，\x01",
            "和以前所见过的品牌不同嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #209
        0xF,
        (
            "但是，一流品牌……\x01",
            "这也是订做的吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xF,
        (
            "虽然很不甘心……\x01",
            "但这设计实在太棒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xF,
        "唉，我也要加油了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A41)

    label("loc_3383")

    TalkEnd(0xF)
    Return()

    # Function_19_2D75 end

    def Function_20_3387(): pass

    label("Function_20_3387")

    TalkBegin(0x10)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3423")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F6")
    OP_A9(0x4C)
    Jump("loc_33F8")

    label("loc_33F6")

    OP_A9(0x4D)

    label("loc_33F8")

    Jump("loc_341A")

    label("loc_33FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340C")
    OP_A9(0x45)
    Jump("loc_341A")

    label("loc_340C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3418")
    OP_A9(0x44)
    Jump("loc_341A")

    label("loc_3418")

    OP_A9(0x42)

    label("loc_341A")

    OP_56(0x0)
    TalkEnd(0x10)
    Return()

    label("loc_3423")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3434")
    TalkEnd(0x10)
    Return()

    label("loc_3434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_35A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355D")

    ChrTalk(    #212
        0x10,
        (
            "全店大酬宾\x01",
            "这事和我无关啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x10,
        (
            "反正我的店铺\x01",
            "每天都在营业嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x10,
        (
            "呵呵，本店也打算作为赞助商\x01",
            "让售卖廉价商品的活动流行起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "喂喂，那边的小姑娘，\x01",
            "读读这本书打起精神来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #216
        "\x07\x00得到了\x1F\x47\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x247, 1)
    OP_A2(0x10C2)
    OP_0D()

    ChrTalk(    #217
        0x101,
        "#1004F哇，谢谢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35A3")

    label("loc_355D")


    ChrTalk(    #218
        0x10,
        (
            "全店的大酬宾\x01",
            "这事和我无关啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x10,
        (
            "反正我的店铺\x01",
            "每天都在营业嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A3")

    Jump("loc_38D4")

    label("loc_35A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_36B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3650")

    ChrTalk(    #220
        0xFE,
        (
            "不管物流停滞与否，\x01",
            "我店跟平时一样准时开门哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "正是这种时候，\x01",
            "才更要让大家鼓起勇气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "……这样的话，\x01",
            "不如把秘藏的那本新刊拿出来卖吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_36B2")

    label("loc_3650")


    ChrTalk(    #223
        0xFE,
        (
            "正是这种时候，\x01",
            "才更要让大家鼓起勇气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "……这样的话，\x01",
            "不如把秘藏的那本新刊拿出来卖吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B2")

    Jump("loc_38D4")

    label("loc_36B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_37E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_370D")

    ChrTalk(    #225
        0x10,
        (
            "共和国制最高級的绒毯～\x01",
            "只要５００米拉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x10,
        "并且买一张送一张哟！\x02",
    )

    CloseMessageWindow()
    Jump("loc_37E5")

    label("loc_370D")


    ChrTalk(    #227
        0x10,
        (
            "看一看。\x01",
            "瞧一瞧！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x10,
        (
            "共和国制最高級的绒毯～\x01",
            "只要５００米拉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x10,
        "只要５００米拉哟！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x10,
        "除此之外！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x10,
        (
            "现在正值\x01",
            "恢复营业的纪念活动期间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x10,
        (
            "买一条绒毯\x01",
            "#4S送一条绒毯！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x10,
        "走过路过千万不要错过！\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_37E5")

    Jump("loc_38D4")

    label("loc_37E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_38D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_385D")

    ChrTalk(    #234
        0x10,
        (
            "古书，纺织品，日用品，应有尽有！\x01",
            "这就是米蕾婆婆的杂货店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x10,
        (
            "请来看一看。\x01",
            "杂志的新刊也到啰。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D4")

    label("loc_385D")


    ChrTalk(    #236
        0x10,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x10,
        (
            "古书，纺织品，日用品，应有尽有！\x01",
            "这就是米蕾婆婆的杂货店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x10,
        (
            "请来看一看。\x01",
            "杂志的新刊也到啰。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_38D4")

    TalkEnd(0x10)
    Return()

    # Function_20_3387 end

    def Function_21_38D8(): pass

    label("Function_21_38D8")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_39B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3969")

    ChrTalk(    #239
        0x11,
        (
            "不愧是大酬宾，\x01",
            "超市很有活力了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x11,
        (
            "感觉很久以前的\x01",
            "活力又回来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x11,
        (
            "再加上小姐前来视察，\x01",
            "大家格外的卖力呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_39B5")

    label("loc_3969")


    ChrTalk(    #242
        0x11,
        (
            "不愧是大酬宾，\x01",
            "超市很有活力了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x11,
        (
            "感觉很久以前的\x01",
            "活力又回来了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39B5")

    Jump("loc_3CD8")

    label("loc_39B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3AC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A72")

    ChrTalk(    #244
        0x11,
        "呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x11,
        (
            "虽然米蕾婆婆很有精神……\x01",
            "但是超市其他的店铺气氛\x01",
            "有点消沉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x11,
        (
            "好不容易恢复了营业，\x01",
            "谁知物流却突然瘫痪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x11,
        "因此变得消沉也是没有办法的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_3AC2")

    label("loc_3A72")


    ChrTalk(    #248
        0x11,
        (
            "米蕾婆婆\x01",
            "跟平时一样精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x11,
        (
            "婆婆的生意人精神\x01",
            "在柏斯里是首屈一指的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC2")

    Jump("loc_3CD8")

    label("loc_3AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3BAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3B24")

    ChrTalk(    #250
        0x11,
        (
            "军队的戒严解除了，\x01",
            "物流也恢复了正常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x11,
        (
            "因此，\x01",
            "新刊也差不多快送到了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA9")

    label("loc_3B24")


    ChrTalk(    #252
        0x11,
        "呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x11,
        (
            "军队的戒严解除了，\x01",
            "物流总算恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x11,
        (
            "因此，\x01",
            "我们这里新刊也开始陆续到货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x11,
        "不介意的话来看看吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3BA9")

    Jump("loc_3CD8")

    label("loc_3BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3CD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3C1D")

    ChrTalk(    #256
        0x11,
        (
            "别看我这样，\x01",
            "其实我是这间店铺的店员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x11,
        (
            "因为我太喜欢书，\x01",
            "所以被人招来这里，当起了店员。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD8")

    label("loc_3C1D")


    ChrTalk(    #258
        0x11,
        (
            "呀，欢迎。\x01",
            "最新号的杂志已经到啰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x11,
        (
            "别看我这样，\x01",
            "其实我是这间店铺的店员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x11,
        (
            "因为我太喜欢书，\x01",
            "所以被人招来这里，当起了店员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x11,
        (
            "呵呵，\x01",
            "没想到会在经常光顾的店里当起店员来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3CD8")

    TalkEnd(0x11)
    Return()

    # Function_21_38D8 end

    def Function_22_3CDC(): pass

    label("Function_22_3CDC")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3DDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D85")

    ChrTalk(    #262
        0xFE,
        (
            "呵呵呵，就是这个。\x01",
            "我一直在等的就是这个！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "酬宾，特卖，大减价！！\x01",
            "啊啊，多么动听的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "只要听到这些词语，\x01",
            "不管何时都会精神百倍！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_3DDC")

    label("loc_3D85")


    ChrTalk(    #265
        0xFE,
        (
            "假如有特卖会的话，\x01",
            "最佳位置是绝对不会让给别人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        "哼哼，开始的同时发动攻击！\x02",
    )

    CloseMessageWindow()

    label("loc_3DDC")

    Jump("loc_401B")

    label("loc_3DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3E53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E50")

    ChrTalk(    #267
        0xFE,
        (
            "定期船和货车都停开了，\x01",
            "这的确是最严重的事态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "总之，\x01",
            "得趁物品尚未短缺之前大买特买才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E50")

    Jump("loc_401B")

    label("loc_3E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3F48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3ECA")

    ChrTalk(    #269
        0xFE,
        (
            "呵呵呵，\x01",
            "今天有一场为纪念重新开业的大酬宾呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "我特意早早赶来排队，\x01",
            "就是为了确保最佳的位置。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F45")

    label("loc_3ECA")


    ChrTalk(    #271
        0xFE,
        (
            "呵呵呵，\x01",
            "今天有一场为纪念重新开业的大酬宾呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "啊啊，久违的大减价啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "最佳位置，\x01",
            "是绝对不会让给别人的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3F45")

    Jump("loc_401B")

    label("loc_3F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_401B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3F9F")

    ChrTalk(    #274
        0xFE,
        (
            "上午的特卖会\x01",
            "好像结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "下一个目标是\x01",
            "傍晚的限时大甩卖。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_401B")

    label("loc_3F9F")


    ChrTalk(    #276
        0xFE,
        (
            "那么，上午的特卖\x01",
            "好像结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "呵呵，\x01",
            "今天当然也把每家店铺都逛过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "收获就是……\x01",
            "肉的最低价又被刷新了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_401B")

    TalkEnd(0x12)
    Return()

    # Function_22_3CDC end

    def Function_23_401F(): pass

    label("Function_23_401F")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_40B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4076")

    ChrTalk(    #279
        0xFE,
        (
            "酬宾就是……\x01",
            "大型展销会吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        "这样啊，丽露露也知道啦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_40AF")

    label("loc_4076")


    ChrTalk(    #281
        0xFE,
        (
            "在酬宾时买东西\x01",
            "妈妈会很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "好，要加油了。\x02",
    )

    CloseMessageWindow()

    label("loc_40AF")

    Jump("loc_42C9")

    label("loc_40B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4114")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F5")

    ChrTalk(    #283
        0xFE,
        "喷水池也没有精神呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "怎么回事啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_4111")

    label("loc_40F5")


    ChrTalk(    #285
        0xFE,
        "喷水池也没有精神呢……\x02",
    )

    CloseMessageWindow()

    label("loc_4111")

    Jump("loc_42C9")

    label("loc_4114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_41EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4167")

    ChrTalk(    #286
        0xFE,
        (
            "嘿嘿，\x01",
            "今天吃蛋糕！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "蛋糕……蛋糕……\x01",
            "蛋糕……蛋～～糕⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41EB")

    label("loc_4167")


    ChrTalk(    #288
        0xFE,
        (
            "嘿嘿，今天\x01",
            "我可不是被人叫出来买东西的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "那你是得到了零用钱，\x01",
            "自己来买东西的了⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "我要吃姐姐卖的那种\x01",
            "软绵绵的蛋糕！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_41EB")

    Jump("loc_42C9")

    label("loc_41EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_42C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4249")

    ChrTalk(    #291
        0xFE,
        (
            "奶酪加上苹果加上\x01",
            "香喷喷的芋头⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "奶酪加上苹果加上\x01",
            "香喷喷的芋头⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C9")

    label("loc_4249")


    ChrTalk(    #293
        0xFE,
        (
            "已经可以一个人\x01",
            "去买东西了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "那个，\x01",
            "就是把买的东西编成歌记住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "奶酪加上苹果加上\x01",
            "香芋头⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        "嘿嘿，厉害吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_42C9")

    TalkEnd(0x14)
    Return()

    # Function_23_401F end

    def Function_24_42CD(): pass

    label("Function_24_42CD")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_43BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_436A")

    ChrTalk(    #297
        0xFE,
        (
            "嘻嘻。\x01",
            "在这种时候卖东西？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "呵呵，岂止是一点点，\x01",
            "这不是一件非常令人愉快的事吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "不愧是柏斯超市。\x01",
            "非常理解百姓的心情啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_43BA")

    label("loc_436A")


    ChrTalk(    #300
        0xFE,
        (
            "这么难得的大减价，\x01",
            "真想做一道丰盛的晚餐呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "呵呵，\x01",
            "今天要做什么菜呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43BA")

    Jump("loc_4689")

    label("loc_43BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4429")

    ChrTalk(    #302
        0xFE,
        (
            "由于导力器停止了工作，\x01",
            "照明和暖房都无法使用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        (
            "吃的东西买好了，\x01",
            "接下来得去看看杂货了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4689")

    label("loc_4429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_45EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_44F5")

    ChrTalk(    #304
        0xFE,
        (
            "如果店铺能在卖菜的同时提供菜单就好了。\x01",
            "那样就可以从中得到做菜的灵感也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "这样的话就能\x01",
            "帮主妇们分忧解难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "嗯，细想一下这是理所当然的吧。\x01",
            "得赶紧去和店里的人沟通一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E8")

    label("loc_44F5")


    ChrTalk(    #307
        0xFE,
        (
            "肉，蔬菜，鱼……\x01",
            "唉，今天该怎么办呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        (
            "作为店铺，不能光是售卖做菜的材料。\x01",
            "要是也能提供菜单给顾客就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        "……细想之下确实如此啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "在买吸尘器的时候，\x01",
            "店员不是也会教我们使用的方法吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        (
            "鱼和肉之类的\x01",
            "为什么不能也这样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_45E8")

    Jump("loc_4689")

    label("loc_45EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_4689")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_4642")

    ChrTalk(    #312
        0xFE,
        (
            "嗯，\x01",
            "今天做什么菜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "干脆去看看有什么特卖品\x01",
            "配合着来做吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4689")

    label("loc_4642")


    ChrTalk(    #314
        0xFE,
        (
            "今日的配菜\x01",
            "做什么好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        (
            "要在傍晚的特卖开始前\x01",
            "决定好才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_4689")

    TalkEnd(0x15)
    Return()

    # Function_24_42CD end

    def Function_25_468D(): pass

    label("Function_25_468D")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_4721")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4701")

    ChrTalk(    #316
        0xFE,
        (
            "超市终于\x01",
            "恢复往日的样子啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        (
            "嗯，看来今天能够集中精神\x01",
            "进行古董鉴赏了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    OP_A2(0xF)
    Jump("loc_471E")

    label("loc_4701")


    ChrTalk(    #318
        0xFE,
        (
            "嗯…\x01",
            "这碟子相当高级啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_471E")

    Jump("loc_499F")

    label("loc_4721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4809")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47AC")

    ChrTalk(    #319
        0xFE,
        (
            "导力器全都瘫痪了，\x01",
            "连保卫国家都做不到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        "心里总觉得有点不安呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        (
            "帝国若是能\x01",
            "遵守互不侵犯条约就好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_4806")

    label("loc_47AC")


    ChrTalk(    #322
        0xFE,
        (
            "导力器全都瘫痪了，\x01",
            "连保卫国家都做不到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "帝国若是能\x01",
            "遵守互不侵犯条约就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4806")

    Jump("loc_499F")

    label("loc_4809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_4915")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_487C")

    ChrTalk(    #324
        0xFE,
        (
            "前几天，\x01",
            "我得到了去市长官邸参观古董的机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "近距离观赏那些珍品，\x01",
            "使我的眼光得到了磨练。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4912")

    label("loc_487C")


    ChrTalk(    #326
        0xFE,
        (
            "前几天，\x01",
            "机缘巧合下拜访了市长官邸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xFE,
        (
            "参观了官邸内的\x01",
            "很多古董。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        "呀，真品果然非同一般啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        (
            "拜那次机会所赐，\x01",
            "我的眼光也得到了磨练。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_4912")

    Jump("loc_499F")

    label("loc_4915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_499F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_4947")

    ChrTalk(    #330
        0xFE,
        (
            "呵呵，\x01",
            "这件东西相当不错啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_499F")

    label("loc_4947")


    ChrTalk(    #331
        0xFE,
        "我对古董很感兴趣。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        (
            "像这样寻找出土的文物，\x01",
            "就是我每天都要做的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    OP_8C(0x16, 90, 0)
    SetChrFlags(0x16, 0x10)

    label("loc_499F")

    TalkEnd(0x16)
    Return()

    # Function_25_468D end

    def Function_26_49A3(): pass

    label("Function_26_49A3")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4A79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A26")

    ChrTalk(    #333
        0xFE,
        (
            "啊啊，\x01",
            "超市果然是个好地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        (
            "听着大家的声音，\x01",
            "我也精神百倍了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        (
            "呵呵，\x01",
            "下定决心来了可真好……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_4A76")

    label("loc_4A26")


    ChrTalk(    #336
        0xFE,
        (
            "听着精神十足的声音，\x01",
            "我也精神百倍了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        (
            "呵呵，\x01",
            "超市果然还是要这样才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A76")

    Jump("loc_4BFB")

    label("loc_4A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_4ACB")

    ChrTalk(    #338
        0xFE,
        (
            "大家的脸上\x01",
            "又恢复了笑容了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xFE,
        (
            "超市果然是\x01",
            "这座柏斯市的象征啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BFB")

    label("loc_4ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_4BFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_4B51")

    ChrTalk(    #340
        0xFE,
        (
            "来到超市，\x01",
            "让我感觉到了人们的活力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        (
            "这是因为\x01",
            "我从小就在这里长大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        (
            "我被这充满生机的世界\x01",
            "深深的吸引了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BFB")

    label("loc_4B51")


    ChrTalk(    #343
        0xFE,
        (
            "父母禁止我\x01",
            "来超市……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        (
            "我一直瞒着他们\x01",
            "来这里玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xFE,
        (
            "我非常喜欢这\x01",
            "超市的气氛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        (
            "虽然人来人往的，\x01",
            "的确不是非常整洁的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xFE,
        (
            "但这里的人们\x01",
            "充满了活力。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_4BFB")

    TalkEnd(0x13)
    Return()

    # Function_26_49A3 end

    def Function_27_4BFF(): pass

    label("Function_27_4BFF")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_4D1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CC3")

    ChrTalk(    #348
        0xFE,
        (
            "蛋糕店的姐姐\x01",
            "也恢复往常的笑容了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xFE,
        (
            "或许是受到了\x01",
            "开冰淇淋店的未婚夫的鼓励吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        (
            "假如真的是这样的话，\x01",
            "我们就认同那个家伙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        (
            "今后也希望他能够\x01",
            "保护那位姐姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_4D19")

    label("loc_4CC3")


    ChrTalk(    #352
        0xFE,
        (
            "蛋糕店的姐姐\x01",
            "也恢复往常的笑容了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        (
            "或许是受到了\x01",
            "开冰淇淋店的未婚夫的鼓励吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D19")

    Jump("loc_509B")

    label("loc_4D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4E6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E1A")

    ChrTalk(    #354
        0xFE,
        (
            "蛋糕店的姐姐\x01",
            "好像也无精打采的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xFE,
        (
            "唉，情况这么糟糕，\x01",
            "不管换了是谁都会这样吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        (
            "不过，\x01",
            "她的未婚夫干什么去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xFE,
        (
            "这种时候在身旁给予支持，\x01",
            "不是身为伴侣的职责吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        (
            "真是的……要不趁着买东西的时候\x01",
            "好好教育那家伙一番吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_4E6C")

    label("loc_4E1A")


    ChrTalk(    #359
        0xFE,
        (
            "姐姐一点精神都没有，\x01",
            "她的未婚夫跑去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xFE,
        (
            "还真想过去\x01",
            "教训教训他一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E6C")

    Jump("loc_509B")

    label("loc_4E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_4F22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_4ECE")

    ChrTalk(    #361
        0xFE,
        (
            "姐姐还是\x01",
            "露出开朗笑容的时候最棒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        (
            "明明肚子饱饱的\x01",
            "却又想买蛋糕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F1F")

    label("loc_4ECE")


    ChrTalk(    #363
        0xFE,
        (
            "蛋糕店姐姐的笑容\x01",
            "真是耀眼啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xFE,
        (
            "全力帮忙施工来的，\x01",
            "觉得十分有意义哟。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_4F1F")

    Jump("loc_509B")

    label("loc_4F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_509B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_4FB6")

    ChrTalk(    #365
        0xFE,
        (
            "那个卖蛋糕的未婚夫\x01",
            "就在对面经营冰淇淋店呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        (
            "既然都订婚了，\x01",
            "怎么不一起开店呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        (
            "不过，作为姐姐的仰慕者\x01",
            "其实这样倒好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_509B")

    label("loc_4FB6")


    ChrTalk(    #368
        0xFE,
        (
            "啊啊，蛋糕店的\x01",
            "姐姐笑起来真是漂亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xFE,
        (
            "不过，其实那位姐姐\x01",
            "已经有约定将来的人了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        (
            "那年轻人就在对面\x01",
            "开冰淇淋店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        (
            "好像是个不服输的人，\x01",
            "为了不输给姐姐的店\x01",
            "自己也开了店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        (
            "既然都订婚了，\x01",
            "一起开店不就好了吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_509B")

    TalkEnd(0x17)
    Return()

    # Function_27_4BFF end

    def Function_28_509F(): pass

    label("Function_28_509F")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_51BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_515D")

    ChrTalk(    #373
        0xFE,
        (
            "超市全店好像\x01",
            "都开始打折了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xFE,
        (
            "这、这种时候\x01",
            "竟然会打折…真是厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xFE,
        (
            "不愧是柏斯超市。\x01",
            "真有种顾客至上的感觉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xFE,
        (
            "我、我再不振作精神\x01",
            "可就跟不上了哦……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_51B7")

    label("loc_515D")


    ChrTalk(    #377
        0xFE,
        (
            "这种时候竟然会打折，\x01",
            "不愧是柏斯超市啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        (
            "我、我也不该因为\x01",
            "开店迟了就惶惶不安的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51B7")

    Jump("loc_5456")

    label("loc_51BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_528B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5244")

    ChrTalk(    #379
        0xFE,
        (
            "由于出现了些问题，\x01",
            "商品还没到达……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xFE,
        (
            "我的店开张营业\x01",
            "也要大幅延期了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "虽说现在这状况\x01",
            "也顾不上这种事了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_5288")

    label("loc_5244")


    ChrTalk(    #382
        0xFE,
        (
            "今天超市里也\x01",
            "没什么活力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xFE,
        (
            "我也是这样，\x01",
            "大家都很不安呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5288")

    Jump("loc_5456")

    label("loc_528B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_5373")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_52E4")

    ChrTalk(    #384
        0xFE,
        (
            "看来古代龙\x01",
            "也已经离开了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xFE,
        (
            "这样我也可以放下心来\x01",
            "准备开店了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5370")

    label("loc_52E4")


    ChrTalk(    #386
        0xFE,
        (
            "看来古代龙\x01",
            "好像到别的地方去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xFE,
        (
            "这样我也可以放下心来\x01",
            "准备开店了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0xFE,
        (
            "虽然估计离开张还要一段时间，\x01",
            "不过，到时候还请多关照哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_5370")

    Jump("loc_5456")

    label("loc_5373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_5456")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_53DE")

    ChrTalk(    #389
        0xFE,
        (
            "提交给超市的开店申请\x01",
            "终于被受理了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xFE,
        (
            "店预计就开在这附近，\x01",
            "小店开张时还请多关照！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5456")

    label("loc_53DE")


    ChrTalk(    #391
        0xFE,
        (
            "给超市的开店请求\x01",
            "终于被受理了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xFE,
        (
            "这就是我作为\x01",
            "商人的第一步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xFE,
        (
            "要不输给任何竞争对手，\x01",
            "开一个出色的店铺。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_5456")

    TalkEnd(0x18)
    Return()

    # Function_28_509F end

    def Function_29_545A(): pass

    label("Function_29_545A")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_54AC")

    ChrTalk(    #394
        0xFE,
        (
            "唉，人太多，\x01",
            "都不知道该问谁……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xFE,
        (
            "啊啊，那女孩到底\x01",
            "住在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54AC")

    TalkEnd(0x19)
    Return()

    # Function_29_545A end

    def Function_30_54B0(): pass

    label("Function_30_54B0")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_5591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_5514")

    ChrTalk(    #396
        0xFE,
        (
            "正在为新客人\x01",
            "做超市的向导。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0xFE,
        (
            "两人都是帝国的商人呢。\x01",
            "是很大方的顾客哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_558E")

    label("loc_5514")


    ChrTalk(    #398
        0xFE,
        (
            "正在为新客人\x01",
            "做超市的向导。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0xFE,
        (
            "两人都是帝国的商人呢。\x01",
            "是很大方的顾客哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xFE,
        (
            "今后和帝国的客人\x01",
            "交流也会增加吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_558E")

    Jump("loc_5639")

    label("loc_5591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_5639")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_55EA")

    ChrTalk(    #401
        0xFE,
        (
            "哎呀，要确认库存的\x01",
            "不是衣料品吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0xFE,
        (
            "工、工作太多\x01",
            "总是容易搞错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5639")

    label("loc_55EA")


    ChrTalk(    #403
        0xFE,
        (
            "嗯～接着是确认\x01",
            "绒毯的库存啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xFE,
        (
            "老样子…～\x01",
            "米拉诺还是那么爱使唤人。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_5639")

    TalkEnd(0x1A)
    Return()

    # Function_30_54B0 end

    def Function_31_563D(): pass

    label("Function_31_563D")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_5720")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_5692")

    ChrTalk(    #405
        0x1B,
        (
            "本来是来商谈的，\x01",
            "结果正赶上开始大减价。\x02\x03",

            "只好暂时等一下了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5720")

    label("loc_5692")


    ChrTalk(    #406
        0x1B,
        (
            "听说超市已经修复好了，\x01",
            "就立刻赶来进行商谈……\x02\x03",

            "结果时机却不太好，\x01",
            "正赶上开始大减价。\x02\x03",

            "一旦有便宜可以捡，婆婆就\x01",
            "说什么也不肯回家的了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_5720")

    TalkEnd(0x1B)
    Return()

    # Function_31_563D end

    def Function_32_5724(): pass

    label("Function_32_5724")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_57A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_5771")

    ChrTalk(    #407
        0xFE,
        (
            "今天是来爸爸的店里\x01",
            "帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0xFE,
        "嘿嘿，我会加油的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_57A7")

    label("loc_5771")


    ChrTalk(    #409
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0xFE,
        (
            "今天是来爸爸的店里\x01",
            "帮忙的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_57A7")

    TalkEnd(0x1C)
    Return()

    # Function_32_5724 end

    def Function_33_57AB(): pass

    label("Function_33_57AB")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_58B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_57FD")

    ChrTalk(    #411
        0xFE,
        (
            "最后终于\x01",
            "找到了签约对象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0xFE,
        (
            "哎呀呀，总算\x01",
            "保住了面子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58B0")

    label("loc_57FD")


    ChrTalk(    #413
        0xFE,
        (
            "在快绝望的时候\x01",
            "有位商人来找我谈合作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0xFE,
        (
            "总算在最后关头\x01",
            "找到了签约对象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0xFE,
        (
            "不过，在这种不明朗的形势下\x01",
            "还这么勇敢的推进交易……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0xFE,
        (
            "米拉诺这个商人。\x01",
            "还真是镇定啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)

    label("loc_58B0")

    TalkEnd(0x1D)
    Return()

    # Function_33_57AB end

    def Function_34_58B4(): pass

    label("Function_34_58B4")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_59D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_5924")

    ChrTalk(    #417
        0xFE,
        (
            "呀，真是热闹啊。\x01",
            "真难以想象这是小国的市场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0xFE,
        (
            "看来可以作为相当不错的\x01",
            "出口地市场哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59D3")

    label("loc_5924")


    ChrTalk(    #419
        0xFE,
        (
            "唔～这就是\x01",
            "柏斯超市啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xFE,
        (
            "呀，真是热闹啊。\x01",
            "真难以想象这是小国的市场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0xFE,
        (
            "我们帝国的产品\x01",
            "似乎也销售得很多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0xFE,
        (
            "唔唔，孤陋寡闻了啊。\x01",
            "看来作为出口地相当不错呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_59D3")

    TalkEnd(0x1E)
    Return()

    # Function_34_58B4 end

    def Function_35_59D7(): pass

    label("Function_35_59D7")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_5AC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A76")

    ChrTalk(    #423
        0xFE,
        (
            "为了修理收银机\x01",
            "去了南街区的工房……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xFE,
        (
            "可是据店主说\x01",
            "这好像不是故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0xFE,
        (
            "似乎今天上门询问故障的客人太多，\x01",
            "店主很疲劳的样子呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)
    Jump("loc_5AC4")

    label("loc_5A76")


    ChrTalk(    #426
        0xFE,
        (
            "我们的收银机\x01",
            "好像不是坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0xFE,
        (
            "唔～不能动的话，\x01",
            "那和故障就没区别了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AC4")

    Jump("loc_5B91")

    label("loc_5AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_5B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_5B0F")

    ChrTalk(    #428
        0xFE,
        (
            "暂时留在柏斯\x01",
            "帮忙店里干活吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0xFE,
        "好，加油啰～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B91")

    label("loc_5B0F")


    ChrTalk(    #430
        0xFE,
        "呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0xFE,
        (
            "暂时留在柏斯\x01",
            "帮忙店里干活吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0xFE,
        (
            "到现在为止一直\x01",
            "给妻子和波波添麻烦嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0xFE,
        (
            "多少也要\x01",
            "补偿他们一些才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)

    label("loc_5B91")

    TalkEnd(0x1F)
    Return()

    # Function_35_59D7 end

    def Function_36_5B95(): pass

    label("Function_36_5B95")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F95")
    TurnDirection(0x20, 0x101, 400)

    ChrTalk(    #434
        0x20,
        (
            "#613F呀，艾丝蒂尔，\x01",
            "还有约修亚也来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x101,
        "#1000F你好，梅贝尔市长。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x102,
        "#1040F……好久不见了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x102, 400)

    ChrTalk(    #437
        0x20,
        (
            "#611F呵呵，真的是……\x02\x03",

            "看起来还是\x01",
            "那么忙碌呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x101,
        (
            "#1016F市长也\x01",
            "很辛苦的样子嘛。\x02\x03",

            "我听卢格兰爷爷说了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x102,
        (
            "#1035F好像这里也有市民\x01",
            "冲进来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x20,
        (
            "#615F嗯嗯，一直说服到半夜\x01",
            "才总算让他们回去了。\x02\x03",

            "#612F不过，这样并不能\x01",
            "消除市民的不安。\x02\x03",

            "这个状况长久持续下去的话\x01",
            "恐怕还会引起骚乱的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x102,
        (
            "#1043F的确是这样……\x02\x03",

            "因为结果还是\x01",
            "什么也没能解决。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x101,
        (
            "#1006F不过，不管怎样\x01",
            "只能做力所能及的事了。\x02\x03",

            "就算低头烦恼，\x01",
            "导力器也不会动起来的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E1B")

    ChrTalk(    #443
        0x106,
        (
            "#051F啊啊，说得对。\x02\x03",

            "不管结果怎样，\x01",
            "我们都只能尽游击士的本分。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC8")

    label("loc_5E1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E72")

    ChrTalk(    #444
        0x103,
        (
            "#020F嗯嗯，说得对呢。\x02\x03",

            "无论结果如何，\x01",
            "我们都只能尽游击士的本分。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC8")

    label("loc_5E72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EC8")

    ChrTalk(    #445
        0x108,
        (
            "#070F噢，你说得对。\x02\x03",

            "尽人事听天命……\x01",
            "我们就尽游击士的本分就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EC8")

    TurnDirection(0x20, 0x101, 400)

    ChrTalk(    #446
        0x20,
        (
            "#610F呵呵，我也有同感。\x02\x03",

            "无论状况如何\x01",
            "保护城市是市长的职责……\x02\x03",

            "当然，我相信各位\x01",
            "最后终能解决问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x101,
        (
            "#1008F啊、啊哈哈……\x01",
            "这可是责任重大哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x102,
        (
            "#1049F我就当是\x01",
            "鼓励的话记下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x19)
    OP_A2(0x2090)
    Jump("loc_6097")

    label("loc_5F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_6001")

    ChrTalk(    #449
        0x20,
        (
            "#610F现在只有各自\x01",
            "尽力而为了吧。\x02\x03",

            "当这些努力积累在一起，\x01",
            "我相信一定能够成为\x01",
            "渡过危机的力量。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6097")

    label("loc_6001")


    ChrTalk(    #450
        0x20,
        (
            "#610F超市似乎也\x01",
            "恢复平静了。\x02\x03",

            "把物价安定下来\x01",
            "果然还是很重要的。\x02\x03",

            "年轻的商人们\x01",
            "也花了很多心思……\x02\x03",

            "#611F呵呵，按现在状况的话\x01",
            "应该可以稍微放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6097")

    TalkEnd(0x20)
    Return()

    # Function_36_5B95 end

    def Function_37_609B(): pass

    label("Function_37_609B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60A8")
    Return()

    label("loc_60A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_60BA")
    Return()

    label("loc_60BA")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x10)"), scpexpr(EXPR_END)), "loc_60F5")
    Call(0, 38)
    Jump("loc_61DB")

    label("loc_60F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xC)"), scpexpr(EXPR_END)), "loc_6104")
    Call(0, 39)
    Jump("loc_61DB")

    label("loc_6104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x9)"), scpexpr(EXPR_END)), "loc_6113")
    Call(0, 40)
    Jump("loc_61DB")

    label("loc_6113")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_6122")
    Call(0, 41)
    Jump("loc_61DB")

    label("loc_6122")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_6131")
    Call(0, 40)
    Jump("loc_61DB")

    label("loc_6131")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E9)"), scpexpr(EXPR_END)), "loc_6140")
    Call(0, 39)
    Jump("loc_61DB")

    label("loc_6140")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_EXEC_OP, "OP_CD(0x4E7)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_619D")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #451
        (
            "\x07\x05试着出示了照片，\x01",
            "但似乎没有见过的印象。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_61DB")

    label("loc_619D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #452
        "\x07\x05附近没有人可以确认照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_61DB")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_37_609B end

    def Function_38_61E2(): pass

    label("Function_38_61E2")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_623D")

    ChrTalk(    #453
        0x10,
        (
            "你们要努力\x01",
            "找到那个孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x10,
        (
            "因为战争而失散，\x01",
            "可以说是最可怜的事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62D8")

    label("loc_623D")


    ChrTalk(    #455
        0x10,
        "怎么，找人吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x10,
        (
            "……原来如此。\x01",
            "１０年前的事了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x10,
        "很遗憾，我没印象。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x10,
        "不过，要加油啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0x10,
        (
            "因为战争而失散，\x01",
            "可以说是最可怜的事了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_62D8")

    TalkEnd(0x10)
    Return()

    # Function_38_61E2 end

    def Function_39_62DC(): pass

    label("Function_39_62DC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_631A")

    ChrTalk(    #460
        0xC,
        (
            "很遗憾…\x01",
            "我没有印象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0xC,
        "请去问问别人吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6392")

    label("loc_631A")


    ChrTalk(    #462
        0xC,
        "噢，找人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0xC,
        (
            "嗯…\x01",
            "原来如此原来如此……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xC,
        (
            "唔～很遗憾…\x01",
            "我没印象呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xC,
        (
            "抱歉帮不上忙。\x01",
            "请去问问别人吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_6392")

    TalkEnd(0xC)
    Return()

    # Function_39_62DC end

    def Function_40_6396(): pass

    label("Function_40_6396")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_63E7")

    ChrTalk(    #466
        0x9,
        (
            "这照片里的女孩……\x01",
            "感觉好像见过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0x9,
        (
            "嗯～不过到底\x01",
            "是谁呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6455")

    label("loc_63E7")


    ChrTalk(    #468
        0x9,
        (
            "咦，这照片里的女孩……\x01",
            "感觉好像在哪儿见过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0x9,
        "嗯～不过可能只是有点像而已。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x9,
        "抱歉，请别在意。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_6455")

    TalkEnd(0x9)
    Return()

    # Function_40_6396 end

    def Function_41_6459(): pass

    label("Function_41_6459")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_64BC")

    ChrTalk(    #471
        0x8,
        (
            "绿色的眼睛\x01",
            "那么清澈，真是漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x8,
        (
            "附近要是有这样的孩子\x01",
            "我绝对不会放过的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_652F")

    label("loc_64BC")


    ChrTalk(    #473
        0x8,
        "哇，好可爱的女孩啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x8,
        (
            "绿色的眼睛\x01",
            "那么清澈，真是漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0x8,
        (
            "附近要是有这样的孩子\x01",
            "我绝对不会放过的呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_652F")

    TalkEnd(0x8)
    Return()

    # Function_41_6459 end

    SaveToFile()

Try(main)
