from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4104   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60018",
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
        '穆拉少校',                             # 9
        '目标用摄影机',                         # 10
        '',                                     # 11
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
        'ED6_DT27/CH03930 ._CH',             # 00
        'ED6_DT07/CH01560 ._CH',             # 01
        'ED6_DT07/CH01200 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH01220 ._CH',             # 04
        'ED6_DT07/CH01230 ._CH',             # 05
        'ED6_DT07/CH01180 ._CH',             # 06
        'ED6_DT07/CH01490 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03930P._CP',             # 00
        'ED6_DT07/CH01560P._CP',             # 01
        'ED6_DT07/CH01200P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH01220P._CP',             # 04
        'ED6_DT07/CH01230P._CP',             # 05
        'ED6_DT07/CH01180P._CP',             # 06
        'ED6_DT07/CH01490P._CP',             # 07
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
        "Function_0_12A",          # 00, 0
        "Function_1_153",          # 01, 1
        "Function_2_160",          # 02, 2
        "Function_3_4B8",          # 03, 3
    )


    def Function_0_12A(): pass

    label("Function_0_12A")

    OP_B1("t4104_n")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_152")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_152")

    Return()

    # Function_0_12A end

    def Function_1_153(): pass

    label("Function_1_153")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_71(0x407, 0x0)
    ExitThread()
    Return()

    # Function_1_153 end

    def Function_2_160(): pass

    label("Function_2_160")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2701D2, 0x2701D7, 0xC)
    OP_D2(0x2702C2, 0x2702CC, 0xD)
    OP_D2(0x2702C2, 0x2702CC, 0xE)
    OP_D2(0x2702D6, 0x2702E0, 0xF)
    OP_D2(0x2702DA, 0x2702E4, 0x10)
    OP_D2(0x2702C4, 0x2702CE, 0x11)
    OP_D2(0x2701D2, 0x2701D7, 0x12)
    OP_D2(0x2701D2, 0x2701D7, 0x13)
    OP_6D(1900, 0, -6140, 0)
    OP_67(0, 9420, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(46000, 0)
    OP_6E(402, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 1000, 0, -3920, 180)
    SetChrPos(0x10E, 1000, 0, -9220, 0)

    def lambda_230():
        OP_6B(3140, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_230)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x0)
    Fade(1000)
    OP_6D(2400, 0, -5760, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(46000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x10,
        (
            "#272F#5P……一战决胜负。\x02\x03",

            "#270F不过，\x01",
            "可以使用魔法或道具。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #1
        0x10E,
        "尤莉亚上尉",
        (
            "#179F#12P……原来如此，\x01",
            "这样似乎确实能散散心。\x02\x03",

            "#171F虽然以埃雷波尼亚\x01",
            "武术名门范德尔为对手，\x01",
            "没有什么取胜的信心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "#277F#5P呵呵，不用客气。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6B(3040, 0)
    SetChrChipByIndex(0x10, 17)
    SetChrSubChip(0x10, 1)
    OP_22(0x1F9, 0x0, 0x64)
    OP_99(0x10, 0x1, 0x6, 0x7D0)
    Sleep(300)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 15)
    SetChrSubChip(0x10E, 0)
    Sleep(700)

    ChrTalk(    #3
        0x10,
        "#272F#5P那么上尉……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #4
        0x10,
        "#271F#5P#4S我会尽全力出战！\x02",
    )

    OP_7C(0x0, 0x12C, 0x64, 0x12C)
    CloseMessageWindow()
    OP_41(0xD, 0x0, 0xFF)
    OP_31(0xD, 0x10, 0x5A)
    OP_31(0xD, 0x5, 0xC8)
    OP_31(0xD, 0xFE, 0x0)
    OP_35(0xD, 0xFFFF)
    OP_34(0xD, 0xFFFF)
    OP_35(0xD, 0x0)
    OP_BB(0xD, 0x6, 0x118)
    OP_37(0xD, 0x7F, 0x0)
    OP_37(0xD, 0x7F, 0x2)
    OP_41(0xD, 0x3E8, 0xFF)
    OP_34(0xD, 0x82)
    OP_34(0xD, 0x83)
    OP_34(0xD, 0x39)
    OP_34(0xD, 0x46)
    OP_34(0xD, 0x47)
    OP_34(0xD, 0x16)
    OP_3E(0x207, 2)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3BA, 0x300003, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 3)
    Return()

    # Function_2_160 end

    def Function_3_4B8(): pass

    label("Function_3_4B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_31(0xD, 0xFC, 0x0)
    OP_31(0xD, 0xFE, 0x0)
    OP_1D(0xE)
    OP_6D(2400, 0, -5760, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(46000, 0)
    OP_6E(262, 0)
    OP_D2(0x2701D2, 0x2701D7, 0xC)
    OP_D2(0x2702C2, 0x2702CC, 0xD)
    OP_D2(0x2702C2, 0x2702CC, 0xE)
    OP_D2(0x2702D6, 0x2702E0, 0xF)
    OP_D2(0x2702DA, 0x2702E4, 0x10)
    OP_D2(0x2701D2, 0x2701D7, 0x11)
    OP_D2(0x2701D2, 0x2701D7, 0x12)
    OP_D2(0x2701D2, 0x2701D7, 0x13)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_56D"),
        (0, "loc_57A"),
        (SWITCH_DEFAULT, "loc_587"),
    )


    label("loc_56D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_587")

    label("loc_57A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_587")

    label("loc_587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "◆赢了\x01",      # 0
            "◆输了\x01",      # 1
        )
    )

    Jump("loc_5C1")

    label("loc_5C1")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)

    label("loc_5D2")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_5E3"),
        (0, "loc_621"),
        (SWITCH_DEFAULT, "loc_65F"),
    )


    label("loc_5E3")

    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 14)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 1000, 0, -3920, 180)
    SetChrPos(0x10E, 1000, 0, -9220, 0)
    SetChrChipByIndex(0x10E, 16)
    SetChrSubChip(0x10E, 3)
    Jump("loc_65F")

    label("loc_621")

    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 14)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 1000, 0, -3920, 180)
    SetChrPos(0x10E, 1000, 0, -9220, 0)
    SetChrChipByIndex(0x10E, 15)
    SetChrSubChip(0x10E, 0)
    Jump("loc_65F")

    label("loc_65F")


    def lambda_665():
        OP_6B(3140, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_665)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_68F"),
        (0, "loc_C93"),
        (SWITCH_DEFAULT, "loc_13FE"),
    )


    label("loc_68F")


    def lambda_695():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_695)
    Sleep(1000)

    NpcTalk(    #5
        0x10E,
        "尤莉亚上尉",
        (
            "#176F#12P#40W呼、呼、呼…………\x02\x03",

            "#179F呼………\x01",
            "的确是强啊…………！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        "#272F#5P上尉…………\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)

    def lambda_752():
        OP_6D(2400, 0, -6120, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_752)

    def lambda_76A():
        OP_8E(0xFE, 0x3E8, 0x0, 0xFFFFE714, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_76A)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #7
        0x10,
        "#270F#5P……输了之后，你失去了什么？\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x10E, 0xFFFFFED4, 1700, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)

    NpcTalk(    #8
        0x10E,
        "尤莉亚上尉",
        "#173F#12P……少校………………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#270F#5P……事物的价值，\x01",
            "只要想像一下失去它的情景\x01",
            "就能很快弄清楚。\x02\x03",

            "不需要什么理由，\x01",
            "自然而然就能看到它的本质了。\x02\x03",

            "#272F……现在你可以想像一下\x01",
            "没有自己的世界会是什么样子。\x02\x03",

            "在此基础上，\x01",
            "如果还有无论如何\x01",
            "都放心不下的事情……\x02\x03",

            "#277F上尉，\x01",
            "那就是你的心之所向。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #10
        0x10E,
        "尤莉亚上尉",
        (
            "#175F#12P…………放心不下的事情……\x02\x03",

            "………………………………\x01",
            "………………………………\x02\x03",

            "#176F（殿下………………\x01",
            "  …………我还是……）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(500)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    OP_99(0x10E, 0x3, 0x2, 0x1F4)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #11
        0x10E,
        "尤莉亚上尉",
        (
            "#179F#12P少校………………\x01",
            "………感激不尽。\x02\x03",

            "#171F多亏了您，\x01",
            "我的迷惑一扫而空。\x02\x03",

            "您的教导，\x01",
            "我会铭记在心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#275F#5P呵呵，不过是现炒现卖罢了。\x02\x03",

            "我在和那家伙相处倦了的时候\x01",
            "也经常以与叔父大人比剑的方式\x01",
            "来转换心情。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)
    OP_8C(0x10, 90, 400)
    Sleep(300)

    ChrTalk(    #13
        0x10,
        (
            "#278F#5P……我差不多\x01",
            "也该回国去了。\x02\x03",

            "总是忍不住\x01",
            "要担心那赖皮蛋啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #14
        0x10E,
        "尤莉亚上尉",
        (
            "#171F#12P呵呵…………是吗。\x02\x03",

            "#179F也请代我\x01",
            "向皇子问好。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)
    Sleep(300)

    ChrTalk(    #15
        0x10,
        (
            "#277F#5P……我明白了。\x02\x03",

            "也祝科洛蒂娅殿下\x01",
            "身体健康。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 500)
    Sleep(300)

    def lambda_C53():
        OP_6D(2400, 0, -4760, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_C53)

    def lambda_C6B():
        OP_8E(0xFE, 0x3E8, 0x0, 0x15CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_C6B)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_13FE")

    label("loc_C93")

    Sleep(500)

    NpcTalk(    #16
        0x10E,
        "尤莉亚上尉",
        "#176F#12P#40W呼……呼…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#273F#5P…………真令人惊讶。\x02\x03",

            "#272F没想到上尉本领如此高超……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #18
        0x10E,
        "尤莉亚上尉",
        (
            "#179F#12P呵呵，见笑了……\x02\x03",

            "#170F少校肯定\x01",
            "手下留情了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#278F#5P……不，\x01",
            "我还没有那种实力。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #20
        0x10,
        (
            "#277F真是期待\x01",
            "再一次的切磋呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #21
        0x10E,
        "尤莉亚上尉",
        "#179F#12P我会不断努力进步的。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #22
        0x10,
        "#272F#5P上尉…………\x02",
    )

    CloseMessageWindow()

    def lambda_E80():
        OP_6D(2400, 0, -6120, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_E80)

    def lambda_E98():
        OP_8E(0xFE, 0x3E8, 0x0, 0xFFFFE714, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E98)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #23
        0x10,
        (
            "#272F#5P……你说你没有守护好\x01",
            "应该守护的人。\x02\x03",

            "#270F……那么，你失去了什么吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #24
        0x10E,
        "尤莉亚上尉",
        "#173F#12P……少校………………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#270F#5P……事物的价值，\x01",
            "只要想像一下失去它的情景\x01",
            "就能很快弄清楚。\x02\x03",

            "不需要什么理由，\x01",
            "自然而然就能看到它的本质了。\x02\x03",

            "#272F……现在你可以想像一下\x01",
            "没有自己的世界会是什么样子。\x02\x03",

            "在此基础上，\x01",
            "如果还有无论如何\x01",
            "都放心不下的事情……\x02\x03",

            "#277F上尉，\x01",
            "那就是你的心之所向。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #26
        0x10E,
        "尤莉亚上尉",
        (
            "#175F#12P…………放心不下的事情……\x02\x03",

            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2200)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #27
        0x10E,
        "尤莉亚上尉",
        (
            "#176F#12P（殿下………………\x01",
            "  …………我还是……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #28
        0x10E,
        "尤莉亚上尉",
        (
            "#179F#12P少校………………\x01",
            "………感激不尽。\x02\x03",

            "#171F多亏了您，\x01",
            "我的迷惑一扫而空。\x02\x03",

            "您的教导，\x01",
            "我会铭记在心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#275F#5P呵呵，不过是现炒现卖罢了。\x02\x03",

            "我在和那家伙相处倦了的时候\x01",
            "也经常以与叔父大人比剑的方式\x01",
            "来转换心情。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)
    OP_8C(0x10, 90, 400)
    Sleep(500)

    ChrTalk(    #30
        0x10,
        (
            "#278F#5P……我差不多\x01",
            "也该回国去了。\x02\x03",

            "总是忍不住\x01",
            "要担心那赖皮蛋啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #31
        0x10E,
        "尤莉亚上尉",
        (
            "#171F#12P呵呵…………是吗。\x02\x03",

            "#179F也请代我\x01",
            "向皇子问好。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)
    Sleep(300)

    ChrTalk(    #32
        0x10,
        (
            "#277F#5P……我明白了。\x02\x03",

            "也祝科洛蒂娅殿下\x01",
            "身体健康。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 500)
    Sleep(300)

    def lambda_13BE():
        OP_6D(2400, 0, -4760, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_13BE)

    def lambda_13D6():
        OP_8E(0xFE, 0x3E8, 0x0, 0x15CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13D6)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_13FE")

    label("loc_13FE")

    OP_20(0xFA0)
    OP_21()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_4B8 end

    SaveToFile()

Try(main)
