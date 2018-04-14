from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0001   ._SN',
        MapName             = 'event',
        Location            = 'E0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        '凯文神父',                             # 9
        '目标用照相机',                         # 10
        '科洛丝',                               # 11
        '基库',                                 # 12
        '奥利维尔',                             # 13
        '提妲',                                 # 14
        '雪拉扎德',                             # 15
        '阿加特',                               # 16
        '金',                                   # 17
        '乘客',                                 # 18
        '乘客',                                 # 19
        '乘客',                                 # 20
        '乘客',                                 # 21
        '提克',                                 # 22
        '莫莉',                                 # 23
        '安敦',                                 # 24
        '利库斯',                               # 25
        '法尔茨',                               # 26
        '诺蒂亚',                               # 27
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
        'ED6_DT27/CH03080 ._CH',             # 00
        'ED6_DT07/CH00040 ._CH',             # 01
        'ED6_DT07/CH02320 ._CH',             # 02
        'ED6_DT07/CH02323 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT07/CH00060 ._CH',             # 05
        'ED6_DT26/CH20311 ._CH',             # 06
        'ED6_DT07/CH00020 ._CH',             # 07
        'ED6_DT07/CH00050 ._CH',             # 08
        'ED6_DT07/CH00070 ._CH',             # 09
        'ED6_DT07/CH01470 ._CH',             # 0A
        'ED6_DT07/CH01170 ._CH',             # 0B
        'ED6_DT07/CH01130 ._CH',             # 0C
        'ED6_DT07/CH01150 ._CH',             # 0D
        'ED6_DT27/CH03085 ._CH',             # 0E
        'ED6_DT07/CH00004 ._CH',             # 0F
        'ED6_DT26/CH20236 ._CH',             # 10
        'ED6_DT06/CH20045 ._CH',             # 11
        'ED6_DT26/CH20241 ._CH',             # 12
        'ED6_DT07/CH01040 ._CH',             # 13
        'ED6_DT07/CH01050 ._CH',             # 14
        'ED6_DT07/CH01140 ._CH',             # 15
        'ED6_DT07/CH01210 ._CH',             # 16
        'ED6_DT07/CH01140 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT27/CH03080P._CP',             # 00
        'ED6_DT07/CH00040P._CP',             # 01
        'ED6_DT07/CH02320P._CP',             # 02
        'ED6_DT07/CH02323P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT07/CH00060P._CP',             # 05
        'ED6_DT26/CH20311P._CP',             # 06
        'ED6_DT07/CH00020P._CP',             # 07
        'ED6_DT07/CH00050P._CP',             # 08
        'ED6_DT07/CH00070P._CP',             # 09
        'ED6_DT07/CH01470P._CP',             # 0A
        'ED6_DT07/CH01170P._CP',             # 0B
        'ED6_DT07/CH01130P._CP',             # 0C
        'ED6_DT07/CH01150P._CP',             # 0D
        'ED6_DT27/CH03085P._CP',             # 0E
        'ED6_DT07/CH00004P._CP',             # 0F
        'ED6_DT26/CH20236P._CP',             # 10
        'ED6_DT06/CH20045P._CP',             # 11
        'ED6_DT26/CH20241P._CP',             # 12
        'ED6_DT07/CH01040P._CP',             # 13
        'ED6_DT07/CH01050P._CP',             # 14
        'ED6_DT07/CH01140P._CP',             # 15
        'ED6_DT07/CH01210P._CP',             # 16
        'ED6_DT07/CH01140P._CP',             # 17
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
        X                   = 3200,
        Z                   = 5000,
        Y                   = -4800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        X                   = 59030,
        Z                   = -1800,
        Y                   = 54020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -2220,
        Z                   = 5000,
        Y                   = -2440,
        Direction           = 128,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 59030,
        Z                   = -1800,
        Y                   = 54020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 5000,
        Y                   = 180,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 5000,
        Y                   = 3860,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 5000,
        Y                   = 4800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -480,
        Z                   = 5000,
        Y                   = -10950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 480,
        Z                   = 5000,
        Y                   = -10950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 5000,
        Y                   = -4050,
        Direction           = 265,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 5000,
        Y                   = -5190,
        Direction           = 271,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )


    ScpFunction(
        "Function_0_3CA",          # 00, 0
        "Function_1_588",          # 01, 1
        "Function_2_5F2",          # 02, 2
        "Function_3_76F",          # 03, 3
        "Function_4_793",          # 04, 4
        "Function_5_7B7",          # 05, 5
        "Function_6_7DE",          # 06, 6
        "Function_7_8B1",          # 07, 7
        "Function_8_AAB",          # 08, 8
        "Function_9_C4C",          # 09, 9
        "Function_10_CED",         # 0A, 10
        "Function_11_D46",         # 0B, 11
        "Function_12_DC7",         # 0C, 12
        "Function_13_E10",         # 0D, 13
        "Function_14_E5E",         # 0E, 14
        "Function_15_F69",         # 0F, 15
        "Function_16_1068",        # 10, 16
        "Function_17_10BB",        # 11, 17
        "Function_18_1182",        # 12, 18
        "Function_19_1279",        # 13, 19
        "Function_20_12AF",        # 14, 20
        "Function_21_130F",        # 15, 21
        "Function_22_209C",        # 16, 22
        "Function_23_2661",        # 17, 23
        "Function_24_2F20",        # 18, 24
        "Function_25_33C7",        # 19, 25
        "Function_26_3BF5",        # 1A, 26
        "Function_27_3C81",        # 1B, 27
        "Function_28_45C1",        # 1C, 28
        "Function_29_46D7",        # 1D, 29
        "Function_30_47D3",        # 1E, 30
        "Function_31_487C",        # 1F, 31
        "Function_32_55F1",        # 20, 32
        "Function_33_5608",        # 21, 33
    )


    def Function_0_3CA(): pass

    label("Function_0_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_3EA")
    SetChrPos(0xE, 3200, 5000, -4800, 90)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_530")

    label("loc_3EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_END)), "loc_411")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_411")

    Jump("loc_530")

    label("loc_414")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_428"),
        (103, "loc_428"),
        (104, "loc_428"),
        (SWITCH_DEFAULT, "loc_436"),
    )


    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_433")

    label("loc_433")

    Jump("loc_436")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_4B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_45D")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3200, 5000, -3870, 180)
    Jump("loc_473")

    label("loc_45D")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3200, 5000, -3870, 270)

    label("loc_473")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, 3200, 5000, -5220, 0)
    SetChrPos(0xB, 3860, 6000, -4520, 270)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_530")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 3)), scpexpr(EXPR_END)), "loc_530")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x11, -1700, 5000, -3890, 0)
    SetChrPos(0x12, -2750, 5000, -1370, 225)
    SetChrPos(0x13, -2410, 5000, -6360, 45)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 7)), scpexpr(EXPR_END)), "loc_530")
    SetChrPos(0xB, 3730, 6000, -5280, 270)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    ClearChrFlags(0xB, 0x80)

    label("loc_530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_541")
    OP_A3(0x10F3)
    Event(0, 30)
    Jump("loc_587")

    label("loc_541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_552")
    OP_A3(0x10F2)
    Event(0, 29)
    Jump("loc_587")

    label("loc_552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_563")
    OP_A3(0x10F1)
    Event(0, 28)
    Jump("loc_587")

    label("loc_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_572")
    Event(0, 21)
    Jump("loc_587")

    label("loc_572")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_587")
    Event(0, 27)

    label("loc_587")

    Return()

    # Function_0_3CA end

    def Function_1_588(): pass

    label("Function_1_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_599")
    OP_22(0x79, 0x1, 0x46)
    OP_22(0x1C3, 0x0, 0x64)

    label("loc_599")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F1")
    Call(0, 32)

    label("loc_5F1")

    Return()

    # Function_1_588 end

    def Function_2_5F2(): pass

    label("Function_2_5F2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_617")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_759")

    label("loc_617")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_630")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_759")

    label("loc_630")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_649")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_759")

    label("loc_649")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_662")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_759")

    label("loc_662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67B")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_759")

    label("loc_67B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_694")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_759")

    label("loc_694")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AD")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_759")

    label("loc_6AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C6")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_759")

    label("loc_6C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DF")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_759")

    label("loc_6DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F8")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_759")

    label("loc_6F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_711")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_759")

    label("loc_711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72A")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_759")

    label("loc_72A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_743")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_759")

    label("loc_743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_759")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_759")

    label("loc_76E")

    Return()

    # Function_2_5F2 end

    def Function_3_76F(): pass

    label("Function_3_76F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_792")
    OP_8D(0xFE, -2000, -5830, 320, -2950, 2000)
    Jump("Function_3_76F")

    label("loc_792")

    Return()

    # Function_3_76F end

    def Function_4_793(): pass

    label("Function_4_793")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B6")
    OP_8D(0xFE, -2220, -2440, -3190, -5300, 2000)
    Jump("Function_4_793")

    label("loc_7B6")

    Return()

    # Function_4_793 end

    def Function_5_7B7(): pass

    label("Function_5_7B7")


    def lambda_7BD():

        label("loc_7BD")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_7BD")

    QueueWorkItem2(0x13, 1, lambda_7BD)

    label("loc_7C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7C8")

    label("loc_7DD")

    Return()

    # Function_5_7B7 end

    def Function_6_7DE(): pass

    label("Function_6_7DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8B0")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_814")
    SetChrSubChip(0xFE, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrSubChip(0xFE, 2)
    Jump("loc_82D")

    label("loc_814")

    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)

    label("loc_82D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_83A")
    OP_A3(0xA)
    Jump("loc_876")

    label("loc_83A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_876")
    Sleep(80)
    SetChrSubChip(0xFE, 3)
    Sleep(100)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(100)
    SetChrSubChip(0xFE, 2)
    OP_A2(0xA)

    label("loc_876")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_899")
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    Jump("loc_8AD")

    label("loc_899")

    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)

    label("loc_8AD")

    Jump("Function_6_7DE")

    label("loc_8B0")

    Return()

    # Function_6_7DE end

    def Function_7_8B1(): pass

    label("Function_7_8B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_A9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 0)), scpexpr(EXPR_END)), "loc_A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AD")
    TalkBegin(0xA)
    OP_4A(0xA, 255)
    OP_A2(0x0)

    ChrTalk(    #0
        0xA,
        (
            "#542F其实那派对的事情\x01",
            "利贝尔通讯发了报道……\x02\x03",

            "自那之后，从社交界到市民，\x01",
            "尤莉亚小姐的倾慕者都急速增加了。\x02\x03",

            "#045F不过这么多的男人围着一个女人\x01",
            "不觉得有些可怜吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#1015F嗯～难道不是自作自受吗？\x02",
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    TalkEnd(0xA)
    Jump("loc_A2A")

    label("loc_9AD")

    TalkBegin(0xA)
    OP_4A(0xA, 255)

    ChrTalk(    #2
        0xA,
        (
            "#542F其实那派对的事情\x01",
            "利贝尔通讯发了报道……\x02\x03",

            "自那之后，从社交界到市民，\x01",
            "尤莉亚小姐的倾慕者都急速增加了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    TalkEnd(0xA)

    label("loc_A2A")

    Jump("loc_A31")

    label("loc_A2D")

    Call(0, 25)

    label("loc_A31")

    Jump("loc_A9B")

    label("loc_A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 5)), scpexpr(EXPR_END)), "loc_A97")
    TalkBegin(0xA)
    OP_4A(0xA, 255)

    ChrTalk(    #3
        0xA,
        (
            "#048F呵呵，连我也\x01",
            "不由得想给老师他们\x01",
            "写信了。\x02\x03",

            "不知道现在怎样了呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    TalkEnd(0xA)
    Jump("loc_A9B")

    label("loc_A97")

    Call(0, 23)

    label("loc_A9B")

    Jump("loc_AAA")

    label("loc_A9E")

    OP_4A(0xA, 255)
    Call(0, 22)
    OP_4B(0xA, 255)

    label("loc_AAA")

    Return()

    # Function_7_8B1 end

    def Function_8_AAB(): pass

    label("Function_8_AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 0)), scpexpr(EXPR_END)), "loc_C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8C")
    TalkBegin(0xC)
    OP_43(0xC, 0x0, 0x0, 0x6)
    OP_A2(0x1)

    ChrTalk(    #4
        0xC,
        (
            "#034F嘿嘿，不愧是王室亲卫队里\x01",
            "倍受称誉的女骑士……\x02\x03",

            "#032F但是，我热情的火焰\x01",
            "绝不会就此熄灭！\x02\x03",

            "#530F实在不行的话，\x01",
            "就全裸弹奏鲁特琴\x01",
            "歌唱出对她的爱意吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1019F呜唔……可以想象。\x02",
    )

    CloseMessageWindow()
    OP_4B(0xC, 255)
    TalkEnd(0xC)
    Jump("loc_C36")

    label("loc_B8C")

    TalkBegin(0xC)
    OP_43(0xC, 0x0, 0x0, 0x6)

    ChrTalk(    #6
        0xC,
        (
            "#034F嘿嘿，不愧是王室亲卫队里\x01",
            "倍受称誉的女骑士……\x02\x03",

            "#032F但是，我热情的火焰\x01",
            "绝不会就此熄灭！\x02\x03",

            "实在不行的话，\x01",
            "#530F就全裸弹奏鲁特琴\x01",
            "歌唱出对她的爱意吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)

    label("loc_C36")

    Jump("loc_C3D")

    label("loc_C39")

    Call(0, 25)

    label("loc_C3D")

    SetChrChipByIndex(0xC, 17)
    SetChrSubChip(0xC, 0)
    OP_4B(0xC, 255)
    Return()

    # Function_8_AAB end

    def Function_9_C4C(): pass

    label("Function_9_C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 5)), scpexpr(EXPR_END)), "loc_CE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 6)), scpexpr(EXPR_END)), "loc_CE1")
    TalkBegin(0xD)
    OP_4A(0xD, 255)

    ChrTalk(    #7
        0xD,
        (
            "#061F说到这个，之前在王都\x01",
            "第一次看到埃尔赛尤号的时候,\x01",
            "感觉真是一艘好漂亮的飞船呢。\x02\x03",

            "嘿嘿……不知道还能再见到吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xD, 255)
    TalkEnd(0xD)
    Jump("loc_CE5")

    label("loc_CE1")

    Call(0, 24)

    label("loc_CE5")

    Jump("loc_CEC")

    label("loc_CE8")

    Call(0, 23)

    label("loc_CEC")

    Return()

    # Function_9_C4C end

    def Function_10_CED(): pass

    label("Function_10_CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_D45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D03")
    Call(0, 31)
    Jump("loc_D45")

    label("loc_D03")

    TalkBegin(0xE)

    ChrTalk(    #8
        0xE,
        (
            "#027F我再稍微\x01",
            "吹吹风就回座位。\x02\x03",

            "你也要在着陆前回去哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)

    label("loc_D45")

    Return()

    # Function_10_CED end

    def Function_11_D46(): pass

    label("Function_11_D46")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_D8C")

    ChrTalk(    #9
        0xFE,
        "哇～是白隼耶。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "好酷～\x01",
            "是那位姐姐的宠物吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xFE, 255)
    Jump("loc_DC3")

    label("loc_D8C")


    ChrTalk(    #11
        0xFE,
        (
            "听说蔡斯\x01",
            "有个会自己动的楼梯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "好想乘乘看啊～\x02",
    )

    CloseMessageWindow()

    label("loc_DC3")

    TalkEnd(0x11)
    Return()

    # Function_11_D46 end

    def Function_12_DC7(): pass

    label("Function_12_DC7")

    TalkBegin(0x12)

    ChrTalk(    #13
        0xFE,
        (
            "比起会动的楼梯，\x01",
            "温泉更好！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "听说是很大很大\x01",
            "的澡堂哦～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_12_DC7 end

    def Function_13_E10(): pass

    label("Function_13_E10")

    TalkBegin(0x13)

    ChrTalk(    #15
        0xFE,
        (
            "喂喂，\x01",
            "不要那样动来动去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "这样会给其它乘客添麻烦的，知道吗？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_13_E10 end

    def Function_14_E5E(): pass

    label("Function_14_E5E")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_F0C")

    ChrTalk(    #17
        0xFE,
        (
            "哼哼，别看我这个样子，\x01",
            "我可是个军事迷哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "我喜欢的战车是帝国陆军用的\x01",
            "莱恩福尔特ＬＰ－Ⅲ初期型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "和百日战役当时的后期型相比\x01",
            "优点在于它耗油量更小。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F65")

    label("loc_F0C")


    ChrTalk(    #20
        0xFE,
        (
            "嗯～可惜……\x01",
            "看不到雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "果然那附近的空域\x01",
            "好像连定期船也不能接近呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_F65")

    TalkEnd(0x14)
    Return()

    # Function_14_E5E end

    def Function_15_F69(): pass

    label("Function_15_F69")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_FD4")

    ChrTalk(    #22
        0xFE,
        (
            "我正要去柏斯的哈肯大门\x01",
            "参观呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "虽然也想顺路去趟洛连特\x01",
            "不过还是想先看看哈肯大门啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1064")

    label("loc_FD4")


    ChrTalk(    #24
        0xFE,
        (
            "我正要去柏斯的哈肯大门\x01",
            "参观呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "在百日战役相关的历史遗迹中，\x01",
            "这里可以说是最重要的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "我打算花足够的时间\x01",
            "仔仔细细看个够。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1064")

    TalkEnd(0x15)
    Return()

    # Function_15_F69 end

    def Function_16_1068(): pass

    label("Function_16_1068")

    TalkBegin(0x16)

    ChrTalk(    #27
        0xFE,
        (
            "到了哈肯大门\x01",
            "要拍很多照片哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "早就想拍一次\x01",
            "那么有魄力的建筑物了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    # Function_16_1068 end

    def Function_17_10BB(): pass

    label("Function_17_10BB")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1110")

    ChrTalk(    #29
        0xFE,
        (
            "我可不是在王都\x01",
            "默默无闻的我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "在某个地方，\x01",
            "一定有人需要我！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117E")

    label("loc_1110")


    ChrTalk(    #31
        0xFE,
        (
            "我可不是在王都\x01",
            "默默无闻的我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "今后要积极地\x01",
            "向周边地区发展。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "在某个地方，\x01",
            "一定有人需要我！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_117E")

    TalkEnd(0x17)
    Return()

    # Function_17_10BB end

    def Function_18_1182(): pass

    label("Function_18_1182")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_11E3")

    ChrTalk(    #34
        0xFE,
        (
            "安敦那家伙\x01",
            "突然说要去柏斯呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "他就是这样一个人，\x01",
            "所以我也跟着来看看情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1275")

    label("loc_11E3")


    ChrTalk(    #36
        0xFE,
        (
            "安敦那家伙\x01",
            "突然说要去柏斯呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "他就是这样一个人，\x01",
            "所以我也跟着来看看情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "嗯，虽然不知道会变成怎样，\x01",
            "就先悠闲地参观一下城市吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_1275")

    TalkEnd(0x18)
    Return()

    # Function_18_1182 end

    def Function_19_1279(): pass

    label("Function_19_1279")

    TalkBegin(0x19)

    ChrTalk(    #39
        0xFE,
        (
            "啊～可以的话真想\x01",
            "再好好享受一下温泉啊……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_19_1279 end

    def Function_20_12AF(): pass

    label("Function_20_12AF")

    TalkBegin(0x1A)

    ChrTalk(    #40
        0xFE,
        (
            "速度就是生命,\x01",
            "杂志记者真是永不能停歇啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "刚回来就马上要写 \x01",
            "关于地震的报告了。 \x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1A)
    Return()

    # Function_20_12AF end

    def Function_21_130F(): pass

    label("Function_21_130F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_23(0x79)
    OP_23(0x1C3)
    OP_D2(0x260157, 0x26015C, 0x16)
    LoadEffect(0x0, "map\\\\mp044_00.eff")
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        (
            "\x07\x05我的艾丝蒂尔……\x01",
            "如太阳般耀眼的你。\x02\x03",

            "和你在一起的时光虽然幸福\x01",
            "但同时，也非常痛苦……\x02\x03",

            "就像明亮的光芒会投下浓重的阴影……\x02\x03",

            "与你在一起相处得越久\x01",
            "我，也对自己令人憎恶的本性\x01",
            "认识得更加深刻……\x02\x03",

            "所以，我甚至曾经想过，\x01",
            "要是当初没遇见你该多好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrPos(0x101, 2660, 5000, -4840, 92)
    OP_6D(-3180, 3500, 2710, 0)
    OP_67(0, 4270, -10000, 0)
    OP_6B(12000, 0)
    OP_6C(149000, 0)
    OP_6E(262, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x79, 0x1, 0x46)
    OP_22(0x1C3, 0x0, 0x64)
    OP_C8(0x200, 0x46, "C_PLAC07._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_14CE():
        OP_6D(3190, 5000, -4610, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14CE)

    def lambda_14E6():
        OP_67(0, 8000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14E6)
    Sleep(4000)

    def lambda_1503():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1503)

    def lambda_1513():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1513)

    def lambda_1523():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1523)
    Sleep(6000)
    SetChrPos(0x8, -3160, 5000, -1280, 267)
    ClearChrFlags(0x8, 0x8)

    ChrTalk(    #43
        0x101,
        (
            "#588F………………………………\x02\x03",

            "我……\x01",
            "伤害了约修亚吗？\x02\x03",

            "竟然说没遇见我该有多好……\x02\x03",

            "……我……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #44
        0x8,
        "青年的声音",
        "#2P不行，不行啊～\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x8, -2960, 5000, 1050, 177)
    ClearChrFlags(0x8, 0x80)
    Sleep(500)

    def lambda_160B():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_160B)

    def lambda_1619():
        OP_6D(1780, 5000, -4750, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1619)

    def lambda_1631():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1631)

    def lambda_1649():
        OP_6C(314000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1649)
    Sleep(1000)

    def lambda_165E():
        OP_8E(0x8, 0xFFFFF7A4, 0x1388, 0xFFFFFB96, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_165E)
    WaitChrThread(0x8, 0x0)

    def lambda_167E():
        OP_8E(0x8, 0xFFFFFCC2, 0x1388, 0xFFFFF128, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_167E)
    OP_8C(0x101, 273, 500)
    WaitChrThread(0x8, 0x0)
    OP_8C(0x8, 80, 1000)

    ChrTalk(    #45
        0x101,
        "#4P#587F……？\x02",
    )

    CloseMessageWindow()

    def lambda_16C0():
        OP_8E(0x8, 0x28A, 0x1388, 0xFFFFEF0C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_16C0)
    WaitChrThread(0x8, 0x0)

    NpcTalk(    #46
        0x8,
        "外表轻浮的青年",
        (
            "#1061F#5P晴空万里的蓝天！\x02\x03",

            "还有，微风轻拂的面庞！\x02\x03",

            "#1060F此情此景，像你这般可爱的女孩，\x01",
            "却一副失魂落魄的表情……这可不行啊。\x02\x03",

            "连女神也会黯然神伤的哦，真的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#4P#587F唔……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #48
        0x8,
        "外表轻浮的青年",
        (
            "#1064F#5P啊，怎么了？\x01",
            "我绝对不是可疑人物哦～\x02\x03",

            "#1065F只不过刚一上船\x01",
            "我就注意到你了。\x02\x03",

            "#1062F看你好像没精打采的样子，\x01",
            "就想用我的连珠妙语让你重展笑颜。\x01",
            "呵呵，仅此而已啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#4P#004F……………………………\x02\x03",

            "#587F嗯……\x01",
            "虽然不知道你是谁，不过，谢谢你。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #50
        0x8,
        "外表轻浮的青年",
        (
            "#1061F#5P不过说白了，\x01",
            "其实，只是搭讪而已啦。\x02\x03",

            "#1060F怎样，不介意的话，\x01",
            "一起到下面的展望室逛逛吧？\x02\x03",

            "那里可以点饮料喝，\x01",
            "让我请客怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#4P#587F啊…那、那个……\x01",
            "你的好意我心领了……\x02\x03",

            "不过我没什么心情……\x02\x03",

            "#003F……对不起……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #52
        0x8,
        "外表轻浮的青年",
        (
            "#1065F#5P嗯～这样啊。\x02\x03",

            "#1060F那么，搭讪就到此为止，\x01",
            "看来还是转回我的本职工作比较好。\x02\x03",

            "毕竟引导迷途羔羊也是我的工作嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#4P#004F本职工作……？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #54
        0x8,
        "外表轻浮的青年",
        "#1071F#5P呵呵，看这个。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x8, 22)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_22(0xD8, 0x0, 0x64)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    PlayEffect(0x0, 0x0, 0x8, 0, 550, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x80, 0x0, 0x64)
    OP_83(0x0, 0x2)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #55
        (
            "\x07\x05外表轻浮的青年\x01",
            "露出佩戴在腰间且刻有杯子图案的吊坠。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #56
        0x101,
        (
            "#4P#004F咦，这个……\x02\x03",

            "记得是七耀教会的……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(200)

    NpcTalk(    #57
        0x8,
        "外表轻浮的青年",
        (
            "#1060F#5P答对了。\x01",
            "是『星杯纹章』。\x02\x03",

            "我叫凯文·格拉汉姆。\x01",
            "别看我这样，我也是七耀教会的神父呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#4P#501F哦～是这样啊。\x02\x03",

            "#505F……这，是开玩笑的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "#1061F#5P怎么会？\x01",
            "我可是相当严肃认真的神父啊。\x02\x03",

            "一天三次的礼拜从来没少过，\x01",
            "你看，连圣典也是寸步不离地带着……\x02\x03",

            "#1062F………………………………………\x02\x03",

            "#1068F抱歉，我忘在座位上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#4P#007F……真是毫无说服力啊。\x02\x03",

            "#586F呵呵……\x01",
            "真是奇怪的大哥哥啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "#1061F#5P啊！刚才你笑了一下吧？\x02\x03",

            "#1061F嗯嗯。\x01",
            "对嘛～可爱的女孩子就是要保持笑容才行啊。\x02\x03",

            "#1060F嗯，总之就是这样，\x01",
            "方便的话，让我以神父的身份倾听你的心声吧。\x02\x03",

            "这绝不是搭讪，我向空之女神发誓。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#4P#586F啊……嗯……\x02\x03",

            "可、可是…\x01",
            "要怎样说才好……\x02\x03",

            "#587F我……\x02\x03",

            "#003F……呜…………………\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 16)
    SetChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 1)
    OP_0D()
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #63
        0x8,
        (
            "#1064F#5P哎，慢着慢着……\x02\x03",

            "虽然不知道是怎么回事！\x01",
            "抱歉，是我不好！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#4P#588F呜，哎……\x02\x03",

            "呜呜呜呜……啊啊啊啊啊……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 15)
    SetChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 1)
    Sleep(500)

    ChrTalk(    #65
        0x101,
        "#4P#589F#4S呜哇啊啊啊啊啊啊啊……！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        "#1068F#5P啊～……\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x640, 0x1388, 0xFFFFEBB0, 0x3E8, 0x0)
    TurnDirection(0x8, 0x101, 400)
    Fade(500)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 5)
    OP_0D()
    OP_1D(0x1)
    SetMapFlags(0x2000000)
    Sleep(500)

    ChrTalk(    #67
        0x8,
        (
            "#1060F#5P好了好了，乖孩子。\x01",
            "你一直强忍到现在啊。\x02\x03",

            "尽情地哭到你觉得好受为止吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #68
        0x101,
        (
            "#4P#589F#4S呜啊啊啊啊……！#2S\x02\x03",

            "#4S呜哇啊啊啊啊啊啊啊啊……！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_206A():
        OP_6D(-1960, 5000, 16820, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_206A)
    FadeToDark(5000, 0, -1)
    OP_0D()
    OP_23(0x79)
    OP_23(0x1C3)
    Sleep(2000)
    NewScene("ED6_DT21/E0011   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_130F end

    def Function_22_209C(): pass

    label("Function_22_209C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2611")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(3240, 5000, -4260, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 3200, 5000, -3800, 180)
    TurnDirection(0xA, 0x101, 0)
    OP_0D()

    ChrTalk(    #69
        0xA,
        (
            "#040F艾丝蒂尔。\x02\x03",

            "难道你是\x01",
            "在船内散步吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1016F#5P嘿嘿，算是吧。\x02\x03",

            "#1011F说起来科洛丝\x01",
            "平时怎样回王都的呢？\x02\x03",

            "让亲卫队的人接送吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#045F呵呵，怎么会。\x01",
            "我是搭定期船回去的哦。\x02\x03",

            "#040F新年的仪式，还有女王诞辰庆典。\x01",
            "每年都回王都两次呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1006F#5P那你经常\x01",
            "搭乘定期船啊。\x02\x03",

            "#1015F啊，这样的话……\x01",
            "基库怎么办呢？\x02\x03",

            "在科洛丝之后\x01",
            "悠闲地飞来王都？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        "#542F啊，基库的话……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xB, 15000, 8000, -4760, 270)
    ClearChrFlags(0xB, 0x80)
    TurnDirection(0xA, 0xB, 400)

    def lambda_229F():

        label("loc_229F")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_229F")

    QueueWorkItem2(0xA, 1, lambda_229F)
    Sleep(500)

    ChrTalk(    #74
        0xA,
        "#040F#6P基库，过来！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1004F#5P咦……\x02",
    )

    CloseMessageWindow()
    OP_22(0x8C, 0x0, 0x64)
    OP_22(0x197, 0x0, 0x64)

    def lambda_22EE():
        OP_6D(10210, 5000, -3880, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22EE)

    def lambda_2306():
        OP_67(0, 6500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2306)

    def lambda_231E():
        OP_6C(55000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_231E)
    WaitChrThread(0x101, 0x1)
    OP_4A(0x11, 255)

    def lambda_2337():
        TurnDirection(0x11, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2337)
    OP_A2(0x9)

    def lambda_2348():
        OP_6D(4360, 5000, -4030, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2348)
    ClearChrFlags(0xB, 0x1)
    OP_8F(0xB, 0xE92, 0x1770, 0xFFFFEB60, 0x1388, 0x0)
    SetChrFlags(0xB, 0x1)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 3)
    Sleep(100)
    SetChrSubChip(0xB, 4)
    Sleep(100)
    SetChrSubChip(0xB, 0)
    OP_44(0xA, 0x1)
    OP_8C(0xA, 90, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #76
        0x101,
        "#1004F#5P哎哎！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #77
        0xB,
        "#310F啾？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        (
            "#542F#6P呵呵，抱歉哦。\x01",
            "只是叫你来一下而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1008F#5P吓，吓我一跳……\x02\x03",

            "基库居然\x01",
            "跟着这艘船飞过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xB,
        "#311F啾⊙\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #81
        0xA,
        (
            "#041F#4P基库可以以时速１８００塞尔矩\x01",
            "进行水平飞行。\x02\x03",

            "这艘定期船的时速\x01",
            "差不多也就９００塞尔矩……\x02\x03",

            "对基库来说\x01",
            "一路跟过来的感觉\x01",
            "可能就跟散步差不多吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1011F#5P这样啊……\x02\x03",

            "#1016F越来越感觉这小家伙\x01",
            "不是一般地厉害了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        "#311F啾～㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        (
            "#048F#4P基库会帮忙进行\x01",
            "亲卫队的传令工作，\x01",
            "也是因为它有这样的速度。\x02\x03",

            "不能使用导力通信的时候，\x01",
            "没有什么东西\x01",
            "能比基库更快地传递情报了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1006F#5P原来如此……\x01",
            "逮捕市长的时候也是这样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1407)
    EventEnd(0x0)
    Jump("loc_2660")

    label("loc_2611")

    TalkBegin(0xA)

    ChrTalk(    #86
        0xA,
        (
            "#047F这风好舒服啊……\x02\x03",

            "#048F看这情况，蔡斯地区\x01",
            "说不定也是好天气呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)

    label("loc_2660")

    Return()

    # Function_22_209C end

    def Function_23_2661(): pass

    label("Function_23_2661")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4A(0xA, 255)
    OP_4A(0xD, 255)
    OP_6D(2940, 5000, -4240, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(49000, 0)
    OP_6E(258, 0)
    SetChrPos(0x101, 1300, 5000, -4640, 109)
    TurnDirection(0xA, 0x101, 0)
    TurnDirection(0xD, 0x101, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #87
        0xD,
        "#061F啊，姐姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xB,
        "#311F#2P啾！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "#040F#2P艾丝蒂尔。\x01",
            "又出来散步吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1006F#6P嗯，算是吧。\x02\x03",

            "科洛丝你们已经\x01",
            "开始增进感情了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        "#048F#2P呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xD,
        (
            "#560F嘿嘿，我和基库\x01",
            "也很熟了哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #93
        0xD,
        "#061F对吧，基库⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xB,
        "#311F#2P啾～㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#1001F#6P啊哈哈，那太好了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #96
        0xD,
        (
            "#060F啊，另外科洛丝姐姐\x01",
            "还告诉我学院祭的事情。\x02\x03",

            "姐姐你们\x01",
            "在戏剧里面演骑士对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1008F#6P嘿嘿，是啊。\x02\x03",

            "#1006F别看我们这样，\x01",
            "那骑士装束还大受好评呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        (
            "#560F哇～真好啊。\x02\x03",

            "#561F我也好想看\x01",
            "姐姐们演戏啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xD, 400)

    ChrTalk(    #99
        0xA,
        (
            "#041F呵呵，明年的学院祭\x01",
            "一定要来玩哦。\x02\x03",

            "我们一定热烈欢迎。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #100
        0xD,
        (
            "#560F哇，可以吗？\x02\x03",

            "嗯～那个时候\x01",
            "爸爸他们也回来了……\x02\x03",

            "#061F跟爷爷商量一下吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #101
        0xA,
        (
            "#048F#2P呵呵，不过这样一来……\x02\x03",

            "明年也要拜托艾丝蒂尔你们\x01",
            "来演出才行呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29D6():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_29D6)

    ChrTalk(    #102
        0x101,
        (
            "#1016F#6P要，要再来一次\x01",
            "还是饶了我吧。\x02\x03",

            "#1025F这么说来……\x01",
            "提妲的爸爸妈妈\x01",
            "好像因工作出国去了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xD,
        (
            "#560F嗯……\x02\x03",

            "到导力器还没有普及的国家\x01",
            "去做技术指导了。\x02\x03",

            "已经快两年都没回来了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1015F#6P嗯～还真久啊。\x02\x03",

            "有互通书信吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xD,
        (
            "#061F嗯，一个月一次吧⊙\x02\x03",

            "#060F前不久我写了姐姐们的事，\x01",
            "收到了爸妈的回信……\x02\x03",

            "要我代他们向你们问好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#1016F#6P嘿嘿，是吗。\x02\x03",

            "#1006F话说回来，提妲的父母\x01",
            "是怎样的人呢？\x02\x03",

            "妈妈一定像提妲吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xD,
        (
            "#064F嗯～怎么说呢？\x02\x03",

            "#060F性格很外向，\x01",
            "很有活力的感觉吧。\x02\x03",

            "#061F经常会和爷爷\x01",
            "扭在一起吵个不停呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1004F#6P扭、扭在一起……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xD, 400)

    ChrTalk(    #109
        0xA,
        (
            "#045F呵呵……\x01",
            "真是有活力的妈妈啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #110
        0xD,
        (
            "#067F啊，其实并不是\x01",
            "关系不好。\x02\x03",

            "爸爸说，那也是\x01",
            "父女之间关系好的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1016F#6P是，是吗。\x02\x03",

            "#1011F那么\x01",
            "爸爸是怎样的人？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #112
        0xD,
        (
            "#560F嗯，是个很沉静\x01",
            "又很壮实的人。\x02\x03",

            "听说十多年前\x01",
            "曾经当过游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1004F#6P咦，是这样吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xD,
        (
            "#060F由于受伤退出之后\x01",
            "就改行当设计技师了。\x02\x03",

            "妈妈倒是说过\x01",
            "他以前很有名的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#1006F#6P哦～这样啊。\x02\x03",

            "#1001F嗯～等他们回来之后\x01",
            "真想见见两人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xD,
        (
            "#061F嗯，我也想介绍给姐姐认识，\x01",
            "等他们回来以后记得来玩哦⊙\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #117
        0xD,
        (
            "#560F科洛丝姐姐到时候\x01",
            "也一定要来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        "#041F好，我很乐意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xB,
        "#310F#2P啾啾！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #120
        0xD,
        (
            "#061F啊，当然\x01",
            "基库也要一起来哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xB,
        "#311F#2P啾～㈱\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(1300, 5000, -4640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TurnDirection(0xA, 0xD, 0)
    TurnDirection(0xD, 0xA, 0)
    OP_4B(0xA, 255)
    OP_4B(0xD, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x1605)
    EventEnd(0x0)
    Return()

    # Function_23_2661 end

    def Function_24_2F20(): pass

    label("Function_24_2F20")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4A(0xA, 255)
    OP_4A(0xD, 255)
    OP_6D(2940, 5000, -4240, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(49000, 0)
    OP_6E(258, 0)
    SetChrPos(0x101, 1300, 5000, -4640, 109)
    TurnDirection(0xA, 0x101, 0)
    TurnDirection(0xD, 0x101, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #122
        0xD,
        (
            "#560F对了姐姐。\x02\x03",

            "你知道这甲板上的风\x01",
            "为什么会这么平静吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        (
            "#1004F#6P因为风本来就很平静……\x01",
            "是这样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xD,
        (
            "#060F不是。\x01",
            "其实这个速度和高度\x01",
            "应该会引起很大的风的。\x02\x03",

            "不要说聊天了,\x01",
            "连站都会站不稳的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        "#1015F#6P是，是这样吗……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xD, 400)

    ChrTalk(    #126
        0xA,
        (
            "#040F也就是说，有什么装置\x01",
            "可以克服这一点吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #127
        0xD,
        (
            "#560F是的，这就是让飞船浮上天空的\x01",
            "『飞翔引擎』它另外的作用。\x02\x03",

            "#061F这个机关运转的时候，\x01",
            "反重力的力场\x01",
            "会覆盖整艘飞船……\x02\x03",

            "据说这个力场同时也会\x01",
            "缓和风与惯性的影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#1019F#6P（……科洛丝，你懂吗？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xA,
        "#045F（一半一半……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #130
        0xD,
        (
            "#060F不过，要启动飞翔引擎\x01",
            "需要大量的导力……\x02\x03",

            "为此就需要\x01",
            "高输出功率的『导力引擎』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        (
            "#1006F#6P原来如此……\x02\x03",

            "决定飞船性能的就是引擎，\x01",
            "原来指的是这个意思啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xA,
        (
            "#040F这么说来……\x02\x03",

            "这次，开发给埃尔赛尤号\x01",
            "使用的新型引擎，\x01",
            "性能似乎相当厉害吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #133
        0xD,
        (
            "#061F是的，我看了性能表，\x01",
            "感觉和以前真的有天壤之别。\x02\x03",

            "我想这都是多亏了开发小组和\x01",
            "维修班各位的努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xA,
        (
            "#048F这样啊……\x01",
            "尤莉亚小姐也会很高兴吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(1300, 5000, -4640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TurnDirection(0xA, 0xD, 0)
    TurnDirection(0xD, 0xA, 0)
    OP_4B(0xA, 255)
    OP_4B(0xD, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x1606)
    EventEnd(0x0)
    Return()

    # Function_24_2F20 end

    def Function_25_33C7(): pass

    label("Function_25_33C7")

    EventBegin(0x0)
    OP_20(0x3E8)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    SetChrChipByIndex(0xC, 18)
    SetChrSubChip(0xC, 0)
    SetChrFlags(0xC, 0x20)
    OP_6D(2940, 5000, -4240, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(49000, 0)
    OP_6E(258, 0)
    SetChrPos(0x101, 1300, 5000, -4640, 109)
    TurnDirection(0xA, 0x101, 0)
    TurnDirection(0xC, 0x101, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #135
        0xC,
        (
            "#031F呀，艾丝蒂尔。\x02\x03",

            "欢迎来到我奥利维尔·朗海姆的\x01",
            "独奏会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#1007F#6P你在装模作样些什么。\x02\x03",

            "#1019F科洛丝也不必特地\x01",
            "来捧场嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xA,
        (
            "#045F#2P呵呵，来到甲板上\x01",
            "就听到演奏\x01",
            "于是擅自欣赏起来了。\x02\x03",

            "#048F真是非常精彩。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)
    Sleep(500)

    ChrTalk(    #138
        0xC,
        (
            "#035F呼……\x01",
            "得您称誉实在是光荣至极。\x02\x03",

            "#037F如何，殿下。\x01",
            "到达王都之前请务必和我\x01",
            "单独畅谈一下音乐理念……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xB,
        "#310F#2P啾～？（瞪）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xC,
        "#033F啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 400)

    def lambda_35E5():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_35E5)

    ChrTalk(    #141
        0xC,
        (
            "#036F#6P嗯，基库。\x01",
            "这叫做社交辞令……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xA,
        "#040F哎呀，原来是社交辞令吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #143
        0xC,
        (
            "#035F呼，当然\x01",
            "如果找到空隙就可以用各种手段\x01",
            "把您弄到手……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        "#310F#3S#2P啾！！\x02",
    )

    CloseMessageWindow()
    OP_22(0x197, 0x0, 0x64)
    OP_22(0x8C, 0x1, 0x64)
    SetChrSubChip(0xB, 0)
    Sleep(100)
    SetChrSubChip(0xB, 4)
    Sleep(100)
    SetChrSubChip(0xB, 3)
    Sleep(100)
    SetChrChipByIndex(0xB, 2)
    OP_A2(0x2)
    OP_43(0xB, 0x1, 0x0, 0x1A)
    Sleep(500)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_8C(0xC, 90, 400)
    Sleep(400)
    OP_8C(0xC, 0, 400)

    ChrTalk(    #145
        0xC,
        (
            "#036F哇哇……\x01",
            "住手啊基库！\x02\x03",

            "对不起！\x01",
            "都是我不好！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1001F#6P啊哈哈，基库\x01",
            "真是个称职的护卫嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x2)
    OP_A6(0x3)
    OP_8E(0xB, 0xF14, 0x1770, 0xFFFFEE58, 0x5DC, 0x0)
    OP_8C(0xB, 275, 0)
    OP_23(0x8C)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 3)
    Sleep(100)
    SetChrSubChip(0xB, 4)
    Sleep(100)
    SetChrSubChip(0xB, 0)
    Sleep(100)
    OP_63(0xC)
    Sleep(500)
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #147
        0xC,
        (
            "#034F哈哈哈哈……\x01",
            "吃，吃苦头了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xA,
        (
            "#041F呵呵……\x01",
            "不好意思，奥利维尔。\x02\x03",

            "#542F不过，刚才那样\x01",
            "也是基库的爱情表现。\x02\x03",

            "它在跟奥利维尔\x01",
            "开玩笑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xB,
        "#311F#2P啾～㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #150
        0xC,
        (
            "#035F哎呀呀，这真是光荣之至。\x02\x03",

            "#030F不过，和利贝尔一样\x01",
            "看来殿下的防守真是坚固啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xA,
        (
            "#048F呵呵……\x01",
            "那也要视对象而定啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1007F#6P真是个随便的家伙……\x02\x03",

            "#1019F你啊，到了王都后\x01",
            "可要克制一点哦。\x02\x03",

            "尤莉亚小姐她们几位\x01",
            "可不是喜欢开玩笑的人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #153
        0xC,
        (
            "#033F哦哦，那位威风凛凛的女士吗。\x02\x03",

            "#030F那种有男子汉气概\x01",
            "威风凛凛的女性也令人憧憬呢。\x02\x03",

            "#031F呼，如果有机会\x01",
            "还真想亲近亲近……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xA,
        "#049F………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #155
        0xC,
        "#033F哎、哎呀？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #156
        0x101,
        "#1004F#6P怎么了，科洛丝？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        (
            "#043F那个，或许对尤莉亚小姐\x01",
            "的确不能开这种玩笑也说不定。\x02\x03",

            "以前在王城的派对上，\x01",
            "有人喝醉了酒\x01",
            "跑来纠缠我……\x02\x03",

            "尤莉亚小姐\x01",
            "用剑把那个人的衣服……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xC,
        "#036F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        (
            "#1008F#6P唔……\x02\x03",

            "#1013F…………全裸？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(500)

    ChrTalk(    #160
        0xA,
        "#540F#2P（咽口水）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x3,
        "#036F（浑身打冷战……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(1300, 5000, -4640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_8C(0xA, 0, 0)
    OP_8C(0xC, 270, 0)
    OP_4B(0xA, 255)
    ClearChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 17)
    SetChrSubChip(0xC, 0)
    OP_4B(0xC, 255)
    OP_1D(0x49)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x1608)
    EventEnd(0x0)
    Return()

    # Function_25_33C7 end

    def Function_26_3BF5(): pass

    label("Function_26_3BF5")

    OP_8E(0xB, 0xFDB, 0x157C, 0xFFFFF164, 0x1F40, 0x0)

    label("loc_3C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3C29")
    OP_97(0xB, 0xCBC, 0xFFFFF0E2, 0xFFFD40E0, 0x1F40, 0x1)
    OP_48()
    Jump("loc_3C09")

    label("loc_3C29")

    OP_97(0xB, 0xCBC, 0xFFFFF0E2, 0xFFFD40E0, 0x1770, 0x1)
    OP_97(0xB, 0xCBC, 0xFFFFF0E2, 0xFFFD40E0, 0xFA0, 0x1)
    OP_97(0xB, 0xCBC, 0xFFFFF0E2, 0xFFFEEE90, 0xBB8, 0x1)
    OP_97(0xB, 0xCBC, 0xFFFFF0E2, 0xFFFF8AD0, 0x7D0, 0x1)
    OP_A2(0x3)
    Return()

    # Function_26_3BF5 end

    def Function_27_3C81(): pass

    label("Function_27_3C81")

    EventBegin(0x0)
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    OP_6D(860, 5000, 20310, 0)
    OP_67(0, 7530, -10000, 0)
    OP_6B(5380, 0)
    OP_6C(188000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2890, 5000, -4960, 90)
    SetChrChipByIndex(0x101, 6)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    def lambda_3CFA():
        OP_6D(2520, 5000, -5080, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3CFA)

    def lambda_3D12():
        OP_6C(236000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D12)

    def lambda_3D22():
        OP_67(0, 6570, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D22)

    def lambda_3D3A():
        OP_6B(4380, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3D3A)
    OP_C8(0x200, 0x46, "C_PLAC07._CH", 0x1, 0x7D0)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6B(2860, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #162
        0x101,
        (
            "#1003F……呼……………\x02\x03",

            "#1007F…………哈……………\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_AD(0x240091, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #163
        (
            "#1007F（这个……\x01",
            "  果然是约修亚吧……）\x02\x03",

            "#1025F（还戴着围巾\x01",
            "装～什么酷呢……）\x02\x03",

            "（有没有……\x01",
            "  好好吃饭呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_99(0x101, 0x0, 0x2, 0x3E8)
    Sleep(500)

    ChrTalk(    #164
        0x101,
        (
            "#1003F（约修亚果然\x01",
            "  在利贝尔某处……）\x02\x03",

            "（和空贼们合作\x01",
            "  打算做些什么……）\x02\x03",

            "#1026F（但是……既然这样的话……）\x02\x03",

            "（为什么……\x01",
            "  为什么不找我帮忙？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_AD(0x240111, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #165
        (
            "#1027F（约修亚这笨蛋……）\x02\x03",

            "（竟然做出袭击军事基地\x01",
            "  这么乱来的事……）\x02\x03",

            "（这么冰冷……\x01",
            "  和初遇时一样的眼神……）\x02\x03",

            "（而且……而且……）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrSubChip(0x101, 0)
    OP_AE(0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #166
        0x101,
        (
            "#1014F#3S为什么看起来\x01",
            "跟那男人婆这么要好啊！？\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_4A(0xE, 255)
    SetChrPos(0xE, 3160, 5000, 4910, 180)
    ClearChrFlags(0xE, 0x80)

    NpcTalk(    #167
        0xE,
        "女性的声音",
        "#1P艾丝蒂尔？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #168
        0x101,
        "#1004F呜哎！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_40CD():
        OP_6D(2650, 5000, -880, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40CD)

    def lambda_40E5():
        OP_67(0, 8000, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40E5)

    def lambda_40FD():
        OP_6E(262, 2500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_40FD)

    def lambda_410D():
        OP_6C(315000, 2500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_410D)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0xE, 0x2)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #169
        0x101,
        "#1015F雪拉姐……\x02",
    )

    CloseMessageWindow()

    def lambda_4147():
        OP_6D(2950, 5000, -4260, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4147)
    OP_8E(0xE, 0xB54, 0x1388, 0xFFFFF092, 0x9C4, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #170
        0xE,
        (
            "#021F#2P原来你在这里啊。\x02\x03",

            "#020F突然就不见了\x01",
            "多让人担心啊。\x02\x03",

            "怎么了？\x01",
            "晕船了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#1025F#6P啊，嗯……别担心。\x02\x03",

            "我并不是不舒服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xE,
        "#020F#2P是吗。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 90, 400)
    Sleep(500)

    ChrTalk(    #173
        0xE,
        "#021F#5P呼，今天也是个好天气呢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(500)

    ChrTalk(    #174
        0xE,
        (
            "#026F#5P这样平和的天空下\x01",
            "却有人在\x01",
            "图谋不轨……\x02\x03",

            "#022F真是够蠢的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#1003F#5P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xE,
        (
            "#524F#5P……还有，艾丝蒂尔。\x02\x03",

            "你没有必要把事情一个人憋在心里哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #177
        0x101,
        "#1004F#6P咦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xE,
        (
            "#524F#5P我倒不会问\x01",
            "记者们说了什么……\x02\x03",

            "不过现在的你\x01",
            "还有很多值得依赖的好同伴。\x02\x03",

            "当然，也包括我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        "#1026F#6P………啊………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xE,
        (
            "#026F#5P当然，你要自己\x01",
            "整理好心情也可以。\x02\x03",

            "#020F只是，我想我们所有人\x01",
            "都很愿意帮助你。\x02\x03",

            "这点千万不要忘记了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#1003F#6P雪拉姐，我……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #182
        0xE,
        (
            "#021F#2P呵呵，我要说的就是这些。\x02\x03",

            "#020F到达柏斯之前\x01",
            "虽然还有很多时间……\x02\x03",

            "不过中途在洛连特着陆的时候\x01",
            "可一定要回到座位哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        "#1025F#6P嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 0, 400)

    def lambda_44CC():
        OP_6D(2910, 5000, 2500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_44CC)
    OP_8E(0xE, 0xB18, 0x13EC, 0x1A68, 0x9C4, 0x0)
    OP_8C(0xE, 270, 400)
    OP_72(0x2, 0x10)
    OP_72(0x2, 0x800)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3B)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x2)
    OP_8E(0xE, 0x2D0, 0x13EC, 0x1BC6, 0x9C4, 0x0)
    SetChrFlags(0xE, 0x80)
    OP_6F(0x2, 59)
    OP_70(0x2, 0x0)
    OP_22(0x7, 0x0, 0x64)

    def lambda_454B():
        OP_6D(2780, 5000, -4080, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_454B)
    OP_73(0x2)
    OP_71(0x2, 0x10)
    OP_71(0x2, 0x800)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #184
        0x101,
        (
            "#1007F#5P依赖吗……\x02\x03",

            "#1015F是不是去和大家\x01",
            "稍微谈谈好呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1806)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    OP_D6(0x1)
    Return()

    # Function_27_3C81 end

    def Function_28_45C1(): pass

    label("Function_28_45C1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xF230, 0x0)
    OP_6D(-7500, -5100, -12260, 0)
    OP_67(0, 3000, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(10000, 0)
    OP_6E(300, 0)
    SetChrPos(0x101, -200, 5000, 3170, 86)
    SetChrFlags(0x101, 0x80)
    OP_C8(0x200, 0x46, "C_PLAC07._CH", 0x1, 0x1388)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    def lambda_465A():
        OP_6D(-2580, 5500, -5200, 9000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_465A)

    def lambda_4672():
        OP_67(0, 7240, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4672)

    def lambda_468A():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_468A)

    def lambda_469A():
        OP_6E(505, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_469A)

    def lambda_46AA():
        OP_6B(3200, 8000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_46AA)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x8, 0x0)
    NewScene("ED6_DT21/E0011   ._SN", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_28_45C1 end

    def Function_29_46D7(): pass

    label("Function_29_46D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xF230, 0x0)
    OP_6D(3710, 0, 27280, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3450, 0)
    OP_6C(206000, 0)
    OP_6E(525, 0)
    SetChrPos(0x101, -200, 5000, 3170, 86)
    SetChrFlags(0x101, 0x80)

    def lambda_474C():
        OP_6D(650, 5000, -4910, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_474C)

    def lambda_4764():
        OP_67(0, 8600, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4764)

    def lambda_477C():
        OP_6C(326000, 13000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_477C)

    def lambda_478C():
        OP_6B(3600, 13000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_478C)
    OP_C8(0x200, 0x46, "C_PLAC07._CH", 0x1, 0x7D0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x8, 0x0)
    NewScene("ED6_DT21/E0011   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_29_46D7 end

    def Function_30_47D3(): pass

    label("Function_30_47D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xF230, 0x0)
    OP_6D(-6810, 5000, 32110, 0)
    OP_67(0, 4910, -10000, 0)
    OP_6B(4680, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_C8(0x80, 0x46, "C_PLAC07._CH", 0x1, 0x3E8)
    FadeToBright(1500, 0)

    def lambda_4850():
        OP_6D(1140, 5000, -29550, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4850)
    Sleep(6000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/E0011   ._SN", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_30_47D3 end

    def Function_31_487C(): pass

    label("Function_31_487C")

    EventBegin(0x0)
    OP_4A(0xE, 255)
    OP_20(0x3E8)
    Fade(1000)
    OP_6D(2850, 5000, -4700, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1870, 5000, -4700, 90)
    TurnDirection(0xE, 0x101, 0)
    OP_0D()
    OP_21()
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #185
        0xE,
        "#020F#2P哎呀，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1025F#6P雪拉姐，你在这里啊。\x02\x03",

            "#1015F唔……\x01",
            "我是不是打扰你了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xE,
        (
            "#027F#2P呵呵，你客气什么。\x02\x03",

            "你想问我关于\x01",
            "露茜奥拉姐姐的事对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1013F#6P啊，嗯……\x02\x03",

            "#1007F以前好像见过，\x01",
            "但是几乎完全不记得了……\x02\x03",

            "她是怎样的人呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xE,
        (
            "#524F#2P这个嘛……\x02\x03",

            "#026F『幻惑之铃』露茜奥拉。\x02\x03",

            "她能藉由使用铃铛与扇子的『舞蹈』\x01",
            "令观众产生幻觉……\x02\x03",

            "#020F在我以前待过的剧团里\x01",
            "是被视为台柱的艺人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#1015F#6P这样啊……\x02\x03",

            "那种幻觉，\x01",
            "是使用导力器产生的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xE,
        (
            "#027F#2P不，似乎是自古流传下来的\x01",
            "名为『幻术』的技术。\x02\x03",

            "因为姐姐她好像原本就\x01",
            "出生于这样的家庭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#1026F#6P原本……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xE,
        (
            "#524F#2P当旅行艺人的人\x01",
            "大致上分为两种。\x02\x03",

            "由于某种原因背井离乡的人\x01",
            "和无依无靠终生孤独的人……\x02\x03",

            "#026F露茜奥拉姐姐是前者……\x01",
            "而我……是后者。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_24(0x79, 0x3C)
    OP_24(0x1C3, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x32)
    OP_24(0x1C3, 0x50)
    Sleep(100)
    OP_24(0x79, 0x28)
    OP_24(0x1C3, 0x46)
    Sleep(100)
    OP_24(0x79, 0x1E)
    OP_24(0x1C3, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x14)
    OP_24(0x1C3, 0x32)
    Sleep(100)
    OP_24(0x79, 0xA)
    OP_24(0x1C3, 0x28)
    Sleep(100)
    OP_24(0x1C3, 0x1E)
    Sleep(100)
    OP_24(0x1C3, 0x14)
    Sleep(100)
    OP_23(0x79)
    OP_23(0x1C3)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #194
        (
            "\x07\x0C我被哈维剧团收养\x01",
            "是在７岁左右的时候吧。\x02\x03",

            "那时的我，流落于城市的贫民窟\x01",
            "终日过着颓废的生活。\x02\x03",

            "扒窃，掉包，顺手牵羊……\x01",
            "真的没干过什么好事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x24007F, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #195
        (
            "\x07\x0C向这样的我\x01",
            "伸出援手的\x01",
            "就是哈维团长和姐姐。\x02\x03",

            "他们教给无法相信他人的我\x01",
            "何谓家庭的温暖……\x02\x03",

            "为了让我找到自己的容身之处\x01",
            "他们教我各种各样的技艺和技术。\x02\x03",

            "舞蹈，驯兽，塔罗牌。\x01",
            "全都是姐姐他们传授给我的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #196
        (
            "\x07\x0C但是……八年前。\x02\x03",

            "在团长死于事故之后，\x01",
            "剧团就变得七零八落了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240080, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #197
        (
            "\x07\x0C我本来打算\x01",
            "跟随姐姐的……\x02\x03",

            "但她却留下『我有要做的事』这句话后\x01",
            "就消失了。\x02\x03",

            "穷途末路的我\x01",
            "只好去找除团长和姐姐之外\x01",
            "唯一可以信赖的人商量。\x02\x03",

            "对──就是当时以游击士身份\x01",
            "展开活跃的卡西乌斯老师。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x79, 0x1, 0xA)
    OP_22(0x1C3, 0x1, 0x14)
    Sleep(100)
    OP_24(0x1C3, 0x1E)
    Sleep(100)
    OP_24(0x1C3, 0x28)
    Sleep(100)
    OP_24(0x79, 0x14)
    OP_24(0x1C3, 0x32)
    Sleep(100)
    OP_24(0x79, 0x1E)
    OP_24(0x1C3, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x28)
    OP_24(0x1C3, 0x46)
    Sleep(100)
    OP_24(0x79, 0x32)
    OP_24(0x1C3, 0x50)
    Sleep(100)
    OP_24(0x79, 0x3C)
    OP_24(0x1C3, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x46)
    OP_24(0x1C3, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(    #198
        0x101,
        "#1026F#6P原来发生过这种事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xE,
        (
            "#026F#2P我会成为游击士，\x01",
            "是为了尽可能地变强。\x02\x03",

            "在姐姐回来之前，\x01",
            "一个人堂堂正正的活下去。\x02\x03",

            "#524F但是……八年过去了。\x02\x03",

            "或许这是个好机会，\x01",
            "该重新审视一下自己所走的道路了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        "#1003F#6P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xE,
        (
            "#021F#2P呵呵，别摆出那副表情啦。\x02\x03",

            "#020F就像金先生说的一样\x01",
            "我并不打算话也不说就迎面开战。\x02\x03",

            "只是想和姐姐\x01",
            "好好地谈一次。\x02\x03",

            "问问她为了什么理由\x01",
            "才会与『结社』勾结。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1025F#6P嗯……说得也是。\x02\x03",

            "#1018F雪拉姐，加油！\x01",
            "我也会尽力帮忙的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xE,
        (
            "#021F#2P呵呵，谢谢。\x02\x03",

            "#027F不过艾丝蒂尔……\x01",
            "你真的长大了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#1004F#6P什，什么啊，突然这么说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xE,
        (
            "#524F#2P虽说一直以来\x01",
            "都觉得你不愧是老师的女儿……\x02\x03",

            "不过或许\x01",
            "我还是看走眼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        "#1015F#6P咦……什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xE,
        (
            "#020F#2P你的力量\x01",
            "和老师的力量好像有些许不同。\x02\x03",

            "老师是拥有像海一般胸怀宽广\x01",
            "而又气魄宏大的力量……\x02\x03",

            "#021F而你嘛……\x01",
            "是拥有照耀自己的同时也照耀他人，\x01",
            "像太阳一般的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_24(0x79, 0x3C)
    OP_24(0x1C3, 0x50)
    Sleep(100)
    OP_24(0x79, 0x32)
    OP_24(0x1C3, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x28)
    OP_24(0x1C3, 0x28)
    Sleep(100)
    OP_24(0x79, 0x1E)
    OP_24(0x1C3, 0x1E)
    Sleep(100)
    OP_24(0x79, 0x14)
    OP_24(0x1C3, 0x14)
    Sleep(100)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #209
        (
            "\x07\x05我的艾丝蒂尔……\x01",
            "如太阳般耀眼的你。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(500, 0)
    OP_24(0x79, 0x1E)
    OP_24(0x1C3, 0x1E)
    Sleep(100)
    OP_24(0x79, 0x28)
    OP_24(0x1C3, 0x28)
    Sleep(100)
    OP_24(0x79, 0x32)
    OP_24(0x1C3, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x3C)
    OP_24(0x1C3, 0x50)
    Sleep(100)
    OP_24(0x79, 0x46)
    OP_24(0x1C3, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(    #210
        0x101,
        "#1025F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xE,
        (
            "#026F#2P我想大家都是\x01",
            "被你这一点所吸引的。\x02\x03",

            "我也是……\x01",
            "当然还有约修亚也是。\x02\x03",

            "#020F你没有必要\x01",
            "因为老师而感到压力哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#1012F#6P嗯……\x02\x03",

            "#1017F嘿嘿，雪拉姐\x01",
            "果然是我的好姐姐。\x02\x03",

            "每次总是……\x01",
            "谢谢你为我打气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xE,
        (
            "#027F#2P呵呵，别客气。\x02\x03",

            "#021F作为回报，\x01",
            "下次陪我喝酒吧。\x02\x03",

            "既然当了正游击士\x01",
            "酒量也要够强才行啊㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1019F#6P我倒觉得这点\x01",
            "实在一点关系也没有……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(1400, 5000, -4730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1400, 5000, -4730, 270)
    OP_8C(0xE, 90, 0)
    OP_4B(0xE, 255)
    Sleep(500)
    OP_A2(0x1A06)
    OP_21()
    OP_1D(0x1)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_31_487C end

    def Function_32_55F1(): pass

    label("Function_32_55F1")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x49)
    Return()

    # Function_32_55F1 end

    def Function_33_5608(): pass

    label("Function_33_5608")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x1)
    Return()

    # Function_33_5608 end

    SaveToFile()

Try(main)
