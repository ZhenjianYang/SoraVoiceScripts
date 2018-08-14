from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'P7013   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P7013.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60174",
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
        '露菲娜',                               # 9
        '临时凯文',                             # 10
        '临时莉丝',                             # 11
        '面具',                                 # 12
        '',                                     # 13
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
        'ED6_DT07/CH02770 ._CH',             # 00
        'ED6_DT07/CH02930 ._CH',             # 01
        'ED6_DT07/CH02940 ._CH',             # 02
        'ED6_DT07/CH02940 ._CH',             # 03
        'ED6_DT26/CH20716 ._CH',             # 04
        'ED6_DT27/CH03151 ._CH',             # 05
        'ED6_DT27/CH04154 ._CH',             # 06
        'ED6_DT27/CH04158 ._CH',             # 07
        'ED6_DT27/CH04150 ._CH',             # 08
        'ED6_DT27/CH04151 ._CH',             # 09
        'ED6_DT27/CH03081 ._CH',             # 0A
        'ED6_DT26/CH20728 ._CH',             # 0B
        'ED6_DT26/CH20724 ._CH',             # 0C
        'ED6_DT27/CH03085 ._CH',             # 0D
        'ED6_DT27/CH03084 ._CH',             # 0E
        'ED6_DT26/CH20720 ._CH',             # 0F
        'ED6_DT26/CH20812 ._CH',             # 10
        'ED6_DT26/CH20676 ._CH',             # 11
        'ED6_DT26/CH20727 ._CH',             # 12
        'ED6_DT26/CH20719 ._CH',             # 13
        'ED6_DT26/CH20717 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02770P._CP',             # 00
        'ED6_DT07/CH02930P._CP',             # 01
        'ED6_DT07/CH02940P._CP',             # 02
        'ED6_DT07/CH02940P._CP',             # 03
        'ED6_DT26/CH20716P._CP',             # 04
        'ED6_DT27/CH03151P._CP',             # 05
        'ED6_DT27/CH04154P._CP',             # 06
        'ED6_DT27/CH04158P._CP',             # 07
        'ED6_DT27/CH04150P._CP',             # 08
        'ED6_DT27/CH04151P._CP',             # 09
        'ED6_DT27/CH03081P._CP',             # 0A
        'ED6_DT26/CH20728P._CP',             # 0B
        'ED6_DT26/CH20724P._CP',             # 0C
        'ED6_DT27/CH03085P._CP',             # 0D
        'ED6_DT27/CH03084P._CP',             # 0E
        'ED6_DT26/CH20720P._CP',             # 0F
        'ED6_DT26/CH20812P._CP',             # 10
        'ED6_DT26/CH20676P._CP',             # 11
        'ED6_DT26/CH20727P._CP',             # 12
        'ED6_DT26/CH20719P._CP',             # 13
        'ED6_DT26/CH20717P._CP',             # 14
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1D2",          # 00, 0
        "Function_1_224",          # 01, 1
        "Function_2_225",          # 02, 2
        "Function_3_4230",         # 03, 3
        "Function_4_646D",         # 04, 4
        "Function_5_6484",         # 05, 5
        "Function_6_649B",         # 06, 6
        "Function_7_64B2",         # 07, 7
        "Function_8_64C9",         # 08, 8
        "Function_9_6500",         # 09, 9
        "Function_10_6536",        # 0A, 10
        "Function_11_656C",        # 0B, 11
        "Function_12_65A2",        # 0C, 12
        "Function_13_6600",        # 0D, 13
        "Function_14_663D",        # 0E, 14
        "Function_15_68E2",        # 0F, 15
        "Function_16_694F",        # 10, 16
        "Function_17_699E",        # 11, 17
        "Function_18_69E7",        # 12, 18
        "Function_19_70E4",        # 13, 19
        "Function_20_70F8",        # 14, 20
        "Function_21_712E",        # 15, 21
        "Function_22_7242",        # 16, 22
        "Function_23_7302",        # 17, 23
        "Function_24_73EA",        # 18, 24
        "Function_25_742E",        # 19, 25
        "Function_26_746C",        # 1A, 26
        "Function_27_751B",        # 1B, 27
        "Function_28_7ACF",        # 1C, 28
        "Function_29_7AE3",        # 1D, 29
        "Function_30_7B14",        # 1E, 30
        "Function_31_7BAA",        # 1F, 31
        "Function_32_7C14",        # 20, 32
        "Function_33_7C58",        # 21, 33
        "Function_34_7C96",        # 22, 34
    )


    def Function_0_1D2(): pass

    label("Function_0_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_1F1")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_223")

    label("loc_1F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_210")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)
    Jump("loc_223")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_223")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_223")

    Return()

    # Function_0_1D2 end

    def Function_1_224(): pass

    label("Function_1_224")

    Return()

    # Function_1_224 end

    def Function_2_225(): pass

    label("Function_2_225")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_01.eff")
    LoadEffect(0x3, "craft\\cr04150.eff")
    LoadEffect(0x4, "craft\\cr04150a.eff")
    LoadEffect(0x5, "craft\\cr04150b.eff")
    LoadEffect(0x6, "monster\\msc0641.eff")
    OP_E0(238, 0x55, 0x2)
    OP_E0(239, 0x56, 0x2)
    OP_E0(240, 0x57, 0x2)
    OP_E0(241, 0x58, 0x2)
    OP_E0(238, 0x59, 0x5)
    OP_E0(239, 0x5A, 0x5)
    OP_E0(240, 0x5B, 0x5)
    OP_E0(241, 0x5C, 0x5)
    SetChrPos(0x109, 110, 0, 1760, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328")
    SetChrPos(0xEF, 110, 0, 370, 0)
    SetChrPos(0xF0, 800, 0, -920, 0)
    SetChrPos(0xF1, -170, 0, -1560, 0)
    Jump("loc_3AD")

    label("loc_328")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C")
    SetChrPos(0xF0, 110, 0, 370, 0)
    SetChrPos(0xEF, 800, 0, -920, 0)
    SetChrPos(0xF1, -170, 0, -1560, 0)
    Jump("loc_3AD")

    label("loc_36C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD")
    SetChrPos(0xF1, 110, 0, 370, 0)
    SetChrPos(0xEF, 800, 0, -920, 0)
    SetChrPos(0xF0, -170, 0, -1560, 0)

    label("loc_3AD")

    OP_6D(260, -750, 29600, 0)
    OP_67(0, 9620, -10000, 0)
    OP_6B(5130, 0)
    OP_6C(295000, 0)
    OP_6E(355, 0)

    def lambda_3F0():
        OP_6B(5600, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3F0)

    def lambda_400():
        OP_6E(390, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_400)

    def lambda_410():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_410)
    FadeToBright(2000, 0)
    Sleep(4000)

    def lambda_42E():
        OP_8F(0xFE, 0x50, 0xFFFFFD12, 0x65E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_42E)
    Sleep(210)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B4")

    def lambda_45C():
        OP_8F(0xFE, 0xB4, 0xFFFFFD12, 0x5E6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_45C)
    Sleep(230)

    def lambda_47C():
        OP_8F(0xFE, 0x3D4, 0xFFFFFC18, 0x57E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_47C)
    Sleep(150)

    def lambda_49C():
        OP_8F(0xFE, 0xFFFFFDBC, 0xFFFFFC18, 0x580C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_49C)
    Jump("loc_589")

    label("loc_4B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_520")

    def lambda_4C8():
        OP_8F(0xFE, 0xB4, 0xFFFFFD12, 0x5E6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_4C8)
    Sleep(230)

    def lambda_4E8():
        OP_8F(0xFE, 0x3D4, 0xFFFFFC18, 0x57E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4E8)
    Sleep(150)

    def lambda_508():
        OP_8F(0xFE, 0xFFFFFDBC, 0xFFFFFC18, 0x580C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_508)
    Jump("loc_589")

    label("loc_520")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589")

    def lambda_534():
        OP_8F(0xFE, 0xB4, 0xFFFFFD12, 0x5E6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_534)
    Sleep(230)

    def lambda_554():
        OP_8F(0xFE, 0x3D4, 0xFFFFFC18, 0x57E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_554)
    Sleep(150)

    def lambda_574():
        OP_8F(0xFE, 0xFFFFFDBC, 0xFFFFFC18, 0x580C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_574)

    label("loc_589")

    WaitChrThread(0xEE, 0x3)
    Fade(500)
    OP_6D(1500, -750, 3000, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_5D6():
        OP_6D(-890, -1000, 26300, 11000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5D6)

    def lambda_5EE():
        OP_6B(3500, 11000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_5EE)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_646")

    ChrTalk(    #0
        0x101,
        "#1020F#6P这、这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_646")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_677")

    ChrTalk(    #1
        0x102,
        "#1502F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_677")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AF")

    ChrTalk(    #2
        0x10B,
        "#216F#6P这、这里是什么……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_6AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E3")

    ChrTalk(    #3
        0x107,
        "#065F#6P这、这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_6E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_718")

    ChrTalk(    #4
        0x10A,
        "#1317F#6P这、这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_718")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_749")

    ChrTalk(    #5
        0x105,
        "#1164F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77A")

    ChrTalk(    #6
        0x103,
        "#1522F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_77A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AA")

    ChrTalk(    #7
        0x106,
        "#052F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_7AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DA")

    ChrTalk(    #8
        0x108,
        "#072F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_7DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80A")

    ChrTalk(    #9
        0x10E,
        "#173F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_80A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83F")

    ChrTalk(    #10
        0x104,
        "#1543F#6P哦，这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_83F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86F")

    ChrTalk(    #11
        0x10D,
        "#276F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_86F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A2")

    ChrTalk(    #12
        0x10C,
        "#112F#6P……这里是………\x02",
    )

    CloseMessageWindow()

    label("loc_8A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E4")

    ChrTalk(    #13
        0x110,
        (
            "#1306F#6P……呼。\x01",
            "竟然有这样的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_8E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92D")

    ChrTalk(    #14
        0x10C,
        (
            "#112F#6P大圣堂的地下\x01",
            "竟然会有这样的地方……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_92D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96B")

    ChrTalk(    #15
        0x10D,
        "#276F#6P地下竟然有这样的地方……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_96B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AF")

    ChrTalk(    #16
        0x104,
        (
            "#1542F#6P在地下竟然\x01",
            "会有这样的地方……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_9AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F8")

    ChrTalk(    #17
        0x10E,
        (
            "#178F#6P大圣堂的地下\x01",
            "竟然会有这样的地方……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_9F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A36")

    ChrTalk(    #18
        0x108,
        "#072F#6P地下竟然有这样的地方……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_A36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A74")

    ChrTalk(    #19
        0x106,
        "#057F#6P地下竟然有这样的地方……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_A74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB3")

    ChrTalk(    #20
        0x103,
        "#1522F#6P地下竟然有这样的地方……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_AB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFD")

    ChrTalk(    #21
        0x105,
        (
            "#1163F#6P大圣堂的地下\x01",
            "竟然会有这样的地方……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_AFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B40")

    ChrTalk(    #22
        0x10A,
        "#1317F#6P地、地下竟然有这样的地方……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_B40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B82")

    ChrTalk(    #23
        0x107,
        "#065F#6P地、地下竟然有这样的地方……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_B82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC4")

    ChrTalk(    #24
        0x10B,
        "#216F#6P地、地下竟然有这样的地方……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_BC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C00")

    ChrTalk(    #25
        0x102,
        "#1502F#6P地下竟然有这样的地方……\x02",
    )

    CloseMessageWindow()

    label("loc_C00")


    ChrTalk(    #26
        0x109,
        (
            "#1067F#5P…………………………………\x02\x03",

            "#1065F正好在这里，\x01",
            "我追上了扛着\x01",
            "失去意识的你的那个猎兵。\x02\x03",

            "#1840F他万万没想到\x01",
            "会遇到阻碍。\x02\x03",

            "焦急之中，\x01",
            "他吓得连枪都掉了，\x01",
            "跑到了那边的台座边。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_CDF():
        OP_6D(-1200, -750, 28500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_CDF)

    def lambda_CF7():
        OP_8F(0xFE, 0xB4, 0xFFFFFD12, 0x6D2E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CF7)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #27
        0x109,
        (
            "#1065F#5P那时，台座上放的是……\x01",
            "被指定将要封印的\x01",
            "名为『洛亚的魔枪』的古代遗物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        "#1802F#6P『洛亚的魔枪』……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #29
        0x109,
        (
            "#1063F#11P……能够将持有它的人\x01",
            "变为『怪物』的枪。\x02\x03",

            "老实说，实在想不到\x01",
            "那是在女神圣域制造出来的东西。\x02\x03",

            "#1065F而被追到走投无路的猎兵……\x01",
            "拿起了那支『魔枪』。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_E6C():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_E6C)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    OP_1D(0xAF)
    OP_44(0xEE, 0x0)
    OP_6D(91010, -750, 14010, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(315000, 0)
    OP_6E(210, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS464._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS465._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS466._CH")
    OP_AD(0x240160, 0x0, 0x0, 0xC8)
    Sleep(2500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("凯文")

    AnonymousTalk(    #30
        (
            "\x07\x0C#40W……场面是压倒性的。\x02\x03",

            "在肉体构造发生变化，\x01",
            "成为异形怪物的猎兵面前，\x01",
            "我瞬间就被打倒了。\x02\x03",

            "而在那怪物……\x01",
            "对着昏倒的你\x01",
            "挥动『魔枪』的时候……\x02\x03",

            "发生了……那件事。\x02",
        )
    )

    Jump("loc_1042")

    label("loc_1042")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x12C)
    Sleep(2000)
    OP_22(0x1BF, 0x0, 0x64)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    Sleep(1000)
    OP_22(0x2F2, 0x1, 0x64)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(3000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_22(0x334, 0x0, 0x64)
    OP_22(0x2D6, 0x0, 0x64)
    Sleep(1500)
    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_22(0x227, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A2, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1B5, 0x0, 0x64)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    FadeToDark(0, 16777215, -1)
    OP_C6(0x2, 0x3, 16777215, 3000, 0)
    OP_43(0x109, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_43(0x109, 0x1, 0x0, 0x5)
    OP_43(0x109, 0x2, 0x0, 0x6)
    Sleep(500)
    OP_43(0x109, 0x3, 0x0, 0x7)
    Sleep(1500)
    Sleep(1500)
    OP_23(0x2F2)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_22(0x271, 0x0, 0x64)
    Sleep(2000)
    OP_C7(0x1, 0xFF, 0x0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("凯文")

    AnonymousTalk(    #31
        (
            "\x07\x0C#40W我的『圣痕』……\x01",
            "当场夺走了\x01",
            "猎兵所持的『魔枪』之力。\x02\x03",

            "然后，那力量增幅到几十倍以上\x01",
            "毫不留情地向着猎兵攻击过去。\x02\x03",

            "那已经不是战斗……\x01",
            "变成单方面的虐杀了。\x02\x03",

            "成为怪物的猎兵……\x01",
            "被撕成数千碎片一命呜呼。\x02\x03",

            "而我……\x02\x03",

            "初次显现『圣痕』的我\x01",
            "被那沸腾的力量所掌控，\x01",
            "完全丧失了自我……\x02",
        )
    )

    Jump("loc_12BC")

    label("loc_12BC")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240164, 0x0, 0x0, 0xC8)
    Sleep(2500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("凯文")

    AnonymousTalk(    #32
        (
            "\x07\x0C#40W……匆匆赶来的姐姐\x01",
            "似乎很快了解了情况。\x02\x03",

            "她用弩枪和法剑进行牵制，\x01",
            "将我从莉丝身边引开……\x02\x03",

            "然后……\x02",
        )
    )

    Jump("loc_1372")

    label("loc_1372")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x12C)
    Sleep(2000)
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS468._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS469._CH")
    OP_C6(0x3, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C6(0x4, 0x3, -1, 1000, 0)
    Sleep(1000)
    OP_C6(0x3, 0x3, 16777215, 0, 0)
    OP_22(0x2F2, 0x1, 0x64)
    OP_22(0x227, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A2, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1B5, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(0, 16777215, -1)
    OP_C6(0x4, 0x3, 16777215, 3000, 0)
    OP_43(0x109, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_43(0x109, 0x1, 0x0, 0x5)
    OP_43(0x109, 0x2, 0x0, 0x6)
    Sleep(500)
    OP_43(0x109, 0x3, 0x0, 0x7)
    Sleep(1500)
    Sleep(1500)
    OP_23(0x2F2)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_22(0x271, 0x0, 0x64)
    Sleep(2000)
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(2000)
    OP_AD(0x240167, 0x0, 0x0, 0x64)
    Sleep(4000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("凯文")

    AnonymousTalk(    #33
        (
            "\x07\x0C#40W当我清醒时……\x01",
            "我发现自己躺在姐姐的怀中。\x02\x03",

            "即使身体被无数次刺穿，\x01",
            "姐姐依然紧紧抱着我……\x02\x03",

            "就这样……断绝了气息。\x07\x00\x02",
        )
    )

    Jump("loc_1561")

    label("loc_1561")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_AE(0x64)
    Sleep(3000)
    OP_6D(-1200, -750, 27200, 0)
    OP_67(0, 4420, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(315000, 0)
    OP_6E(210, 0)
    Sleep(1000)

    def lambda_15CA():
        OP_6B(4300, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_15CA)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #34
        0x10F,
        "#1809F#6P#60W………啊……………\x02",
    )

    CloseMessageWindow()

    def lambda_1615():

        label("loc_1615")

        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        OP_48()
        Jump("loc_1615")

    QueueWorkItem2(0x10F, 3, lambda_1615)

    def lambda_1632():
        OP_8F(0xFE, 0xB4, 0xFFFFFD12, 0x5D5C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1632)
    WaitChrThread(0x10F, 0x0)
    OP_44(0x10F, 0x3)
    Sleep(1000)

    ChrTalk(    #35
        0x109,
        (
            "#1846F#11P嗯，就是这么回事。\x02\x03",

            "#1845F不是我救不了\x01",
            "露菲娜姐姐。\x02\x03",

            "#1844F而是我……\x02\x03",

            "正是你面前这个\x01",
            "无能的瘟神\x01",
            "亲手杀了你姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10F,
        (
            "#1960F#6P但、但是……\x02\x03",

            "#1449F……但是凯文你……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x109,
        (
            "#1843F#11P并不是故意杀人的……\x01",
            "这种话只是借口罢了。\x02\x03",

            "当时的我\x01",
            "被『圣痕』的力量所控制，\x01",
            "沉醉于血腥与暴力。\x02\x03",

            "#1844F如果我的心灵没有那么脆弱……\x01",
            "就不会发生这种事了吧。\x02",
        )
    )

    Jump("loc_1801")

    label("loc_1801")

    CloseMessageWindow()

    ChrTalk(    #38
        0x10F,
        "#1809F#6P#40W………凯文…………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        (
            "#1076F#11P#40W而且……而且啊……\x02\x03",

            "我呢，当时把姐姐的身影\x01",
            "与自己的妈妈重叠在一起。\x02\x03",

            "就像勒住我的脖子……\x01",
            "那时的妈妈一样。\x02\x03",

            "#1065F然后……\x01",
            "就怀着被背叛的怨念\x01",
            "用『魔枪』不断攻击……\x02\x03",

            "她们明明都是我最喜欢的……\x01",
            "想亲手去守护的人……\x02\x03",

            "#1845F呵呵呵……\x01",
            "这与我亲手杀了妈妈\x01",
            "和露菲娜姐姐有什么两样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10F,
        "#1445F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x10F, 4)
    SetChrSubChip(0x10F, 16)
    SetChrFlags(0x10F, 0x2)
    OP_0D()
    OP_9E(0x10F, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #41
        0x10F,
        "#1960F#6P……为什么………呢……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        "#1074F#11P……嗯……？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_99(0x10F, 0x11, 0x13, 0x5DC)
    OP_0D()
    Sleep(500)

    ChrTalk(    #43
        0x10F,
        "#1964F#6P#3S为什么没说出来呢！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #44
        0x10F,
        (
            "#1963F#6P这五年间……\x01",
            "你一句话都没告诉过我……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1076F#11P是啊……\x01",
            "真的很对不起你。\x02\x03",

            "#1065F不过，\x01",
            "现在说出来表示我已有所觉悟。\x02\x03",

            "#1844F就算你……\x01",
            "要找我寻仇也没关系。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #46
        0x10F,
        "#1961F#4S#6P……笨蛋！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0x10F, 0x2)
    SetChrFlags(0x10F, 0x20)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)

    def lambda_1BB6():
        OP_8F(0xFE, 0xFA, 0xFFFFFD12, 0x6F54, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1BB6)

    def lambda_1BD1():
        OP_99(0xFE, 0x0, 0x7, 0x960)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1BD1)
    Sleep(100)
    Fade(500)
    OP_6D(-650, -750, 28650, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(250, 0)
    WaitChrThread(0x10F, 0x1)

    def lambda_1C2D():
        OP_99(0xFE, 0x0, 0x1, 0x960)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1C2D)
    Sleep(30)
    OP_44(0x10F, 0x0)
    ClearChrFlags(0x10F, 0x20)
    SetChrChipByIndex(0x109, 4)
    SetChrSubChip(0x109, 20)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x800)
    SetChrFlags(0x10F, 0x8)
    OP_99(0x109, 0x15, 0x16, 0x3E8)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0x109, 4)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x10F, 200, -750, 27300, 0)
    WaitChrThread(0x10F, 0x0)
    Sleep(800)

    ChrTalk(    #47
        0x109,
        "#1079F#11P喂、喂……\x02",
    )

    CloseMessageWindow()
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    Sleep(300)

    ChrTalk(    #48
        0x10F,
        (
            "#1964F#6P你在说什么胡话！\x01",
            "凯文·格拉汉姆！\x02\x03",

            "我生气根本不是\x01",
            "因为那些事……！\x02\x03",

            "为什么……\x01",
            "为什么你要独自怀着这么沉痛的回忆\x01",
            "孤单地生存下去……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #49
        0x10F,
        (
            "#1960F#6P对我……！\x01",
            "身为你家人的我……！\x02\x03",

            "却一句话都不说……！\x01",
            "不让我和你一起分担……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E6A")

    ChrTalk(    #50
        0x101,
        "#1026F#5P莉丝小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC6")

    label("loc_1E6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EA0")

    ChrTalk(    #51
        0x107,
        "#063F#5P莉、莉丝姐姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC6")

    label("loc_1EA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED3")

    ChrTalk(    #52
        0x105,
        "#1163F#5P莉丝小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC6")

    label("loc_1ED3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F05")

    ChrTalk(    #53
        0x10A,
        "#813F#5P莉丝小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC6")

    label("loc_1F05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F33")

    ChrTalk(    #54
        0x10B,
        "#215F#5P修女……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC6")

    label("loc_1F33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F65")

    ChrTalk(    #55
        0x10E,
        "#175F#5P莉丝小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC6")

    label("loc_1F65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F98")

    ChrTalk(    #56
        0x102,
        "#1503F#5P莉丝小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC6")

    label("loc_1F98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC6")

    ChrTalk(    #57
        0x104,
        "#1542F#5P莉丝君……\x02",
    )

    CloseMessageWindow()

    label("loc_1FC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF2")

    ChrTalk(    #58
        0x110,
        "#1307F#5P姐姐……\x02",
    )

    CloseMessageWindow()

    label("loc_1FF2")

    WaitChrThread(0xEE, 0x3)
    OP_99(0x109, 0x7, 0xB, 0x3E8)
    Sleep(300)

    ChrTalk(    #59
        0x109,
        "#1067F#11P………莉丝……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10F,
        (
            "#1960F#6P#40W我终于明白了……\x02\x03",

            "凯文为什么\x01",
            "要去当『异端制裁者』……\x02\x03",

            "#1962F……其实并不是打算\x01",
            "为姐姐的死赎罪吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x109, 0)
    OP_0D()

    ChrTalk(    #61
        0x109,
        "#1847F#11P什……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10F,
        (
            "#1960F#6P#40W我已经……都明白了……\x02\x03",

            "不是为了赎罪……\x02\x03",

            "……也不是为了消除罪恶感……\x02\x03",

            "#1963F凯文……凯文是……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    OP_20(0x7D0)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        (
            "\x07\x02说得没错……\x01",
            "是为了接受『惩罚』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_222F")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2296")

    label("loc_222F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2257")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2296")

    label("loc_2257")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_227F")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2296")

    label("loc_227F")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2296")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C3")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_232A")

    label("loc_22C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22EB")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_232A")

    label("loc_22EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2313")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_232A")

    label("loc_2313")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_232A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2357")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_23BE")

    label("loc_2357")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_237F")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_23BE")

    label("loc_237F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A7")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_23BE")

    label("loc_23A7")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_23BE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23EB")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2452")

    label("loc_23EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2413")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2452")

    label("loc_2413")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2452")

    label("loc_243B")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2452")

    Sleep(1000)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -9900, -1000, 27300, 90)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 20)
    SetChrSubChip(0x10, 11)
    OP_1D(0xE0)
    Fade(1000)
    OP_6D(-10970, -1000, 28100, 0)
    OP_67(0, 4760, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(315000, 0)
    OP_6E(171, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)

    def lambda_24EF():
        OP_6B(4300, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_24EF)
    Sleep(500)
    OP_22(0xBA, 0x1, 0x64)
    PlayEffect(0x0, 0x0, 0x10, 0, 100, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x1, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_257D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_257D)
    OP_22(0x59, 0x0, 0x64)
    WaitChrThread(0x10, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0xBA)
    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C0")
    OP_8C(0xF0, 270, 0)
    OP_8C(0xF1, 270, 0)
    Jump("loc_25FB")

    label("loc_25C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25DF")
    OP_8C(0xEF, 270, 0)
    OP_8C(0xF1, 270, 0)
    Jump("loc_25FB")

    label("loc_25DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25FB")
    OP_8C(0xEF, 270, 0)
    OP_8C(0xF0, 270, 0)

    label("loc_25FB")

    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-4700, -750, 27500, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(315000, 0)
    OP_6E(327, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #64
        0x10F,
        "#1444F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_269E")

    ChrTalk(    #65
        0x10D,
        "#271F#5P『影之王』……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_27AB")

    label("loc_269E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26D4")

    ChrTalk(    #66
        0x108,
        "#076F#5P『影之王』……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_27AB")

    label("loc_26D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_270A")

    ChrTalk(    #67
        0x106,
        "#054F#5P『影之王』……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_27AB")

    label("loc_270A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2741")

    ChrTalk(    #68
        0x103,
        "#1524F#5P『影之王』……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_27AB")

    label("loc_2741")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2778")

    ChrTalk(    #69
        0x102,
        "#1506F#5P『影之王』……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_27AB")

    label("loc_2778")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27AB")

    ChrTalk(    #70
        0x10E,
        "#177F#5P『影之王』……！\x02",
    )

    CloseMessageWindow()

    label("loc_27AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27DD")

    ChrTalk(    #71
        0x104,
        "#1542F#5P出现了吗……！\x02",
    )

    CloseMessageWindow()

    label("loc_27DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2810")

    ChrTalk(    #72
        0x10B,
        "#216F#5P出、出现了……！\x02",
    )

    CloseMessageWindow()

    label("loc_2810")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2844")

    ChrTalk(    #73
        0x10A,
        "#1317F#5P什、什么时候！？\x02",
    )

    CloseMessageWindow()

    label("loc_2844")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2871")

    ChrTalk(    #74
        0x107,
        "#065F#5P哇哇……！\x02",
    )

    CloseMessageWindow()

    label("loc_2871")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28AC")

    ChrTalk(    #75
        0x101,
        "#1002F#5P在、在这种时候……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_28AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28E2")

    ChrTalk(    #76
        0x105,
        "#1163F#5P在、在这种时候……\x02",
    )

    CloseMessageWindow()

    label("loc_28E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2919")

    ChrTalk(    #77
        0x10C,
        "#112F#5P是吗……就是这家伙。\x02",
    )

    CloseMessageWindow()

    label("loc_2919")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2951")

    ChrTalk(    #78
        0x110,
        "#1305F#5P哼……就是这家伙吗。\x02",
    )

    CloseMessageWindow()

    label("loc_2951")

    ClearChrFlags(0x109, 0x800)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x10F, 0x8)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x10F, 0x0, 0x0, 0x8)

    def lambda_2980():
        OP_6D(-4900, -750, 27700, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2980)

    def lambda_2998():
        OP_67(0, 4500, -10000, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2998)

    def lambda_29B0():
        OP_6B(3200, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_29B0)

    def lambda_29C0():
        OP_6C(307000, 500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_29C0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29FB")
    OP_43(0xF0, 0x0, 0x0, 0x9)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 24)
    SetChrSubChip(0xF1, 0)
    WaitChrThread(0xF0, 0x0)
    Jump("loc_2A5A")

    label("loc_29FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A2C")
    OP_43(0xEF, 0x0, 0x0, 0xA)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 24)
    SetChrSubChip(0xF1, 0)
    WaitChrThread(0xEF, 0x0)
    Jump("loc_2A5A")

    label("loc_2A2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A5A")
    OP_43(0xEF, 0x0, 0x0, 0xB)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 23)
    SetChrSubChip(0xF0, 0)
    WaitChrThread(0xEF, 0x0)

    label("loc_2A5A")

    WaitChrThread(0x10F, 0x0)
    OP_8C(0x109, 270, 400)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(800)

    NpcTalk(    #79
        0x10,
        "影之王",
        (
            "\x07\x02#1580F#5P呵呵……\x01",
            "你们终于来了。\x02\x03",

            "前方就是『第七星层』……\x02\x03",

            "是我诞生的地方，\x01",
            "也是所有星层的基础。\x07\x00\x02",
        )
    )

    Jump("loc_2B03")

    label("loc_2B03")

    CloseMessageWindow()

    ChrTalk(    #80
        0x109,
        (
            "#1065F#12P果然是这样吗……\x02\x03",

            "#1067F……既然通向那里的\x01",
            "是这个场所……\x02\x03",

            "#1840F看来我的『确信』\x01",
            "果然没错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10F,
        "#1444F#6P咦……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0x10,
        "影之王",
        (
            "\x07\x02#1580F#5P呵呵，\x01",
            "那么我就再问一次。\x02\x03",

            "怎么样，凯文·格拉汉姆。\x02\x03",

            "你是否真的……\x01",
            "想知道我的真面目呢？\x07\x00\x02",
        )
    )

    Jump("loc_2C32")

    label("loc_2C32")

    CloseMessageWindow()

    ChrTalk(    #83
        0x109,
        (
            "#1075F#12P……自不用说。\x02\x03",

            "#1063F赶快摘掉\x01",
            "你那恶趣味的面具吧……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #84
        0x109,
        (
            "#1069F#12P#3S『影之王』──\x01",
            "不，露菲娜·亚尔珍特！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D03")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D6A")

    label("loc_2D03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2B")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D6A")

    label("loc_2D2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D53")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D6A")

    label("loc_2D53")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2D6A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D97")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2DFE")

    label("loc_2D97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DBF")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2DFE")

    label("loc_2DBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE7")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2DFE")

    label("loc_2DE7")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2DFE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E2B")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2E92")

    label("loc_2E2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E53")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2E92")

    label("loc_2E53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2E92")

    label("loc_2E7B")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2E92")

    Sleep(1300)

    NpcTalk(    #85
        0x10,
        "影之王",
        "\x07\x02#1580F#5P#3S哈哈哈，好吧！\x07\x00\x02",
    )

    Jump("loc_2ED1")

    label("loc_2ED1")

    CloseMessageWindow()
    Sleep(150)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2EE6():
        OP_6D(-11500, -1000, 29200, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2EE6)

    def lambda_2EFE():
        OP_67(0, 3590, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2EFE)

    def lambda_2F16():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2F16)

    def lambda_2F26():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2F26)

    def lambda_2F36():
        OP_6E(281, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2F36)
    WaitChrThread(0xEE, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x109, 0, -1000, 23000, 270)
    Sleep(300)
    OP_99(0x10, 0x0, 0x2, 0x4B0)
    OP_0D()
    Sleep(500)
    Fade(500)

    def lambda_2F7E():
        OP_6B(2850, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2F7E)
    OP_22(0x8F, 0x0, 0x64)
    OP_99(0x10, 0x3, 0x7, 0x3E8)
    OP_0D()
    Sleep(500)
    OP_99(0x10, 0x7, 0xA, 0x4B0)
    Sleep(500)

    NpcTalk(    #86
        0x109,
        "莉丝",
        "#1809F#1P姐、姐姐………\x02",
    )

    Jump("loc_2FD8")

    label("loc_2FD8")

    CloseMessageWindow()
    OP_59()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS471._CH")
    OP_C6(0x0, 0x0, 140000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1200)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("露菲娜")

    AnonymousTalk(    #87
        (
            "\x07\x02好久不见呢，莉丝。\x02\x03",

            "还有凯文……\x01",
            "亏你能看穿我的真实身份呢。\x02",
        )
    )

    Jump("loc_3091")

    label("loc_3091")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    Sleep(1000)

    ChrTalk(    #88
        0x109,
        (
            "#1065F#1P不……\x01",
            "答案我一开始就知道了。\x02\x03",

            "#1067F意味深长的言行……\x01",
            "还有众多挑衅的台词。\x02\x03",

            "#1840F以前没有确信……\x01",
            "是因为我内心并不想察觉。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-4800, -750, 27500, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(315000, 0)
    OP_6E(327, 0)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, 180, -750, 27950, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #89
        0x10,
        (
            "\x07\x02#1586F#5P呵呵，是啊。\x01",
            "你从很久以前就这么软弱。\x02\x03",

            "#1587F没想到你竟然能打败\x01",
            "我最强的骑士。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x109,
        (
            "#1065F#12P黑骑士……\x01",
            "不，是说『剑帝』吗……\x02\x03",

            "#1063F他到底和姐姐\x01",
            "有什么关系？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10,
        (
            "\x07\x02#1581F#5P大概是六年前……\x01",
            "我们在某个事件中相识了。\x02\x03",

            "#1586F我当时虽然和他对立，\x01",
            "但最后以双方都能接受的形式\x01",
            "了结了事件。\x02\x03",

            "#1582F而他似乎认为\x01",
            "是欠了我的『人情』吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x109,
        (
            "#1075F#12P原来如此……\x01",
            "你就巧妙地利用了这个人情，\x01",
            "让『剑帝』的概念苏醒了吗。\x02\x03",

            "#1840F真是的……\x01",
            "很像是姐姐会使用的伎俩嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10,
        (
            "\x07\x02#1586F#5P呵呵……\x01",
            "你夸我也没有用哦。\x02\x03",

            "#1587F既然已经到达这里……\x01",
            "你应该已经明白我的目的了吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x109,
        (
            "#1840F#12P啊啊……我已有所觉悟了。\x02\x03",

            "#1075F要带我走的话\x01",
            "就赶快动手吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #95
        0x10F,
        (
            "#1809F#6P等、等一下……！\x02\x03",

            "你们……\x01",
            "你们俩在说什么！？\x02",
        )
    )

    Jump("loc_3511")

    label("loc_3511")

    CloseMessageWindow()

    ChrTalk(    #96
        0x109,
        "#1067F#11P莉丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x10,
        (
            "\x07\x02#1586F#5P呵呵……\x01",
            "你不是也明白了吗？\x02\x03",

            "#1582F凯文啊……\x01",
            "想要接受『惩罚』哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35BC")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3623")

    label("loc_35BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E4")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3623")

    label("loc_35E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_360C")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3623")

    label("loc_360C")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3623")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3650")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_36B7")

    label("loc_3650")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3678")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_36B7")

    label("loc_3678")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A0")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_36B7")

    label("loc_36A0")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_36B7")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E4")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_374B")

    label("loc_36E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_370C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_374B")

    label("loc_370C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3734")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_374B")

    label("loc_3734")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_374B")

    Sleep(1200)

    ChrTalk(    #98
        0x10F,
        "#1444F#6P难、难道姐姐要……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10,
        (
            "\x07\x02#1586F#5P没错，\x01",
            "我就是为了给凯文带来『惩罚』\x01",
            "而诞生于此地的存在……\x02\x03",

            "为此我特地\x01",
            "改造了这个『影之国』，\x01",
            "将你们全部接了过来。\x02\x03",

            "#1587F而希望这一切的\x01",
            "就是凯文自身。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10F,
        "#1449F#6P骗、骗人……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        (
            "#1065F#11P……很遗憾，她说的没错。\x02\x03",

            "#1067F虽然我不完全清楚\x01",
            "为什么会变成这样……\x02\x03",

            "#1840F但姐姐说的话\x01",
            "的确是事实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10F,
        "#1445F#6P怎、怎么会……\x02",
    )

    CloseMessageWindow()

    def lambda_3910():
        OP_6D(-5700, -750, 27600, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3910)
    OP_8F(0x109, 0xFFFFFA92, 0xFFFFFC18, 0x6E32, 0x3E8, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #103
        0x109,
        (
            "#1846F#12P恐怕『第七星层』\x01",
            "就是不断给我惩罚的地方。\x02\x03",

            "对母亲见死不救，\x01",
            "还亲手杀死了姐姐，\x01",
            "对这样的我来说一定是再适合不过的场所。\x02\x03",

            "#1844F而且……\x01",
            "只要我坠落到那里，\x01",
            "这个事件就会顺利解决了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A4C")

    ChrTalk(    #104
        0x10E,
        "#172F#5P说、说什么……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AAD")

    label("loc_3A4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A7E")

    ChrTalk(    #105
        0x108,
        "#077F#5P说什么……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AAD")

    label("loc_3A7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AAD")

    ChrTalk(    #106
        0x10C,
        "#117F#5P说什么……！\x02",
    )

    CloseMessageWindow()

    label("loc_3AAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AF0")

    ChrTalk(    #107
        0x107,
        (
            "#566F#5P怎、怎么会……\x01",
            "这绝对不行啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2F")

    label("loc_3AF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B2F")

    ChrTalk(    #108
        0x105,
        (
            "#1163F#5P怎、怎么会……\x01",
            "这绝对不行！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B79")

    ChrTalk(    #109
        0x101,
        (
            "#1020F#5P等、等一下！\x01",
            "为什么会变成这样呢！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C08")

    label("loc_3B79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BC4")

    ChrTalk(    #110
        0x10B,
        (
            "#214F#5P等、等一下啊！\x01",
            "为什么会变成这样啊！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C08")

    label("loc_3BC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C08")

    ChrTalk(    #111
        0x10A,
        (
            "#815F#5P等、等一下！\x01",
            "怎么会变成这样啊！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C52")

    ChrTalk(    #112
        0x102,
        (
            "#1502F#5P凯文先生……\x01",
            "你是真心这么想的吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D18")

    label("loc_3C52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C9C")

    ChrTalk(    #113
        0x103,
        (
            "#1522F#5P你、你啊……\x01",
            "难道真是这么想的吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D18")

    label("loc_3C9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CE1")

    ChrTalk(    #114
        0x106,
        (
            "#057F#5P喂喂……\x01",
            "你是真心这么想的吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D18")

    label("loc_3CE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D18")

    ChrTalk(    #115
        0x10D,
        "#270F#5P你是认真的吗……！？\x02",
    )

    CloseMessageWindow()

    label("loc_3D18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D76")

    ChrTalk(    #116
        0x104,
        (
            "#1544F#5P哎呀哎呀……\x02\x03",

            "#1542F再怎么说\x01",
            "这结论也下得太快了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DD2")

    ChrTalk(    #117
        0x110,
        (
            "#268F#6P嗯……\x01",
            "这确实说得过去。\x02\x03",

            "#262F但是玲却不能理解呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD2")


    ChrTalk(    #118
        0x10F,
        "#1960F#6P…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3E10():
        OP_6D(-10110, -1000, 28290, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E10)

    def lambda_3E28():
        OP_67(0, 4300, -10000, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3E28)

    def lambda_3E40():
        OP_6B(2750, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3E40)

    def lambda_3E50():
        OP_6E(280, 500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3E50)
    SetChrFlags(0x10F, 0x1000)
    OP_7D(0x0, 0x10F, 0x32, 0x1F4)
    SetChrChipByIndex(0x10F, 9)

    def lambda_3E72():
        OP_8F(0xFE, 0xFFFFEDB8, 0xFFFFFC18, 0x6702, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3E72)
    WaitChrThread(0x10F, 0x1)
    OP_7D(0x1, 0x10F, 0x0, 0x0)
    OP_22(0x19A, 0x0, 0x64)
    OP_22(0xC9, 0x0, 0x64)
    PlayEffect(0x3, 0x3, 0x10F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_51(0x10F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 4)
    PlayEffect(0x4, 0x4, 0x10F, 0, 500, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x5, 0x0, 0x10F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_23(0xC9)
    PlayEffect(0x0, 0x5, 0x10, 0, 100, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x7, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_40A5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_40A5)
    OP_22(0x1F9, 0x0, 0x64)
    OP_22(0x2CE, 0x0, 0x64)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_82(0x5, 0x2)
    OP_82(0x7, 0x2)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(600)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Fade(250)
    OP_51(0x10F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10F, 8)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #119
        0xF0,
        "凯文",
        "#1847F#1P莉丝！？\x02",
    )

    Jump("loc_4225")

    label("loc_4225")

    CloseMessageWindow()
    Sleep(300)
    Call(0, 3)
    Return()

    # Function_2_225 end

    def Function_3_4230(): pass

    label("Function_3_4230")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_01.eff")
    OP_E0(238, 0x55, 0x2)
    OP_E0(239, 0x56, 0x2)
    OP_E0(240, 0x57, 0x2)
    OP_E0(241, 0x58, 0x2)
    OP_E0(238, 0x59, 0x5)
    OP_E0(239, 0x5A, 0x5)
    OP_E0(240, 0x5B, 0x5)
    OP_E0(241, 0x5C, 0x5)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-7770, 1350, 28370, 0)
    OP_67(0, 4410, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(254000, 0)
    OP_6E(385, 0)
    SetChrPos(0x109, -1870, -1000, 28340, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4320")
    SetChrPos(0xEF, -8400, -1000, 28050, 270)
    SetChrPos(0xF0, -1000, -1000, 24910, 315)
    SetChrPos(0xF1, -1770, -1000, 23520, 315)
    Jump("loc_43A5")

    label("loc_4320")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4364")
    SetChrPos(0xF0, -8400, -1000, 28050, 270)
    SetChrPos(0xEF, -1000, -1000, 24910, 315)
    SetChrPos(0xF1, -1770, -1000, 23520, 315)
    Jump("loc_43A5")

    label("loc_4364")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43A5")
    SetChrPos(0xF1, -8400, -1000, 28050, 270)
    SetChrPos(0xEF, -1000, -1000, 24910, 315)
    SetChrPos(0xF0, -1770, -1000, 23520, 315)

    label("loc_43A5")

    SetChrChipByIndex(0xEF, 22)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 23)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 24)
    SetChrSubChip(0xF1, 0)
    Sleep(500)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -13610, 1300, 31690, 135)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)

    def lambda_43EE():

        label("loc_43EE")

        OP_99(0xFE, 0x0, 0x7, 0x4B0)
        OP_48()
        Jump("loc_43EE")

    QueueWorkItem2(0x10, 2, lambda_43EE)
    PlayEffect(0x1, 0x1, 0x10, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4436():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4436)
    OP_22(0x59, 0x0, 0x64)
    OP_82(0x1, 0x2)
    OP_0D()
    Sleep(300)

    def lambda_4456():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_4456)

    def lambda_4464():
        OP_6D(-16640, -1000, 28090, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_4464)

    def lambda_447C():
        OP_67(0, 3950, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_447C)

    def lambda_4494():
        OP_6B(3200, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4494)

    def lambda_44A4():
        OP_6C(254000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_44A4)

    def lambda_44B4():
        OP_6E(364, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_44B4)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    NpcTalk(    #120
        0x10,
        "露菲娜",
        (
            "\x07\x02#1582F#11P嘻嘻，怎么了，莉丝？\x02\x03",

            "竟然面对姐姐\x01",
            "做出这种淘气举动……\x07\x00\x02",
        )
    )

    Jump("loc_4530")

    label("loc_4530")

    CloseMessageWindow()

    ChrTalk(    #121
        0x10F,
        (
            "#1961F#6P住口……！\x02\x03",

            "#1449F你不是姐姐……！\x02\x03",

            "姐姐是决不会\x01",
            "对凯文做这种事的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x109,
        "#1063F#5P莉、莉丝……\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()
    OP_1D(0xB2)
    Sleep(500)

    ChrTalk(    #123
        0x10F,
        (
            "#1445F#5P凯文，你快想起来！\x02\x03",

            "你对我发过誓……\x01",
            "说绝对不会做出\x01",
            "让姐姐伤心的事情的！\x02\x03",

            "#1446F如果你真的这样做了……\x02\x03",

            "#1449F牺牲自己一个人，\x01",
            "你以为姐姐会高兴吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x109,
        "#1063F#5P#3S！！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #125
        0x10,
        "露菲娜",
        (
            "\x07\x02#1586F#11P呵呵……这可难说哦？\x02\x03",

            "#1587F虽然『我』的确\x01",
            "不是真正的露菲娜，\x01",
            "但却是无限接近于她的存在……\x02\x03",

            "如果凯文渴望『惩罚』，\x01",
            "那我不是应该成全他吗？\x07\x00\x02",
        )
    )

    Jump("loc_4765")

    label("loc_4765")

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #126
        0x10F,
        "#1961F#6P#3S没有这种事！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #127
        0x10F,
        (
            "#1964F#6P真正的姐姐，\x01",
            "才不会这样惯着凯文！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #128
        0x109,
        "#1079F#5P什……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x10,
        "\x07\x02#1583F#11P…………………………………\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x10F,
        (
            "#1960F#5P快想起来，凯文！\x01",
            "我们初次见面时的事！\x02\x03",

            "那时你陷入绝望……\x01",
            "还企图赶走我们，\x01",
            "可姐姐没有让你得逞对吧……！\x02\x03",

            "#1963F还不由分说\x01",
            "就塞给你巧克力吃，\x01",
            "把你带回我们这里不是吗……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x109,
        "#1847F#5P…………啊………………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_AD(0x24010D, 0x0, 0x0, 0x12C)
    Sleep(3000)
    SetChrPos(0x109, -2510, -1000, 229370, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49AF")
    SetChrPos(0xEF, -8950, -1000, 228090, 315)
    SetChrPos(0xF0, -1680, -1000, 224520, 315)
    SetChrPos(0xF1, -3130, -1000, 223400, 315)
    Jump("loc_4A34")

    label("loc_49AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49F3")
    SetChrPos(0xF0, -8950, -1000, 228090, 315)
    SetChrPos(0xEF, -1680, -1000, 224520, 315)
    SetChrPos(0xF1, -3130, -1000, 223400, 315)
    Jump("loc_4A34")

    label("loc_49F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A34")
    SetChrPos(0xF1, -8950, -1000, 228090, 315)
    SetChrPos(0xEF, -1680, -1000, 224520, 315)
    SetChrPos(0xF0, -3130, -1000, 223400, 315)

    label("loc_4A34")

    SetChrPos(0x10, -10000, 1800, 235260, 135)
    OP_6D(-1690, -1000, 227040, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(155000, 0)
    OP_6E(457, 0)
    OP_AE(0x12C)
    Sleep(1500)
    Fade(250)
    SetChrChipByIndex(0x109, 12)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(300)

    ChrTalk(    #132
        0x109,
        (
            "#1067F#5P#40W………………………………\x02\x03",

            "…………我…………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-6710, -100, 228480, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(155000, 0)
    OP_6E(486, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #133
        0x10,
        "露菲娜",
        (
            "\x07\x02#1586F#6P呵呵……真令人吃惊。\x02\x03",

            "#1582F没想到\x01",
            "你已经如此成熟，\x01",
            "竟然这么能说会道……\x07\x00\x02",
        )
    )

    Jump("loc_4BD1")

    label("loc_4BD1")

    CloseMessageWindow()

    ChrTalk(    #134
        0x10F,
        (
            "#1964F#5P我叫你住口……！\x02\x03",

            "绝不容许……\x01",
            "你再继续侮辱姐姐！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #135
        0x10,
        "露菲娜",
        (
            "\x07\x02#1586F#6P呵呵，好吧。\x02\x03",

            "#1587F既然如此……\x01",
            "你就代替凯文\x01",
            "接受招待吧。\x07\x00\x02",
        )
    )

    Jump("loc_4C8A")

    label("loc_4C8A")

    CloseMessageWindow()

    ChrTalk(    #136
        0x10F,
        "#1809F#5P咦……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    LoadEffect(0x0, "map\\mp300_00.eff")
    LoadEffect(0x1, "map\\mp300_01.eff")
    LoadEffect(0x2, "map\\mp300_02.eff")
    LoadEffect(0x3, "map\\mp307_00.eff")
    LoadEffect(0x4, "map\\mp262_02.eff")
    LoadEffect(0x5, "monster\\msc1000.eff")
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x137, 0x1, 0x50)
    OP_22(0x32E, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x25D, 0x0, 0x64)
    OP_22(0x25E, 0x0, 0x64)
    OP_22(0x2A5, 0x0, 0x64)
    OP_22(0x339, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -9050, -950, 27500, -45, 0, 0, 850, 850, 850, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, -9150, -950, 228000, -45, 0, 0, 850, 850, 850, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E10")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E77")

    label("loc_4E10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E38")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E77")

    label("loc_4E38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E60")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E77")

    label("loc_4E60")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4E77")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EA4")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4F0B")

    label("loc_4EA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ECC")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4F0B")

    label("loc_4ECC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EF4")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4F0B")

    label("loc_4EF4")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4F0B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F38")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4F9F")

    label("loc_4F38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F60")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4F9F")

    label("loc_4F60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F88")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4F9F")

    label("loc_4F88")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4F9F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FCC")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5033")

    label("loc_4FCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FF4")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5033")

    label("loc_4FF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_501C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5033")

    label("loc_501C")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5033")

    Sleep(1000)
    OP_44(0x109, 0x3)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x10F, 0x20)
    SetChrFlags(0x10F, 0x4)
    SetChrChipByIndex(0x10F, 6)

    def lambda_5060():
        OP_8F(0xFE, 0xFFFFDD0A, 0xFFFFFBB4, 0x37AFA, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_5060)
    OP_99(0x10F, 0x0, 0x3, 0x5DC)
    OP_43(0x10F, 0x3, 0x0, 0xD)
    Fade(1000)
    SetChrPos(0x109, -1560, -1000, 28800, 270)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50E9")
    SetChrPos(0xEF, -8600, -1100, 27600, 0)
    SetChrPos(0xF0, -770, -1000, 24740, 315)
    SetChrPos(0xF1, -1400, -1000, 23310, 315)
    Jump("loc_516E")

    label("loc_50E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_512D")
    SetChrPos(0xF0, -8600, -1100, 27600, 0)
    SetChrPos(0xEF, -770, -1000, 24740, 315)
    SetChrPos(0xF1, -1400, -1000, 23310, 315)
    Jump("loc_516E")

    label("loc_512D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_516E")
    SetChrPos(0xF1, -8600, -1100, 27600, 0)
    SetChrPos(0xEF, -770, -1000, 24740, 315)
    SetChrPos(0xF0, -1400, -1000, 23310, 315)

    label("loc_516E")

    SetChrPos(0x10, -10000, 1800, 32500, 135)
    OP_6D(-6410, -1000, 27820, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(318000, 0)
    OP_6E(314, 0)
    OP_82(0x2, 0x2)
    OP_23(0x32E)
    OP_23(0x137)
    OP_0D()

    ChrTalk(    #137
        0x109,
        "#1069F#6P什……！\x02",
    )

    CloseMessageWindow()

    def lambda_51EA():
        OP_6D(-3580, 1550, 25440, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_51EA)

    def lambda_5202():
        OP_67(0, 3500, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5202)

    def lambda_521A():
        OP_6B(3000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_521A)

    def lambda_522A():
        OP_6C(318000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_522A)

    def lambda_523A():
        OP_6E(331, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_523A)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    NpcTalk(    #138
        0x10,
        "露菲娜",
        (
            "\x07\x02#1582F#6P呵呵……\x01",
            "你就在一边老实地看着吧。\x07\x00\x02",
        )
    )

    Jump("loc_5298")

    label("loc_5298")

    CloseMessageWindow()
    PlayEffect(0x3, 0x1, 0xFF, -3800, 2000, 26680, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Fade(1000)
    PlayEffect(0x4, 0x2, 0xFF, -2000, -1000, 29020, 0, 0, 0, 500, 700, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x3, 0xFF, -1200, -1000, 24060, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0x1B9, 0x0, 0x64)
    OP_22(0x3DC, 0x1, 0x50)
    OP_0D()
    Fade(500)

    def lambda_5358():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5358)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 16)
    SetChrSubChip(0x109, 4)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53ED")

    def lambda_5399():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_5399)
    SetChrChipByIndex(0xF0, 27)
    SetChrSubChip(0xF0, 3)
    SetChrFlags(0xF0, 0x800)
    Sleep(30)

    def lambda_53C7():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_53C7)
    SetChrChipByIndex(0xF1, 28)
    SetChrSubChip(0xF1, 3)
    SetChrFlags(0xF1, 0x800)
    Jump("loc_54BA")

    label("loc_53ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5455")

    def lambda_5401():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_5401)
    SetChrChipByIndex(0xEF, 26)
    SetChrSubChip(0xEF, 3)
    SetChrFlags(0xEF, 0x800)
    Sleep(30)

    def lambda_542F():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_542F)
    SetChrChipByIndex(0xF1, 28)
    SetChrSubChip(0xF1, 3)
    SetChrFlags(0xF1, 0x800)
    Jump("loc_54BA")

    label("loc_5455")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54BA")

    def lambda_5469():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_5469)
    SetChrChipByIndex(0xEF, 26)
    SetChrSubChip(0xEF, 3)
    SetChrFlags(0xEF, 0x800)
    Sleep(30)

    def lambda_5497():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_5497)
    SetChrChipByIndex(0xF0, 27)
    SetChrSubChip(0xF0, 3)
    SetChrFlags(0xF0, 0x800)

    label("loc_54BA")

    OP_0D()
    OP_82(0x1, 0x0)
    Sleep(300)

    ChrTalk(    #139
        0x109,
        "#1070F#5P呜……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5516")

    ChrTalk(    #140
        0x101,
        "#1021F#5P这、这是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_557A")

    label("loc_5516")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5549")

    ChrTalk(    #141
        0x104,
        "#1549F#5P这是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_557A")

    label("loc_5549")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_557A")

    ChrTalk(    #142
        0x10E,
        "#172F#5P这、这是……！\x02",
    )

    CloseMessageWindow()

    label("loc_557A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55B2")

    ChrTalk(    #143
        0x10B,
        "#216F#5P动、动不了了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_55E8")

    label("loc_55B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55E8")

    ChrTalk(    #144
        0x103,
        "#1533F#5P动、动不了了……！\x02",
    )

    CloseMessageWindow()

    label("loc_55E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5617")

    ChrTalk(    #145
        0x107,
        "#562F#5P呜、呜……！\x02",
    )

    CloseMessageWindow()

    label("loc_5617")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_564D")

    ChrTalk(    #146
        0x10A,
        "#1312F#5P怎、怎么了……！？\x02",
    )

    CloseMessageWindow()

    label("loc_564D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_567F")

    ChrTalk(    #147
        0x105,
        "#1381F#5P怎、怎么会……\x02",
    )

    CloseMessageWindow()

    label("loc_567F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56AE")

    ChrTalk(    #148
        0x106,
        "#057F#5P可恶……！？\x02",
    )

    CloseMessageWindow()

    label("loc_56AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56E0")

    ChrTalk(    #149
        0x108,
        "#077F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5741")

    label("loc_56E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5712")

    ChrTalk(    #150
        0x10D,
        "#271F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5741")

    label("loc_5712")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5741")

    ChrTalk(    #151
        0x10C,
        "#117F#5P什么……！？\x02",
    )

    CloseMessageWindow()

    label("loc_5741")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5775")

    ChrTalk(    #152
        0x110,
        "#1301F#5P『魔眼』……！？\x02",
    )

    CloseMessageWindow()

    label("loc_5775")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57BC")

    ChrTalk(    #153
        0x102,
        (
            "#1507F#5P和那个时候的恶魔\x01",
            "所使用的一样……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57BC")

    OP_22(0x25E, 0x0, 0x64)
    OP_22(0x339, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, -9050, -950, 27740, -45, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    SetChrFlags(0x10F, 0x4)
    SetChrFlags(0x10F, 0x2)
    SetChrChipByIndex(0x10F, 16)
    SetChrSubChip(0x10F, 2)
    SetChrFlags(0x10F, 0x20)
    SetChrFlags(0x10F, 0x1000)

    def lambda_5824():
        OP_67(0, 3200, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5824)

    def lambda_583C():
        OP_8F(0xFE, 0xFFFFDE68, 0xFFFFF9C0, 0x6BD0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_583C)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0x10F, 0x0)
    Fade(500)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #154
        0x10F,
        "#1804F#6P…………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x109,
        (
            "#1067F#12P……莉丝……！\x02\x03",

            "#1069F住手，姐姐！\x01",
            "这和莉丝没有一点关系吧！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #156
        0x10,
        "露菲娜",
        (
            "\x07\x02#1581F#6P这也是『惩罚』之一哦。\x02\x03",

            "#1586F让这孩子代替你\x01",
            "承受无尽的痛苦……\x02\x03",

            "#1587F这样你的痛苦\x01",
            "也会变得更加深重吧？\x07\x00\x02",
        )
    )

    Jump("loc_5987")

    label("loc_5987")

    CloseMessageWindow()

    ChrTalk(    #157
        0x109,
        "#1079F#12P什……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #158
        0x10F,
        (
            "#1961F#6P#4S做得到的话\x01",
            "你就试试看吧……！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x109, 0xFFFFFEA2, 1600, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    NpcTalk(    #159
        0x10,
        "露菲娜",
        "\x07\x02#1583F#6P哎呀……\x07\x00\x02",
    )

    Jump("loc_5A55")

    label("loc_5A55")

    CloseMessageWindow()

    ChrTalk(    #160
        0x109,
        "#1847F#12P莉丝……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x10F,
        (
            "#1445F#6P#40W无论坠落到何处\x01",
            "我都一定会活下去……！\x02\x03",

            "#1446F为了不让凯文……\x01",
            "再次孤单一人……\x02\x03",

            "#1806F……我绝对……\x01",
            "要平安回来给你看……！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #162
        0x109,
        "#1079F#12P………啊……………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #163
        0x10,
        "露菲娜",
        (
            "\x07\x02#1586F#6P呵呵，说得好啊。\x02\x03",

            "#1582F那么……\x01",
            "你就好好加油吧。\x07\x00\x02",
        )
    )

    Jump("loc_5BAB")

    label("loc_5BAB")

    CloseMessageWindow()
    OP_22(0x25E, 0x0, 0x64)
    OP_22(0x339, 0x0, 0x64)
    PlayEffect(0x2, 0x0, 0xFF, -9050, -950, 27740, -45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_5BF1():
        OP_67(0, 2800, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5BF1)
    Sleep(1000)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #164 op#A op#5
        0x10F,
        "#1809F#5P#40W#10A啊……………\x05\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x10F, 3)

    def lambda_5C55():
        OP_8F(0xFE, 0xFFFFDE68, 0xFFFFEC78, 0x6BD0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_5C55)
    Sleep(200)

    def lambda_5C75():
        OP_8F(0xFE, 0xFFFFDE68, 0xFFFFEC78, 0x6BD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_5C75)
    Sleep(200)

    def lambda_5C95():
        OP_8F(0xFE, 0xFFFFDE68, 0xFFFFEC78, 0x6BD0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_5C95)
    WaitChrThread(0x10F, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "map\\mp261_00.eff")
    LoadEffect(0x1, "map\\mp283_00.eff")
    LoadEffect(0x3, "map\\mp284_00.eff")
    LoadEffect(0x5, "map\\mp262_01.eff")
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x85, 0x1, 0x64)

    def lambda_5D18():

        label("loc_5D18")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_5D18")

    QueueWorkItem2(0x10F, 3, lambda_5D18)
    OP_22(0x34F, 0x0, 0x64)

    def lambda_5D38():
        OP_6D(-2830, -1000, 29900, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_5D38)

    def lambda_5D50():
        OP_67(0, 4500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5D50)

    def lambda_5D68():
        OP_6B(2470, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5D68)

    def lambda_5D78():
        OP_6E(331, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_5D78)
    OP_43(0x109, 0x0, 0x0, 0x10)
    Sleep(1000)

    ChrTalk(    #165 op#A op#5
        0x109,
        "#1847F#4S#20A#11P噢噢噢噢噢！！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x0, 0x6, 0x109, 0, 1300, -700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_44(0x10F, 0x3)
    OP_23(0x85)
    OP_22(0x353, 0x0, 0x64)
    OP_22(0x34F, 0x0, 0x64)
    PlayEffect(0x3, 0x5, 0x109, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_5E5C():

        label("loc_5E5C")

        OP_7C(0xC8, 0xC8, 0xBB8, 0x64)
        OP_48()
        Jump("loc_5E5C")

    QueueWorkItem2(0x10F, 3, lambda_5E5C)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_22(0x139, 0x0, 0x64)
    OP_9E(0x109, 0xF, 0x0, 0x1F4, 0xFA0)
    Sleep(300)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 18)
    SetChrSubChip(0x109, 0)
    OP_22(0x1B3, 0x0, 0x64)
    OP_82(0x1, 0x2)
    PlayEffect(0x5, 0x7, 0xFF, -2000, -1000, 29020, 0, 0, 0, 500, 700, 500, 0xFF, 0, 0, 0, 0)
    OP_82(0x2, 0x2)
    OP_44(0x10F, 0x3)
    OP_23(0x85)
    OP_23(0x3DC)

    def lambda_5EFB():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_5EFB)

    def lambda_5F13():
        OP_6B(2600, 300)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5F13)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6072")
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F6F")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5FD6")

    label("loc_5F6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F97")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5FD6")

    label("loc_5F97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FBF")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5FD6")

    label("loc_5FBF")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5FD6")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6003")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_606A")

    label("loc_6003")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_602B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_606A")

    label("loc_602B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6053")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_606A")

    label("loc_6053")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_606A")

    Sleep(1000)
    Jump("loc_6319")

    label("loc_6072")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61C7")
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60C4")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_612B")

    label("loc_60C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60EC")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_612B")

    label("loc_60EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6114")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_612B")

    label("loc_6114")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_612B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6158")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_61BF")

    label("loc_6158")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6180")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_61BF")

    label("loc_6180")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61A8")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_61BF")

    label("loc_61A8")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_61BF")

    Sleep(1000)
    Jump("loc_6319")

    label("loc_61C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6319")
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6219")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6280")

    label("loc_6219")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6241")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6280")

    label("loc_6241")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6269")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6280")

    label("loc_6269")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6280")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62AD")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6314")

    label("loc_62AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62D5")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6314")

    label("loc_62D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62FD")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6314")

    label("loc_62FD")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6314")

    Sleep(1000)

    label("loc_6319")

    OP_82(0x5, 0x2)
    Sleep(500)

    ChrTalk(    #166 op#A op#5
        0x10,
        "\x07\x02#1584F#6P#15A什……\x05\x07\x00\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_43(0x109, 0x0, 0x0, 0x11)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_6370():
        OP_6D(-8020, -1000, 27820, 500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6370)

    def lambda_6388():
        OP_67(0, 5870, -10000, 500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6388)

    def lambda_63A0():
        OP_6B(2400, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_63A0)
    OP_82(0x6, 0x2)
    SetChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 10)
    OP_7D(0x0, 0x109, 0x32, 0x1F4)

    def lambda_63C5():
        OP_8E(0xFE, 0xFFFFE7F0, 0xFFFFFC18, 0x6DBA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63C5)
    WaitChrThread(0x109, 0x1)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 16)
    SetChrSubChip(0x109, 6)

    def lambda_63FE():
        OP_96(0xFE, 0xFFFFDE54, 0xFFFFD8F0, 0x6C70, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63FE)
    Sleep(300)
    SetChrSubChip(0x109, 7)
    WaitChrThread(0x109, 0x1)
    OP_7D(0x1, 0x109, 0x0, 0x0)
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_44(0x10F, 0x0)
    OP_44(0x10F, 0x1)
    OP_44(0x10F, 0x2)
    OP_44(0x10F, 0x3)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    AddParty(0xE, 0xEF, 0xFF)
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/P7013   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_4230 end

    def Function_4_646D(): pass

    label("Function_4_646D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6483")
    OP_22(0xCB, 0x0, 0x64)
    Sleep(100)
    Jump("Function_4_646D")

    label("loc_6483")

    Return()

    # Function_4_646D end

    def Function_5_6484(): pass

    label("Function_5_6484")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_649A")
    OP_22(0x38F, 0x0, 0x64)
    Sleep(150)
    Jump("Function_5_6484")

    label("loc_649A")

    Return()

    # Function_5_6484 end

    def Function_6_649B(): pass

    label("Function_6_649B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64B1")
    OP_22(0x2F0, 0x0, 0x64)
    Sleep(100)
    Jump("Function_6_649B")

    label("loc_64B1")

    Return()

    # Function_6_649B end

    def Function_7_64B2(): pass

    label("Function_7_64B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64C8")
    Sleep(300)
    OP_22(0x271, 0x0, 0x64)
    Jump("Function_7_64B2")

    label("loc_64C8")

    Return()

    # Function_7_64B2 end

    def Function_8_64C9(): pass

    label("Function_8_64C9")


    def lambda_64CF():
        OP_8F(0xFE, 0x1C2, 0xFFFFFD12, 0x661C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_64CF)
    OP_8C(0x10F, 270, 400)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 8)
    SetChrSubChip(0x10F, 0)
    WaitChrThread(0x10F, 0x1)
    Return()

    # Function_8_64C9 end

    def Function_9_6500(): pass

    label("Function_9_6500")

    OP_8E(0xFE, 0x168, 0xFFFFFD12, 0x5E56, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 23)
    SetChrSubChip(0xFE, 0)
    OP_0D()
    Return()

    # Function_9_6500 end

    def Function_10_6536(): pass

    label("Function_10_6536")

    OP_8E(0xFE, 0x168, 0xFFFFFD12, 0x5E56, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    OP_0D()
    Return()

    # Function_10_6536 end

    def Function_11_656C(): pass

    label("Function_11_656C")

    OP_8E(0xFE, 0x168, 0xFFFFFD12, 0x5E56, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    OP_0D()
    Return()

    # Function_11_656C end

    def Function_12_65A2(): pass

    label("Function_12_65A2")

    OP_22(0x228, 0x0, 0x64)

    def lambda_65AD():

        label("loc_65AD")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_65AD")

    QueueWorkItem2(0xFE, 3, lambda_65AD)

    def lambda_65BE():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_65BE)
    SetChrSubChip(0xFE, 2)

    def lambda_65DD():
        OP_96(0xFE, 0xFFFFF704, 0xFFFFFD12, 0x6EF0, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65DD)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_65A2 end

    def Function_13_6600(): pass

    label("Function_13_6600")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_663C")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_13_6600")

    label("loc_663C")

    Return()

    # Function_13_6600 end

    def Function_14_663D(): pass

    label("Function_14_663D")

    SetChrFlags(0xFE, 0x4)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    SetChrFlags(0xFE, 0x1000)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 2)

    def lambda_6664():
        OP_8F(0xFE, 0xFFFFEDB8, 0xFFFFFC18, 0x6702, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6664)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_6689():
        OP_96(0xFE, 0xFFFFDF94, 0xFFFFFC18, 0x6B6C, 0x6A4, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6689)
    OP_51(0xFE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 2)
    Sleep(200)

    def lambda_6766():
        OP_99(0xFE, 0x3, 0x5, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6766)
    PlayEffect(0x0, 0x0, 0x10, 0, 100, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_67E0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_67E0)
    OP_22(0x59, 0x0, 0x64)
    Sleep(100)
    OP_22(0x389, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    OP_51(0xFE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 6)
    SetChrSubChip(0xFE, 3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_14_663D end

    def Function_15_68E2(): pass

    label("Function_15_68E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_694E")
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    Sleep(2000)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    Sleep(2500)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    Sleep(3000)
    Jump("Function_15_68E2")

    label("loc_694E")

    Return()

    # Function_15_68E2 end

    def Function_16_694F(): pass

    label("Function_16_694F")

    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 16)
    SetChrSubChip(0x109, 4)
    Sleep(500)
    OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xFA0)
    SetChrFlags(0x109, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 5)
    OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xFA0)
    Sleep(500)
    Return()

    # Function_16_694F end

    def Function_17_699E(): pass

    label("Function_17_699E")


    ChrTalk(    #167 op#A op#5
        0x109,
        "#1069F#3S#10A#11P喝啊啊啊啊啊啊啊啊啊！！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Return()

    # Function_17_699E end

    def Function_18_69E7(): pass

    label("Function_18_69E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp205_05.eff")
    LoadEffect(0x1, "map\\mp205_06.eff")
    OP_C4(0x0, 0x20000)
    SetChrFlags(0x11, 0x2000)
    SetChrFlags(0x12, 0x2000)
    SetChrFlags(0x13, 0x2000)
    SetChrFlags(0x11, 0x1000)
    SetChrFlags(0x12, 0x1000)
    SetChrFlags(0x13, 0x1000)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 64)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 33)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(313500, 75500, -117060, 0)
    OP_67(0, -1500, -10000, 0)
    OP_6B(100, 0)
    OP_6C(0, 0)
    OP_6E(572, 0)
    OP_D0(-30140, 0)
    PlayEffect(0x0, 0x0, 0xFF, 300350, -1000, 0, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, 300350, -1000, 0, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, 1594360, 50000, -12280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x17A, 0x1, 0x64)
    OP_22(0x85, 0x1, 0x64)
    OP_22(0x96, 0x0, 0x64)

    def lambda_6B9F():

        label("loc_6B9F")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_6B9F")

    QueueWorkItem2(0x10, 3, lambda_6B9F)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x11, 314130, 65000, -114660, 0)
    SetChrPos(0x12, 314130, 75500, -114660, 0)
    SetChrPos(0x13, 313030, 75000, -113700, 0)
    SetChrFlags(0x11, 0x8)
    OP_43(0x12, 0x0, 0x0, 0x17)
    FadeToBright(1000, 0)

    def lambda_6C07():
        OP_6D(313080, 74500, -110560, 8000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6C07)

    def lambda_6C1F():
        OP_67(0, -500, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C1F)

    def lambda_6C37():
        OP_6B(4000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6C37)

    def lambda_6C47():
        OP_6E(600, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6C47)
    WaitChrThread(0x12, 0x0)

    def lambda_6C5C():

        label("loc_6C5C")

        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        OP_48()
        Jump("loc_6C5C")

    QueueWorkItem2(0x12, 1, lambda_6C5C)
    OP_82(0x2, 0x2)

    def lambda_6C72():
        OP_6E(600, 2800)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6C72)

    def lambda_6C82():
        OP_D0(-40110, 2800)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6C82)

    def lambda_6C92():
        OP_67(0, 4000, -10000, 2800)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C92)

    def lambda_6CAA():
        OP_6B(2500, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6CAA)
    Sleep(500)

    def lambda_6CBF():
        OP_99(0xFE, 0x0, 0x1D, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6CBF)
    WaitChrThread(0x12, 0x1)

    def lambda_6CD4():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6CD4)

    def lambda_6CEC():
        OP_D0(-50110, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6CEC)

    def lambda_6CFC():
        OP_99(0xFE, 0x1E, 0x20, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6CFC)
    WaitChrThread(0x12, 0x1)

    def lambda_6D11():
        OP_8F(0xFE, 0x4BB72, 0x2710, 0xFFFE401C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6D11)

    def lambda_6D2C():
        OP_99(0xFE, 0x21, 0x2C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6D2C)
    OP_43(0x13, 0x0, 0x0, 0x19)
    WaitChrThread(0x12, 0x1)

    def lambda_6D48():

        label("loc_6D48")

        OP_99(0xFE, 0x39, 0x3C, 0x9C4)
        OP_48()
        Jump("loc_6D48")

    QueueWorkItem2(0x12, 1, lambda_6D48)

    def lambda_6D5B():
        OP_6D(313080, 75500, -111560, 4500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6D5B)

    def lambda_6D73():
        OP_6E(650, 4500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6D73)

    def lambda_6D83():
        OP_6B(6000, 4500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6D83)
    Sleep(4000)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x13, 0x0)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x2)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_44(0x10F, 0x0)
    OP_6D(1593280, 50000, 72610, 0)
    OP_67(0, -200, -10000, 0)
    OP_6B(11000, 0)
    OP_6C(180000, 0)
    OP_6E(850, 0)
    OP_D0(0, 0)
    ClearChrFlags(0x11, 0x8)
    SetChrPos(0x11, 1593370, 47100, 100140, 0)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 45)

    def lambda_6E36():

        label("loc_6E36")

        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        OP_48()
        Jump("loc_6E36")

    QueueWorkItem2(0x11, 0, lambda_6E36)
    ClearChrFlags(0x13, 0x8)
    SetChrPos(0x13, 1592700, 46500, 184800, 0)
    SetChrFlags(0x13, 0x40)
    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 0)

    def lambda_6E6E():
        OP_8F(0xFE, 0x184CB4, 0xB3B0, 0x28514, 0xF3C, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6E6E)

    def lambda_6E89():
        OP_6E(924, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6E89)

    def lambda_6E99():
        OP_D0(-25600, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_6E99)

    def lambda_6EA9():
        OP_6B(8000, 10000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6EA9)

    def lambda_6EB9():
        OP_8F(0xFE, 0x18522C, 0xB7FC, 0x24A7C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6EB9)
    Sleep(2500)
    OP_43(0x13, 0x0, 0x0, 0x14)
    OP_43(0x11, 0x0, 0x0, 0x15)
    Sleep(3500)

    def lambda_6EEC():
        OP_8F(0xFE, 0x18522C, 0xB7FC, 0x2989C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6EEC)

    def lambda_6F07():
        OP_6B(7000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6F07)
    Sleep(1000)
    OP_44(0x10F, 0x0)
    OP_44(0x10F, 0x1)
    OP_44(0x10F, 0x2)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_6D(305250, 30000, -6140, 0)
    OP_67(0, 9950, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(42000, 0)
    OP_6E(761, 0)
    OP_D0(10000, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 290520, 60000, -30450, 0)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 48)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 290520, 10000, 500, 0)
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 45)
    SetChrFlags(0x13, 0x80)
    OP_82(0x1, 0x0)

    def lambda_6FBE():
        OP_6D(300250, 30000, -5140, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6FBE)

    def lambda_6FD6():
        OP_67(0, 17620, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6FD6)

    def lambda_6FEE():
        OP_6B(4300, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6FEE)

    def lambda_6FFE():
        OP_6E(777, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_6FFE)

    def lambda_700E():
        OP_D0(3000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_700E)
    OP_43(0x11, 0x0, 0x0, 0x13)

    def lambda_7025():

        label("loc_7025")

        OP_99(0xFE, 0x39, 0x3C, 0xDAC)
        OP_48()
        Jump("loc_7025")

    QueueWorkItem2(0x12, 0, lambda_7025)

    def lambda_7038():
        OP_8F(0xFE, 0x44C14, 0x2904, 0x27D8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7038)

    def lambda_7053():
        OP_8F(0xFE, 0x447C8, 0x2710, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7053)
    Sleep(3000)
    OP_22(0x99, 0x0, 0x64)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_43(0x109, 0x1, 0x0, 0x1A)
    WaitChrThread(0x109, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    Sleep(2000)
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_C4(0x1, 0x20000)
    Sleep(3000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_69E7 end

    def Function_19_70E4(): pass

    label("Function_19_70E4")


    def lambda_70EA():

        label("loc_70EA")

        OP_99(0xFE, 0x39, 0x3B, 0xDAC)
        OP_48()
        Jump("loc_70EA")

    QueueWorkItem2(0xFE, 1, lambda_70EA)
    Return()

    # Function_19_70E4 end

    def Function_20_70F8(): pass

    label("Function_20_70F8")

    SetChrSubChip(0x13, 0)

    def lambda_7103():
        OP_99(0xFE, 0x0, 0x1F, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7103)

    def lambda_7113():
        OP_8F(0xFE, 0x184BEC, 0xBC48, 0x1D4C0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7113)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_20_70F8 end

    def Function_21_712E(): pass

    label("Function_21_712E")


    def lambda_7134():
        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7134)
    WaitChrThread(0xFE, 0x1)

    def lambda_7149():
        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7149)
    WaitChrThread(0xFE, 0x1)

    def lambda_715E():
        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_715E)
    WaitChrThread(0xFE, 0x1)

    def lambda_7173():
        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7173)
    WaitChrThread(0xFE, 0x1)

    def lambda_7188():
        OP_99(0xFE, 0x3C, 0x3E, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7188)
    WaitChrThread(0xFE, 0x1)

    def lambda_719D():
        OP_99(0xFE, 0x3D, 0x3C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_719D)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x1)

    def lambda_71B6():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_71B6)
    WaitChrThread(0xFE, 0x1)

    def lambda_71CB():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_71CB)
    WaitChrThread(0xFE, 0x1)

    def lambda_71E0():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_71E0)
    WaitChrThread(0xFE, 0x1)

    def lambda_71F5():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_71F5)
    WaitChrThread(0xFE, 0x1)

    def lambda_720A():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_720A)
    WaitChrThread(0xFE, 0x1)

    def lambda_721F():
        OP_99(0xFE, 0x42, 0x44, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_721F)
    WaitChrThread(0xFE, 0x1)

    def lambda_7234():

        label("loc_7234")

        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        OP_48()
        Jump("loc_7234")

    QueueWorkItem2(0xFE, 1, lambda_7234)
    Return()

    # Function_21_712E end

    def Function_22_7242(): pass

    label("Function_22_7242")


    def lambda_7248():
        OP_99(0xFE, 0x3C, 0x3E, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7248)
    WaitChrThread(0xFE, 0x1)

    def lambda_725D():
        OP_99(0xFE, 0x3D, 0x3C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_725D)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x1)

    def lambda_7276():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7276)
    WaitChrThread(0xFE, 0x1)

    def lambda_728B():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_728B)
    WaitChrThread(0xFE, 0x1)

    def lambda_72A0():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_72A0)
    WaitChrThread(0xFE, 0x1)

    def lambda_72B5():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_72B5)
    WaitChrThread(0xFE, 0x1)

    def lambda_72CA():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_72CA)
    WaitChrThread(0xFE, 0x1)

    def lambda_72DF():
        OP_99(0xFE, 0x42, 0x44, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_72DF)
    WaitChrThread(0xFE, 0x1)

    def lambda_72F4():

        label("loc_72F4")

        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        OP_48()
        Jump("loc_72F4")

    QueueWorkItem2(0xFE, 1, lambda_72F4)
    Return()

    # Function_22_7242 end

    def Function_23_7302(): pass

    label("Function_23_7302")


    def lambda_7308():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7308)
    WaitChrThread(0xFE, 0x1)

    def lambda_731D():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_731D)
    WaitChrThread(0xFE, 0x1)

    def lambda_7332():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7332)
    WaitChrThread(0xFE, 0x1)

    def lambda_7347():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7347)
    WaitChrThread(0xFE, 0x1)

    def lambda_735C():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_735C)
    WaitChrThread(0xFE, 0x1)

    def lambda_7371():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7371)
    WaitChrThread(0xFE, 0x1)

    def lambda_7386():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7386)
    WaitChrThread(0xFE, 0x1)

    def lambda_739B():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_739B)
    WaitChrThread(0xFE, 0x1)

    def lambda_73B0():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_73B0)
    WaitChrThread(0xFE, 0x1)

    def lambda_73C5():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_73C5)
    WaitChrThread(0xFE, 0x1)

    def lambda_73DA():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_73DA)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_23_7302 end

    def Function_24_73EA(): pass

    label("Function_24_73EA")


    def lambda_73F0():
        OP_8F(0xFE, 0x4CEFA, 0xFDE8, 0xFFFDE25C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_73F0)

    def lambda_740B():
        OP_99(0xFE, 0x0, 0x2C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_740B)
    WaitChrThread(0xFE, 0x1)

    def lambda_7420():

        label("loc_7420")

        OP_99(0xFE, 0x39, 0x3B, 0xDAC)
        OP_48()
        Jump("loc_7420")

    QueueWorkItem2(0xFE, 1, lambda_7420)
    Return()

    # Function_24_73EA end

    def Function_25_742E(): pass

    label("Function_25_742E")

    Sleep(350)
    ClearChrFlags(0xFE, 0x80)

    def lambda_743E():
        OP_8F(0xFE, 0x4C72A, 0x186A0, 0xFFFDCED4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_743E)

    def lambda_7459():

        label("loc_7459")

        OP_99(0xFE, 0x21, 0x3F, 0x9C4)
        OP_48()
        Jump("loc_7459")

    QueueWorkItem2(0xFE, 1, lambda_7459)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_25_742E end

    def Function_26_746C(): pass

    label("Function_26_746C")

    OP_24(0x17A, 0x5A)
    OP_24(0x85, 0x5A)
    OP_24(0x96, 0x5A)
    Sleep(300)
    OP_24(0x17A, 0x50)
    OP_24(0x85, 0x50)
    OP_24(0x96, 0x50)
    Sleep(300)
    OP_24(0x17A, 0x46)
    OP_24(0x85, 0x46)
    OP_24(0x96, 0x46)
    Sleep(300)
    OP_24(0x17A, 0x3C)
    OP_24(0x85, 0x3C)
    OP_24(0x96, 0x3C)
    Sleep(300)
    OP_24(0x17A, 0x32)
    OP_24(0x85, 0x32)
    OP_24(0x96, 0x32)
    Sleep(300)
    OP_24(0x17A, 0x28)
    OP_24(0x85, 0x28)
    OP_24(0x96, 0x28)
    Sleep(300)
    OP_24(0x17A, 0x1E)
    OP_24(0x85, 0x1E)
    OP_24(0x96, 0x1E)
    Sleep(300)
    OP_24(0x17A, 0x14)
    OP_24(0x85, 0x14)
    OP_24(0x96, 0x14)
    Sleep(300)
    OP_24(0x17A, 0xA)
    OP_24(0x85, 0xA)
    OP_24(0x96, 0xA)
    Sleep(300)
    OP_24(0x17A, 0x0)
    OP_24(0x85, 0x0)
    OP_24(0x96, 0x0)
    OP_23(0x17A)
    OP_23(0x85)
    OP_23(0x96)
    Return()

    # Function_26_746C end

    def Function_27_751B(): pass

    label("Function_27_751B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp205_05.eff")
    LoadEffect(0x1, "map\\mp205_06.eff")
    OP_C4(0x0, 0x20000)
    SetChrFlags(0x11, 0x2000)
    SetChrFlags(0x12, 0x2000)
    SetChrFlags(0x13, 0x2000)
    SetChrFlags(0x11, 0x1000)
    SetChrFlags(0x12, 0x1000)
    SetChrFlags(0x13, 0x1000)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 64)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 33)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(313500, 47500, -117060, 0)
    OP_67(0, -1840, -10000, 0)
    OP_6B(50, 0)
    OP_6C(0, 0)
    OP_6E(572, 0)
    OP_D0(-30140, 0)
    PlayEffect(0x0, 0x0, 0xFF, 300350, -1000, 0, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, 300350, -1000, 0, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, 594360, 50000, -12280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x32E, 0x1, 0x64)
    OP_22(0x85, 0x1, 0x64)
    OP_22(0x96, 0x0, 0x64)

    def lambda_76D3():

        label("loc_76D3")

        OP_7C(0x96, 0x96, 0xBB8, 0x64)
        OP_48()
        Jump("loc_76D3")

    QueueWorkItem2(0x10, 3, lambda_76D3)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x11, 314130, 65000, -114660, 0)
    SetChrPos(0x12, 314130, 47500, -114660, 0)
    SetChrPos(0x13, 314130, 48000, -114660, 0)
    OP_43(0x11, 0x0, 0x0, 0x20)
    OP_43(0x12, 0x0, 0x0, 0x1F)
    FadeToBright(1000, 0)

    def lambda_773D():
        OP_6D(314080, 57500, -118060, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_773D)

    def lambda_7755():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7755)

    def lambda_7765():
        OP_6E(523, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_7765)

    def lambda_7775():
        OP_D0(-50860, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7775)

    def lambda_7785():
        OP_67(0, 4200, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7785)
    Sleep(1000)
    WaitChrThread(0x12, 0x0)

    def lambda_77A7():
        OP_67(0, 4200, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_77A7)
    OP_43(0x13, 0x0, 0x0, 0x21)

    def lambda_77C6():
        OP_99(0xFE, 0x21, 0x2C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_77C6)
    WaitChrThread(0x12, 0x1)

    def lambda_77DB():

        label("loc_77DB")

        OP_99(0xFE, 0x39, 0x3C, 0xDAC)
        OP_48()
        Jump("loc_77DB")

    QueueWorkItem2(0x12, 1, lambda_77DB)
    Sleep(500)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x13, 0x0)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x2)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_44(0x10F, 0x0)
    OP_6D(593280, 50000, 72610, 0)
    OP_67(0, -200, -10000, 0)
    OP_6B(10000, 0)
    OP_6C(180000, 0)
    OP_6E(729, 0)
    OP_D0(0, 0)
    SetChrPos(0x11, 594370, 47100, 154140, 0)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 45)
    SetChrPos(0x13, 592370, 47300, 160140, 0)
    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 0)

    def lambda_78A7():
        OP_6E(924, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_78A7)

    def lambda_78B7():
        OP_D0(-25600, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_78B7)
    OP_43(0x11, 0x0, 0x0, 0x1E)
    OP_43(0x13, 0x0, 0x0, 0x1D)
    Sleep(700)

    def lambda_78DA():
        OP_6E(924, 500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_78DA)
    Sleep(500)

    def lambda_78EF():
        OP_6B(8000, 800)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_78EF)
    Sleep(500)
    OP_82(0x2, 0x0)
    OP_44(0x10F, 0x0)
    OP_44(0x10F, 0x1)
    OP_44(0x10F, 0x2)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_6D(305250, 30000, -6140, 0)
    OP_67(0, 9950, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(42000, 0)
    OP_6E(761, 0)
    OP_D0(10000, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 290520, 60000, -30450, 0)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 48)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 290520, 10000, 500, 0)
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 45)
    SetChrFlags(0x13, 0x80)
    OP_82(0x1, 0x0)

    def lambda_79A9():
        OP_6D(300250, 30000, -5140, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_79A9)

    def lambda_79C1():
        OP_67(0, 17620, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_79C1)

    def lambda_79D9():
        OP_6B(4300, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_79D9)

    def lambda_79E9():
        OP_6E(777, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_79E9)

    def lambda_79F9():
        OP_D0(3000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_79F9)
    OP_43(0x11, 0x0, 0x0, 0x1C)

    def lambda_7A10():

        label("loc_7A10")

        OP_99(0xFE, 0x39, 0x3C, 0xDAC)
        OP_48()
        Jump("loc_7A10")

    QueueWorkItem2(0x12, 0, lambda_7A10)

    def lambda_7A23():
        OP_8F(0xFE, 0x44C14, 0x2904, 0x27D8, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7A23)

    def lambda_7A3E():
        OP_8F(0xFE, 0x447C8, 0x2710, 0x251C, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7A3E)
    Sleep(1500)
    OP_22(0x99, 0x0, 0x64)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_43(0x109, 0x1, 0x0, 0x22)
    WaitChrThread(0x109, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    Sleep(2000)
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_C4(0x1, 0x20000)
    Sleep(3000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_751B end

    def Function_28_7ACF(): pass

    label("Function_28_7ACF")


    def lambda_7AD5():

        label("loc_7AD5")

        OP_99(0xFE, 0x39, 0x3B, 0xDAC)
        OP_48()
        Jump("loc_7AD5")

    QueueWorkItem2(0xFE, 1, lambda_7AD5)
    Return()

    # Function_28_7ACF end

    def Function_29_7AE3(): pass

    label("Function_29_7AE3")


    def lambda_7AE9():
        OP_99(0xFE, 0x0, 0x1F, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AE9)

    def lambda_7AF9():
        OP_8F(0xFE, 0x909F2, 0xBCAC, 0x1D54C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7AF9)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_29_7AE3 end

    def Function_30_7B14(): pass

    label("Function_30_7B14")


    def lambda_7B1A():
        OP_99(0xFE, 0x3C, 0x3E, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B1A)
    WaitChrThread(0xFE, 0x1)

    def lambda_7B2F():
        OP_99(0xFE, 0x3D, 0x3C, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B2F)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x1)

    def lambda_7B48():
        OP_99(0xFE, 0x40, 0x43, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B48)
    WaitChrThread(0xFE, 0x1)

    def lambda_7B5D():
        OP_99(0xFE, 0x41, 0x43, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B5D)
    WaitChrThread(0xFE, 0x1)

    def lambda_7B72():
        OP_99(0xFE, 0x41, 0x43, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B72)
    WaitChrThread(0xFE, 0x1)

    def lambda_7B87():
        OP_99(0xFE, 0x42, 0x44, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B87)
    WaitChrThread(0xFE, 0x1)

    def lambda_7B9C():

        label("loc_7B9C")

        OP_99(0xFE, 0x2D, 0x2F, 0xDAC)
        OP_48()
        Jump("loc_7B9C")

    QueueWorkItem2(0xFE, 1, lambda_7B9C)
    Return()

    # Function_30_7B14 end

    def Function_31_7BAA(): pass

    label("Function_31_7BAA")


    def lambda_7BB0():
        OP_99(0xFE, 0x6, 0x7, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BB0)
    WaitChrThread(0xFE, 0x1)

    def lambda_7BC5():
        OP_99(0xFE, 0x6, 0x7, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BC5)
    WaitChrThread(0xFE, 0x1)

    def lambda_7BDA():
        OP_99(0xFE, 0x6, 0x7, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BDA)
    WaitChrThread(0xFE, 0x1)

    def lambda_7BEF():
        OP_99(0xFE, 0x6, 0x7, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BEF)
    WaitChrThread(0xFE, 0x1)

    def lambda_7C04():
        OP_99(0xFE, 0x8, 0x20, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C04)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_31_7BAA end

    def Function_32_7C14(): pass

    label("Function_32_7C14")


    def lambda_7C1A():
        OP_8F(0xFE, 0x4CEFA, 0xFDE8, 0xFFFDE25C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7C1A)

    def lambda_7C35():
        OP_99(0xFE, 0x0, 0x2C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C35)
    WaitChrThread(0xFE, 0x1)

    def lambda_7C4A():

        label("loc_7C4A")

        OP_99(0xFE, 0x39, 0x3B, 0xDAC)
        OP_48()
        Jump("loc_7C4A")

    QueueWorkItem2(0xFE, 1, lambda_7C4A)
    Return()

    # Function_32_7C14 end

    def Function_33_7C58(): pass

    label("Function_33_7C58")

    Sleep(400)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7C68():
        OP_8F(0xFE, 0x4CB12, 0x186A0, 0xFFFDDA8C, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7C68)

    def lambda_7C83():

        label("loc_7C83")

        OP_99(0xFE, 0x21, 0x3F, 0xDAC)
        OP_48()
        Jump("loc_7C83")

    QueueWorkItem2(0xFE, 1, lambda_7C83)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_33_7C58 end

    def Function_34_7C96(): pass

    label("Function_34_7C96")

    OP_24(0x32E, 0x5A)
    OP_24(0x85, 0x5A)
    OP_24(0x96, 0x5A)
    Sleep(300)
    OP_24(0x32E, 0x50)
    OP_24(0x85, 0x50)
    OP_24(0x96, 0x50)
    Sleep(300)
    OP_24(0x32E, 0x46)
    OP_24(0x85, 0x46)
    OP_24(0x96, 0x46)
    Sleep(300)
    OP_24(0x32E, 0x3C)
    OP_24(0x85, 0x3C)
    OP_24(0x96, 0x3C)
    Sleep(300)
    OP_24(0x32E, 0x32)
    OP_24(0x85, 0x32)
    OP_24(0x96, 0x32)
    Sleep(300)
    OP_24(0x32E, 0x28)
    OP_24(0x85, 0x28)
    OP_24(0x96, 0x28)
    Sleep(300)
    OP_24(0x32E, 0x1E)
    OP_24(0x85, 0x1E)
    OP_24(0x96, 0x1E)
    Sleep(300)
    OP_24(0x32E, 0x14)
    OP_24(0x85, 0x14)
    OP_24(0x96, 0x14)
    Sleep(300)
    OP_24(0x32E, 0xA)
    OP_24(0x85, 0xA)
    OP_24(0x96, 0xA)
    Sleep(300)
    OP_24(0x32E, 0x0)
    OP_24(0x85, 0x0)
    OP_24(0x96, 0x0)
    OP_23(0x32E)
    OP_23(0x85)
    OP_23(0x96)
    Return()

    # Function_34_7C96 end

    SaveToFile()

Try(main)
