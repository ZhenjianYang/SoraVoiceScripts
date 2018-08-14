from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1101   ._SN',
        MapName             = 'Bose',
        Location            = 'T1101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        '梅贝尔市长',                           # 9
        '莉拉',                                 # 10
        '雅哈多老人',                           # 11
        '哈里',                                 # 12
        '米娜',                                 # 13
        '奥维德',                               # 14
        '爱蕾吉娅',                             # 15
        '雷塔',                                 # 16
        '法娜',                                 # 17
        '修女萝萨',                             # 18
        '雷纳德',                               # 19
        '亚妮拉丝',                             # 20
        '目标用照相机',                         # 21
        '',                                     # 22
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02360 ._CH',             # 00
        'ED6_DT07/CH02370 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH01160 ._CH',             # 03
        'ED6_DT07/CH01170 ._CH',             # 04
        'ED6_DT07/CH01120 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT07/CH01410 ._CH',             # 09
        'ED6_DT07/CH01270 ._CH',             # 0A
        'ED6_DT27/CH03090 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02360P._CP',             # 00
        'ED6_DT07/CH02370P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH01160P._CP',             # 03
        'ED6_DT07/CH01170P._CP',             # 04
        'ED6_DT07/CH01120P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT07/CH01410P._CP',             # 09
        'ED6_DT07/CH01270P._CP',             # 0A
        'ED6_DT27/CH03090P._CP',             # 0B
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48310,
        Z                   = 0,
        Y                   = 46460,
        Direction           = 262,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35880,
        Z                   = 0,
        Y                   = 53880,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35880,
        Z                   = 0,
        Y                   = 52760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 49430,
        Z                   = 0,
        Y                   = 47820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63060,
        Z                   = 0,
        Y                   = 49000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 68240,
        Z                   = 0,
        Y                   = 53360,
        Direction           = 180,
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
        X                   = 68240,
        Z                   = 0,
        Y                   = 51940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
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
        NpcIndex            = 0x1C1,
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


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_329",          # 01, 1
        "Function_2_32A",          # 02, 2
        "Function_3_4A7",          # 03, 3
        "Function_4_5A4",          # 04, 4
        "Function_5_6A1",          # 05, 5
        "Function_6_1113",         # 06, 6
        "Function_7_1128",         # 07, 7
        "Function_8_1151",         # 08, 8
        "Function_9_118F",         # 09, 9
        "Function_10_11CD",        # 0A, 10
        "Function_11_1231",        # 0B, 11
        "Function_12_1291",        # 0C, 12
        "Function_13_12EF",        # 0D, 13
        "Function_14_144A",        # 0E, 14
        "Function_15_157F",        # 0F, 15
        "Function_16_263E",        # 10, 16
        "Function_17_2B18",        # 11, 17
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_2CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2ED")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 15)
    Jump("loc_328")

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_30C")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_328")

    label("loc_30C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_328")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_328")

    Return()

    # Function_0_2AA end

    def Function_1_329(): pass

    label("Function_1_329")

    Return()

    # Function_1_329 end

    def Function_2_32A(): pass

    label("Function_2_32A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_491")

    label("loc_34F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_368")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_491")

    label("loc_368")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_381")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_491")

    label("loc_381")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_491")

    label("loc_39A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_491")

    label("loc_3B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_491")

    label("loc_3CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_491")

    label("loc_3E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_491")

    label("loc_3FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_417")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_491")

    label("loc_417")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_430")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_491")

    label("loc_430")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_491")

    label("loc_449")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_462")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_491")

    label("loc_462")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_491")

    label("loc_47B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_491")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_491")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_491")

    label("loc_4A6")

    Return()

    # Function_2_32A end

    def Function_3_4A7(): pass

    label("Function_3_4A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A3")
    OP_8E(0xFE, 0xF654, 0x0, 0x119F4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF2A8, 0x0, 0x12214, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEF74, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8A16, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x839A, 0x0, 0x120A2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0x11E36, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0xBC66, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8264, 0x0, 0xB414, 0x9C4, 0x0)
    OP_8E(0xFE, 0x85E8, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEB96, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF122, 0x0, 0xB1C6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF654, 0x0, 0xB874, 0x9C4, 0x0)
    Jump("Function_3_4A7")

    label("loc_5A3")

    Return()

    # Function_3_4A7 end

    def Function_4_5A4(): pass

    label("Function_4_5A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A0")
    OP_8E(0xFE, 0x8E44, 0x0, 0xB57C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88F4, 0x0, 0xB770, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0xB9DC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0x118D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88C2, 0x0, 0x11D00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8B1A, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEA06, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEE34, 0x0, 0x11CBA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0x11A62, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0xBB44, 0x7D0, 0x0)
    OP_8E(0xFE, 0xED62, 0x0, 0xB6EE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEB82, 0x0, 0xB57C, 0x7D0, 0x0)
    Jump("Function_4_5A4")

    label("loc_6A0")

    Return()

    # Function_4_5A4 end

    def Function_5_6A1(): pass

    label("Function_5_6A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(49340, 0, 59250, 0)
    OP_67(0, 19070, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(171000, 0)
    OP_6E(683, 0)
    OP_11(0xA4, 0xB7, 0xFF, 0x61A8, 0x29810, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Sleep(500)
    StopSound(0x9470, 0x14C08, 0x3A98)

    def lambda_749():
        OP_6D(46310, 0, 55980, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_749)

    def lambda_761():
        OP_67(0, 5680, -10000, 15000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_761)

    def lambda_779():
        OP_6B(2530, 15000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_779)

    def lambda_789():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_789)

    def lambda_799():
        OP_6E(380, 15000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_799)
    OP_1D(0xB)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)

    def lambda_7BA():
        OP_6D(74510, 500, 44650, 9000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_7BA)
    WaitChrThread(0x0, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_4A(0x12, 255)
    OP_4A(0x16, 255)
    Sleep(3000)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)

    def lambda_805():
        OP_6D(70000, 0, 45120, 4500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_805)
    OP_43(0x10, 0x0, 0x0, 0xB)
    OP_43(0x19, 0x0, 0x0, 0xC)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #0
        0x19,
        (
            "#5P今日您能够前来\x01",
            "真是太感谢了。\x02\x03",

            "可以的话，\x01",
            "以后还请每天都来做礼拜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "#610F呼，\x01",
            "看来我不得不这么做呢。\x02\x03",

            "如果不来的话，\x01",
            "莉拉就又要啰嗦了……\x02",
        )
    )

    Jump("loc_8D7")

    label("loc_8D7")

    CloseMessageWindow()

    ChrTalk(    #2
        0x19,
        (
            "#5P身边有这样的人\x01",
            "实在是非常幸运呢。\x02\x03",

            "能够直言不讳提出批评的人\x01",
            "才是理想的伙伴啊。\x02\x03",

            "不过，真是太好了……\x01",
            "莉拉小姐也完全康复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "#610F嗯，是的……\x02\x03",

            "超市恢复了往日的熙攘，\x01",
            "空中的浮游都市也消失了……\x02\x03",

            "这下一切都恢复原状了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x19,
        (
            "#5P让我们共同向女神祈祷，\x01",
            "希望这和平的日子能持续下去吧。\x02\x03",

            "……我们随时恭候您的到来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        "#610F替我向神父大人问个好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x19,
        "#5P好的，再见。\x02",
    )

    CloseMessageWindow()
    OP_43(0x19, 0x0, 0x0, 0xA)
    WaitChrThread(0x19, 0x0)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    Sleep(300)
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #7
        0x10,
        (
            "#610F#5P接下来……\x02\x03",

            "要不要去\x01",
            "视察一下超市呢。\x02",
        )
    )

    Jump("loc_ADA")

    label("loc_ADA")

    CloseMessageWindow()
    Sleep(300)

    def lambda_AE6():
        OP_6D(67100, 0, 45120, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_AE6)
    OP_8E(0x10, 0xFC39, 0x0, 0xAF6E, 0x7D0, 0x0)
    WaitChrThread(0x10, 0x0)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    OP_8C(0x10, 0, 400)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #8
        0x10,
        "#610F#5P哎呀，那是……\x02",
    )

    CloseMessageWindow()

    def lambda_B5D():
        OP_6D(62800, 0, 61880, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_B5D)

    def lambda_B75():
        OP_67(0, 4950, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B75)

    def lambda_B8D():
        OP_6B(2360, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B8D)

    def lambda_B9D():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_B9D)

    def lambda_BAD():
        OP_6E(392, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_BAD)
    Sleep(2000)
    OP_43(0x11, 0x0, 0x0, 0x9)
    OP_43(0x1A, 0x0, 0x0, 0x8)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x1A, 0x0)
    WaitChrThread(0x0, 0x0)
    Sleep(300)
    SetChrPos(0x10, 69740, 0, 46480, 0)

    NpcTalk(    #9
        0x1A,
        "给人以好印象的青年",
        (
            "#5P谢谢。\x01",
            "今天真是开心。\x02",
        )
    )

    Jump("loc_C2A")

    label("loc_C2A")

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "#620F哪里，彼此彼此……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x1A,
        "给人以好印象的青年",
        (
            "#5P以后再联络哦。\x02\x03",

            "我妹妹\x01",
            "也非常期待呢。\x02",
        )
    )

    Jump("loc_C97")

    label("loc_C97")

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#620F好，一定。\x02\x03",

            "那么，我差不多该走了……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x1A,
        "给人以好印象的青年",
        (
            "#5P哦……\x01",
            "礼拜时间已经结束了吗。\x02\x03",

            "……那就回头见吧。\x02",
        )
    )

    Jump("loc_D24")

    label("loc_D24")

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        "#620F嗯，告辞了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x1A, 0, 400)
    Sleep(200)

    def lambda_D55():
        OP_8E(0xFE, 0xF51E, 0x0, 0x11332, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_D55)
    Sleep(3000)
    Fade(500)
    OP_6D(70600, 0, 47820, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(1880, 0)
    OP_6C(45000, 0)
    OP_6E(392, 0)
    OP_0D()
    Sleep(300)
    OP_44(0x1A, 0x0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x1A, 0x80)

    ChrTalk(    #15
        0x10,
        (
            "#610F#5P刚、刚才的男人是……\x02\x03",

            "………………………\x02\x03",

            "对啊……\x01",
            "莉拉也正值当年呢。\x02\x03",

            "嗯，虽然态度很冷淡，\x01",
            "不过气质和才干都很不错。\x02\x03",

            "没有那种流言，\x01",
            "反倒觉得不可思议呢。\x02\x03",

            "虽然觉得有点寂寞……\x01",
            "不过，我应该支持她才对。\x02",
        )
    )

    Jump("loc_EB1")

    label("loc_EB1")

    CloseMessageWindow()

    def lambda_EB8():
        OP_6D(68530, 0, 47650, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_EB8)

    def lambda_ED0():
        OP_67(0, 8770, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_ED0)

    def lambda_EE8():
        OP_6B(1780, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_EE8)
    SetChrPos(0x11, 63970, 0, 53590, 180)

    def lambda_F09():
        OP_8E(0xFE, 0x10040, 0x0, 0xB61C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F09)
    WaitChrThread(0x11, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(600)
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #16
        0x11,
        (
            "#620F#6P小姐……\x02\x03",

            "您在这种地方干什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_FAA():
        OP_8F(0xFE, 0x1108A, 0x0, 0xB432, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_FAA)
    OP_8C(0x10, 270, 500)
    WaitChrThread(0x10, 0x0)
    Sleep(200)

    ChrTalk(    #17
        0x10,
        (
            "#610F哎、哎呀……莉拉。\x02\x03",

            "你、你什么时候站在这里的？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #18
        0x11,
        (
            "#620F……………………………\x02\x03",

            "看上去，\x01",
            "您好像非常疲劳呢。\x02\x03",

            "我已经那样叮嘱过您，\x01",
            "不能勉强行事了。\x02",
        )
    )

    Jump("loc_1088")

    label("loc_1088")

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#610F不不，我没事。\x02\x03",

            "好了，快去超市吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        "#620F哦……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x10, 0x0, 0x0, 0x7)

    def lambda_10DF():

        label("loc_10DF")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_10DF")

    QueueWorkItem2(0x11, 0, lambda_10DF)
    Sleep(3000)
    OP_43(0x11, 0x0, 0x0, 0x6)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T1111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_6A1 end

    def Function_6_1113(): pass

    label("Function_6_1113")

    OP_8E(0xFE, 0xF730, 0x0, 0xE74A, 0x7D0, 0x0)
    Return()

    # Function_6_1113 end

    def Function_7_1128(): pass

    label("Function_7_1128")

    OP_8F(0xFE, 0xFDA2, 0x0, 0xBAF4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF730, 0x0, 0xE74A, 0x7D0, 0x0)
    Return()

    # Function_7_1128 end

    def Function_8_1151(): pass

    label("Function_8_1151")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 58570, 0, 60450, 90)

    def lambda_116D():
        OP_8E(0xFE, 0xF51E, 0x0, 0xEC22, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_116D)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_8_1151 end

    def Function_9_118F(): pass

    label("Function_9_118F")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 58390, 0, 58930, 90)

    def lambda_11AB():
        OP_8E(0xFE, 0xF51E, 0x0, 0xE54C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11AB)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_9_118F end

    def Function_10_11CD(): pass

    label("Function_10_11CD")

    OP_8C(0xFE, 90, 400)

    def lambda_11DA():
        OP_8E(0xFE, 0x11D5A, 0x1F4, 0xADDE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11DA)
    WaitChrThread(0xFE, 0x2)

    def lambda_11FA():
        OP_8E(0xFE, 0x120E8, 0x1F4, 0xADE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11FA)

    def lambda_1215():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1215)
    WaitChrThread(0xFE, 0x2)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_11CD end

    def Function_11_1231(): pass

    label("Function_11_1231")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 74570, 500, 44500, 270)

    def lambda_1258():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1258)

    def lambda_126A():
        OP_8E(0xFE, 0x10658, 0x0, 0xAF6E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_126A)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_11_1231 end

    def Function_12_1291(): pass

    label("Function_12_1291")

    Sleep(900)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 74570, 500, 44500, 270)

    def lambda_12BD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12BD)

    def lambda_12CF():
        OP_8E(0xFE, 0x110A8, 0x0, 0xAFAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12CF)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_12_1291 end

    def Function_13_12EF(): pass

    label("Function_13_12EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(22300, 0, 55980, 0)
    OP_67(0, 9330, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(212000, 0)
    OP_6E(405, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05过了几天――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    def lambda_13A4():
        OP_6D(19230, 0, 57650, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_13A4)

    def lambda_13BC():
        OP_67(0, 7970, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_13BC)

    def lambda_13D4():
        OP_6B(3040, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_13D4)

    def lambda_13E4():
        OP_6C(270000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_13E4)

    def lambda_13F4():
        OP_6E(372, 6000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_13F4)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)

    def lambda_1413():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1413)

    def lambda_1423():
        OP_6E(355, 2000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1423)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2507)
    NewScene("ED6_DT21/T1111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_12EF end

    def Function_14_144A(): pass

    label("Function_14_144A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(48000, 0, 60000, 0)
    OP_67(0, 18700, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(45000, 0)
    OP_6E(746, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_C8(0x200, 0x46, "C_PLAC15._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_14EE():
        OP_6D(59000, 0, 84600, 9000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_14EE)

    def lambda_1506():
        OP_67(0, 6000, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1506)

    def lambda_151E():
        OP_6B(2000, 9000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_151E)

    def lambda_152E():
        OP_6E(616, 9000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_152E)

    def lambda_153E():
        OP_6C(0, 9000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_153E)
    WaitChrThread(0x1C, 0x0)
    Sleep(500)

    def lambda_1558():
        OP_6B(1900, 3000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_1558)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_144A end

    def Function_15_157F(): pass

    label("Function_15_157F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(49340, 0, 59250, 0)
    OP_67(0, 19070, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(171000, 0)
    OP_6E(683, 0)
    OP_11(0xA4, 0xB7, 0xFF, 0x61A8, 0x29810, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    StopSound(0x9470, 0x14C08, 0x3A98)

    def lambda_1622():
        OP_6D(46310, 0, 55980, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1622)

    def lambda_163A():
        OP_67(0, 5680, -10000, 15000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_163A)

    def lambda_1652():
        OP_6B(2530, 15000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1652)

    def lambda_1662():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1662)

    def lambda_1672():
        OP_6E(380, 15000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1672)
    OP_C8(0x200, 0x46, "C_PLAC15._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)

    def lambda_16A6():
        OP_6D(74510, 500, 44650, 9000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_16A6)
    WaitChrThread(0x0, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_4A(0x12, 255)
    OP_4A(0x16, 255)
    Sleep(3000)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)

    def lambda_16F1():
        OP_6D(70000, 0, 45120, 4500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_16F1)
    OP_43(0x10, 0x0, 0x0, 0xB)
    OP_43(0x19, 0x0, 0x0, 0xC)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #22
        0x19,
        (
            "#5P今日您能够前来\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x19,
        (
            "可以的话，\x01",
            "以后还请尽量\x01",
            "每天都来做礼拜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#615F#6P呼，请不用担心，\x01",
            "我也不得不这么做呢。\x02\x03",

            "#610F如果不来的话，\x01",
            "莉拉就又要啰嗦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x19,
        (
            "#5P呵呵，\x01",
            "身边有这样的人\x01",
            "实在是非常幸运呢。\x02",
        )
    )

    Jump("loc_182A")

    label("loc_182A")

    CloseMessageWindow()

    ChrTalk(    #26
        0x19,
        (
            "#5P能够直言不讳提出批评的人\x01",
            "才是最珍贵的伙伴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#610F#6P嗯嗯，\x01",
            "我也这么想。\x02\x03",

            "#618F只是……\x01",
            "就算稍微偷下懒，\x01",
            "也不会遭报应的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x19,
        (
            "#5P呵呵，\x01",
            "这是她将梅贝尔小姐\x01",
            "放在心中最重要位置的证据啊。\x02",
        )
    )

    Jump("loc_1916")

    label("loc_1916")

    CloseMessageWindow()

    ChrTalk(    #29
        0x19,
        (
            "#5P听说您最近一直忙于工作，\x01",
            "非常辛苦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x19,
        (
            "#5P换种角度来看，\x01",
            "做礼拜也是一种不错的休息方式，\x01",
            "这大概就是莉拉小姐的想法吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#617F#6P嗯，虽然有点不甘心，\x01",
            "不过的确有这种感觉。\x02\x03",

            "#610F……唉，这个暂且不提，\x01",
            "今天我就先告辞了。\x02\x03",

            "也请替我向\x01",
            "教区长大人问个好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x19,
        (
            "#5P呵呵，明白了。\x01",
            "那么，请保重。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x19, 0x0, 0x0, 0xA)
    WaitChrThread(0x19, 0x0)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    Sleep(300)
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #33
        0x10,
        (
            "#615F#5P呼，\x01",
            "最近修女也总和莉拉说一样的话呢。\x02\x03",

            "#610F好了，\x01",
            "接下来是超市的视察……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 315, 400)
    Sleep(800)
    OP_8C(0x10, 225, 400)
    Sleep(800)
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #34
        0x10,
        (
            "#615F#5P莉拉怎么还没来接我呢。\x02\x03",

            "#618F话说回来……\x01",
            "最近莉拉好像有点冷淡呢。\x02\x03",

            "今天也是，\x01",
            "以买东西为由不陪我做礼拜……\x02\x03",

            "#610F也罢，\x01",
            "这些原因以后直接去问本人吧……\x02\x03",

            "先去超市好了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1C0D():
        OP_6D(67100, 0, 45120, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1C0D)
    OP_8E(0x10, 0xFC39, 0x0, 0xAF6E, 0x7D0, 0x0)
    WaitChrThread(0x10, 0x0)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 0, 400)
    WaitChrThread(0x0, 0x0)
    Sleep(300)

    ChrTalk(    #35
        0x10,
        "#613F#11P哎呀，那是……\x02",
    )

    CloseMessageWindow()

    def lambda_1C8F():
        OP_6D(62800, 0, 61880, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1C8F)

    def lambda_1CA7():
        OP_67(0, 4950, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1CA7)

    def lambda_1CBF():
        OP_6B(2360, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1CBF)

    def lambda_1CCF():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1CCF)

    def lambda_1CDF():
        OP_6E(392, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1CDF)
    Sleep(2000)
    OP_43(0x11, 0x0, 0x0, 0x9)
    OP_43(0x1A, 0x0, 0x0, 0x8)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x1A, 0x0)
    WaitChrThread(0x0, 0x0)
    Sleep(300)
    SetChrPos(0x10, 69740, 0, 46480, 0)

    NpcTalk(    #36
        0x1A,
        "给人以好印象的青年",
        (
            "#5P谢谢。\x01",
            "今天真是帮大忙了。\x02",
        )
    )

    Jump("loc_1D65")

    label("loc_1D65")

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        "#620F#6P哪里，彼此彼此……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0x1A,
        "给人以好印象的青年",
        (
            "#5P那就这样吧，\x01",
            "以后随时都可以联络我。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #39
        0x1A,
        "给人以好印象的青年",
        (
            "#5P至于日程，\x01",
            "应该能配合你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        "#620F#6P好的，近日一定联络。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #41
        0x1A,
        "给人以好印象的青年",
        (
            "#5P嗯，\x01",
            "我妹妹也很有干劲呢。\x02",
        )
    )

    Jump("loc_1E7B")

    label("loc_1E7B")

    CloseMessageWindow()
    CloseMessageWindow()

    NpcTalk(    #42
        0x1A,
        "给人以好印象的青年",
        (
            "#5P敬请期待\x01",
            "当天的招待吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x11,
        (
            "#621F呵呵，好啊。\x02\x03",

            "那么，我差不多该走了……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #44
        0x1A,
        "给人以好印象的青年",
        (
            "#5P是吗，\x01",
            "市长礼拜的时间该结束了吧。\x02",
        )
    )

    Jump("loc_1F42")

    label("loc_1F42")

    CloseMessageWindow()

    NpcTalk(    #45
        0x1A,
        "给人以好印象的青年",
        "#5P……那么，回头见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        "#620F好的，告辞了。（点头）\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x1A, 0, 400)
    Sleep(200)

    def lambda_1FB7():
        OP_8E(0xFE, 0xF51E, 0x0, 0x11332, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1FB7)
    Sleep(3000)
    Fade(500)
    OP_6D(70600, 0, 47820, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(1880, 0)
    OP_6C(45000, 0)
    OP_6E(392, 0)
    OP_0D()
    OP_44(0x1A, 0x0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x1A, 0x80)
    Sleep(500)

    ChrTalk(    #47
        0x10,
        "#613F#12P刚、刚才的男人难道是………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #48
        0x10,
        (
            "#615F#12P是吗……\x01",
            "最近她那么冷淡\x01",
            "就是因为这个啊。\x02\x03",

            "#618F跟我说一声不就好了……\x01",
            "莉拉真是见外呢。\x02\x03",

            "………………………………\x02\x03",

            "#610F不过，也是啊……\x01",
            "莉拉也是到该谈婚论嫁的年龄了……\x02\x03",

            "嗯，虽然态度很冷淡，\x01",
            "不过气质和才干都很不错。\x02\x03",

            "至今为止\x01",
            "都没有那种绯闻，\x01",
            "反倒觉得不可思议呢。\x02\x03",

            "#617F……………嗯，对了。\x02\x03",

            "#611F虽然觉得有点寂寞……\x01",
            "不过我应该支持她才对。\x02",
        )
    )

    Jump("loc_2220")

    label("loc_2220")

    CloseMessageWindow()

    def lambda_2227():
        OP_6D(68530, 0, 47650, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2227)

    def lambda_223F():
        OP_67(0, 8770, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_223F)

    def lambda_2257():
        OP_6B(1780, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2257)
    SetChrPos(0x11, 63970, 0, 53590, 180)

    def lambda_2278():
        OP_8E(0xFE, 0x10040, 0x0, 0xB61C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2278)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #49
        0x11,
        "#623F#5P呼，稍微迟到了点……\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #50
        0x11,
        (
            "#622F#6P小姐……\x02\x03",

            "您在这种地方干什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2351():
        OP_8F(0xFE, 0x1108A, 0x0, 0xB432, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2351)
    OP_8C(0x10, 270, 500)
    WaitChrThread(0x10, 0x0)
    Sleep(300)

    ChrTalk(    #51
        0x10,
        (
            "#613F#11P哎、哎呀……这不是莉拉吗。\x02\x03",

            "#617F你、你什么时候到这里的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x11,
        (
            "#622F#6P……………………………\x02\x03",

            "#625F看起来，\x01",
            "您好像非常疲劳呢。\x02\x03",

            "我已经那样叮嘱过您，\x01",
            "不能勉强行事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "#617F#11P不不，不用担心。\x02\x03",

            "#611F好了，快去超市吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        "#622F#6P哦……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_24BB():
        OP_6D(65000, 0, 55000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_24BB)

    def lambda_24D3():
        OP_6C(33000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_24D3)
    OP_43(0x10, 0x0, 0x0, 0x7)

    def lambda_24EA():

        label("loc_24EA")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_24EA")

    QueueWorkItem2(0x11, 0, lambda_24EA)
    Sleep(3000)
    OP_43(0x11, 0x0, 0x0, 0x6)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x00第二天――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(30640, 0, 75000, 0)
    OP_67(0, 12800, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(270000, 0)
    OP_6E(502, 0)

    def lambda_25A0():
        OP_6D(55060, 0, 75000, 6000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_25A0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x1C, 0x0)

    def lambda_25C7():
        OP_6D(55060, 0, 84540, 5000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_25C7)

    def lambda_25DF():
        OP_67(0, 5500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_25DF)

    def lambda_25F7():
        OP_6B(2600, 5000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_25F7)

    def lambda_2607():
        OP_6E(482, 5000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_2607)

    def lambda_2617():
        OP_6C(320000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2617)
    WaitChrThread(0x1C, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_157F end

    def Function_16_263E(): pass

    label("Function_16_263E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(36790, 0, 69390, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1B, 0x80)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    SetChrPos(0x13, 36000, 0, 70120, 225)
    SetChrPos(0x14, 36000, 0, 68660, 315)
    SetChrPos(0x1B, 34300, 0, 69390, 90)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #56 op#A
        "\x07\x00#15A#4S证言②\x18\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0x14,
        "#11P嗯嗯，我确实看到了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x14,
        (
            "#11P有个男人\x01",
            "把女佣小姐送到了\x01",
            "市长家的门口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x13,
        (
            "#5P不过，\x01",
            "要是稍微进去坐坐就更好了。\x02",
        )
    )

    Jump("loc_27D4")

    label("loc_27D4")

    CloseMessageWindow()

    ChrTalk(    #60
        0x13,
        (
            "#5P我送米娜回家的时候\x01",
            "总是这样的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x14,
        "#11P……………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 0, 400)
    Sleep(300)

    ChrTalk(    #62
        0x14,
        "#2P……唉，哈里。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x14,
        (
            "#2P这种情况下，\x01",
            "是你做的不对哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x13, 180, 400)

    ChrTalk(    #64
        0x13,
        "#1P咦？\x02",
    )

    Jump("loc_28BB")

    label("loc_28BB")

    CloseMessageWindow()

    ChrTalk(    #65
        0x14,
        (
            "#2P绅士送淑女回家的时候，\x01",
            "一般都不会进去的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x13,
        "#1P是吗？\x02",
    )

    Jump("loc_2913")

    label("loc_2913")

    CloseMessageWindow()

    ChrTalk(    #67
        0x14,
        "#2P是啊。\x02",
    )

    Jump("loc_2931")

    label("loc_2931")

    CloseMessageWindow()

    ChrTalk(    #68
        0x13,
        (
            "#1P但、但是，\x01",
            "这就说明我和米娜\x01",
            "关系很好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x14,
        "#2P这个，谁知道呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x14,
        (
            "#2P女佣小姐他们\x01",
            "看起来关系也很好的样子。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #71
        0x13,
        "#1P……（消沉）。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x14,
        (
            "#2P……哎呀，\x01",
            "我也不是说\x01",
            "以后就不能进家里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x14,
        "#2P和以前一样不就好了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x13,
        "#1P米、米娜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x13,
        "#1P嗯、嗯，就这么办啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x14,
        (
            "#2P（呼，\x01",
            "　这人还真是麻烦……）\x02",
        )
    )

    Jump("loc_2AC3")

    label("loc_2AC3")

    CloseMessageWindow()

    ChrTalk(    #77
        0x1B,
        (
            "#819F#6P啊哈哈……\x01",
            "谢谢你们提供情报。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_263E end

    def Function_17_2B18(): pass

    label("Function_17_2B18")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(22300, 0, 55980, 0)
    OP_67(0, 9330, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(212000, 0)
    OP_6E(405, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #78
        "\x07\x00#40W几天后――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_1D(0xB)

    def lambda_2BE2():
        OP_6D(19230, 0, 57650, 6000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_2BE2)

    def lambda_2BFA():
        OP_67(0, 7970, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2BFA)

    def lambda_2C12():
        OP_6B(3040, 6000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2C12)

    def lambda_2C22():
        OP_6C(270000, 6000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_2C22)

    def lambda_2C32():
        OP_6E(372, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2C32)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x1C, 0x0)
    Sleep(500)

    def lambda_2C56():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_2C56)

    def lambda_2C66():
        OP_6E(355, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2C66)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T1111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2B18 end

    SaveToFile()

Try(main)
