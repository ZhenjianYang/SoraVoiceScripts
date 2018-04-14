from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3120_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3120_1 ._SN',
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_510",          # 01, 1
        "Function_2_713",          # 02, 2
        "Function_3_A41",          # 03, 3
        "Function_4_C31",          # 04, 4
        "Function_5_E82",          # 05, 5
        "Function_6_10D3",         # 06, 6
        "Function_7_1273",         # 07, 7
        "Function_8_14BB",         # 08, 8
        "Function_9_1595",         # 09, 9
        "Function_10_16CA",        # 0A, 10
        "Function_11_17E3",        # 0B, 11
        "Function_12_2360",        # 0C, 12
        "Function_13_2518",        # 0D, 13
        "Function_14_3608",        # 0E, 14
        "Function_15_3667",        # 0F, 15
        "Function_16_36DB",        # 10, 16
        "Function_17_3C16",        # 11, 17
        "Function_18_3D23",        # 12, 18
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13A")
    Jump("loc_17C")

    label("loc_13A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_156")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17C")

    label("loc_156")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_172")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17C")

    label("loc_172")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17C")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_20E")

    ChrTalk(    #0
        0xE,
        (
            "#030F想不到寻宝过程中\x01",
            "会发现古代遗物呢。\x02\x03",

            "无论何时都拥有坚定信念的心……\x01",
            "这应该是很重要的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C1")

    label("loc_20E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_297")

    ChrTalk(    #1
        0xE,
        (
            "#030F呀，诸位。\x01",
            "贵安。\x02\x03",

            "没想到在寻宝过程中竟然\x01",
            "会发现古代遗物呢。\x02\x03",

            "无论何时都拥有坚定信念的心……\x01",
            "这应该是很重要的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2C1")

    label("loc_297")


    ChrTalk(    #2
        0xE,
        (
            "#030F呀，诸位。\x01",
            "贵安。\x02\x03",

            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C1")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31E"),
        (1, "loc_378"),
        (SWITCH_DEFAULT, "loc_378"),
    )


    label("loc_31E")


    ChrTalk(    #3
        0xE,
        (
            "#030F呼，原来如此。\x02\x03",

            "看来你们还是需要\x01",
            "我这个天才的力量啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_371")
    Call(1, 7)
    Jump("loc_375")

    label("loc_371")

    Call(1, 6)

    label("loc_375")

    Jump("loc_507")

    label("loc_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_4B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F1")

    ChrTalk(    #4
        0xE,
        (
            "#031F那我就在这里\x01",
            "稍微休息一会儿吧\x02\x03",

            "呼呼～～趁这个机会，要和\x01",
            "亲爱的提妲好好加深一下感情～～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B2")

    label("loc_3F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45F")

    ChrTalk(    #5
        0xE,
        (
            "#031F那我就继续\x01",
            "在这里待命了。\x02\x03",

            "呵呵，让我陪伴在公主殿下的身旁，\x01",
            "一起渡过优雅的片刻吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B2")

    label("loc_45F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B2")

    ChrTalk(    #6
        0xE,
        (
            "#031F那么就让我们在此\x01",
            "畅谈一会儿吧。\x02\x03",

            "如果有葡萄酒喝\x01",
            "就更好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B2")

    Jump("loc_504")

    label("loc_4B5")


    ChrTalk(    #7
        0xE,
        (
            "#030F我就继续\x01",
            "在这里待命了。\x02\x03",

            "如果需要我这个天才的话\x01",
            "随时可以过来找我哟。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_504")

    Jump("loc_507")

    label("loc_507")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_0_AA end

    def Function_1_510(): pass

    label("Function_1_510")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A0")
    Jump("loc_5E2")

    label("loc_5A0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BC")
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E2")

    label("loc_5BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D8")
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E2")

    label("loc_5D8")

    OP_51(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E2")

    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(    #8
        0xF,
        (
            "#040F各位，辛苦了。\x02\x03",

            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_68B"),
        (1, "loc_6C7"),
        (SWITCH_DEFAULT, "loc_6C7"),
    )


    label("loc_68B")


    ChrTalk(    #9
        0xF,
        (
            "#040F明白了。\x01",
            "要调整队伍吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C0")
    Call(1, 7)
    Jump("loc_6C4")

    label("loc_6C0")

    Call(1, 6)

    label("loc_6C4")

    Jump("loc_70A")

    label("loc_6C7")


    ChrTalk(    #10
        0xF,
        (
            "#040F我就在这里待命。\x02\x03",

            "如果有需要的话，\x01",
            "请尽管开口就好啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70A")

    label("loc_70A")

    SetChrSubChip(0xF, 0)
    TalkEnd(0xF)
    Return()

    # Function_1_510 end

    def Function_2_713(): pass

    label("Function_2_713")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A3")
    Jump("loc_7E5")

    label("loc_7A3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7BF")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7E5")

    label("loc_7BF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DB")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7E5")

    label("loc_7DB")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E5")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_848")

    ChrTalk(    #11
        0xA,
        (
            "#560F啊，阿加特哥哥。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0")

    label("loc_848")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_875")

    ChrTalk(    #12
        0xA,
        (
            "#060F啊，姐姐。\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0")

    label("loc_875")


    ChrTalk(    #13
        0xA,
        (
            "#060F啊，是姐姐。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A0")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8FD"),
        (1, "loc_981"),
        (SWITCH_DEFAULT, "loc_981"),
    )


    label("loc_8FD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_941")

    ChrTalk(    #14
        0xA,
        (
            "#060F啊，嗯，明白了。\x01",
            "要调整队伍是吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_967")

    label("loc_941")


    ChrTalk(    #15
        0xA,
        (
            "#560F啊，明白了。\x01",
            "要调整队伍么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_967")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97A")
    Call(1, 7)
    Jump("loc_97E")

    label("loc_97A")

    Call(1, 6)

    label("loc_97E")

    Jump("loc_A38")

    label("loc_981")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E8")

    ChrTalk(    #16
        0xA,
        (
            "#064F咦，不要了吗……？\x02\x03",

            "#060F那我就在这里等着大家，\x01",
            "有什么事就来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A35")

    label("loc_9E8")


    ChrTalk(    #17
        0xA,
        (
            "#064F咦，不要了吗……？\x02\x03",

            "#060F我会一直在这里等着的，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A35")

    Jump("loc_A38")

    label("loc_A38")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_2_713 end

    def Function_3_A41(): pass

    label("Function_3_A41")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x0, 0)
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AD1")
    Jump("loc_B13")

    label("loc_AD1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AED")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B13")

    label("loc_AED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B09")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B13")

    label("loc_B09")

    OP_51(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B13")

    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)

    ChrTalk(    #18
        0x11,
        "#070F哦，情况怎么样？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BB0"),
        (1, "loc_BE3"),
        (SWITCH_DEFAULT, "loc_BE3"),
    )


    label("loc_BB0")


    ChrTalk(    #19
        0x11,
        "#070F要调整队伍吧？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDC")
    Call(1, 7)
    Jump("loc_BE0")

    label("loc_BDC")

    Call(1, 6)

    label("loc_BE0")

    Jump("loc_C28")

    label("loc_BE3")


    ChrTalk(    #20
        0x11,
        (
            "#070F喔，不用了吗？\x02\x03",

            "如果需要我的拳头的话，\x01",
            "尽管开口就是了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C28")

    label("loc_C28")

    SetChrSubChip(0x11, 0)
    TalkEnd(0x11)
    Return()

    # Function_3_A41 end

    def Function_4_C31(): pass

    label("Function_4_C31")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x0, 0)
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CC1")
    Jump("loc_D03")

    label("loc_CC1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CDD")
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D03")

    label("loc_CDD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF9")
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D03")

    label("loc_CF9")

    OP_51(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D03")

    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4E")

    ChrTalk(    #21
        0x17,
        "#020F嗯，怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D60")

    label("loc_D4E")


    ChrTalk(    #22
        0x17,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()

    label("loc_D60")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DBD"),
        (1, "loc_E17"),
        (SWITCH_DEFAULT, "loc_E17"),
    )


    label("loc_DBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEB")

    ChrTalk(    #23
        0x17,
        "#020F哎呀，要调整队伍吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_DFD")

    label("loc_DEB")


    ChrTalk(    #24
        0x17,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()

    label("loc_DFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E10")
    Call(1, 7)
    Jump("loc_E14")

    label("loc_E10")

    Call(1, 6)

    label("loc_E14")

    Jump("loc_E79")

    label("loc_E17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E64")

    ChrTalk(    #25
        0x17,
        (
            "#020F呵呵，我就在这儿\x01",
            "慢慢休养吧。\x02\x03",

            "那么，之后就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E76")

    label("loc_E64")


    ChrTalk(    #26
        0x17,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()

    label("loc_E76")

    Jump("loc_E79")

    label("loc_E79")

    SetChrSubChip(0x17, 0)
    TalkEnd(0x17)
    Return()

    # Function_4_C31 end

    def Function_5_E82(): pass

    label("Function_5_E82")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x18)
    ClearChrFlags(0x18, 0x10)
    TurnDirection(0x18, 0x0, 0)
    OP_51(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F12")
    Jump("loc_F54")

    label("loc_F12")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F2E")
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F54")

    label("loc_F2E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F4A")
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F54")

    label("loc_F4A")

    OP_51(0x18, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F54")

    OP_51(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x18, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9F")

    ChrTalk(    #27
        0x18,
        "#050F哟，怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB1")

    label("loc_F9F")


    ChrTalk(    #28
        0x18,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()

    label("loc_FB1")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_100E"),
        (1, "loc_1066"),
        (SWITCH_DEFAULT, "loc_1066"),
    )


    label("loc_100E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103A")

    ChrTalk(    #29
        0x18,
        "#050F要替换队伍成员吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_104C")

    label("loc_103A")


    ChrTalk(    #30
        0x18,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()

    label("loc_104C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105F")
    Call(1, 7)
    Jump("loc_1063")

    label("loc_105F")

    Call(1, 6)

    label("loc_1063")

    Jump("loc_10CA")

    label("loc_1066")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B5")

    ChrTalk(    #31
        0x18,
        (
            "#051F我就在此处待命。\x02\x03",

            "如果需要我出力的话，\x01",
            "随时说话就是。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C7")

    label("loc_10B5")


    ChrTalk(    #32
        0x18,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()

    label("loc_10C7")

    Jump("loc_10CA")

    label("loc_10CA")

    SetChrSubChip(0x18, 0)
    TalkEnd(0x18)
    Return()

    # Function_5_E82 end

    def Function_6_10D3(): pass

    label("Function_6_10D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1111")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_10F9")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_110E")

    label("loc_10F9")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_110E")

    Jump("loc_113D")

    label("loc_1111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_112C")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_113D")

    label("loc_112C")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_113D")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_A3(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_119A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119A")
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 23530, 200, -2100, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 18)
    OP_A2(0x9)

    label("loc_119A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11ED")
    SetChrFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CC")
    SetChrPos(0xE, 23530, 200, -2100, 0)
    OP_A2(0xA)
    Jump("loc_11E0")

    label("loc_11CC")

    SetChrPos(0xE, 23530, 200, 400, 180)
    OP_A3(0xA)

    label("loc_11E0")

    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 6)
    OP_A2(0x9)

    label("loc_11ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1240")
    SetChrFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121F")
    SetChrPos(0xF, 23530, 200, -2100, 0)
    OP_A2(0xB)
    Jump("loc_1233")

    label("loc_121F")

    SetChrPos(0xF, 23530, 200, 400, 180)
    OP_A3(0xB)

    label("loc_1233")

    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 7)
    OP_A2(0x9)

    label("loc_1240")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1271")
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 23530, 200, 400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 17)
    OP_A2(0x9)

    label("loc_1271")

    OP_0D()
    Return()

    # Function_6_10D3 end

    def Function_7_1273(): pass

    label("Function_7_1273")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_A3(0xD)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1310")
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrChipByIndex(0x17, 15)
    SetChrPos(0x17, 23550, 200, 420, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F5")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_12F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1310")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_1310")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1373")
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x4)
    SetChrChipByIndex(0x18, 16)
    SetChrPos(0x18, 26270, 200, -480, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1358")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_1358")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_1373")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13D6")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 17)
    SetChrPos(0xA, 28530, 200, -570, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13BB")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_13BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D6")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_13D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1439")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 18)
    SetChrPos(0x11, 23550, 200, -2170, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141E")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_141E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1439")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_1439")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_14BA")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "\x07\x05※要待命的成员\x01",
            "　装备着『零力场发生器』。\x01",
            "　将其回收后放入队伍的携带品中。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_14BA")

    Return()

    # Function_7_1273 end

    def Function_8_14BB(): pass

    label("Function_8_14BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_14CC")
    OP_2A(0xBB, 0xBC, 0xFFFF)
    Jump("loc_1591")

    label("loc_14CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_14ED")
    OP_2A(0x6C, 0x6D, 0x6E, 0xA5, 0xA6, 0x6F, 0x70, 0xA7, 0xA8, 0x71, 0xFFFF)
    Jump("loc_1591")

    label("loc_14ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_150C")
    OP_2A(0x6C, 0x6D, 0x6E, 0xA5, 0xA6, 0x6F, 0x70, 0xA7, 0xA8, 0xFFFF)
    Jump("loc_1591")

    label("loc_150C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_152B")
    OP_2A(0x6C, 0x6D, 0x6E, 0xA5, 0xA6, 0x6F, 0x70, 0xA7, 0xA8, 0xFFFF)
    Jump("loc_1591")

    label("loc_152B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 3)), scpexpr(EXPR_END)), "loc_1542")
    OP_2A(0x6C, 0x6D, 0x6E, 0xA5, 0xA6, 0xFFFF)
    Jump("loc_1591")

    label("loc_1542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1559")
    OP_2A(0x6C, 0x6D, 0x6E, 0xA5, 0xA6, 0xFFFF)
    Jump("loc_1591")

    label("loc_1559")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #34
        "\x07\x05没有什么特别的委托。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1591")

    TalkEnd(0xFF)
    Return()

    # Function_8_14BB end

    def Function_9_1595(): pass

    label("Function_9_1595")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    Call(1, 15)

    ChrTalk(    #35
        0x8,
        (
            "#790F你们看过告示板了吧。\x02\x03",

            "你们也要\x01",
            "协助我们调查吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C5")

    ChrTalk(    #36
        0x101,
        (
            "#1015F#7P不，不是这样的……\x02\x03",

            "#1006F只不过有点感兴趣而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#792F是吗，那就专心于\x01",
            "其他的调查吧。\x02\x03",

            "这里的事情\x01",
            "并不是什么紧急性的案件。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6C, 0x1, 0x8000)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    label("loc_16C5")

    Call(1, 11)
    Return()

    # Function_9_1595 end

    def Function_10_16CA(): pass

    label("Function_10_16CA")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    Call(1, 15)

    ChrTalk(    #38
        0x8,
        (
            "#790F看来你对招牌板的\x01",
            "案件很有兴趣啊，\x02\x03",

            "愿意协助我们调查吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DE")

    ChrTalk(    #39
        0x101,
        "#1015F#7P不，不是这样的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "#792F是吗，那就专心于\x01",
            "其他的调查吧。\x02\x03",

            "这里的事情\x01",
            "并不是什么紧急性的案件。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    label("loc_17DE")

    Call(1, 11)
    Return()

    # Function_10_16CA end

    def Function_11_17E3(): pass

    label("Function_11_17E3")

    EventBegin(0x0)

    ChrTalk(    #41
        0x101,
        (
            "#1002F#7P嗯、嗯……\x01",
            "是的。\x02\x03",

            "招牌指的是\x01",
            "吊在支部檐头上的\x01",
            "那个带有徽章的招牌？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#792F嗯，那个招牌被盗了。\x02\x03",

            "虽然不构成什么实际问题，\x01",
            "不过徽章是协会的使命和义务的象征……\x02\x03",

            "#790F那东西被盗的话\x01",
            "我们也不能坐视不管了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1015F是，是吗……\x02\x03",

            "确实不能忽视呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_193C")

    ChrTalk(    #44
        0x106,
        (
            "#053F#5P呼，看来我们被别人小看了。\x02\x03",

            "#050F……那么，案件的经过是？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1983")

    label("loc_193C")


    ChrTalk(    #45
        0x103,
        (
            "#025F#5P真是的，看来我们被别人小看了。\x02\x03",

            "#022F那么，案件的经过是？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1983")


    ChrTalk(    #46
        0x8,
        (
            "#790F是在昨天午后\x01",
            "被支部所属的王发现的。\x02\x03",

            "他回来报告的时候，\x01",
            "注意到外面的招牌不见了。\x02\x03",

            "#792F被盗时间应该是\x01",
            "当天上午。\x02\x03",

            "我因为有事出去所以支部内无人看守，\x01",
            "正好在那时有人目击到\x01",
            "支部面前有个施工人员。\x02\x03",

            "#790F看来那个人就是\x01",
            "化装后的罪犯。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x101,
        "#1004F#7P化、化装？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0C")

    ChrTalk(    #48
        0x105,
        (
            "#043F艾、艾丝蒂尔……\x02\x03",

            "这难道是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1020F#7P虽、虽然觉得有点不可思议……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B60")

    label("loc_1B0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B60")

    ChrTalk(    #50
        0x104,
        (
            "#033F哟，这可有意思……\x02\x03",

            "莫非这是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1020F#7P莫、莫非……\x02",
    )

    CloseMessageWindow()

    label("loc_1B60")


    ChrTalk(    #52
        0x8,
        (
            "#790F看来你们有方向了呢。\x02\x03",

            "#792F那么……\x01",
            "这个是怎么回事？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #53
        (
            "\x07\x05　　美丽的公主及其随从啊。　\x01",
            "　　　　众勇士之魂\x01",
            "　　　 已落入我手中　\x02\x03",

            "　　　如若期望得以解放\x01",
            " 　　只需胜我所施诅咒即可 　\x02\x03",

            "　　　 第一把钥匙在市内　　　\x01",
            "　寻『年龄４０之老翁』之背吧\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #54
        0x8,
        (
            "#790F这是案发后\x01",
            "寄来的卡片。\x02\x03",

            "从内容来看\x01",
            "可以认为这是犯罪声明。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1D0A")

    ChrTalk(    #55
        0x106,
        "#551F#5P…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D2C")

    label("loc_1D0A")


    ChrTalk(    #56
        0x103,
        "#025F#5P…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_1D2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D56")

    ChrTalk(    #57
        0x105,
        "#045F看来是没错了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D7B")

    label("loc_1D56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D7B")

    ChrTalk(    #58
        0x104,
        "#032F看来没错呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1D7B")


    ChrTalk(    #59
        0x101,
        "#1007F#7P呼，是那家伙干的好事啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#792F『那家伙』指的是\x01",
            "那个怪盗布卢布兰？\x02\x03",

            "#790F在卢安发生的一切\x01",
            "我都听嘉恩说了。\x02\x03",

            "此次的案件……\x01",
            "可以说成是怪盗Ｂ的挑战吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E6F")

    ChrTalk(    #61
        0x104,
        (
            "#031F呵呵，有意思。\x02\x03",

            "这正是我那劲敌的挑战。\x01",
            "接受挑战吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E6F")


    ChrTalk(    #62
        0x101,
        "#1003F#7P竟然自说自话的发起挑战……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1F09")

    ChrTalk(    #63
        0x106,
        (
            "#050F#5P不过，这是对方找上门的挑衅。\x01",
            "我们只能接受挑战了。\x02\x03",

            "总之先以卡片为依据\x01",
            "开始调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F67")

    label("loc_1F09")


    ChrTalk(    #64
        0x103,
        (
            "#022F#5P虽然对方是自说自话地发起挑战，\x01",
            "我们也只有接受。\x02\x03",

            "总之先以卡片为依据\x01",
            "开始调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F67")

    TurnDirection(0x101, 0xF7, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFE")

    ChrTalk(    #65
        0x101,
        (
            "#1000F#7P嗯，卡片上所写的是……\x01",
            "『市内』和『４０岁老翁的后背』呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #66
        0x107,
        (
            "#063F嗯～是不是要去找\x01",
            "城里的某位老爷爷呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2075")

    label("loc_1FFE")


    ChrTalk(    #67
        0x101,
        (
            "#1015F#7P嗯，卡片上所写的是……\x01",
            "『市内』和『４０岁老翁的后背』呢。\x02\x03",

            "嗯～如果从字面意思理解的话，\x01",
            "就是去找老爷爷。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2075")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20FF")
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #68
        0x104,
        (
            "#032F唔，直接理解的话\x01",
            "就是那样了……\x02\x03",

            "但是，从在学院发生的一系列事件来看，\x01",
            "用普通的方法明显是不行的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    Jump("loc_217A")

    label("loc_20FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_217A")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #69
        0x105,
        (
            "#042F嗯，直接理解的话\x01",
            "就是那样了……\x02\x03",

            "不过从学院的系列谜团来看的话\x01",
            "就不会是这么简单的了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_217A")


    ChrTalk(    #70
        0x101,
        (
            "#1002F#7P那时的讯息\x01",
            "都是某种『比喻』吧。\x02\x03",

            "这次会不会也是那样呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2210")

    ChrTalk(    #71
        0x106,
        (
            "#053F#5P嗯，这可不好说……\x02\x03",

            "#050F发愁也没用。\x01",
            "赶快去城里调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2256")

    label("loc_2210")


    ChrTalk(    #72
        0x103,
        (
            "#026F#5P嗯，这可不好说……\x02\x03",

            "#022F发愁也没用。\x01",
            "赶快去城里调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2256")


    ChrTalk(    #73
        0x8,
        (
            "#790F嗯，只能这样了。\x02\x03",

            "那我就在这里静候佳音吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2291():
        OP_8C(0x1, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2291)
    Sleep(50)

    def lambda_22A4():
        OP_8C(0x2, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_22A4)
    Sleep(100)

    def lambda_22B7():
        OP_8C(0x3, 0, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_22B7)
    OP_8C(0x0, 0, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2311")

    ChrTalk(    #74
        0x104,
        "#031F呵呵，交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1006F#7P那我们先走了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2340")

    label("loc_2311")


    ChrTalk(    #76
        0x101,
        (
            "#1006F#7P嗯，交给我们吧。\x02\x03",

            "那我们先走了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2340")

    OP_28(0x6C, 0x1, 0x1)
    OP_28(0x6C, 0x1, 0x2)
    OP_28(0x6C, 0x4, 0x4)
    OP_28(0x6C, 0x4, 0x8)
    OP_A2(0x11)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_11_17E3 end

    def Function_12_2360(): pass

    label("Function_12_2360")


    ChrTalk(    #77
        0x8,
        (
            "#790F要再次确认\x01",
            "卡片内容？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E8")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #78
        (
            "\x07\x05给美丽的公主和她的臣仆们。\x01",
            "众勇士之魂\x01",
            "已落入我手中。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #79
        (
            "\x07\x05如若期望得以解放\x01",
            "只需胜我所施诅咒即可。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #80
        (
            "\x07\x05第一把钥匙在市内。\x01",
            "寻找『年龄４０之老翁』吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #81
        0x8,
        (
            "#790F关键点在于\x01",
            "『市内』和『年龄４０之老翁』呢。\x02\x03",

            "那么调查就\x01",
            "麻烦您了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_24E8")


    ChrTalk(    #82
        0x8,
        (
            "#790F那就拜托你们调查吧。\x02\x03",

            "我可期待着哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2517")

    Return()

    # Function_12_2360 end

    def Function_13_2518(): pass

    label("Function_13_2518")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    SetChrPos(0x8, 3500, 0, 1200, 180)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 3500, 0, -3440, 0)
    SetChrPos(0x101, 3500, 0, -2210, 180)
    SetChrPos(0xF7, 4300, 0, -1830, 180)
    SetChrPos(0xF8, 2800, 0, -800, 180)
    SetChrPos(0xF9, 4200, 0, -800, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25AD")
    SetChrPos(0xE, 2120, 0, -1810, 135)
    SetChrChipByIndex(0xE, 4)

    label("loc_25AD")

    OP_6B(2720, 0)
    OP_6D(2650, 0, -1360, 0)
    OP_67(0, 6000, -10000, 0)
    OP_0D()

    ChrTalk(    #83
        0x8,
        (
            "#792F#2P──真可谓千钧一发啊。\x02\x03",

            "如果先开宝箱的话\x01",
            "你现在一定已经\x01",
            "成为企鹅的食物了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #84
        0x19,
        (
            "啊、啊啊～！？\x01",
            "企鹅的食物……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x19,
        (
            "我、我在反省啊，\x01",
            "别吓唬我了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_26FB")

    ChrTalk(    #86
        0x106,
        (
            "#050F我并没有吓唬你。\x02\x03",

            "因为这次你会得救\x01",
            "真的是太偶然了。\x02\x03",

            "以此为鉴，\x01",
            "你就好好认真反省吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_275C")

    label("loc_26FB")


    ChrTalk(    #87
        0x103,
        (
            "#020F我并没有吓唬你。\x02\x03",

            "因为这次你会得救\x01",
            "真的只是偶然的幸运。\x02\x03",

            "以此为鉴，\x01",
            "你就好好地反省吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_275C")


    ChrTalk(    #88
        0x19,
        "嗯、嗯，我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x19,
        (
            "总、总之我要找份固定工作，\x01",
            "挣够能够请护卫的米拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #90
        0x101,
        (
            "#1016F原、原来是这么回事儿……\x02\x03",

            "就算反省了也还是\x01",
            "要去危险的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x19,
        (
            "那、那当然了。\x01",
            "寻宝是男人的浪漫啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x19,
        (
            "为了像这次这样的发现，\x01",
            "少许的危险也是不得已的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2911")

    ChrTalk(    #93
        0x104,
        (
            "#030F呼，那么所谓的\x01",
            "『这次的发现』怎么样了？\x02\x03",

            "好像从状况来看，\x01",
            "是货真价实的海盗宝藏呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#1011F啊，是哦。\x02\x03",

            "总之要先把宝物\x01",
            "还给吉米先生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A80")

    label("loc_2911")


    ChrTalk(    #95
        0xE,
        (
            "#030F呼，那么所谓的\x01",
            "『这次的发现』怎么样了？\x02\x03",

            "从刚才的话中，\x01",
            "是货真价实的海盗宝藏呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #96
        0x101,
        (
            "#1011F啊，是哦。\x02\x03",

            "#1019F……咦，你怎么会\x01",
            "见缝插针地站在这儿？\x02\x03",

            "你不是在2楼\x01",
            "度过优雅的片刻吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xE,
        (
            "#031F那个，因为听到了\x01",
            "欢快的声音。\x02\x03",

            "好了，不用管我，\x01",
            "继续你们的谈话吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1007F我总是对你的好奇心\x01",
            "深感钦佩啊。\x02\x03",

            "#1015F好，先不管这家伙，\x01",
            "首先要返还宝物。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x19, 400)

    label("loc_2A80")

    OP_94(0x1, 0x101, 0x0, 0xC8, 0x3E8, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #99
        "\x07\x02#16I银露宝珠\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x3E8, 0x0)

    ChrTalk(    #100
        0x19,
        "啊，谢谢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x19,
        (
            "感觉像梦境一样。\x01",
            "竟然真能找到财宝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1015F嗯，不过不知道\x01",
            "这是什么东西。\x02\x03",

            "根据残留下来的信件内容记载，\x01",
            "这好像是很了不起的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x19,
        "确、确实如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x19,
        (
            "我也没见过\x01",
            "这种东西。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C6E")

    ChrTalk(    #105
        0x108,
        (
            "#070F嗯，这恐怕是\x01",
            "古代遗物吧。\x02\x03",

            "从外观来看\x01",
            "应该已经没有力量了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2C24():
        TurnDirection(0x101, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C24)

    def lambda_2C32():
        TurnDirection(0xF7, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2C32)

    def lambda_2C40():
        TurnDirection(0xF8, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2C40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C64")

    def lambda_2C5C():
        TurnDirection(0xE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2C5C)

    label("loc_2C64")

    TurnDirection(0xF9, 0x108, 400)
    Jump("loc_2DB5")

    label("loc_2C6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D0C")

    ChrTalk(    #106
        0x104,
        (
            "#030F嗯，这恐怕是\x01",
            "古代遗物吧。\x02\x03",

            "从外观来看\x01",
            "应该已经没有力量了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2CDE():
        TurnDirection(0x101, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CDE)

    def lambda_2CEC():
        TurnDirection(0xF7, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2CEC)

    def lambda_2CFA():
        TurnDirection(0xF8, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2CFA)
    TurnDirection(0xF9, 0x104, 400)
    Jump("loc_2DB5")

    label("loc_2D0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DB5")

    ChrTalk(    #107
        0x105,
        (
            "#042F这恐怕是……\x01",
            "古代遗物吧。\x02\x03",

            "从外观来看\x01",
            "应该已经没有力量了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2D7C():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D7C)

    def lambda_2D8A():
        TurnDirection(0xF7, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2D8A)

    def lambda_2D98():
        TurnDirection(0xF8, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2D98)

    def lambda_2DA6():
        TurnDirection(0xE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2DA6)
    TurnDirection(0xF9, 0x105, 400)

    label("loc_2DB5")

    WaitChrThread(0x101, 0x1)
    Sleep(400)

    ChrTalk(    #108
        0x19,
        (
            "咦咦！？\x01",
            "古、古代遗物！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1004F古代遗物是……\x01",
            "就是古代文明的遗物。\x02\x03",

            "即便已经没有了力量，\x01",
            "可这也算是了不得的东西吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EAC")

    ChrTalk(    #110
        0x108,
        (
            "#070F嗯，应该拿到相关部门\x01",
            "去让他们调查一下比较好。\x02\x03",

            "个人持有的话\x01",
            "会碰上很多麻烦的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F84")

    label("loc_2EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F0A")

    ChrTalk(    #111
        0x104,
        (
            "#030F应该拿到相关部门\x01",
            "去让他们调查一下。\x02\x03",

            "我不推荐个人\x01",
            "持有这种东西……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F84")

    label("loc_2F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F84")

    ChrTalk(    #112
        0x105,
        (
            "#047F嗯，我觉得应该拿到相关部门\x01",
            "去让他们调查一下比较好。\x02\x03",

            "#042F因为这种东西由个人\x01",
            "持有不是什么好事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F84")


    ChrTalk(    #113
        0x8,
        (
            "#790F说起附近的研究机关，\x01",
            "那就是王都的历史资料馆了。\x02\x03",

            "如果你愿意的话\x01",
            "我们可以帮你联系。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FE7():
        TurnDirection(0x101, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FE7)
    Sleep(100)

    def lambda_2FFA():
        OP_8C(0xF7, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2FFA)
    Sleep(50)

    def lambda_300D():
        TurnDirection(0xF8, 0x19, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_300D)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3036")

    def lambda_3029():
        TurnDirection(0xE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3029)
    Sleep(50)

    label("loc_3036")

    TurnDirection(0xF9, 0x19, 400)

    ChrTalk(    #114
        0x19,
        "请、请一定帮我联系！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x19,
        (
            "如果是这么了不得的东西的话，\x01",
            "我希望能被保管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "#790F……这样啊，明白了。\x02\x03",

            "那么，到王都的票也\x01",
            "一并帮你安排了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x19,
        (
            "啊，谢谢！\x01",
            "服务真周到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "#792F不，这是必要的经费安排。\x02\x03",

            "因为你现在\x01",
            "身无分文吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #119
        0x19,
        (
            "啊！？\x01",
            "你、你怎么会知道的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#1016F哈哈，这么快\x01",
            "就被看穿了啊。\x02\x03",

            "#1000F不过，这样的话\x01",
            "就尽管使用定期船吧。\x02\x03",

            "老实说，让吉米先生\x01",
            "在大道上步行还真令人不安呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_320E")

    ChrTalk(    #121
        0x106,
        "#551F嗯，我有同感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3227")

    label("loc_320E")


    ChrTalk(    #122
        0x103,
        "#025F嗯，我有同感。\x02",
    )

    CloseMessageWindow()

    label("loc_3227")


    ChrTalk(    #123
        0x8,
        (
            "#790F#2P船票你就在飞船坪的\x01",
            "接待处领取吧。\x02\x03",

            "那么，请小心前往王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x19,
        "今天真是太谢谢你们了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x8000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_329F")
    OP_A2(0x12)

    label("loc_329F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3318")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇曾经完成上部吉米任务】\x01",      # 0
            "【◇不变更】\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3312"),
        (SWITCH_DEFAULT, "loc_3318"),
    )


    label("loc_3312")

    OP_A2(0x12)
    Jump("loc_3318")

    label("loc_3318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_3455")

    ChrTalk(    #125
        0x19,
        (
            "……不，想想的话也\x01",
            "不光是今天一天的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x19,
        (
            "一直以来都受\x01",
            "你的照顾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x19,
        "……对了，请收下这个。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #128
        "\x07\x00得到了\x1F\xD7\x02\x07\x00结晶回路。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x2D7, 1)

    ChrTalk(    #129
        0x19,
        (
            "这是我爱用的东西。\x01",
            "从现在起由你来使用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#1004F可以吗？　我收这种东西……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x19,
        (
            "这表示我一直以来的谢意。\x01",
            "请收下来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3455")


    ChrTalk(    #132
        0x19,
        "那么我们在王都再会！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1006F嗯，明白了。\x02\x03",

            "那个『宝珠』……\x01",
            "要好好地送交资料馆哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x19,
        "嗯，交给我吧！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_351D")

    ChrTalk(    #135
        0xE,
        (
            "#031F那我也要\x01",
            "撤了。\x02\x03",

            "那么再见了，吉米。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xE, 400)

    ChrTalk(    #136
        0x19,
        "嗯，你也要保重。\x02",
    )

    CloseMessageWindow()

    label("loc_351D")


    def lambda_3523():
        OP_6D(1820, 0, -4980, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3523)
    OP_8C(0x19, 270, 400)
    OP_43(0xE, 0x0, 0x1, 0xE)
    OP_8E(0x19, 0x5AA, 0x0, 0xFFFFE7DC, 0x7D0, 0x0)

    def lambda_355D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_355D)
    OP_8E(0x19, 0x5AA, 0x0, 0xFFFFE0AC, 0x7D0, 0x0)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x8, 0x1)
    OP_28(0x71, 0x4, 0x10)
    OP_28(0x71, 0x1, 0x4)
    OP_28(0x71, 0x1, 0x8)
    OP_28(0x71, 0x1, 0x10)
    OP_69(0x101, 0x7D0)
    WaitChrThread(0xE, 0x0)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #137
        "\x07\x02任务【投宿客人的搜索】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0xC)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_13_2518 end

    def Function_14_3608(): pass

    label("Function_14_3608")

    Sleep(400)
    OP_8C(0xE, 315, 500)
    SetChrFlags(0xE, 0x4)
    OP_8E(0xE, 0xFFFFF8D0, 0x0, 0x51E, 0x9C4, 0x0)
    OP_8E(0xE, 0xFFFFF858, 0x0, 0x992, 0x9C4, 0x0)
    OP_8C(0xE, 90, 500)
    ClearChrFlags(0xE, 0x4)
    OP_8E(0xE, 0x9C4, 0x8CA, 0xAAA, 0x9C4, 0x0)
    SetChrFlags(0xE, 0x80)
    Return()

    # Function_14_3608 end

    def Function_15_3667(): pass

    label("Function_15_3667")

    Fade(1000)
    OP_8C(0x8, 180, 0)
    SetChrPos(0x101, 4230, 0, -710, 0)
    SetChrPos(0xF7, 3180, 0, -700, 0)
    SetChrPos(0xF8, 4300, 0, -1950, 0)
    SetChrPos(0xF9, 3380, 0, -2100, 0)
    OP_6D(3550, 0, 330, 0)
    OP_67(0, 6000, -10000, 0)
    OP_0D()
    Return()

    # Function_15_3667 end

    def Function_16_36DB(): pass

    label("Function_16_36DB")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x151, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36FC")
    OP_3F(0x151, 1)
    Jump("loc_3C15")

    label("loc_36FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C15")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #138
        "\x07\x05请选择取下零力场发生器的成员。\x02",
    )

    CloseMessageWindow()
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3765")
    Call(1, 17)
    Jump("loc_3769")

    label("loc_3765")

    Call(1, 18)

    label("loc_3769")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3790")
    Call(1, 17)
    Jump("loc_3794")

    label("loc_3790")

    Call(1, 18)

    label("loc_3794")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_37BB")
    Call(1, 17)
    Jump("loc_37BF")

    label("loc_37BB")

    Call(1, 18)

    label("loc_37BF")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_37E6")
    Call(1, 17)
    Jump("loc_37EA")

    label("loc_37E6")

    Call(1, 18)

    label("loc_37EA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3831"),
        (1, "loc_3877"),
        (2, "loc_38BD"),
        (3, "loc_3903"),
        (SWITCH_DEFAULT, "loc_3949"),
    )


    label("loc_3831")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3854")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3874")

    label("loc_3854")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3874")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3874")

    Jump("loc_3949")

    label("loc_3877")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_389A")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38BA")

    label("loc_389A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38BA")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38BA")

    Jump("loc_3949")

    label("loc_38BD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38E0")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3900")

    label("loc_38E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3900")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3900")

    Jump("loc_3949")

    label("loc_3903")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3926")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3946")

    label("loc_3926")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3946")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3946")

    Jump("loc_3949")

    label("loc_3949")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3972")

    AnonymousTalk(    #139
        "\x07\x05未装备零力场发生器。\x02",
    )

    Jump("loc_3C06")

    label("loc_3972")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39BA")

    AnonymousTalk(    #140
        (
            "\x07\x05艾丝蒂尔已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_3C06")

    label("loc_39BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A00")

    AnonymousTalk(    #141
        (
            "\x07\x05约修亚已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_3C06")

    label("loc_3A00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A48")

    AnonymousTalk(    #142
        (
            "\x07\x05雪拉扎德已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_3C06")

    label("loc_3A48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A90")

    AnonymousTalk(    #143
        (
            "\x07\x05奥利维尔已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_3C06")

    label("loc_3A90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD6")

    AnonymousTalk(    #144
        (
            "\x07\x05科洛丝已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_3C06")

    label("loc_3AD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1C")

    AnonymousTalk(    #145
        (
            "\x07\x05阿加特已取下零力场发生器，\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_3C06")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B87")

    AnonymousTalk(    #146
        (
            "\x07\x05提妲已取下零力场发生器，\x01",
            "无法使用魔法，战技，普通攻击。\x01",
            "但Ｓ战技『炮射冲击』仍可使用。\x02",
        )
    )

    Jump("loc_3C06")

    label("loc_3B87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BC7")

    AnonymousTalk(    #147
        (
            "\x07\x05金已取下零力场发生器\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )

    Jump("loc_3C06")

    label("loc_3BC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C06")

    AnonymousTalk(    #148
        (
            "\x07\x05凯文已取下零力场发生器\x01",
            "所以暂时无法使用魔法。\x02",
        )
    )


    label("loc_3C06")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_36FC")

    label("loc_3C15")

    Return()

    # Function_16_36DB end

    def Function_17_3C16(): pass

    label("Function_17_3C16")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3C43"),
        (1, "loc_3C5E"),
        (2, "loc_3C77"),
        (3, "loc_3C92"),
        (4, "loc_3CAD"),
        (5, "loc_3CC6"),
        (6, "loc_3CDF"),
        (7, "loc_3CF6"),
        (8, "loc_3D0B"),
        (SWITCH_DEFAULT, "loc_3D22"),
    )


    label("loc_3C43")

    OP_CC(0x1, 0x0, "【艾丝蒂尔　装备中】")
    Jump("loc_3D22")

    label("loc_3C5E")

    OP_CC(0x1, 0x0, "【约修亚　装备中】")
    Jump("loc_3D22")

    label("loc_3C77")

    OP_CC(0x1, 0x0, "【雪拉扎德　装备中】")
    Jump("loc_3D22")

    label("loc_3C92")

    OP_CC(0x1, 0x0, "【奥利维尔　装备中】")
    Jump("loc_3D22")

    label("loc_3CAD")

    OP_CC(0x1, 0x0, "【科洛丝　装备中】")
    Jump("loc_3D22")

    label("loc_3CC6")

    OP_CC(0x1, 0x0, "【阿加特　装备中】")
    Jump("loc_3D22")

    label("loc_3CDF")

    OP_CC(0x1, 0x0, "【提妲　装备中】")
    Jump("loc_3D22")

    label("loc_3CF6")

    OP_CC(0x1, 0x0, "【金　装备中】")
    Jump("loc_3D22")

    label("loc_3D0B")

    OP_CC(0x1, 0x0, "【凯文　装备中】")
    Jump("loc_3D22")

    label("loc_3D22")

    Return()

    # Function_17_3C16 end

    def Function_18_3D23(): pass

    label("Function_18_3D23")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3D50"),
        (1, "loc_3D6B"),
        (2, "loc_3D84"),
        (3, "loc_3D9F"),
        (4, "loc_3DBA"),
        (5, "loc_3DD3"),
        (6, "loc_3DEC"),
        (7, "loc_3E03"),
        (8, "loc_3E18"),
        (SWITCH_DEFAULT, "loc_3E2F"),
    )


    label("loc_3D50")

    OP_CC(0x1, 0x0, "【艾丝蒂尔　未装备】")
    Jump("loc_3E2F")

    label("loc_3D6B")

    OP_CC(0x1, 0x0, "【约修亚　未装备】")
    Jump("loc_3E2F")

    label("loc_3D84")

    OP_CC(0x1, 0x0, "【雪拉扎德　未装备】")
    Jump("loc_3E2F")

    label("loc_3D9F")

    OP_CC(0x1, 0x0, "【奥利维尔　未装备】")
    Jump("loc_3E2F")

    label("loc_3DBA")

    OP_CC(0x1, 0x0, "【科洛丝　未装备】")
    Jump("loc_3E2F")

    label("loc_3DD3")

    OP_CC(0x1, 0x0, "【阿加特　未装备】")
    Jump("loc_3E2F")

    label("loc_3DEC")

    OP_CC(0x1, 0x0, "【提妲　未装备】")
    Jump("loc_3E2F")

    label("loc_3E03")

    OP_CC(0x1, 0x0, "【金　未装备】")
    Jump("loc_3E2F")

    label("loc_3E18")

    OP_CC(0x1, 0x0, "【凯文　未装备】")
    Jump("loc_3E2F")

    label("loc_3E2F")

    Return()

    # Function_18_3D23 end

    SaveToFile()

Try(main)
