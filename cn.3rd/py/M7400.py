from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7400   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60225",
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
        '提妲',                                 # 9
        '尤莉亚\u3000\u3000\u3000\u3000\u3000\u3000\u3000',# 10
        '穆拉',                                 # 11
        '乔丝特',                               # 12
        '约修亚',                               # 13
        '科洛丝',                               # 14
        '基库',                                 # 15
        '奥利维尔',                             # 16
        '金',                                   # 17
        '亚妮拉丝',                             # 18
        '雪拉扎德',                             # 19
        '阿加特',                               # 20
        '艾丝蒂尔',                             # 21
        '理查德',                               # 22
        '玲',                                   # 23
        '莉丝',                                 # 24
        '凯文',                                 # 25
        '赛雷斯托',                             # 26
        '基尔巴特',                             # 27
        '',                                     # 28
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
        'ED6_DT27/CH03080 ._CH',             # 00
        'ED6_DT27/CH03080 ._CH',             # 01
        'ED6_DT27/CH03470 ._CH',             # 02
        'ED6_DT07/CH00060 ._CH',             # 03
        'ED6_DT27/CH03580 ._CH',             # 04
        'ED6_DT27/CH03570 ._CH',             # 05
        'ED6_DT27/CH03100 ._CH',             # 06
        'ED6_DT27/CH03250 ._CH',             # 07
        'ED6_DT27/CH03210 ._CH',             # 08
        'ED6_DT07/CH02323 ._CH',             # 09
        'ED6_DT27/CH03260 ._CH',             # 0A
        'ED6_DT07/CH00070 ._CH',             # 0B
        'ED6_DT07/CH01630 ._CH',             # 0C
        'ED6_DT27/CH03240 ._CH',             # 0D
        'ED6_DT06/CH20053 ._CH',             # 0E
        'ED6_DT27/CH03000 ._CH',             # 0F
        'ED6_DT07/CH02030 ._CH',             # 10
        'ED6_DT27/CH03510 ._CH',             # 11
        'ED6_DT07/CH02891 ._CH',             # 12
        'ED6_DT27/CH03750 ._CH',             # 13
        'ED6_DT26/CH20454 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT27/CH03080P._CP',             # 00
        'ED6_DT27/CH03080P._CP',             # 01
        'ED6_DT27/CH03470P._CP',             # 02
        'ED6_DT07/CH00060P._CP',             # 03
        'ED6_DT27/CH03580P._CP',             # 04
        'ED6_DT27/CH03570P._CP',             # 05
        'ED6_DT27/CH03100P._CP',             # 06
        'ED6_DT27/CH03250P._CP',             # 07
        'ED6_DT27/CH03210P._CP',             # 08
        'ED6_DT07/CH02323P._CP',             # 09
        'ED6_DT27/CH03260P._CP',             # 0A
        'ED6_DT07/CH00070P._CP',             # 0B
        'ED6_DT07/CH01630P._CP',             # 0C
        'ED6_DT27/CH03240P._CP',             # 0D
        'ED6_DT06/CH20053P._CP',             # 0E
        'ED6_DT27/CH03000P._CP',             # 0F
        'ED6_DT07/CH02030P._CP',             # 10
        'ED6_DT27/CH03510P._CP',             # 11
        'ED6_DT07/CH02891P._CP',             # 12
        'ED6_DT27/CH03750P._CP',             # 13
        'ED6_DT26/CH20454P._CP',             # 14
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_3B2",          # 00, 0
        "Function_1_3CF",          # 01, 1
        "Function_2_3E9",          # 02, 2
        "Function_3_270D",         # 03, 3
        "Function_4_2776",         # 04, 4
        "Function_5_27DA",         # 05, 5
        "Function_6_2843",         # 06, 6
        "Function_7_28AC",         # 07, 7
        "Function_8_2915",         # 08, 8
        "Function_9_2979",         # 09, 9
        "Function_10_29E2",        # 0A, 10
        "Function_11_2A4B",        # 0B, 11
        "Function_12_2A9B",        # 0C, 12
        "Function_13_2AEB",        # 0D, 13
        "Function_14_2B3B",        # 0E, 14
        "Function_15_2B8B",        # 0F, 15
        "Function_16_2C2B",        # 10, 16
        "Function_17_2CCB",        # 11, 17
        "Function_18_2D84",        # 12, 18
    )


    def Function_0_3B2(): pass

    label("Function_0_3B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3CE")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_3CE")

    Return()

    # Function_0_3B2 end

    def Function_1_3CF(): pass

    label("Function_1_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E8")

    Return()

    # Function_1_3CF end

    def Function_2_3E9(): pass

    label("Function_2_3E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed6_dt49.dat", 0xCC, 0x1)

    label("loc_419")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_433")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_430")
    Jump("loc_433")

    label("loc_430")

    Jump("loc_419")

    label("loc_433")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C4(0x1, 0x10)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 2090, 1000, -2950, 0)

    def lambda_4DE():

        label("loc_4DE")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_4DE")

    QueueWorkItem2(0x21, 0, lambda_4DE)
    OP_9F(0x21, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    PlayEffect(0x0, 0x7, 0x21, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x20, -1190, 0, -3000, 0)
    SetChrPos(0x1F, 10, 0, -3270, 0)
    SetChrPos(0x1C, -1350, 0, -5090, 0)
    SetChrPos(0x14, -360, 0, -5480, 0)
    SetChrPos(0x1E, -2690, 0, -5060, 0)
    SetChrPos(0x10, -4019, 0, -5520, 0)
    SetChrPos(0x11, -2740, 0, -8150, 0)
    SetChrPos(0x12, -1450, 0, -8450, 0)
    SetChrPos(0x13, 810, 0, -5930, 0)
    SetChrPos(0x15, -2060, 0, -6760, 0)
    SetChrPos(0x17, -890, 0, -7140, 0)
    SetChrPos(0x18, 100, 0, -8530, 0)
    SetChrPos(0x19, -4700, 0, -6990, 0)
    SetChrPos(0x1A, -3500, 0, -6840, 0)
    SetChrPos(0x1B, -4150, 0, -8130, 0)
    SetChrPos(0x1D, 700, 0, -7110, 0)
    SetChrSubChip(0x15, 3)
    OP_72(0x400, 0x0)
    ExitThread()
    OP_6D(0, 28900, 29080, 0)
    OP_67(0, 4310, -10000, 0)
    OP_6B(6460, 0)
    OP_6C(0, 0)
    OP_6E(346, 0)

    def lambda_689():
        OP_6D(0, 6100, 20180, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_689)

    def lambda_6A1():
        OP_67(0, 3150, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_6A1)

    def lambda_6B9():
        OP_6B(6750, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_6B9)

    def lambda_6C9():
        OP_6E(432, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_6C9)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x2)
    Fade(1000)
    OP_6D(5200, 0, 25130, 0)
    OP_67(0, 7360, -10000, 0)
    OP_6B(7130, 0)
    OP_6C(45000, 0)
    OP_6E(345, 0)

    def lambda_72A():
        OP_6D(-200, 0, -4000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_72A)

    def lambda_742():
        OP_67(0, 9000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_742)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Fade(1000)
    OP_6D(0, 0, -4140, 0)
    OP_67(0, 5910, -10000, 0)
    OP_6B(2630, 0)
    OP_6C(45000, 0)
    OP_6E(335, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x14,
        (
            "#1502F#12P这里……\x01",
            "好像是『城』的玄关。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x1C,
        (
            "#1002F#6P怎、怎么有\x01",
            "这么多入口……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x1F,
        (
            "#1935F#5P这种构造……\x02\x03",

            "#1933F和亚尔特利亚的\x01",
            "大圣堂风格很像呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x20,
        "#1067F#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1F, 270, 400)

    def lambda_898():

        label("loc_898")

        TurnDirection(0xFE, 0x20, 400)
        OP_48()
        Jump("loc_898")

    QueueWorkItem2(0x1F, 3, lambda_898)
    Sleep(300)

    ChrTalk(    #4
        0x1F,
        "#1934F#11P……凯文……？\x02",
    )

    CloseMessageWindow()

    def lambda_8D3():
        OP_6D(260, 0, -2000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_8D3)
    OP_8E(0x20, 0xFFFFFC4A, 0x0, 0xFFFFF894, 0x5DC, 0x0)
    OP_44(0x1F, 0x3)
    OP_8C(0x1F, 0, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #5
        0x20,
        (
            "#1069F#6P露菲娜姐姐……\x01",
            "不──『影之王』！\x02\x03",

            "我知道你在里面！\x02\x03",

            "我已经决定……\x01",
            "不再逃避也不再躲藏！\x02\x03",

            "差不多该在这里\x01",
            "做个了结吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #6
        "\x07\x02#40W呵呵，来得正好……\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #7
        (
            "\x07\x02#40W欢迎来到我的『幻影城』。\x02\x03",

            "#40W事到如今已无须多言──\x01",
            "来，让我们开始最后的游戏吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    OP_22(0xD2, 0x1, 0x64)
    Sleep(500)
    OP_22(0x85, 0x1, 0x3C)

    def lambda_C5E():

        label("loc_C5E")

        OP_7C(0x5, 0x5, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_C5E")

    QueueWorkItem2(0x21, 3, lambda_C5E)
    Sleep(500)
    OP_22(0x85, 0x1, 0x50)

    def lambda_C83():

        label("loc_C83")

        OP_7C(0xA, 0xA, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_C83")

    QueueWorkItem2(0x21, 3, lambda_C83)
    Sleep(500)
    Fade(1000)
    OP_6D(0, -4100, 27150, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(5730, 0)
    OP_6C(0, 0)
    OP_6E(539, 0)
    OP_72(0x400, 0x0)
    ExitThread()
    OP_22(0x85, 0x1, 0x64)

    def lambda_CF0():

        label("loc_CF0")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_CF0")

    QueueWorkItem2(0x21, 3, lambda_CF0)

    def lambda_D0B():
        OP_6D(0, 3900, 31950, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_D0B)

    def lambda_D23():
        OP_67(0, 2210, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_D23)

    def lambda_D3B():
        OP_6B(6460, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_D3B)

    def lambda_D4B():
        OP_6E(554, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_D4B)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 0)
    OP_70(0x1, 0xDC)
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_B0(0x2, 0x1E)
    OP_6F(0x2, 0)
    OP_70(0x2, 0xDC)
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 0)
    OP_70(0x3, 0xDC)
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_B0(0x4, 0x1E)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x118)
    OP_73(0x1)
    OP_73(0x2)
    OP_73(0x3)
    OP_73(0x4)
    OP_44(0x21, 0x3)
    OP_23(0xD2)
    OP_23(0x85)
    OP_7C(0x190, 0x190, 0xBB8, 0x64)
    OP_22(0x88, 0x0, 0x50)
    WaitChrThread(0xEE, 0x0)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #8
        (
            "\x07\x02#40W『赎罪之人』及其同伴\x01",
            "请进入屹立在上方的大门……\x02\x03",

            "其他人请平均分散进入三扇门……\x02\x03",

            "我在各自的终点为你们准备了\x01",
            "充满趣味的节目。\x02\x03",

            "呵呵，\x01",
            "那么就预祝彼此都玩得愉快吧。\x07\x00\x02",
        )
    )

    Jump("loc_ED5")

    label("loc_ED5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(500)
    OP_6D(700, 0, -6620, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(2660, 0)
    OP_6C(140000, 0)
    OP_6E(339, 0)
    SetChrPos(0x21, 1960, 1000, -2610, 0)
    SetChrPos(0x20, -830, 0, -2020, 0)
    SetChrPos(0x1F, 790, 0, -3520, 0)
    SetChrPos(0x1C, -690, 0, -5190, 0)
    SetChrPos(0x14, 380, 0, -5220, 0)
    SetChrPos(0x1E, -2040, 0, -4950, 0)
    SetChrPos(0x10, -3050, 0, -5250, 0)
    SetChrPos(0x11, -2260, 0, -8150, 0)
    SetChrPos(0x12, -820, 0, -8300, 0)
    SetChrPos(0x13, 1670, 0, -6400, 0)
    SetChrPos(0x15, -1190, 0, -6860, 0)
    SetChrPos(0x17, 100, 0, -7000, 0)
    SetChrPos(0x18, 750, 0, -8620, 0)
    SetChrPos(0x19, -3950, 0, -5920, 0)
    SetChrPos(0x1A, -2400, 0, -6850, 0)
    SetChrPos(0x1B, -3750, 0, -7360, 0)
    SetChrPos(0x1D, 1640, 0, -7650, 0)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_62(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x20, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x18, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1E, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x20)
    OP_63(0x1F)
    OP_63(0x1C)
    OP_63(0x14)
    OP_63(0x21)
    OP_63(0x18)
    OP_63(0x11)
    OP_63(0x15)
    OP_63(0x12)
    OP_63(0x17)
    OP_63(0x13)
    OP_63(0x1B)
    OP_63(0x19)
    OP_63(0x1A)
    OP_63(0x1E)
    OP_63(0x1D)
    OP_63(0x21)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #9
        0x20,
        "#1063F#11P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x1F,
        "#1942F#11P姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x21,
        (
            "\x07\x0C#1615F#5P到最后还要\x01",
            "拘泥于『规则』吗。\x02\x03",

            "#1613F恐怕不这样做\x01",
            "就无法到达\x01",
            "『影之王』所在之处吧。\x02\x03",

            "#1610F……然而某种意义上来说\x01",
            "她本身也是基于『规则』\x01",
            "才得以存在。\x02\x03",

            "我想应该不会\x01",
            "设置什么陷阱。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x1C,
        (
            "#1006F#11P……完全是打算\x01",
            "堂堂正正地击溃我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x14,
        "#1513F#5P嗯……看来是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x1E,
        (
            "#263F#11P嘻嘻……\x01",
            "招待得相当周到嘛。\x02\x03",

            "#1306F玲啊，\x01",
            "感觉有些兴奋起来了⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x19,
        (
            "#816F#11P啊哈哈……\x01",
            "好像可以理解。\x02\x03",

            "#1315F我倒是一半兴奋，\x01",
            "一半担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x1A,
        (
            "#1536F#11P算了，\x01",
            "既然被卷进这里来，\x01",
            "也得送个回礼才行嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x1B,
        (
            "#051F#11P既然对方来挑衅\x01",
            "就开开心心的接受好啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        "#067F#6P阿、阿加特大哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x1D,
        (
            "#110F#5P无论如何……\x01",
            "看来这是避不开的路了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#176F#11P这个『影之国』\x01",
            "是否会给利贝尔\x01",
            "带来新的灾祸……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x15,
        (
            "#1162F#11P就算为了确认这一点\x01",
            "也不能置之不理。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #22
        0x15,
        "基库",
        "#311F#5P啾！\x02",
    )

    Jump("loc_15BA")

    label("loc_15BA")

    CloseMessageWindow()

    ChrTalk(    #23
        0x13,
        (
            "#413F#5P我……\x01",
            "要早点回到哥哥们身边\x01",
            "让他们放心才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x18,
        (
            "#071F#5P哈哈，\x01",
            "我要是回去太迟\x01",
            "也会被雾香痛扁一顿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x17,
        (
            "#1541F#5P呼，\x01",
            "我倒是希望能继续\x01",
            "像这样和大家在一起……\x02\x03",

            "#1540F不过，\x01",
            "看来是没办法了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x12,
        "#274F#11P这是当然的了，呆子。\x02",
    )

    CloseMessageWindow()

    def lambda_16D7():
        OP_6D(700, 0, -7100, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_16D7)

    def lambda_16EF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_16EF)
    Sleep(100)

    def lambda_1702():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1702)
    Sleep(100)
    OP_8C(0x21, 225, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #27
        0x1F,
        "#1946F#6P大家……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x20,
        (
            "#1075F#6P……看来大家的心情\x01",
            "都是一致的呢。\x02\x03",

            "#1078F那么就按照这些门\x01",
            "分成四组行动吧。\x02\x03",

            "其中的大门……\x01",
            "就由我和莉丝进去。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x21, 270, 400)
    Sleep(300)

    ChrTalk(    #29
        0x21,
        (
            "\x07\x0C#1616F#5P嗯……\x01",
            "就这样吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_180C():
        OP_6D(1200, 0, -6700, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_180C)

    def lambda_1824():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1824)
    Sleep(100)
    OP_8C(0x1F, 90, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #30
        0x21,
        (
            "\x07\x0C#1612F#5P估计大门里面\x01",
            "是最危险最困难的道路。\x02\x03",

            "因此人员的分配\x01",
            "最好慎重决定。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18AB():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_18AB)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x0)
    Sleep(1000)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x21, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C4(0x0, 0x10)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x1A2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05保存到此为止的过程吗？\x18\x02",
    )

    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存】\x01",          # 0
            "【继续进行】\x01",      # 1
        )
    )

    Jump("loc_19B9")

    label("loc_19B9")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CF")
    ShowSaveMenu()

    label("loc_19CF")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0xBB8)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(3000)
    OP_A3(0x2582)
    OP_C4(0x1, 0x10)
    OP_21()
    OP_1D(0xD5)
    ClearMapFlags(0x2000000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "\x07\x05右门　拦路的是金色巨人\x01",
            "左门　拦路的是黑色幻想\x01",
            "正门　拦路的是红色圣兽\x01",
            "大门　拦路的是世界之意志\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    ClearParty()
    OP_AA(8192)
    OP_DD(0x4, 0x0, 0x0, 0, 0, 0, 16640)
    OP_DC(0x0, 0x0)
    FadeToDark(0, 0, -1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C10")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "\x07\x05\x18\x06右门　拦路的是金色巨人\x01",
            "左门　拦路的是黑色幻想\x01",
            "正门　拦路的是红色圣兽\x01",
            "大门　拦路的是世界之意志\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        300,
        0,
        (
            "【替换装备】\x01",      # 0
            "【重新编队】\x01",      # 1
            "【继续进行】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B9E"),
        (1, "loc_1BDF"),
        (SWITCH_DEFAULT, "loc_1C00"),
    )


    label("loc_1B9E")

    OP_C4(0x0, 0x200)
    OP_C2(0x1, 0x78)
    OP_C0(0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C2(0x1, 0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x1, 0x200)
    Jump("loc_1C0D")

    label("loc_1BDF")

    OP_DD(0x4, 0x0, 0x0, 0, 0, 0, 16640)
    FadeToDark(0, 0, -1)
    Jump("loc_1C0D")

    label("loc_1C00")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C0D")

    label("loc_1C0D")

    Jump("loc_1AC0")

    label("loc_1C10")

    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_DF(0x0, 0x1, 0x1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 220)
    OP_70(0x1, 0xDC)
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_B0(0x2, 0x1E)
    OP_6F(0x2, 220)
    OP_70(0x2, 0xDC)
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 220)
    OP_70(0x3, 0xDC)
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_B0(0x4, 0x1E)
    OP_6F(0x4, 280)
    OP_70(0x4, 0x118)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 2480, 500, 5290, 0)
    SetChrFlags(0x21, 0x4)

    def lambda_1CBB():

        label("loc_1CBB")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_1CBB")

    QueueWorkItem2(0x21, 0, lambda_1CBB)
    OP_9F(0x21, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    PlayEffect(0x0, 0x7, 0x21, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0xEE, 810, 0, 1950, 0)
    SetChrPos(0xEF, 2330, 0, 2120, 0)
    SetChrPos(0xF0, 920, 0, 100, 0)
    SetChrPos(0xF1, 2850, 0, 850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrFlags(0x5, 0x80)
    ClearChrFlags(0x6, 0x80)
    ClearChrFlags(0x7, 0x80)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    SetChrPos(0xF2, -3250, 0, 2460, 0)
    SetChrPos(0xF3, -5040, 0, 1720, 0)
    SetChrPos(0xF4, -2900, 0, 880, 0)
    SetChrPos(0xF5, -4700, 0, 70, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    SetChrPos(0xF6, -1290, 0, 260, 0)
    SetChrPos(0xF7, -3190, 0, -980, 0)
    SetChrPos(0xF8, -590, 0, -980, 0)
    SetChrPos(0xF9, -2390, 0, -2490, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    SetChrPos(0xFA, -690, 0, 5300, 0)
    SetChrPos(0xFB, 620, 0, 5040, 0)
    SetChrPos(0xFC, -1460, 0, 3330, 0)
    SetChrPos(0xFD, 360, 0, 3180, 0)
    OP_6D(1600, 0, 6000, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(45000, 0)
    OP_6E(244, 0)
    Sleep(2000)

    def lambda_1F00():
        OP_6B(3650, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1F00)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #34
        0x10F,
        (
            "#1932F#12P现在……\x01",
            "已经全部准备好了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x109,
        (
            "#1075F#6P嗯……\x01",
            "差不多该出发了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x21, 270, 400)
    Sleep(300)

    ChrTalk(    #36
        0x21,
        (
            "\x07\x0C#1616F#11P……祝大家好运。\x02\x03",

            "#1611F如果基尔巴特先生到了的话\x01",
            "就由我来向他说明事由吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FFC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1FFC)
    Sleep(100)
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #37
        0x109,
        (
            "#1840F#6P哈哈……\x01",
            "那就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_204B():
        OP_6D(500, 0, 4000, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_204B)

    def lambda_2063():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2063)
    Sleep(100)

    def lambda_2076():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2076)
    Sleep(100)
    OP_8C(0x21, 225, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #38
        0x109,
        (
            "#1065F#5P……事到如今\x01",
            "就不说什么见外的话了。\x02\x03",

            "#1060F只有一句话……\x01",
            "我想说在前头。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 280, -1, -1)
    SetChrName("全员")

    AnonymousTalk(    #39
        "\x07\x00…………………………………\x02",
    )

    Jump("loc_2134")

    label("loc_2134")

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #40
        0x109,
        (
            "#1078F#5P各位，一会儿见！\x02\x03",

            "大家都要平平安安……\x01",
            "再次相会哦！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(350, 250, -1, -1)
    SetChrName("全员")

    AnonymousTalk(    #41
        "\x07\x00#5S 是！\x02",
    )

    Jump("loc_21BB")

    label("loc_21BB")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0x5DC)

    def lambda_21E3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_21E3)
    Sleep(100)

    def lambda_21F6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_21F6)
    Sleep(400)
    Fade(1000)
    OP_6D(0, 0, 4710, 0)
    OP_67(0, 7690, -10000, 0)
    OP_6B(4170, 0)
    OP_6C(0, 0)
    OP_6E(434, 0)

    def lambda_224B():
        OP_6D(0, 6950, 19500, 8000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_224B)

    def lambda_2263():
        OP_67(0, 3970, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2263)

    def lambda_227B():
        OP_6B(5620, 10000)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_227B)

    def lambda_228B():
        OP_6E(495, 10000)
        ExitThread()

    QueueWorkItem(0x22, 3, lambda_228B)
    OP_DF(0x1, 0x1, 0x1)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0xEE, 2390, 0, 2810, 0)
    SetChrPos(0xEF, 3750, 0, 2340, 0)
    SetChrPos(0xF0, 2070, 0, 830, 0)
    SetChrPos(0xF1, 3530, 0, 230, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrFlags(0x5, 0x80)
    ClearChrFlags(0x6, 0x80)
    ClearChrFlags(0x7, 0x80)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    SetChrPos(0xF2, -1980, 0, 2700, 0)
    SetChrPos(0xF3, -3530, 0, 2330, 0)
    SetChrPos(0xF4, -1670, 0, 430, 0)
    SetChrPos(0xF5, -3060, 0, 350, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    SetChrPos(0xF6, 260, 0, 1290, 0)
    SetChrPos(0xF7, -480, 0, -530, 0)
    SetChrPos(0xF8, 1300, 0, -890, 0)
    SetChrPos(0xF9, 420, 0, -1790, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    SetChrPos(0xFA, -590, 0, 5760, 0)
    SetChrPos(0xFB, 890, 0, 5610, 0)
    SetChrPos(0xFC, -820, 0, 4000, 0)
    SetChrPos(0xFD, 1290, 0, 3800, 0)
    OP_43(0xEE, 0x0, 0x0, 0x3)
    OP_43(0xEF, 0x0, 0x0, 0x4)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    OP_43(0xF2, 0x0, 0x0, 0x7)
    OP_43(0xF3, 0x0, 0x0, 0x8)
    OP_43(0xF4, 0x0, 0x0, 0x9)
    OP_43(0xF5, 0x0, 0x0, 0xA)
    OP_43(0xF6, 0x0, 0x0, 0xB)
    OP_43(0xF7, 0x0, 0x0, 0xC)
    OP_43(0xF8, 0x0, 0x0, 0xD)
    OP_43(0xF9, 0x0, 0x0, 0xE)
    OP_43(0xFA, 0x0, 0x0, 0xF)
    OP_43(0xFB, 0x0, 0x0, 0x10)
    OP_43(0xFC, 0x0, 0x0, 0x11)
    OP_43(0xFD, 0x0, 0x0, 0x12)
    Sleep(500)

    def lambda_24C4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_24C4)
    OP_21()
    OP_1D(0xE1)
    WaitChrThread(0x22, 0x0)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2C22)
    OP_28(0x3E, 0x4, 0x10)
    OP_28(0x3E, 0x4, 0x20)
    OP_28(0x40, 0x4, 0x4)
    OP_28(0x40, 0x4, 0x8)
    OP_28(0x40, 0x1, 0x1)
    OP_28(0x40, 0x1, 0x2)
    Sleep(2000)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #42
        "\x07\x05请选择行进的线路。\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_255F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_270C")
    OP_CC(0x0, 0x0, 0xFFFF, 0xAA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_END)), "loc_2590")
    OP_CC(0x1, 0x0, "右门的道路")
    OP_CC(0x3, 0x0, 0x0)
    Jump("loc_259E")

    label("loc_2590")

    OP_CC(0x1, 0x0, "右门的道路")

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_END)), "loc_25BA")
    OP_CC(0x1, 0x0, "左门的道路")
    OP_CC(0x3, 0x0, 0x1)
    Jump("loc_25C8")

    label("loc_25BA")

    OP_CC(0x1, 0x0, "左门的道路")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_END)), "loc_25E4")
    OP_CC(0x1, 0x0, "正门的道路")
    OP_CC(0x3, 0x0, 0x2)
    Jump("loc_25F2")

    label("loc_25E4")

    OP_CC(0x1, 0x0, "正门的道路")

    label("loc_25F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2612")
    OP_CC(0x1, 0x0, "大门的道路")
    Jump("loc_2624")

    label("loc_2612")

    OP_CC(0x1, 0x0, "大门的道路")
    OP_CC(0x3, 0x0, 0x3)

    label("loc_2624")

    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_264F"),
        (1, "loc_267E"),
        (2, "loc_26AD"),
        (3, "loc_26DC"),
        (SWITCH_DEFAULT, "loc_2709"),
    )


    label("loc_264F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267E")
    OP_56(0x0)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_DC(0x0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7409   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2709")

    label("loc_267E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26AD")
    OP_56(0x0)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_DC(0x0, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7413   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2709")

    label("loc_26AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26DC")
    OP_56(0x0)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_DC(0x0, 0x2)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7418   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2709")

    label("loc_26DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2709")
    OP_56(0x0)
    OP_DC(0x0, 0x3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7422   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2709")

    label("loc_2709")

    Jump("loc_255F")

    label("loc_270C")

    Return()

    # Function_2_3E9 end

    def Function_3_270D(): pass

    label("Function_3_270D")

    Sleep(800)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x20F8, 0x0, 0x29E0, 0x1388, 0x0)
    OP_8E(0xFE, 0x4074, 0x0, 0x4038, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_2750():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2750)
    OP_8E(0xFE, 0x46B4, 0x0, 0x466E, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_3_270D end

    def Function_4_2776(): pass

    label("Function_4_2776")

    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x27F6, 0x0, 0x2D46, 0x1388, 0x0)
    OP_8E(0xFE, 0x4074, 0x0, 0x4038, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_27B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27B4)
    OP_8E(0xFE, 0x46B4, 0x0, 0x466E, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_4_2776 end

    def Function_5_27DA(): pass

    label("Function_5_27DA")

    Sleep(1000)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x20C6, 0x0, 0x2238, 0x1388, 0x0)
    OP_8E(0xFE, 0x4074, 0x0, 0x4038, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_281D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_281D)
    OP_8E(0xFE, 0x46B4, 0x0, 0x466E, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_5_27DA end

    def Function_6_2843(): pass

    label("Function_6_2843")

    Sleep(300)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x288C, 0x0, 0x2620, 0x1388, 0x0)
    OP_8E(0xFE, 0x4074, 0x0, 0x4038, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_2886():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2886)
    OP_8E(0xFE, 0x46B4, 0x0, 0x466E, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_2843 end

    def Function_7_28AC(): pass

    label("Function_7_28AC")

    Sleep(800)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFDA30, 0x0, 0x260C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFBFDC, 0x0, 0x40CE, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_28EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28EF)
    OP_8E(0xFE, 0xFFFFBA28, 0x0, 0x468C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_7_28AC end

    def Function_8_2915(): pass

    label("Function_8_2915")

    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFD3D2, 0x0, 0x29F4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFBFDC, 0x0, 0x40CE, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_2953():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2953)
    OP_8E(0xFE, 0xFFFFBA28, 0x0, 0x468C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_8_2915 end

    def Function_9_2979(): pass

    label("Function_9_2979")

    Sleep(1000)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFDD6E, 0x0, 0x1F40, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFBFDC, 0x0, 0x40CE, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_29BC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29BC)
    OP_8E(0xFE, 0xFFFFBA28, 0x0, 0x468C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_2979 end

    def Function_10_29E2(): pass

    label("Function_10_29E2")

    Sleep(300)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFD6E8, 0x0, 0x20DA, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFBFDC, 0x0, 0x40CE, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_2A25():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A25)
    OP_8E(0xFE, 0xFFFFBA28, 0x0, 0x468C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_29E2 end

    def Function_11_2A4B(): pass

    label("Function_11_2A4B")

    Sleep(700)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x0, 0x0, 0x5276, 0x1388, 0x0)

    def lambda_2A75():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A75)
    OP_8E(0xFE, 0x0, 0x0, 0x5C08, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_2A4B end

    def Function_12_2A9B(): pass

    label("Function_12_2A9B")

    Sleep(1000)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x0, 0x0, 0x5276, 0x1388, 0x0)

    def lambda_2AC5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AC5)
    OP_8E(0xFE, 0x0, 0x0, 0x5C08, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_12_2A9B end

    def Function_13_2AEB(): pass

    label("Function_13_2AEB")

    Sleep(1300)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x0, 0x0, 0x5276, 0x1388, 0x0)

    def lambda_2B15():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B15)
    OP_8E(0xFE, 0x0, 0x0, 0x5C08, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_13_2AEB end

    def Function_14_2B3B(): pass

    label("Function_14_2B3B")

    Sleep(1600)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x0, 0x0, 0x5276, 0x1388, 0x0)

    def lambda_2B65():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B65)
    OP_8E(0xFE, 0x0, 0x0, 0x5C08, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_2B3B end

    def Function_15_2B8B(): pass

    label("Function_15_2B8B")

    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFD468, 0x0, 0x45F6, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFD67A, 0x7D0, 0x57A8, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFDF62, 0xFA0, 0x61B2, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF97A, 0x1770, 0x69FA, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFD44, 0x1770, 0x7F62, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_2C05():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C05)
    OP_8E(0xFE, 0xFFFFFD44, 0x1770, 0x88AE, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_2B8B end

    def Function_16_2C2B(): pass

    label("Function_16_2C2B")

    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x2C88, 0x0, 0x46DC, 0x1388, 0x0)
    OP_8E(0xFE, 0x2BAC, 0x7D0, 0x57F8, 0x1388, 0x0)
    OP_8E(0xFE, 0x20E4, 0xFA0, 0x623E, 0x1388, 0x0)
    OP_8E(0xFE, 0x618, 0x1770, 0x6900, 0x1388, 0x0)
    OP_8E(0xFE, 0x3B6, 0x1770, 0x7F1C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_2CA5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CA5)
    OP_8E(0xFE, 0x384, 0x1770, 0x88AE, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_2C2B end

    def Function_17_2CCB(): pass

    label("Function_17_2CCB")

    Sleep(500)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0xFFFFFC54, 0x0, 0x1A7C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFD468, 0x0, 0x45F6, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFD67A, 0x7D0, 0x57A8, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFDF62, 0xFA0, 0x61B2, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF97A, 0x1770, 0x69FA, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFD44, 0x1770, 0x7F62, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_2D5E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D5E)
    OP_8E(0xFE, 0xFFFFFD44, 0x1770, 0x88AE, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_2CCB end

    def Function_18_2D84(): pass

    label("Function_18_2D84")

    Sleep(500)
    OP_51(0xFE, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8E(0xFE, 0x2C88, 0x0, 0x46DC, 0x1388, 0x0)
    OP_8E(0xFE, 0x2BAC, 0x7D0, 0x57F8, 0x1388, 0x0)
    OP_8E(0xFE, 0x20E4, 0xFA0, 0x623E, 0x1388, 0x0)
    OP_8E(0xFE, 0x618, 0x1770, 0x6900, 0x1388, 0x0)
    OP_8E(0xFE, 0x3B6, 0x1770, 0x7F1C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_2E03():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E03)
    OP_8E(0xFE, 0x384, 0x1770, 0x88AE, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_2D84 end

    SaveToFile()

Try(main)
