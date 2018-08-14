from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M4110   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
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
        'ED6_DT29/CH14360 ._CH',             # 00
        'ED6_DT29/CH14360 ._CH',             # 01
        'ED6_DT29/CH14690 ._CH',             # 02
        'ED6_DT29/CH14691 ._CH',             # 03
        'ED6_DT29/CH14460 ._CH',             # 04
        'ED6_DT29/CH14461 ._CH',             # 05
        'ED6_DT29/CH14620 ._CH',             # 06
        'ED6_DT29/CH14621 ._CH',             # 07
        'ED6_DT29/CH14630 ._CH',             # 08
        'ED6_DT29/CH14631 ._CH',             # 09
        'ED6_DT29/CH14010 ._CH',             # 0A
        'ED6_DT29/CH14011 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14360P._CP',             # 00
        'ED6_DT29/CH14360P._CP',             # 01
        'ED6_DT29/CH14690P._CP',             # 02
        'ED6_DT29/CH14691P._CP',             # 03
        'ED6_DT29/CH14460P._CP',             # 04
        'ED6_DT29/CH14461P._CP',             # 05
        'ED6_DT29/CH14620P._CP',             # 06
        'ED6_DT29/CH14621P._CP',             # 07
        'ED6_DT29/CH14630P._CP',             # 08
        'ED6_DT29/CH14631P._CP',             # 09
        'ED6_DT29/CH14010P._CP',             # 0A
        'ED6_DT29/CH14011P._CP',             # 0B
    )

    DeclMonster(
        X                   = -2320,
        Z                   = 0,
        Y                   = -5480,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x258,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10670,
        Z                   = -20,
        Y                   = 23680,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22750,
        Z                   = 0,
        Y                   = 29730,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x259,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -8610,
        Z                   = 0,
        Y                   = -37690,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -44400,
        TriggerZ            = 500,
        TriggerY            = 7650,
        TriggerRange        = 1500,
        ActorX              = -44400,
        ActorZ              = 4000,
        ActorY              = 7650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7980,
        TriggerZ            = 0,
        TriggerY            = 17210,
        TriggerRange        = 1000,
        ActorX              = 7980,
        ActorZ              = 1000,
        ActorY              = 17210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_214",          # 01, 1
        "Function_2_269",          # 02, 2
        "Function_3_3A2",          # 03, 3
        "Function_4_112A",         # 04, 4
        "Function_5_18B5",         # 05, 5
        "Function_6_1BA5",         # 06, 6
        "Function_7_1DD8",         # 07, 7
        "Function_8_1EBF",         # 08, 8
        "Function_9_1FD5",         # 09, 9
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_1DA"),
        (SWITCH_DEFAULT, "loc_1E1"),
    )


    label("loc_1DA")

    Event(0, 7)
    Jump("loc_1E1")

    label("loc_1E1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1ED"),
        (SWITCH_DEFAULT, "loc_1F5"),
    )


    label("loc_1ED")

    SetMapFlags(0x10000000)
    Jump("loc_1F5")

    label("loc_1F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_213")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_213")

    Return()

    # Function_0_1C2 end

    def Function_1_214(): pass

    label("Function_1_214")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFE0C00, 0x230063)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_237")
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x88, 0x0)

    label("loc_237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244")
    OP_79(0x0, 0x2)
    OP_7B()

    label("loc_244")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_261")
    OP_6F(0x2, 0)
    Jump("loc_268")

    label("loc_261")

    OP_6F(0x2, 60)

    label("loc_268")

    Return()

    # Function_1_214 end

    def Function_2_269(): pass

    label("Function_2_269")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-45540, 2600, 6230, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(225000, 0)
    OP_6E(376, 0)

    def lambda_2CC():
        OP_6D(-45540, 600, 6230, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2CC)

    def lambda_2E4():
        OP_67(0, 4660, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2E4)

    def lambda_2FC():
        OP_6B(2230, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2FC)

    def lambda_30C():
        OP_6E(376, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_30C)
    FadeToBright(1500, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    def lambda_330():
        OP_6B(2000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_330)
    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    OP_72(0x401, 0x0)
    ExitThread()
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    OP_0D()
    Sleep(1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M3204   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_269 end

    def Function_3_3A2(): pass

    label("Function_3_3A2")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-45100, 250, 6960, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(225000, 0)
    OP_6E(348, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D1")
    SetChrPos(0x102, -42310, 0, 9750, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449")
    SetChrPos(0x109, -40950, 0, 9840, 225)
    SetChrPos(0xF0, -42200, 0, 11190, 225)
    SetChrPos(0xF1, -40780, 0, 11320, 225)
    Jump("loc_4CE")

    label("loc_449")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48D")
    SetChrPos(0x109, -40950, 0, 9840, 225)
    SetChrPos(0xEF, -42200, 0, 11190, 225)
    SetChrPos(0xF1, -40780, 0, 11320, 225)
    Jump("loc_4CE")

    label("loc_48D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CE")
    SetChrPos(0x109, -40950, 0, 9840, 225)
    SetChrPos(0xEF, -42200, 0, 11190, 225)
    SetChrPos(0xF0, -40780, 0, 11320, 225)

    label("loc_4CE")

    Jump("loc_515")

    label("loc_4D1")

    SetChrPos(0x109, -42310, 0, 9750, 225)
    SetChrPos(0xEF, -40950, 0, 9840, 225)
    SetChrPos(0xF0, -42200, 0, 11190, 225)
    SetChrPos(0xF1, -40780, 0, 11320, 225)

    label("loc_515")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        (
            "\x07\x05石碑表面的表盘发出了光芒，\x01",
            "逐渐浮现出了一段文章。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x02#40W『黑骑士』代替『王』宣告——\x01",
            "#500W \x01",
            "#40W       前方是黑色方舟。\x01",
            "#500W \x01",
            "#40W      请与灭亡故里的遗孤\x01",
            "      一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_665")
    OP_A2(0x2B22)

    ChrTalk(    #2
        0x102,
        "#1504F#6P#3S！！！\x02",
    )

    CloseMessageWindow()

    label("loc_665")


    ChrTalk(    #3
        0x109,
        "#1069F#6P什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BC")

    ChrTalk(    #4
        0x101,
        "#1020F#6P那、那是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_6BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F0")

    ChrTalk(    #5
        0x10B,
        "#216F#6P那、那是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_6F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_725")

    ChrTalk(    #6
        0x105,
        "#1164F#6P那、那是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_725")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75A")

    ChrTalk(    #7
        0x103,
        "#1523F#6P那、那是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_75A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_792")

    ChrTalk(    #8
        0x106,
        "#055F#6P喂喂，那不就是！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_792")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CA")

    ChrTalk(    #9
        0x108,
        "#072F#6P……那不就是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_7CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FB")

    ChrTalk(    #10
        0x104,
        "#1542F#6P那可是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_7FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82F")

    ChrTalk(    #11
        0x10D,
        "#273F#6P……什么………\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_82F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_863")

    ChrTalk(    #12
        0x107,
        "#065F#6P那、那是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_863")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_895")

    ChrTalk(    #13
        0x110,
        "#262F#6P那应该是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_895")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C9")

    ChrTalk(    #14
        0x10C,
        "#112F#6P……那是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FA")

    label("loc_8C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FA")

    ChrTalk(    #15
        0x10E,
        "#172F#6P……那是……！\x02",
    )

    CloseMessageWindow()

    label("loc_8FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A14")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_968")

    ChrTalk(    #16
        0x10F,
        "#1444F#6P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        "#814F#6P怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F0")

    label("loc_968")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AA")

    ChrTalk(    #18
        0x10F,
        (
            "#1444F#6P？？？\x02\x03",

            "……怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F0")

    label("loc_9AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F0")

    ChrTalk(    #19
        0x10A,
        (
            "#814F#6P？？？\x02\x03",

            "怎么了？\x02",
        )
    )

    Jump("loc_9EF")

    label("loc_9EF")

    CloseMessageWindow()

    label("loc_9F0")


    ChrTalk(    #20
        0x109,
        "#1067F#5P不，没什么……\x02",
    )

    CloseMessageWindow()

    label("loc_A14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D20")
    Sleep(500)

    ChrTalk(    #21
        0x102,
        (
            "#1503F#5P……………………………\x02\x03",

            "#1513F……看来，『黑骑士』\x01",
            "就在这最后的领域中啊。\x02\x03",

            "#1514F而且不知为何，\x01",
            "故意点了我的名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        (
            "#1065F#6P啊啊……看来是这样。\x02\x03",

            "#1063F约修亚。\x01",
            "你打算怎么办呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 45, 400)
    Sleep(300)

    ChrTalk(    #23
        0x102,
        (
            "#1505F#5P那还用说……\x01",
            "当然是接受招待了。\x02\x03",

            "#1500F我随时都可以去摸表盘，\x01",
            "等做好准备了就告诉我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBC")

    ChrTalk(    #24
        0x101,
        "#1026F#6P约修亚……\x02",
    )

    CloseMessageWindow()

    label("loc_BBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BEB")

    ChrTalk(    #25
        0x10B,
        "#215F#6P哎，那个……\x02",
    )

    CloseMessageWindow()

    label("loc_BEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C19")

    ChrTalk(    #26
        0x105,
        "#1163F#6P约修亚……\x02",
    )

    CloseMessageWindow()

    label("loc_C19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C48")

    ChrTalk(    #27
        0x107,
        "#063F#6P哥、哥哥……\x02",
    )

    CloseMessageWindow()

    label("loc_C48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7C")

    ChrTalk(    #28
        0x110,
        "#1307F#6P…………可以吗？\x02",
    )

    CloseMessageWindow()

    label("loc_C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D1D")

    ChrTalk(    #29
        0x102,
        (
            "#1513F#5P……没关系。\x01",
            "不管发生什么都无所谓。\x02\x03",

            "#1500F总之……\x01",
            "现在只需考虑如何前进。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1D")

    Jump("loc_1113")

    label("loc_D20")

    Sleep(500)

    ChrTalk(    #30
        0x109,
        (
            "#1065F#5P（『灭亡故里的遗孤』……\x01",
            "  其含义不言自明。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 45, 400)
    Sleep(300)

    ChrTalk(    #31
        0x109,
        (
            "#1063F#5P总之，先回据点\x01",
            "和约修亚商量一下吧。\x02\x03",

            "然后再决定怎么办。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF9")

    ChrTalk(    #32
        0x101,
        "#1007F#6P……嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_DF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E29")

    ChrTalk(    #33
        0x10B,
        "#413F#6P嗯，好……\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_E29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5C")

    ChrTalk(    #34
        0x105,
        "#1169F#6P……好………\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_E5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E91")

    ChrTalk(    #35
        0x103,
        "#1532F#6P……是啊………\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_E91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC5")

    ChrTalk(    #36
        0x106,
        "#552F#6P……是啊………\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_EC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF9")

    ChrTalk(    #37
        0x108,
        "#074F#6P……没错………\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_EF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F28")

    ChrTalk(    #38
        0x104,
        "#1542F#6P是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_F28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F58")

    ChrTalk(    #39
        0x10D,
        "#272F#6P……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_F58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F88")

    ChrTalk(    #40
        0x107,
        "#561F#6P是、是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_F88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB8")

    ChrTalk(    #41
        0x110,
        "#268F#6P……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_FB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FE6")

    ChrTalk(    #42
        0x10C,
        "#115F#6P是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_FE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_100F")

    ChrTalk(    #43
        0x10E,
        "#176F#6P嗯……\x02",
    )

    CloseMessageWindow()

    label("loc_100F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1081")

    ChrTalk(    #44
        0x10A,
        "#1317F#6P（总、总感觉……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10F,
        "#1445F#6P（发生过很多事情啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1113")

    label("loc_1081")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C4")

    ChrTalk(    #46
        0x10F,
        "#1445F#6P（……好像发生过很多事情。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1113")

    label("loc_10C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1113")

    ChrTalk(    #47
        0x10A,
        (
            "#1317F#6P（总、总感觉……\x01",
            "  好像发生过很多事情啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1113")

    OP_A2(0x2B21)
    OP_28(0x3A, 0x1, 0x2)
    OP_28(0x3A, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_3A2 end

    def Function_4_112A(): pass

    label("Function_4_112A")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-45100, 250, 6960, 0)
    OP_67(0, 5420, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(225000, 0)
    OP_6E(348, 0)
    SetChrPos(0x109, -42320, 0, 9790, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C3")
    SetChrPos(0xEF, -43440, 480, 8590, 225)
    SetChrPos(0xF0, -41000, 0, 10170, 225)
    SetChrPos(0xF1, -41900, 0, 11120, 225)
    Jump("loc_1248")

    label("loc_11C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1207")
    SetChrPos(0xF0, -43440, 480, 8590, 225)
    SetChrPos(0xEF, -41000, 0, 10170, 225)
    SetChrPos(0xF1, -41900, 0, 11120, 225)
    Jump("loc_1248")

    label("loc_1207")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1248")
    SetChrPos(0xF1, -43440, 480, 8590, 225)
    SetChrPos(0xEF, -41000, 0, 10170, 225)
    SetChrPos(0xF0, -41900, 0, 11120, 225)

    label("loc_1248")

    OP_0D()
    Sleep(300)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #48
        (
            "\x07\x02#40W『黑骑士』代替『王』宣告——\x01",
            "#500W \x01",
            "#40W       前方是黑色方舟。\x01",
            "#500W \x01",
            "#40W      请与灭亡故里的遗孤\x01",
            "      一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1357")
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #49
        0x102,
        "#1502F#6P……………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    label("loc_1357")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_136A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B2")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "触摸表盘\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    Jump("loc_13A0")

    label("loc_13A0")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13C6"),
        (SWITCH_DEFAULT, "loc_189D"),
    )


    label("loc_13C6")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143E")

    def lambda_142C():
        OP_6D(-45100, 10000, 6960, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_142C)

    label("loc_143E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A2")
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1491():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1491)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_14E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14E7)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_153D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_153D)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1593():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1593)
    Jump("loc_1867")

    label("loc_15A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1706")
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_15F5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_15F5)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_164B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_164B)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_16A1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_16A1)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_16F7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_16F7)
    Jump("loc_1867")

    label("loc_1706")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1867")
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1759():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1759)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_17AF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17AF)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1805():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1805)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_185B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_185B)

    label("loc_1867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1877")
    Sleep(1500)
    Jump("loc_187C")

    label("loc_1877")

    Sleep(500)

    label("loc_187C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M5408   ._SN", 103, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18AF")

    label("loc_189D")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18AF")

    label("loc_18AF")

    Jump("loc_136A")

    label("loc_18B2")

    EventEnd(0x0)
    Return()

    # Function_4_112A end

    def Function_5_18B5(): pass

    label("Function_5_18B5")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-43550, 0, 6920, 0)
    OP_67(0, 6510, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(179000, 0)
    OP_6E(339, 0)
    SetChrPos(0x0, -43470, 490, 8880, 225)
    SetChrPos(0x1, -42470, 0, 10010, 225)
    SetChrPos(0x2, -41040, 0, 10440, 225)
    SetChrPos(0x3, -42120, 0, 11800, 225)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1960")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA2")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "触摸表盘\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    Jump("loc_1996")

    label("loc_1996")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_19BC"),
        (SWITCH_DEFAULT, "loc_1B8D"),
    )


    label("loc_19BC")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1A59():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A59)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1AAF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1AAF)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1B05():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1B05)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1B5B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1B5B)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M5408   ._SN", 103, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B9F")

    label("loc_1B8D")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B9F")

    label("loc_1B9F")

    Jump("loc_1960")

    label("loc_1BA2")

    EventEnd(0x0)
    Return()

    # Function_5_18B5 end

    def Function_6_1BA5(): pass

    label("Function_6_1BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_1BB4")
    Call(0, 5)
    Return()

    label("loc_1BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_END)), "loc_1CA0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD1")
    Call(0, 4)
    Return()

    label("loc_1BD1")

    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #50
        (
            "\x07\x02#40W『黑骑士』代替『王』宣告——\x01",
            "#500W \x01",
            "#40W       前方是黑色方舟。\x01",
            "#500W \x01",
            "#40W      请与灭亡故里的遗孤\x01",
            "      一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_1DD7")

    label("loc_1CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D7B")
    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #51
        (
            "\x07\x02#40W『黑骑士』代替『王』宣告——\x01",
            "#500W \x01",
            "#40W       前方是黑色方舟。\x01",
            "#500W \x01",
            "#40W      请与灭亡故里的遗孤\x01",
            "      一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_1DD7")

    label("loc_1D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_1D8A")
    Call(0, 3)
    Return()

    label("loc_1D8A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #52
        "\x07\x05黒耀石的石碑上没有刻任何东西。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_1DD7")

    Return()

    # Function_6_1BA5 end

    def Function_7_1DD8(): pass

    label("Function_7_1DD8")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -42220, 0, 10120, 45)
    SetChrPos(0x1, -42220, 0, 10120, 45)
    SetChrPos(0x2, -42220, 0, 10120, 45)
    SetChrPos(0x3, -42220, 0, 10120, 45)
    OP_69(0x0, 0x0)
    OP_6C(180000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 8)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_7_1DD8 end

    def Function_8_1EBF(): pass

    label("Function_8_1EBF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EE8")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1EDC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1EDC)

    label("loc_1EE8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F11")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F05():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1F05)

    label("loc_1F11")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F3A")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F2E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1F2E)

    label("loc_1F3A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F63")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F57():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1F57)

    label("loc_1F63")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8F")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1F8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FA6")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1FA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FBD")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1FBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FD4")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1FD4")

    Return()

    # Function_8_1EBF end

    def Function_9_1FD5(): pass

    label("Function_9_1FD5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x297, 1)"), scpexpr(EXPR_END)), "loc_2047")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x00得到了\x1F\x97\x02\x07\x00。\x02",
    )

    Jump("loc_202C")

    label("loc_202C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B9C)
    Jump("loc_20B3")

    label("loc_2047")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #54
        (
            "宝箱里装有\x1F\x97\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x97\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2094")

    label("loc_2094")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_20B3")

    Jump("loc_20E7")

    label("loc_20B6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_20E7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1FD5 end

    SaveToFile()

Try(main)
