from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3108   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3108.x',
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
        '卡西乌斯',                             # 9
        '警备艇',                               # 10
        '警备艇',                               # 11
        '警备艇',                               # 12
        '警备艇',                               # 13
        '希德中校',                             # 14
        '格斯塔夫维修长',                       # 15
        '菲',                                   # 16
        '维修员',                               # 17
        '维修员',                               # 18
        '维修员',                               # 19
        '维修员',                               # 20
        '工房船',                               # 21
        '工房船影',                             # 22
        '埃尔赛尤号的影子',                     # 23
        '警备艇影',                             # 24
        '警备艇影',                             # 25
        '警备艇影',                             # 26
        '警备艇影',                             # 27
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
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT27/CH03590 ._CH',             # 01
        'ED6_DT07/CH02440 ._CH',             # 02
        'ED6_DT07/CH01550 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT27/CH03590P._CP',             # 01
        'ED6_DT07/CH02440P._CP',             # 02
        'ED6_DT07/CH01550P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_332",          # 00, 0
        "Function_1_375",          # 01, 1
        "Function_2_376",          # 02, 2
        "Function_3_C25",          # 03, 3
        "Function_4_C6E",          # 04, 4
        "Function_5_CB7",          # 05, 5
        "Function_6_D00",          # 06, 6
        "Function_7_D49",          # 07, 7
        "Function_8_D92",          # 08, 8
        "Function_9_DDB",          # 09, 9
        "Function_10_111C",        # 0A, 10
        "Function_11_1152",        # 0B, 11
        "Function_12_140F",        # 0C, 12
        "Function_13_174E",        # 0D, 13
        "Function_14_1A06",        # 0E, 14
        "Function_15_1D4C",        # 0F, 15
    )


    def Function_0_332(): pass

    label("Function_0_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_35A")
    OP_B1("C3108_1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_374")

    label("loc_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_374")
    SetMapFlags(0x10000000)
    OP_B1("C3108_2")
    Event(0, 2)

    label("loc_374")

    Return()

    # Function_0_332 end

    def Function_1_375(): pass

    label("Function_1_375")

    Return()

    # Function_1_375 end

    def Function_2_376(): pass

    label("Function_2_376")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearMapFlags(0x10)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x40)
    SetChrPos(0x14, 570, 30000, 22920, 360)
    SetChrPos(0x15, 570, 15000, 22920, 360)
    SetChrPos(0x16, 10000, -10000, 54840, 270)
    OP_A1(0x14, 0x0)
    OP_A1(0x15, 0x1)
    OP_A1(0x16, 0x2)
    OP_6D(5630, 0, 36820, 0)
    OP_67(0, 22750, -10000, 0)
    OP_6B(11040, 0)
    OP_6C(45000, 0)
    OP_6E(150, 0)
    OP_22(0x79, 0x0, 0x64)

    def lambda_42F():
        OP_6D(2240, 0, 31860, 10000)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_42F)

    def lambda_447():
        OP_67(0, 20330, -10000, 10000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_447)

    def lambda_45F():
        OP_6B(9000, 10000)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_45F)
    OP_C8(0x200, 0x46, "C_PLAC10._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    OP_6F(0x0, 60)

    def lambda_494():
        OP_91(0xFE, 0x0, 0xFFFFC568, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_494)

    def lambda_4AF():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4AF)
    Sleep(2500)

    def lambda_4CF():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4CF)
    Sleep(1500)

    def lambda_4EF():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0xE10, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4EF)
    Sleep(900)

    def lambda_50F():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0xC80, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_50F)
    Sleep(800)

    def lambda_52F():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0xAF0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_52F)
    Sleep(700)

    def lambda_54F():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_54F)
    FadeToDark(1000, 0, -1)
    Sleep(600)

    def lambda_579():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_579)
    Sleep(500)
    OP_0D()
    Sleep(500)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x14, 0x1)
    OP_44(0xE, 0x0)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x0)
    OP_44(0xF, 0x1)
    SetChrPos(0x14, 570, 100, 22920, 360)
    SetChrPos(0x15, 570, 100, 22920, 360)
    OP_6D(-15480, 15220, 18720, 0)
    OP_67(0, 9940, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(31000, 0)
    OP_6E(367, 0)
    SetChrBattleFlags(0xE, 0x20)
    SetChrBattleFlags(0xF, 0x20)
    SetChrBattleFlags(0x10, 0x20)
    SetChrBattleFlags(0x11, 0x20)
    SetChrBattleFlags(0x12, 0x20)
    SetChrBattleFlags(0x13, 0x20)
    OP_48()
    OP_89(0xE, -800, 2300, 23440, 270)
    OP_89(0xF, -1170, 2300, 23910, 270)
    OP_89(0x11, -740, 2300, 23530, 270)
    OP_89(0x10, -1600, 2300, 22200, 270)
    OP_89(0x13, -740, 2300, 23530, 270)
    OP_89(0x12, -740, 2300, 23530, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x1)
    OP_73(0x0)
    OP_43(0xF, 0x0, 0x0, 0x7)
    Sleep(700)
    OP_43(0x11, 0x1, 0x0, 0x4)
    Sleep(600)
    OP_43(0x10, 0x1, 0x0, 0x3)
    Sleep(600)
    OP_43(0x12, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0x13, 0x1, 0x0, 0x6)
    Sleep(1000)
    OP_43(0xE, 0x0, 0x0, 0x8)
    Sleep(3000)

    def lambda_70C():
        OP_6D(1040, 0, 47760, 5000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_70C)

    def lambda_724():
        OP_67(0, 9770, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_724)

    def lambda_73C():
        OP_6B(3510, 5000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_73C)

    def lambda_74C():
        OP_6C(66000, 5000)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_74C)

    def lambda_75C():
        OP_6E(349, 5000)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_75C)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0xE, 0x3)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0xF, 0x2)
    Sleep(500)

    ChrTalk(    #0
        0xE,
        (
            "#691F#5P哦哦，埃尔赛尤号\x01",
            "好像先到达了。\x02\x03",

            "#693F啊～真是无论何时看\x01",
            "都会令人震撼的机体啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xF,
        (
            "#2P真的是……\x01",
            "令人着迷啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xF,
        (
            "#2P要是每天都能整备这种飞船，\x01",
            "维修技师可是享尽福气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xE,
        "#691F#5P嗨，这应该是我说才对。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -10930, 0, 35080, 72)

    NpcTalk(    #4
        0xD,
        "男性的声音",
        (
            "#1P呀，格斯塔夫维修长。\x01",
            "多亏你百忙之中能过来。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_8DD():
        TurnDirection(0xF, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8DD)
    TurnDirection(0xE, 0xD, 400)

    def lambda_8F2():
        OP_8E(0xFE, 0xFFFFEA52, 0x0, 0x9E3E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8F2)
    Fade(1000)
    OP_6D(-4280, 0, 41130, 0)
    OP_67(0, 10220, -10000, 0)
    OP_6B(2490, 0)
    OP_6C(192000, 0)
    OP_6E(262, 0)

    def lambda_94F():

        label("loc_94F")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_94F")

    QueueWorkItem2(0xE, 1, lambda_94F)

    def lambda_960():

        label("loc_960")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_960")

    QueueWorkItem2(0xF, 1, lambda_960)
    OP_0D()
    WaitChrThread(0xD, 0x1)
    TurnDirection(0xD, 0xE, 400)
    WaitChrThread(0xD, 0x2)

    ChrTalk(    #5
        0xE,
        (
            "#691F#6P哟，希德中校。\x01",
            "又是你来迎接吗。\x02\x03",

            "莫非升迁之后成了这里的\x01",
            "守备队长了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xD,
        (
            "#701F#2P哈哈，你说的没错。\x02\x03",

            "其实我正准备和部下过一会儿一起\x01",
            "搭乘警备艇出发呢。\x02\x03",

            "准备工作已经结束了，反正也闲着，\x01",
            "就来接你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xE,
        (
            "#693F#6P哈哈，辛苦了。\x02\x03",

            "#692F说起来，这里\x01",
            "似乎也发生地震了吧？\x02\x03",

            "埃尔赛尤号不会\x01",
            "有所损坏吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        (
            "#703F#2P不，埃尔赛尤号是在\x01",
            "地震发生之后到达的。\x02\x03",

            "地震的时候，也是因为事先已经作了周全的准备，\x01",
            "所以几乎没有出现什么太大的损害。\x02\x03",

            "#701F这里的设施也都运行正常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xE,
        (
            "#691F#6P那可真是帮了大忙了。\x02\x03",

            "我想现在就立刻\x01",
            "开始进入作业……\x02\x03",

            "亲卫队的人都在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xD,
        (
            "#701F#2P啊啊……我来带路。\x02\x03",

            "现在去的话，我想\x01",
            "还能看到有趣的东西哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xE,
        "#692F#6P啊？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_376 end

    def Function_3_C25(): pass

    label("Function_3_C25")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD896, 0x0, 0x5C1C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDD8C, 0x0, 0x98E4, 0xFA0, 0x0)
    OP_8E(0xFE, 0x500, 0x0, 0xB6F8, 0xFA0, 0x0)
    OP_8C(0xFE, 325, 400)
    Return()

    # Function_3_C25 end

    def Function_4_C6E(): pass

    label("Function_4_C6E")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD74C, 0x0, 0x5CDA, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDD1E, 0x0, 0x94B6, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xB716, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_C6E end

    def Function_5_CB7(): pass

    label("Function_5_CB7")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD80A, 0x0, 0x5A5A, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDD1E, 0x0, 0x8CE6, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFF6C8, 0x0, 0xB96E, 0xFA0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_5_CB7 end

    def Function_6_D00(): pass

    label("Function_6_D00")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD670, 0x0, 0x5D66, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDD1E, 0x0, 0x8CE6, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFF24A, 0x0, 0xB9C8, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 45)
    Return()

    # Function_6_D00 end

    def Function_7_D49(): pass

    label("Function_7_D49")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD80A, 0x0, 0x5A5A, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDD1E, 0x0, 0x90CE, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFFC04, 0x0, 0xA56E, 0xFA0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_7_D49 end

    def Function_8_D92(): pass

    label("Function_8_D92")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD670, 0x0, 0x5D66, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFE408, 0x0, 0x9934, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFF4AC, 0x0, 0xA5C8, 0xFA0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_8_D92 end

    def Function_9_DDB(): pass

    label("Function_9_DDB")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    OP_6D(1860, 0, 29300, 0)
    OP_67(0, 15020, -10000, 0)
    OP_6C(15000, 0)
    OP_6B(8600, 0)
    OP_6E(255, 0)
    OP_A1(0x9, 0x3)
    OP_A1(0xA, 0x1)
    OP_A1(0xB, 0x2)
    OP_A1(0xC, 0x0)
    SetChrPos(0x9, 1620, 0, 23850, 0)
    SetChrPos(0xA, 10180, -10450, 61010, 0)
    SetChrPos(0xB, 28590, -10450, 60800, 0)
    SetChrPos(0xC, -8380, -10450, 60710, 0)
    OP_A1(0x17, 0x7)
    OP_A1(0x18, 0x5)
    OP_A1(0x19, 0x6)
    OP_A1(0x1A, 0x4)
    SetChrPos(0x17, 1620, 100, 23850, 0)
    SetChrPos(0x18, 10180, -10450, 61010, 0)
    SetChrPos(0x19, 28590, -10450, 60800, 0)
    SetChrPos(0x1A, -8380, -10450, 60710, 0)
    ClearMapFlags(0x10)
    SetChrPos(0x8, 10750, 0, 30020, 270)
    ClearChrFlags(0x8, 0x80)

    def lambda_EF0():

        label("loc_EF0")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_EF0")

    QueueWorkItem2(0x8, 1, lambda_EF0)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    OP_43(0x9, 0x0, 0x0, 0xA)

    def lambda_F1C():
        OP_6D(9110, 0, 26810, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F1C)

    def lambda_F34():
        OP_67(0, 18670, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F34)

    def lambda_F4C():
        OP_6B(6000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F4C)

    def lambda_F5C():
        OP_6C(56000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F5C)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(11060, 0, 30510, 0)
    OP_67(0, 7040, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(    #12
        0x8,
        (
            "#1125F#5P……没想到它竟然\x01",
            "会落到那些人手里。\x02\x03",

            "#1122F既然如此，不如让我亲手了结……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0x1)
    OP_8C(0x8, 270, 400)
    Sleep(500)

    ChrTalk(    #13
        0x8,
        (
            "#1128F#5P……不行不行。\x02\x03",

            "如果我在此时贸然行动，\x01",
            "只会重蹈覆辙而已。\x02\x03",

            "#1120F呼呼，也就是说，不管是我还是它\x01",
            "都处在相同立场啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_8C(0x8, 90, 400)
    Sleep(500)

    ChrTalk(    #14
        0x8,
        (
            "#1125F#6P女神啊……\x02\x03",

            "#1122F请引导我们这些\x01",
            "混乱大地上的人吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_9_DDB end

    def Function_10_111C(): pass

    label("Function_10_111C")

    OP_22(0x75, 0x0, 0x64)
    OP_43(0x9, 0x1, 0x0, 0xB)
    Sleep(500)
    OP_43(0xA, 0x1, 0x0, 0xC)
    Sleep(500)
    OP_43(0xB, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0xE)
    Sleep(8500)
    Return()

    # Function_10_111C end

    def Function_11_1152(): pass

    label("Function_11_1152")

    OP_22(0x77, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, 1620, 0, 23850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_6F(0x0, 360)
    OP_70(0x0, 0x1F4)
    Sleep(500)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
    OP_82(0x1, 0x2)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
    OP_B0(0x0, 0x2D)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 500)
    OP_70(0x0, 0x208)
    Sleep(500)

    def lambda_1241():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1241)

    def lambda_125C():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_125C)
    Sleep(300)

    def lambda_127C():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_127C)

    def lambda_1297():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1297)
    Sleep(300)

    def lambda_12B7():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12B7)

    def lambda_12D2():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_12D2)
    Sleep(300)

    def lambda_12F2():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12F2)

    def lambda_130D():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_130D)
    Sleep(300)

    def lambda_132D():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_132D)

    def lambda_1348():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1348)
    Sleep(300)

    def lambda_1368():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1368)

    def lambda_1383():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1383)
    Sleep(300)

    def lambda_13A3():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13A3)

    def lambda_13BE():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_13BE)
    Sleep(300)

    def lambda_13DE():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13DE)

    def lambda_13F9():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_13F9)
    Return()

    # Function_11_1152 end

    def Function_12_140F(): pass

    label("Function_12_140F")

    PlayEffect(0x1, 0x2, 0xFF, 10180, -10450, 61010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_6F(0x1, 360)
    OP_70(0x1, 0x1F4)
    Sleep(500)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)

    def lambda_1476():
        OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1476)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)

    def lambda_14A5():
        OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_14A5)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
    OP_82(0x2, 0x2)

    def lambda_14D7():
        OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_14D7)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)

    def lambda_1506():
        OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1506)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)

    def lambda_1535():
        OP_91(0xFE, 0x0, 0x1C2, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1535)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
    OP_B0(0x1, 0x2D)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x208)
    Sleep(500)

    def lambda_1580():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1580)

    def lambda_159B():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_159B)
    Sleep(300)

    def lambda_15BB():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15BB)

    def lambda_15D6():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_15D6)
    Sleep(300)

    def lambda_15F6():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15F6)

    def lambda_1611():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1611)
    Sleep(300)

    def lambda_1631():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1631)

    def lambda_164C():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_164C)
    Sleep(300)

    def lambda_166C():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_166C)

    def lambda_1687():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1687)
    Sleep(300)

    def lambda_16A7():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_16A7)

    def lambda_16C2():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_16C2)
    Sleep(300)

    def lambda_16E2():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_16E2)

    def lambda_16FD():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_16FD)
    Sleep(300)

    def lambda_171D():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_171D)

    def lambda_1738():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1738)
    Return()

    # Function_12_140F end

    def Function_13_174E(): pass

    label("Function_13_174E")

    PlayEffect(0x1, 0x3, 0xFF, 28590, -10450, 60800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_6F(0x2, 360)
    OP_70(0x2, 0x1F4)
    Sleep(500)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
    OP_82(0x3, 0x2)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
    OP_B0(0x2, 0x2D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 500)
    OP_70(0x2, 0x208)
    Sleep(500)

    def lambda_1838():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1838)

    def lambda_1853():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1853)
    Sleep(300)

    def lambda_1873():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1873)

    def lambda_188E():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_188E)
    Sleep(300)

    def lambda_18AE():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18AE)

    def lambda_18C9():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_18C9)
    Sleep(300)

    def lambda_18E9():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18E9)

    def lambda_1904():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1904)
    Sleep(300)

    def lambda_1924():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1924)

    def lambda_193F():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_193F)
    Sleep(300)

    def lambda_195F():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_195F)

    def lambda_197A():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_197A)
    Sleep(300)

    def lambda_199A():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_199A)

    def lambda_19B5():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_19B5)
    Sleep(300)

    def lambda_19D5():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_19D5)

    def lambda_19F0():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_19F0)
    Return()

    # Function_13_174E end

    def Function_14_1A06(): pass

    label("Function_14_1A06")

    PlayEffect(0x1, 0x4, 0xFF, -8380, -10450, 60710, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x1F4)
    Sleep(500)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)

    def lambda_1A6D():
        OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1A6D)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)

    def lambda_1A9C():
        OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1A9C)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
    OP_82(0x4, 0x2)

    def lambda_1ACE():
        OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1ACE)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)

    def lambda_1AFD():
        OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1AFD)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)

    def lambda_1B2C():
        OP_91(0xFE, 0x0, 0x1C2, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1B2C)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
    OP_B0(0x3, 0x2D)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 500)
    OP_70(0x3, 0x208)
    Sleep(500)

    def lambda_1B77():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF7CCA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B77)

    def lambda_1B92():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF7CCA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1B92)
    Sleep(300)

    def lambda_1BB2():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF7CCA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BB2)

    def lambda_1BCD():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF7CCA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1BCD)
    Sleep(300)

    def lambda_1BED():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BED)

    def lambda_1C08():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1C08)
    Sleep(300)

    def lambda_1C28():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C28)

    def lambda_1C43():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1C43)
    Sleep(300)

    def lambda_1C63():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C63)

    def lambda_1C7E():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1C7E)
    Sleep(300)

    def lambda_1C9E():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C9E)

    def lambda_1CB9():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1CB9)
    Sleep(300)

    def lambda_1CD9():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1CD9)

    def lambda_1CF4():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1CF4)
    Sleep(300)

    def lambda_1D14():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1D14)

    def lambda_1D2F():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1D2F)
    OP_43(0x9, 0x1, 0x0, 0xF)
    Return()

    # Function_14_1A06 end

    def Function_15_1D4C(): pass

    label("Function_15_1D4C")

    OP_24(0x75, 0x5A)
    OP_24(0x77, 0x5A)
    Sleep(200)
    OP_24(0x75, 0x50)
    OP_24(0x77, 0x50)
    Sleep(200)
    OP_24(0x75, 0x46)
    OP_24(0x77, 0x46)
    Sleep(200)
    OP_24(0x75, 0x3C)
    OP_24(0x77, 0x3C)
    Sleep(200)
    OP_24(0x75, 0x32)
    OP_24(0x77, 0x32)
    Sleep(200)
    OP_24(0x75, 0x28)
    OP_24(0x77, 0x28)
    Sleep(200)
    OP_24(0x75, 0x1E)
    OP_24(0x77, 0x1E)
    Sleep(200)
    OP_23(0x75)
    OP_23(0x77)
    OP_23(0xCF)
    Return()

    # Function_15_1D4C end

    SaveToFile()

Try(main)
