from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4203   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4203.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '士兵丹',                               # 9
        '士兵阿尔兹',                           # 10
        '奈尔',                                 # 11
        '朵洛希',                               # 12
        '目标用照相机',                         # 13
        '王都格兰赛尔·北街区',                 # 14
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT06/CH20122 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT06/CH20122P._CP',             # 03
    )

    DeclNpc(
        X                   = -790,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Y                   = -22550,
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


    ScpFunction(
        "Function_0_18A",          # 00, 0
        "Function_1_1B3",          # 01, 1
        "Function_2_1C6",          # 02, 2
        "Function_3_1CD",          # 03, 3
        "Function_4_1D4",          # 04, 4
    )


    def Function_0_18A(): pass

    label("Function_0_18A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1B2")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_1B2")

    Return()

    # Function_0_18A end

    def Function_1_1B3(): pass

    label("Function_1_1B3")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x230060)
    Return()

    # Function_1_1B3 end

    def Function_2_1C6(): pass

    label("Function_2_1C6")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_2_1C6 end

    def Function_3_1CD(): pass

    label("Function_3_1CD")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_3_1CD end

    def Function_4_1D4(): pass

    label("Function_4_1D4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0 op#A
        "\x07\x00\x18#20W#5S#20A号外！！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x00#20W       #4S利贝尔通讯　特别号#3S\x01",
            " \x01",
            "『浮游都市崩坏！　王国危机消散！』#2S\x01",
            " \x01",
            "  成功阻止空前阴谋！　多亏了年轻游击士！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_B8(0x326, 0xFF)
    Sleep(2000)
    OP_22(0x1CC, 0x1, 0x64)
    OP_1D(0x11)
    OP_6D(3000, 0, -9940, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x12, 3000, 0, -20900, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_361():
        OP_8E(0xFE, 0xBB8, 0x0, 0x2EE0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_361)
    Sleep(1000)

    def lambda_381():
        OP_6D(3000, 0, 12200, 6300)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_381)

    def lambda_399():
        OP_67(0, 5500, -10000, 6300)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_399)

    def lambda_3B1():
        OP_6C(0, 6300)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3B1)

    def lambda_3C1():
        OP_6B(3300, 6300)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_3C1)
    Sleep(1000)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    def lambda_420():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_420)

    ChrTalk(    #2
        0x12,
        "#145F#5P#40W呼啊、呼啊、呼啊…………\x02",
    )

    CloseMessageWindow()

    def lambda_46B():
        OP_6D(4200, 0, 12200, 1000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_46B)

    def lambda_483():
        OP_67(0, 6020, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_483)

    def lambda_49B():
        OP_6C(50000, 1000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_49B)

    def lambda_4AB():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_4AB)
    OP_8C(0x12, 180, 300)
    Sleep(300)

    ChrTalk(    #3
        0x12,
        (
            "#144F#5P#3S朵洛希，你在干什么！#2S\x02\x03",

            "#3S不管你了！！#2S\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrPos(0x13, 3000, 0, 1100, 0)

    def lambda_53D():
        OP_8E(0xFE, 0xBB8, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_53D)
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #4
        0x13,
        (
            "#152F#3P等、等等我～啊……\x01",
            "奈尔前～辈……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_595():
        OP_8E(0xFE, 0xBB8, 0x0, 0x2008, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_595)
    WaitChrThread(0x13, 0x1)
    Sleep(300)

    def lambda_5BA():
        OP_8E(0xFE, 0xBB8, 0x0, 0x2904, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5BA)
    WaitChrThread(0x13, 0x1)
    Sleep(300)

    ChrTalk(    #5
        0x12,
        (
            "#144F#5P不要磨磨蹭蹭的了！\x01",
            "庆祝会马上就要开始了！\x02\x03",

            "#142F这可是艾莉茜雅女王\x01",
            "为了庆贺『异变』的平息\x01",
            "而主办的特别宴会啊！\x02\x03",

            "这样的大事件，\x01",
            "是绝对不能迟到的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x13,
        (
            "#156F#12P#40W可、可是我\x01",
            "已经饿得肚子咕咕叫了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x160, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0x13, 3)
    SetChrSubChip(0x13, 0)
    SetChrFlags(0x13, 0x20)
    Sleep(1200)

    def lambda_6FD():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6FD)

    ChrTalk(    #7
        0x13,
        "#152F#12P#40W一步也走不动了……\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(300)

    ChrTalk(    #8
        0x12,
        (
            "#145F#5P难道说你…………\x02\x03",

            "#142F为了把肚子留给宴会，\x01",
            "白天连一点饭都没吃吗……\x01",
            "只有这种可能了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x13,
        (
            "#154F#12P不只是今天白天，\x01",
            "从昨天开始就没有吃饭了。\x02\x03",

            "#152F已经绝食超过３０小时了，\x01",
            "呜，眼前好多星星啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0x12,
        (
            "#144F#5P#3S朵洛希，你这家伙\x01",
            "到底在想些什么啊………！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #11
        0x13,
        (
            "#152F#12P奈尔前辈，\x01",
            "背背我吧～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x12,
        "#145F#5P唉，你知不知道！！\x02",
    )

    CloseMessageWindow()

    def lambda_913():
        OP_8E(0xFE, 0xBB8, 0x0, 0x2BC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_913)
    WaitChrThread(0x12, 0x1)
    Sleep(200)
    OP_8C(0x12, 0, 400)
    Sleep(500)

    ChrTalk(    #13
        0x12,
        (
            "#144F#5P难得今天整个王国\x01",
            "有名的人士齐聚一堂。\x01",
            "给我坚持住！！\x02\x03",

            "#141F首先要给女王陛下\x01",
            "和科洛蒂娅殿下\x01",
            "拍一张宝贵的照片……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9CF():
        OP_8E(0xFE, 0xBB8, 0x0, 0x32C8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9CF)

    def lambda_9EA():
        OP_8E(0xFE, 0xBB8, 0x0, 0x300C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9EA)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #14
        0x13,
        "#152F#12P#40W呜呜呜呜…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x13,
        (
            "#153F#12P咦、咦～？\x02\x03",

            "#151F也许会很有意思呢～㈱\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A92():
        OP_8E(0xFE, 0xBB8, 0x0, 0x7DC8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A92)

    def lambda_AAD():
        OP_8E(0xFE, 0xBB8, 0x0, 0x57E4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_AAD)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x13, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4206   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_1D4 end

    SaveToFile()

Try(main)
