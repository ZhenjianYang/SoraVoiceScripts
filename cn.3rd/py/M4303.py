from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M4303   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4303.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        '影之王',                               # 9
        '洛斯托尔姆',                           # 10
        '封印石',                               # 11
        '',                                     # 12
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
        'ED6_DT26/CH20630 ._CH',             # 01
        'ED6_DT27/CH04082 ._CH',             # 02
        'ED6_DT26/CH20631 ._CH',             # 03
        'ED6_DT26/CH20297 ._CH',             # 04
        'ED6_DT26/CH20641 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02770P._CP',             # 00
        'ED6_DT26/CH20630P._CP',             # 01
        'ED6_DT27/CH04082P._CP',             # 02
        'ED6_DT26/CH20631P._CP',             # 03
        'ED6_DT26/CH20297P._CP',             # 04
        'ED6_DT26/CH20641P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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


    DeclEvent(
        X                   = -170,
        Y                   = -1000,
        Z                   = 23130,
        Range               = 4000,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 14,
    )


    ScpFunction(
        "Function_0_15A",          # 00, 0
        "Function_1_1AE",          # 01, 1
        "Function_2_1D8",          # 02, 2
        "Function_3_1E1",          # 03, 3
        "Function_4_25B7",         # 04, 4
        "Function_5_25F0",         # 05, 5
        "Function_6_262E",         # 06, 6
        "Function_7_266C",         # 07, 7
        "Function_8_26AA",         # 08, 8
        "Function_9_41C8",         # 09, 9
        "Function_10_4433",        # 0A, 10
        "Function_11_4470",        # 0B, 11
        "Function_12_44B2",        # 0C, 12
        "Function_13_44F4",        # 0D, 13
        "Function_14_4536",        # 0E, 14
        "Function_15_53F6",        # 0F, 15
        "Function_16_5556",        # 10, 16
        "Function_17_5634",        # 11, 17
        "Function_18_5701",        # 12, 18
        "Function_19_5817",        # 13, 19
    )


    def Function_0_15A(): pass

    label("Function_0_15A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_172"),
        (SWITCH_DEFAULT, "loc_179"),
    )


    label("loc_172")

    Event(0, 16)
    Jump("loc_179")

    label("loc_179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_18F")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_1AD")

    label("loc_18F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_1AD")

    Return()

    # Function_0_15A end

    def Function_1_1AE(): pass

    label("Function_1_1AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C7")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C7")

    OP_1B(0x1, 0x0, 0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7")
    OP_82(0x80, 0x0)

    label("loc_1D7")

    Return()

    # Function_1_1AE end

    def Function_2_1D8(): pass

    label("Function_2_1D8")

    Call(0, 3)
    Call(0, 8)
    Return()

    # Function_2_1D8 end

    def Function_3_1E1(): pass

    label("Function_3_1E1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_01.eff")
    LoadEffect(0x2, "map\\mp253_00.eff")
    LoadEffect(0x3, "map\\mp253_01.eff")
    LoadEffect(0x4, "monster\\msc1000.eff")
    OP_E0(238, 0x46, 0x2)
    OP_E0(238, 0x47, 0x3)
    OP_E0(239, 0x48, 0x2)
    OP_E0(239, 0x49, 0x3)
    OP_E0(240, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x3)
    OP_E0(241, 0x4C, 0x2)
    OP_E0(241, 0x4D, 0x3)
    OP_6D(-550, 4850, 9540, 0)
    OP_67(0, 10710, -10000, 0)
    OP_6B(3110, 0)
    OP_6C(45000, 0)
    OP_6E(417, 0)
    SetChrPos(0x109, -1180, 0, -23280, 0)
    SetChrPos(0x10F, 550, 0, -24030, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_309")
    SetChrPos(0x10E, -1090, 0, -25610, 0)
    SetChrPos(0xF1, 560, 0, -26500, 0)
    Jump("loc_339")

    label("loc_309")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339")
    SetChrPos(0x10E, -1090, 0, -25610, 0)
    SetChrPos(0xF0, 560, 0, -26500, 0)

    label("loc_339")

    OP_43(0x109, 0x0, 0x0, 0x4)
    OP_43(0x10F, 0x0, 0x0, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_366")
    OP_43(0x10E, 0x0, 0x0, 0x6)
    OP_43(0xF1, 0x0, 0x0, 0x7)
    Jump("loc_382")

    label("loc_366")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    OP_43(0x10E, 0x0, 0x0, 0x6)
    OP_43(0xF0, 0x0, 0x0, 0x7)

    label("loc_382")


    def lambda_388():
        OP_6D(-90, 0, -9340, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_388)

    def lambda_3A0():
        OP_67(0, 7570, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3A0)

    def lambda_3B8():
        OP_6B(3110, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3B8)

    def lambda_3C8():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3C8)

    def lambda_3D8():
        OP_6E(417, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_3D8)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x1)
    Fade(1000)
    OP_6D(320, 0, -9000, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(45000, 0)
    OP_6E(256, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(1000)

    ChrTalk(    #0
        0x10F,
        "#1443F#5P……凯文………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        (
            "#1063F#5P啊啊……\x01",
            "又是那股气味……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10E,
        (
            "#178F#6P就像是\x01",
            "从灵柩出来的恶魔那样……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_507")

    ChrTalk(    #3
        0x102,
        "#1503F#6P（……在哪里………？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B1")

    label("loc_507")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_539")

    ChrTalk(    #4
        0x107,
        "#065F#6P哇、哇啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B1")

    label("loc_539")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_584")

    ChrTalk(    #5
        0x10B,
        (
            "#215F#6P光、光是想像一下子，\x01",
            "就觉得好恐怖呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B1")

    label("loc_584")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B1")

    ChrTalk(    #6
        0x10D,
        "#277F#6P……有趣。\x02",
    )

    CloseMessageWindow()

    label("loc_5B1")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 600, 17880, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #7
        0x10,
        "嘶哑的声音",
        (
            "\x07\x02呵呵……\x01",
            "闻到气味了吗？\x02\x03",

            "不愧是教会的猎犬……\x01",
            "鼻子倒是相当的灵敏。\x07\x00\x02",
        )
    )

    Jump("loc_642")

    label("loc_642")

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A3")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_70A")

    label("loc_6A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CB")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_70A")

    label("loc_6CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F3")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_70A")

    label("loc_6F3")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_70A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_737")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_79E")

    label("loc_737")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_79E")

    label("loc_75F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_787")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_79E")

    label("loc_787")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_79E")

    Sleep(1000)

    def lambda_7A9():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7A9)
    Sleep(50)

    def lambda_7BC():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7BC)
    Sleep(50)

    def lambda_7CF():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_7CF)
    Sleep(50)
    OP_8C(0xF1, 0, 600)

    ChrTalk(    #8
        0x109,
        "#1069F#6P……是谁！？\x02",
    )

    CloseMessageWindow()
    OP_1D(0xB0)

    def lambda_80D():
        OP_6D(670, 600, 18340, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_80D)

    def lambda_825():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_825)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    OP_22(0xBA, 0x1, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 0, 600, 17880, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Fade(1000)

    def lambda_883():
        OP_6B(2950, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_883)
    PlayEffect(0x1, 0x1, 0xFF, 0, 600, 17880, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x59, 0x0, 0x64)

    def lambda_8CD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_8CD)
    OP_0D()
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0xBA)
    Sleep(1000)

    ChrTalk(    #9
        0x109,
        "#1079F#5P#4S！！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(0, 400, 23390, 0)
    OP_67(-210, 3050, -14480, 0)
    OP_6B(1890, 0)
    OP_6C(0, 0)
    OP_6E(403, 0)
    OP_0D()

    def lambda_966():
        OP_6D(0, 800, 12570, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_966)

    def lambda_97E():
        OP_67(-210, 4120, -14480, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_97E)

    def lambda_996():
        OP_6B(1820, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_996)

    def lambda_9A6():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_9A6)

    def lambda_9B6():
        OP_6E(406, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_9B6)
    SetChrPos(0x109, -760, 0, -2080, 0)
    SetChrPos(0x10F, 550, 0, -3930, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A15")
    SetChrPos(0x10E, 1050, 0, -4180, 0)
    SetChrPos(0xF1, -1400, 0, -4280, 0)
    Jump("loc_A45")

    label("loc_A15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A45")
    SetChrPos(0x10E, -1400, 0, -4280, 0)
    SetChrPos(0xF0, 1050, 0, -4180, 0)

    label("loc_A45")

    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 6)
    SetChrSubChip(0x109, 0)

    def lambda_A5A():
        OP_8E(0xFE, 0xFFFFFD08, 0x0, 0x1BA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A5A)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 8)
    SetChrSubChip(0x10F, 0)

    def lambda_A89():
        OP_8E(0xFE, 0x226, 0x0, 0x1B12, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_A89)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0D")
    Sleep(150)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 10)
    SetChrSubChip(0x10E, 0)

    def lambda_AC6():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x14A0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_AC6)
    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 12)
    SetChrSubChip(0xF1, 0)

    def lambda_AF5():
        OP_8E(0xFE, 0x41A, 0x0, 0x143C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_AF5)
    Jump("loc_B79")

    label("loc_B0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B79")
    Sleep(150)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 12)
    SetChrSubChip(0x10E, 0)

    def lambda_B35():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x14A0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_B35)
    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 10)
    SetChrSubChip(0xF0, 0)

    def lambda_B64():
        OP_8E(0xFE, 0x41A, 0x0, 0x143C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_B64)

    label("loc_B79")

    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #10
        0x10F,
        "#1441F#6P什么人……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        (
            "#1075F#6P……果然现身了啊。\x02\x03",

            "#1060F你就是那个黑骑士所说的『王』，\x01",
            "对吧？\x02",
        )
    )

    Jump("loc_C1F")

    label("loc_C1F")

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS417._CH")
    OP_C6(0x0, 0x0, 140000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1200)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("蒙面人物")

    AnonymousTalk(    #12
        (
            "\x07\x02呵呵，如你所言。\x02\x03",

            "从统治『影之国』\x01",
            "这个意义上来说，\x01",
            "正是如此吧。\x02\x03",

            "请称呼我为\x01",
            "『影之王』。\x07\x00\x02",
        )
    )

    Jump("loc_D03")

    label("loc_D03")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    Sleep(1000)

    ChrTalk(    #13
        0x10F,
        "#1802F#6P影之……王。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "\x07\x02#1580F哈哈，这名字的由来\x01",
            "圣典里应该找不到。\x02\x03",

            "是这样吧？\x01",
            "莉丝·亚尔珍特。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x10F,
        "#1441F#6P……连我的事情都………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1063F#6P哼，看来\x01",
            "调查得还挺仔细的啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 4)
    SetChrSubChip(0x10E, 0)
    OP_51(0x10E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(500)

    ChrTalk(    #17
        0x10E,
        (
            "#176F#6P……寒暄\x01",
            "就到此为止吧。\x02\x03",

            "#178F你说你叫做『影之王』对吧……\x02\x03",

            "如果你就是\x01",
            "造成这状况的幕后黑手……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(2570, 0, 8230, 0)
    OP_67(0, 3720, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(140000, 0)
    OP_6E(274, 0)
    SetChrPos(0x109, -500, 0, 7650, 0)
    SetChrPos(0x10F, 950, 0, 7110, 0)
    SetChrPos(0x10E, -2000, 0, 7290, 0)
    OP_51(0x10E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6A")
    SetChrPos(0xF1, 130, 0, 5410, 0)
    Jump("loc_F89")

    label("loc_F6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F89")
    SetChrPos(0xF0, 130, 0, 5410, 0)

    label("loc_F89")

    OP_0D()
    Sleep(300)
    Fade(250)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDF")
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x10E, 1)
    OP_0D()
    Sleep(300)
    OP_22(0x1F8, 0x0, 0x64)
    OP_51(0x10E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10E, 0x23, (scpexpr(EXPR_PUSH_LONG, 0x8F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10E, 10)
    SetChrSubChip(0x10E, 0)
    Jump("loc_1027")

    label("loc_FDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1027")
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x10E, 1)
    OP_0D()
    Sleep(300)
    OP_22(0x1F8, 0x0, 0x64)
    OP_51(0x10E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10E, 0x23, (scpexpr(EXPR_PUSH_LONG, 0x8F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10E, 12)
    SetChrSubChip(0x10E, 0)

    label("loc_1027")

    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x10E,
        (
            "#177F#5P#3S请你立即\x01",
            "将王都恢复正常！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #19
        0x10E,
        "#177F#5P#3S否则休怪我剑下无情！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #20
        0x10,
        (
            "\x07\x02#1580F#5P呵呵，\x01",
            "你的要求实在毫无意义。\x02\x03",

            "敬爱之心一旦过度，\x01",
            "也将成为看清真相的障碍。\x02\x03",

            "明白吗？\x01",
            "尤莉亚·舒华兹。\x07\x00\x02",
        )
    )

    Jump("loc_114E")

    label("loc_114E")

    CloseMessageWindow()

    ChrTalk(    #21
        0x10E,
        "#173F#5P什、什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D1")

    ChrTalk(    #22
        0x102,
        (
            "#1505F#5P果然……\x01",
            "是这么回事啊。\x02\x03",

            "#1502F我们刚才所在的\x01",
            "格兰赛尔完全是假货……\x02\x03",

            "不，\x01",
            "是在『影之国』里重现的仿制品吧？\x02",
        )
    )

    Jump("loc_1216")

    label("loc_1216")

    CloseMessageWindow()
    OP_62(0x10E, 0xFFFFFF38, 1800, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x10E)

    ChrTalk(    #23
        0x10E,
        "#177F#5P什……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10F,
        "#1802F#5P这怎么可能……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        (
            "#1063F#6P……不过，\x01",
            "这么一来一切都能解释得通了。\x02\x03",

            "#1065F漆黑的大门和无人的街道……\x02\x03",

            "回到过去的房屋\x01",
            "和连结构都发生了变化的遗迹……\x02\x03",

            "#1060F是吧，约修亚？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1500F#5P嗯，你说得没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "\x07\x02#1580F#5P哼哼……哎呀哎呀。\x01",
            "你也太有板有眼了。\x02\x03",

            "要能表现得再可爱点\x01",
            "我倒是会更开心。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1505F#5P我对你的娱乐没兴趣。\x02\x03",

            "#1502F……有兴趣的\x01",
            "只有艾丝蒂尔的安危而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "\x07\x02#1580F#5P呵呵，我明白。\x02\x03",

            "然而，\x01",
            "爱恋之心越强离真相也会越远。\x02\x03",

            "不是吗？\x01",
            "约修亚·布莱特。\x07\x00\x02",
        )
    )

    Jump("loc_14A9")

    label("loc_14A9")

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        "#1503F#5P…………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_15D6")

    label("loc_14D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D6")

    ChrTalk(    #31
        0x109,
        (
            "#1075F#5P哼……\x01",
            "果然是这么回事吗。\x02\x03",

            "#1060F我们刚才所在的\x01",
            "格兰赛尔全是假货……\x02\x03",

            "不，\x01",
            "是在这『影之国』里重现的仿制品吧？\x02",
        )
    )

    Jump("loc_1575")

    label("loc_1575")

    CloseMessageWindow()
    OP_62(0x10E, 0xFFFFFF38, 1800, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x10E)

    ChrTalk(    #32
        0x10E,
        "#177F#5P什……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10F,
        "#1802F#5P这怎么可能……\x02",
    )

    CloseMessageWindow()

    label("loc_15D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F9")

    ChrTalk(    #34
        0x10D,
        (
            "#272F#5P不过，\x01",
            "这种说法确实能解释王都的异常……\x02\x03",

            "#270F也就是说，\x01",
            "我们被迫登上了你恶趣味的舞台吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "\x07\x02#1580F#5P呵呵，说得不错。\x02\x03",

            "能同时品味\x01",
            "演员和观众的感觉……\x02\x03",

            "是很难得的体验吧？\x01",
            "穆拉·范德尔。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10D,
        "#277F#5P哼……无聊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_16F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1838")

    ChrTalk(    #37
        0x10B,
        (
            "#216F#5P难、难道说……\x02\x03",

            "港口里的山猫号\x01",
            "也是假货！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "\x07\x02#1580F#5P谁知道呢……\x01",
            "这个问题\x01",
            "不在这次所讨论的范围内。\x02\x03",

            "……真正的飞艇\x01",
            "是否隐藏在其它地方呢。\x02\x03",

            "而你的哥哥们\x01",
            "现在怎么样了呢。\x02\x03",

            "你怎么想？\x01",
            "乔丝特·卡普亚。\x07\x00\x02",
        )
    )

    Jump("loc_1819")

    label("loc_1819")

    CloseMessageWindow()

    ChrTalk(    #39
        0x10B,
        "#212F#5P呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_1838")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1975")

    ChrTalk(    #40
        0x107,
        (
            "#062F#5P但、但是这样一来\x01",
            "确实能解释很多事情。\x02\x03",

            "#561F虽然还是不明白\x01",
            "『影之国』到底是什么东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "\x07\x02#1580F#5P哈哈……这样就行了。\x02\x03",

            "你的理解是正确的，\x01",
            "而且位于理想的阶段。\x02\x03",

            "我很满意。\x01",
            "提妲·拉赛尔。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x107,
        (
            "#065F#5P哎……！？\x02\x03",

            "那、那个，过奖了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1975")

    Sleep(300)
    Fade(500)
    OP_6D(1240, 400, 12120, 0)
    OP_67(0, 3970, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(45000, 0)
    OP_6E(303, 0)
    OP_51(0x10E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10E, 0x23, (scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(500)

    ChrTalk(    #43
        0x10E,
        (
            "#176F#6P是吗……\x01",
            "陛下和殿下现在依然平安无事……\x02\x03",

            "#171F女神啊……\x01",
            "感谢您的慈悲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "\x07\x02#1580F#5P哦……？\x01",
            "你在放心什么？\x02\x03",

            "有谁说过你所担心的人们\x01",
            "已经没事了吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10E,
        "#173F#6P咦……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x12, 0x80)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x12, -600, 1600, 17100, 0)
    PlayEffect(0x2, 0x7, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x80, 0x0, 0x64)
    OP_0D()
    Sleep(300)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x10E,
        (
            "#177F#6P什……！\x02\x03",

            "难、难不成……\x01",
            "那石头中……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        (
            "\x07\x02#1580F#5P呵呵……\x01",
            "这可说是『第二星层』中\x01",
            "最后的宝物吧。\x02\x03",

            "而当然……\x01",
            "宝物总伴随着试炼。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    PlayEffect(0x4, 0x3, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x10, 8)
    Sleep(200)
    LoadEffect(0x0, "map\\mp251_00.eff")
    LoadEffect(0x1, "map\\mp251_01.eff")
    LoadEffect(0x5, "monster\\ms32000.eff")
    LoadEffect(0x6, "monster\\ms32000b.eff")
    OP_20(0x5DC)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(4680, 0, 8610, 0)
    OP_67(-210, 6250, -14480, 0)
    OP_6B(1930, 0)
    OP_6C(126000, 0)
    OP_6E(513, 0)
    SetChrPos(0x12, -600, 1600, 17500, 0)
    Sleep(300)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 10080, 200, 930, 0, 0, 0, 1600, 1600, 1600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    OP_21()
    OP_1D(0x9A)
    OP_22(0x85, 0x1, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, 10080, 200, 930, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    def lambda_1DB4():

        label("loc_1DB4")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1DB4")

    QueueWorkItem2(0x10F, 3, lambda_1DB4)

    def lambda_1DCF():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1DCF)
    Sleep(100)

    def lambda_1DE2():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1DE2)
    Sleep(100)

    def lambda_1DF5():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1DF5)
    Sleep(100)
    OP_8C(0xF0, 135, 400)

    def lambda_1E0F():
        OP_6D(10520, 0, 730, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1E0F)

    def lambda_1E27():
        OP_67(-210, 7810, -14480, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E27)

    def lambda_1E3F():
        OP_6B(1710, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1E3F)

    def lambda_1E4F():
        OP_6C(131000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1E4F)

    def lambda_1E5F():
        OP_6E(460, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1E5F)
    WaitChrThread(0x109, 0x0)
    SetChrPos(0x11, 10080, -8000, 930, 310)
    OP_A1(0x11, 0x6)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_B0(0x6, 0x1E)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x28)

    def lambda_1EA2():
        OP_8F(0xFE, 0x2760, 0x3E8, 0x3A2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1EA2)
    Sleep(1000)

    def lambda_1EC2():
        OP_6D(16540, 0, 1480, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1EC2)

    def lambda_1EDA():
        OP_67(-210, 8380, -14480, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1EDA)

    def lambda_1EF2():
        OP_6B(2040, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1EF2)

    def lambda_1F02():
        OP_6C(83000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1F02)

    def lambda_1F12():
        OP_6E(428, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1F12)
    WaitChrThread(0x11, 0x0)
    OP_44(0x10F, 0x3)
    OP_23(0x85)
    PlayEffect(0x5, 0x2, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x109, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x3, 0x2)
    Sleep(1000)
    OP_22(0x99, 0x0, 0x64)

    def lambda_1F7B():
        OP_6B(1500, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1F7B)
    FadeToDark(300, 16777215, -1)
    OP_0D()
    OP_44(0x109, 0x2)
    OP_6D(10430, 1200, 4300, 0)
    OP_67(-210, 2770, -14480, 0)
    OP_6B(4470, 0)
    OP_6C(122000, 0)
    OP_6E(206, 0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, -700, 0, 9440, 135)
    SetChrPos(0x10F, 1900, 0, 9040, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2030")
    SetChrPos(0x10E, -990, 0, 7530, 135)
    SetChrPos(0xF1, 1210, 0, 7350, 135)
    Jump("loc_2060")

    label("loc_2030")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2060")
    SetChrPos(0x10E, -990, 0, 7530, 135)
    SetChrPos(0xF0, 1210, 0, 7350, 135)

    label("loc_2060")

    SetChrPos(0x11, 9650, 0, 2770, 305)
    FadeToBright(1000, 16777215)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DB")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2142")

    label("loc_20DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2103")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2142")

    label("loc_2103")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_212B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2142")

    label("loc_212B")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2142")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_216F")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_21D6")

    label("loc_216F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2197")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_21D6")

    label("loc_2197")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21BF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_21D6")

    label("loc_21BF")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_21D6")

    Sleep(1000)

    ChrTalk(    #48
        0x10E,
        "#173F#6P#4S！！！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2237")

    ChrTalk(    #49
        0x102,
        (
            "#1506F#6P这是……\x01",
            "圣典中的恶魔！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D4")

    label("loc_2237")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2267")

    ChrTalk(    #50
        0x107,
        "#065F#6P哇哇……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_22D4")

    label("loc_2267")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22A1")

    ChrTalk(    #51
        0x10B,
        "#216F#6P这、这家伙是什么！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_22D4")

    label("loc_22A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22D4")

    ChrTalk(    #52
        0x10D,
        "#271F#6P这是恶魔吗……！\x02",
    )

    CloseMessageWindow()

    label("loc_22D4")


    ChrTalk(    #53
        0x10F,
        (
            "#1446F#6P圣典中所记载的\x01",
            "七十七恶魔之一……\x02\x03",

            "作为守护炼狱的看门人之一、\x01",
            "统率众多妖魔的军团长……\x02\x03",

            "#1441F『暴虐』之洛斯托尔姆……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x109,
        (
            "#1069F#6P哼……你到底在想什么！\x02\x03",

            "将这种东西实体化，\x01",
            "你也不会平安无事的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "\x07\x02#1580F#5P呵呵，要防止变成最坏的结果，\x01",
            "这任务就交给你们了。\x02\x03",

            "来，敬请享受吧！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_243B():
        OP_6D(15210, 500, -670, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_243B)

    def lambda_2453():
        OP_67(-210, 2910, -14480, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2453)

    def lambda_246B():
        OP_6B(2900, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_246B)

    def lambda_247B():
        OP_6C(122000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_247B)

    def lambda_248B():
        OP_6E(330, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_248B)
    OP_22(0x1E6, 0x0, 0x64)
    OP_72(0x2006, 0x0)
    ExitThread()
    OP_B0(0x6, 0x1E)
    OP_6F(0x6, 141)
    OP_70(0x6, 0x96)
    OP_73(0x6)
    OP_71(0x2006, 0x0)
    ExitThread()
    OP_6F(0x6, 151)
    OP_70(0x6, 0xA0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    WaitChrThread(0x109, 0x2)
    OP_72(0x2006, 0x0)
    ExitThread()
    OP_D8(0x6, 0x1F4)
    SetMapFlags(0x100000)
    OP_22(0x85, 0x1, 0x64)

    def lambda_24F2():

        label("loc_24F2")

        OP_7C(0x78, 0x78, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_24F2")

    QueueWorkItem2(0x10F, 3, lambda_24F2)
    OP_23(0x1E6)
    OP_22(0xF3, 0x0, 0x64)
    OP_22(0x1EF, 0x0, 0x64)
    OP_22(0x148, 0x0, 0x64)
    OP_6F(0x6, 161)
    OP_70(0x6, 0xAA)
    OP_73(0x6)
    OP_71(0x2006, 0x0)
    ExitThread()
    OP_6F(0x6, 171)
    OP_70(0x6, 0xBE)

    def lambda_2544():

        label("loc_2544")

        OP_7C(0x12C, 0x12C, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_2544")

    QueueWorkItem2(0x10F, 3, lambda_2544)

    def lambda_255F():
        OP_6D(15210, 1200, -670, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_255F)

    def lambda_2577():
        OP_6B(1800, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2577)

    def lambda_2587():
        OP_6E(560, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2587)
    Sleep(2300)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x10F, 0x1)
    OP_44(0x10F, 0x3)
    OP_23(0x85)
    Battle(0xF9, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_1E1 end

    def Function_4_25B7(): pass

    label("Function_4_25B7")

    OP_8E(0xFE, 0xFFFFF9F2, 0x0, 0xFFFFDD1E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    Return()

    # Function_4_25B7 end

    def Function_5_25F0(): pass

    label("Function_5_25F0")

    Sleep(200)
    OP_8E(0xFE, 0xAA, 0x0, 0xFFFFDCD8, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    Return()

    # Function_5_25F0 end

    def Function_6_262E(): pass

    label("Function_6_262E")

    Sleep(200)
    OP_8E(0xFE, 0xFFFFF813, 0x0, 0xFFFFD5B2, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    Return()

    # Function_6_262E end

    def Function_7_266C(): pass

    label("Function_7_266C")

    Sleep(250)
    OP_8E(0xFE, 0x190, 0x0, 0xFFFFD684, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    Return()

    # Function_7_266C end

    def Function_8_26AA(): pass

    label("Function_8_26AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0xB0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "battle\\btgun10.eff")
    LoadEffect(0x4, "battle\\damage2.eff")
    OP_E0(238, 0x46, 0x2)
    OP_E0(238, 0x47, 0x5)
    OP_E0(239, 0x48, 0x2)
    OP_E0(239, 0x49, 0x5)
    OP_E0(240, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x5)
    OP_E0(241, 0x4C, 0x2)
    OP_E0(241, 0x4D, 0x5)
    SetChrChipByIndex(0x10F, 5)
    SetChrSubChip(0x10F, 3)
    OP_71(0x406, 0x0)
    ExitThread()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 600, 17880, 180)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x20)
    ClearChrFlags(0x12, 0x80)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x12, -400, 1600, 17100, 0)
    PlayEffect(0x1, 0x0, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -1870, 0, 5950, 90)
    SetChrPos(0x10F, 110, 0, 5890, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2849")
    SetChrPos(0x10E, -1990, 0, 4100, 90)
    SetChrPos(0xF1, 0, 0, 4090, 90)
    Jump("loc_2879")

    label("loc_2849")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2879")
    SetChrPos(0x10E, -1990, 0, 4100, 90)
    SetChrPos(0xF0, 0, 0, 4090, 90)

    label("loc_2879")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0xEE, 7)
    SetChrSubChip(0xEE, 3)
    SetChrChipByIndex(0xEF, 9)
    SetChrSubChip(0xEF, 3)
    SetChrChipByIndex(0xF0, 11)
    SetChrSubChip(0xF0, 3)
    SetChrChipByIndex(0xF1, 13)
    SetChrSubChip(0xF1, 3)
    OP_6D(7770, 3500, -150, 0)
    OP_67(0, 7270, -10000, 0)
    OP_6B(3770, 0)
    OP_6C(66000, 0)
    OP_6E(308, 0)
    Sleep(500)

    def lambda_2911():
        OP_6D(-3580, 3500, 3000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2911)

    def lambda_2929():
        OP_67(0, 7270, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2929)

    def lambda_2941():
        OP_6B(3500, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2941)

    def lambda_2951():
        OP_6C(66000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2951)

    def lambda_2961():
        OP_6E(300, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2961)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_6D(440, 0, 5710, 0)
    OP_67(0, 6310, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(56000, 0)
    OP_6E(262, 0)
    OP_43(0x109, 0x0, 0x0, 0xA)
    OP_43(0x10F, 0x0, 0x0, 0xB)
    OP_43(0xF0, 0x0, 0x0, 0xC)
    OP_43(0xF1, 0x0, 0x0, 0xD)
    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x109,
        (
            "#1070F#6P呜……\x01",
            "真、真是乱来……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10F,
        (
            "#1445F#5P难以置信……\x01",
            "……竟然把它赶回去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10E,
        "#172F#6P比、比起这个……！\x02",
    )

    CloseMessageWindow()
    OP_44(0x109, 0x0)
    OP_44(0x10F, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    Fade(250)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ACC")
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    Sleep(100)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    Sleep(100)
    SetChrChipByIndex(0xF1, 65535)
    SetChrSubChip(0xF1, 0)
    Jump("loc_2B11")

    label("loc_2ACC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B11")
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    Sleep(100)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    Sleep(100)
    SetChrChipByIndex(0xF0, 65535)
    SetChrSubChip(0xF0, 0)

    label("loc_2B11")

    OP_0D()

    def lambda_2B18():
        OP_6D(970, 300, 12540, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2B18)

    def lambda_2B30():
        OP_67(0, 3800, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2B30)

    def lambda_2B48():
        OP_6B(3250, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2B48)

    def lambda_2B58():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2B58)

    def lambda_2B68():
        OP_6E(331, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2B68)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BC3")

    def lambda_2B86():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_2B86)
    Sleep(100)

    def lambda_2B99():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2B99)
    Sleep(100)

    def lambda_2BAC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2BAC)
    Sleep(100)
    OP_8C(0xF1, 0, 400)
    Jump("loc_2C11")

    label("loc_2BC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C11")

    def lambda_2BD7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_2BD7)
    Sleep(100)

    def lambda_2BEA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2BEA)
    Sleep(100)

    def lambda_2BFD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2BFD)
    Sleep(100)
    OP_8C(0xF0, 0, 400)

    label("loc_2C11")

    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #59
        0x10,
        (
            "\x07\x02#1580F呵呵……\x01",
            "身手倒是不错。\x02\x03",

            "这是奖励──收下吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x99, 0x0, 0x64)
    SetChrPos(0x12, -1850, -10000, 4970, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_6D(1040, 0, 4350, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(140000, 0)
    OP_6E(246, 0)
    SetChrPos(0x109, -960, 0, 7350, 0)
    SetChrPos(0x10F, 950, 0, 7010, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1E")
    SetChrPos(0x10E, -900, 0, 5450, 0)
    SetChrPos(0xF1, 1130, 0, 5210, 0)
    Jump("loc_2D4E")

    label("loc_2D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D4E")
    SetChrPos(0x10E, -900, 0, 5450, 0)
    SetChrPos(0xF0, 1130, 0, 5210, 0)

    label("loc_2D4E")

    OP_0D()
    Sleep(500)
    Fade(250)
    OP_22(0x99, 0x0, 0x64)
    SetChrPos(0x12, -900, 1000, 6250, 0)
    PlayEffect(0x1, 0x0, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()

    def lambda_2DE0():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2DE0)
    Sleep(50)

    def lambda_2DF3():
        OP_8C(0xFE, 225, 600)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2DF3)
    Sleep(80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E18")
    OP_8C(0xF1, 270, 600)
    Jump("loc_2E2D")

    label("loc_2E18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E2D")
    OP_8C(0xF0, 270, 600)

    label("loc_2E2D")


    ChrTalk(    #60
        0x10E,
        "#173F#11P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10E, 5)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x12, 0xFFFFFDA8, 0x41A, 0x1644, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    SetChrFlags(0x12, 0x80)
    OP_0D()
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #61
        "\x07\x00得到了\x1F\x57\x03\x07\x00。\x02",
    )

    Jump("loc_2EC3")

    label("loc_2EC3")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x357, 1)
    Sleep(1000)

    ChrTalk(    #62
        0x10E,
        "#171F#11P太好了，这下……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F3D")

    ChrTalk(    #63
        0x102,
        "#1500F#5P尤莉亚小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FD4")

    label("loc_2F3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F75")

    ChrTalk(    #64
        0x107,
        "#560F#5P尤、尤莉亚小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FD4")

    label("loc_2F75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FA3")

    ChrTalk(    #65
        0x10B,
        "#210F#5P上尉……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FD4")

    label("loc_2FA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FD4")

    ChrTalk(    #66
        0x10D,
        "#277F#5P……上尉………\x02",
    )

    CloseMessageWindow()

    label("loc_2FD4")


    def lambda_2FDA():
        OP_6D(2009, 0, 9850, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2FDA)

    def lambda_2FF2():
        OP_67(0, 4260, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2FF2)

    def lambda_300A():
        OP_6B(3800, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_300A)

    def lambda_301A():
        OP_6E(274, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_301A)
    Sleep(500)

    def lambda_302F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_302F)
    Sleep(100)

    def lambda_3042():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3042)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3067")
    OP_8C(0xF1, 0, 400)
    Jump("loc_307C")

    label("loc_3067")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_307C")
    OP_8C(0xF0, 0, 400)

    label("loc_307C")

    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #67
        0x109,
        (
            "#1075F#2P哼，\x01",
            "看来还算是守信。\x02\x03",

            "#1063F我开门见山地问吧──\x01",
            "你的目的是什么？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #68
        0x109,
        "#1069F#2P#3S到底想要把我们怎么样！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        (
            "\x07\x02#1580F#5P哈哈，凯文·格拉汉姆。\x02\x03",

            "希望你\x01",
            "不要太让我失望。\x02\x03",

            "我的名字是影──\x01",
            "因此真相\x01",
            "也仅存于你们之中。\x02\x03",

            "你明白我的意思吗……？\x07\x00\x02",
        )
    )

    Jump("loc_31EE")

    label("loc_31EE")

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        "#1079F#2P……咦…………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_22(0x164, 0x0, 0x64)
    OP_AD(0x240112, 0x0, 0x0, 0x5DC)
    Sleep(500)
    OP_AE(0x3E8)
    Sleep(1000)
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #71
        0x10F,
        "#1802F#5P凯文……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x109,
        (
            "#1075F#2P……哼，一派胡言。\x02\x03",

            "#1840F你就算故弄玄虚\x01",
            "也是没用的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "\x07\x02#1580F#5P不错，\x01",
            "我的话都是戏言……\x02\x03",

            "既然你这么认为，\x01",
            "那就大概没错吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #74
        0x109,
        "#1076F#2P少来这套……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        (
            "\x07\x02#1580F#5P呵呵，对了。\x02\x03",

            "干脆把『影之王』改掉，\x01",
            "以后叫『戏言王』如何？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x109, 0x14, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #76
        0x109,
        "#1069F#2P#4S我叫你少来这套！\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(150)
    Fade(500)

    def lambda_340C():
        OP_6D(1570, 0, 5000, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_340C)

    def lambda_3424():
        OP_6B(3100, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3424)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    OP_0D()
    SetChrChipByIndex(0x109, 2)
    OP_99(0x109, 0x0, 0x7, 0xBB8)
    OP_22(0xD8, 0x0, 0x64)
    Fade(500)
    OP_6D(970, 300, 12000, 0)
    OP_67(0, 3500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(331, 0)
    SetChrPos(0x109, -1870, 0, 5950, 0)
    SetChrPos(0x10F, 110, 0, 5890, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34E8")
    SetChrPos(0x10E, -1990, 0, 4100, 0)
    SetChrPos(0xF1, 0, 0, 4090, 0)
    Jump("loc_3518")

    label("loc_34E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3518")
    SetChrPos(0x10E, -1990, 0, 4100, 0)
    SetChrPos(0xF0, 0, 0, 4090, 0)

    label("loc_3518")

    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3528():
        OP_6D(360, 600, 18500, 1000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3528)

    def lambda_3540():
        OP_67(0, 4710, -10000, 1000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3540)

    def lambda_3558():
        OP_6B(3450, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 2, lambda_3558)

    def lambda_3568():
        OP_6E(212, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_3568)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_357D():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_357D)
    PlayEffect(0x3, 0x0, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x10, 0, 700, 0, 0)
    Sleep(200)

    def lambda_35C7():
        OP_8C(0x10F, 0, 600)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_35C7)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_35DA():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_35DA)
    PlayEffect(0x3, 0x1, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x10, 0, 700, 0, 0)
    Sleep(200)
    OP_43(0x10, 0x0, 0x0, 0x9)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_3630():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3630)
    PlayEffect(0x3, 0x2, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x10, 0, 700, 0, 0)
    Sleep(200)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_367F():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_367F)
    PlayEffect(0x3, 0x3, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x10, 0, 700, 0, 0)
    Sleep(200)
    WaitChrThread(0x10, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3715")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_377C")

    label("loc_3715")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_373D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_377C")

    label("loc_373D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3765")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_377C")

    label("loc_3765")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_377C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A9")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3810")

    label("loc_37A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D1")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3810")

    label("loc_37D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37F9")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3810")

    label("loc_37F9")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3810")

    Sleep(1000)
    Fade(1000)
    OP_6D(970, 0, 11370, 0)
    OP_67(0, 3700, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(45000, 0)
    OP_6E(331, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_388A")

    ChrTalk(    #77
        0x107,
        "#065F哎……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_38B4")

    label("loc_388A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38B4")

    ChrTalk(    #78
        0x10B,
        "#216F咦……！？\x02",
    )

    CloseMessageWindow()

    label("loc_38B4")

    OP_8C(0x10F, 270, 600)

    ChrTalk(    #79
        0x10F,
        (
            "#1802F#2P凯文……！？\x02\x03",

            "怎、怎么突然……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x109, 0x7, 0x0, 0x7D0)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #80
        0x109,
        (
            "#1065F#6P……冷静点。\x02\x01",

            "#1063F这正是『影』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10F,
        "#1444F#2P咦……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)
    OP_22(0x117, 0x0, 0x64)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
    Sleep(1000)

    ChrTalk(    #82
        0x10F,
        "#1802F#2P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10E,
        "#178F#4P分身……不，该说是金蝉脱壳吗。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A15")

    ChrTalk(    #84
        0x102,
        (
            "#1502F在我们战斗的时候\x01",
            "偷换了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ABC")

    label("loc_3A15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A59")

    ChrTalk(    #85
        0x10D,
        (
            "#272F哼……\x01",
            "在我们战斗的时候偷换了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ABC")

    label("loc_3A59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A8C")

    ChrTalk(    #86
        0x107,
        "#063F什、什么时候……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ABC")

    label("loc_3A8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ABC")

    ChrTalk(    #87
        0x10B,
        "#212F什、什么时候！？\x02",
    )

    CloseMessageWindow()

    label("loc_3ABC")

    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(130, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #88
        (
            "\x07\x02#40W呵呵，亏你能看穿。\x02\x03",

            "#40W你们在『第二星层』的任务\x01",
            "已经结束了。\x02\x03",

            "#40W既然取回了洁白之翼，\x01",
            "就去挑战更前方的深渊吧。\x02\x03",

            "#40W哈哈……\x01",
            "我期待着下一次的邂逅………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(800)

    def lambda_3BC2():
        OP_6D(500, 600, 23720, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3BC2)

    def lambda_3BDA():
        OP_67(0, 5780, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3BDA)

    def lambda_3BF2():
        OP_6B(2930, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3BF2)

    def lambda_3C02():
        OP_6C(33000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3C02)

    def lambda_3C12():
        OP_6E(302, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3C12)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3C6B():
        OP_6B(2800, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3C6B)
    OP_0D()
    Sleep(1500)

    def lambda_3C81():
        OP_6D(690, 0, 6750, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C81)

    def lambda_3C99():
        OP_67(0, 4230, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3C99)

    def lambda_3CB1():
        OP_6B(2930, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3CB1)

    def lambda_3CC1():
        OP_6C(45000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3CC1)

    def lambda_3CD1():
        OP_6E(302, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3CD1)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D22")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3D7A")

    label("loc_3D22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D45")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3D7A")

    label("loc_3D45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D68")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3D7A")

    label("loc_3D68")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3D7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D9D")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3DF5")

    label("loc_3D9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC0")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3DF5")

    label("loc_3DC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE3")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3DF5")

    label("loc_3DE3")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3DF5")

    WaitChrThread(0x109, 0x0)
    OP_63(0x109)
    OP_63(0x10F)
    OP_63(0xF0)
    OP_63(0xF1)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #89
        0x109,
        (
            "#1075F#5P哼……\x01",
            "装模作样。\x02\x03",

            "那种演技\x01",
            "只会让人感到很冷的。\x02",
        )
    )

    Jump("loc_3E7D")

    label("loc_3E7D")

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #90
        0x10F,
        "#1802F#2P……凯文………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F7B")

    ChrTalk(    #91
        0x109,
        (
            "#1078F#5P好了，\x01",
            "既然得到了新的封印石……\x02\x03",

            "暂时先回据点\x01",
            "解放里面的人吧。\x02\x03",

            "从『洁白之翼』这个词\x01",
            "大概也猜得到其中含义。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x10D,
        "#277F#6P呵呵，的确。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40A9")

    label("loc_3F7B")


    ChrTalk(    #93
        0x109,
        (
            "#1078F#5P好了，\x01",
            "既然得到了新的封印石……\x02\x03",

            "暂时先回据点\x01",
            "解放里面的人吧。\x02\x03",

            "从『洁白之翼』这个词\x01",
            "大概也猜得到其中含义。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_403B")

    ChrTalk(    #94
        0x102,
        "#1500F#6P嗯，的确。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40A9")

    label("loc_403B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_406B")

    ChrTalk(    #95
        0x107,
        "#560F#6P是、是啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_40A9")

    label("loc_406B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40A9")

    ChrTalk(    #96
        0x10B,
        (
            "#210F#6P嗯。\x01",
            "就算是我也灵光一现了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40A9")


    ChrTalk(    #97
        0x10E,
        (
            "#170F#6P……啊啊。\x01",
            "这样就太好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_40E2():
        OP_6B(3500, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_40E2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x2)
    Sleep(2000)
    OP_A2(0x2720)
    OP_AD(0x2400EE, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x157), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存】\x01",              # 0
            "【继续下面剧情】\x01",      # 1
        )
    )

    Jump("loc_416B")

    label("loc_416B")

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_417F")
    ShowSaveMenu()

    label("loc_417F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0x7D0)
    OP_21()
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x250B)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_26AA end

    def Function_9_41C8(): pass

    label("Function_9_41C8")

    Sleep(200)
    SetChrFlags(0xFE, 0x800)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 0)
    OP_20(0x0)
    PlayEffect(0x4, 0xFF, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4221():
        OP_8F(0xFE, 0x0, 0x3E8, 0x4844, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4221)

    def lambda_423C():
        OP_9E(0xFE, 0x1E, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_423C)

    def lambda_4256():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4256)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_42A0():
        OP_9E(0xFE, 0x1E, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_42A0)

    def lambda_42BA():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_42BA)
    Sleep(200)
    OP_22(0x22B, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4309():
        OP_9E(0xFE, 0x1E, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4309)

    def lambda_4323():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4323)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_436D():
        OP_9E(0xFE, 0x1E, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_436D)

    def lambda_4387():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4387)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_43D1():
        OP_9E(0xFE, 0x1E, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_43D1)

    def lambda_43EB():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_43EB)
    WaitChrThread(0xFE, 0x1)
    Sleep(500)

    def lambda_4405():
        OP_99(0xFE, 0x8, 0xD, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4405)
    OP_8F(0xFE, 0x0, 0x258, 0x4844, 0x1388, 0x0)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    OP_22(0x20C, 0x0, 0x64)
    Return()

    # Function_9_41C8 end

    def Function_10_4433(): pass

    label("Function_10_4433")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_446F")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_10_4433")

    label("loc_446F")

    Return()

    # Function_10_4433 end

    def Function_11_4470(): pass

    label("Function_11_4470")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44B1")
    Sleep(300)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_11_4470")

    label("loc_44B1")

    Return()

    # Function_11_4470 end

    def Function_12_44B2(): pass

    label("Function_12_44B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44F3")
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_12_44B2")

    label("loc_44F3")

    Return()

    # Function_12_44B2 end

    def Function_13_44F4(): pass

    label("Function_13_44F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4535")
    Sleep(500)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(800)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_13_44F4")

    label("loc_4535")

    Return()

    # Function_13_44F4 end

    def Function_14_4536(): pass

    label("Function_14_4536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 1)), scpexpr(EXPR_END)), "loc_453E")
    Return()

    label("loc_453E")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-30, 600, 21600, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(3970, 0)
    OP_6C(33000, 0)
    OP_6E(212, 0)
    SetChrPos(0x109, -770, 600, 19530, 0)
    SetChrPos(0x10F, 520, 600, 19440, 0)
    SetChrPos(0xF0, -1140, 600, 17900, 0)
    SetChrPos(0xF1, 50, 600, 17850, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #98
        0x109,
        (
            "#1063F#6P这就是通往\x01",
            "『第三星层』的传送阵吧……\x02\x03",

            "本来，\x01",
            "这里应该放着\x01",
            "封印『环』的古代装置。\x02",
        )
    )

    Jump("loc_466A")

    label("loc_466A")

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #99
        0x10F,
        (
            "#1444F#11P封印『环』……\x02\x03",

            "#1443F难不成就是报告书中\x01",
            "提到的『第一结界』？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #100
        0x109,
        (
            "#1065F#6P是的，\x01",
            "好像是将『环』的时间\x01",
            "冻结在异空间里的装置。\x02\x03",

            "#1063F不过就算如此，\x01",
            "似乎也无法防范\x01",
            "『福音』的影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10F,
        "#1446F#11P……原来如此。\x02",
    )

    CloseMessageWindow()

    def lambda_478E():
        OP_67(0, 6500, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_478E)
    OP_6D(-30, 600, 20600, 1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4893")

    ChrTalk(    #102
        0x107,
        (
            "#561F#6P但是最后，\x01",
            "『辉之环』消失不见了对吧……\x02\x03",

            "妈妈他们调查湖底\x01",
            "似乎也是抱着\x01",
            "说不定能找到『环』的希望……\x02\x03",

            "#063F只是因为浮游都市的崩毁，\x01",
            "似乎也有推测认为\x01",
            "它可能已完全被破坏掉了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B37")

    label("loc_4893")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_496F")

    ChrTalk(    #103
        0x102,
        (
            "#1503F#6P但是结果，\x01",
            "『辉之环』消失不见了。\x02\x03",

            "因为浮游都市的崩毁，\x01",
            "似乎也有推测认为\x01",
            "它可能已完全被破坏掉了……\x02\x03",

            "#1502F既然当时怀斯曼在动摇，\x01",
            "就可以肯定发生了什么\x01",
            "意想不到的事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B37")

    label("loc_496F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A04")

    ChrTalk(    #104
        0x10E,
        (
            "#176F#6P然而结果，\x01",
            "『辉之环』消失不见了。\x02\x03",

            "#178F因为浮游都市的崩毁，\x01",
            "似乎也有推测认为\x01",
            "它可能已完全被破坏掉了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B37")

    label("loc_4A04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AA3")

    ChrTalk(    #105
        0x10D,
        (
            "#272F#6P然而结果，\x01",
            "所谓的『辉之环』似乎消失不见了。\x02\x03",

            "#270F因为浮游都市的崩毁，\x01",
            "似乎也有推测认为\x01",
            "它可能已完全被破坏掉了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B37")

    label("loc_4AA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B37")

    ChrTalk(    #106
        0x105,
        (
            "#1167F#6P但是结果，\x01",
            "『辉之环』消失不见了。\x02\x03",

            "#1169F因为浮游都市的崩毁，\x01",
            "似乎也有推测认为\x01",
            "它可能已完全被破坏掉了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BC6")

    ChrTalk(    #107
        0x10B,
        (
            "#212F#6P说到底，\x01",
            "不抓到那个戴眼镜的恶趣味家伙\x01",
            "就无法了解真相吧？\x02\x03",

            "#416F虽然完全不知道\x01",
            "他现在在哪里干什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF0")

    label("loc_4BC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C4D")

    ChrTalk(    #108
        0x105,
        (
            "#1163F#6P……知道真相的\x01",
            "或许只有那个\x01",
            "怀斯曼教授吧。\x02\x03",

            "#1167F虽然完全想像不到\x01",
            "他现在在哪里干什么……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF0")

    label("loc_4C4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CE0")

    ChrTalk(    #109
        0x10D,
        (
            "#270F#6P恐怕，\x01",
            "不抓到那个在逃的怀斯曼，\x01",
            "真相永远都隐藏在黑暗中吧。\x02\x03",

            "#272F虽然完全想像不到\x01",
            "他现在在哪里干什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF0")

    label("loc_4CE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D75")

    ChrTalk(    #110
        0x10E,
        (
            "#178F#6P恐怕，\x01",
            "不抓到那个在逃的怀斯曼，\x01",
            "真相永远都隐藏在黑暗中吧。\x02\x03",

            "#176F虽然完全想像不到\x01",
            "他现在在哪里干什么……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF0")

    label("loc_4D75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DF0")

    ChrTalk(    #111
        0x102,
        (
            "#1505F#6P……知道真相的\x01",
            "或许只有怀斯曼而已。\x02\x03",

            "#1503F虽然我也不知道\x01",
            "他逃走后干什么去了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF0")

    OP_8C(0x10F, 225, 400)
    Sleep(300)

    ChrTalk(    #112
        0x10F,
        (
            "#1444F#5P咦……\x02\x03",

            "#1802F……但是根据报告……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F15")
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #113
        0x109,
        (
            "#1065F#5P──这件事\x01",
            "教会也在继续调查啊。\x02\x03",

            "#1060F不过，单说这次事件的话，\x01",
            "我觉得和怀斯曼没关系。\x02\x03",

            "如果有关系，\x01",
            "他应该会耀武扬威地过来挑衅的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FC6")

    label("loc_4F15")

    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #114
        0x109,
        (
            "#1065F#5P──这件事\x01",
            "教会也在继续调查啊。\x02\x03",

            "#1060F不过，单说这次事件的话\x01",
            "我觉得和怀斯曼没关系。\x02\x03",

            "如果有关系，\x01",
            "他应该会耀武扬威地过来挑衅的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FF7")

    ChrTalk(    #115
        0x102,
        "#1500F#6P……的确。\x02",
    )

    CloseMessageWindow()
    Jump("loc_50B7")

    label("loc_4FF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5029")

    ChrTalk(    #116
        0x107,
        "#060F#6P的、的确……\x02",
    )

    CloseMessageWindow()
    Jump("loc_50B7")

    label("loc_5029")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5059")

    ChrTalk(    #117
        0x10B,
        "#210F#6P嗯，的确。\x02",
    )

    CloseMessageWindow()
    Jump("loc_50B7")

    label("loc_5059")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5088")

    ChrTalk(    #118
        0x105,
        "#1160F#6P的确……\x02",
    )

    CloseMessageWindow()
    Jump("loc_50B7")

    label("loc_5088")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50B7")

    ChrTalk(    #119
        0x10E,
        "#170F#6P嗯……的确。\x02",
    )

    CloseMessageWindow()

    label("loc_50B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50FA")

    ChrTalk(    #120
        0x10D,
        (
            "#277F#6P特地戴着面具出现\x01",
            "也没意义啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5210")

    label("loc_50FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5141")

    ChrTalk(    #121
        0x10E,
        (
            "#170F#6P特地戴着面具出现\x01",
            "也没有意义嘛……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5210")

    label("loc_5141")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5189")

    ChrTalk(    #122
        0x105,
        (
            "#1382F#6P特地戴着面具出现\x01",
            "似乎也没意义呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5210")

    label("loc_5189")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51CE")

    ChrTalk(    #123
        0x10B,
        (
            "#210F#6P应该也不会\x01",
            "特地戴着面具登场吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5210")

    label("loc_51CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5210")

    ChrTalk(    #124
        0x107,
        (
            "#560F#6P应该也不会\x01",
            "特地戴着面具登场吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5210")

    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #125
        0x10F,
        "#1443F#11P………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_531B")

    ChrTalk(    #126
        0x109,
        (
            "#1075F#5P嗯，包括这些在内，\x01",
            "似乎还有很多谜团没有解开。\x02\x03",

            "#1060F要继续前进，\x01",
            "敌人的动向也要多加注意才好。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #127
        0x109,
        "#1078F#6P对吧，莉丝？\x02",
    )

    CloseMessageWindow()
    Jump("loc_53C4")

    label("loc_531B")


    ChrTalk(    #128
        0x109,
        (
            "#1075F#5P嗯，包括这些在内，\x01",
            "似乎还有很多谜团没有解开。\x02\x03",

            "#1060F要继续前进，\x01",
            "敌人的动向也要多加注意才好。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #129
        0x109,
        "#1078F#6P对吧，莉丝？\x02",
    )

    CloseMessageWindow()

    label("loc_53C4")


    ChrTalk(    #130
        0x10F,
        "#1446F#11P……嗯嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2801)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_14_4536 end

    def Function_15_53F6(): pass

    label("Function_15_53F6")

    EventBegin(0x0)
    Fade(500)
    OP_6D(330, 1250, 23660, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(35000, 0)
    OP_6E(324, 0)
    SetChrPos(0x109, 20, 600, 24220, 0)
    SetChrPos(0x10F, 770, 600, 23280, 0)
    SetChrPos(0xF0, -800, 600, 23250, 0)
    SetChrPos(0xF1, -40, 600, 22450, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 600, 23260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_5504():
        OP_67(0, 8000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_5504)

    def lambda_551C():
        OP_6B(3500, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_551C)
    Call(0, 19)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    Sleep(1000)
    NewScene("ED6_DT21/M7100   ._SN", 102, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_15_53F6 end

    def Function_16_5556(): pass

    label("Function_16_5556")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -40, 600, 22450, 180)
    SetChrPos(0x1, -800, 600, 23250, 180)
    SetChrPos(0x2, 770, 600, 23280, 180)
    SetChrPos(0x3, 20, 600, 24220, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 600, 23260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 18)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_16_5556 end

    def Function_17_5634(): pass

    label("Function_17_5634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5645")
    Call(0, 15)
    Return()

    label("loc_5645")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -40, 600, 22450, 0)
    SetChrPos(0x2, -800, 600, 23250, 0)
    SetChrPos(0x1, 770, 600, 23280, 0)
    SetChrPos(0x0, 20, 600, 24220, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 600, 23260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    NewScene("ED6_DT21/M7100   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_5634 end

    def Function_18_5701(): pass

    label("Function_18_5701")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_572A")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_571E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_571E)

    label("loc_572A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5753")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5747():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5747)

    label("loc_5753")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_577C")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5770():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5770)

    label("loc_577C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57A5")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5799():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5799)

    label("loc_57A5")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57D1")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_57D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57E8")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_57E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57FF")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_57FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5816")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_5816")

    Return()

    # Function_18_5701 end

    def Function_19_5817(): pass

    label("Function_19_5817")


    def lambda_581D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_581D)

    def lambda_582F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_582F)

    def lambda_5841():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5841)

    def lambda_5853():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5853)
    Sleep(1000)
    Return()

    # Function_19_5817 end

    SaveToFile()

Try(main)
