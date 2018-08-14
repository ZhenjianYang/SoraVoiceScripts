from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4100   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4100.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '徘徊魔兽',                             # 9
        '徘徊魔兽',                             # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT29/CH14500 ._CH',             # 00
        'ED6_DT29/CH14501 ._CH',             # 01
        'ED6_DT29/CH14510 ._CH',             # 02
        'ED6_DT29/CH14511 ._CH',             # 03
        'ED6_DT29/CH14520 ._CH',             # 04
        'ED6_DT29/CH14521 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14500P._CP',             # 00
        'ED6_DT29/CH14501P._CP',             # 01
        'ED6_DT29/CH14510P._CP',             # 02
        'ED6_DT29/CH14511P._CP',             # 03
        'ED6_DT29/CH14520P._CP',             # 04
        'ED6_DT29/CH14521P._CP',             # 05
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -140,
        Z                   = 0,
        Y                   = -21440,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xC8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 140,
        Z                   = 0,
        Y                   = -5820,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xC8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -140,
        Z                   = 0,
        Y                   = -21440,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 140,
        Z                   = 0,
        Y                   = -5820,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 8880,
        TriggerZ            = 0,
        TriggerY            = -43040,
        TriggerRange        = 1000,
        ActorX              = 8880,
        ActorZ              = 2000,
        ActorY              = -43040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1AE",          # 00, 0
        "Function_1_224",          # 01, 1
        "Function_2_2DF",          # 02, 2
        "Function_3_137E",         # 03, 3
        "Function_4_1417",         # 04, 4
        "Function_5_148D",         # 05, 5
        "Function_6_14C9",         # 06, 6
        "Function_7_15D9",         # 07, 7
        "Function_8_16DD",         # 08, 8
        "Function_9_1975",         # 09, 9
        "Function_10_1A60",        # 0A, 10
        "Function_11_1B1C",        # 0B, 11
        "Function_12_1C32",        # 0C, 12
        "Function_13_1C80",        # 0D, 13
        "Function_14_1C98",        # 0E, 14
    )


    def Function_0_1AE(): pass

    label("Function_0_1AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (115, "loc_1E0"),
        (116, "loc_1E7"),
        (SWITCH_DEFAULT, "loc_1FA"),
    )


    label("loc_1E0")

    Event(0, 9)
    Jump("loc_1FA")

    label("loc_1E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_1F7")
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_1F7")

    Jump("loc_1FA")

    label("loc_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_210")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 7)
    Jump("loc_223")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_223")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_223")

    Return()

    # Function_0_1AE end

    def Function_1_224(): pass

    label("Function_1_224")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x23005B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A")
    SoundDistance(0x1CB, 0x64, 0x0, 0xFFFF4BD8, 0x7D0, 0x3A98, 0x64, 0x0)

    label("loc_25A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_26D")
    OP_B1("U4100_y")
    Jump("loc_276")

    label("loc_26D")

    OP_B1("U4100_n")

    label("loc_276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_28A")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_294")

    label("loc_28A")

    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2")
    OP_10(0xA, 0x0)
    Jump("loc_2A8")

    label("loc_2A2")

    OP_71(0x41A, 0x0)
    ExitThread()

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6")
    OP_10(0x9, 0x0)
    Jump("loc_2BC")

    label("loc_2B6")

    OP_71(0x41B, 0x0)
    ExitThread()

    label("loc_2BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD")
    OP_1B(0xF, 0x0, 0xA)

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    OP_82(0x8C, 0x0)
    OP_82(0x8D, 0x0)
    OP_82(0x8F, 0x0)

    label("loc_2DE")

    Return()

    # Function_1_224 end

    def Function_2_2DF(): pass

    label("Function_2_2DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 120, 0, -54230, 0)
    SetChrPos(0x10F, 910, 0, -55320, 0)
    SetChrPos(0x107, -910, 0, -55370, 0)
    SetChrPos(0x10E, -20, 0, -56270, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-140, 0, -54880, 0)
    OP_67(0, 9630, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(270000, 0)
    OP_6E(272, 0)
    Sleep(1000)

    def lambda_3A3():
        OP_6D(-600, 0, -54600, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3A3)

    def lambda_3BB():
        OP_67(0, 10270, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3BB)

    def lambda_3D3():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_3D3)

    def lambda_3E3():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_3E3)
    FadeToBright(2000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, 0, -55300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(200)

    def lambda_454():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_454)

    def lambda_466():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_466)

    def lambda_478():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_478)

    def lambda_48A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_48A)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x2)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x109,
        "#1079F#5P啊……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_54D():
        OP_6D(-1480, 500, -47750, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_54D)

    def lambda_565():
        OP_67(0, 5180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_565)

    def lambda_57D():
        OP_6B(3220, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_57D)

    def lambda_58D():
        OP_6E(323, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_58D)

    def lambda_59D():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFF3BC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_59D)
    Sleep(300)

    def lambda_5BD():
        OP_8E(0xFE, 0x334, 0x0, 0xFFFF383C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_5BD)
    Sleep(300)

    def lambda_5DD():
        OP_8E(0xFE, 0xFFFFFA92, 0x0, 0xFFFF380A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_5DD)
    Sleep(300)

    def lambda_5FD():
        OP_8E(0xFE, 0xFFFFFE34, 0x0, 0xFFFF340E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_5FD)
    OP_6D(78070, -8000, -23700, 1500)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #1
        0x109,
        (
            "#1078F#6P白隼的雕像……\x01",
            "也就是说，这里是！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10E,
        (
            "#171F#6P没错……\x01",
            "是格兰赛尔的南街区！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        (
            "#067F#6P太、太好了……\x01",
            "终于回来了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x10F, 180, 400)
    Sleep(500)

    ChrTalk(    #4
        0x10F,
        "#1444F#6P………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_756():
        OP_6D(-1370, 0, -49900, 1300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_756)

    def lambda_76E():
        OP_67(0, 5380, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_76E)

    def lambda_786():
        OP_6B(2970, 1300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_786)

    def lambda_796():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_796)
    Sleep(50)

    def lambda_7A9():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_7A9)
    Sleep(50)

    def lambda_7BC():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_7BC)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #5
        0x109,
        (
            "#1079F#5P怎么，莉丝。\x01",
            "看你一脸惊慌失措的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        (
            "#1802F#6P唔……\x01",
            "我想问你们一件事。\x02\x03",

            "格兰赛尔的城门\x01",
            "竟然是这样恐怖的气氛吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        "#1064F#5P哎……\x02",
    )

    CloseMessageWindow()
    OP_1D(0xDD)

    def lambda_88B():
        OP_6D(2550, 0, -61010, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_88B)

    def lambda_8A3():
        OP_67(0, 7590, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8A3)

    def lambda_8BB():
        OP_6B(3190, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8BB)

    def lambda_8CB():
        OP_6C(33000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_8CB)

    def lambda_8DB():
        OP_6E(444, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_8DB)

    def lambda_8EB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8EB)
    Sleep(50)

    def lambda_8FE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_8FE)
    Sleep(50)

    def lambda_911():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_911)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    OP_6D(30, 0, -53360, 0)
    OP_67(0, 8029, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(180000, 0)
    OP_6E(304, 0)

    def lambda_966():
        OP_6D(20, 9090, -58470, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_966)

    def lambda_97E():
        OP_67(0, 6770, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_97E)

    def lambda_996():
        OP_6B(2800, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_996)

    def lambda_9A6():
        OP_6C(180000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_9A6)

    def lambda_9B6():
        OP_6E(262, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_9B6)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #8
        0x109,
        "#1069F#5P#4S！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(1310, 0, -49490, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(304, 0)
    SetChrPos(0x109, 0, 0, -50280, 180)
    SetChrPos(0x10F, 1060, 0, -50870, 180)
    SetChrPos(0x107, -1330, 0, -50890, 180)
    SetChrPos(0x10E, -600, 0, -51780, 180)
    OP_0D()
    Sleep(300)

    ChrTalk(    #9
        0x107,
        "#065F#5P那、那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10E,
        "#177F#5P那、那是什么啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_AD9():
        OP_6D(-1240, 0, -47340, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AD9)

    def lambda_AF1():
        OP_67(0, 5320, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AF1)

    def lambda_B09():
        OP_6B(2950, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_B09)

    def lambda_B19():
        OP_6E(304, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_B19)
    OP_43(0x10E, 0x0, 0x0, 0x5)

    def lambda_B30():

        label("loc_B30")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_B30")

    QueueWorkItem2(0x109, 0, lambda_B30)

    def lambda_B41():

        label("loc_B41")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_B41")

    QueueWorkItem2(0x10F, 0, lambda_B41)

    def lambda_B52():

        label("loc_B52")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_B52")

    QueueWorkItem2(0x107, 0, lambda_B52)
    WaitChrThread(0x10E, 0x0)
    OP_44(0x109, 0x0)
    OP_44(0x10F, 0x0)
    OP_44(0x107, 0x0)
    WaitChrThread(0x109, 0x1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 4280, 0, -1520, 180)
    SetChrPos(0x11, -3740, 0, -19500, 270)

    def lambda_BA5():

        label("loc_BA5")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_BA5")

    QueueWorkItem2(0x10, 1, lambda_BA5)

    def lambda_BB8():

        label("loc_BB8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_BB8")

    QueueWorkItem2(0x11, 1, lambda_BB8)
    OP_43(0x10, 0x0, 0x0, 0x3)
    OP_43(0x11, 0x0, 0x0, 0x4)
    Fade(1000)
    OP_23(0x1CB)
    SetChrPos(0x10E, -4380, 0, -48840, 0)
    OP_6D(80, 3150, -50840, 0)
    OP_67(0, 6830, -10000, 0)
    OP_6B(4070, 0)
    OP_6C(0, 0)
    OP_6E(322, 0)

    def lambda_C2F():
        OP_6D(80, 4550, -21340, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C2F)

    def lambda_C47():
        OP_67(0, 5560, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C47)

    def lambda_C5F():
        OP_6B(4070, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_C5F)

    def lambda_C6F():
        OP_6E(338, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_C6F)
    Sleep(500)

    def lambda_C84():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_C84)
    Sleep(50)

    def lambda_C97():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_C97)
    Sleep(100)

    def lambda_CAA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_CAA)
    Sleep(100)
    WaitChrThread(0x109, 0x0)
    Fade(1000)
    OP_6D(38000, 0, -1390, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(101000, 0)
    OP_6E(364, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_6D(-35060, 0, -19650, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(260000, 0)
    OP_6E(364, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_6D(3860, 3150, -3200, 0)
    OP_67(0, 7640, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(45000, 0)
    OP_6E(335, 0)
    OP_0D()
    Sleep(1000)

    def lambda_D9A():
        OP_6B(3500, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_D9A)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x10F, 0x0)
    Sleep(1000)
    OP_AD(0x2400E4, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    SetChrPos(0x109, -3670, 0, -47720, 0)
    SetChrPos(0x10F, -3420, 0, -49110, 0)
    SetChrPos(0x107, -4770, 0, -50200, 0)
    SetChrPos(0x10E, -5390, 0, -48730, 0)
    OP_6D(-3590, 300, -48330, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(45000, 0)
    OP_6E(364, 0)
    Sleep(2000)
    SoundDistance(0x1CB, 0x64, 0x0, 0xFFFF4BD8, 0x7D0, 0x3A98, 0x64, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #11
        0x107,
        "#065F#6P甲、甲胄士兵……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10E,
        (
            "#172F#6P这、这到底……\x02\x03",

            "为什么格兰赛尔……\x01",
            "……王都会变成这个样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1063F#5P……这实在是\x01",
            "大大出乎意料啊……\x02\x03",

            "#1067F我们在那边的那段时间里\x01",
            "难道发生了什么事，或者……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10F,
        (
            "#1446F……『影之国』的影响\x01",
            "已经波及到这边了吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10E, 90, 400)
    Sleep(300)

    ChrTalk(    #15
        0x10E,
        (
            "#177F#6P呜……\x01",
            "凯文神父、莉丝小姐！\x02\x03",

            "十分抱歉，\x01",
            "我要赶快到王城去看看！\x02\x03",

            "虽然不知道市民们都怎么样了，\x01",
            "但我很担心陛下和殿下的安危！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_107F():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_107F)
    Sleep(100)
    OP_8C(0x10F, 270, 400)
    Sleep(200)

    ChrTalk(    #16
        0x109,
        (
            "#1063F#5P这样的话，\x01",
            "我们一起去吧。\x02\x03",

            "就算是尤莉亚小姐，\x01",
            "一个人行动\x01",
            "也太过危险了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10E,
        "#172F#6P可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#1446F#2P……欲速则不达。\x02\x03",

            "#1443F越是这种异常事态\x01",
            "就越应该冷静行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10E,
        (
            "#175F#6P……………………………\x02\x03",

            "#176F……我明白了。\x01",
            "你们说的没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x109,
        (
            "#1063F#5P好……\x01",
            "那我们就一边调查街道的情况\x01",
            "一边前往王城吧。\x02\x03",

            "看来有不少强力的魔兽\x01",
            "在四处徘徊着，\x01",
            "我们要小心行事。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)

    ChrTalk(    #21
        0x10F,
        "#1443F……了解。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x107,
        "#062F#6P好、好的！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-4130, 0, -50490, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -4130, 0, -50490, 0)
    SetChrPos(0x1, -4130, 0, -50490, 0)
    SetChrPos(0x2, -4130, 0, -50490, 0)
    SetChrPos(0x3, -4130, 0, -50490, 0)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_69(0x0, 0x0)
    OP_A2(0x2702)
    OP_28(0x2B, 0x1, 0x2)
    OP_28(0x2B, 0x1, 0x4)
    OP_28(0x2B, 0x1, 0x8)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_2_2DF end

    def Function_3_137E(): pass

    label("Function_3_137E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1416")
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xFC8, 0x0, 0x4EC, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0x1CC0, 0x0, 0xFFFFFD4E, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xDAC, 0x0, 0xFFFFED90, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(2000)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xF50, 0x0, 0xFFFFF678, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1500)
    Jump("Function_3_137E")

    label("loc_1416")

    Return()

    # Function_3_137E end

    def Function_4_1417(): pass

    label("Function_4_1417")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_148C")
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xFFFFF2AE, 0x0, 0xFFFFA862, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xFFFFB24E, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xFFFFF2E0, 0x0, 0xFFFFBBAE, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(1500)
    Jump("Function_4_1417")

    label("loc_148C")

    Return()

    # Function_4_1417 end

    def Function_5_148D(): pass

    label("Function_5_148D")

    OP_8C(0x10E, 270, 600)
    Sleep(100)
    OP_8E(0xFE, 0xFFFFF52E, 0x0, 0xFFFF3508, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFEAFC, 0x0, 0xFFFF4138, 0x1388, 0x0)
    OP_8C(0x10E, 0, 600)
    Return()

    # Function_5_148D end

    def Function_6_14C9(): pass

    label("Function_6_14C9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(12710, 2900, 1350, 0)
    OP_67(0, 9260, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(45000, 0)
    OP_6E(352, 0)

    def lambda_152C():
        OP_6D(33810, 2900, -1050, 5500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_152C)

    def lambda_1544():
        OP_67(0, 5570, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1544)

    def lambda_155C():
        OP_6B(2450, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_155C)

    def lambda_156C():
        OP_6C(90000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_156C)

    def lambda_157C():
        OP_6E(352, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_157C)
    FadeToBright(2000, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)

    def lambda_15A4():
        OP_6B(2250, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_15A4)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_0D()
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/U4200   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_6_14C9 end

    def Function_7_15D9(): pass

    label("Function_7_15D9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_72(0x41B, 0x0)
    ExitThread()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-3000, 6050, -19740, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(270000, 0)
    OP_6E(352, 0)

    def lambda_1642():
        OP_6D(-35770, -500, -19740, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1642)

    def lambda_165A():
        OP_67(0, 7410, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_165A)

    def lambda_1672():
        OP_6B(3040, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1672)

    def lambda_1682():
        OP_6E(322, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1682)
    FadeToBright(2000, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(1000)

    def lambda_16AA():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_16AA)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2508)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_15D9 end

    def Function_8_16DD(): pass

    label("Function_8_16DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AC")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x8C, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(768)
    Sleep(500)
    Jump("loc_17AF")

    label("loc_17AC")

    TalkBegin(0xFF)

    label("loc_17AF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #23
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_17D9")

    label("loc_17D9")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1944")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_183E")

    label("loc_183E")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_185B"),
        (1, "loc_18D6"),
        (2, "loc_1905"),
        (SWITCH_DEFAULT, "loc_1934"),
    )


    label("loc_185B")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDD)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1941")

    label("loc_18D6")

    OP_A9(0x16)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #24
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_1902")

    label("loc_1902")

    Jump("loc_1941")

    label("loc_1905")

    OP_A9(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #25
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_1931")

    label("loc_1931")

    Jump("loc_1941")

    label("loc_1934")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1941")

    label("loc_1941")

    Jump("loc_17EC")

    label("loc_1944")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1971")
    OP_A2(0x2586)
    EventEnd(0x1)
    Jump("loc_1974")

    label("loc_1971")

    TalkEnd(0xFF)

    label("loc_1974")

    Return()

    # Function_8_16DD end

    def Function_9_1975(): pass

    label("Function_9_1975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1982")
    Call(0, 2)
    Return()

    label("loc_1982")

    OP_DE(0x0, 0xF, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 120, 0, -54230, 0)
    SetChrPos(0x1, 910, 0, -55320, 0)
    SetChrPos(0x2, -910, 0, -55370, 0)
    SetChrPos(0x3, -20, 0, -56270, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, 0, -55300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 11)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_9_1975 end

    def Function_10_1A60(): pass

    label("Function_10_1A60")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 120, 0, -54230, 180)
    SetChrPos(0x2, 910, 0, -55320, 180)
    SetChrPos(0x1, -910, 0, -55370, 180)
    SetChrPos(0x0, -20, 0, -56270, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -10, 0, -55300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 12)
    NewScene("ED6_DT21/M7005   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1A60 end

    def Function_11_1B1C(): pass

    label("Function_11_1B1C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B45")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1B39():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1B39)

    label("loc_1B45")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B6E")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1B62():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1B62)

    label("loc_1B6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B97")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1B8B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1B8B)

    label("loc_1B97")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC0")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1BB4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1BB4)

    label("loc_1BC0")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BEC")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1BEC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C03")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1C03")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C1A")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1C1A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C31")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1C31")

    Return()

    # Function_11_1B1C end

    def Function_12_1C32(): pass

    label("Function_12_1C32")


    def lambda_1C38():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1C38)

    def lambda_1C4A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1C4A)

    def lambda_1C5C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1C5C)

    def lambda_1C6E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1C6E)
    Sleep(1000)
    Return()

    # Function_12_1C32 end

    def Function_13_1C80(): pass

    label("Function_13_1C80")

    EventBegin(0x1)
    OP_23(0x1CB)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/U4150   ._SN", 116, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1C80 end

    def Function_14_1C98(): pass

    label("Function_14_1C98")

    EventBegin(0x0)
    SetChrPos(0x0, 6000, 0, -42000, 270)
    SetChrPos(0x1, 6000, 0, -44000, 270)
    SetChrPos(0x2, 8000, 0, -42000, 270)
    SetChrPos(0x3, 8000, 0, -44000, 270)
    Call(6, 27)
    EventEnd(0x0)
    Return()

    # Function_14_1C98 end

    SaveToFile()

Try(main)
