from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R0201   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0201.x',
        MapIndex            = 22,
        MapDefaultBGM       = "ed60029",
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
        '约修亚',                               # 9
        '目标用照相机',                         # 10
        '雾调整',                               # 11
        '洛连特方向',                           # 12
        '威尔特桥·关所方向',                   # 13
        '帕赛尔农场方向',                       # 14
        '',                                     # 15
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
        'ED6_DT07/CH02750 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02750P._CP',             # 00
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
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
        X                   = -131580,
        Z                   = 0,
        Y                   = -18130,
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
        X                   = -224350,
        Z                   = 20,
        Y                   = -16180,
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
        X                   = -184980,
        Z                   = 0,
        Y                   = -81290,
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


    DeclActor(
        TriggerX            = -179550,
        TriggerZ            = 0,
        TriggerY            = -15360,
        TriggerRange        = 1500,
        ActorX              = -179550,
        ActorZ              = 1500,
        ActorY              = -15360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_196",          # 00, 0
        "Function_1_1B5",          # 01, 1
        "Function_2_1C8",          # 02, 2
        "Function_3_1DE",          # 03, 3
        "Function_4_879",          # 04, 4
        "Function_5_8DA",          # 05, 5
    )


    def Function_0_196(): pass

    label("Function_0_196")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_1B4")

    Return()

    # Function_0_196 end

    def Function_1_1B5(): pass

    label("Function_1_1B5")

    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    Return()

    # Function_1_1B5 end

    def Function_2_1C8(): pass

    label("Function_2_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1C8")

    label("loc_1DD")

    Return()

    # Function_2_1C8 end

    def Function_3_1DE(): pass

    label("Function_3_1DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0 op#A op#5
        "\x18\x07\x00#35A#40W――Several Weeks Later.　\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00就这样，平稳的几个星期过去了……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00约修亚的伤渐渐痊愈，能够走路了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x00艾丝蒂尔自然喜出望外，\x01",
            "东跑西跑地带着约修亚到处玩耍。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x00可是身体能够行动，\x01",
            "并不代表他已找到了答案。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00抉择的时刻，慢慢迫近……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_1D(0x58)
    OP_6D(-152800, 0, -17910, 0)
    OP_67(0, 8980, -10000, 0)
    OP_6B(3810, 0)
    OP_6C(237000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, -148950, 0, -17700, 270)
    SetChrPos(0x10, -147000, 0, -17700, 270)
    OP_43(0x101, 0x3, 0x0, 0x4)
    OP_43(0x10, 0x3, 0x0, 0x4)

    def lambda_3BE():
        OP_6D(-179410, 0, -15260, 10000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3BE)

    def lambda_3D6():
        OP_67(0, 5500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3D6)

    def lambda_3EE():
        OP_6B(2900, 10000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3EE)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrPos(0x101, -171150, 0, -10350, 240)
    SetChrPos(0x10, -170520, 0, -9030, 240)

    def lambda_437():
        OP_8E(0xFE, 0xFFFD4A86, 0xFFFFFFF6, 0xFFFFC752, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_437)
    Sleep(100)

    def lambda_457():
        OP_8E(0xFE, 0xFFFD4B76, 0xFFFFFFF6, 0xFFFFCB8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_457)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #6
        "\x07\x05南　帕赛尔农场\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #7
        0x10,
        (
            "#1678F#6P帕赛尔…………\x02\x03",

            "#1676F是那个短发的女孩吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #8
        0x101,
        (
            "#290F#5P嗯，这个农场，\x01",
            "就是缇欧的家呢～。\x02\x03",

            "缇欧家啊，前不久……\x02\x03",

            "#291F刚刚生下\x01",
            "一对双胞胎哦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)
    Sleep(300)

    ChrTalk(    #9
        0x10,
        (
            "#1677F#12P……我知道。\x01",
            "你当时还又跳又闹的呢。\x02\x03",

            "#1671F都去看过好多次了吧。\x01",
            "还有那么稀奇吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#291F#5P嗯，不是啦。\x01",
            "今天一天，要帮忙干农活哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x101,
        (
            "#290F#5P现在刚好是收获季节。\x02\x03",

            "但是汉娜阿姨行动不方便，\x01",
            "会比往常更辛苦吧？\x02\x03",

            "#291F我跟伊莉莎说了，\x01",
            "打算一起来帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#1677F#12P……你的这份心意\x01",
            "确实令人感动……\x02\x03",

            "#1675F可是，为什么连我也要……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#292F#5P少在那里啰啰嗦嗦的啦！\x02\x03",

            "好了，快走啦！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_787():
        OP_8E(0xFE, 0xFFFD4AEA, 0xFFFFFFF6, 0xFFFFC93C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_787)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 500)

    def lambda_7AE():
        OP_8E(0xFE, 0xFFFD4AEA, 0xFFFFFFF6, 0xFFFFA22C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7AE)

    def lambda_7C9():
        OP_8E(0xFE, 0xFFFD4B76, 0xFFFFFFF6, 0xFFFFA47A, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7C9)
    Sleep(400)

    ChrTalk(    #14 op#A
        0x101,
        (
            "#294F#2P#15A这也算是『康福运动』啦，\x01",
            "『康福运动』！\x02",
        )
    )

    Sleep(1800)

    ChrTalk(    #15 op#A
        0x10,
        "#1677F#4P#25A你是想说『康复运动』吧……\x02",
    )

    Sleep(1800)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T0400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1DE end

    def Function_4_879(): pass

    label("Function_4_879")


    def lambda_87F():
        OP_8E(0xFE, 0xFFFDA0BC, 0x0, 0xFFFFBADC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87F)
    WaitChrThread(0xFE, 0x1)

    def lambda_89F():
        OP_8E(0xFE, 0xFFFD93E2, 0xA, 0xFFFFCBBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_89F)
    WaitChrThread(0xFE, 0x1)

    def lambda_8BF():
        OP_8E(0xFE, 0xFFFD6A0C, 0x0, 0xFFFFCBBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8BF)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_879 end

    def Function_5_8DA(): pass

    label("Function_5_8DA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        "\x07\x05南　帕赛尔农场\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_8DA end

    SaveToFile()

Try(main)
