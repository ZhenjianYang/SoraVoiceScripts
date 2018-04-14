from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4310   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '希德中校',                             # 9
        '贝尔克副队长',                         # 10
        '王国军士兵',                           # 11
        '王国军士兵',                           # 12
        '王国军士兵',                           # 13
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
        'ED6_DT27/CH03590 ._CH',             # 00
        'ED6_DT07/CH01600 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT27/CH03590P._CP',             # 00
        'ED6_DT07/CH01600P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_162",          # 00, 0
        "Function_1_176",          # 01, 1
        "Function_2_177",          # 02, 2
    )


    def Function_0_162(): pass

    label("Function_0_162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_175")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_175")

    Return()

    # Function_0_162 end

    def Function_1_176(): pass

    label("Function_1_176")

    Return()

    # Function_1_176 end

    def Function_2_177(): pass

    label("Function_2_177")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, -80, 250, 68550, 180)
    SetChrPos(0x9, -1060, 250, 69080, 180)
    SetChrPos(0xA, 700, 0, 66610, 0)
    SetChrPos(0xB, -700, 0, 66610, 0)
    OP_6D(-50, 250, 68390, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0xA,
        (
            "#2P现在在周游道的西北地区\x01",
            "第１和第２小队已经展开。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        "#2P即将完成包围。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xB,
        (
            "#6P在东南地区有数名特务兵\x01",
            "正在往罗马尔池的反方向更深处逃窜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xB,
        (
            "#6P第３和第４小队\x01",
            "正在继续追击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#703F辛苦了。\x02\x03",

            "#700F维持现状，努力\x01",
            "盯紧那两伙儿人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        "#2P#1K是！\x02",
    )


    ChrTalk(    #6
        0xB,
        "#6P#1K是！\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_334():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_334)
    Sleep(100)

    def lambda_347():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_347)
    Sleep(500)

    def lambda_35A():
        OP_6D(-50, 250, 65390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35A)

    def lambda_372():
        OP_8E(0xFE, 0x2BC, 0x0, 0xCDD2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_372)
    Sleep(50)

    def lambda_392():
        OP_8E(0xFE, 0xFFFFFD44, 0x0, 0xCDD2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_392)
    Sleep(3000)
    WaitChrThread(0x101, 0x1)

    def lambda_3B7():
        OP_6D(-50, 250, 69390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B7)
    WaitChrThread(0x101, 0x1)

    def lambda_3D4():
        OP_8C(0x9, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3D4)
    Sleep(400)

    ChrTalk(    #7
        0x9,
        (
            "#8P不过真是无法理解……\x01",
            "他们到底在想什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        "#8P难道是在声东击西？\x02",
    )

    CloseMessageWindow()

    def lambda_432():
        OP_8C(0x8, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_432)
    Sleep(400)

    ChrTalk(    #9
        0x8,
        (
            "#703F#2P格兰赛尔配备有\x01",
            "一个中队的兵力。\x02\x03",

            "他们就算在这里拖住我们\x01",
            "也不可能攻下王都。\x02\x03",

            "#702F难道说他们手里有\x01",
            "我们不知道的王牌……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        "#8P王……牌？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 0, 0, 60000, 0)

    ChrTalk(    #11
        0xC,
        "#1P报告！\x02",
    )

    CloseMessageWindow()

    def lambda_50D():
        OP_6D(-50, 250, 68390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50D)

    def lambda_525():
        OP_8C(0x9, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_525)
    Sleep(100)

    def lambda_538():
        OP_8C(0x8, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_538)
    OP_8E(0xC, 0x0, 0x0, 0x10432, 0xFA0, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #12
        0x8,
        "#700F什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xC,
        "已经和要塞司令部联络过了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xC,
        (
            "不过跟游击士协会\x01",
            "王都支部的联络……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xC,
        (
            "可能是出了什么问题，\x01",
            "对方始终没有应答。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        "#702F什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        "您怎么认为？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#700F嗯，让我想想……\x02\x03",

            "#703F……以防万一，\x01",
            "还是要下一道保险。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    Sleep(500)

    ChrTalk(    #19
        0x8,
        (
            "#700F#2P副队长，这里就交给你了。\x02\x03",

            "我去一下通讯室。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    ChrTalk(    #20
        0x9,
        "#8P明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        "#8P那么您是要联络哪边？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "#701F#2P再一次联络要塞司令部。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4150   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_177 end

    SaveToFile()

Try(main)
