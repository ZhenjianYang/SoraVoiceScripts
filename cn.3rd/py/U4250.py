from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4250   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4250.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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
        '骷髅邪首',                             # 9
        '骷髅邪首',                             # 10
        '骷髅邪首',                             # 11
        '骷髅邪首',                             # 12
        '',                                     # 13
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
        'ED6_DT29/CH14450 ._CH',             # 00
        'ED6_DT29/CH14450 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT29/CH14450P._CP',             # 00
        'ED6_DT29/CH14450P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -140,
        TriggerZ            = 1000,
        TriggerY            = 1520,
        TriggerRange        = 1000,
        ActorX              = -140,
        ActorZ              = 3000,
        ActorY              = 1520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_174",          # 01, 1
        "Function_2_186",          # 02, 2
        "Function_3_BDC",          # 03, 3
        "Function_4_C3D",          # 04, 4
        "Function_5_C9E",          # 05, 5
        "Function_6_CFF",          # 06, 6
        "Function_7_D60",          # 07, 7
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_173")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_173")

    Return()

    # Function_0_15E end

    def Function_1_174(): pass

    label("Function_1_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185")
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)

    label("loc_185")

    Return()

    # Function_1_174 end

    def Function_2_186(): pass

    label("Function_2_186")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(238, 0x42, 0x2)
    OP_E0(239, 0x43, 0x2)
    OP_E0(240, 0x44, 0x2)
    OP_E0(241, 0x45, 0x2)
    SetChrPos(0x109, -1030, 0, -25890, 0)
    SetChrPos(0x10F, 280, 0, -26320, 0)
    SetChrPos(0xF0, -1200, 0, -26590, 0)
    SetChrPos(0xF1, 390, 0, -26590, 0)
    OP_6D(-610, 12950, 19400, 0)
    OP_67(0, 8460, -10000, 0)
    OP_6B(3310, 0)
    OP_6C(45000, 0)
    OP_6E(344, 0)
    FadeToBright(2000, 0)

    def lambda_236():
        OP_6D(190, 1700, -14550, 9000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_236)

    def lambda_24E():
        OP_67(0, 8470, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_24E)

    def lambda_266():
        OP_6B(3310, 9000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_266)

    def lambda_276():
        OP_6C(45000, 9000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_276)

    def lambda_286():
        OP_6E(344, 9000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_286)
    Sleep(4000)

    def lambda_29B():
        OP_8E(0xFE, 0xFFFFFBBE, 0x0, 0xFFFFC72A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_29B)
    Sleep(300)

    def lambda_2BB():
        OP_8E(0xFE, 0x230, 0x0, 0xFFFFC6BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2BB)
    Sleep(300)

    def lambda_2DB():
        OP_8E(0xFE, 0xFFFFFB1E, 0x0, 0xFFFFC0FF, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2DB)
    Sleep(300)

    def lambda_2FB():
        OP_8E(0xFE, 0x10E, 0x0, 0xFFFFC054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2FB)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    OP_6D(780, 0, -14130, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(45000, 0)
    OP_6E(298, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A9")

    ChrTalk(    #0
        0x10E,
        "#178F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_3A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E8")

    ChrTalk(    #1
        0x102,
        (
            "#1503F……果然，\x01",
            "没有人的气息呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49F")

    label("loc_3E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_426")

    ChrTalk(    #2
        0x10D,
        (
            "#276F……果然，\x01",
            "没有人的气息呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49F")

    label("loc_426")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_466")

    ChrTalk(    #3
        0x10B,
        (
            "#215F果、果然……\x01",
            "一个人也没有呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49F")

    label("loc_466")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49F")

    ChrTalk(    #4
        0x107,
        (
            "#063F果、果然……\x01",
            "谁也不在呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49F")


    ChrTalk(    #5
        0x109,
        (
            "#1067F#5P不……\x01",
            "也不是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        (
            "#1441F#5P……小心。\x01",
            "他们包围过来了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_523")

    ChrTalk(    #7
        0x10E,
        "#172F嗯……！？\x02",
    )

    CloseMessageWindow()

    label("loc_523")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_550")

    ChrTalk(    #8
        0x107,
        "#065F哎……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D1")

    label("loc_550")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57D")

    ChrTalk(    #9
        0x10B,
        "#213F咦……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D1")

    label("loc_57D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A8")

    ChrTalk(    #10
        0x10D,
        "#273F唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D1")

    label("loc_5A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D1")

    ChrTalk(    #11
        0x102,
        "#1502F……！？\x02",
    )

    CloseMessageWindow()

    label("loc_5D1")

    LoadEffect(0x1, "map\\mp258_00.eff")
    OP_20(0x7D0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_611")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_678")

    label("loc_611")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_639")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_678")

    label("loc_639")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_661")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_678")

    label("loc_661")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_678")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A5")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_70C")

    label("loc_6A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CD")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_70C")

    label("loc_6CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F5")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_70C")

    label("loc_6F5")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_70C")

    Sleep(1000)

    def lambda_717():
        OP_6D(1030, 0, -10500, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_717)

    def lambda_72F():
        OP_67(0, 5900, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_72F)

    def lambda_747():
        OP_6B(2730, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_747)

    def lambda_757():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_757)

    def lambda_767():
        OP_6E(338, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_767)
    WaitChrThread(0x109, 0x0)
    OP_22(0x32E, 0x0, 0x64)
    OP_43(0x10, 0x0, 0x0, 0x3)
    Sleep(100)
    OP_43(0x11, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x5)
    Sleep(100)
    OP_43(0x13, 0x0, 0x0, 0x6)
    WaitChrThread(0x13, 0x0)
    OP_23(0x137)
    OP_1D(0x97)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 3)
    SetChrSubChip(0x10F, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 4)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 5)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #12
        0x109,
        "#1063F#6P开门见山地迎接吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1446F#2P女神啊……\x02\x03",

            "#1443F请让这些迷茫的灵魂\x01",
            "得到安息……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_894():
        OP_6D(1190, 0, -12350, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_894)

    def lambda_8AC():
        OP_67(0, 6150, -10000, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8AC)

    def lambda_8C4():
        OP_6B(2200, 400)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8C4)

    def lambda_8D4():
        OP_6E(297, 400)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8D4)
    SetChrChipByIndex(0x11, 1)

    def lambda_8E9():
        OP_8F(0xFE, 0xFFFFFD6C, 0x0, 0xFFFFCD88, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_8E9)
    Sleep(10)
    SetChrChipByIndex(0x13, 1)

    def lambda_90E():
        OP_8F(0xFE, 0x168, 0x0, 0xFFFFCDB0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_90E)
    Sleep(20)
    SetChrChipByIndex(0x10, 1)

    def lambda_933():
        OP_8F(0xFE, 0xFFFFF8D0, 0x0, 0xFFFFCE32, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_933)
    Sleep(20)
    SetChrChipByIndex(0x12, 1)

    def lambda_958():
        OP_8F(0xFE, 0x514, 0x0, 0xFFFFCC98, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_958)
    WaitChrThread(0x109, 0x0)
    Battle(0xF6, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x109, -710, 0, -10400, 0)
    SetChrPos(0x10F, 750, 0, -10520, 0)
    SetChrPos(0xF0, -890, 0, -12050, 0)
    SetChrPos(0xF1, 490, 0, -12220, 0)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_6D(910, 0, -10440, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(45000, 0)
    OP_6E(292, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #14
        0x10E,
        (
            "#175F呜，没想到……\x02\x03",

            "#177F城里面的人\x01",
            "到底到哪里去了！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AC6():
        TurnDirection(0xFE, 0x10E, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_AC6)

    def lambda_AD4():
        TurnDirection(0xFE, 0x10E, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_AD4)
    Sleep(50)

    def lambda_AE7():
        TurnDirection(0xFE, 0x10E, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_AE7)
    Sleep(50)
    TurnDirection(0x109, 0x10E, 400)
    Sleep(300)

    ChrTalk(    #15
        0x109,
        (
            "#1065F#5P总之……\x01",
            "在城里面调查一番吧。\x02\x03",

            "#1063F也许会发现\x01",
            "什么线索也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10E,
        (
            "#176F嗯……\x02\x03",

            "#178F谒见室、亲卫队值班室、\x01",
            "地下区域以及女王宫……\x02\x03",

            "这些地方都调查一遍吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2716)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_186 end

    def Function_3_BDC(): pass

    label("Function_3_BDC")

    SetChrPos(0xFE, -3370, 0, -9660, 135)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_C03():

        label("loc_C03")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_C03")

    QueueWorkItem2(0xFE, 3, lambda_C03)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)
    OP_82(0x0, 0x2)

    def lambda_C23():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C23)
    Sleep(500)
    OP_23(0x87)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_3_BDC end

    def Function_4_C3D(): pass

    label("Function_4_C3D")

    SetChrPos(0xFE, -1450, 300, -8480, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_C64():

        label("loc_C64")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_C64")

    QueueWorkItem2(0xFE, 3, lambda_C64)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)
    OP_82(0x1, 0x2)

    def lambda_C84():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C84)
    Sleep(500)
    OP_23(0x87)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_C3D end

    def Function_5_C9E(): pass

    label("Function_5_C9E")

    SetChrPos(0xFE, 2900, 0, -9580, 225)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_CC5():

        label("loc_CC5")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_CC5")

    QueueWorkItem2(0xFE, 3, lambda_CC5)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)
    OP_82(0x2, 0x2)

    def lambda_CE5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CE5)
    Sleep(500)
    OP_23(0x87)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_5_C9E end

    def Function_6_CFF(): pass

    label("Function_6_CFF")

    SetChrPos(0xFE, 830, 300, -8600, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_D26():

        label("loc_D26")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D26")

    QueueWorkItem2(0xFE, 3, lambda_D26)
    OP_22(0x99, 0x0, 0x64)
    Sleep(200)
    OP_82(0x3, 0x2)

    def lambda_D46():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D46)
    Sleep(500)
    OP_23(0x87)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_6_CFF end

    def Function_7_D60(): pass

    label("Function_7_D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2F")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(1280)
    Sleep(500)
    Jump("loc_E32")

    label("loc_E2F")

    TalkBegin(0xFF)

    label("loc_E32")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #17
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_E5C")

    label("loc_E5C")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC7")

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

    Jump("loc_EC1")

    label("loc_EC1")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EDE"),
        (1, "loc_F59"),
        (2, "loc_F88"),
        (SWITCH_DEFAULT, "loc_FB7"),
    )


    label("loc_EDE")

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
    OP_1D(0xE6)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC4")

    label("loc_F59")

    OP_A9(0x18)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_F85")

    label("loc_F85")

    Jump("loc_FC4")

    label("loc_F88")

    OP_A9(0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_FB4")

    label("loc_FB4")

    Jump("loc_FC4")

    label("loc_FB7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC4")

    label("loc_FC4")

    Jump("loc_E6F")

    label("loc_FC7")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF4")
    OP_A2(0x2588)
    EventEnd(0x1)
    Jump("loc_FF7")

    label("loc_FF4")

    TalkEnd(0xFF)

    label("loc_FF7")

    Return()

    # Function_7_D60 end

    SaveToFile()

Try(main)
