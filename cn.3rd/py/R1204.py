from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'R1204   ._SN',
        MapName             = 'Bose',
        Location            = 'R1204.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '玲',                                   # 9
        '帕蒂尔·玛蒂尔',                       # 10
        '目标用照相机',                         # 11
        ' ',                                    # 12
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
        'ED6_DT27/CH03510 ._CH',             # 00
        'ED6_DT27/CH03511 ._CH',             # 01
        'ED6_DT26/CH20662 ._CH',             # 02
        'ED6_DT26/CH20288 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03510P._CP',             # 00
        'ED6_DT27/CH03511P._CP',             # 01
        'ED6_DT26/CH20662P._CP',             # 02
        'ED6_DT26/CH20288P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_250",          # 01, 1
        "Function_2_251",          # 02, 2
        "Function_3_35C",          # 03, 3
        "Function_4_1C58",         # 04, 4
        "Function_5_26AD",         # 05, 5
        "Function_6_32BC",         # 06, 6
        "Function_7_4637",         # 07, 7
        "Function_8_4C1A",         # 08, 8
        "Function_9_6004",         # 09, 9
        "Function_10_604D",        # 0A, 10
        "Function_11_618E",        # 0B, 11
        "Function_12_619C",        # 0C, 12
        "Function_13_61AA",        # 0D, 13
        "Function_14_6203",        # 0E, 14
        "Function_15_6267",        # 0F, 15
        "Function_16_739C",        # 10, 16
        "Function_17_73BD",        # 11, 17
        "Function_18_7416",        # 12, 18
        "Function_19_8EF6",        # 13, 19
        "Function_20_8F4F",        # 14, 20
        "Function_21_8FA8",        # 15, 21
        "Function_22_9008",        # 16, 22
        "Function_23_908E",        # 17, 23
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_END)), "loc_189")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x250A)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_1A9")
    OP_A3(0x2509)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_1A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_1D2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_1F2")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_212")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_232")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_24F")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_24F")

    Return()

    # Function_0_14A end

    def Function_1_250(): pass

    label("Function_1_250")

    Return()

    # Function_1_250 end

    def Function_2_251(): pass

    label("Function_2_251")

    LoadEffect(0x0, "map\\\\mp207_00.eff")
    LoadEffect(0x1, "map\\\\mp207_01.eff")
    LoadEffect(0x2, "map\\\\mp207_02.eff")
    LoadEffect(0x3, "map\\\\mp207_03.eff")
    OP_6D(0, 0, 10000000, 0)
    OP_67(0, 0, -30000, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(276, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF")
    Call(0, 3)

    label("loc_2EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300")
    Call(0, 4)

    label("loc_300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311")
    Call(0, 5)

    label("loc_311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_322")
    Call(0, 6)

    label("loc_322")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_333")
    Call(0, 7)

    label("loc_333")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344")
    Call(0, 8)

    label("loc_344")

    OP_84(0x0)
    OP_84(0x1)
    OP_84(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B")
    Call(0, 15)

    label("loc_35B")

    Return()

    # Function_2_251 end

    def Function_3_35C(): pass

    label("Function_3_35C")

    EventBegin(0x1)
    OP_6D(0, 0, 10000000, 0)
    OP_67(0, 0, -30000, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(276, 0)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "#0C#40W超然于善恶生死之处，\x01",
            "我淡然走过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #1
        "#0C#40W无幸无厄。无悲无喜。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #2
        (
            "#0C#40W黑白将我撕裂，天地将我捉弄，\x01",
            "我变得污秽不堪。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #3
        "#0C#40W何处为始，何处为终。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #4
        (
            "#0C#40W我无处容身。\x01",
            "也未曾前行。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #5
        "#0C#40W然而，世界依然转动。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6 op#A op#5
        "#20A#0C#4S１．乐园#0C\x05\x02",
    )

    Sleep(2000)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_1D(0xAF)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(80, 110, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #7
        "#12C请问您想要几号呢。#0C\x02",
    )

    Jump("loc_570")

    label("loc_570")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 280, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #8
        "#12C１５号吧。#0C\x02",
    )

    Jump("loc_5A2")

    label("loc_5A2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 110, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #9
        "#12C明白了。#0C\x02",
    )

    Jump("loc_5D2")

    label("loc_5D2")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #10
        (
            "#12C『玲』，这次轮到你了。\x01",
            "别让客人失望啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "#0C那里是被称作『乐园』的地方。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #12
        (
            "#0C此馆本身大概也有名字，\x01",
            "只是没有告诉我们。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #13
        (
            "#0C当然，乐园的所在之处，\x01",
            "我们所做为何事，#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #14
        "#0C甚至为何在这里，也都无人知晓。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #15
        "#12C早上好。#0C\x02",
    )

    Jump("loc_730")

    label("loc_730")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("？？？")

    AnonymousTalk(    #16
        "#12C……………………#0C\x02",
    )

    Jump("loc_76E")

    label("loc_76E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #17
        "#12C早上好，１５号。#0C\x02",
    )

    Jump("loc_7A6")

    label("loc_7A6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #18
        "#12C…………？？#0C\x02",
    )

    Jump("loc_7D6")

    label("loc_7D6")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS570._CH")
    OP_C6(0x1, 0x3, -1, 3000, 0)
    OP_43(0x10, 0x3, 0x0, 0xE)
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    Sleep(3500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #19
        "#12C呀，你终于起来了呢。#0C\x02",
    )

    Jump("loc_88E")

    label("loc_88E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 320, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #20
        "#12C…………『克洛斯』#0C\x02",
    )

    Jump("loc_8C4")

    label("loc_8C4")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS575._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #21
        "#12C嘻嘻……\x02",
    )

    Jump("loc_945")

    label("loc_945")

    CloseMessageWindow()

    AnonymousTalk(    #22
        "#12C欢迎来到乐园，『玲』#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "#0C…………欢迎，来到『乐园』。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C4(0x1, 0x800)
    FadeToBright(0, 0)
    OP_0D()
    OP_C6(0x0, 0x3, -1, 3000, 0)
    OP_C6(0x1, 0x3, 16777215, 3000, 0)
    FadeToDark(3000, 16777215, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #24
        (
            "#12C玲，我去工作了。\x01",
            "又被指名了。#0C\x02",
        )
    )

    Jump("loc_A5B")

    label("loc_A5B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #25
        "#12C克洛斯，又要去工作？#0C\x02",
    )

    Jump("loc_A93")

    label("loc_A93")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #26
        (
            "#12C没事的，玲。\x01",
            "很快就能再见的。\x02",
        )
    )

    Jump("loc_ADA")

    label("loc_ADA")

    CloseMessageWindow()

    AnonymousTalk(    #27
        (
            "#12C在那之前\x01",
            "你可要乖乖待着哦？#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    FadeToBright(2000, 16777215)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    FadeToBright(1, 0)
    OP_0D()
    OP_C4(0x0, 0x800)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "#0C名为克洛斯的少年，\x01",
            "和平时一样忙着出去工作了。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #29
        (
            "#0C在我所不知道的地方，\x01",
            "他似乎每天都重复着悲惨的工作。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #30
        "#0C不，其他的孩子也都一样。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #31
        (
            "#0C在我所不知道的地方，\x01",
            "孩子们都在工作着。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_82(0x0, 0x0)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS576._CH")
    OP_C6(0x0, 0x3, -1, 1500, 0)
    Sleep(2500)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "#0C不知为何，我却没有工作。\x01",
            "是的，我一次也没有接到过工作。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #33
        (
            "#0C其他的孩子们都逐渐变得衰弱和瘦小，\x01",
            "只有我吃着好吃的东西，\x01",
            "每天玩着洋娃娃即可。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #34
        "#0C只有我，是特别的。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #35
        "#0C……克洛斯他，叫我『公主殿下』。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    OP_C6(0x0, 0x3, 8947848, 1000, 0)
    Sleep(2000)
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS570._CH")
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS573._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, 290, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #36
        (
            "#12C早上好，玲。今天也是好天气呢。\x01",
            "不过这里有些通风不畅。开开窗户吧！#0C\x02",
        )
    )

    Jump("loc_EE1")

    label("loc_EE1")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x0, 0x800)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "#0C这个爽朗的孩子名叫艾塔。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #38
        (
            "#0C总是面带笑容，而且好奇心旺盛，\x01",
            "喜欢在房间里到处跑来跑去，常常惹克洛斯生气。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, 290, -1, -1)
    SetChrName("艾塔")

    AnonymousTalk(    #39
        (
            "#12C我说，玲。一起玩吧？\x01",
            "我也想玩洋娃娃呢～。#0C\x02",
        )
    )

    Jump("loc_1017")

    label("loc_1017")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #40
        (
            "#12C好啊，艾塔。不过你的工作呢？\x01",
            "今天不用穿那身奇怪的洋装吗？#0C\x02",
        )
    )

    Jump("loc_1074")

    label("loc_1074")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 290, -1, -1)
    SetChrName("艾塔")

    AnonymousTalk(    #41
        (
            "#12C今天休息啊。\x01",
            "因为克洛斯去做了嘛。#0C\x02",
        )
    )

    Jump("loc_10BD")

    label("loc_10BD")

    CloseMessageWindow()

    AnonymousTalk(    #42
        (
            "#12C嘻嘻，那孩子最近被指名的次数增加了哦。\x01",
            "是不是社会性需要呢。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #43
        (
            "#0C艾塔有些老成。\x01",
            "面对无聊的玩笑，\x01",
            "她习惯呵呵笑着掩饰过去。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS572._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "#0C阿洁是个惹人怜爱又成熟的女孩子。\x01",
            "所以常常被大叔们指名。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #45
        (
            "#0C但是阿洁绝不会露出厌恶的表情。\x01",
            "总能巧妙地应付好工作。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #46
        (
            "#12C阿洁，你不喜欢这工作吧？\x01",
            "很痛的吧？#0C\x02",
        )
    )

    Jump("loc_131F")

    label("loc_131F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("阿洁")

    AnonymousTalk(    #47
        (
            "#12C……没关系。\x01",
            "玲不用介意的。\x02",
        )
    )

    Jump("loc_135F")

    label("loc_135F")

    CloseMessageWindow()

    AnonymousTalk(    #48
        (
            "#12C其实有不少技巧的。\x01",
            "处理得好的话就很简单了。#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #49
        (
            "#12C玲不用担心这种事情的。\x01",
            "玲一直都会幸福的。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #50
        "#12C…………嗯。#0C\x02",
    )

    Jump("loc_1405")

    label("loc_1405")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("阿洁")

    AnonymousTalk(    #51
        (
            "#12C这样就够了。\x01",
            "因为只要玲幸福的话，我也就幸福了。#0C\x02",
        )
    )

    Jump("loc_145C")

    label("loc_145C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS574._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #52
        (
            "#0C卡托鲁是个经常挨打的男孩子。\x01",
            "可能是因为他身材瘦小，\x01",
            "总是被人当玩偶一样耍弄。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #53
        (
            "#12C喂，卡托鲁、卡托鲁啊。\x01",
            "你又被欺负了吗？#0C\x02",
        )
    )

    Jump("loc_15BC")

    label("loc_15BC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("卡托鲁")

    AnonymousTalk(    #54
        (
            "#12C嗯、嗯……\x01",
            "搞不懂……#0C\x02",
        )
    )

    Jump("loc_15FE")

    label("loc_15FE")

    CloseMessageWindow()

    AnonymousTalk(    #55
        (
            "#12C说是新的游戏。\x01",
            "我完全搞不懂啊……#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #56
        "#12C…………………………………#0C\x02",
    )

    Jump("loc_166E")

    label("loc_166E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("卡托鲁")

    AnonymousTalk(    #57
        (
            "#12C啊，没关系的，玲。\x01",
            "我没事，一点事都没有啦。#0C\x02",
        )
    )

    Jump("loc_16C6")

    label("loc_16C6")

    CloseMessageWindow()

    AnonymousTalk(    #58
        (
            "#12C这是常有的事，我一点也不觉得痛的。\x01",
            "有玲在我就完全不觉得痛苦。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #59
        (
            "#0C卡托鲁总是在\x01",
            "别人看不到的地方流血。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #60
        "#0C我想，这可能也是一种魔咒。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #61
        "#0C美丽的人，一定会流出美丽的血。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0xFEC0, 0xFE20, 0x140, 0x0, 0x140, 0x1E0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS575._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #62
        (
            "#12C我回来了，玲。\x01",
            "这次稍微晚了一会儿。#0C\x02",
        )
    )

    Jump("loc_18AD")

    label("loc_18AD")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        (
            "#0C还有克洛斯。\x01",
            "他是我们的领袖。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS572._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS573._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS574._CH")
    OP_C6(0x0, 0x1, 800, 800, 0)
    OP_C6(0x2, 0x1, 600, 600, 0)
    OP_C6(0x3, 0x1, 700, 700, 0)
    OP_C6(0x4, 0x1, 500, 500, 0)
    OP_C6(0x2, 0x0, 300000, 200000, 0)
    OP_C6(0x3, 0x0, -120000, 150000, 0)
    OP_C6(0x4, 0x0, 50000, 250000, 0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    Sleep(1000)
    OP_C6(0x3, 0x3, -1, 1000, 0)
    Sleep(500)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(500)
    OP_C6(0x4, 0x3, -1, 1000, 0)
    Sleep(500)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    OP_C6(0x2, 0x3, -7829368, 500, 0)
    OP_C6(0x3, 0x3, -7829368, 500, 0)
    OP_C6(0x4, 0x3, -7829368, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #64
        (
            "#0C克洛斯、艾塔、阿洁、卡托鲁，\x01",
            "还有我——玲……#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #65
        (
            "#0C我们都是住在同一个房间，\x01",
            "是无可替代的伙伴……#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #66
        (
            "#0C好像还有些其他的孩子在这里工作，\x01",
            "不过那些人都无所谓。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #67
        "#0C只有我们五个人住在乐园里。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 8947848, 2000, 0)
    OP_C6(0x1, 0x3, 8947848, 2000, 0)
    OP_C6(0x2, 0x3, 8947848, 2000, 0)
    OP_C6(0x3, 0x3, 8947848, 2000, 0)
    OP_C6(0x4, 0x3, 8947848, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x0, 0x3, 0x3)
    OP_C7(0x0, 0x4, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_35C end

    def Function_4_1C58(): pass

    label("Function_4_1C58")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #68 op#A op#5
        "#20A#0C#4S２．公主殿下#0C\x05\x02",
    )

    Sleep(2000)
    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(500)
    OP_1D(0xB7)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS570._CH")
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    Sleep(500)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #69
        "#12C克洛斯，其他人呢？#0C\x02",
    )

    Jump("loc_1D78")

    label("loc_1D78")

    CloseMessageWindow()

    AnonymousTalk(    #70
        (
            "#12C为什么屋子里\x01",
            "只有玲和克洛斯啊？#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0xFEC0, 0xFE20, 0x140, 0x0, 0x140, 0x1E0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS575._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #71
        "#12C啊哈哈，你说什么呢，玲。#0C\x02",
    )

    Jump("loc_1E41")

    label("loc_1E41")

    CloseMessageWindow()

    AnonymousTalk(    #72
        (
            "#12C这里一开始就只有我们俩。\x01",
            "只有我们俩住在这里啊。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #73
        "#12C……是，是吗……#0C\x02",
    )

    Jump("loc_1EB5")

    label("loc_1EB5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #74
        (
            "#12C是啊。\x01",
            "从一开始，这里就是只有我们的世界啊。#0C\x02",
        )
    )

    Jump("loc_1F0D")

    label("loc_1F0D")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #75
        (
            "#0C后来我才发觉，\x01",
            "是克洛斯把其他人藏起来了。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #76
        (
            "#0C是为了不让我担心，\x01",
            "或者是因为现在的情况已不容我正视。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #77
        (
            "#0C克洛斯总是遮蔽我的视线，\x01",
            "注意着不让我看到任何东西。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS573._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, 290, -1, -1)
    SetChrName("艾塔")

    AnonymousTalk(    #78
        (
            "#12C玲，我教你点好东西。\x01",
            "叫做『好，非常乐意』。#0C\x02",
        )
    )

    Jump("loc_20CB")

    label("loc_20CB")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #79
        (
            "#12C这样对方就会非常高兴了。\x01",
            "『好，非常乐意』\x01",
            "『好，非常乐意』#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #80
        (
            "#12C无论被怎样对待都要说『好，非常乐意』，\x01",
            "这样大家都会很高兴的。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #81
        (
            "#12C嘻嘻，很奇怪吧？\x01",
            "高兴的明明只有客人嘛。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS572._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("阿洁")

    AnonymousTalk(    #82
        (
            "#12C我也再教你一个。\x01",
            "这可是珍藏的秘诀。#0C\x02",
        )
    )

    Jump("loc_2245")

    label("loc_2245")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #83
        (
            "#12C就是呀，要想像对方的感觉。\x01",
            "对方一定很舒服啦，\x01",
            "现在一定很有感觉啦，等等。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #84
        (
            "#12C虽然疼痛无法忍耐，\x01",
            "但讨厌的感觉就会消失了。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #85
        (
            "#12C不能勉强乱来。\x01",
            "怎样做对方才会高兴，\x01",
            "一定要好好考虑。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS574._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("卡托鲁")

    AnonymousTalk(    #86
        "#12C那，我、我也说说……#0C\x02",
    )

    Jump("loc_23BE")

    label("loc_23BE")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #87
        (
            "#12C那就是，绝对不能说声『对不起』\x01",
            "然后就哭起来。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #88
        (
            "#12C一说『对不起』，\x01",
            "就会更加被欺负。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #89
        (
            "#12C无论多疼痛多伤心都不能哭。\x01",
            "因为就算说『对不起』\x01",
            "也不会得到原谅的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C6(0x1, 0x3, 16777215, 2000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS592._CH")
    OP_C6(0x0, 0x3, -1, 1500, 0)
    Sleep(2500)
    SetMessageWindowPos(-1, 330, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #90
        (
            "#12C大家，谢谢你们。\x01",
            "不过玲应该不需要这些的。#0C\x02",
        )
    )

    Jump("loc_253A")

    label("loc_253A")

    CloseMessageWindow()

    AnonymousTalk(    #91
        "#12C玲都没有工作嘛。#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #92
        (
            "#12C总是在这里抱着娃娃。\x01",
            "玲要一直待在这里。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 80, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #93
        "#12C是呢，玲。#0C\x02",
    )

    Jump("loc_25CC")

    label("loc_25CC")

    CloseMessageWindow()

    AnonymousTalk(    #94
        (
            "#12C你是我们的公主殿下。\x01",
            "是最重要最重要的人。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #95
        (
            "#12C#40W我们会守护你。\x01",
            "所以你不用看任何东西。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #96
        "#12C#40W『玲』#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C7(0x1, 0xFF, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_1C58 end

    def Function_5_26AD(): pass

    label("Function_5_26AD")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #97 op#A op#5
        "#20A#0C#4S３．游戏#0C\x05\x02",
    )

    Sleep(2000)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_1D(0xAE)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS570._CH")
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS575._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #98
        "#12C玲，你在干什么？#0C\x02",
    )

    Jump("loc_2819")

    label("loc_2819")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #99
        "#12C画画啦。#0C\x02",
    )

    Jump("loc_2845")

    label("loc_2845")

    CloseMessageWindow()

    AnonymousTalk(    #100
        (
            "#12C看，这是怪兽。\x01",
            "把我们关起来的怪兽哦。#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #101
        (
            "#12C金色的眼睛漆黑的鳞。\x01",
            "嘴巴被那些被它吃掉的人\x01",
            "的血染红了。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #102
        "#12C罪恶的颜色吗。画得真棒。#0C\x02",
    )

    Jump("loc_290B")

    label("loc_290B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #103
        (
            "#12C不过肚子一定是纯白色的。\x01",
            "不然的话就不知道\x01",
            "哪边是前面了。#0C\x02",
        )
    )

    Jump("loc_2967")

    label("loc_2967")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #104
        (
            "#12C哈哈，是啊。\x01",
            "肚子一定是纯白色的呢。#0C\x02",
        )
    )

    Jump("loc_29B7")

    label("loc_29B7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #105
        "#12C………………？#0C\x02",
    )

    Jump("loc_29E9")

    label("loc_29E9")

    CloseMessageWindow()

    AnonymousTalk(    #106
        (
            "#12C对了克洛斯。其他人呢？\x01",
            "大家都去工作了吗？#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #107
        "#12C……玲。#0C\x02",
    )

    Jump("loc_2A59")

    label("loc_2A59")

    CloseMessageWindow()

    AnonymousTalk(    #108
        (
            "#12C这里一开始就只有我们俩。\x01",
            "只有我们俩住在这里啊。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x0, 0x0, 0xB)
    PlayEffect(0xCB, 0x3, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #109
        "#12C……是这样吗……#0C\x02",
    )

    Jump("loc_2B0E")

    label("loc_2B0E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #110
        (
            "#12C是啊。\x01",
            "从一开始，这里就是只有我们的世界啊。#0C\x02",
        )
    )

    Jump("loc_2B66")

    label("loc_2B66")

    CloseMessageWindow()

    AnonymousTalk(    #111
        (
            "#12C这里只有我们两个人。\x01",
            "来，继续画画吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #112
        "#12C接下来就画公主殿下的画吧。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #113
        (
            "#0C克洛斯虽然很擅长隐瞒，\x01",
            "但我还是渐渐看到了一些东西。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #114
        (
            "#0C克洛斯好像累了。\x01",
            "这也是因为『其他人』都不见了的缘故吗。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #115
        (
            "#0C所有的工作都由克洛斯一个人承担了。\x01",
            "而克洛斯，也开始渐渐地消失了。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C7(0x1, 0xFF, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x19, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS578._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x19, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS580._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x19, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS579._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS570._CH")
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C6(0x3, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #116
        (
            "#12C玲，我来帮你擦拭身体吧。\x01",
            "今天脏得这么厉害啊。#0C\x02",
        )
    )

    Jump("loc_2E38")

    label("loc_2E38")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 330, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #117
        (
            "#12C谢谢你经常照顾我。\x01",
            "克洛斯好温柔。#0C\x02",
        )
    )

    Jump("loc_2E7D")

    label("loc_2E7D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #118
        "#12C……玲。#0C\x02",
    )

    Jump("loc_2EB2")

    label("loc_2EB2")

    CloseMessageWindow()

    AnonymousTalk(    #119
        (
            "#12C对不起，玲。\x01",
            "都怪我做得不好。#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #120
        "#12C明明决定要守护你的……#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 330, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #121
        (
            "#12C克洛斯？　……怎么了？\x01",
            "你脸色好差哦？#0C\x02",
        )
    )

    Jump("loc_2F73")

    label("loc_2F73")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #122
        (
            "#12C没什么。\x01",
            "没什么啦。#0C\x02",
        )
    )

    Jump("loc_2FB3")

    label("loc_2FB3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 330, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #123
        "#12C…………克洛斯？#0C\x02",
    )

    Jump("loc_2FE7")

    label("loc_2FE7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #124
        "#12C………………。#0C\x02",
    )

    Jump("loc_3022")

    label("loc_3022")

    CloseMessageWindow()

    AnonymousTalk(    #125
        "#12C我说了，什么事也没有！#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #126
        "#12C#40W…………都是你不好。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 330, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #127
        "#12C…………克洛斯……#0C\x02",
    )

    Jump("loc_30CB")

    label("loc_30CB")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #128
        (
            "#12C#40W都是你不好。\x01",
            "一切的一切，都是因为你。#0C\x02",
        )
    )

    Jump("loc_3126")

    label("loc_3126")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(800)
    SetMessageWindowPos(50, 120, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #129
        (
            "#12C#40W其他人很快就被杀了。\x01",
            "为什么只有我还活着啊。#0C\x02",
        )
    )

    Jump("loc_3187")

    label("loc_3187")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(800)
    SetMessageWindowPos(-1, 200, -1, -1)
    SetChrName("克洛斯")

    AnonymousTalk(    #130
        (
            "#2C都是你不好。都怪你没有杀了我。\x01",
            "都是你不好。都怪你没有杀了我。\x01",
            "都是你不好。都怪你没有杀了我。#0C\x02",
        )
    )

    Jump("loc_3214")

    label("loc_3214")

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x2, 0x3)
    OP_20(0xBB8)
    OP_21()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #131
        "#2C#40W我明明已经，死了很久了。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    OP_C7(0x1, 0xFF, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_26AD end

    def Function_6_32BC(): pass

    label("Function_6_32BC")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #132 op#A op#5
        "#20A#0C#4S４．玲#0C\x05\x02",
    )

    Sleep(2000)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #133
        "#0C然后，『第一件工作』来了。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #134
        (
            "#0C这里，已经没有任何人了。\x01",
            "没有任何人可以代替我去了。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #135
        (
            "#0C所以玲必须去工作了。\x01",
            "……玲第一次，来到外面。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_1D(0xAF)
    Sleep(500)
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS571._CH")
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x32, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS580._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x32, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS577._CH")
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C6(0x2, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(60, 60, -1, -1)
    SetChrName("主管人")

    AnonymousTalk(    #136
        (
            "#12C玲，到你出场了。\x01",
            "别对客人无礼啊。#0C\x02",
        )
    )

    Jump("loc_3526")

    label("loc_3526")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #137
        "#12C……………………………#0C\x02",
    )

    Jump("loc_3560")

    label("loc_3560")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 60, -1, -1)
    SetChrName("主管人")

    AnonymousTalk(    #138
        (
            "#12C怎么了，玲。\x01",
            "就和平时一样做啊。#0C\x02",
        )
    )

    Jump("loc_35AC")

    label("loc_35AC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #139
        "#12C……………………………#0C\x02",
    )

    Jump("loc_35E6")

    label("loc_35E6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 50, -1, -1)
    SetChrName("客人")

    AnonymousTalk(    #140
        (
            "#12C喂，怎么和宣传说的不一样啊。\x01",
            "１５号不是最特别的吗？#0C\x02",
        )
    )

    Jump("loc_3641")

    label("loc_3641")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 60, -1, -1)
    SetChrName("主管人")

    AnonymousTalk(    #141
        (
            "#12C真奇怪。\x01",
            "平时真得是很乖的孩子啊。#0C\x02",
        )
    )

    Jump("loc_368F")

    label("loc_368F")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #142
        (
            "#12C能满足客人们的任何要求，\x01",
            "是珍藏的天使哦。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #143
        (
            "#12C喂，玲，快打招呼啊。\x01",
            "就像平时那样。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #144
        (
            "#12C今天要扮演哪个角色呢？\x01",
            "楚楚可怜的人偶？\x01",
            "还是酷酷的男孩子？#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #145
        "#12C……不是我。#0C\x02",
    )

    Jump("loc_377E")

    label("loc_377E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 60, -1, -1)
    SetChrName("主管人")

    AnonymousTalk(    #146
        "#12C咦……？#0C\x02",
    )

    Jump("loc_37B3")

    label("loc_37B3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #147
        (
            "#12C不是我。\x01",
            "不是我。#0C\x02",
        )
    )

    Jump("loc_37E8")

    label("loc_37E8")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 350, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #148
        "#12C#3S不是我、不是我！#2S#0C\x02",
    )

    Jump("loc_3845")

    label("loc_3845")

    CloseMessageWindow()

    AnonymousTalk(    #149
        "#12C#3S那不是我！#2S#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #150
        "#12C#3S那不是我啊！！#2S#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_82(0x0, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #151
        (
            "#0C#40W有人在说着什么。我和平常一样塞住耳朵。\x01",
            "有人在做着什么。我和平常一样闭上眼睛。\x01",
            "我就和平常一样。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #152
        (
            "#0C#60W我就和平常一样。\x01",
            "我就和平常一样。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #153
        "#0C#80W我就和平常一样，去工作了。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x165, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #154
        "#0C啊啊，是生命之水。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #155
        (
            "#0C克洛斯说过。\x01",
            "即使快死的人喝了也能恢复精神。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #156
        (
            "#0C克洛斯经常喝的。\x01",
            "有着非常甜美、蜜糖一般的味道……#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    Sleep(1000)
    SetMessageWindowPos(80, 110, -1, -1)
    SetChrName("主管人")

    AnonymousTalk(    #157
        (
            "#12C来，玲。\x01",
            "今天放了很多蜜糖哦。#0C\x02",
        )
    )

    Jump("loc_3AF5")

    label("loc_3AF5")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #158
        (
            "#12C慢慢喝掉吧。\x01",
            "慢慢地慢慢地，对了对了。\x01",
            "别洒出来哦。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #159
        "#12C慢慢喝掉，一点也别剩下哦。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #160
        "#12C……那么，请慢用。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #161
        (
            "#0C#40W主管人离开的时候，头好像偏了一下。\x01",
            "是因为上了年纪呢，还是想故意掩饰什么。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #162
        "#0C#60W…………啊啊，药起效了。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_43(0x10, 0x3, 0x0, 0xE)
    FadeToBright(3000, 16777215)
    OP_C6(0x2, 0x3, -1, 3000, 0)
    Sleep(1000)
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    OP_C7(0x0, 0x2, 0x3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    SetMessageWindowPos(330, 100, -1, -1)
    SetChrName("客人")

    AnonymousTalk(    #163
        (
            "#12C来，小玲。\x01",
            "我们坐下谈谈吧。#0C\x02",
        )
    )

    Jump("loc_3CE1")

    label("loc_3CE1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #164
        "#12C好，非常乐意。#0C\x02",
    )

    Jump("loc_3D13")

    label("loc_3D13")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 80, -1, -1)
    SetChrName("客人")

    AnonymousTalk(    #165
        "#12C嗯嗯，回答得非常好。#0C\x02",
    )

    Jump("loc_3D4F")

    label("loc_3D4F")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #166
        "#0C#40W好，非常乐意。#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #167
        "#0C#40W好，非常乐意。#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #168
        (
            "#0C好，非常乐意。好，非常乐意。\x01",
            "好，非常乐意。好，非常乐意。\x01",
            "好，非常乐意。好，非常乐意。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x13, 0x0, 0x0, 0xA)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #169
        (
            "#50W#0C早上好，玲。今天也是好天气呢。\x01",
            "#40W不过这里有些通风不畅。开开窗户吧！\x01",
            "#30W我说，玲。一起玩吧？\x01",
            "#20W我也想玩洋娃娃呢～。今天休息啊。\x01",
            "#10W因为克洛斯去做了嘛。\x01",
            "嘻嘻，那孩子最近被指名的次数增加了哦。\x01",
            "是不是社会性需要呢。玲，我教你点好\x01",
            "东西。叫做『好，非常乐意』。\x01",
            "这样对方就会非常高兴了。\x01",
            "『好，非常乐意』『好，非常乐意』\x01",
            "无论被怎样对待都要说『好，非常乐意』。\x01",
            "这样大家都会很高兴的。嘻嘻，\x01",
            "很奇怪吧？高兴的明明只有客人嘛。\x01",
            "我们会守护你。所以你不用看\x01",
            "任何东西。         『玲』 \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #170
        (
            "#50W#0C没关系。玲不用介意的。其实有\x01",
            "#40W不少技巧的。处理得好的话就很\x01",
            "#30W简单了。玲不用担心这种事情的。\x01",
            "#20W玲一直都会幸福的。这样就够了。\x01",
            "#10W因为只要玲幸福的话，我也就幸福了。\x01",
            "我也再教你一个。这可是珍藏的秘诀。\x01",
            "就是呀，要想像对方的感觉。对方一定\x01",
            "很舒服啦，现在一定很有感觉啦，等等。\x01",
            "虽然疼痛无法忍耐，但讨厌的感觉\x01",
            "就会消失了。不能勉强乱来。\x01",
            "怎样做对方才会高兴，一定要好好考虑。\x01",
            "我们会守护你。所以你不用看\x01",
            "任何东西。          『玲』\x01",
            "　\x02",
        )
    )

    Jump("loc_41FF")

    label("loc_41FF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #171
        (
            "#50W#0C嗯、嗯……搞不懂……说是\x01",
            "#40W新的游戏。我完全搞不懂啊……\x01",
            "#30W啊，没关系的，玲。我没事。\x01",
            "#20W一点事都没有啦。这是常有的事，\x01",
            "#10W我一点也不觉得痛的。有玲在我就\x01",
            "完全不觉得痛苦。那，我、我也\x01",
            "说说……那就是，绝对不能说声\x01",
            "『对不起』然后就哭起来。一说\x01",
            "『对不起』，就会更加被欺负。\x01",
            "无论多疼痛多伤心都不能哭。因\x01",
            "为就算说『对不起』也不会得到\x01",
            "原谅的。我们会守护你。所以你\x01",
            "不用看任何东西。      『玲』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #172
        (
            "#40W#0C玲，你在干什么？罪恶的颜色吗。\x01",
            "#30W画得真棒。哈哈，是啊。肚子一定\x01",
            "#20W是纯白色的呢。……玲。这里一开\x01",
            "#10W始就只有我们俩。只有我们俩住在\x01",
            "这里啊。是啊。从一开始，就是只\x01",
            "有我们的世界啊。这里只有我们两\x01",
            "#5W个人。来，继续画画吧。…………\x01",
            "#5W………。我说了，什么事也没有！\x01",
            "…………都是你不好。都是你不好。\x01",
            "一切的一切，都是因为你。其他人\x01",
            "很快就被杀了。为什么只有我还活\x01",
            "着啊。都是你不好。都怪你没有杀了\x01",
            "我。都是你不好。都怪你没有杀了我。\x01",
            "都是你不好。都怪你没有杀了我。我\x01",
            "明明已经，死了很久了。#60W  『玲』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_23(0x18E)
    OP_82(0x0, 0x0)
    OP_44(0x13, 0x0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #173
        "#2C大家，都不见了呢。#0C\x02",
    )

    Jump("loc_460C")

    label("loc_460C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xC1, 0x0, 0x64)
    OP_C6(0x2, 0x3, 16777215, 100, 0)
    Sleep(2000)
    OP_C7(0x1, 0xFF, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_32BC end

    def Function_7_4637(): pass

    label("Function_7_4637")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    Sleep(500)
    OP_22(0x87, 0x0, 0x64)
    Sleep(2000)
    OP_43(0x10, 0x1, 0x0, 0x17)
    Sleep(2000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS581._CH")
    OP_C6(0x0, 0x3, -1, 1500, 0)
    OP_43(0x10, 0x3, 0x0, 0xE)
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    PlayEffect(0xC9, 0x1, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 5000)
    OP_E7(0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0)
    OP_E7(0x0, 0x1, 0xFF, 0xFF, 0xFF, 0xFF, 1500)
    Sleep(1000)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(500)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x10, 0x1)
    OP_22(0x226, 0x0, 0x64)
    Sleep(800)
    OP_22(0x38F, 0x0, 0x64)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(300)
    OP_22(0x389, 0x0, 0x64)
    Sleep(500)
    OP_22(0x38F, 0x0, 0x64)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x226, 0x0, 0x64)
    Sleep(500)
    OP_22(0x389, 0x0, 0x64)
    Sleep(800)
    OP_22(0x38F, 0x0, 0x64)
    Sleep(300)
    OP_22(0x38F, 0x0, 0x64)
    Sleep(500)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(300)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_E7(0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 1000)
    OP_C7(0x0, 0x0, 0x3)
    OP_24(0x87, 0x5F)
    Sleep(100)
    OP_24(0x87, 0x5A)
    Sleep(100)
    OP_24(0x87, 0x55)
    Sleep(100)
    OP_24(0x87, 0x50)
    Sleep(100)
    OP_24(0x87, 0x4B)
    Sleep(100)
    OP_24(0x87, 0x46)
    Sleep(1500)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS582._CH")
    OP_C6(0x0, 0x3, -8947849, 2000, 0)
    OP_82(0x1, 0x0)
    PlayEffect(0xCA, 0x1, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 5000)
    OP_E7(0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0)
    OP_E7(0x0, 0x1, 0xFF, 0xFF, 0xFF, 0xFF, 1500)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(380, 220, -1, -1)
    SetChrName("银发的青年")

    AnonymousTalk(    #174
        "#12C这是……#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #175
        "#12C……那些卑鄙的家伙。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 350, -1, -1)
    SetChrName("黑发的少年")

    AnonymousTalk(    #176
        "#12C………………………………#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #177
        (
            "#12C……即使变成这样，\x01",
            "人还能继续生存下去吗……？#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #178
        (
            "#12C…………变成这样，\x01",
            "还能称之为活着吗……？#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 220, -1, -1)
    SetChrName("银发的青年")

    AnonymousTalk(    #179
        "#12C………………………………#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #180
        (
            "#12C……这无数的十字伤\x01",
            "应该都是自己划下的。#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #181
        (
            "#12C恐怕只有这样，\x01",
            "才能够保持自我吧。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 350, -1, -1)
    SetChrName("黑发的少年")

    AnonymousTalk(    #182
        "#12C………………………………#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #183
        "#12C……即使如此，还是想生存下去吗……#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #184
        "#12C（这就是，活着的人……）#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x0, 0x3, 16777215, 3000, 0)

    def lambda_4B25():
        OP_E7(0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_4B25)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_22(0x166, 0x0, 0x64)
    OP_24(0x87, 0x3C)
    Sleep(100)
    OP_24(0x87, 0x32)
    Sleep(100)
    OP_24(0x87, 0x28)
    Sleep(100)
    OP_24(0x87, 0x1E)
    Sleep(100)
    OP_24(0x87, 0x19)
    Sleep(100)
    OP_24(0x87, 0xA)
    Sleep(100)
    OP_23(0x87)
    Sleep(7000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("黑发的少年")

    AnonymousTalk(    #185
        (
            "#12C……莱维，我想看到\x01",
            "这孩子真正活着的样子。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #186
        "#12C『结社』能接管她吗？#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C7(0x1, 0xFF, 0x0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_4637 end

    def Function_8_4C1A(): pass

    label("Function_8_4C1A")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #187 op#A op#5
        "#20A#0C#4S５．梦的延续#0C\x05\x02",
    )

    Sleep(2000)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_1D(0xB2)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #188
        (
            "#0C#40W玲很强。\x01",
            "有一天约修亚这么说。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #189
        "#0C#40W…………这是我所不知道的话语。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS583._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS584._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS585._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS586._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #190
        "#0C#40W玲很强。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)

    AnonymousTalk(    #191
        "#0C#40W是的。玲很强。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(1000)

    AnonymousTalk(    #192
        (
            "#0C玲很强。玲很强。\x01",
            "玲很强。玲很强。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)

    AnonymousTalk(    #193
        "#0C玲很强。玲是很强的！#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #194
        (
            "#0C执行者候补『玲』\x01",
            "优秀得无与伦比。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x0, 0x3, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #195
        (
            "#0C#40W而不知不觉中，\x01",
            "约修亚不见了。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #196
        "#0C#40W世界，依然不变地转动。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0xE)
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 5000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS587._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS588._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS589._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS590._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS591._CH")
    OP_C6(0x0, 0x3, -1, 1500, 0)
    Sleep(2500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #197
        (
            "#12C呼……约修亚真是的，\x01",
            "跑到哪里去了呢。#0C\x02",
        )
    )

    Jump("loc_513C")

    label("loc_513C")

    CloseMessageWindow()

    AnonymousTalk(    #198
        (
            "#12C虽然说是去工作，\x01",
            "不过怎么花了这么长时间呢。#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #199
        (
            "#12C玲好不容易才当上\x01",
            "正式的『执行者』……#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #200
        (
            "#12C而且……\x01",
            "还想介绍真正的\x01",
            "『爸爸和妈妈』给他……#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #201
        "#12C……………………………#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #202
        "#12C……嘻嘻，不过没关系。#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #203
        "#12C约修亚一定会回来的。#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #204
        (
            "#12C回来以后……\x01",
            "就让他给我讲讲旅行的见闻吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #205
        (
            "#12C是的……\x01",
            "……只要他愿意的话，随时都可以………#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0x9)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(400, 160, -1, -1)
    SetChrName("小婴儿")

    AnonymousTalk(    #206
        "#12C……呜哇………#0C\x02",
    )

    Jump("loc_5345")

    label("loc_5345")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #207
        "#12C呜哇！　呜哇！#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #208
        "#12C…………小婴儿？#0C\x02",
    )

    Jump("loc_539A")

    label("loc_539A")

    CloseMessageWindow()

    AnonymousTalk(    #209
        "#12C嘻嘻，好可爱……#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x10, 0x0, 0x0, 0xB)
    PlayEffect(0xCB, 0x3, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #210
        "#12C#40W……真的，好漂亮呢。#0C\x02",
    )

    Jump("loc_5444")

    label("loc_5444")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #211
        (
            "#0C#40W……这是崭新的生命。\x01",
            "纯白而纯粹，是美丽无比的存在。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #212
        (
            "#0C#40W那孩子一定会是个正直的孩子吧。\x01",
            "会健康成长，成为出色的大人吧。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #213
        "#0C#40W虽然我是不可能了。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #214
        "#0C#40W虽然我已经是不可能的了。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #215
        (
            "#0C#40W不知名的小婴儿，\x01",
            "请你一定要幸福。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_43(0x10, 0x0, 0x0, 0xB)
    PlayEffect(0xCB, 0x3, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    Sleep(500)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #216
        "#12C#40W……………………………………#0C\x02",
    )

    Jump("loc_5637")

    label("loc_5637")

    CloseMessageWindow()
    OP_56(0x0)
    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #217
        (
            "#12C#60W………………………………\x01",
            "……为……什么…………？#0C\x02",
        )
    )

    Jump("loc_569B")

    label("loc_569B")

    CloseMessageWindow()
    OP_56(0x0)
    CloseMessageWindow()
    OP_44(0x10, 0x3)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 1500, 0)
    Sleep(2500)
    SetMessageWindowPos(400, 180, -1, -1)
    SetChrName("似曾相识的男性")

    AnonymousTalk(    #218
        (
            "#12C好可爱呢。\x01",
            "简直长得和你一摸一样。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #219
        "#12C喏～好乖好乖……#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("似曾相识的女性")

    AnonymousTalk(    #220
        (
            "#12C呵呵，\x01",
            "虽然在前一个孩子身上发生了那种事……#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #221
        (
            "#12C不过太好了。\x01",
            "女神并没有\x01",
            "舍弃我们呢。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 180, -1, -1)
    SetChrName("似曾相识的男性")

    AnonymousTalk(    #222
        (
            "#12C喂喂。\x01",
            "不是说好不提那件事的吗？#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #223
        "#12C以前的事情就忘了吧。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("似曾相识的女性")

    AnonymousTalk(    #224
        (
            "#12C嗯嗯……虽然可怜，\x01",
            "但那样做也是为了那孩子好啊。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(230, 220, -1, -1)
    SetChrName("小婴儿")

    AnonymousTalk(    #225
        "#12C呜哇、呜哇……#0C\x02",
    )

    Jump("loc_58D0")

    label("loc_58D0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("似曾相识的女性")

    AnonymousTalk(    #226
        "#12C哦哦～好好，乖宝宝哦～。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -7829368, 500, 0)
    Sleep(800)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #227
        (
            "#0C#40W『玲』\x01",
            "已不再纯洁的孩子。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x1, 0x800)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #228
        (
            "#0C#40W以前的事。\x01",
            "『发生那种事情』的前一个孩子。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #229
        "#0C#40W原来，是这样。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #230
        (
            "#0C#40W玲　原来　是这样的啊。\x01",
            "从一开始就是。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #231
        "#0C#60W玲是#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #232
        (
            "#0C#40W玲是\x01",
            "#40W玲是\x01",
            "#40W玲从#150W　生　下　　来　　就　　　是#0C\x02",
        )
    )

    Jump("loc_5AA6")

    label("loc_5AA6")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(200, 350, -1, -1)
    SetChrName("青年的声音")

    AnonymousTalk(    #233
        "#12C………玲。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x13, 0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 1500, 0)
    Sleep(2500)
    SetMessageWindowPos(380, 250, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #234
        "#12C#40W……啊……………#0C\x02",
    )

    Jump("loc_5B53")

    label("loc_5B53")

    CloseMessageWindow()

    AnonymousTalk(    #235
        "#12C#40W………莱维………#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("剑帝莱维")

    AnonymousTalk(    #236
        "#12C………………………………#0C\x02",
    )

    Jump("loc_5BC4")

    label("loc_5BC4")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #237
        (
            "#12C我们『执行者』\x01",
            "所有的行动都是被允许的。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #238
        (
            "#12C要怎么处置他们……\x01",
            "随你自己的意思就行。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #239
        (
            "#12C虽然，\x01",
            "我怀疑他们是否有值得我们动手的价值……#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x0, 0x3, 0x3)
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #240
        (
            "#0C#40W超然于善恶生死之处，\x01",
            "我淡然走过。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #241
        "#0C#40W无幸无厄。无悲无喜。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #242
        (
            "#0C#40W黑白将我撕裂，天地将我捉弄，\x01",
            "我变得污秽不堪。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #243
        "#0C#40W何处为始，何处为终。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #244
        (
            "#0C#40W我无处容身。\x01",
            "也未曾前行。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #245
        "#0C#40W然而，世界依然转动。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #246
        "#0C#40W在我所不知道的地方，只有世界在……#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #247
        "#0C#40W那么──就这样吧。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #248
        (
            "#0C#40W世界永远\x01",
            "都是为玲而转动的。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #249
        (
            "#0C#40W所以……\x01",
            "没什么好伤心的。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #250
        "#12C……嘻………#0C\x02",
    )

    Jump("loc_5F21")

    label("loc_5F21")

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C6(0x4, 0x4, 0, 0, 0)
    OP_C6(0x4, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(380, 250, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #251
        (
            "#12C嘻嘻……\x01",
            "我才不管那些假货。#0C\x02",
        )
    )

    Jump("loc_5F8A")

    label("loc_5F8A")

    CloseMessageWindow()

    AnonymousTalk(    #252
        "#12C真正的爸爸和妈妈在别的地方呢。#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x4, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x4, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_C4(0x1, 0x10)
    OP_48()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_4C1A end

    def Function_9_6004(): pass

    label("Function_9_6004")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_604C")
    OP_22(0x184, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1100)
    OP_22(0x184, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x64)
    Sleep(1200)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1300)
    Jump("Function_9_6004")

    label("loc_604C")

    Return()

    # Function_9_6004 end

    def Function_10_604D(): pass

    label("Function_10_604D")

    OP_43(0x10, 0x0, 0x0, 0xB)
    PlayEffect(0xCB, 0x3, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2500)

    label("loc_608E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_618D")
    OP_43(0x10, 0x0, 0x0, 0xC)
    PlayEffect(0xCB, 0x3, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_60F2")
    Sleep(250)
    Jump("loc_618A")

    label("loc_60F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6107")
    Sleep(400)
    Jump("loc_618A")

    label("loc_6107")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_611C")
    Sleep(700)
    Jump("loc_618A")

    label("loc_611C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6131")
    Sleep(1000)
    Jump("loc_618A")

    label("loc_6131")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x23), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6146")
    Sleep(1500)
    Jump("loc_618A")

    label("loc_6146")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_615B")
    Sleep(2000)
    Jump("loc_618A")

    label("loc_615B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6170")
    Sleep(3000)
    Jump("loc_618A")

    label("loc_6170")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6185")
    Sleep(4000)
    Jump("loc_618A")

    label("loc_6185")

    Sleep(5000)

    label("loc_618A")

    Jump("loc_608E")

    label("loc_618D")

    Return()

    # Function_10_604D end

    def Function_11_618E(): pass

    label("Function_11_618E")

    OP_22(0x3C0, 0x0, 0x64)
    Sleep(500)
    OP_23(0x3C0)
    Return()

    # Function_11_618E end

    def Function_12_619C(): pass

    label("Function_12_619C")

    OP_22(0x3C0, 0x0, 0x32)
    Sleep(500)
    OP_23(0x3C0)
    Return()

    # Function_12_619C end

    def Function_13_61AA(): pass

    label("Function_13_61AA")

    OP_24(0x18E, 0x5A)
    Sleep(300)
    OP_24(0x18E, 0x50)
    Sleep(300)
    OP_24(0x18E, 0x46)
    Sleep(300)
    OP_24(0x18E, 0x3C)
    Sleep(300)
    OP_24(0x18E, 0x32)
    Sleep(300)
    OP_24(0x18E, 0x28)
    Sleep(300)
    OP_24(0x18E, 0x1E)
    Sleep(300)
    OP_24(0x18E, 0x14)
    Sleep(300)
    OP_24(0x18E, 0xA)
    Sleep(300)
    OP_24(0x18E, 0x0)
    OP_23(0x18E)
    Return()

    # Function_13_61AA end

    def Function_14_6203(): pass

    label("Function_14_6203")

    OP_22(0x18E, 0x1, 0x0)
    OP_24(0x18E, 0x0)
    Sleep(50)
    OP_24(0x18E, 0xA)
    Sleep(50)
    OP_24(0x18E, 0x14)
    Sleep(50)
    OP_24(0x18E, 0x1E)
    Sleep(50)
    OP_24(0x18E, 0x28)
    Sleep(50)
    OP_24(0x18E, 0x32)
    Sleep(50)
    OP_24(0x18E, 0x3C)
    Sleep(50)
    OP_24(0x18E, 0x46)
    Sleep(50)
    OP_24(0x18E, 0x50)
    Sleep(50)
    OP_24(0x18E, 0x5A)
    Sleep(50)
    OP_24(0x18E, 0x64)
    Return()

    # Function_14_6203 end

    def Function_15_6267(): pass

    label("Function_15_6267")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp014_00.eff")
    LoadEffect(0x1, "map\\mp295_00.eff")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, -54650, 100, 42240, 180)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x11, -52420, 100, 44100, 180)
    OP_A1(0x11, 0x0)
    OP_6D(-55520, 100, 44450, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(327000, 0)
    OP_6E(370, 0)
    OP_D8(0x0, 0x1F4)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 520)
    OP_70(0x0, 0x208)
    Sleep(1000)
    PlayEffect(0x0, 0xFF, 0xFF, -54650, 100, 42240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1C9, 0x0, 0x64)
    Sleep(1000)
    FadeToBright(3000, 0)
    OP_6B(2520, 3000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #253
        0x10,
        "#1309F#40W#6P……啊………………\x02",
    )

    CloseMessageWindow()

    def lambda_63BC():
        OP_6B(2320, 30000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_63BC)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x27), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_99(0x10, 0x0, 0x6, 0x3E8)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)
    OP_9E(0x10, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(1000)

    ChrTalk(    #254
        0x10,
        "#268F#6P#40W……好冷………\x02",
    )

    CloseMessageWindow()
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x18D, 0x1, 0x64)
    PlayEffect(0x1, 0x1, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(1000)

    ChrTalk(    #255
        0x10,
        (
            "#264F#6P……………………………………\x02\x03",

            "#261F谢谢，『爸爸、妈妈』。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x11)
    Sleep(1000)
    OP_62(0x10, 0x0, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #256
        0x10,
        (
            "#263F#6P是啊，这也不错。\x01",
            "这也不错嘛。\x02\x03",

            "#265F玲一直都很幸福。\x01",
            "一直都很快乐。\x02\x03",

            "#261F所以玲……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #257
        (
            "#5C世界不是以玲\x01",
            "为中心而转动的。\x02\x03",

            "不会为了玲\x01",
            "而做什么改变。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(100, 250, -1, -1)

    AnonymousTalk(    #258
        (
            "#5C呵呵，这还用说吗。\x01",
            "因为我喜欢玲嘛。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #259
        (
            "#5C我什么也不会说……\x02\x03",

            "……玲就照自己心里\x01",
            "真实的感觉去判断吧。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    SetChrSubChip(0x10, 21)
    LoadEffect(0x1, "map\\mp021_00.eff")
    LoadEffect(0x2, "map\\mp064_01.eff")
    LoadEffect(0x3, "map\\mp065_01.eff")
    LoadEffect(0x4, "map\\mp064_00.eff")
    LoadEffect(0x5, "map\\mp065_00.eff")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #260
        0x10,
        "#1309F#6P……………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x800)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(1500)

    ChrTalk(    #261
        0x10,
        (
            "#1300F#6P……差不多要天亮了呢。\x02\x03",

            "#1302F走吧。\x01",
            "『帕蒂尔·玛蒂尔』。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_44(0x10, 0x2)

    def lambda_68AF():
        OP_6D(-55140, 740, 45990, 5000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_68AF)

    def lambda_68C7():
        OP_6B(2370, 5000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_68C7)

    def lambda_68D7():
        OP_6E(398, 5000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_68D7)
    OP_22(0x113, 0x1, 0x3C)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x11, 0, -800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    Play3DEffect(0x4, 0x1, 0x0, "Frame86__jet_0", 0x0, 0xFFFFFE0C, 0x0, 0x3C, 0xFFA6, 0xB4, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x4, 0x2, 0x0, "Frame87__jet_1", 0x0, 0xFFFFFE0C, 0x0, 0x1E, 0x46, 0xFF4C, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1000)

    def lambda_699A():
        OP_8F(0xFE, 0xFFFF333C, 0x4B0, 0xAC44, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_699A)
    Sleep(500)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 521)
    OP_70(0x0, 0x230)
    OP_73(0x0)
    Fade(500)
    PlayEffect(0x5, 0x1, 0x11, 4950, 2800, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x5, 0x2, 0x11, -4950, 2800, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_D8(0x0, 0x5DC)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 1)
    OP_70(0x0, 0x28)

    def lambda_6A5C():
        OP_8F(0xFE, 0xFFFF333C, 0x64, 0xAC44, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_6A5C)
    WaitChrThread(0x11, 0x0)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_22(0x111, 0x0, 0x64)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x5DC)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 461)
    OP_70(0x0, 0x1E0)
    OP_73(0x0)
    WaitChrThread(0x11, 0x0)
    OP_43(0x10, 0x0, 0x0, 0x10)
    OP_6F(0x0, 401)
    OP_70(0x0, 0x1A4)
    OP_73(0x0)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    ClearChrFlags(0x10, 0x10)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    OP_8C(0x10, 0, 0)
    Sleep(200)
    SetChrSubChip(0x10, 1)
    Sleep(200)

    def lambda_6B25():
        OP_99(0x10, 0x2, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6B25)

    def lambda_6B35():
        OP_6D(-54290, 2720, 43500, 1000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6B35)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x10, 0xFFFF286A, 0xDAC, 0xA47E, 0xFA0, 0x1F40)
    ClearChrFlags(0x10, 0x4)
    OP_CF(0x10, 0x0, "Frame85__ren")
    WaitChrThread(0x10, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_8C(0x10, 315, 400)
    WaitChrThread(0x10, 0x0)
    Sleep(500)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0x11, 4600, 2600, 0, 0, 0, 18, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x11, -4600, 2600, 0, 0, 0, 342, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_6C23():
        OP_6D(-52190, 1000, 47820, 4500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6C23)

    def lambda_6C3B():
        OP_67(0, 6920, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6C3B)

    def lambda_6C53():
        OP_6B(2860, 4500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6C53)

    def lambda_6C63():
        OP_6C(23000, 4500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_6C63)

    def lambda_6C73():
        OP_6E(407, 4500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_6C73)
    OP_43(0x11, 0x0, 0x0, 0x15)

    def lambda_6C8A():
        OP_8F(0xFE, 0xFFFF3062, 0x9C4, 0x9F92, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6C8A)
    Sleep(300)

    def lambda_6CAA():
        OP_8F(0xFE, 0xFFFF3062, 0x9C4, 0x9F92, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6CAA)
    Sleep(300)

    def lambda_6CCA():
        OP_8F(0xFE, 0xFFFF3062, 0x9C4, 0x9F92, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6CCA)
    OP_24(0x113, 0x50)
    Sleep(2000)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x5DC)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x104)
    WaitChrThread(0x12, 0x0)
    Sleep(500)

    ChrTalk(    #262
        0x10,
        (
            "#1304F#5P目的地是克洛斯贝尔……\x02\x03",

            "到达一定高度以后\x01",
            "就关掉推进器\x01",
            "切换到飞翔引擎吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x0, 0x2)
    Sleep(1000)
    OP_24(0x113, 0x5A)
    Sleep(100)
    OP_24(0x113, 0x64)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x11, 0x0)
    Fade(500)
    OP_6D(-62040, 1600, 39420, 0)
    OP_67(0, 4990, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(271000, 0)
    OP_6E(440, 0)

    def lambda_6DE5():
        OP_6B(2890, 8000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6DE5)
    OP_11(0xF0, 0xE6, 0xB4, 0x14C08, 0x21EF8, 0x0)
    OP_0D()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x3E8)
    OP_6F(0x0, 261)
    OP_70(0x0, 0x118)
    OP_22(0x116, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x3E8)
    OP_6F(0x0, 281)
    OP_70(0x0, 0x12C)
    PlayEffect(0x3, 0x0, 0x11, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x11, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x11, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x5, 0x11, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x6, 0x11, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x7, 0x11, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x114, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x0, 0x11, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x11, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x11, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x11, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x11, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0x11, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)

    def lambda_70CA():
        OP_6D(-70410, 6250, 39710, 4000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_70CA)

    def lambda_70E2():
        OP_67(0, 6070, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_70E2)

    def lambda_70FA():
        OP_6B(3440, 6000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_70FA)

    def lambda_710A():
        OP_6C(283000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_710A)

    def lambda_711A():
        OP_6E(420, 6000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_711A)

    def lambda_712A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_712A)
    Sleep(100)

    def lambda_714A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_714A)
    Sleep(100)

    def lambda_716A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_716A)
    Sleep(100)

    def lambda_718A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_718A)
    Sleep(100)

    def lambda_71AA():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_71AA)
    Sleep(100)
    FadeToDark(2000, 0, -1)

    def lambda_71D4():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_71D4)
    Sleep(100)

    def lambda_71F4():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_71F4)
    Sleep(100)

    def lambda_7214():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7214)
    Sleep(100)

    def lambda_7234():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x80E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7234)
    Sleep(100)

    def lambda_7254():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x9470, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7254)
    Sleep(100)

    def lambda_7274():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xA7F8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7274)
    Sleep(100)

    def lambda_7294():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xBB80, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7294)
    OP_0D()
    OP_44(0x11, 0x1)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    OP_43(0x10, 0x0, 0x0, 0x13)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_43(0x10, 0x1, 0x0, 0x14)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #263
        "\x07\x00Episode『乐园的少女』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_738F")
    Sleep(1000)
    OP_28(0xF, 0x4, 0x10)
    OP_28(0xF, 0x4, 0x20)
    OP_3E(0x2E8, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #264
        "\x07\x00得到了\x1F\xE8\x02\x07\x00。\x02",
    )

    Jump("loc_7383")

    label("loc_7383")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_738F")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7313   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_6267 end

    def Function_16_739C(): pass

    label("Function_16_739C")

    OP_8C(0x10, 90, 400)
    Sleep(300)
    OP_8F(0x10, 0xFFFF327E, 0x64, 0xA118, 0x7D0, 0x0)
    Return()

    # Function_16_739C end

    def Function_17_73BD(): pass

    label("Function_17_73BD")

    OP_24(0x18D, 0x5A)
    Sleep(150)
    OP_24(0x18D, 0x50)
    Sleep(150)
    OP_24(0x18D, 0x46)
    Sleep(150)
    OP_24(0x18D, 0x3C)
    Sleep(150)
    OP_24(0x18D, 0x32)
    Sleep(150)
    OP_24(0x18D, 0x28)
    Sleep(150)
    OP_24(0x18D, 0x1E)
    Sleep(150)
    OP_24(0x18D, 0x14)
    Sleep(150)
    OP_24(0x18D, 0xA)
    Sleep(150)
    OP_24(0x18D, 0x0)
    OP_23(0x18D)
    Return()

    # Function_17_73BD end

    def Function_18_7416(): pass

    label("Function_18_7416")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    OP_1D(0x6E)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #265
        (
            "\x07\x05耸立在巨大都市的角落，\x01",
            "地主馆风格的坚实宅邸――\x02\x03",

            "大理石装饰的外表，\x01",
            "沐浴在冰冷的月光下\x01",
            "在幽深的黑暗中熠熠生辉――\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #266
        (
            "\x07\x05这里是某个组织\x01",
            "所运营的黑暗世界的社交场――\x02\x03",

            "白色的牢狱中\x01",
            "囚禁着小男孩少女――\x02\x03",

            "供给怀着无尽欲望者\x01",
            "作为邪恶的飨宴――\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_AD(0x240068, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #267
        (
            "\x07\x05承受着肉体、精神的沉重，\x01",
            "许多孩子都日渐衰弱――\x02\x03",

            "但其中有一位少女，保持了精神上的平衡\x01",
            "熬过了苦难的岁月――\x02\x03",

            "不过才5岁的少女，\x01",
            "也是被父母舍弃来到馆邸的\x01",
            "可怜人之一。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #268
        (
            "\x07\x05然后，随着黑暗降临\x01",
            "馆邸的门扉再度开启――\x02\x03",

            "政府高官乘坐的马车，\x01",
            "横在宅邸之前。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xFA, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(300, 250, -1, -1)
    SetChrName("主管人")

    AnonymousTalk(    #269
        (
            "\x07\x00阁下……\x01",
            "好久不见。\x02",
        )
    )

    Jump("loc_76CF")

    label("loc_76CF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 100, -1, -1)
    SetChrName("高官")

    AnonymousTalk(    #270
        (
            "\x07\x00唔……马上带路。\x02\x03",

            "主管人啊……\x01",
            "今晚心情特别好。\x02\x03",

            "因为我期待着\x01",
            "特别的招待呢。\x02",
        )
    )

    Jump("loc_773E")

    label("loc_773E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 250, -1, -1)
    SetChrName("主管人")

    AnonymousTalk(    #271
        "\x07\x00是，我明白了\x02",
    )

    Jump("loc_776E")

    label("loc_776E")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1500)
    SetMessageWindowPos(200, 200, -1, -1)
    SetChrName("主管人")

    AnonymousTalk(    #272
        (
            "\x07\x00来，玲……\x02\x03",

            "……向你最喜欢的\x01",
            "叔叔打声招呼吧。\x02",
        )
    )

    Jump("loc_77D0")

    label("loc_77D0")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS303._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #273
        "\x07\x00………………………………\x02",
    )

    Jump("loc_7856")

    label("loc_7856")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 60, -1, -1)
    SetChrName("高官")

    AnonymousTalk(    #274
        (
            "\x07\x00哦哦……\x01",
            "这真是太棒了……\x02\x03",

            "来，玲……\x01",
            "来这边吧。\x02\x03",

            "这可爱的脸蛋\x01",
            "可要让我好好看看。\x02",
        )
    )

    Jump("loc_78D6")

    label("loc_78D6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #275
        "\x07\x00………………………………\x02",
    )

    Jump("loc_7908")

    label("loc_7908")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 60, -1, -1)
    SetChrName("高官")

    AnonymousTalk(    #276
        (
            "\x07\x00呼呼呼……\x01",
            "没什么好怕的。\x02\x03",

            "只要忍耐一小会儿，\x01",
            "乖乖待着就行……\x02\x03",

            "那样的话\x01",
            "下次睁开眼睛的时候……\x02\x03",

            "……所有的一切，\x01",
            "都会结束了。\x02",
        )
    )

    Jump("loc_79B7")

    label("loc_79B7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #277
        "\x07\x00咦……！？\x02",
    )

    Jump("loc_79DB")

    label("loc_79DB")

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    OP_22(0x245, 0x0, 0x64)
    OP_22(0x22C, 0x0, 0x64)
    OP_C6(0x0, 0x0, 0, 10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x0, 0, -10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x0, 0, 10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x0, 0, -10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x0, 0, 10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x0, 0, -10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x3, 16777215, 200, 0)
    Sleep(1000)
    OP_1D(0x29)
    OP_43(0x0, 0x1, 0x0, 0x17)
    Sleep(1000)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(500)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x0, 0x1)
    OP_22(0x226, 0x0, 0x64)
    Sleep(800)
    OP_22(0x38F, 0x0, 0x64)
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("男人的惨叫")

    AnonymousTalk(    #278
        "\x07\x00#3S啊啊！　\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(300)
    OP_22(0x389, 0x0, 0x64)
    Sleep(500)
    OP_22(0x38F, 0x0, 0x64)
    SetMessageWindowPos(100, 250, -1, -1)
    SetChrName("男人的惨叫")

    AnonymousTalk(    #279
        "\x07\x00#3S呜哇！！　\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x87, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(200, 200, -1, -1)
    SetChrName("主管人")

    AnonymousTalk(    #280
        "\x07\x00怎、怎么了！？\x02",
    )

    Jump("loc_7B5A")

    label("loc_7B5A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 80, -1, -1)
    SetChrName("高官")

    AnonymousTalk(    #281
        "\x07\x00发生了什么事……\x02",
    )

    Jump("loc_7B89")

    label("loc_7B89")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(200, 80, -1, -1)
    SetChrName("高官")

    AnonymousTalk(    #282
        "\x07\x00#3S……呜、呜！！\x02",
    )

    Jump("loc_7BBE")

    label("loc_7BBE")

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x226, 0x0, 0x64)
    Sleep(500)
    OP_22(0x389, 0x0, 0x64)
    Sleep(800)
    OP_22(0x38F, 0x0, 0x64)
    Sleep(300)
    OP_22(0x38F, 0x0, 0x64)
    Sleep(500)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(300)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(1000)
    OP_AE(0x5DC)
    Sleep(500)
    OP_AD(0x24006A, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #283
        (
            "\x07\x00……又肥又胖的猪。\x02\x03",

            "不仅是样子丑陋，\x01",
            "连叫声都那么难听……\x02",
        )
    )

    Jump("loc_7C70")

    label("loc_7C70")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 180, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #284
        (
            "\x07\x00……一楼处理完了。\x02\x03",

            "剩下的敌人团体\x01",
            "好像撤退到2楼了。\x02",
        )
    )

    Jump("loc_7CCA")

    label("loc_7CCA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #285
        (
            "\x07\x00瓮中之鳖啊……\x02\x03",

            "……麻烦带路。\x02",
        )
    )

    Jump("loc_7D09")

    label("loc_7D09")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 180, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #286
        "\x07\x00明白……　　\x02",
    )

    Jump("loc_7D39")

    label("loc_7D39")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(2000)
    OP_20(0x7D0)
    OP_24(0x87, 0x5A)
    Sleep(150)
    OP_24(0x87, 0x50)
    Sleep(150)
    OP_24(0x87, 0x46)
    Sleep(150)
    OP_24(0x87, 0x3C)
    Sleep(150)
    OP_24(0x87, 0x32)
    Sleep(150)
    OP_24(0x87, 0x28)
    Sleep(150)
    OP_24(0x87, 0x1E)
    Sleep(150)
    OP_24(0x87, 0x14)
    Sleep(150)
    OP_24(0x87, 0xA)
    Sleep(150)
    OP_24(0x87, 0x0)
    OP_23(0x87)
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #287
        (
            "\x07\x05袭击馆邸的，\x01",
            "是『结社』所属的两名战斗人员。\x02\x03",

            "光凭这两人\x01",
            "就将组织的人杀个片甲不留。\x02\x03",

            "作为对黑暗街市的示威\x01",
            "『结社』进行了敌对势力的排除――\x02\x03",

            "――由于馆邸是其对象\x01",
            "少女勉强得以幸存。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    OP_1D(0x73)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #288
        (
            "\x07\x05被『结社』接收的少女\x01",
            "在各方面都发挥出惊人的才能――\x02\x03",

            "很快就作为干部候补\x01",
            "接受了正式的训练。\x02\x03",

            "从那地狱将其救出的\x01",
            "约修亚和莱维成为其兄长。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #289
        (
            "\x07\x05约修亚因为特殊任务\x01",
            "长期离开『结社』――\x02\x03",

            "消息传来时，\x01",
            "少女才刚刚\x01",
            "投身『结社』不久。\x02\x03",

            "心中怀着一缕寂寥，\x01",
            "她时隔多日再度来到城市。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x24006B, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #290
        (
            "\x07\x05此时映入\x01",
            "少女眼帘的――\x02\x03",

            "消息传来时，\x01",
            "是抱着刚刚出生的婴儿，\x01",
            "似曾相识的男女的身影。\x02",
        )
    )

    Jump("loc_803C")

    label("loc_803C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #291
        (
            "\x07\x00………………………………\x02\x03",

            "……爸……爸……妈妈……\x02",
        )
    )

    Jump("loc_808A")

    label("loc_808A")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(400, 80, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #292
        (
            "\x07\x00那么……\x01",
            "你打算怎么办？\x02",
        )
    )

    Jump("loc_80D1")

    label("loc_80D1")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS306._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS348._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1000)
    SetMessageWindowPos(380, 60, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #293
        "\x07\x00莱维……\x02",
    )

    Jump("loc_8184")

    label("loc_8184")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 200, -1, -1)
    SetChrName("莱维")

    AnonymousTalk(    #294
        (
            "\x07\x00虽然有没有被杀的价值还是个问题……\x02\x03",

            "要怎么处理他们\x01",
            "是你的自由……\x02",
        )
    )

    Jump("loc_81E6")

    label("loc_81E6")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(350, 60, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #295
        (
            "\x07\x00……不，算了。\x02\x03",

            "那些假货\x01",
            "怎样都无所谓。\x02\x03",

            "真正的爸爸和妈妈\x01",
            "在别的地方呢。\x02",
        )
    )

    Jump("loc_8280")

    label("loc_8280")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_20(0x7D0)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C7(0x1, 0xFF, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -54650, 100, 42240, 180)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x11, -52420, 100, 44100, 180)
    OP_A1(0x11, 0x0)
    OP_6D(-55520, 100, 44450, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(327000, 0)
    OP_6E(370, 0)
    Sleep(1000)
    LoadEffect(0x0, "map\\\\mp014_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -54650, 100, 42240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1C9, 0x0, 0x64)
    OP_1D(0x54)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #296
        0x10,
        "#260F#6P……啊…………\x02",
    )

    CloseMessageWindow()
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x27), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_99(0x10, 0x0, 0x6, 0x3E8)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)
    OP_9E(0x10, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(1000)

    ChrTalk(    #297
        0x10,
        (
            "#260F#6P是了……\x02\x03",

            "我说怎么这么冷，\x01",
            "原来下雨了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x1F4)
    OP_6F(0x0, 461)
    OP_70(0x0, 0x1E0)
    OP_73(0x0)
    OP_D8(0x0, 0x1F4)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    Sleep(1000)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #298
        0x10,
        (
            "#260F#6P呵呵，谢谢。\x01",
            "『帕蒂尔·玛蒂尔』。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x10, 0xFFFF287E, 0x3C, 0x9A1A, 0x7D0, 0x0)

    def lambda_85D3():
        OP_6D(-55780, 1980, 44190, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_85D3)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 1)

    def lambda_85FF():
        OP_99(0x10, 0x0, 0x2, 0x9C4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_85FF)
    SetChrFlags(0x10, 0x4)
    OP_96(0x10, 0xFFFF286A, 0xDAC, 0xA47E, 0xFA0, 0x1F40)
    ClearChrFlags(0x10, 0x4)
    OP_CF(0x10, 0x0, "Frame85__ren")
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrFlags(0x10, 0x10)
    OP_8C(0x10, 180, 0)
    Sleep(500)
    OP_8C(0x10, 0, 400)
    ClearChrFlags(0x10, 0x10)
    WaitChrThread(0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    LoadEffect(0x4, "map\\\\mp064_00.eff")
    LoadEffect(0x5, "map\\\\mp065_00.eff")
    Sleep(500)
    OP_22(0x113, 0x1, 0x46)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x11, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    PlayEffect(0x4, 0x1, 0x11, 4950, 2800, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0x11, -4950, 2800, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0x1, 0x11, 5000, 2500, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x11, -4900, 2500, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_87F8():
        OP_6D(-52190, 710, 47820, 4500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_87F8)

    def lambda_8810():
        OP_67(0, 6920, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8810)

    def lambda_8828():
        OP_6B(2860, 4500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_8828)

    def lambda_8838():
        OP_6C(23000, 4500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_8838)

    def lambda_8848():
        OP_6E(407, 4500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8848)
    OP_43(0x11, 0x0, 0x0, 0x15)

    def lambda_885F():
        OP_8F(0xFE, 0xFFFF3062, 0x834, 0x9F92, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_885F)
    Sleep(300)

    def lambda_887F():
        OP_8F(0xFE, 0xFFFF3062, 0x834, 0x9F92, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_887F)
    Sleep(300)

    def lambda_889F():
        OP_8F(0xFE, 0xFFFF3062, 0x834, 0x9F92, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_889F)
    OP_24(0x113, 0x50)
    Sleep(100)
    Sleep(2000)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x1F4)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x104)
    OP_82(0x0, 0x2)
    Sleep(50)
    PlayEffect(0x2, 0x1, 0x11, 4600, 2600, 0, 0, 0, 18, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x11, -4600, 2600, 0, 0, 0, 342, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_8957():
        OP_8F(0xFE, 0xFFFF3062, 0x834, 0x9F92, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8957)
    OP_24(0x113, 0x5A)
    Sleep(100)
    OP_24(0x113, 0x64)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x0, 0x0)
    Fade(500)
    OP_6D(-62040, 1600, 39420, 0)
    OP_67(0, 4990, -10000, 0)
    OP_6B(2890, 0)
    OP_6C(271000, 0)
    OP_6E(440, 0)
    OP_11(0xF0, 0xE6, 0xB4, 0x14C08, 0x21EF8, 0x0)
    OP_0D()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x3E8)
    OP_6F(0x0, 261)
    OP_70(0x0, 0x118)
    OP_22(0x116, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x3E8)
    OP_6F(0x0, 281)
    OP_70(0x0, 0x12C)
    PlayEffect(0x3, 0x0, 0x11, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x11, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x11, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x5, 0x11, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x6, 0x11, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x7, 0x11, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x114, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x0, 0x11, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x11, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x11, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x11, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x11, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0x11, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)

    def lambda_8CA5():
        OP_6D(-62040, 2500, 39670, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8CA5)

    def lambda_8CBD():
        OP_67(0, 3700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8CBD)

    def lambda_8CD5():
        OP_6B(4050, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_8CD5)

    def lambda_8CE5():
        OP_6E(382, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_8CE5)
    Sleep(500)

    def lambda_8CFA():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8CFA)
    Sleep(100)

    def lambda_8D1A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D1A)
    Sleep(100)

    def lambda_8D3A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D3A)
    Sleep(100)

    def lambda_8D5A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D5A)
    Sleep(100)

    def lambda_8D7A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D7A)
    Sleep(100)

    def lambda_8D9A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D9A)
    Sleep(100)

    def lambda_8DBA():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8DBA)
    Sleep(100)

    def lambda_8DDA():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8DDA)
    Sleep(100)

    def lambda_8DFA():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x80E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8DFA)
    Sleep(100)

    def lambda_8E1A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x9470, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8E1A)
    Sleep(100)

    def lambda_8E3A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xA7F8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8E3A)
    Sleep(100)

    def lambda_8E5A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xBB80, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8E5A)
    WaitChrThread(0x11, 0x1)
    OP_43(0x10, 0x0, 0x0, 0x13)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_43(0x10, 0x1, 0x0, 0x14)
    OP_20(0x7D0)
    Sleep(2000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EE9")
    Sleep(1000)
    OP_28(0xF, 0x4, 0x10)
    OP_3E(0x2E8, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #299
        "\x07\x00得到了\x1F\xE8\x02\x07\x00。\x02",
    )

    Jump("loc_8EDD")

    label("loc_8EDD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_8EE9")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7313   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_7416 end

    def Function_19_8EF6(): pass

    label("Function_19_8EF6")

    OP_24(0x113, 0x5A)
    Sleep(200)
    OP_24(0x113, 0x50)
    Sleep(200)
    OP_24(0x113, 0x46)
    Sleep(200)
    OP_24(0x113, 0x3C)
    Sleep(200)
    OP_24(0x113, 0x32)
    Sleep(200)
    OP_24(0x113, 0x28)
    Sleep(200)
    OP_24(0x113, 0x1E)
    Sleep(200)
    OP_24(0x113, 0x14)
    Sleep(200)
    OP_24(0x113, 0xA)
    Sleep(200)
    OP_24(0x113, 0x0)
    OP_23(0x113)
    Return()

    # Function_19_8EF6 end

    def Function_20_8F4F(): pass

    label("Function_20_8F4F")

    OP_24(0x1C9, 0x5A)
    Sleep(200)
    OP_24(0x1C9, 0x50)
    Sleep(200)
    OP_24(0x1C9, 0x46)
    Sleep(200)
    OP_24(0x1C9, 0x3C)
    Sleep(200)
    OP_24(0x1C9, 0x32)
    Sleep(200)
    OP_24(0x1C9, 0x28)
    Sleep(200)
    OP_24(0x1C9, 0x1E)
    Sleep(200)
    OP_24(0x1C9, 0x14)
    Sleep(200)
    OP_24(0x1C9, 0xA)
    Sleep(200)
    OP_24(0x1C9, 0x0)
    OP_23(0x1C9)
    Return()

    # Function_20_8F4F end

    def Function_21_8FA8(): pass

    label("Function_21_8FA8")

    Sleep(1000)

    def lambda_8FB3():
        OP_8C(0xFE, 250, 10)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_8FB3)
    Sleep(200)

    def lambda_8FC6():
        OP_8C(0xFE, 250, 15)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_8FC6)
    Sleep(200)

    def lambda_8FD9():
        OP_8C(0xFE, 250, 20)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_8FD9)
    Sleep(500)

    def lambda_8FEC():
        OP_8C(0xFE, 250, 30)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_8FEC)
    Sleep(100)

    def lambda_8FFF():
        OP_8C(0xFE, 250, 40)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_8FFF)
    Return()

    # Function_21_8FA8 end

    def Function_22_9008(): pass

    label("Function_22_9008")

    OP_8F(0xFE, 0xFFFF287E, 0x3C, 0x9A1A, 0x7D0, 0x0)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 1)

    def lambda_9036():
        OP_99(0xFE, 0x0, 0x2, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9036)
    OP_96(0xFE, 0xFFFF286A, 0xBEA, 0xA47E, 0xDAC, 0x1F40)
    OP_CF(0xFE, 0x0, "Frame85__ren")
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)
    SetChrFlags(0xFE, 0x10)
    OP_8C(0xFE, 180, 400)
    ClearChrFlags(0xFE, 0x10)
    Return()

    # Function_22_9008 end

    def Function_23_908E(): pass

    label("Function_23_908E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90C2")
    OP_22(0x235, 0x0, 0x50)
    Sleep(1000)
    OP_22(0x1F7, 0x0, 0x50)
    Sleep(1000)
    OP_22(0x1F7, 0x0, 0x50)
    Sleep(500)
    OP_22(0x235, 0x0, 0x50)
    Sleep(800)
    Jump("Function_23_908E")

    label("loc_90C2")

    Return()

    # Function_23_908E end

    SaveToFile()

Try(main)
