from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5413   ._SN',
        MapName             = 'Other',
        Location            = 'C5413.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '怀斯曼教授',                           # 9
        '剑帝莱维',                             # 10
        '怪盗布卢布兰',                         # 11
        '幻惑之铃露茜奥拉',                     # 12
        '瘦狼瓦鲁特',                           # 13
        '歼灭天使玲',                           # 14
        '小丑肯帕雷拉',                         # 15
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
        'ED6_DT27/CH03550 ._CH',             # 00
        'ED6_DT07/CH02040 ._CH',             # 01
        'ED6_DT27/CH03530 ._CH',             # 02
        'ED6_DT27/CH03520 ._CH',             # 03
        'ED6_DT27/CH03500 ._CH',             # 04
        'ED6_DT27/CH03510 ._CH',             # 05
        'ED6_DT27/CH03600 ._CH',             # 06
        'ED6_DT26/CH20280 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03550P._CP',             # 00
        'ED6_DT07/CH02040P._CP',             # 01
        'ED6_DT27/CH03530P._CP',             # 02
        'ED6_DT27/CH03520P._CP',             # 03
        'ED6_DT27/CH03500P._CP',             # 04
        'ED6_DT27/CH03510P._CP',             # 05
        'ED6_DT27/CH03600P._CP',             # 06
        'ED6_DT26/CH20280P._CP',             # 07
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1CA",          # 00, 0
        "Function_1_1E2",          # 01, 1
        "Function_2_21A",          # 02, 2
        "Function_3_7C7",          # 03, 3
    )


    def Function_0_1CA(): pass

    label("Function_0_1CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_1E1")
    OP_A3(0x10F4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_1E1")

    Return()

    # Function_0_1CA end

    def Function_1_1E2(): pass

    label("Function_1_1E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_200")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_219")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_219")

    Return()

    # Function_1_1E2 end

    def Function_2_21A(): pass

    label("Function_2_21A")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(780, 0, -76180, 0)
    OP_67(0, 14130, -10000, 0)
    OP_6B(4800, 0)
    OP_6C(48000, 0)
    OP_6E(834, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x131, 0x1, 0x46)
    SetChrPos(0x8, 7490, 0, -52610, 90)
    SetChrPos(0x9, 5870, 0, -52030, 90)
    SetChrPos(0xD, 5130, 0, -53010, 90)
    SetChrPos(0xA, 5550, 0, -54200, 90)
    SetChrPos(0xC, 4720, 0, -55500, 90)
    SetChrPos(0xB, 4860, 0, -51240, 90)
    SetChrPos(0xE, 7500, 0, -54150, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0xC, 7)
    SetChrSubChip(0xC, 0)
    OP_C4(0x0, 0x2)
    OP_7E(0xBFBE, 0xE61A, 0xFDF8, 0x6E, 0x320)
    LoadEffect(0x1, "map\\mp092_00.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 60000, 22000, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_38F():
        OP_6D(30, 150, -38510, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_38F)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    PlayEffect(0x1, 0xFF, 0xFF, 50000, 3000, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(8000, 0, -52570, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(65000, 0)
    OP_6E(322, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0xA,
        "#233F#6P哦哦……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xB,
        "#243F#6P这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xC,
        "#252F#6P哈哈……这是真的吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xD,
        "#261F#6P呵呵……真不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xE,
        (
            "#851F#6P哈哈！\x01",
            "这个确实了不起！\x02\x03",

            "#854F难怪教授这么重视！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#1154F#6P呵呵……\x01",
            "你们喜欢就好。\x02\x03",

            "#1151F『辉之环』长久以来\x01",
            "被封印于异次元……\x02\x03",

            "但是只要有了作为终端的『福音』，\x01",
            "同样也能够影响到我们的次元。\x02\x03",

            "问题是复制品的精确度\x01",
            "能提升到什么样的程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "#125F#5P然后，在经过了多次实验后，\x01",
            "真正的『福音』终于完成了……\x02\x03",

            "『环』透过它们已经\x01",
            "拔出了连接自己的『桩』……\x02\x03",

            "而现在从昏暗的深渊中苏醒了。\x02\x03",

            "#122F──这就是第三阶段的真相吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "#1155F#6P呵呵呵……没错。\x02",
    )

    CloseMessageWindow()

    def lambda_672():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_672)
    OP_43(0x8, 0x3, 0x0, 0x3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("怀斯曼教授")

    AnonymousTalk(    #8
        (
            "\x07\x00多亏了诸位的奔波，\x01",
            "第三阶段顺利完成！\x02\x03",

            "接下来『福音计划』\x01",
            "将进入最终阶段──\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AD(0x2400B4, 0x0, 0x0, 0x64)
    WaitChrThread(0x8, 0x3)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1E30)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x129), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_6D(-162160, 0, -33060, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存进度】\x01",        # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_785")
    ShowSaveMenu()

    label("loc_785")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0x7D0)
    OP_21()
    OP_C4(0x1, 0x10)
    OP_A3(0x1E30)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10FD)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_21A end

    def Function_3_7C7(): pass

    label("Function_3_7C7")

    OP_24(0x1C3, 0x5A)
    OP_24(0x131, 0x41)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    OP_24(0x131, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    OP_24(0x131, 0x37)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    OP_24(0x131, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    OP_24(0x131, 0x2D)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    OP_24(0x131, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    OP_24(0x131, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    OP_24(0x131, 0x14)
    Sleep(200)
    OP_23(0x1C3)
    OP_23(0x131)
    Return()

    # Function_3_7C7 end

    SaveToFile()

Try(main)
