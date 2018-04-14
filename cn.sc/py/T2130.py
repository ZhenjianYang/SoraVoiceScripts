from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2130   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2130   ._SN',
            'ED6_DT21/T2130_1 ._SN',
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
        '迪恩',                                 # 9
        '雷斯',                                 # 10
        '洛克',                                 # 11
        '托尼奥',                               # 12
        '迪奥德罗教区长',                       # 13
        '修女芙丽达',                           # 14
        '凯文神父',                             # 15
        '爱蕾塔',                               # 16
        '豆豆',                                 # 17
        '阿杰',                                 # 18
        '路易',                                 # 19
        '布鲁托',                               # 20
        '巴克',                                 # 21
        '多姆斯',                               # 22
        '加布',                                 # 23
        '皮卡罗',                               # 24
        '布拉奥',                               # 25
        '朵洛希',                               # 26
        '目标用照相机',                         # 27
        '托尼奥',                               # 28
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
        'ED6_DT07/CH02510 ._CH',             # 00
        'ED6_DT07/CH02520 ._CH',             # 01
        'ED6_DT07/CH02530 ._CH',             # 02
        'ED6_DT07/CH01043 ._CH',             # 03
        'ED6_DT07/CH01170 ._CH',             # 04
        'ED6_DT07/CH01670 ._CH',             # 05
        'ED6_DT07/CH01410 ._CH',             # 06
        'ED6_DT27/CH03080 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
        'ED6_DT07/CH01070 ._CH',             # 09
        'ED6_DT26/CH20237 ._CH',             # 0A
        'ED6_DT07/CH01390 ._CH',             # 0B
        'ED6_DT07/CH01393 ._CH',             # 0C
        'ED6_DT07/CH00450 ._CH',             # 0D
        'ED6_DT07/CH00460 ._CH',             # 0E
        'ED6_DT07/CH00470 ._CH',             # 0F
        'ED6_DT27/CH04000 ._CH',             # 10
        'ED6_DT07/CH00120 ._CH',             # 11
        'ED6_DT07/CH00150 ._CH',             # 12
        'ED6_DT07/CH00454 ._CH',             # 13
        'ED6_DT07/CH00464 ._CH',             # 14
        'ED6_DT07/CH00474 ._CH',             # 15
        'ED6_DT06/CH20063 ._CH',             # 16
        'ED6_DT07/CH00122 ._CH',             # 17
        'ED6_DT07/CH01000 ._CH',             # 18
        'ED6_DT06/CH20064 ._CH',             # 19
        'ED6_DT07/CH01040 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT07/CH02510P._CP',             # 00
        'ED6_DT07/CH02520P._CP',             # 01
        'ED6_DT07/CH02530P._CP',             # 02
        'ED6_DT07/CH01043P._CP',             # 03
        'ED6_DT07/CH01170P._CP',             # 04
        'ED6_DT07/CH01670P._CP',             # 05
        'ED6_DT07/CH01410P._CP',             # 06
        'ED6_DT27/CH03080P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
        'ED6_DT07/CH01070P._CP',             # 09
        'ED6_DT26/CH20237P._CP',             # 0A
        'ED6_DT07/CH01390P._CP',             # 0B
        'ED6_DT07/CH01393P._CP',             # 0C
        'ED6_DT07/CH00450P._CP',             # 0D
        'ED6_DT07/CH00460P._CP',             # 0E
        'ED6_DT07/CH00470P._CP',             # 0F
        'ED6_DT27/CH04000P._CP',             # 10
        'ED6_DT07/CH00120P._CP',             # 11
        'ED6_DT07/CH00150P._CP',             # 12
        'ED6_DT07/CH00454P._CP',             # 13
        'ED6_DT07/CH00464P._CP',             # 14
        'ED6_DT07/CH00474P._CP',             # 15
        'ED6_DT06/CH20063P._CP',             # 16
        'ED6_DT07/CH00122P._CP',             # 17
        'ED6_DT07/CH01000P._CP',             # 18
        'ED6_DT06/CH20064P._CP',             # 19
        'ED6_DT07/CH01040P._CP',             # 1A
    )

    DeclNpc(
        X                   = -4150,
        Z                   = 0,
        Y                   = 9070,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -1590,
        Z                   = 0,
        Y                   = 7520,
        Direction           = 322,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -2970,
        Z                   = 0,
        Y                   = 7390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 56350,
        Z                   = 80,
        Y                   = 44530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 58970,
        Z                   = 1000,
        Y                   = 52150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 54460,
        Z                   = 0,
        Y                   = 50690,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 60540,
        Z                   = 1000,
        Y                   = 52350,
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
        X                   = 59120,
        Z                   = 0,
        Y                   = 47050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 57540,
        Z                   = 0,
        Y                   = 47300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 59980,
        Z                   = 0,
        Y                   = 47260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 61430,
        Z                   = 0,
        Y                   = 47360,
        Direction           = 303,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -10050,
        Z                   = 0,
        Y                   = 3740,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -12730,
        Z                   = 0,
        Y                   = 4160,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -9930,
        Z                   = 0,
        Y                   = 7470,
        Direction           = 280,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -13330,
        Z                   = 600,
        Y                   = 6230,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -11600,
        Z                   = 250,
        Y                   = 1950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 59140,
        Z                   = 0,
        Y                   = 46600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 52250,
        Z                   = 5000,
        Y                   = 51330,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        X                   = 56350,
        Z                   = -600,
        Y                   = 44730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 59140,
        TriggerZ            = 1000,
        TriggerY            = 50250,
        TriggerRange        = 400,
        ActorX              = 58970,
        ActorZ              = 2700,
        ActorY              = 52150,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_426",          # 00, 0
        "Function_1_580",          # 01, 1
        "Function_2_591",          # 02, 2
        "Function_3_70E",          # 03, 3
        "Function_4_8A3",          # 04, 4
        "Function_5_9DC",          # 05, 5
        "Function_6_CD0",          # 06, 6
        "Function_7_E95",          # 07, 7
        "Function_8_FD5",          # 08, 8
        "Function_9_1253",         # 09, 9
        "Function_10_1533",        # 0A, 10
        "Function_11_1667",        # 0B, 11
        "Function_12_16DB",        # 0C, 12
        "Function_13_1743",        # 0D, 13
        "Function_14_17EB",        # 0E, 14
        "Function_15_18B6",        # 0F, 15
        "Function_16_1EF0",        # 10, 16
        "Function_17_1F56",        # 11, 17
        "Function_18_216D",        # 12, 18
        "Function_19_221F",        # 13, 19
        "Function_20_2367",        # 14, 20
        "Function_21_4FA6",        # 15, 21
        "Function_22_4FC0",        # 16, 22
        "Function_23_4FD5",        # 17, 23
    )


    def Function_0_426(): pass

    label("Function_0_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_45F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_45C")
    SetChrFlags(0x18, 0x10)

    label("loc_45C")

    Jump("loc_4D7")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D7")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0xC, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_49E")
    Jump("loc_4D7")

    label("loc_49E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4C1")
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xD, 53390, 0, 52130, 180)
    Jump("loc_4D7")

    label("loc_4C1")

    SetChrFlags(0xD, 0x10)
    SetChrPos(0xD, -16840, 0, 42910, 270)

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_521")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F5")
    OP_A2(0xD)

    label("loc_4F5")

    Jump("loc_502")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_502")
    OP_A2(0xD)

    label("loc_502")

    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_515")
    Jump("loc_521")

    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0xA, 0x10)

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_52D")
    SetChrFlags(0xA, 0x80)

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_556")
    ClearChrFlags(0xE, 0x80)
    TurnDirection(0xC, 0xE, 0)
    TurnDirection(0xE, 0xC, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_556")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_562"),
        (SWITCH_DEFAULT, "loc_57F"),
    )


    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 6)), scpexpr(EXPR_END)), "loc_56C")
    Jump("loc_57C")

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_57C")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_57C")

    Jump("loc_57F")

    label("loc_57F")

    Return()

    # Function_0_426 end

    def Function_1_580(): pass

    label("Function_1_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_590")
    OP_64(0x0, 0x1)

    label("loc_590")

    Return()

    # Function_1_580 end

    def Function_2_591(): pass

    label("Function_2_591")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B6")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_6F8")

    label("loc_5B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CF")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_6F8")

    label("loc_5CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E8")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_6F8")

    label("loc_5E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_601")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_6F8")

    label("loc_601")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61A")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_6F8")

    label("loc_61A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_633")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_6F8")

    label("loc_633")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_6F8")

    label("loc_64C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_665")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_6F8")

    label("loc_665")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67E")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_6F8")

    label("loc_67E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_697")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_6F8")

    label("loc_697")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B0")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_6F8")

    label("loc_6B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C9")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_6F8")

    label("loc_6C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_6F8")

    label("loc_6E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F8")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_6F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_6F8")

    label("loc_70D")

    Return()

    # Function_2_591 end

    def Function_3_70E(): pass

    label("Function_3_70E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_757")

    ChrTalk(    #0
        0xFE,
        (
            "贝尔夫那家伙\x01",
            "在帮忙选举呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "洛克他们\x01",
            "不会生气啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89F")

    label("loc_757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_809")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_798")

    ChrTalk(    #2
        0xFE,
        "唉，孩提时代多好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "真想回到那时候啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_806")

    label("loc_798")

    OP_A2(0xC)

    ChrTalk(    #4
        0xFE,
        "今天是主日学校的日子啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "别看我这样，我以前因为努力学习\x01",
            "经常被修女称赞呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "唉，那时候多好。\x02",
    )

    CloseMessageWindow()

    label("loc_806")

    Jump("loc_89F")

    label("loc_809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_850")

    ChrTalk(    #7
        0xFE,
        "全城都是选举气氛呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "反正闲着\x01",
            "就偷偷去投票吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89F")

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_89F")

    ChrTalk(    #9
        0xFE,
        (
            "呼～好久没有\x01",
            "这么紧张的场面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "总，总而言之\x01",
            "还好没被卷进去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89F")

    TalkEnd(0xFE)
    Return()

    # Function_3_70E end

    def Function_4_8A3(): pass

    label("Function_4_8A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_8F6")

    ChrTalk(    #11
        0xFE,
        (
            "选举那么麻烦，\x01",
            "真是受不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "如果能给米拉\x01",
            "那倒还能考虑考虑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D8")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_944")

    ChrTalk(    #13
        0xFE,
        (
            "娱乐场是挺有趣的，\x01",
            "就是稍微远了点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "桥又出问题了\x01",
            "过不去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D8")

    label("loc_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_996")

    ChrTalk(    #15
        0xFE,
        (
            "参加了武术大会\x01",
            "一点好处也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "所以我说麻烦\x01",
            "不要去了嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D8")

    label("loc_996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_9D8")

    ChrTalk(    #17
        0xFE,
        (
            "洛克大哥他们\x01",
            "也真是爱打架呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "明知道会被打败的。\x02",
    )

    CloseMessageWindow()

    label("loc_9D8")

    TalkEnd(0xFE)
    Return()

    # Function_4_8A3 end

    def Function_5_9DC(): pass

    label("Function_5_9DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_A92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A46")

    ChrTalk(    #19
        0xFE,
        (
            "洛克那家伙好像想把\x01",
            "渡鸦帮变成自卫团呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "嗯，要是惹上麻烦\x01",
            "我就闪人好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_A8F")

    label("loc_A46")


    ChrTalk(    #21
        0xFE,
        (
            "洛克那家伙好像想把\x01",
            "渡鸦帮变成自卫团呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "不过，反正和我没关系。\x02",
    )

    CloseMessageWindow()

    label("loc_A8F")

    Jump("loc_CCC")

    label("loc_A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B20")

    ChrTalk(    #23
        0xFE,
        "嗯？什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "我们的成员\x01",
            "全都出去了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "渡口在这边～这样\x01",
            "叫喊着，没看见？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "洛克那家伙真是的，\x01",
            "想什么呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_B62")

    label("loc_B20")


    ChrTalk(    #27
        0xFE,
        (
            "我们的成员\x01",
            "全都出去了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "洛克那家伙真是的，\x01",
            "想什么呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B62")

    Jump("loc_CCC")

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_BAB")

    ChrTalk(    #29
        0xFE,
        (
            "洛克的样子\x01",
            "好像挺奇怪的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "说不定准备\x01",
            "逃跑比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCC")

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_C2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_BD5")

    ChrTalk(    #31
        0xFE,
        (
            "卷进纠纷\x01",
            "就麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C28")

    label("loc_BD5")

    OP_A2(0xB)

    ChrTalk(    #32
        0xFE,
        (
            "卷进纠纷\x01",
            "就麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "关于这个我总是\x01",
            "不疏防范的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "出问题之前就撤。\x02",
    )

    CloseMessageWindow()

    label("loc_C28")

    Jump("loc_CCC")

    label("loc_C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C81")

    ChrTalk(    #35
        0xFE,
        (
            "正商量着要干什么呢，\x01",
            "不知不觉天就黑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "真是的，\x01",
            "浪费人生啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCC")

    label("loc_C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_CCC")

    ChrTalk(    #37
        0xFE,
        (
            "呼，这次\x01",
            "也没被卷进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "我可不想惹麻烦。\x01",
            "人生就得圆滑点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCC")

    TalkEnd(0xFE)
    Return()

    # Function_5_9DC end

    def Function_6_CD0(): pass

    label("Function_6_CD0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_D27")

    ChrTalk(    #39
        0xFE,
        (
            "嘿嘿，欧尼尔老爷子\x01",
            "多找钱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "当然要保持沉默啦。\x01",
            "我可真是坏啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E91")

    label("loc_D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_D6F")

    ChrTalk(    #41
        0xFE,
        (
            "巧克力香烟\x01",
            "没有了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "我要是没有这个\x01",
            "就镇定不下来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E91")

    label("loc_D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DF6")

    ChrTalk(    #43
        0xFE,
        (
            "在娱乐场拣到的游戏币\x01",
            "变卖了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "嘿，嘿嘿……\x01",
            "白拿１００啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "嗯，不知道店员有没有发现。\x01",
            "……哆嗦，哆哆嗦嗦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E91")

    label("loc_DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_E91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_E4D")

    ChrTalk(    #46
        0xFE,
        (
            "洛克大哥他们\x01",
            "虽然强了很多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "终究还是敌不过\x01",
            "那些游击士啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E91")

    label("loc_E4D")


    ChrTalk(    #48
        0xFE,
        (
            "洛克大哥他们\x01",
            "虽然强了很多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "终究还不是\x01",
            "阿加特的对手啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E91")

    TalkEnd(0xFE)
    Return()

    # Function_6_CD0 end

    def Function_7_E95(): pass

    label("Function_7_E95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_EDD")

    ChrTalk(    #50
        0xFE,
        (
            "贝尔夫那家伙好像在他老爸的\x01",
            "事务所里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "真奇怪。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FD1")

    label("loc_EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_F1E")

    ChrTalk(    #52
        0xFE,
        "居然在城市中心吵架。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "选举的人\x01",
            "一定也很闲啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD1")

    label("loc_F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_F49")

    ChrTalk(    #54
        0xFE,
        "呼啊～好无聊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F85")

    label("loc_F49")

    OP_A2(0xA)

    ChrTalk(    #55
        0xFE,
        "呼啊～好无聊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "想去娱乐场，\x01",
            "没米拉也不行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F85")

    Jump("loc_FD1")

    label("loc_F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_FD1")

    ChrTalk(    #57
        0xFE,
        (
            "贝尔夫那家伙\x01",
            "和老爸关系不好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "所以，就加入\x01",
            "我们这里了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD1")

    TalkEnd(0xFE)
    Return()

    # Function_7_E95 end

    def Function_8_FD5(): pass

    label("Function_8_FD5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1024")

    ChrTalk(    #59
        0xFE,
        (
            "洛克到底\x01",
            "怎么了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "说要『活动一下身体』\x01",
            "一去就不回了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_124F")

    label("loc_1024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_10B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1079")

    ChrTalk(    #61
        0xFE,
        (
            "想当市长的家伙\x01",
            "让他们当不就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "谁来\x01",
            "都比那个戴尔蒙强。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B4")

    label("loc_1079")

    OP_A2(0x7)

    ChrTalk(    #63
        0xFE,
        (
            "这么说来\x01",
            "正在选举呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "当然我是\x01",
            "不能去投票的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B4")

    Jump("loc_124F")

    label("loc_10B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_112B")

    ChrTalk(    #65
        0xFE,
        (
            "我们应该也\x01",
            "变强了许多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "但是最近，魔兽\x01",
            "变得更强了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "弄得我们一点也没有变强的感觉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_124F")

    label("loc_112B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_124F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_END)), "loc_11A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_116F")

    ChrTalk(    #68
        0xFE,
        "哟，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "贝尔夫那家伙怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_11A0")

    label("loc_116F")


    ChrTalk(    #70
        0xFE,
        "啊，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "贝尔夫那家伙，\x01",
            "说什么了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A0")

    Jump("loc_124F")

    label("loc_11A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_11FB")

    ChrTalk(    #72
        0xFE,
        (
            "贝尔夫的家\x01",
            "在市长官邸的右边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "一个叫诺曼的大叔家，\x01",
            "他是家里的长子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_124F")

    label("loc_11FB")


    ChrTalk(    #74
        0xFE,
        (
            "贝尔夫的家是\x01",
            "市长官邸右边的房子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "一个叫诺曼的大叔家，\x01",
            "他是家里的长子哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124F")

    TalkEnd(0x8)
    Return()

    # Function_8_FD5 end

    def Function_9_1253(): pass

    label("Function_9_1253")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1348")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_12BF")

    ChrTalk(    #76
        0xFE,
        (
            "刚才出去了一趟，\x01",
            "洛克在仓库的后面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "那家伙一个人不声不响的\x01",
            "在努力练习挥刀呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1345")

    label("loc_12BF")

    OP_A2(0x8)

    ChrTalk(    #78
        0xFE,
        (
            "刚才出去了一趟，\x01",
            "洛克在仓库的后面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "那家伙一个人不声不响的\x01",
            "在努力练习挥刀呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "洛克一旦开始锻炼身体\x01",
            "就没什么好事啦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1345")

    Jump("loc_152F")

    label("loc_1348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1416")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_13A3")

    ChrTalk(    #81
        0xFE,
        (
            "嘿嘿，支持者们\x01",
            "发生了争执呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "装得品格高尚，\x01",
            "骨子里还不是一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1413")

    label("loc_13A3")

    OP_A2(0x8)

    ChrTalk(    #83
        0xFE,
        (
            "嘿嘿，支持者们\x01",
            "发生了争执呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "装得品格高尚，\x01",
            "骨子里还不是一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "戴尔蒙那家伙\x01",
            "就是最好的例子～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1413")

    Jump("loc_152F")

    label("loc_1416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1450")

    ChrTalk(    #86
        0xFE,
        (
            "最近洛克那家伙\x01",
            "好像在想些什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A3")

    label("loc_1450")

    OP_A2(0x8)

    ChrTalk(    #87
        0xFE,
        (
            "洛克那家伙\x01",
            "好像在想些什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "那家伙变成那样的时候\x01",
            "最好还是不要靠近。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A3")

    Jump("loc_152F")

    label("loc_14A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_152F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DD")

    ChrTalk(    #89
        0xFE,
        (
            "嘿嘿，艾丝蒂尔。\x01",
            "要再来哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152F")

    label("loc_14DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_150D")

    ChrTalk(    #90
        0xFE,
        (
            "辛、辛苦了。\x01",
            "再等你们来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152F")

    label("loc_150D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152F")

    ChrTalk(    #91
        0xFE,
        "要再来哦～大姐。\x02",
    )

    CloseMessageWindow()

    label("loc_152F")

    TalkEnd(0x9)
    Return()

    # Function_9_1253 end

    def Function_10_1533(): pass

    label("Function_10_1533")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1566")

    ChrTalk(    #92
        0xFE,
        "市长选举啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "哼，无聊啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1663")

    label("loc_1566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_159B")

    ChrTalk(    #94
        0xFE,
        "…………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "可恶…\x02",
    )

    CloseMessageWindow()
    Jump("loc_15CB")

    label("loc_159B")

    OP_A2(0x9)

    ChrTalk(    #96
        0xFE,
        "可恶…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "这样下去不行\x01",
            "我们也明白啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CB")

    Jump("loc_1663")

    label("loc_15CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1609")

    ChrTalk(    #98
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "…………可恶。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1663")

    label("loc_1609")


    ChrTalk(    #100
        0xFE,
        (
            "看到那影子之后\x01",
            "贝尔夫就把自己关在家里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "本来就是好人家的小孩嘛，\x01",
            "胆小的家伙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1663")

    TalkEnd(0xA)
    Return()

    # Function_10_1533 end

    def Function_11_1667(): pass

    label("Function_11_1667")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16B6")

    ChrTalk(    #102
        0xFE,
        (
            "嗯，果然还是\x01",
            "游击士有型啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "我也想当当看啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_16D7")

    label("loc_16B6")


    ChrTalk(    #104
        0xFE,
        (
            "今天教区长的\x01",
            "授课真有趣啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D7")

    TalkEnd(0xFE)
    Return()

    # Function_11_1667 end

    def Function_12_16DB(): pass

    label("Function_12_16DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1724")

    ChrTalk(    #105
        0xFE,
        (
            "游击士\x01",
            "还当学校的老师啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "真吃了一惊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_173F")

    label("loc_1724")


    ChrTalk(    #107
        0xFE,
        (
            "和爱蕾塔\x01",
            "一起学习哦⊙\x02",
        )
    )

    CloseMessageWindow()

    label("loc_173F")

    TalkEnd(0xFE)
    Return()

    # Function_12_16DB end

    def Function_13_1743(): pass

    label("Function_13_1743")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A1")

    ChrTalk(    #108
        0xFE,
        (
            "上课差、差不多\x01",
            "该结束了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "再不赶快\x01",
            "下一艘定期船就要到了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E7")

    label("loc_17A1")


    ChrTalk(    #110
        0xFE,
        (
            "我在飞船坪\x01",
            "经常看见游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "总是很忙的样子，\x01",
            "工作很辛苦吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E7")

    TalkEnd(0xFE)
    Return()

    # Function_13_1743 end

    def Function_14_17EB(): pass

    label("Function_14_17EB")

    OP_4A(0xC, 255)
    OP_4A(0xE, 255)

    ChrTalk(    #112
        0xC,
        (
            "哟，辛苦了。\x01",
            "孤儿院的孩子们怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xE,
        (
            "#1060F很有精神呢。\x02\x03",

            "好像已经\x01",
            "完全恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        (
            "唔，就像幼苗一样\x01",
            "茁壮成长吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xC,
        (
            "这下，我们\x01",
            "都不得不向他们学习了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xE,
        "#1060F呀，真的呢。\x02",
    )

    CloseMessageWindow()
    OP_4B(0xC, 255)
    OP_4B(0xE, 255)
    Return()

    # Function_14_17EB end

    def Function_15_18B6(): pass

    label("Function_15_18B6")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1957")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192B")

    ChrTalk(    #117
        0xC,
        (
            "渡鸦帮那些年轻人\x01",
            "也相当有用的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xC,
        (
            "经历挫折的人\x01",
            "复苏后会更努力，\x01",
            "感觉就是这样的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1954")

    label("loc_192B")


    ChrTalk(    #119
        0xC,
        (
            "渡鸦帮那些年轻人\x01",
            "也相当有用的样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1954")

    Jump("loc_1EEC")

    label("loc_1957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F8")

    ChrTalk(    #120
        0xC,
        (
            "这个现象发生的时候\x01",
            "市内一片骚乱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xC,
        (
            "现在总算镇定下来了，\x01",
            "但那时还真是着急啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "完全可以看出来\x01",
            "平时我们是多么\x01",
            "依赖导力器啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1A4A")

    label("loc_19F8")


    ChrTalk(    #123
        0xC,
        (
            "现象发生之初，\x01",
            "市内一片骚乱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xC,
        (
            "嗯，说明我们已经\x01",
            "这么的依赖导力器了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A4A")

    Jump("loc_1EEC")

    label("loc_1A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1AAB")

    ChrTalk(    #125
        0xC,
        (
            "无论哪边胜出，\x01",
            "还是赶快做个了结吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xC,
        (
            "选举结束的话\x01",
            "卢安市民就会团结努力了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEC")

    label("loc_1AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1CEF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B65")

    ChrTalk(    #127
        0xC,
        (
            "多亏这样的特质,\x01",
            "协会才会超越国家间的框架\x01",
            "成为整体的组织啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xC,
        (
            "此外协会和国家之间\x01",
            "也有一些规定……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xC,
        (
            "其中最有名的约定\x01",
            "就是不干涉国家权力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C27")

    label("loc_1B65")

    OP_A2(0x2)

    ChrTalk(    #130
        0xC,
        (
            "……在这时候\x01",
            "登场的组织就是游击士协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xC,
        (
            "大家都知道\x01",
            "游击士协会是统率\x01",
            "全境游击士的巨大组织……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xC,
        (
            "但其最大的特征\x01",
            "是非政府性的组织。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xC,
        (
            "啊～『非政府性』\x01",
            "就是和国家没有关系的意思。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C27")

    Jump("loc_1CEC")

    label("loc_1C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1C87")

    ChrTalk(    #134
        0xC,
        (
            "那么，授课最后再次\x01",
            "复习一下今天学的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xC,
        "首先是关于游击士协会的成立……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CEC")

    label("loc_1C87")

    OP_A2(0x2)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #136
        0xC,
        (
            "哦，是你们啊。\x01",
            "今天辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xC,
        (
            "还在授课中，\x01",
            "不好意思，我先失陪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 0)

    label("loc_1CEC")

    Jump("loc_1EEC")

    label("loc_1CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_1D44")

    ChrTalk(    #138
        0xC,
        "哦。那么着急，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xC,
        (
            "那位巡回神父哥哥\x01",
            "已经出发去下一个任地了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEC")

    label("loc_1D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_1DC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1DB7")
    OP_4A(0xE, 255)

    ChrTalk(    #140
        0xC,
        (
            "对了，凯文神父。\x01",
            "准备出发去下一个任地了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xC,
        (
            "机会难得，\x01",
            "再稍微在卢安享受一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xE, 255)
    Jump("loc_1DBE")

    label("loc_1DB7")

    OP_A2(0x4)
    Call(0, 14)

    label("loc_1DBE")

    Jump("loc_1EEC")

    label("loc_1DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E08")

    ChrTalk(    #142
        0xC,
        "好，今天有主日学校。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xC,
        (
            "鼓足干劲\x01",
            "去教导小鬼们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEC")

    label("loc_1E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1EEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1E6F")

    ChrTalk(    #144
        0xC,
        (
            "选举热闹倒是很好，\x01",
            "但希望别出现骚乱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xC,
        (
            "别看卢安这样，\x01",
            "当地人性情可火暴啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEC")

    label("loc_1E6F")

    OP_A2(0x2)

    ChrTalk(    #146
        0xC,
        (
            "选举热闹倒是很好，\x01",
            "但希望别出现骚乱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xC,
        (
            "别看卢安这样，\x01",
            "毕竟是海的男人们建立的城市嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xC,
        "当地人性情可火暴啦。\x02",
    )

    CloseMessageWindow()

    label("loc_1EEC")

    TalkEnd(0xC)
    Return()

    # Function_15_18B6 end

    def Function_16_1EF0(): pass

    label("Function_16_1EF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1F4B")
    OP_4A(0xC, 255)

    ChrTalk(    #149
        0xE,
        (
            "#1060F稍微休息一下\x01",
            "就打算马上出发了。\x02\x03",

            "调查了很多\x01",
            "但还是不够啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 255)
    Jump("loc_1F52")

    label("loc_1F4B")

    OP_A2(0x4)
    Call(0, 14)

    label("loc_1F52")

    TalkEnd(0xFE)
    Return()

    # Function_16_1EF0 end

    def Function_17_1F56(): pass

    label("Function_17_1F56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1F63")
    Jump("loc_2169")

    label("loc_1F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2169")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2062")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1FD8")

    ChrTalk(    #150
        0xFE,
        (
            "嗯～１１８７年吗。\x01",
            "好，这次记住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "尤迪斯是１１８７年。\x01",
            "是１１８７年。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205F")

    label("loc_1FD8")

    OP_A2(0x1)

    ChrTalk(    #152
        0xFE,
        (
            "嗯……\x01",
            "艾莉茜雅Ⅱ世即位是１１６２年。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "嗯～此后\x01",
            "尤迪斯皇太子逝世是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "……啊～又忘记了。\x02",
    )

    CloseMessageWindow()

    label("loc_205F")

    Jump("loc_2169")

    label("loc_2062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_20DD")

    ChrTalk(    #156
        0xFE,
        (
            "啊，刚设立的时候不叫中央工房，\x01",
            "是叫《技术工房》啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "这些地方\x01",
            "入学考试很可能会考到，\x01",
            "要注意才行啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_20DD")

    OP_A2(0x1)

    ChrTalk(    #158
        0xFE,
        (
            "嗯……\x01",
            "中央工房的设立是１１５７年。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "『卡特兰帕号』\x01",
            "试飞是１１６８年，\x01",
            "定期船开航是１１７５年……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "……好，到这里都记住了。\x02",
    )

    CloseMessageWindow()

    label("loc_2169")

    TalkEnd(0xFE)
    Return()

    # Function_17_1F56 end

    def Function_18_216D(): pass

    label("Function_18_216D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_217A")
    Jump("loc_221B")

    label("loc_217A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_221B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21C2")

    ChrTalk(    #161
        0xFE,
        "啊～是刚才的老师。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "又来教课了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_221B")

    label("loc_21C2")


    ChrTalk(    #163
        0xFE,
        (
            "嘿嘿，爱蕾塔\x01",
            "也能上主日学校了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "要好好学习，\x01",
            "和基诺奇奥哥哥\x01",
            "上同一所学校哦⊙\x02",
        )
    )

    CloseMessageWindow()

    label("loc_221B")

    TalkEnd(0xFE)
    Return()

    # Function_18_216D end

    def Function_19_221F(): pass

    label("Function_19_221F")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_229D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2279")

    ChrTalk(    #165
        0xFE,
        (
            "女神啊……\x01",
            "请宽恕我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "失去信仰的人们\x01",
            "一定也会悔改吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_229A")

    label("loc_2279")


    ChrTalk(    #167
        0xFE,
        (
            "啊啊，女神……\x01",
            "请宽恕我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_229A")

    Jump("loc_2363")

    label("loc_229D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2363")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2327")

    ChrTalk(    #168
        0xFE,
        (
            "到卢安\x01",
            "是来找熟人的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "没想到运气不好变成这样\x01",
            "想回也回不去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "呼，不管怎样现在只能\x01",
            "祈求女神保佑了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_2363")

    label("loc_2327")


    ChrTalk(    #171
        0xFE,
        (
            "来，你们也来\x01",
            "向女神祈祷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "变成这样\x01",
            "只能祈祷了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2363")

    TalkEnd(0x18)
    Return()

    # Function_19_221F end

    def Function_20_2367(): pass

    label("Function_20_2367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2378")
    Call(0, 23)

    label("loc_2378")

    EventBegin(0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x101, 110, 0, 450, 348)
    SetChrPos(0xF7, -790, 0, -230, 347)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_8C(0x8, 135, 0)
    OP_8C(0x9, 270, 0)
    OP_6D(-3640, 0, 9320, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #173
        0x8,
        "#5P唉，感觉最近懒洋洋的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x8,
        (
            "#5P进行了各种锻炼\x01",
            "却没觉得有什么长进……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        "#3P哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        (
            "#3P没想到现在还会和\x01",
            "街道出没的魔兽苦战啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x9,
        (
            "#4P啊～感觉最近\x01",
            "魔兽好像比以前更凶残了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        (
            "#4P据说变得有以前的\x01",
            "2～3倍那么强了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 400)

    ChrTalk(    #179
        0xA,
        "#5P原来如此，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xA,
        (
            "#5P……没办法了。\x01",
            "好久没去了，再去街上转转吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        (
            "#5P如何，去北区的\x01",
            "拉旺塔尔游戏吧转转吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "#4P啊～２楼的娱乐场\x01",
            "重新装修开放了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x9,
        (
            "#4P好呀，听说还有\x01",
            "漂亮的服务小姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x9,
        (
            "#4P嘿嘿，运气好的话\x01",
            "说不定还可以亲近一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #185
        0x8,
        "#5P就是这个！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x8,
        (
            "#5P卡露娜大姐似乎也不在，\x01",
            "稍微放松下也无所谓吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_38D0")

    NpcTalk(    #187
        0x106,
        "青年的声音",
        "#2P……什么无所谓？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, 410, 0, -450, 348)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2704():
        OP_6D(-2500, 0, 4470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2704)

    def lambda_271C():
        OP_67(0, 6500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_271C)

    def lambda_2734():
        OP_6B(2670, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2734)

    def lambda_2744():
        OP_6E(280, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2744)

    def lambda_2754():

        label("loc_2754")

        TurnDirection(0x8, 0x106, 400)
        OP_48()
        Jump("loc_2754")

    QueueWorkItem2(0x8, 1, lambda_2754)

    def lambda_2765():

        label("loc_2765")

        TurnDirection(0x9, 0x106, 400)
        OP_48()
        Jump("loc_2765")

    QueueWorkItem2(0x9, 1, lambda_2765)

    def lambda_2776():

        label("loc_2776")

        TurnDirection(0xA, 0x106, 400)
        OP_48()
        Jump("loc_2776")

    QueueWorkItem2(0xA, 1, lambda_2776)
    TurnDirection(0x13, 0x106, 800)
    TurnDirection(0x14, 0x106, 800)
    TurnDirection(0x15, 0x106, 800)
    Sleep(300)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #188
        0x8,
        "#4P阿、阿加特！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        "#5P……………\x02",
    )

    CloseMessageWindow()

    def lambda_27DF():

        label("loc_27DF")

        TurnDirection(0x101, 0x9, 0)
        OP_48()
        Jump("loc_27DF")

    QueueWorkItem2(0x106, 1, lambda_27DF)

    def lambda_27F0():

        label("loc_27F0")

        TurnDirection(0x106, 0xA, 0)
        OP_48()
        Jump("loc_27F0")

    QueueWorkItem2(0x106, 2, lambda_27F0)

    def lambda_2801():

        label("loc_2801")

        TurnDirection(0x13, 0x106, 0)
        OP_48()
        Jump("loc_2801")

    QueueWorkItem2(0x13, 0, lambda_2801)

    def lambda_2812():

        label("loc_2812")

        TurnDirection(0x14, 0x106, 0)
        OP_48()
        Jump("loc_2812")

    QueueWorkItem2(0x14, 0, lambda_2812)

    def lambda_2823():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0x12B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2823)
    Sleep(300)

    def lambda_2843():
        OP_8F(0xFE, 0xFFFFF8F8, 0x0, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2843)
    Sleep(500)

    def lambda_2863():
        OP_6D(-3350, 0, 7460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2863)

    def lambda_287B():
        OP_67(0, 8350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_287B)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x106, 0x0)
    OP_44(0x106, 0x1)
    OP_44(0x106, 0x2)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x14, 0x1)

    ChrTalk(    #190
        0x106,
        (
            "#057F真是的，你们这些人……\x02\x03",

            "稍微对你们改观了点\x01",
            "马上就偷懒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x8,
        (
            "#5P讨、讨厌啦～\x01",
            "只不过是开玩笑啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #192
        0x8,
        "#5P对了，那边的是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #193
        0x9,
        (
            "#2P这不是新人游击士\x01",
            "艾丝蒂尔吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#6P#1006F你们好，好久不见呢。\x01",
            "武术大会对战之后就没见过吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xA,
        "#5P啊～对了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x9,
        (
            "#2P呀～我们在那之后\x01",
            "一直观战到决胜战了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x9,
        (
            "#2P真是厉害啊。\x01",
            "我重新开始仰慕你了㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#6P#1016F啊哈哈……谢了。\x02\x03",

            "#1002F对了，今天来访\x01",
            "是为了协会的事……\x02\x03",

            "嗯，你们之中\x01",
            "是不是有人看到了『白影』？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #199
        0x8,
        "#5P那是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #200
        0x9,
        "#4P……是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        "#6P#1011F啊，你们果然知道啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x106,
        (
            "#053F那就赶快\x01",
            "把你们知道的说出来。\x02\x03",

            "别浪费我们的时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #203
        0xA,
        "#5P……稍等一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xA,
        (
            "#5P你啊，是不是\x01",
            "稍微得意忘形过头了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x106,
        "#052F……啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xA,
        "#5P烦死了，你。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xA,
        (
            "#5P随意离开组织\x01",
            "当了游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xA,
        (
            "#5P只在需要我们的时候\x01",
            "跑回来问话？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xA,
        "#5P真是受不了了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #210
        0x8,
        "#5P喂、喂洛克！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x106,
        (
            "#051F哼，还是那么\x01",
            "逞强啊。\x02\x03",

            "那么，要怎样\x01",
            "你才会满足？\x02\x03",

            "跪下求饶吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xA,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #213
        0xA,
        (
            "#5P就在这里……\x01",
            "跟我们决一胜负吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #214
        0x8,
        "#5P为、为什么会是这样啊！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #215
        0x9,
        "#2P喂喂，干嘛头脑发热啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xA,
        "#5P别吵，怎么也要有一个结果。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xA,
        (
            "#5P你们赢了\x01",
            "我们就说出知道的情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xA,
        (
            "#5P要是我们赢了……\x01",
            "就别再摆那么大架子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x106,
        "#051F哼，好。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 18)
    SetChrSubChip(0x106, 0)
    Sleep(500)

    ChrTalk(    #220
        0x106,
        (
            "#053F就用我这重剑\x01",
            "确认一下你们强了多少吧……\x02\x03",

            "#054F你们三个，鼓足劲来吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)

    def lambda_2F14():
        OP_8E(0xFE, 0xFFFFEEE4, 0x0, 0x1E46, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2F14)
    WaitChrThread(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)

    def lambda_2F39():
        TurnDirection(0x8, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F39)

    def lambda_2F47():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2F47)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #221
        0x8,
        (
            "#5P唉哟哟……\x01",
            "怎么会这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x9,
        (
            "#2P不过，能再和艾丝蒂尔\x01",
            "战斗真是幸运㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#6P#1016F是、是这样吗？\x02\x03",

            "#1018F算了。\x01",
            "我们也不会手软的！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 16)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    Battle(0x79A, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3046"),
        (SWITCH_DEFAULT, "loc_304B"),
    )


    label("loc_3046")

    OP_B4(0x0)
    Jump("loc_304B")

    label("loc_304B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    ClearMapFlags(0x1)
    SetChrPos(0x101, -1240, 0, 3520, 357)
    SetChrPos(0x106, -2620, 0, 3570, 359)
    SetChrPos(0xA, -2360, 0, 6360, 182)
    SetChrPos(0x9, -1110, 0, 7050, 195)
    SetChrPos(0x8, -3870, 0, 6790, 123)
    SetChrChipByIndex(0x8, 19)
    SetChrSubChip(0x8, 3)
    SetChrChipByIndex(0x9, 20)
    SetChrSubChip(0x9, 3)
    SetChrChipByIndex(0xA, 21)
    SetChrSubChip(0xA, 3)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x106, 65535)
    OP_6D(-2650, 0, 5850, 0)
    OP_67(0, 8350, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #224
        0x8,
        "哇～果然是强啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x9,
        "白旗白旗，投降啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xA,
        "……可恶………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x106,
        (
            "#051F哼，能出席武术大会\x01",
            "看来不完全是骗人的嘛。\x02\x03",

            "不过，本事还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        (
            "#1006F#6P但身为普通人来说\x01",
            "应该算是相当强了。\x02\x03",

            "别窝在这种地方了\x01",
            "不如也试着当游击士看看？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0xA, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    Sleep(500)

    ChrTalk(    #229
        0xA,
        "什么……\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_99(0x8, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    Sleep(500)

    ChrTalk(    #230
        0x8,
        "我、我们当游击士？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x9,
        "不、不可能啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        (
            "#1011F#6P看，像我这样的小女孩\x01",
            "也能当上游击士哦。\x02\x03",

            "你们也一样，只要有心\x01",
            "就一定能成功的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x8)
    OP_63(0x9)
    OP_63(0xA)
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #233
        0x106,
        (
            "#050F#5P喂，别说得那么简单。\x02\x03",

            "游击士又不是佣兵。\x01",
            "要做的事又不只是打架。\x02\x03",

            "你不是也经历了很多事吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #234
        0x101,
        (
            "#1015F#4P嗯……\x01",
            "那倒是啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x8,
        "就、就是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x8,
        (
            "我们几个，除了打架\x01",
            "又没别的本事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x9,
        (
            "那么好的事，\x01",
            "怎么可能嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xA,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xA,
        "总之，约定就是约定。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xA,
        (
            "你们想知道的事\x01",
            "我就说出来吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0xA, 400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #241
        0x106,
        "#051F哦，那就开始吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x101,
        (
            "#1002F#6P刚才也说了，\x01",
            "我们在找目击了\x01",
            "『白影』的人。\x02\x03",

            "听说\x01",
            "有你们的伙伴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xA,
        "啊啊，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xA,
        (
            "但是今天他没来，\x01",
            "是个叫贝尔夫的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x8,
        "１年前加入的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x8,
        (
            "阿加特也应该\x01",
            "记得有这个人的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x106,
        (
            "#552F啊啊，那家伙啊。\x02\x03",

            "调查之前的事件时\x01",
            "稍微说过几句话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x9,
        (
            "贝尔夫那家伙，这几天\x01",
            "都没来这个仓库呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x9,
        (
            "可能因为看到幽灵\x01",
            "太过受惊关在家里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #250
        0x101,
        (
            "#1020F#6P咦咦！？\x02\x03",

            "那、那难不成是\x01",
            "中了诅咒什么的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xA,
        (
            "这就不知道了……\x01",
            "不过确实被吓得够呛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xA,
        (
            "原本就是好人家的小孩，\x01",
            "胆小的家伙嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x106,
        (
            "#053F哼，生在正经的家庭\x01",
            "却还来当不良少年啊。\x02\x03",

            "#050F算了，详细情况\x01",
            "就去问本人吧，把他家地址告诉我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x8,
        (
            "嗯～\x01",
            "在市长官邸右边的房子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x8,
        (
            "住在那里的是诺曼大叔一家，\x01",
            "贝尔夫是他的长子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x101,
        (
            "#1011F#6P市长官邸右邻的房子，对吧。\x02\x03",

            "#1001F多谢你们提供情报。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #257
        0x101,
        (
            "#1006F#6P既然知道了地方\x01",
            "就去拜访贝尔夫看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #258
        0x106,
        "#051F#5P啊啊，就这样吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0xA, 400)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #259
        0x106,
        (
            "#051F那我们走了。\x01",
            "别闲着就去做坏事哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xA,
        "哼，多管闲事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x8,
        (
            "辛苦了。\x01",
            "有空请再来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x9,
        "加油哦～艾丝蒂尔㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E80")

    label("loc_38D0")


    ChrTalk(    #263
        0x101,
        (
            "#2P唉……\x01",
            "才刚刚有点改观……\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3956():
        OP_6D(-2500, 0, 4470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3956)

    def lambda_396E():
        OP_67(0, 6500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_396E)

    def lambda_3986():
        OP_6B(2670, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3986)

    def lambda_3996():
        OP_6E(280, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3996)

    def lambda_39A6():

        label("loc_39A6")

        TurnDirection(0x8, 0x103, 400)
        OP_48()
        Jump("loc_39A6")

    QueueWorkItem2(0x8, 1, lambda_39A6)

    def lambda_39B7():

        label("loc_39B7")

        TurnDirection(0x9, 0x101, 400)
        OP_48()
        Jump("loc_39B7")

    QueueWorkItem2(0x9, 1, lambda_39B7)

    def lambda_39C8():

        label("loc_39C8")

        TurnDirection(0xA, 0x103, 400)
        OP_48()
        Jump("loc_39C8")

    QueueWorkItem2(0xA, 1, lambda_39C8)
    TurnDirection(0x13, 0x103, 800)
    TurnDirection(0x14, 0x103, 800)
    TurnDirection(0x15, 0x103, 800)
    Sleep(300)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #264
        0x8,
        "#4P你、你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x9,
        "#6P哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x9,
        (
            "#6P这不是新人游击士\x01",
            "艾丝蒂尔吗！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A53():

        label("loc_3A53")

        TurnDirection(0x101, 0x9, 0)
        OP_48()
        Jump("loc_3A53")

    QueueWorkItem2(0x103, 1, lambda_3A53)

    def lambda_3A64():

        label("loc_3A64")

        TurnDirection(0x103, 0xA, 0)
        OP_48()
        Jump("loc_3A64")

    QueueWorkItem2(0x103, 2, lambda_3A64)

    def lambda_3A75():

        label("loc_3A75")

        TurnDirection(0x13, 0x103, 0)
        OP_48()
        Jump("loc_3A75")

    QueueWorkItem2(0x13, 0, lambda_3A75)

    def lambda_3A86():

        label("loc_3A86")

        TurnDirection(0x14, 0x103, 0)
        OP_48()
        Jump("loc_3A86")

    QueueWorkItem2(0x14, 0, lambda_3A86)

    def lambda_3A97():
        OP_8F(0xFE, 0xFFFFF8F8, 0x0, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A97)
    Sleep(300)

    def lambda_3AB7():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0x12B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3AB7)
    Sleep(500)

    def lambda_3AD7():
        OP_6D(-3350, 0, 7460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3AD7)

    def lambda_3AEF():
        OP_67(0, 8350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AEF)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x103, 0x0)
    OP_44(0x103, 0x1)
    OP_44(0x103, 0x2)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x14, 0x1)

    ChrTalk(    #267
        0x101,
        (
            "#6P#1006F你们好，好久不见呢。\x01",
            "武术大会对战之后就没见过吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xA,
        "#5P啊～对了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x9,
        (
            "#2P呀～我们在那之后\x01",
            "一直观战到决胜战了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x9,
        (
            "#2P真是厉害啊。\x01",
            "我重新开始仰慕你了㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        (
            "#6P#1008F啊哈哈……谢了。\x02\x03",

            "#1007F话说回来……\x01",
            "卡露娜姐姐一不在\x01",
            "你们就想偷懒啊。\x02\x03",

            "#1019F被阿加特知道了\x01",
            "可有你们好受的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x8,
        "#5P只、只不过是开玩笑嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x8,
        (
            "#5P可千万别\x01",
            "跟那家伙说哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xA,
        (
            "#5P切……那种家伙，\x01",
            "有什么好怕的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x9,
        "#2P嗯，对了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x9,
        (
            "#2P这位\x01",
            "妩媚的姐姐是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x101,
        (
            "#6P#1011F这是雪拉姐。\x01",
            "和我同为游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x103,
        (
            "#021F幸会。\x01",
            "我是雪拉扎德·哈维。\x02\x03",

            "和你们的阿加特前辈\x01",
            "关系很好哦。\x02\x03",

            "#027F呵呵……\x01",
            "多多关照哦，不良少年们㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #279
        0x8,
        "#5P吞口水……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xA,
        "#5P这真是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x9,
        "#2P好、好迷人～……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #282
        0x101,
        (
            "#4P#1019F我说，雪拉姐。\x01",
            "干嘛这么的散发魅力。\x02\x03",

            "这些人本来就\x01",
            "很少接触女性，很危险的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #283
        0x103,
        (
            "#021F#5P好了，\x01",
            "知道了。\x02\x03",

            "#027F先不说这些了，那件事\x01",
            "不问问他们看吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x101,
        "#1004F#4P啊，是哦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    TurnDirection(0x103, 0xA, 400)

    ChrTalk(    #285
        0x101,
        (
            "#1002F#6P那个，这次来找你们\x01",
            "是为了协会的事……\x02\x03",

            "嗯，你们之中\x01",
            "是不是有人看到了『白影』？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #286
        0x8,
        "#5P那是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #287
        0x9,
        "#4P……是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        "#1011F#6P啊，你们果然知道啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x103,
        (
            "#020F不介意的话\x01",
            "能不能告诉我们？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)
    TurnDirection(0x9, 0xA, 400)
    OP_8C(0xA, 0, 400)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #290
        0x8,
        "#5P果然这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xA,
        "#3P是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x9,
        "#4P……呜哦～太棒了～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #293
        0x101,
        "#1015F#6P（在说什么呢……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x8)
    OP_63(0x9)
    OP_63(0xA)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 400)
    TurnDirection(0xA, 0x103, 400)
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #294
        0x8,
        "#5P告诉你们是可以，不过有条件。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x9,
        (
            "#2P只要你们答应的话\x01",
            "就告诉你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x101,
        (
            "#1019F#6P什、什么啦。\x01",
            "什么条件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x103,
        (
            "#025F（嗯～是不是\x01",
            "有点挑拨过头了呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xA,
        "#5P哼，这还用说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xA,
        (
            "#5P说到那时候\x01",
            "的约定……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)

    def lambda_41D1():
        OP_8E(0xFE, 0xFFFFEEE4, 0x0, 0x1E46, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_41D1)
    WaitChrThread(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)

    def lambda_41F6():
        TurnDirection(0x8, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_41F6)

    def lambda_4204():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4204)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 0)
    Sleep(200)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #300
        0x8,
        "#5P那就是，一决胜负！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x8,
        (
            "#5P武术大会时的仇\x01",
            "就在这里讨回来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x103,
        "#6P#023F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x9,
        (
            "#2P从那以后，我们\x01",
            "可是强多～了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x9,
        (
            "#2P而且现在是３对２，\x01",
            "绝对不会输哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x101,
        "#6P#1006F怎么，原来是这种事啊。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 16)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #306
        0x101,
        (
            "#1018F#6P求之不得！\x01",
            "雪拉姐也没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x103,
        (
            "#023F嗯、嗯，倒是无所谓……\x02\x03",

            "#027F算了。\x01",
            "那就不客气了哦。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 17)
    SetChrSubChip(0x103, 0)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x103, 23)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_43D3():
        OP_99(0x103, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_43D3)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_43FA():
        OP_96(0xA, 0xFFFFF466, 0x0, 0x1D4C, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_43FA)
    WaitChrThread(0x103, 0x0)

    def lambda_441D():
        OP_99(0x103, 0x7, 0x9, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_441D)
    WaitChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 17)
    SetChrSubChip(0x103, 0)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #308
        0xA,
        "#2P#1K呜哦！？\x02",
    )


    ChrTalk(    #309
        0x8,
        "#3P#1K呜哎！？\x02",
    )


    ChrTalk(    #310
        0x9,
        "#4P#1K呜啊！？\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #311
        0x103,
        (
            "#021F欢迎，小男孩们。\x02\x03",

            "姐姐会\x01",
            "好好疼爱你们的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #312
        0x8,
        "#5P呀，啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xA,
        (
            "#5P果然跟女人打\x01",
            "实在是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x9,
        "#2P感觉没有男人风度啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x103,
        (
            "#021F呵呵，不用客气哦。\x02\x03",

            "#027F机会难得，\x01",
            "我会让你们酥软到骨子里的！㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0xA, 0xFF)
    Battle(0x79A, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_45C6"),
        (SWITCH_DEFAULT, "loc_45CB"),
    )


    label("loc_45C6")

    OP_B4(0x0)
    Jump("loc_45CB")

    label("loc_45CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    ClearMapFlags(0x1)
    SetChrPos(0x101, -1240, 0, 3520, 357)
    SetChrPos(0x103, -2620, 0, 3570, 359)
    SetChrPos(0xA, -2360, 0, 6360, 182)
    SetChrPos(0x9, -1110, 0, 7050, 195)
    SetChrPos(0x8, -3870, 0, 6790, 123)
    SetChrChipByIndex(0x8, 19)
    SetChrSubChip(0x8, 3)
    SetChrChipByIndex(0x9, 20)
    SetChrSubChip(0x9, 3)
    SetChrChipByIndex(0xA, 21)
    SetChrSubChip(0xA, 3)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    OP_6D(-2650, 0, 5850, 0)
    OP_67(0, 8350, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #316
        0x8,
        "啊呜啊呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x9,
        "麻、麻掉了～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xA,
        "败、败了………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x103,
        (
            "#023F哎呀，这么快就结束了？\x02\x03",

            "#021F最近的孩子真柔弱啊。\x01",
            "再多来点也没关系嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x101,
        (
            "#1007F#6P唉，面对雪拉姐\x01",
            "来多少都不够啦。\x02\x03",

            "#1006F不过，大会结束后\x01",
            "你们好像也有认真锻炼呢。\x02\x03",

            "别窝在这种地方了，\x01",
            "不如也试着当游击士看看？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0xA, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    Sleep(500)

    ChrTalk(    #321
        0xA,
        "什么……\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_99(0x8, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    Sleep(500)

    ChrTalk(    #322
        0x8,
        "我、我们当游击士？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x9,
        "不、不可能啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x101,
        (
            "#1011F#6P看，像我这样的小女孩\x01",
            "也能当上游击士哦。\x02\x03",

            "你们也一样，只要有心\x01",
            "就一定能成功的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x8)
    OP_63(0x9)
    OP_63(0xA)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #325
        0x103,
        (
            "#020F#5P嗯，单说打斗的话\x01",
            "应该跟准游击士差不多了。\x02\x03",

            "不过，游击士要做的\x01",
            "并不只是战斗的工作。\x02\x03",

            "不要以为嘴上说说\x01",
            "就能轻易当上哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #326
        0x101,
        "#1015F#4P嗯……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x8,
        "就、就是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x8,
        (
            "我们几个，除了打架\x01",
            "又没别的本事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x9,
        (
            "那么好的事，\x01",
            "怎么可能嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xA,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xA,
        "总之，约定就是约定。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xA,
        (
            "你们想知道的事\x01",
            "我就说出来吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xA, 400)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #333
        0x103,
        "#021F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x101,
        (
            "#1002F#6P刚才也说了，\x01",
            "我们在找目击了\x01",
            "『白影』的人。\x02\x03",

            "听说\x01",
            "有你们的伙伴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xA,
        "啊啊，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xA,
        (
            "但是今天他没来，\x01",
            "是个叫贝尔夫的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x8,
        "１年前加入帮里的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x8,
        (
            "你应该\x01",
            "也见过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x101,
        (
            "#1015F#6P嗯～你们以外的人\x01",
            "就没什么印象了……\x02\x03",

            "不过感觉好像是有这么个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x9,
        (
            "贝尔夫那家伙，差不多一周\x01",
            "都没来这个仓库呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x9,
        (
            "可能因为看到幽灵太过受惊，\x01",
            "就把自己关在家里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #342
        0x101,
        (
            "#1020F#6P咦咦！？\x02\x03",

            "那、那难不成是\x01",
            "中了诅咒什么的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xA,
        (
            "这就不知道了……\x01",
            "不过确实被吓得够呛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xA,
        (
            "原本就是好人家的小孩，\x01",
            "胆小的家伙嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x103,
        (
            "#026F好像有各种原因呢。\x02\x03",

            "#020F详细情况去问本人好了，\x01",
            "能告诉我们他住的地方吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x8,
        (
            "嗯～\x01",
            "在市长官邸右边的房子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x8,
        (
            "住在那里的是诺曼大叔一家，\x01",
            "贝尔夫是他的长子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x101,
        (
            "#1011F#6P市长官邸右边的房子，对吧。\x02\x03",

            "#1001F多谢你们提供情报。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #349
        0x101,
        (
            "#1006F#6P既然知道了地方\x01",
            "就去拜访贝尔夫看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #350
        0x103,
        "#020F#5P是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xA, 400)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #351
        0x103,
        (
            "#021F谢谢了，不良少年们。\x01",
            "我们告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xA,
        "哦，哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x8,
        (
            "辛苦了！\x01",
            "再来哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x9,
        (
            "加油哦～㈱\x01",
            "大姐姐还有艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E80")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x8, -4150, 0, 9070, 90)
    SetChrPos(0x9, -1590, 0, 7520, 322)
    SetChrPos(0xA, -2970, 0, 7390, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_8C(0x13, 280, 0)
    OP_8C(0x14, 80, 0)
    OP_8C(0x15, 303, 0)
    OP_8C(0x16, 90, 0)
    OP_8C(0x17, 0, 0)
    OP_6D(-3460, 0, 3720, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -3460, 0, 3720, 0)
    SetChrPos(0xF7, -3460, 0, 3720, 0)
    OP_6A(0x0)
    OP_A2(0x120E)
    OP_28(0x82, 0x2, 0x10)
    OP_28(0x82, 0x1, 0x20)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_20_2367 end

    def Function_21_4FA6(): pass

    label("Function_21_4FA6")

    ClearChrFlags(0xFE, 0x8)
    OP_8E(0xFE, 0xFFFFE656, 0x0, 0xED8, 0x1770, 0x0)
    Return()

    # Function_21_4FA6 end

    def Function_22_4FC0(): pass

    label("Function_22_4FC0")

    OP_8E(0xFE, 0xFFFFE110, 0x0, 0xB22, 0x1770, 0x0)
    Return()

    # Function_22_4FC0 end

    def Function_23_4FD5(): pass

    label("Function_23_4FD5")

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
        (0, "loc_504F"),
        (1, "loc_5055"),
        (SWITCH_DEFAULT, "loc_505B"),
    )


    label("loc_504F")

    OP_A2(0x1200)
    Jump("loc_505B")

    label("loc_5055")

    OP_A2(0x1201)
    Jump("loc_505B")

    label("loc_505B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5069")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_506D")

    label("loc_5069")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_506D")

    Return()

    # Function_23_4FD5 end

    SaveToFile()

Try(main)
