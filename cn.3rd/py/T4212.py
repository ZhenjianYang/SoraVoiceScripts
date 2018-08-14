from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4212   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4212.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '达扬',                                 # 9
        '托克斯',                               # 10
        '目标用照相机',                         # 11
        '',                                     # 12
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
        'ED6_DT07/CH01570 ._CH',             # 00
        'ED6_DT07/CH01560 ._CH',             # 01
        'ED6_DT07/CH01220 ._CH',             # 02
        'ED6_DT07/CH02140 ._CH',             # 03
        'ED6_DT07/CH02470 ._CH',             # 04
        'ED6_DT07/CH01120 ._CH',             # 05
        'ED6_DT07/CH01020 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
        'ED6_DT27/CH03233 ._CH',             # 08
        'ED6_DT26/CH20692 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01570P._CP',             # 00
        'ED6_DT07/CH01560P._CP',             # 01
        'ED6_DT07/CH01220P._CP',             # 02
        'ED6_DT07/CH02140P._CP',             # 03
        'ED6_DT07/CH02470P._CP',             # 04
        'ED6_DT07/CH01120P._CP',             # 05
        'ED6_DT07/CH01020P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
        'ED6_DT27/CH03233P._CP',             # 08
        'ED6_DT26/CH20692P._CP',             # 09
    )

    DeclNpc(
        X                   = -68100,
        Z                   = 0,
        Y                   = -32320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -70880,
        Z                   = 0,
        Y                   = -37790,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_15A",          # 00, 0
        "Function_1_170",          # 01, 1
        "Function_2_17A",          # 02, 2
        "Function_3_D41",          # 03, 3
        "Function_4_D89",          # 04, 4
    )


    def Function_0_15A(): pass

    label("Function_0_15A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_16F")

    Return()

    # Function_0_15A end

    def Function_1_170(): pass

    label("Function_1_170")

    OP_B1("t4212_n")
    Return()

    # Function_1_170 end

    def Function_2_17A(): pass

    label("Function_2_17A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-57780, 0, -39420, 0)
    OP_67(0, 7600, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x151, -58000, -750, -39360, 270)
    SetChrPos(0x103, -58000, -750, -40820, 270)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)

    def lambda_20A():
        OP_6D(-60780, 0, -39420, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_20A)
    Sleep(1000)

    def lambda_227():
        OP_8E(0xFE, 0xFFFF1000, 0x0, 0xFFFF608C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_227)

    def lambda_242():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_242)

    def lambda_254():
        OP_8E(0xFE, 0xFFFF0F88, 0x0, 0xFFFF6640, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_254)

    def lambda_26F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_26F)
    WaitChrThread(0x151, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x151,
        (
            "#1650F呼，\x01",
            "终于到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        (
            "#1645F呼、呼、呼……\x02\x03",

            "你竟然能跟上我跑步的速度，\x01",
            "真是不简单啊………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x151, 0x103, 500)
    Sleep(1000)
    TurnDirection(0x103, 0x151, 500)
    Sleep(300)

    ChrTalk(    #2
        0x103,
        (
            "#1640F……好，\x01",
            "赶快把手续办了吧。\x02\x03",

            "我就在这里等着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x151,
        (
            "#1650F…………嗯。\x02\x03",

            "#1651F请稍等。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x151, 0x40)
    SetChrFlags(0x151, 0x4)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x103, 0x4)

    def lambda_3C6():

        label("loc_3C6")

        TurnDirection(0xFE, 0x151, 400)
        OP_48()
        Jump("loc_3C6")

    QueueWorkItem2(0x103, 3, lambda_3C6)

    def lambda_3D7():
        OP_8E(0xFE, 0xFFFF0600, 0x0, 0xFFFF6640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3D7)
    WaitChrThread(0x151, 0x1)

    def lambda_3F7():
        OP_6D(-65160, 0, -33200, 4500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3F7)

    def lambda_40F():
        OP_8E(0xFE, 0xFFFF0600, 0x0, 0xFFFF8238, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_40F)
    WaitChrThread(0x151, 0x1)

    def lambda_42F():
        OP_8E(0xFE, 0xFFFEFE30, 0x0, 0xFFFF8238, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_42F)
    WaitChrThread(0x151, 0x1)
    Sleep(300)
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x151)
    Sleep(500)

    def lambda_473():

        label("loc_473")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_473")

    QueueWorkItem2(0x151, 2, lambda_473)
    Fade(500)
    SetChrPos(0x10, -67100, 0, -32000, 90)
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10)
    Sleep(500)

    def lambda_4BE():
        OP_8E(0xFE, 0xFFFEFEBC, 0x0, 0xFFFF8774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4BE)
    WaitChrThread(0x10, 0x1)

    def lambda_4DE():
        OP_8E(0xFE, 0xFFFF03E4, 0x0, 0xFFFF8274, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4DE)
    WaitChrThread(0x10, 0x1)

    def lambda_4FE():
        OP_6D(-63500, 0, -39200, 3500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_4FE)

    def lambda_516():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_516)

    def lambda_526():
        OP_8E(0xFE, 0xFFFF03E4, 0x0, 0xFFFF6938, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_526)
    Sleep(500)
    OP_44(0x151, 0x2)
    OP_43(0x151, 0x3, 0x0, 0x3)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 270, 500)
    Sleep(500)
    OP_22(0x12, 0x0, 0x5A)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10)
    Sleep(500)

    def lambda_586():
        OP_8F(0xFE, 0xFFFF07CC, 0x0, 0xFFFF6938, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_586)
    WaitChrThread(0x10, 0x1)

    def lambda_5A6():
        OP_8E(0xFE, 0xFFFF03E4, 0x0, 0xFFFF6938, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5A6)
    WaitChrThread(0x151, 0x1)

    def lambda_5C6():
        OP_8E(0xFE, 0xFFFF0024, 0x0, 0xFFFF6938, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5C6)
    WaitChrThread(0x151, 0x1)
    Fade(500)
    SetChrChipByIndex(0x151, 9)
    SetChrSubChip(0x151, 0)
    SetChrFlags(0x151, 0x4)
    SetChrPos(0x151, -65780, 200, -39500, 270)
    Sleep(500)

    def lambda_610():
        OP_8E(0xFE, 0xFFFF0024, 0x0, 0xFFFF6938, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_610)
    WaitChrThread(0x10, 0x1)
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10)
    Sleep(1000)
    OP_62(0x151, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x151)
    Sleep(500)

    def lambda_673():
        OP_8F(0xFE, 0xFFFF040C, 0x0, 0xFFFF6B90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_673)
    WaitChrThread(0x10, 0x1)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05爱娜在继承条款上签了字。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #5
        0x103,
        (
            "#1640F（太好了，爱娜。）\x02\x03",

            "（…………恭喜你。）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x151, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x151)
    Sleep(500)
    OP_62(0x151, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)
    Fade(500)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    ClearChrFlags(0x151, 0x4)
    SetChrPos(0x151, -65420, 0, -40300, 270)
    Sleep(800)
    OP_8C(0x151, 90, 500)
    Sleep(300)

    def lambda_791():
        OP_8E(0xFE, 0xFFFF0524, 0x0, 0xFFFF6168, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_791)
    WaitChrThread(0x151, 0x1)

    ChrTalk(    #6
        0x151,
        (
            "#1650F#3P对了，雪拉扎德。\x02\x03",

            "好像还需要一个人\x01",
            "作为公证人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        "#1643F诶…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x151,
        "#1650F#3P我能拜托你吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#1643F诶……哎，好的。#1800W \x01",
            "#20W如果我可以的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x151,
        (
            "#1650F#3P……嗯。\x02\x03",

            "#1651F我想拜托你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        (
            "#1643F…………………………\x02\x03",

            "#1640F这点小事当然没问题了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x103, 0x3)
    OP_43(0x151, 0x3, 0x0, 0x4)

    def lambda_911():
        OP_8E(0xFE, 0xFFFF0024, 0x0, 0xFFFF6294, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_911)
    WaitChrThread(0x103, 0x1)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x103, 8)
    SetChrSubChip(0x103, 0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, -65780, 200, -39500, 270)
    WaitChrThread(0x151, 0x3)
    Sleep(800)
    OP_62(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x103)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x18\x07\x0C#40W我从来没想到过\x01",
            "自己能为别人当一次公证人。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #13
        "\x18\x07\x0C#40W作为一名游击士。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #14
        "\x18\x07\x0C#40W能够有这样自豪的生存方式……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(100)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05根据萨乌尔·乔·霍尔登的遗嘱，\x01",
            "其遗产由爱娜·霍尔登继承。\x01",
            "　#7640W \x01",
            "#20W　\x01",
            "　\x01",
            "　　　　　　　公证人 雪拉扎德·哈维\x02",
        )
    )

    Jump("loc_AC3")

    label("loc_AC3")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("爱娜")

    AnonymousTalk(    #16
        "\x07\x00#1650F谢谢你，雪拉扎德。\x02",
    )

    Jump("loc_AFB")

    label("loc_AFB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrPos(0x151, -64099, 0, -40460, 270)
    OP_22(0xB5, 0x0, 0x50)
    Sleep(2500)
    OP_22(0xB5, 0x0, 0x50)
    Sleep(1000)
    FadeToBright(2500, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #17
        0x103,
        "#1640F……结束了………………\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    SetChrPos(0x103, -65500, 0, -40300, 270)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    ClearChrFlags(0x103, 0x4)
    WaitChrThread(0x151, 0x3)
    Sleep(800)

    ChrTalk(    #18
        0x103,
        "#1640F这样委托就完成了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x151,
        (
            "#1654F#11P……不，\x01",
            "还有一件工作要做。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x103, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    TurnDirection(0x103, 0x151, 500)
    Sleep(500)

    ChrTalk(    #20
        0x103,
        "#1643F#3S#6P哎…………！！？#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x151, 0x10, 400)
    Sleep(500)

    ChrTalk(    #21
        0x151,
        (
            "#1650F#12P对不起……\x01",
            "请问这里能领张申请书吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x151, 400)
    FadeToDark(2000, 0, -1)

    def lambda_CC6():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CC6)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #22
        (
            "\x07\x00我想把这些钱寄给\x01",
            "女王陛下的福利基金会……\x02",
        )
    )

    Jump("loc_D20")

    label("loc_D20")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/T4150   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_17A end

    def Function_3_D41(): pass

    label("Function_3_D41")


    def lambda_D47():
        OP_8E(0xFE, 0xFFFF03E4, 0x0, 0xFFFF8238, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_D47)
    WaitChrThread(0x151, 0x1)

    def lambda_D67():
        OP_8E(0xFE, 0xFFFF03E4, 0x0, 0xFFFF6E4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_D67)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x151, 225, 500)
    Return()

    # Function_3_D41 end

    def Function_4_D89(): pass

    label("Function_4_D89")


    def lambda_D8F():

        label("loc_D8F")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_D8F")

    QueueWorkItem2(0x151, 2, lambda_D8F)
    Sleep(400)

    def lambda_DA5():
        OP_8F(0xFE, 0xFFFF0560, 0x0, 0xFFFF5D80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_DA5)
    WaitChrThread(0x151, 0x1)
    Sleep(400)

    def lambda_DCA():
        OP_8F(0xFE, 0xFFFF0380, 0x0, 0xFFFF6334, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_DCA)
    WaitChrThread(0x151, 0x1)
    OP_44(0x151, 0x2)
    OP_8C(0x151, 270, 500)
    Return()

    # Function_4_D89 end

    SaveToFile()

Try(main)
