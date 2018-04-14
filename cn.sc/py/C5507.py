from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5507   ._SN',
        MapName             = 'Other',
        Location            = 'C5507.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        '女猎兵',                               # 9
        '发烟筒用目标角色',                     # 10
        '目标用照相机',                         # 11
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
        'ED6_DT07/CH00261 ._CH',             # 00
        'ED6_DT27/CH04000 ._CH',             # 01
        'ED6_DT27/CH04001 ._CH',             # 02
        'ED6_DT07/CH00420 ._CH',             # 03
        'ED6_DT07/CH00421 ._CH',             # 04
        'ED6_DT07/CH00264 ._CH',             # 05
        'ED6_DT27/CH03005 ._CH',             # 06
        'ED6_DT27/CH03095 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT27/CH04640 ._CH',             # 09
        'ED6_DT27/CH04641 ._CH',             # 0A
        'ED6_DT27/CH04642 ._CH',             # 0B
        'ED6_DT27/CH04644 ._CH',             # 0C
        'ED6_DT26/CH20265 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH00261P._CP',             # 00
        'ED6_DT27/CH04000P._CP',             # 01
        'ED6_DT27/CH04001P._CP',             # 02
        'ED6_DT07/CH00420P._CP',             # 03
        'ED6_DT07/CH00421P._CP',             # 04
        'ED6_DT07/CH00264P._CP',             # 05
        'ED6_DT27/CH03005P._CP',             # 06
        'ED6_DT27/CH03095P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT27/CH04640P._CP',             # 09
        'ED6_DT27/CH04641P._CP',             # 0A
        'ED6_DT27/CH04642P._CP',             # 0B
        'ED6_DT27/CH04644P._CP',             # 0C
        'ED6_DT26/CH20265P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 1900552,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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


    DeclEvent(
        X                   = -2500,
        Y                   = -100,
        Z                   = 28500,
        Range               = 8500,
        Unknown_10          = 0x76C,
        Unknown_14          = 0x7724,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -3520,
        Y                   = 0,
        Z                   = -11140,
        Range               = 8109,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE17E,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    DeclActor(
        TriggerX            = 5300,
        TriggerZ            = 0,
        TriggerY            = 9990,
        TriggerRange        = 800,
        ActorX              = 5300,
        ActorZ              = 1000,
        ActorY              = 9990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_201",          # 01, 1
        "Function_2_202",          # 02, 2
        "Function_3_212",          # 03, 3
        "Function_4_F50",          # 04, 4
        "Function_5_1002",         # 05, 5
        "Function_6_1229",         # 06, 6
        "Function_7_1919",         # 07, 7
        "Function_8_1E12",         # 08, 8
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1EC")
    OP_A3(0x10F0)
    Event(0, 5)

    label("loc_1EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_200")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200")

    label("loc_200")

    Return()

    # Function_0_1DE end

    def Function_1_201(): pass

    label("Function_1_201")

    Return()

    # Function_1_201 end

    def Function_2_202(): pass

    label("Function_2_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211")
    Call(0, 3)
    Jump("loc_211")

    label("loc_211")

    Return()

    # Function_2_202 end

    def Function_3_212(): pass

    label("Function_3_212")

    EventBegin(0x0)
    OP_A2(0x1011)
    Fade(1000)
    OP_6D(2510, 0, -9490, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4140, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2310, 0, -8920, 339)
    SetChrPos(0x10A, 3870, 0, -9500, 1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇回收６个装备】\x01",          # 0
            "【◇装备１个也不回收】\x01",      # 1
            "【◇什么也没有变更】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312")
    OP_A2(0x1120)
    OP_A2(0x1121)
    OP_A2(0x1122)
    OP_A2(0x1130)
    OP_A2(0x1132)
    OP_A2(0x1133)
    Jump("loc_331")

    label("loc_312")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_331")
    OP_A3(0x1120)
    OP_A3(0x1121)
    OP_A3(0x1122)
    OP_A3(0x1130)
    OP_A3(0x1132)
    OP_A3(0x1133)

    label("loc_331")

    FadeToBright(300, 0)

    label("loc_33A")


    def lambda_340():
        OP_8E(0x101, 0x514, 0x0, 0xB0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_340)
    Sleep(100)

    def lambda_360():
        OP_8E(0x10A, 0x9C4, 0x0, 0xB0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_360)

    def lambda_37B():
        OP_6D(2090, 0, 22590, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37B)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)

    def lambda_39D():
        OP_6D(2150, 0, 2820, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_39D)

    def lambda_3B5():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3B5)

    def lambda_3CD():
        OP_6B(3220, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3CD)
    WaitChrThread(0x10A, 0x0)
    WaitChrThread(0x10A, 0x1)
    WaitChrThread(0x10A, 0x2)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10A, 500)
    Sleep(100)
    TurnDirection(0x10A, 0x101, 500)

    ChrTalk(    #0
        0x101,
        (
            "#1018F#6P亚妮拉丝！\x01",
            "那里好像是出口！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10A,
        (
            "#2P#819F呼～……\x01",
            "总算能松一口气了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 70, 0, 18120, 180)
    TurnDirection(0x8, 0x101, 1000)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 3)

    NpcTalk(    #2
        0x8,
        "女人的声音",
        "哎呀哎呀……\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    NpcTalk(    #3
        0x8,
        "女人的声音",
        (
            "稍微转移一下视线\x01",
            "就趁机逃跑的坏孩子们。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)

    def lambda_510():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_510)

    def lambda_51E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_51E)
    Sleep(300)
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 440, 1000, 10570, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1180, 1000, 8170, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 820, 1000, 5160, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_5F8():
        OP_96(0xFE, 0x0, 0x0, 0x5DC, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F8)
    Sleep(50)

    def lambda_61B():
        OP_96(0xFE, 0xA8C, 0x0, 0x53C, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_61B)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1740, 1000, 1930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 6)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 7)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1300, 1000, -600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1680, 1000, -2630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 2000, 1000, -4630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    ChrTalk(    #4
        0x101,
        "#6P#1021F#1K呀……！\x02",
    )


    ChrTalk(    #5
        0x10A,
        "#5P#1312F#1K呜……！\x02",
    )

    Sleep(1000)
    OP_56(0x1)
    OP_59()
    OP_1D(0x56)
    Sleep(500)
    OP_69(0x8, 0x7D0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 10)

    def lambda_7AF():
        OP_8E(0xFE, 0x82, 0x0, 0x2044, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7AF)

    def lambda_7CA():
        OP_6D(900, 0, 4900, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7CA)
    WaitChrThread(0x8, 0x1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)
    WaitChrThread(0x8, 0x2)

    NpcTalk(    #6
        0x8,
        "女猎兵",
        (
            "#5P呵呵……\x01",
            "欢迎来到我的猎场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1004F#6P女、女人！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        (
            "#815F#2P艾丝蒂尔，小心！\x02\x03",

            "这个人……相当强哦！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #9
        0x8,
        "女猎兵",
        (
            "#5P哎呀……\x01",
            "观察力很有一套啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #10
        0x8,
        "女猎兵",
        (
            "#5P而且，吸了那种气体后\x01",
            "居然这么快就醒来，真令人吃惊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x8,
        "女猎兵",
        (
            "#5P不愧是游击士。\x01",
            "看来不只是体力过人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1005F#6P你、你们这些人！\x01",
            "到底有什么目的！？\x02\x03",

            "为什么要袭击训练场！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x8,
        "女猎兵",
        (
            "#5P呵呵……\x01",
            "我没有义务回答你。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #14
        0x8,
        "女猎兵",
        "#5P你们的选择只有两个。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #15
        0x8,
        "女猎兵",
        (
            "#5P乖乖地投降，\x01",
            "或是就这样成为我的猎物。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 0)), scpexpr(EXPR_END)), "loc_9F6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 1)), scpexpr(EXPR_END)), "loc_A07")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 2)), scpexpr(EXPR_END)), "loc_A18")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 0)), scpexpr(EXPR_END)), "loc_A29")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 2)), scpexpr(EXPR_END)), "loc_A3A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 3)), scpexpr(EXPR_END)), "loc_A4B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A9D")

    ChrTalk(    #16
        0x101,
        (
            "#1002F#6P呜……\x02\x03",

            "（用回收来的装备\x01",
            "  好歹可以应战吧……！？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE1")

    label("loc_A9D")


    ChrTalk(    #17
        0x101,
        (
            "#1003F#6P呜……\x02\x03",

            "（要跟这个人战斗，\x01",
            "  装备实在太贫乏了……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE1")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【暂且撤退】\x01",        # 0
            "【就这样挑战】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E96")

    ChrTalk(    #18
        0x101,
        "#1005F#6P……亚妮拉丝！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        "#815F#2P嗯……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 65535)

    def lambda_B8D():
        OP_8C(0xFE, 180, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B8D)
    Sleep(200)

    def lambda_BA0():
        OP_8C(0xFE, 180, 800)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_BA0)
    WaitChrThread(0x101, 0x1)

    def lambda_BB3():
        OP_8E(0xFE, 0x7D0, 0x0, 0xFFFFC0CC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BB3)
    WaitChrThread(0x10A, 0x1)

    def lambda_BD3():
        OP_8E(0xFE, 0x7D0, 0x0, 0xFFFFC0CC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_BD3)

    def lambda_BEE():
        OP_6D(2970, 0, -7130, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BEE)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 3)
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    LoadEffect(0x1, "monster\\\\msc0310.eff")
    Sleep(200)
    OP_43(0x8, 0x3, 0x0, 0x4)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1300, 1000, -600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1280, 1000, -2630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 900, 1000, -3630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1300, 1000, -4630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1000, 1000, -5760, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1300, 1000, -6630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1960, 1000, -7810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)

    def lambda_E21():
        OP_69(0x8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_E21)
    WaitChrThread(0x10A, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)

    NpcTalk(    #20
        0x8,
        "女猎兵",
        (
            "也罢。\x01",
            "反正出口只有这里……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #21
        0x8,
        "女猎兵",
        "就让我慢慢狩猎吧。\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5512   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_F4B")

    label("loc_E96")


    ChrTalk(    #22
        0x101,
        "#1005F#6P亚妮拉丝！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        "#815F#2P嗯！\x02",
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 1)
    Sleep(100)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 3)
    Sleep(500)

    NpcTalk(    #24
        0x8,
        "女猎兵",
        (
            "#5P呵呵……\x01",
            "好吧，小猫咪们。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #25
        0x8,
        "女猎兵",
        "#5P就让我尽情狩猎吧！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)

    label("loc_F4B")

    Call(0, 6)
    Return()

    # Function_3_212 end

    def Function_4_F50(): pass

    label("Function_4_F50")

    PlayEffect(0x1, 0x0, 0xFF, 210, 800, 7650, 148, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0x0, 0xFF, 210, 800, 7650, 148, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0x0, 0xFF, 210, 800, 7650, 148, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_82(0x0, 0x2)
    Return()

    # Function_4_F50 end

    def Function_5_1002(): pass

    label("Function_5_1002")

    EventBegin(0x0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 0, 0, 10770, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x10A, 3)
    SetChrPos(0x101, 1370, 0, -36430, 0)
    SetChrPos(0x10A, 3490, 0, -37430, 0)
    FadeToBright(1000, 0)

    def lambda_1081():
        OP_8E(0x101, 0xFFFFFA42, 0x0, 0x1D4C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1081)

    def lambda_109C():
        OP_8E(0x10A, 0x5BE, 0x0, 0x1D4C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_109C)
    Sleep(1000)
    OP_0D()
    Fade(500)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    SetChrPos(0x101, -470, 0, -3500, 0)
    SetChrPos(0x10A, 1320, 0, -4500, 0)

    def lambda_10EC():
        OP_8E(0x101, 0xFFFFFE2A, 0x0, 0x11EE, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10EC)

    def lambda_1107():
        OP_8E(0x10A, 0x528, 0x0, 0x11A8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1107)
    OP_6D(390, 0, 7240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #26
        0x101,
        "#1005F#6P让你久等了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10A,
        (
            "#815F#2P我们这次一定要\x01",
            "通过那里！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #28
        0x8,
        "女猎兵",
        (
            "#5P呵呵……\x01",
            "好吧，小猫咪们。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #29
        0x8,
        "女猎兵",
        "#5P就让我尽情狩猎吧！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    Call(0, 6)
    Return()

    # Function_5_1002 end

    def Function_6_1229(): pass

    label("Function_6_1229")

    ClearMapFlags(0x1)
    OP_6D(730, 0, 7340, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 0, 0, 10770, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 12)
    SetChrSubChip(0x8, 3)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x10A, 3)
    SetChrPos(0x101, -580, 0, 5380, 6)
    SetChrPos(0x10A, 2060, 0, 5380, 343)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #30
        0x8,
        "女猎兵",
        (
            "#5P唔……\x01",
            "有点小看你们了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1005F#6P呼呼……\x01",
            "可别小看游击士哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10A,
        (
            "#812F#2P被我们两个小丫头羞辱，\x01",
            "你的好运也到此为止了！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #33
        0x8,
        "女猎兵",
        (
            "#5P呵呵，好勇敢的\x01",
            "小猫咪们……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0x8, 13)
    SetChrFlags(0x8, 0x2)
    LoadEffect(0x0, "map\\\\mp004_00.eff")
    SetChrPos(0x9, 70, 0, 6150, 28)

    def lambda_13B6():
        OP_99(0xFE, 0x0, 0x9, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13B6)
    Sleep(800)
    PlayEffect(0x0, 0xFF, 0x8, 250, 900, -500, 0, 0, 0, 1000, 1000, 1000, 0x9, 0, 0, 0, 0)

    ChrTalk(    #34 op#A op#5
        0x101,
        "#6P#1020F#10A……又来了！\x05\x02",
    )

    Sleep(1200)
    OP_22(0x7F, 0x0, 0x64)

    ChrTalk(    #35 op#A op#5
        0x10A,
        "#815F#2P#16A艾丝蒂尔，摒住呼吸！\x05\x02",
    )

    Sleep(1700)
    OP_8C(0x101, 45, 0)
    OP_8C(0x101, 315, 0)

    def lambda_1462():
        OP_96(0xFE, 0xFFFFF4D4, 0x0, 0x13A6, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1462)

    def lambda_1480():
        OP_96(0xFE, 0x8FC, 0x0, 0x1504, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1480)
    Sleep(100)
    TurnDirection(0x101, 0x8, 1000)
    TurnDirection(0x10A, 0x8, 1000)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10A, 0x1)
    Sleep(300)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    Sleep(2000)

    NpcTalk(    #36
        0x8,
        "女人的声音",
        "方术使已经被抓住。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #37
        0x8,
        "女人的声音",
        "小猫咪们没有同伴了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0x8,
        "女人的声音",
        "赶快死心投降吧……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 10)

    def lambda_1545():
        OP_8E(0xFE, 0xFFFFFFCE, 0x0, 0x556E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1545)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_44(0x8, 0x1)
    OP_20(0x7D0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    SetChrFlags(0x8, 0x80)
    OP_8C(0x101, 0, 0)
    OP_8C(0x101, 0, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)

    ChrTalk(    #39
        0x101,
        "#1007F#6P逃掉了吗……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    Sleep(100)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 65535)
    Sleep(200)
    TurnDirection(0x101, 0x10A, 500)

    def lambda_15E1():
        OP_8E(0xFE, 0xFFFFFD44, 0x0, 0x145A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15E1)

    def lambda_15FC():
        OP_6D(-100, 0, 5180, 1200)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_15FC)

    def lambda_1614():
        TurnDirection(0x10A, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1614)
    WaitChrThread(0x10A, 0x1)

    def lambda_1627():
        OP_8E(0xFE, 0x258, 0x0, 0x140A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1627)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10A, 0x1)
    Sleep(500)

    ChrTalk(    #40
        0x101,
        (
            "#1002F#6P亚妮拉丝。\x01",
            "我们还是别追击比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10A,
        (
            "#812F是啊……\x01",
            "而且也有被伏击的危险。\x02\x03",

            "#813F对了，艾丝蒂尔。\x02\x03",

            "刚才那人说\x01",
            "『方术使被抓住』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1026F#6P啊……\x02\x03",

            "#1003F嗯……\x01",
            "我想指的应该是克鲁茨前辈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10A,
        (
            "#813F是吗……\x02\x03",

            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1018F#6P没、没问题的啦！\x02\x03",

            "即使真的被抓住，\x01",
            "克鲁茨前辈也一定会没事的！\x02\x03",

            "#1006F而且……这种时候才\x01",
            "更应该活用训练中学到的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10A,
        (
            "#814F啊……\x02\x03",

            "非常时期的行动——确保安全、\x01",
            "还有反恐技术……\x02\x03",

            "#816F嗯……确实如此！\x02\x03",

            "我们必须活用所学到的东西\x01",
            "救出克鲁茨前辈！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1001F#6P嗯嗯，就是这种气势！\x02\x03",

            "#1006F对了，亚妮拉丝。\x01",
            "我们要不要先回宿舍一趟？\x02\x03",

            "我想最好去确认一下\x01",
            "是否已经被敌人占领了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10A,
        (
            "#810F嗯，说得也是。\x02\x03",

            "那么就出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1012)
    OP_28(0x7F, 0x1, 0x2000)
    OP_28(0x7F, 0x1, 0x4000)
    OP_28(0x7F, 0x1, 0x8000)
    OP_28(0x80, 0x4, 0x2)
    OP_28(0x80, 0x4, 0x8)
    OP_1D(0x15)
    EventEnd(0x0)
    Return()

    # Function_6_1229 end

    def Function_7_1919(): pass

    label("Function_7_1919")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_1937")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1948")

    label("loc_1937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_END)), "loc_1948")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1948")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS137._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD6")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_19E4"),
        (1, "loc_1A10"),
        (2, "loc_1A4D"),
        (SWITCH_DEFAULT, "loc_1A9F"),
    )


    label("loc_19E4")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
        )
    )

    Jump("loc_1A9F")

    label("loc_1A10")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
            "【圣科洛瓦森林】\x01",      # 2
        )
    )

    Jump("loc_1A9F")

    label("loc_1A4D")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",            # 0
            "【巴斯塔尔水道】\x01",          # 1
            "【圣科洛瓦森林】\x01",          # 2
            "【格林姆瑟尔小要塞】\x01",      # 3
        )
    )

    Jump("loc_1A9F")

    label("loc_1A9F")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AC9"),
        (1, "loc_1B49"),
        (2, "loc_1BCB"),
        (3, "loc_1C4D"),
        (SWITCH_DEFAULT, "loc_1CD3"),
    )


    label("loc_1AC9")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #48
        "\x07\x05要移动至【训练场宿舍】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B36"),
        (1, "loc_1B43"),
        (SWITCH_DEFAULT, "loc_1B46"),
    )


    label("loc_1B36")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B46")

    label("loc_1B43")

    Jump("loc_1B46")

    label("loc_1B46")

    Jump("loc_1CD3")

    label("loc_1B49")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #49
        "\x07\x05要移动至【巴斯塔尔水道】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BB8"),
        (1, "loc_1BC5"),
        (SWITCH_DEFAULT, "loc_1BC8"),
    )


    label("loc_1BB8")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC8")

    label("loc_1BC5")

    Jump("loc_1BC8")

    label("loc_1BC8")

    Jump("loc_1CD3")

    label("loc_1BCB")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #50
        "\x07\x05要移动至【圣科洛瓦森林】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C3A"),
        (1, "loc_1C47"),
        (SWITCH_DEFAULT, "loc_1C4A"),
    )


    label("loc_1C3A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C4A")

    label("loc_1C47")

    Jump("loc_1C4A")

    label("loc_1C4A")

    Jump("loc_1CD3")

    label("loc_1C4D")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #51
        "\x07\x05要移动至【格林姆瑟尔小要塞】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CC0"),
        (1, "loc_1CCD"),
        (SWITCH_DEFAULT, "loc_1CD0"),
    )


    label("loc_1CC0")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CD0")

    label("loc_1CCD")

    Jump("loc_1CD0")

    label("loc_1CD0")

    Jump("loc_1CD3")

    label("loc_1CD3")

    Jump("loc_19B9")

    label("loc_1CD6")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1CEF"),
        (1, "loc_1D23"),
        (2, "loc_1D57"),
        (3, "loc_1D8B"),
        (SWITCH_DEFAULT, "loc_1DBF"),
    )


    label("loc_1CEF")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_1DBF")

    label("loc_1D23")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_1DBF")

    label("loc_1D57")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_1DBF")

    label("loc_1D8B")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_1DBF")

    label("loc_1DBF")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1DE1"),
        (1, "loc_1DED"),
        (2, "loc_1DF9"),
        (3, "loc_1E05"),
        (SWITCH_DEFAULT, "loc_1E11"),
    )


    label("loc_1DE1")

    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1E11")

    label("loc_1DED")

    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1E11")

    label("loc_1DF9")

    NewScene("ED6_DT21/C5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_1E11")

    label("loc_1E05")

    NewScene("ED6_DT21/C5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_1E11")

    label("loc_1E11")

    Return()

    # Function_7_1919 end

    def Function_8_1E12(): pass

    label("Function_8_1E12")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #52
        "\x07\x05【圣科洛瓦森林】\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #53
        (
            "\x07\x05除了巡逻训练之外，\x01",
            "也推荐进行生存训练等等。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1E12 end

    SaveToFile()

Try(main)
