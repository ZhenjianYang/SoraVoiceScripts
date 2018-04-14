from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R2300   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2300.x',
        MapIndex            = 102,
        MapDefaultBGM       = "ed60021",
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
        '米克',                                 # 9
        '剑齿虎',                               # 10
        '剑齿虎',                               # 11
        '梅威海道方向',                         # 12
        '杰尼丝王立学院方向',                   # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT09/CH10520 ._CH',             # 00
        'ED6_DT09/CH10521 ._CH',             # 01
        'ED6_DT29/CH12040 ._CH',             # 02
        'ED6_DT29/CH12041 ._CH',             # 03
        'ED6_DT09/CH10340 ._CH',             # 04
        'ED6_DT09/CH10341 ._CH',             # 05
        'ED6_DT09/CH11040 ._CH',             # 06
        'ED6_DT09/CH11041 ._CH',             # 07
        'ED6_DT09/CH11070 ._CH',             # 08
        'ED6_DT09/CH11071 ._CH',             # 09
        'ED6_DT09/CH11080 ._CH',             # 0A
        'ED6_DT09/CH11081 ._CH',             # 0B
        'ED6_DT07/CH01080 ._CH',             # 0C
        'ED6_DT29/CH12900 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT09/CH10520P._CP',             # 00
        'ED6_DT09/CH10521P._CP',             # 01
        'ED6_DT29/CH12040P._CP',             # 02
        'ED6_DT29/CH12041P._CP',             # 03
        'ED6_DT09/CH10340P._CP',             # 04
        'ED6_DT09/CH10341P._CP',             # 05
        'ED6_DT09/CH11040P._CP',             # 06
        'ED6_DT09/CH11041P._CP',             # 07
        'ED6_DT09/CH11070P._CP',             # 08
        'ED6_DT09/CH11071P._CP',             # 09
        'ED6_DT09/CH11080P._CP',             # 0A
        'ED6_DT09/CH11081P._CP',             # 0B
        'ED6_DT07/CH01080P._CP',             # 0C
        'ED6_DT29/CH12900P._CP',             # 0D
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -31370,
        Z                   = 0,
        Y                   = 1980,
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

    DeclNpc(
        X                   = 119440,
        Z                   = 0,
        Y                   = -7810,
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


    DeclMonster(
        X                   = 8930,
        Z                   = 370,
        Y                   = 11870,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x191,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 55220,
        Z                   = -110,
        Y                   = 8450,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x195,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 87920,
        Z                   = 100,
        Y                   = 10050,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x193,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 93230,
        Z                   = 60,
        Y                   = 5930,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x194,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -11190,
        Y                   = -1000,
        Z                   = -5490,
        Range               = -8710,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x189C,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_24A",          # 00, 0
        "Function_1_24B",          # 01, 1
        "Function_2_25E",          # 02, 2
        "Function_3_3A3",          # 03, 3
        "Function_4_3AC",          # 04, 4
        "Function_5_E57",          # 05, 5
        "Function_6_1601",         # 06, 6
        "Function_7_1622",         # 07, 7
        "Function_8_1649",         # 08, 8
        "Function_9_16DC",         # 09, 9
        "Function_10_1733",        # 0A, 10
        "Function_11_1798",        # 0B, 11
        "Function_12_1806",        # 0C, 12
        "Function_13_183B",        # 0D, 13
        "Function_14_1870",        # 0E, 14
        "Function_15_18A5",        # 0F, 15
        "Function_16_192C",        # 10, 16
    )


    def Function_0_24A(): pass

    label("Function_0_24A")

    Return()

    # Function_0_24A end

    def Function_1_24B(): pass

    label("Function_1_24B")

    OP_16(0x2, 0xFA0, 0xFFFEBBC8, 0xFFFE0C00, 0x230029)
    Return()

    # Function_1_24B end

    def Function_2_25E(): pass

    label("Function_2_25E")

    OP_D2(0x2601B0, 0x2601B5, 0xE)
    OP_D2(0x2601B0, 0x2601B5, 0xF)
    OP_D2(0x270110, 0x270120, 0x10)
    OP_D2(0x270112, 0x270122, 0x11)
    OP_D2(0x270130, 0x270140, 0x12)
    OP_D2(0x270131, 0x270141, 0x13)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_2B3"),
        (5, "loc_2CA"),
        (6, "loc_2E1"),
        (7, "loc_2F8"),
        (SWITCH_DEFAULT, "loc_30F"),
    )


    label("loc_2B3")

    OP_D2(0x701D0, 0x701DC, 0x14)
    OP_D2(0x701D1, 0x701DD, 0x15)
    Jump("loc_30F")

    label("loc_2CA")

    OP_D2(0x70218, 0x70224, 0x14)
    OP_D2(0x70219, 0x70225, 0x15)
    Jump("loc_30F")

    label("loc_2E1")

    OP_D2(0x70230, 0x7023C, 0x14)
    OP_D2(0x70231, 0x7023D, 0x15)
    Jump("loc_30F")

    label("loc_2F8")

    OP_D2(0x70248, 0x70254, 0x14)
    OP_D2(0x70249, 0x70255, 0x15)
    Jump("loc_30F")

    label("loc_30F")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_328"),
        (5, "loc_33F"),
        (6, "loc_356"),
        (7, "loc_36D"),
        (SWITCH_DEFAULT, "loc_384"),
    )


    label("loc_328")

    OP_D2(0x701D0, 0x701DC, 0x16)
    OP_D2(0x701D1, 0x701DD, 0x17)
    Jump("loc_384")

    label("loc_33F")

    OP_D2(0x70218, 0x70224, 0x16)
    OP_D2(0x70219, 0x70225, 0x17)
    Jump("loc_384")

    label("loc_356")

    OP_D2(0x70230, 0x7023C, 0x16)
    OP_D2(0x70231, 0x7023D, 0x17)
    Jump("loc_384")

    label("loc_36D")

    OP_D2(0x70248, 0x70254, 0x16)
    OP_D2(0x70249, 0x70255, 0x17)
    Jump("loc_384")

    label("loc_384")

    OP_D2(0x290387, 0x29038B, 0x18)
    OP_D2(0x270111, 0x270121, 0x19)
    OP_D2(0x290389, 0x29038D, 0x1A)
    Return()

    # Function_2_25E end

    def Function_3_3A3(): pass

    label("Function_3_3A3")

    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_3A3 end

    def Function_4_3AC(): pass

    label("Function_4_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B9")
    Return()

    label("loc_3B9")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D9")
    Call(0, 15)
    Call(0, 16)
    FadeToBright(0, 0)

    label("loc_3D9")

    OP_A3(0x2031)
    OP_A3(0x2032)
    OP_A3(0x2033)
    OP_A3(0x2034)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F5")
    OP_A2(0x2031)

    label("loc_3F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_405")
    OP_A2(0x2032)

    label("loc_405")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_415")
    OP_A2(0x2033)

    label("loc_415")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_425")
    OP_A2(0x2034)

    label("loc_425")

    Call(0, 2)
    Fade(1000)
    SetChrPos(0x101, -10370, 0, 1110, 90)
    SetChrPos(0x102, -10310, 0, 90, 90)
    SetChrPos(0xF9, -11900, 0, 1000, 90)
    SetChrPos(0xF8, -11900, 0, -440, 90)
    OP_6D(-10660, 0, 480, 0)
    OP_67(0, 8290, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetChrPos(0x8, 6950, -50, 900, 0)

    NpcTalk(    #0
        0x8,
        "少年的声音",
        "#3P呜哇啊啊啊啊～！！\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54B")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_589")

    label("loc_54B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_572")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_589")

    label("loc_572")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_589")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B5")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5F3")

    label("loc_5B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DC")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5F3")

    label("loc_5DC")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5F3")

    Sleep(1000)
    OP_21()
    OP_1D(0x29)
    Sleep(500)

    ChrTalk(    #1
        0x101,
        "#1004F#5P刚才那是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1042F#6P赶快，艾丝蒂尔！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 25)
    SetChrChipByIndex(0x102, 18)
    SetChrChipByIndex(0xF9, 22)
    SetChrChipByIndex(0xF8, 20)
    SetChrFlags(0x101, 0x1000)

    def lambda_65D():
        OP_91(0xFE, 0x2710, 0x0, 0x3E8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_65D)
    Sleep(100)

    def lambda_67D():
        OP_91(0xFE, 0x2710, 0x0, 0x3E8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_67D)
    Sleep(20)

    def lambda_69D():
        OP_91(0xFE, 0x2710, 0x0, 0x3E8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_69D)
    Sleep(100)

    def lambda_6BD():
        OP_91(0xFE, 0x2710, 0x0, 0x3E8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_6BD)
    Sleep(1000)
    Fade(1000)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF9, 0x0)
    OP_44(0xF8, 0x0)
    SetChrChipByIndex(0x102, 18)
    SetChrChipByIndex(0xF9, 20)
    SetChrChipByIndex(0xF8, 22)
    AddParty(0x4B, 0xFF, 0xFF)
    SetChrFlags(0x14C, 0x8)
    OP_6D(107510, 0, -6820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 115040, 0, -7820, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_774():
        OP_8E(0xFE, 0x18286, 0x0, 0xFFFFE5DE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_774)
    OP_0D()

    def lambda_790():
        OP_6D(99000, 0, -6480, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_790)
    WaitChrThread(0x8, 0x1)
    OP_63(0x8)

    def lambda_7B0():
        OP_96(0xFE, 0x18060, 0x0, 0xFFFFE5DE, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7B0)
    SetChrChipByIndex(0x8, 14)
    WaitChrThread(0x8, 0x1)
    OP_22(0x20C, 0x0, 0x50)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #3
        0x8,
        "#2P啊呜……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 1)
    OP_0D()

    ChrTalk(    #4
        0x8,
        (
            "#2P可、可恶……\x01",
            "怎么会这样……\x02\x03",

            "得、得赶快报告……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x193, 0x0, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x8, 2)
    Sleep(500)
    Fade(500)
    OP_6D(103940, 0, -7410, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(98000, 0)
    OP_6E(434, 0)
    OP_43(0x9, 0x1, 0x0, 0xA)
    OP_43(0xA, 0x1, 0x0, 0xB)
    OP_43(0x9, 0x3, 0x0, 0x6)
    SetChrSubChip(0x8, 1)
    SetChrFlags(0x8, 0x20)
    OP_8C(0x8, 90, 500)
    ClearChrFlags(0x8, 0x20)
    SetChrSubChip(0x8, 1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x9, 0x1)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #5
        0x8,
        "呜……\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    LoadEffect(0x0, "scraft\\\\sc000_11.eff")

    def lambda_92B():
        OP_6D(101140, 500, -5910, 1200)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_92B)

    def lambda_943():
        OP_67(0, 7530, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_943)

    def lambda_95B():
        OP_6B(1500, 1200)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_95B)

    def lambda_96B():
        OP_6C(45000, 1200)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_96B)

    def lambda_97B():
        OP_6E(434, 1200)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_97B)
    OP_43(0x9, 0x1, 0x0, 0x9)
    OP_43(0x9, 0x3, 0x0, 0x6)

    def lambda_999():
        OP_6D(101940, 0, -7410, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_999)
    SetChrPos(0x101, 91500, -10, -5720, 90)
    SetChrPos(0x102, 91120, -30, -6800, 90)
    SetChrPos(0xF9, 90660, 30, -5210, 90)
    SetChrPos(0xF8, 90530, 300, -7050, 90)
    SetChrChipByIndex(0x102, 18)
    SetChrChipByIndex(0xF9, 22)
    SetChrChipByIndex(0xF8, 20)
    OP_43(0x102, 0x1, 0x0, 0xC)
    OP_43(0xF9, 0x1, 0x0, 0xD)
    OP_43(0xF8, 0x1, 0x0, 0xE)
    SetChrSubChip(0x101, 0)

    def lambda_A1E():
        OP_8F(0xFE, 0x17836, 0x0, 0xFFFFE890, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A1E)
    WaitChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 17)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_A48():
        OP_96(0xFE, 0x18A9C, 0x0, 0xFFFFE5AC, 0x9C4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A48)
    Sleep(200)

    ChrTalk(    #6 op#5
        0x101,
        "#1005F#1P喝啊啊啊！\x05\x02",
    )


    def lambda_A84():
        OP_99(0xFE, 0x0, 0x9, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A84)
    OP_22(0x1F4, 0x0, 0x64)
    Sleep(300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1000, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_43(0x9, 0x1, 0x0, 0x8)
    WaitChrThread(0x101, 0x2)
    OP_22(0xD5, 0x0, 0x64)

    def lambda_AFA():
        OP_99(0xFE, 0x9, 0xC, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AFA)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x0)
    OP_43(0xA, 0x1, 0x0, 0x7)

    def lambda_B1B():
        OP_6D(103750, 0, -6570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B1B)

    def lambda_B33():
        OP_67(0, 8020, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B33)

    def lambda_B4B():
        OP_6B(1810, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B4B)

    def lambda_B5B():
        OP_6E(505, 1500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B5B)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #7
        0x8,
        "你，你们……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1005F#5P稍后再说！\x01",
            "现在先击退这些家伙！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1042F#6P快退下。\x01",
            "被卷进来就危险了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C42")

    ChrTalk(    #10
        0x107,
        (
            "#065F#6P为、为什么这种地方\x01",
            "会有『结社』的装甲兽……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC5")

    label("loc_C42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8A")

    ChrTalk(    #11
        0x103,
        (
            "#022F#6P为什么这种地方\x01",
            "会有『结社』的装甲兽……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC5")

    label("loc_C8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC5")

    ChrTalk(    #12
        0x106,
        (
            "#057F#6P为什么这种地方\x01",
            "会有装甲兽……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CEE")

    ChrTalk(    #13
        0x108,
        "#076F#6P……来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D3D")

    label("loc_CEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D17")

    ChrTalk(    #14
        0x106,
        "#054F#6P……来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D3D")

    label("loc_D17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3D")

    ChrTalk(    #15
        0x103,
        "#024F#6P……来了！\x02",
    )

    CloseMessageWindow()

    label("loc_D3D")


    def lambda_D43():
        OP_6D(104360, 0, -6540, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D43)

    def lambda_D5B():
        OP_6B(1650, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D5B)
    SetChrChipByIndex(0x9, 24)
    OP_43(0x9, 0x3, 0x0, 0x6)

    def lambda_D77():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_D77)
    SetChrChipByIndex(0x101, 25)
    SetChrFlags(0x101, 0x1000)

    def lambda_D9C():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D9C)

    def lambda_DB7():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DB7)
    Sleep(50)
    SetChrChipByIndex(0xA, 24)

    def lambda_DDC():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_DDC)

    def lambda_DF7():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_DF7)

    def lambda_E12():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_E12)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x197, 0x0, 0x0, 0x0, 0xFF)
    OP_31(0xFF, 0xF9, 0x0)
    Return()

    # Function_4_3AC end

    def Function_5_E57(): pass

    label("Function_5_E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E64")
    Return()

    label("loc_E64")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x4B, 0xFF)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    Sleep(500)
    OP_1D(0x15)
    Call(0, 2)
    OP_6D(104070, 0, -6980, 0)
    OP_67(0, 8710, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(317, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x101, 103920, 0, -6740, 90)
    SetChrPos(0x102, 103800, 0, -8039, 90)
    SetChrPos(0xF9, 102580, 0, -6370, 90)
    SetChrPos(0xF8, 102590, 0, -8440, 90)
    SetChrPos(0x8, 98440, 0, -7170, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 16)
    SetChrChipByIndex(0x102, 18)
    SetChrChipByIndex(0xF9, 22)
    SetChrChipByIndex(0xF8, 20)
    SetChrChipByIndex(0x8, 12)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrSubChip(0x8, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #16
        0x101,
        (
            "#1007F呼……\x01",
            "很强的装甲兽啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#1035F#6P啊啊……\x01",
            "幸好总算赶上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "#6P得、得救了……\x02",
    )

    CloseMessageWindow()

    def lambda_1013():
        OP_6D(103000, 0, -6950, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1013)
    OP_8E(0x8, 0x18858, 0x0, 0xFFFFE37C, 0xBB8, 0x0)

    def lambda_103F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_103F)
    Sleep(50)

    def lambda_1052():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1052)
    Sleep(60)

    def lambda_1065():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1065)
    Sleep(70)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #19
        0x8,
        (
            "#6P艾丝蒂尔……\x01",
            "还有约修亚。\x02\x03",

            "不好意思……\x01",
            "危急之时承蒙相救……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1006F#2P嗯，这就是我们的\x01",
            "工作嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#1042F#2P话说回来……\x01",
            "到底发生了什么事？\x02\x03",

            "刚才的魔兽，一般来说\x01",
            "可不会出现在这里的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "#6P其、其实……\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(1000)

    ChrTalk(    #23
        0x8,
        (
            "#6P学院……\x01",
            "王立学院被袭击了！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C1")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_11FF")

    label("loc_11C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E8")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_11FF")

    label("loc_11E8")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_11FF")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122B")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1269")

    label("loc_122B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1252")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1269")

    label("loc_1252")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1269")

    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x6E)
    Sleep(500)

    ChrTalk(    #24
        0x101,
        "#1005F#2P什…什么…！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12FB")

    ChrTalk(    #25
        0x103,
        "#022F#2P……请说清楚点儿。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1358")

    label("loc_12FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1328")

    ChrTalk(    #26
        0x106,
        "#057F#2P……说清楚点。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1358")

    label("loc_1328")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1358")

    ChrTalk(    #27
        0x108,
        "#072F#2P……能说清楚点儿吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1358")


    ChrTalk(    #28
        0x8,
        (
            "#6P啊，嗯……\x02\x03",

            "我……和平时一样\x01",
            "在校舍后面跷课。\x02\x03",

            "穿红色装甲的士兵们\x01",
            "突然从正门闯了进来。\x02\x03",

            "勤务员大叔\x01",
            "打算拦住他们……\x02\x03",

            "但、但他们用枪……\x01",
            "打、打伤了大叔……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1441")

    ChrTalk(    #29
        0x107,
        "#065F#2P…………！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1020F#2P怎、怎么会……\x02",
    )

    CloseMessageWindow()
    Jump("loc_14CA")

    label("loc_1441")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1487")

    ChrTalk(    #31
        0x101,
        "#1020F#2P怎、怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x108,
        "#072F#2P糟糕了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_14CA")

    label("loc_1487")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14CA")

    ChrTalk(    #33
        0x101,
        "#1020F#2P怎、怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x106,
        "#057F#2P不妙啊……\x02",
    )

    CloseMessageWindow()

    label("loc_14CA")


    ChrTalk(    #35
        0x8,
        (
            "#6P我一看到这个情景……\x01",
            "脑子就一片空白……\x02\x03",

            "想着要去找人帮忙\x01",
            "就逃到这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#1035F#2P……情况了解了。\x02\x03",

            "#1040F你能继续前往卢安\x01",
            "帮我们转告协会吗？\x02\x03",

            "我们直接到\x01",
            "学院附近看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#6P知、知道了……\x02\x03",

            "那些家伙们，除了刚才的魔兽之外，\x01",
            "还带着奇怪的人形机甲……\x02\x03",

            "你们要多加小心！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_E57 end

    def Function_6_1601(): pass

    label("Function_6_1601")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1621")
    OP_22(0x13F, 0x0, 0x50)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x50)
    Sleep(300)
    Jump("Function_6_1601")

    label("loc_1621")

    Return()

    # Function_6_1601 end

    def Function_7_1622(): pass

    label("Function_7_1622")

    SetChrChipByIndex(0xFE, 24)
    OP_96(0xFE, 0x1A838, 0x12C, 0xFFFFDE9A, 0x1F4, 0x1388)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_1622 end

    def Function_8_1649(): pass

    label("Function_8_1649")

    OP_44(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_1662():

        label("loc_1662")

        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1662")

    QueueWorkItem2(0xFE, 3, lambda_1662)
    OP_96(0xFE, 0x19C94, 0x0, 0xFFFFE69C, 0x64, 0x2710)
    OP_44(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)

    def lambda_16AD():

        label("loc_16AD")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_16AD")

    QueueWorkItem2(0x9, 2, lambda_16AD)
    OP_22(0x23B, 0x0, 0x64)
    OP_96(0xFE, 0x1A7D4, 0x12C, 0xFFFFE82C, 0x3E8, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_8_1649 end

    def Function_9_16DC(): pass

    label("Function_9_16DC")

    SetChrChipByIndex(0xFE, 24)

    def lambda_16E7():

        label("loc_16E7")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_16E7")

    QueueWorkItem2(0xFE, 2, lambda_16E7)
    OP_8F(0xFE, 0x1955A, 0x0, 0xFFFFE5DE, 0x1388, 0x0)
    OP_44(0x9, 0x3)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    OP_22(0x23B, 0x0, 0x64)
    OP_96(0xFE, 0x18A88, 0x0, 0xFFFFE5DE, 0x6A4, 0xFA0)
    Return()

    # Function_9_16DC end

    def Function_10_1733(): pass

    label("Function_10_1733")

    SetChrPos(0xFE, 119000, 500, -6800, 270)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 24)

    def lambda_1759():

        label("loc_1759")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_1759")

    QueueWorkItem2(0xFE, 2, lambda_1759)
    OP_8F(0xFE, 0x1A23E, 0x1F4, 0xFFFFE570, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)

    def lambda_178A():

        label("loc_178A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_178A")

    QueueWorkItem2(0xFE, 2, lambda_178A)
    Return()

    # Function_10_1733 end

    def Function_11_1798(): pass

    label("Function_11_1798")

    Sleep(300)
    SetChrPos(0xFE, 119000, 500, -9000, 270)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 24)

    def lambda_17C3():

        label("loc_17C3")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_17C3")

    QueueWorkItem2(0xFE, 2, lambda_17C3)
    OP_8F(0xFE, 0x1A1C6, 0x1F4, 0xFFFFDCD8, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)

    def lambda_17F4():

        label("loc_17F4")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_17F4")

    QueueWorkItem2(0xFE, 2, lambda_17F4)
    OP_44(0x9, 0x3)
    Return()

    # Function_11_1798 end

    def Function_12_1806(): pass

    label("Function_12_1806")

    Sleep(1000)
    OP_8E(0xFE, 0x17CAA, 0x0, 0xFFFFE11A, 0x1770, 0x0)
    OP_8E(0xFE, 0x189AC, 0x0, 0xFFFFE0C0, 0x1770, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_1806 end

    def Function_13_183B(): pass

    label("Function_13_183B")

    Sleep(500)
    OP_8E(0xFE, 0x17E1C, 0x0, 0xFFFFEDAE, 0x1770, 0x0)
    OP_8E(0xFE, 0x186C8, 0x0, 0xFFFFE926, 0x1770, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_13_183B end

    def Function_14_1870(): pass

    label("Function_14_1870")

    Sleep(1300)
    OP_8E(0xFE, 0x1794E, 0xA, 0xFFFFE188, 0x1770, 0x0)
    OP_8E(0xFE, 0x182FE, 0x0, 0xFFFFE142, 0x1770, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_14_1870 end

    def Function_15_18A5(): pass

    label("Function_15_18A5")

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
        (0, "loc_191F"),
        (1, "loc_1925"),
        (SWITCH_DEFAULT, "loc_192B"),
    )


    label("loc_191F")

    OP_A2(0x1200)
    Jump("loc_192B")

    label("loc_1925")

    OP_A2(0x1201)
    Jump("loc_192B")

    label("loc_192B")

    Return()

    # Function_15_18A5 end

    def Function_16_192C(): pass

    label("Function_16_192C")

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

    # Function_16_192C end

    SaveToFile()

Try(main)
