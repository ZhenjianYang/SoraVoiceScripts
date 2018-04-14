from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2105   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2105.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        '银发的青年',                           # 10
        '迪恩',                                 # 11
        '雷斯',                                 # 12
        '洛克',                                 # 13
        '凯文神父',                             # 14
        '中型福音',                             # 15
        '阿伊纳街道方向',                       # 16
        '卢安市·北街区',                       # 17
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
        'ED6_DT07/CH02040 ._CH',             # 01
        'ED6_DT27/CH04530 ._CH',             # 02
        'ED6_DT27/CH04540 ._CH',             # 03
        'ED6_DT07/CH02510 ._CH',             # 04
        'ED6_DT07/CH02520 ._CH',             # 05
        'ED6_DT07/CH02530 ._CH',             # 06
        'ED6_DT27/CH03080 ._CH',             # 07
        'ED6_DT27/CH04087 ._CH',             # 08
        'ED6_DT26/CH20243 ._CH',             # 09
        'ED6_DT26/CH20273 ._CH',             # 0A
        'ED6_DT26/CH20283 ._CH',             # 0B
        'ED6_DT26/CH20278 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT27/CH03530P._CP',             # 00
        'ED6_DT07/CH02040P._CP',             # 01
        'ED6_DT27/CH04530P._CP',             # 02
        'ED6_DT27/CH04540P._CP',             # 03
        'ED6_DT07/CH02510P._CP',             # 04
        'ED6_DT07/CH02520P._CP',             # 05
        'ED6_DT07/CH02530P._CP',             # 06
        'ED6_DT27/CH03080P._CP',             # 07
        'ED6_DT27/CH04087P._CP',             # 08
        'ED6_DT26/CH20243P._CP',             # 09
        'ED6_DT26/CH20273P._CP',             # 0A
        'ED6_DT26/CH20283P._CP',             # 0B
        'ED6_DT26/CH20278P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 73210,
        Z                   = 0,
        Y                   = -16650,
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
        X                   = 50980,
        Z                   = 400,
        Y                   = 77990,
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


    DeclEvent(
        X                   = 31200,
        Y                   = 0,
        Z                   = 25340,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = 77280,
        Y                   = 0,
        Z                   = 22060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 7,
    )


    ScpFunction(
        "Function_0_272",          # 00, 0
        "Function_1_280",          # 01, 1
        "Function_2_2C0",          # 02, 2
        "Function_3_125D",         # 03, 3
        "Function_4_12E6",         # 04, 4
        "Function_5_1374",         # 05, 5
        "Function_6_138A",         # 06, 6
        "Function_7_138E",         # 07, 7
    )


    def Function_0_272(): pass

    label("Function_0_272")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Return()

    # Function_0_272 end

    def Function_1_280(): pass

    label("Function_1_280")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFE7960, 0x230048)
    OP_22(0x1C5, 0x0, 0x64)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    Return()

    # Function_1_280 end

    def Function_2_2C0(): pass

    label("Function_2_2C0")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, 23440, 7780, 1910, 0)
    SetChrPos(0x1, 23440, 7780, 1910, 0)
    SetChrPos(0x2, 23440, 7780, 1910, 0)
    SetChrPos(0x3, 23440, 7780, 1910, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 23460, 8800, 3630, 0)
    OP_6D(47110, 7780, 30010, 0)
    OP_67(0, 8050, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(31000, 0)
    OP_6E(505, 0)

    def lambda_37D():
        OP_6D(25710, 8800, 4920, 9000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_37D)

    def lambda_395():
        OP_67(0, 14180, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_395)

    def lambda_3AD():
        OP_6C(142000, 9000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3AD)

    def lambda_3BD():
        OP_6E(241, 9000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3BD)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(8000)
    OP_44(0x0, 0x1)
    OP_44(0x0, 0x2)
    OP_44(0x0, 0x3)
    OP_44(0x1, 0x1)
    Fade(1000)
    OP_6D(24530, 6120, 8189, 0)
    OP_67(0, 6940, -10000, 0)
    OP_6B(2050, 0)
    OP_6C(33000, 0)
    OP_6E(487, 0)
    OP_0D()
    SetChrPos(0x9, 31670, 7800, 110, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#231F──就这样宴会终于结束，\x01",
            "留在热气中的我们只有困惑……\x02\x03",

            "苍凉的月影和跨海的凉风\x01",
            "静静等待着灼热血潮的冷却……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #1
        0x9,
        "青年的声音",
        "#1P……久等了。\x02",
    )

    CloseMessageWindow()

    def lambda_4E9():
        OP_6D(28050, 7800, 2290, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_4E9)

    def lambda_501():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_501)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x2)
    OP_8C(0x8, 90, 400)
    Sleep(500)

    ChrTalk(    #2
        0x8,
        (
            "#231F#5P呵呵，时间刚刚好。\x02\x03",

            "你还是那个守规矩的男人。\x02\x03",

            "偶尔迟到一下\x01",
            "也没什么关系吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_580():

        label("loc_580")

        TurnDirection(0x8, 0x9, 400)
        OP_48()
        Jump("loc_580")

    QueueWorkItem2(0x8, 3, lambda_580)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 1)
    OP_99(0x9, 0x1, 0x2, 0x5DC)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_5B1():
        OP_6D(23740, 7800, 1150, 1500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_5B1)

    def lambda_5C9():
        OP_67(0, 7500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C9)

    def lambda_5E1():
        OP_96(0x9, 0x5B5E, 0x1E78, 0xFFFFFDDA, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5E1)
    WaitChrThread(0x9, 0x1)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    TurnDirection(0x9, 0x8, 400)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x3)

    ChrTalk(    #3
        0x9,
        (
            "#124F这是天性。\x02\x03",

            "#120F事不宜迟，\x01",
            "赶快报告给我听吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_96(0x8, 0x5B90, 0x1E78, 0x8AC, 0x64, 0x1388)
    Sleep(500)

    ChrTalk(    #4
        0x8,
        (
            "#230F#5P哈哈，别那么着急嘛。\x02\x03",

            "今晚心情多好。\x01",
            "让我稍微沉浸一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#123F哎呀哎呀……\x01",
            "看来相当中意啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#231F#5P唔，美丽的公主\x01",
            "越发夺去了我的心。\x02\x03",

            "而且在意外之处\x01",
            "还遇到了美妙的好对手。\x02\x03",

            "#230F呵呵呵……\x01",
            "看来就要忙起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "#124F真拿你没办法。\x02\x03",

            "#120F个人兴趣倒也无妨，\x01",
            "但记住别因为兴趣而妨碍计划。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#230F#5P呵呵，这个不必担心。\x02\x03",

            "那么收下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x9, 0x3E8, 0x7D0, 0x0)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrSubChip(0x8, 8)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 23740, 7500, 400, 0)
    OP_0D()
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 7)
    SetChrFlags(0xE, 0x80)
    OP_0D()
    OP_8F(0x8, 0x5B90, 0x1E78, 0x76C, 0x7D0, 0x0)

    ChrTalk(    #9
        0x9,
        (
            "#124F……确认回收。\x02\x03",

            "#120F那……\x01",
            "实验成果怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#232F#5P唔，这个啊。\x01",
            "可以说成功了九成左右吧。\x02\x03",

            "投影装置生出的映像\x01",
            "能够传送到相当远的地方。\x02\x03",

            "只不过，最初的１，２次\x01",
            "传送好像失败了……\x02\x03",

            "超过３次以后\x01",
            "运作就变得完美了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "#123F唔……\x01",
            "虽然有不稳定因素，但还不坏。\x02\x03",

            "赶快传达给教授吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#230F#5P不过这个『福音』……\x02\x03",

            "导力停止现象已经\x01",
            "远远超越了现在的技术。\x02\x03",

            "好像是『十三工房』制造的，\x01",
            "到底是个怎样的装置呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "#124F谁知道……\x01",
            "我也不清楚详情。\x02\x03",

            "#120F只是据教授所说，这些现象\x01",
            "只不过是『奇迹』的冰山一角。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#233F#5P噢，奇迹吗。\x02\x03",

            "#230F嗯……\x01",
            "奇迹是只有女神才能做到的事。\x02\x03",

            "到底代表着什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "#123F无论如何，真正的潜力\x01",
            "就用今后的实验来弄清楚吧。\x02\x03",

            "这样的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_B25():
        OP_8C(0x9, 250, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B25)
    WaitChrThread(0x9, 0x1)
    Fade(1000)
    OP_6D(22960, 7800, 30, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(1870, 0)
    OP_6C(306000, 0)
    OP_6E(487, 0)
    OP_0D()

    ChrTalk(    #16
        0x9,
        "#121F#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "#233F噢？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 250, 400)
    Sleep(500)

    ChrTalk(    #18
        0x8,
        (
            "#231F呵呵，今晚似乎\x01",
            "有不少意外的登场人物啊。\x02\x03",

            "那么，剧本该怎么写呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        "#124F#6P呼……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x9, 0x800)
    SetChrChipByIndex(0x9, 3)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #20
        0x9,
        (
            "#123F#6P那就要看藏身于此\x01",
            "的小老鼠的态度了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "#231F呵呵，没错。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x8,
        (
            "#231F好了……\x01",
            "小老鼠会用怎样的声音叫出来呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 29570, 0, 20890, 180)
    SetChrPos(0xB, 30570, 0, 21930, 180)
    SetChrPos(0xC, 28570, 0, 21930, 180)

    NpcTalk(    #23
        0xA,
        "醉了的声音",
        "#1P#1S……呜咿～………\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_D5D():
        OP_6D(23740, 7800, 2150, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_D5D)

    def lambda_D75():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D75)

    def lambda_D8D():
        OP_6C(35000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D8D)
    OP_8C(0x9, 0, 400)
    Sleep(200)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    WaitChrThread(0xA, 0x0)

    ChrTalk(    #24
        0x8,
        "#230F#5P呼……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x8, 250, 400)
    Sleep(300)

    ChrTalk(    #25
        0x8,
        (
            "#231F#5P虽不知道是哪里的小老鼠，\x01",
            "看来是捡回了条小命。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 1)
    OP_0D()
    Sleep(300)
    OP_8C(0x9, 250, 400)

    ChrTalk(    #26
        0x9,
        (
            "#121F#2P呵……\x01",
            "感谢女神吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E80():
        OP_6D(23020, 7800, -6000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E80)

    def lambda_E98():
        OP_6C(75000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E98)
    Sleep(500)
    OP_43(0x9, 0x0, 0x0, 0x3)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x9, 0x0)
    OP_43(0x8, 0x0, 0x0, 0x4)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x2)
    Sleep(500)

    def lambda_ED6():
        OP_6D(29380, 0, 7350, 5000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ED6)

    def lambda_EEE():
        OP_6C(108000, 5000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_EEE)

    def lambda_EFE():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_EFE)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    def lambda_F25():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFC75C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F25)
    Sleep(50)

    def lambda_F45():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFC950, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F45)
    Sleep(50)
    OP_90(0xC, 0x0, 0x0, 0xFFFFC75C, 0x7D0, 0x0)
    WaitChrThread(0x9, 0x2)
    OP_8C(0xB, 46, 400)
    Sleep(500)

    ChrTalk(    #27
        0xB,
        "#5P嘎哈哈，拿～酒来！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 135, 400)
    Sleep(500)

    ChrTalk(    #28
        0xA,
        "唔咕，不能再喝了……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 300, 400)
    Sleep(500)

    ChrTalk(    #29
        0xC,
        (
            "可恶…\x01",
            "我也是……我也是啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_FFF():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_FFF)
    OP_8C(0xA, 90, 400)

    def lambda_1021():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1021)
    OP_8C(0xC, 90, 400)

    def lambda_1043():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1043)
    Sleep(1000)
    SetChrPos(0xD, 9100, 0, 1600, 268)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 8)
    SetChrSubChip(0xD, 1)

    def lambda_1088():
        OP_6D(9700, 0, 1630, 4000)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1088)

    def lambda_10A0():
        OP_67(0, 8000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10A0)

    def lambda_10B8():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_10B8)
    WaitChrThread(0xD, 0x0)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xD, 0x2)
    Sleep(500)

    ChrTalk(    #30
        0xD,
        (
            "#1068F#5P唉～……\x01",
            "真是折寿……\x02\x03",

            "#1067F嘿，就算在心中祈祷也要\x01",
            "拼命感谢女神啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xD, 0x1, 0x9, 0x5DC)
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 7)
    SetChrSubChip(0xD, 0)

    def lambda_1151():
        OP_6D(10100, 0, 2440, 3500)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1151)

    def lambda_1169():
        OP_6C(225000, 3500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1169)
    OP_8C(0xD, 0, 400)
    SetChrFlags(0xD, 0x4)
    OP_8E(0xD, 0x23FA, 0x0, 0x9C4, 0x3E8, 0x0)
    OP_8E(0xD, 0x297C, 0x0, 0xB54, 0x3E8, 0x0)
    WaitChrThread(0xD, 0x0)
    WaitChrThread(0xD, 0x2)

    ChrTalk(    #31
        0xD,
        (
            "#1063F#5P……不过…\x01",
            "真都是些怪物啊。\x02\x03",

            "#1065F那些就是结社的『执行者』吗……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_AD(0x2400A5, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_A2(0x1400)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_2C0 end

    def Function_3_125D(): pass

    label("Function_3_125D")

    OP_8C(0x9, 180, 400)
    OP_8E(0x9, 0x5B04, 0x1E78, 0xFFFFF722, 0x1770, 0x0)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 1)
    OP_96(0x9, 0x5BAE, 0x2260, 0xFFFFF0B0, 0x3E8, 0x1770)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)
    SetChrSubChip(0x9, 2)

    def lambda_12B1():
        OP_96(0x9, 0x5A14, 0x1F40, 0xFFFFCD38, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12B1)
    Sleep(200)
    OP_22(0x99, 0x0, 0x64)

    def lambda_12D9():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_12D9)
    Return()

    # Function_3_125D end

    def Function_4_12E6(): pass

    label("Function_4_12E6")

    OP_8E(0x8, 0x5B04, 0x1E78, 0xFFFFF722, 0x1770, 0x0)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 0)
    OP_96(0x8, 0x5BAE, 0x2260, 0xFFFFF0B0, 0x3E8, 0x1770)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_132E():
        OP_96(0x8, 0x5A14, 0x1F40, 0xFFFFCD38, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_132E)
    OP_43(0x8, 0x3, 0x0, 0x5)
    Sleep(200)
    OP_22(0x99, 0x0, 0x64)

    def lambda_135D():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_135D)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    Return()

    # Function_4_12E6 end

    def Function_5_1374(): pass

    label("Function_5_1374")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1389")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_5_1374")

    label("loc_1389")

    Return()

    # Function_5_1374 end

    def Function_6_138A(): pass

    label("Function_6_138A")

    SetPlaceName(0x69)
    Return()

    # Function_6_138A end

    def Function_7_138E(): pass

    label("Function_7_138E")

    SetPlaceName(0x52)
    Return()

    # Function_7_138E end

    SaveToFile()

Try(main)
