from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0705   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0705.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        '怪盗布卢布兰',                         # 9
        '跳梁小丑',                             # 10
        '跳梁小丑',                             # 11
        '福音',                                 # 12
        '幻惑之铃露茜奥拉',                     # 13
        '瘦狼瓦鲁特',                           # 14
        '小丑肯帕雷拉',                         # 15
        '红色飞艇',                             # 16
        '红色飞艇的踪影',                       # 17
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
        'ED6_DT27/CH03530 ._CH',             # 00
        'ED6_DT29/CH12160 ._CH',             # 01
        'ED6_DT27/CH04530 ._CH',             # 02
        'ED6_DT27/CH04000 ._CH',             # 03
        'ED6_DT27/CH04001 ._CH',             # 04
        'ED6_DT27/CH04010 ._CH',             # 05
        'ED6_DT27/CH04011 ._CH',             # 06
        'ED6_DT06/CH20021 ._CH',             # 07
        'ED6_DT29/CH12161 ._CH',             # 08
        'ED6_DT26/CH20273 ._CH',             # 09
        'ED6_DT27/CH03520 ._CH',             # 0A
        'ED6_DT27/CH03500 ._CH',             # 0B
        'ED6_DT27/CH03600 ._CH',             # 0C
        'ED6_DT26/CH20431 ._CH',             # 0D
        'ED6_DT27/CH03500 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT27/CH03530P._CP',             # 00
        'ED6_DT29/CH12160P._CP',             # 01
        'ED6_DT27/CH04530P._CP',             # 02
        'ED6_DT27/CH04000P._CP',             # 03
        'ED6_DT27/CH04001P._CP',             # 04
        'ED6_DT27/CH04010P._CP',             # 05
        'ED6_DT27/CH04011P._CP',             # 06
        'ED6_DT06/CH20021P._CP',             # 07
        'ED6_DT29/CH12161P._CP',             # 08
        'ED6_DT26/CH20273P._CP',             # 09
        'ED6_DT27/CH03520P._CP',             # 0A
        'ED6_DT27/CH03500P._CP',             # 0B
        'ED6_DT27/CH03600P._CP',             # 0C
        'ED6_DT26/CH20431P._CP',             # 0D
        'ED6_DT27/CH03500P._CP',             # 0E
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458759,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        NpcIndex            = 0x180,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_2B9",          # 01, 1
        "Function_2_2E0",          # 02, 2
        "Function_3_45D",          # 03, 3
        "Function_4_B66",          # 04, 4
        "Function_5_B9A",          # 05, 5
        "Function_6_BCA",          # 06, 6
        "Function_7_C38",          # 07, 7
        "Function_8_C92",          # 08, 8
        "Function_9_E3C",          # 09, 9
        "Function_10_10F9",        # 0A, 10
        "Function_11_1102",        # 0B, 11
        "Function_12_2994",        # 0C, 12
        "Function_13_2F04",        # 0D, 13
        "Function_14_2F8B",        # 0E, 14
    )


    def Function_0_242(): pass

    label("Function_0_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_261")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_2B8")

    label("loc_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_280")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)
    Jump("loc_2B8")

    label("loc_280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_29F")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_2B8")

    label("loc_29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 5)), scpexpr(EXPR_END)), "loc_2B8")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_2B8")

    Return()

    # Function_0_242 end

    def Function_1_2B9(): pass

    label("Function_1_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CA")
    OP_22(0xEB, 0x1, 0x50)

    label("loc_2CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x454), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DF")

    Return()

    # Function_1_2B9 end

    def Function_2_2E0(): pass

    label("Function_2_2E0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_305")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_447")

    label("loc_305")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_447")

    label("loc_31E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_337")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_447")

    label("loc_337")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_350")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_447")

    label("loc_350")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_447")

    label("loc_369")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_447")

    label("loc_382")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_447")

    label("loc_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_447")

    label("loc_3B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_447")

    label("loc_3CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_447")

    label("loc_3E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_447")

    label("loc_3FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_418")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_447")

    label("loc_418")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_431")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_447")

    label("loc_431")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_447")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_447")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_447")

    label("loc_45C")

    Return()

    # Function_2_2E0 end

    def Function_3_45D(): pass

    label("Function_3_45D")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_82(0x80, 0x0)
    OP_71(0x9, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    OP_6D(40, 0, 35830, 0)
    OP_67(0, 7740, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(297, 0)
    SetChrPos(0xC, 40, 0, -7480, 0)
    ClearChrFlags(0xC, 0x80)
    OP_22(0x1C3, 0x0, 0x64)
    FadeToBright(2000, 0)

    def lambda_510():
        OP_6D(40, 0, 0, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_510)
    Sleep(5000)
    OP_8E(0xC, 0x28, 0x0, 0x0, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0xC,
        (
            "#240F『翡翠之塔』──\x01",
            "看来和报告一样呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_57E():
        OP_6D(370, 0, 9730, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57E)

    def lambda_596():
        OP_6B(3000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_596)

    def lambda_5A6():
        OP_67(0, 6900, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5A6)
    OP_8E(0xC, 0xA0, 0x0, 0x2026, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #1
        0xC,
        (
            "#244F和王城封印区域有密切关联的\x01",
            "『设备塔』的一角……\x02\x03",

            "利用了表里两面的『第二结界』……\x02\x03",

            "#241F呵呵，教授也调查得够仔细的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x10, 0x7)
    SetChrPos(0x10, -25390, 1500, 11620, 180)
    OP_72(0x7, 0x4)
    OP_22(0x79, 0x1, 0x46)
    Sleep(1000)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_24(0x79, 0x50)
    Sleep(1000)

    def lambda_69B():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_69B)
    OP_24(0x79, 0x55)
    Sleep(1000)

    def lambda_6B2():

        label("loc_6B2")

        TurnDirection(0xFE, 0x10, 100)
        OP_48()
        Jump("loc_6B2")

    QueueWorkItem2(0xC, 1, lambda_6B2)
    OP_24(0x79, 0x5A)

    def lambda_6C7():
        OP_8E(0xFE, 0x5244, 0x5DC, 0x2B7A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6C7)
    Sleep(1000)
    OP_24(0x79, 0x5F)
    Sleep(1000)
    OP_24(0x79, 0x64)
    WaitChrThread(0x10, 0x1)
    OP_44(0xC, 0x1)
    Fade(500)
    OP_6D(15450, 0, 9560, 0)
    OP_67(0, 8440, -10000, 0)
    OP_6B(4120, 0)
    OP_6C(45000, 0)
    OP_6E(433, 0)
    OP_71(0x7, 0x4)
    OP_A1(0xF, 0x8)
    SetChrPos(0xF, 18810, 5000, 10000, 90)
    OP_72(0x8, 0x4)
    OP_B0(0x8, 0x14)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 830)
    OP_70(0x8, 0x352)

    def lambda_776():
        OP_6D(19500, 250, 8310, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_776)

    def lambda_78E():
        OP_67(0, 6470, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_78E)

    def lambda_7A6():
        OP_6B(3380, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7A6)

    def lambda_7B6():
        OP_6E(364, 10000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7B6)

    def lambda_7C6():
        OP_8F(0xF, 0x5532, 0xFFFFFC18, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_7C6)

    def lambda_7E1():
        OP_8C(0xF, 0, 10)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7E1)
    Sleep(1000)

    def lambda_7F4():
        OP_8F(0xF, 0x5532, 0xFFFFFC18, 0x2710, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_7F4)

    def lambda_80F():
        OP_8C(0xF, 0, 12)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_80F)
    Sleep(1000)

    def lambda_822():
        OP_8F(0xF, 0x5532, 0xFFFFFC18, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_822)

    def lambda_83D():
        OP_8C(0xF, 0, 15)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_83D)
    Sleep(1000)

    def lambda_850():
        OP_8F(0xF, 0x5532, 0xFFFFFC18, 0x2710, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_850)

    def lambda_86B():
        OP_8C(0xF, 0, 12)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_86B)
    Sleep(1500)

    def lambda_87E():
        OP_8C(0xF, 0, 10)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_87E)

    def lambda_88C():
        OP_8F(0xF, 0x5532, 0xFFFFFC18, 0x2710, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_88C)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0xF, 0x1)
    OP_43(0xC, 0x0, 0x0, 0x5)
    OP_72(0x8, 0x20)
    OP_D8(0x8, 0x12C)
    OP_6F(0x8, 1220)
    OP_70(0x8, 0x50A)
    Sleep(1000)
    OP_22(0xFD, 0x0, 0x64)
    OP_73(0x8)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 1290)
    OP_70(0x8, 0x51D)
    OP_48()
    Sleep(100)
    OP_43(0xE, 0x0, 0x0, 0x7)
    Sleep(800)
    OP_43(0xD, 0x0, 0x0, 0x6)
    Sleep(1500)
    OP_43(0xF, 0x0, 0x0, 0x4)
    WaitChrThread(0xD, 0x0)
    Sleep(200)

    ChrTalk(    #2
        0xD,
        "#252F#2P哟，久等了。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x0)

    ChrTalk(    #3
        0xE,
        "#851F#5P呵呵，辛苦了。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0x0)

    ChrTalk(    #4
        0xC,
        (
            "#243F#6P哎呀……\x01",
            "你们竟然会来。\x02\x03",

            "#240F我还以为\x01",
            "会是莱维过来接我呢。\x02\x03",

            "今天刮的什么风？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xE,
        (
            "#850F#5P呵呵，莱维\x01",
            "正在陪着教授呢。\x02\x03",

            "所以就改由我们\x01",
            "来迎接你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xD,
        (
            "#250F#2P反正到下一阶段之前\x01",
            "也没什么好做的了。\x02\x03",

            "就当是来消磨时间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xC,
        (
            "#241F#6P呵呵，说得倒轻巧。\x02\x03",

            "不过教授和莱维\x01",
            "既然在一起……\x02\x03",

            "这么说终于要进行\x01",
            "最后的试验了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        (
            "#252F#2P呼呼，好像是。\x02\x03",

            "『福音计划』也\x01",
            "终于到下一阶段了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xE,
        (
            "#853F#5P人偶和猎兵的准备也很顺利。\x02\x03",

            "#850F这样一来，如果『β』完成了，\x01",
            "我看就会变得非常忙碌了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_45D end

    def Function_4_B66(): pass

    label("Function_4_B66")

    OP_72(0x8, 0x20)
    OP_6F(0x8, 1300)
    OP_70(0x8, 0x564)
    Sleep(500)
    OP_22(0xFD, 0x0, 0x64)
    OP_73(0x8)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 800)
    OP_70(0x8, 0x384)
    Return()

    # Function_4_B66 end

    def Function_5_B9A(): pass

    label("Function_5_B9A")

    OP_8E(0xFE, 0x1B44, 0xFA, 0x2602, 0xBB8, 0x0)
    OP_8E(0xFE, 0x35F2, 0xFA, 0x191E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_B9A end

    def Function_6_BCA(): pass

    label("Function_6_BCA")

    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    OP_89(0xFE, 21840, 2300, 9970, 0)
    OP_8E(0xFE, 0x5532, 0x8FC, 0x1DBA, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x4B78, 0x938, 0x1A9A, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_BCA end

    def Function_7_C38(): pass

    label("Function_7_C38")

    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    OP_89(0xFE, 21840, 2300, 9970, 0)
    OP_8E(0xFE, 0x5532, 0x8FC, 0x1DBA, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x497A, 0x92E, 0x1D92, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_7_C38 end

    def Function_8_C92(): pass

    label("Function_8_C92")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(60, 0, -2000, 0)
    OP_67(0, 8910, -10000, 0)
    OP_6B(4370, 0)
    OP_6C(21000, 0)
    OP_6E(254, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 4059, 3450, 6990, 315)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x1)
    OP_82(0x80, 0x0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(1000)

    def lambda_D50():
        OP_6D(520, 0, 12220, 4000)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_D50)
    OP_C8(0x200, 0x46, "C_PLAC19._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    WaitChrThread(0xB, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_6D(1400, 0, 14000, 0)
    OP_67(0, 6630, -10000, 0)
    OP_6B(2029, 0)
    OP_6C(9000, 0)
    OP_6E(507, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #10
        0x8,
        (
            "#231F#8P──这里是『怪盗绅士』。\x02\x03",

            "设置完成了。\x01",
            "仪式开始之前会在此待命。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3605   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_C92 end

    def Function_9_E3C(): pass

    label("Function_9_E3C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(1220, 950, 14960, 0)
    OP_67(0, 8600, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(408, 0)
    SetChrPos(0x8, 40, 950, 12620, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 4059, 3450, 6990, 315)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x1)
    OP_82(0x80, 0x0)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_6F(0x0, 60)
    OP_6F(0x1, 60)
    OP_6F(0x2, 60)
    OP_6F(0x3, 60)
    OP_6F(0x4, 60)
    OP_70(0x0, 0x3C)
    OP_70(0x1, 0x3C)
    OP_70(0x2, 0x3C)
    OP_70(0x3, 0x3C)
    LoadEffect(0x1, "map\\\\mp061_00.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_B0(0x0, 0x50)
    OP_B0(0x1, 0x50)
    OP_B0(0x2, 0x50)
    OP_B0(0x3, 0x50)
    OP_B0(0x4, 0x50)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)
    OP_73(0x2)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)
    OP_73(0x4)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_79(0x0, 0x1)
    OP_79(0x1, 0x1)
    OP_79(0x2, 0x1)
    OP_79(0x3, 0x1)
    OP_79(0x4, 0x1)
    OP_7B()
    Fade(1000)
    OP_11(0xA0, 0xB4, 0xFF, 0x17ED0, 0x38E28, 0x0)
    OP_6D(-32090, 30000, -26260, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp049_03.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -32090, 30000, -26260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    Sleep(3000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C3605   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_E3C end

    def Function_10_10F9(): pass

    label("Function_10_10F9")

    Call(0, 11)
    Call(0, 12)
    Return()

    # Function_10_10F9 end

    def Function_11_1102(): pass

    label("Function_11_1102")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1119")
    Call(0, 13)
    Call(0, 14)

    label("loc_1119")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_113A"),
        (5, "loc_1151"),
        (4, "loc_1168"),
        (6, "loc_117F"),
        (7, "loc_1196"),
        (8, "loc_11AD"),
        (SWITCH_DEFAULT, "loc_11C4"),
    )


    label("loc_113A")

    OP_D2(0x701D0, 0x701DC, 0xF)
    OP_D2(0x701D1, 0x701DD, 0x10)
    Jump("loc_11C4")

    label("loc_1151")

    OP_D2(0x70218, 0x70224, 0xF)
    OP_D2(0x70219, 0x70225, 0x10)
    Jump("loc_11C4")

    label("loc_1168")

    OP_D2(0x70200, 0x7020C, 0xF)
    OP_D2(0x70201, 0x7020D, 0x10)
    Jump("loc_11C4")

    label("loc_117F")

    OP_D2(0x70230, 0x7023C, 0xF)
    OP_D2(0x70231, 0x7023D, 0x10)
    Jump("loc_11C4")

    label("loc_1196")

    OP_D2(0x70248, 0x70254, 0xF)
    OP_D2(0x70249, 0x70255, 0x10)
    Jump("loc_11C4")

    label("loc_11AD")

    OP_D2(0x270176, 0x270183, 0xF)
    OP_D2(0x270177, 0x270184, 0x10)
    Jump("loc_11C4")

    label("loc_11C4")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_11E5"),
        (5, "loc_11FC"),
        (4, "loc_1213"),
        (6, "loc_122A"),
        (7, "loc_1241"),
        (8, "loc_1258"),
        (SWITCH_DEFAULT, "loc_126F"),
    )


    label("loc_11E5")

    OP_D2(0x701D0, 0x701DC, 0x11)
    OP_D2(0x701D1, 0x701DD, 0x12)
    Jump("loc_126F")

    label("loc_11FC")

    OP_D2(0x70218, 0x70224, 0x11)
    OP_D2(0x70219, 0x70225, 0x12)
    Jump("loc_126F")

    label("loc_1213")

    OP_D2(0x70200, 0x7020C, 0x11)
    OP_D2(0x70201, 0x7020D, 0x12)
    Jump("loc_126F")

    label("loc_122A")

    OP_D2(0x70230, 0x7023C, 0x11)
    OP_D2(0x70231, 0x7023D, 0x12)
    Jump("loc_126F")

    label("loc_1241")

    OP_D2(0x70248, 0x70254, 0x11)
    OP_D2(0x70249, 0x70255, 0x12)
    Jump("loc_126F")

    label("loc_1258")

    OP_D2(0x270176, 0x270183, 0x11)
    OP_D2(0x270177, 0x270184, 0x12)
    Jump("loc_126F")

    label("loc_126F")

    OP_D2(0x27026E, 0x270278, 0x13)
    OP_6D(720, 0, -6220, 0)
    OP_67(0, 9730, -10000, 0)
    OP_6B(1820, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    SetChrPos(0x8, 700, 950, 12150, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -650, -1750, -7480, 0)
    SetChrPos(0x102, 740, -1750, -7480, 0)
    SetChrPos(0xF8, -750, -1750, -7480, 0)
    SetChrPos(0xF9, 820, -1750, -7480, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_71(0x5, 0x4)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_70(0x0, 0x8)
    OP_70(0x1, 0x8)
    OP_70(0x2, 0x8)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    LoadEffect(0x1, "map\\\\mp061_00.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)

    def lambda_13C7():
        OP_6D(600, 0, -350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13C7)
    ClearChrFlags(0x101, 0x80)

    def lambda_13E4():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xFFFFF827, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13E4)
    Sleep(100)
    ClearChrFlags(0x102, 0x80)

    def lambda_1409():
        OP_8E(0xFE, 0x3B6, 0x0, 0xFFFFF808, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1409)
    Sleep(800)
    ClearChrFlags(0xF8, 0x80)

    def lambda_142E():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0xFFFFF1FA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_142E)
    Sleep(100)
    ClearChrFlags(0xF9, 0x80)

    def lambda_1453():
        OP_8E(0xFE, 0x334, 0x0, 0xFFFFF240, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1453)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #11
        0x101,
        "#1020F#5P这、这里是……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C8")

    ChrTalk(    #12
        0x109,
        (
            "#1063F#6P好像来到塔顶了……\x01",
            "  \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1599")

    label("loc_14C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FC")

    ChrTalk(    #13
        0x106,
        (
            "#057F#6P好像来到塔顶了……\x01",
            "  \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1599")

    label("loc_14FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1530")

    ChrTalk(    #14
        0x103,
        (
            "#022F#6P好像来到塔顶了……\x01",
            "  \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1599")

    label("loc_1530")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1564")

    ChrTalk(    #15
        0x108,
        (
            "#072F#6P好像来到塔顶了……\x01",
            "  \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1599")

    label("loc_1564")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1599")

    ChrTalk(    #16
        0x107,
        (
            "#065F#6P好、好像来到塔顶了……\x01",
            "  \x02",
        )
    )

    CloseMessageWindow()

    label("loc_1599")


    ChrTalk(    #17
        0x102,
        (
            "#1043F#5P包围塔顶的『结界』\x01",
            "内侧吗……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #18
        0x8,
        "男人的声音",
        (
            "#4P呵呵……\x01",
            "动作还挺快的嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1651")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_168F")

    label("loc_1651")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1678")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_168F")

    label("loc_1678")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_168F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BB")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16F9")

    label("loc_16BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E2")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16F9")

    label("loc_16E2")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_16F9")

    Sleep(1000)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_170B():
        OP_6D(1800, 0, 8900, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_170B)

    def lambda_1723():
        OP_67(0, 5400, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1723)

    def lambda_173B():
        OP_6B(2520, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_173B)
    Sleep(2500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 3)

    def lambda_175A():
        OP_8E(0xFE, 0xFFFFFD44, 0x0, 0x122A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_175A)
    Sleep(200)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 5)

    def lambda_1784():
        OP_8E(0xFE, 0x2BC, 0x0, 0x11A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1784)
    Sleep(200)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 15)

    def lambda_17AE():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xB72, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_17AE)
    Sleep(200)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 17)

    def lambda_17D8():
        OP_8E(0xFE, 0x320, 0x0, 0xAF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_17D8)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #19
        0x101,
        (
            "#1002F#6P果然来了啊……\x01",
            "这个变态假面。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1912")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◆布卢布兰的挑战全部完成】\x01",          # 0
            "【◆布卢布兰的挑战完成１个以上】\x01",      # 1
            "【◆无视布卢布兰的挑战】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18C4"),
        (1, "loc_18DB"),
        (2, "loc_18F2"),
        (SWITCH_DEFAULT, "loc_1909"),
    )


    label("loc_18C4")

    OP_28(0x6C, 0x4, 0x10)
    OP_28(0x77, 0x4, 0x10)
    OP_28(0x78, 0x4, 0x10)
    OP_28(0xC4, 0x4, 0x10)
    Jump("loc_1909")

    label("loc_18DB")

    OP_28(0x6C, 0x4, 0x10)
    OP_28(0x77, 0x3, 0x10)
    OP_28(0x78, 0x3, 0x10)
    OP_28(0xC4, 0x3, 0x10)
    Jump("loc_1909")

    label("loc_18F2")

    OP_28(0x6C, 0x3, 0x10)
    OP_28(0x77, 0x3, 0x10)
    OP_28(0x78, 0x3, 0x10)
    OP_28(0xC4, 0x3, 0x10)
    Jump("loc_1909")

    label("loc_1909")

    FadeToBright(300, 0)

    label("loc_1912")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1926")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1926")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_193A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_193A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_194E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_194E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1962")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1962")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19FE")

    ChrTalk(    #20
        0x8,
        (
            "#232F呼……\x01",
            "别说得那么难听嘛。\x02\x03",

            "再怎么说，你们也完成过我的挑战。\x01",
            "连这点风度都没有的话可是很伤脑筋的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1019F#6P要、要你多管闲事！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B0E")

    label("loc_19FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A9F")

    ChrTalk(    #22
        0x8,
        (
            "#230F哎呀哎呀，说得这么难听。\x02\x03",

            "你们不是也曾响应过我的挑战吗。\x01",
            "表现出一点风度来也不算什么吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1019F#6P没、没风度真是抱歉啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B0E")

    label("loc_1A9F")


    ChrTalk(    #24
        0x8,
        (
            "#231F哼，说得真难听。\x02\x03",

            "不但没有胆量响应我的挑战，\x01",
            "就连一点风度也完全没有吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1019F#6P什、什么～！？\x02",
    )

    CloseMessageWindow()

    label("loc_1B0E")


    ChrTalk(    #26
        0x8,
        (
            "#230F这个暂且不说……\x01",
            "咱们还真是好久不见了啊。\x02\x03",

            "#231F『漆黑之牙』──\x01",
            "约修亚·阿斯特雷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#1035F#4P……没错。\x02\x03",

            "#1042F让我疑惑的是，\x01",
            "为什么你会配合教授的计划……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#230F呼呼，别人先姑且不论，\x01",
            "我自己是因为有点兴趣。\x02\x03",

            "#233F这个叫利贝尔的国家\x01",
            "洋溢着不可思议的气质。\x02\x03",

            "人，土地，甚至空气。\x02\x03",

            "#231F这种气质是真是假\x01",
            "我想要亲自确认一下。\x02\x03",

            "因为越是面临困难，\x01",
            "它就越会绽放光芒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1042F#4P原来如此……\x02\x03",

            "#1035F某种程度上，你和教授\x01",
            "可能很像。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#231F哈哈，我所追求的是美，\x01",
            "而教授却明显不同。\x02\x03",

            "这点你也应该知道才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#1042F#4P…………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2276")

    ChrTalk(    #32
        0x8,
        (
            "#230F不过，没想到公主殿下\x01",
            "会来到这种地方……\x02\x03",

            "莫非是已经决定接受\x01",
            "我的崇敬之心了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x105,
        (
            "#047F#4P很遗憾……\x01",
            "我不是那种会\x01",
            "响应你期望的人。\x02\x03",

            "#043F如果真是高尚的人\x01",
            "又怎会感到迷惘呢。\x02\x03",

            "将『埃尔赛尤』还给陛下的时候，\x01",
            "也是我必须作出回答的时候。\x02\x03",

            "#049F我……我很害怕这一刻的到来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1026F#5P科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#1043F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#231F啊哈哈！\x01",
            "那股恐惧正是高尚的证据！\x02\x03",

            "这是那些在地上匍匐的蝼蚁们\x01",
            "向往不已的翅膀！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    OP_0D()
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 19)
    OP_99(0x8, 0x0, 0xE, 0x7D0)

    def lambda_1F31():
        OP_6D(1280, 0, 7850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F31)

    def lambda_1F49():
        OP_67(0, 5250, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F49)

    def lambda_1F61():
        OP_6B(2520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F61)
    SetChrPos(0x9, 6410, 8800, 5150, 270)
    SetChrPos(0xA, -6950, 8800, 3250, 90)
    OP_9F(0x9, 0xFF, 0x0, 0x0, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_1FBD():
        OP_96(0xFE, 0x190A, 0x320, 0x141E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1FBD)
    OP_9F(0x9, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0x9, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_43(0x9, 0x3, 0x0, 0x2)

    def lambda_2013():
        OP_96(0xFE, 0xFFFFE4DA, 0x320, 0xCB2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2013)
    OP_9F(0xA, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0xA, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_43(0xA, 0x3, 0x0, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C2")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2100")

    label("loc_20C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20E9")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2100")

    label("loc_20E9")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2100")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_212C")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_216A")

    label("loc_212C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2153")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_216A")

    label("loc_2153")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_216A")

    Sleep(1000)

    def lambda_2175():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2175)
    Sleep(50)

    def lambda_2188():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2188)
    Sleep(50)

    def lambda_219B():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_219B)
    Sleep(50)

    def lambda_21AE():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_21AE)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #37
        0x105,
        "#042F#6P！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1020F#5P哇哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#1046F#6P强袭用人形兵器——\x01",
            "『跳梁小丑』！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #40
        0x8,
        (
            "#231F来吧，让我看看！\x02\x03",

            "那道连覆满阴影的大地\x01",
            "也能照亮的光辉！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2885")

    label("loc_2276")


    ChrTalk(    #41
        0x8,
        (
            "#232F话说回来，你们\x01",
            "也该稍微机警一点吧。\x02\x03",

            "你们收到了报告\x01",
            "应该知道我在这里。\x02\x03",

            "既然如此还带公主殿下来\x01",
            "也太没脑子了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1019F#6P开、开什么玩笑！\x02\x03",

            "谁要把科洛丝给你这种人啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2368")

    ChrTalk(    #43
        0x107,
        (
            "#065F#4P啊呜……\x01",
            "(怎、怎么会有这样的人？)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2368")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23AE")

    ChrTalk(    #44
        0x108,
        (
            "#075F#4P怎么说呢……\x01",
            "是非常厚颜无耻的大哥哥呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246C")

    label("loc_23AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F0")

    ChrTalk(    #45
        0x103,
        (
            "#025F#4P真是的……\x01",
            "厚颜无耻也要有个限度吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246C")

    label("loc_23F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_242E")

    ChrTalk(    #46
        0x106,
        (
            "#551F#4P哼……\x01",
            "厚颜无耻也要有个限度吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246C")

    label("loc_242E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_246C")

    ChrTalk(    #47
        0x109,
        (
            "#1068F#4P怎么说呢……\x01",
            "算是非常厚颜无耻吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246C")


    ChrTalk(    #48
        0x102,
        (
            "#1035F#4P布卢布兰……\x01",
            "游戏就到此为止吧。\x02\x03",

            "#1042F我们是为了阻止\x01",
            "『结社』的计划而来的。\x02\x03",

            "那么彼此之间，\x01",
            "要做的事只有一件吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        "#231F呵呵……没错。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    OP_0D()
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 19)
    OP_99(0x8, 0x0, 0xE, 0x7D0)

    def lambda_2538():
        OP_6D(1280, 0, 7850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2538)

    def lambda_2550():
        OP_67(0, 5250, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2550)

    def lambda_2568():
        OP_6B(2520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2568)
    SetChrPos(0x9, 6410, 8800, 5150, 270)
    SetChrPos(0xA, -6950, 8800, 3250, 90)
    OP_9F(0x9, 0xFF, 0x0, 0x0, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_25C4():
        OP_96(0xFE, 0x190A, 0x320, 0x141E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25C4)
    OP_9F(0x9, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0x9, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_43(0x9, 0x3, 0x0, 0x2)

    def lambda_261A():
        OP_96(0xFE, 0xFFFFE4DA, 0x320, 0xCB2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_261A)
    OP_9F(0xA, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0xA, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_43(0xA, 0x3, 0x0, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C9")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2707")

    label("loc_26C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F0")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2707")

    label("loc_26F0")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2707")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2733")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2771")

    label("loc_2733")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_275A")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2771")

    label("loc_275A")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2771")

    Sleep(1000)

    def lambda_277C():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_277C)
    Sleep(50)

    def lambda_278F():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_278F)
    Sleep(50)

    def lambda_27A2():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_27A2)
    Sleep(50)

    def lambda_27B5():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_27B5)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #50
        0x101,
        "#1020F#5P哇哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1046F#6P强袭用人形兵器——\x01",
            "『跳梁小丑』！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #52
        0x8,
        (
            "#231F『漆黑之牙』……\x01",
            "这还是第一次跟你比试吧。\x02\x03",

            "加上『剑圣』的女儿\x01",
            "就让我尽情地享受吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2885")

    OP_D2(0x2900A3, 0x2900A7, 0xF)
    OP_D2(0x26008F, 0x260094, 0x10)

    def lambda_289F():
        OP_6D(440, 0, 5440, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_289F)

    def lambda_28B7():
        OP_6B(2000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28B7)
    OP_22(0x23B, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_28DE():
        OP_96(0xFE, 0x1E, 0x0, 0x18CE, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_28DE)
    Sleep(100)
    OP_44(0x9, 0x3)
    SetChrFlags(0x9, 0x1000)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 8)

    def lambda_2914():
        OP_8E(0xFE, 0x5FA, 0x320, 0x1144, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2914)
    OP_44(0xA, 0x3)
    SetChrFlags(0xA, 0x1000)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 8)

    def lambda_2942():
        OP_8E(0xFE, 0xFFFFF5B0, 0x320, 0xE10, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2942)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x8, 0x1)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    Battle(0x454, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_298E"),
        (SWITCH_DEFAULT, "loc_2993"),
    )


    label("loc_298E")

    OP_B4(0x0)
    Jump("loc_2993")

    label("loc_2993")

    Return()

    # Function_11_1102 end

    def Function_12_2994(): pass

    label("Function_12_2994")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(330, 200, 12720, 0)
    OP_67(0, 3720, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(0, 0)
    OP_6E(501, 0)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_71(0x5, 0x4)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_70(0x0, 0x8)
    OP_70(0x1, 0x8)
    OP_70(0x2, 0x8)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    OP_7B()
    LoadEffect(0x1, "map\\\\mp061_00.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x8, 700, 950, 12150, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -530, 0, 5830, 0)
    SetChrPos(0x102, 660, 0, 5640, 0)
    SetChrPos(0xF8, -790, 0, 3690, 0)
    SetChrPos(0xF9, 920, 0, 3630, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_2B03"),
        (5, "loc_2B1A"),
        (4, "loc_2B31"),
        (6, "loc_2B48"),
        (7, "loc_2B5F"),
        (8, "loc_2B76"),
        (SWITCH_DEFAULT, "loc_2B8D"),
    )


    label("loc_2B03")

    OP_D2(0x701D0, 0x701DC, 0xF)
    OP_D2(0x701D1, 0x701DD, 0x10)
    Jump("loc_2B8D")

    label("loc_2B1A")

    OP_D2(0x70218, 0x70224, 0xF)
    OP_D2(0x70219, 0x70225, 0x10)
    Jump("loc_2B8D")

    label("loc_2B31")

    OP_D2(0x70200, 0x7020C, 0xF)
    OP_D2(0x70201, 0x7020D, 0x10)
    Jump("loc_2B8D")

    label("loc_2B48")

    OP_D2(0x70230, 0x7023C, 0xF)
    OP_D2(0x70231, 0x7023D, 0x10)
    Jump("loc_2B8D")

    label("loc_2B5F")

    OP_D2(0x70248, 0x70254, 0xF)
    OP_D2(0x70249, 0x70255, 0x10)
    Jump("loc_2B8D")

    label("loc_2B76")

    OP_D2(0x270176, 0x270183, 0xF)
    OP_D2(0x270177, 0x270184, 0x10)
    Jump("loc_2B8D")

    label("loc_2B8D")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_2BAE"),
        (5, "loc_2BC5"),
        (4, "loc_2BDC"),
        (6, "loc_2BF3"),
        (7, "loc_2C0A"),
        (8, "loc_2C21"),
        (SWITCH_DEFAULT, "loc_2C38"),
    )


    label("loc_2BAE")

    OP_D2(0x701D0, 0x701DC, 0x11)
    OP_D2(0x701D1, 0x701DD, 0x12)
    Jump("loc_2C38")

    label("loc_2BC5")

    OP_D2(0x70218, 0x70224, 0x11)
    OP_D2(0x70219, 0x70225, 0x12)
    Jump("loc_2C38")

    label("loc_2BDC")

    OP_D2(0x70200, 0x7020C, 0x11)
    OP_D2(0x70201, 0x7020D, 0x12)
    Jump("loc_2C38")

    label("loc_2BF3")

    OP_D2(0x70230, 0x7023C, 0x11)
    OP_D2(0x70231, 0x7023D, 0x12)
    Jump("loc_2C38")

    label("loc_2C0A")

    OP_D2(0x70248, 0x70254, 0x11)
    OP_D2(0x70249, 0x70255, 0x12)
    Jump("loc_2C38")

    label("loc_2C21")

    OP_D2(0x270176, 0x270183, 0x11)
    OP_D2(0x270177, 0x270184, 0x12)
    Jump("loc_2C38")

    label("loc_2C38")

    OP_D2(0x27026E, 0x270278, 0x13)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 15)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 17)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #53
        0x8,
        (
            "#230F#5P呼……\x01",
            "比我预料中的还要能干。\x02\x03",

            "#231F那么我也要动真格的了──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x99, 0x0, 0x64)
    OP_23(0xEB)
    OP_20(0x7D0)
    Fade(500)
    OP_6B(2500, 0)
    OP_82(0x1, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x83, 0x2)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(500)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    Sleep(500)
    OP_72(0x1, 0x20)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    Sleep(100)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    Sleep(100)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    Sleep(100)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 0, 600)
    Sleep(400)

    ChrTalk(    #54
        0x8,
        "#233F#6P唔！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        "#1042F#6P！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(43000, 0)
    OP_6E(363, 0)
    OP_0D()

    def lambda_2E83():
        OP_6B(5500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2E83)
    Sleep(500)
    OP_22(0x139, 0x0, 0x64)
    LoadEffect(0x2, "map\\mp049_02.eff")
    PlayEffect(0x2, 0x2, 0xFF, 0, 0, 6720, 0, 0, 0, 550, 550, 550, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_82(0x80, 0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C0707   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2994 end

    def Function_13_2F04(): pass

    label("Function_13_2F04")

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
        (0, "loc_2F7E"),
        (1, "loc_2F84"),
        (SWITCH_DEFAULT, "loc_2F8A"),
    )


    label("loc_2F7E")

    OP_A2(0x1200)
    Jump("loc_2F8A")

    label("loc_2F84")

    OP_A2(0x1201)
    Jump("loc_2F8A")

    label("loc_2F8A")

    Return()

    # Function_13_2F04 end

    def Function_14_2F8B(): pass

    label("Function_14_2F8B")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_14_2F8B end

    SaveToFile()

Try(main)
