from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4121_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4121_1 ._SN',
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
        "Function_1_AF",           # 01, 1
        "Function_2_B4",           # 02, 2
        "Function_3_B9",           # 03, 3
        "Function_4_2AB",          # 04, 4
        "Function_5_491",          # 05, 5
        "Function_6_72E",          # 06, 6
        "Function_7_8DF",          # 07, 7
        "Function_8_BF5",          # 08, 8
        "Function_9_E39",          # 09, 9
        "Function_10_19F9",        # 0A, 10
        "Function_11_22A7",        # 0B, 11
        "Function_12_27F8",        # 0C, 12
        "Function_13_331C",        # 0D, 13
        "Function_14_44F3",        # 0E, 14
        "Function_15_4552",        # 0F, 15
        "Function_16_4596",        # 10, 16
        "Function_17_45E2",        # 11, 17
        "Function_18_4626",        # 12, 18
        "Function_19_4682",        # 13, 19
        "Function_20_473D",        # 14, 20
        "Function_21_4779",        # 15, 21
        "Function_22_47BF",        # 16, 22
        "Function_23_47E9",        # 17, 23
        "Function_24_4837",        # 18, 24
        "Function_25_4871",        # 19, 25
        "Function_26_48A3",        # 1A, 26
        "Function_27_48DB",        # 1B, 27
        "Function_28_4911",        # 1C, 28
        "Function_29_4939",        # 1D, 29
        "Function_30_4954",        # 1E, 30
        "Function_31_49A0",        # 1F, 31
        "Function_32_49C8",        # 20, 32
        "Function_33_4A29",        # 21, 33
        "Function_34_4A51",        # 22, 34
        "Function_35_4A93",        # 23, 35
        "Function_36_4AF2",        # 24, 36
        "Function_37_4CD6",        # 25, 37
        "Function_38_7C19",        # 26, 38
        "Function_39_7EB8",        # 27, 39
        "Function_40_7F9E",        # 28, 40
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Call(1, 12)
    Return()

    # Function_0_AA end

    def Function_1_AF(): pass

    label("Function_1_AF")

    Call(0, 37)
    Return()

    # Function_1_AF end

    def Function_2_B4(): pass

    label("Function_2_B4")

    Call(1, 9)
    Return()

    # Function_2_B4 end

    def Function_3_B9(): pass

    label("Function_3_B9")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_149")
    Jump("loc_18B")

    label("loc_149")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_165")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18B")

    label("loc_165")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_181")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18B")

    label("loc_181")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18B")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(    #0
        0xA,
        "#051F哟，怎么了？\x02",
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
        (0, "loc_220"),
        (SWITCH_DEFAULT, "loc_260"),
    )


    label("loc_220")


    ChrTalk(    #1
        0xA,
        (
            "#051F哦，知道了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_259")
    Call(0, 5)
    Jump("loc_25D")

    label("loc_259")

    Call(0, 4)

    label("loc_25D")

    Jump("loc_2A2")

    label("loc_260")


    ChrTalk(    #2
        0xA,
        (
            "#052F怎么，不调整了吗？\x02\x03",

            "#050F需要我的重剑时\x01",
            "尽管开口吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2")

    label("loc_2A2")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_3_B9 end

    def Function_4_2AB(): pass

    label("Function_4_2AB")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33B")
    Jump("loc_37D")

    label("loc_33B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_357")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37D")

    label("loc_357")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_373")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37D")

    label("loc_373")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37D")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(    #3
        0x9,
        "#020F嗯，怎么了？\x02",
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
        (0, "loc_412"),
        (SWITCH_DEFAULT, "loc_44B"),
    )


    label("loc_412")


    ChrTalk(    #4
        0x9,
        "#020F哎呀，要调整队伍吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_444")
    Call(0, 5)
    Jump("loc_448")

    label("loc_444")

    Call(0, 4)

    label("loc_448")

    Jump("loc_488")

    label("loc_44B")


    ChrTalk(    #5
        0x9,
        (
            "#020F呵呵，我就在这儿\x01",
            "休息吧。\x02\x03",

            "那么，之后就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_488")

    label("loc_488")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    # Function_4_2AB end

    def Function_5_491(): pass

    label("Function_5_491")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_521")
    Jump("loc_563")

    label("loc_521")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_53D")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_563")

    label("loc_53D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_559")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_563")

    label("loc_559")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_563")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(    #6
        0xB,
        "#030F哎呀，怎么了？\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_68E")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_601"),
        (SWITCH_DEFAULT, "loc_642"),
    )


    label("loc_601")


    ChrTalk(    #7
        0xB,
        (
            "#030F呵，原来如此。\x02\x03",

            "看来是需要\x01",
            "我这个天才的力量啊。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 4)
    Jump("loc_68B")

    label("loc_642")


    ChrTalk(    #8
        0xB,
        (
            "#030F哎呀，不要我了吗？\x02\x03",

            "呼，思恋我美妙的琴声时，\x01",
            "尽管来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B")

    label("loc_68B")

    Jump("loc_725")

    label("loc_68E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_69B"),
        (SWITCH_DEFAULT, "loc_6DC"),
    )


    label("loc_69B")


    ChrTalk(    #9
        0xB,
        (
            "#030F呵，原来如此。\x02\x03",

            "看来是需要\x01",
            "我这个天才的力量啊。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 2)
    Jump("loc_725")

    label("loc_6DC")


    ChrTalk(    #10
        0xB,
        (
            "#030F哎呀，不要我了吗？\x02\x03",

            "呼，思恋我美妙的琴声时，\x01",
            "尽管来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_725")

    label("loc_725")

    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_5_491 end

    def Function_6_72E(): pass

    label("Function_6_72E")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_762")

    ChrTalk(    #11
        0xC,
        (
            "#040F各位，辛苦了。\x02\x03",

            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BF")

    label("loc_762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_798")

    ChrTalk(    #12
        0xC,
        (
            "#040F各位，辛苦了。\x02\x03",

            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BF")

    label("loc_798")


    ChrTalk(    #13
        0xC,
        (
            "#040F各位，辛苦了。\x02\x03",

            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BF")

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
        (0, "loc_818"),
        (SWITCH_DEFAULT, "loc_8A6"),
    )


    label("loc_818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_848")

    ChrTalk(    #14
        0xC,
        (
            "#040F明白了。\x01",
            "要调整队伍吧？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 4)
    Jump("loc_8A3")

    label("loc_848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87D")

    ChrTalk(    #15
        0xC,
        (
            "#040F明白了。\x01",
            "要调整队伍吧？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 3)
    Jump("loc_8A3")

    label("loc_87D")


    ChrTalk(    #16
        0xC,
        (
            "#040F明白了。\x01",
            "要调整队伍吧？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 2)

    label("loc_8A3")

    Jump("loc_8DB")

    label("loc_8A6")


    ChrTalk(    #17
        0xC,
        (
            "#040F我在这里待命。\x02\x03",

            "如果有事，\x01",
            "请尽管开口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DB")

    label("loc_8DB")

    TalkEnd(0xC)
    Return()

    # Function_6_72E end

    def Function_7_8DF(): pass

    label("Function_7_8DF")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_920")

    ChrTalk(    #18
        0xD,
        (
            "#560F啊，阿加特哥哥。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98B")

    label("loc_920")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_95C")

    ChrTalk(    #19
        0xD,
        (
            "#060F啊，姐姐是你们。\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98B")

    label("loc_95C")


    ChrTalk(    #20
        0xD,
        (
            "#060F啊，姐姐是你们。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98B")

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
        (0, "loc_9E4"),
        (SWITCH_DEFAULT, "loc_B44"),
    )


    label("loc_9E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A32")

    ChrTalk(    #21
        0xD,
        (
            "#060F啊，嗯，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A58")

    label("loc_A32")


    ChrTalk(    #22
        0xD,
        (
            "#560F啊，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A58")

    Call(0, 5)
    Jump("loc_B41")

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_AD5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AA8")

    ChrTalk(    #23
        0xD,
        (
            "#060F啊，嗯，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACE")

    label("loc_AA8")


    ChrTalk(    #24
        0xD,
        (
            "#560F啊，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACE")

    Call(0, 4)
    Jump("loc_B41")

    label("loc_AD5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B17")

    ChrTalk(    #25
        0xD,
        (
            "#060F啊，嗯，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B3D")

    label("loc_B17")


    ChrTalk(    #26
        0xD,
        (
            "#560F啊，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3D")

    Call(0, 2)

    label("loc_B41")

    Jump("loc_BF1")

    label("loc_B44")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BA5")

    ChrTalk(    #27
        0xD,
        (
            "#064F咦，又不要了吗……？\x02\x03",

            "#060F我就在这里等，\x01",
            "有什么事就来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEE")

    label("loc_BA5")


    ChrTalk(    #28
        0xD,
        (
            "#064F咦，又不要了吗……？\x02\x03",

            "#060F我会在这里等的，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEE")

    Jump("loc_BF1")

    label("loc_BF1")

    TalkEnd(0xD)
    Return()

    # Function_7_8DF end

    def Function_8_BF5(): pass

    label("Function_8_BF5")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C85")
    Jump("loc_CC7")

    label("loc_C85")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CA1")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC7")

    label("loc_CA1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CBD")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC7")

    label("loc_CBD")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC7")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #29
        0xE,
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
        (0, "loc_D60"),
        (SWITCH_DEFAULT, "loc_DFF"),
    )


    label("loc_D60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8C")

    ChrTalk(    #30
        0xE,
        "#070F要调整队伍吧？\x02",
    )

    CloseMessageWindow()
    Call(0, 5)
    Jump("loc_DFC")

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_DB3")

    ChrTalk(    #31
        0xE,
        "#070F要调整队伍吧？\x02",
    )

    CloseMessageWindow()
    Call(0, 4)
    Jump("loc_DFC")

    label("loc_DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDF")

    ChrTalk(    #32
        0xE,
        "#070F要调整队伍吧？\x02",
    )

    CloseMessageWindow()
    Call(0, 3)
    Jump("loc_DFC")

    label("loc_DDF")


    ChrTalk(    #33
        0xE,
        "#070F要调整队伍吧？\x02",
    )

    CloseMessageWindow()
    Call(0, 2)

    label("loc_DFC")

    Jump("loc_E30")

    label("loc_DFF")


    ChrTalk(    #34
        0xE,
        (
            "#070F嗯，需要我的时候\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E30")

    label("loc_E30")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_8_BF5 end

    def Function_9_E39(): pass

    label("Function_9_E39")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_40(0x415, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1034")
    TurnDirection(0x19, 0x101, 0)

    ChrTalk(    #35
        0x19,
        "…………唔唔？\x02",
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x19,
        (
            "这、这不是如假包换的……\x01",
            "『特级钓师认定证书』吗！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1015F咦……啊啊，\x01",
            "罗伊德先生给的东西吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x19,
        (
            "唔，只有钓上湖之主的人\x01",
            "才能得到的特级钓师认定证书……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x19,
        (
            "同时也是我等的\x01",
            "同道之人的证据。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1016F是，是吗？\x02\x03",

            "（不知道是该\x01",
            "　高兴还是不高兴……）\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x19,
        (
            "而且，特级钓师\x01",
            "在我们师团本部\x01",
            "要多少钓饵就可以买多少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1018F啊，这有点\x01",
            "令人高兴……\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x19,
        "唔，是吧是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x19,
        (
            "如果需要鱼饵，\x01",
            "就尽管跟我说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20E7)
    TalkEnd(0x19)
    Return()

    label("loc_1034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 7)), scpexpr(EXPR_END)), "loc_1066")
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1055")
    OP_A9(0xDC)
    TalkEnd(0x19)
    Return()

    label("loc_1055")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1066")
    TalkEnd(0x19)
    Return()

    label("loc_1066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1070")
    Jump("loc_19F5")

    label("loc_1070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1183")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111E")

    ChrTalk(    #45
        0x19,
        (
            "哪怕导力器停了,\x01",
            "我们对钓鱼火热的\x01",
            "热情也不会冷却。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x19,
        (
            "这种时候，正应该\x01",
            "让市民们一起享受钓鱼的乐趣，\x01",
            "让心情平静下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x19,
        "还能确保食物，一石二鸟。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1180")

    label("loc_111E")


    ChrTalk(    #48
        0x19,
        (
            "这种时候，正应该\x01",
            "让市民们一起享受钓鱼的乐趣，\x01",
            "让心情平静下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x19,
        "还能确保食物，一石二鸟。\x02",
    )

    CloseMessageWindow()

    label("loc_1180")

    Jump("loc_19F5")

    label("loc_1183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_12B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1257")

    ChrTalk(    #50
        0x19,
        (
            "咱们的同伴佩苏尔\x01",
            "去调查洛连特的钓鱼场了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x19,
        (
            "如果找到不为人知的好地方，\x01",
            "说不定就潜藏着湖之主呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x19,
        (
            "而且还有在洛连特召开\x01",
            "讲习会的大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x19,
        (
            "对我们师团的发展来说,\x01",
            "他的任务至关重要。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_12B3")

    label("loc_1257")


    ChrTalk(    #54
        0x19,
        (
            "咱们的同伴佩苏尔\x01",
            "去调查洛连特的钓鱼场了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x19,
        (
            "对我们师团的发展来说\x01",
            "他的任务至关重要。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B3")

    Jump("loc_19F5")

    label("loc_12B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_1311")

    ChrTalk(    #56
        0x19,
        "看你似乎有点慌张……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x19,
        (
            "如果不冷静沉着观察\x01",
            "整个钓鱼场，是钓不到东西的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F5")

    label("loc_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_1465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1408")

    ChrTalk(    #58
        0x19,
        (
            "这瓦雷利亚湖里的湖之主\x01",
            "在过去１０年以上时间里,\x01",
            "可都重复着和我们钓公师团的死斗啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x19,
        (
            "要把那巨大的鱼\x01",
            "给钓上来是我们毕生的誓愿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x19,
        (
            "相信我们同心协力，\x01",
            "一定能够做到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x19,
        (
            "没有钓不上的鱼！\x01",
            "这就是我们钓公师团的座右铭。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1462")

    label("loc_1408")


    ChrTalk(    #62
        0x19,
        (
            "相信我们同心协力，\x01",
            "一定能够做到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x19,
        (
            "没有钓不上的鱼！\x01",
            "这就是我们钓公师团的座右铭。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1462")

    Jump("loc_19F5")

    label("loc_1465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_14F7")

    ChrTalk(    #64
        0x19,
        (
            "穿白裙子的少女\x01",
            "问了在下一个奇怪的问题，\x01",
            "已经走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x19,
        "问的问题记得是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x19,
        (
            "是『你知道又辣又苦又美味\x01",
            "的店在哪里吗？』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1536")

    label("loc_14F7")


    ChrTalk(    #67
        0x19,
        "唔，在找谁吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x19,
        (
            "现在这里除了我\x01",
            "和团员应该没别人了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1536")

    Jump("loc_19F5")

    label("loc_1539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_15B9")

    ChrTalk(    #69
        0x19,
        "师团创立已经２０年……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x19,
        (
            "赞同我们理念的\x01",
            "同志的数量稳步增加着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x19,
        (
            "唔嗯，为了纪念这个\x01",
            "打算召开盛大的活动……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F5")

    label("loc_15B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1610")

    ChrTalk(    #72
        0x19,
        (
            "不过今天打算早早\x01",
            "结束这边去瓦雷利亚湖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x19,
        "我今晚的目标是银伞鱼。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19F5")

    label("loc_1610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_175B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E4")

    ChrTalk(    #74
        0x19,
        (
            "跨越三国的互不侵犯条约……\x01",
            "是动力引起的响声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x19,
        (
            "……我们钓公师团也总有一天\x01",
            "会在帝国和共和国拥有支部。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x19,
        (
            "那时才能与游击士协会对抗\x01",
            "挂上『钓公师协会』的名号。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x19,
        "这是我小小的野心。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1758")

    label("loc_16E4")


    ChrTalk(    #78
        0x19,
        (
            "……我们钓公师团也总有一天\x01",
            "会在帝国和共和国拥有支部。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x19,
        (
            "那时才能与游击士协会对抗\x01",
            "挂上『钓公师协会』的名号。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1758")

    Jump("loc_19F5")

    label("loc_175B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_196D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191E")

    ChrTalk(    #80
        0x19,
        "哦哦，来得好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x19,
        (
            "我们『钓公师团』今天\x01",
            "也在积极准备活动,\x01",
            "为了钓上利贝尔全境的湖之主。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x12F,
        "#264F……湖之主，是什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12F, 400)

    ChrTalk(    #83
        0x101,
        (
            "#1015F嗯……\x01",
            "唔，也就是大鱼了。\x02\x03",

            "#1000F这里似乎是利贝尔\x01",
            "钓鱼迷们汇集的地方哦。\x02\x03",

            "玲和爸爸一起钓过鱼吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #84
        0x12F,
        (
            "#261F呵呵呵……\x01",
            "姐姐真是的。\x02\x03",

            "钓鱼不是小孩\x01",
            "和男人做的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1019F呜……\x01",
            "话，话是没错啦。\x02\x03",

            "#1016F但是，我也钓的哦。\x01",
            "很有趣嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x12F,
        (
            "#264F是吗？\x02\x03",

            "#265F那，玲下次\x01",
            "也试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x164D)
    Jump("loc_196A")

    label("loc_191E")


    ChrTalk(    #87
        0x19,
        (
            "你要是也喜欢钓鱼\x01",
            "随时都可以来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x19,
        (
            "我们衷心期盼着\x01",
            "有爱的人入团。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196A")

    Jump("loc_19F5")

    label("loc_196D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_19F5")

    ChrTalk(    #89
        0x19,
        (
            "哦哦！\x01",
            "欢迎来到『钓公师团』！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x19,
        (
            "我乃『钓鱼男爵』\x01",
            "是钓鱼者的团长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x19,
        (
            "诸位是志愿入团者吗？\x01",
            "如果喜欢钓鱼那可是热烈欢迎。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F5")

    TalkEnd(0x19)
    Return()

    # Function_9_E39 end

    def Function_10_19F9(): pass

    label("Function_10_19F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1A06")
    Jump("loc_22A3")

    label("loc_1A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A5E")

    ChrTalk(    #92
        0xFE,
        (
            "即使没有导力\x01",
            "也没什么好不安的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "和寻找湖之主露营的时候\x01",
            "完全一样嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A3")

    label("loc_1A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1B8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B11")

    ChrTalk(    #94
        0xFE,
        (
            "昨天去了港湾区\x01",
            "碰上了不得了的事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "战车跑出来，\x01",
            "还出现巨大人偶样的东西.\x01",
            "真是不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "从我的角度来说，\x01",
            "那附近的鱼会不会变敏感，\x01",
            "才是最担心的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1B8C")

    label("loc_1B11")


    ChrTalk(    #97
        0xFE,
        (
            "港湾区出现了战车，\x01",
            "还出现巨大人偶样的东西.\x01",
            "真是不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "从我的角度来说，\x01",
            "那附近的鱼会不会变敏感，\x01",
            "才是最担心的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8C")

    Jump("loc_22A3")

    label("loc_1B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_1BED")

    ChrTalk(    #99
        0xFE,
        (
            "好吧，明天难得要\x01",
            "挑战夜晚的瓦雷利亚湖！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "此外港湾区的仓库街\x01",
            "有很大的鱼哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A3")

    label("loc_1BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_1D07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA4")

    ChrTalk(    #101
        0xFE,
        (
            "根据报告瓦雷利亚湖的\x01",
            "湖之主好像还在柏斯地区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "我打算近日飞去柏斯地区\x01",
            "再次挑战那家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "上次就差一点点,\x01",
            "没想到鱼线断了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "这次一定，这次一定……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1D04")

    label("loc_1CA4")


    ChrTalk(    #105
        0xFE,
        (
            "根据报告瓦雷利亚湖的\x01",
            "湖之主好像还在柏斯地区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "我打算近日飞去柏斯地区\x01",
            "再次挑战那家伙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D04")

    Jump("loc_22A3")

    label("loc_1D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1E6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_END)), "loc_1D63")

    ChrTalk(    #107
        0xFE,
        (
            "刚才１楼有位穿着飘逸的\x01",
            "白裙子的女孩来过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "莫非是希望入团的人吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E6B")

    label("loc_1D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1D")

    ChrTalk(    #109
        0xFE,
        (
            "入团以后，有位女士的水平\x01",
            "是节节提高的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "她叫诺琪，\x01",
            "是诞辰庆典前后入团的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "前阵子终于钓上了湖之主\x01",
            "成为和我同级的特级钓师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "这下，我也\x01",
            "不能不当回事了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1E6B")

    label("loc_1E1D")


    ChrTalk(    #113
        0xFE,
        (
            "入团以后，有位女士的水平\x01",
            "是节节提高的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "这下，我也\x01",
            "不能不当回事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E6B")

    Jump("loc_22A3")

    label("loc_1E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1EE6")

    ChrTalk(    #115
        0xFE,
        (
            "作为普及钓鱼文化的\x01",
            "一环我们打算\x01",
            "开拓新的钓鱼场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "不仅如此\x01",
            "为了不使钓鱼场荒废\x01",
            "还要进行环境保护活动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A3")

    label("loc_1EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F47")

    ChrTalk(    #117
        0xFE,
        (
            "糟糕！！\x01",
            "已经到黄昏时间了吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "这个时间不去钓鱼场\x01",
            "多么可惜啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1F8A")

    label("loc_1F47")


    ChrTalk(    #119
        0xFE,
        (
            "傍晚的这个时间，\x01",
            "鱼很活跃非常容易钓起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "没理由错过这个。\x02",
    )

    CloseMessageWindow()

    label("loc_1F8A")

    Jump("loc_22A3")

    label("loc_1F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1FFF")

    ChrTalk(    #121
        0xFE,
        "钓鱼就是和自然作战。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "经常使出全力\x01",
            "也无法顺自己的意行事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "呵呵……\x01",
            "这也是钓鱼的奥妙所在。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A3")

    label("loc_1FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_20F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20AC")

    ChrTalk(    #124
        0xFE,
        (
            "格兰赛尔地区水边比较少,\x01",
            "应该钓鱼场也少吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "但是且慢！\x01",
            "附近有意外的好地方哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "艾尔贝离宫附近\x01",
            "的罗马尔池知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "那里的鱼影相当多哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_20ED")

    label("loc_20AC")


    ChrTalk(    #128
        0xFE,
        (
            "艾尔贝离宫附近\x01",
            "的罗马尔池知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "那里的鱼影相当多哦。\x02",
    )

    CloseMessageWindow()

    label("loc_20ED")

    Jump("loc_22A3")

    label("loc_20F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_22A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2249")
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #130
        0xFE,
        "咦…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1004F啊，罗伊德先生？\x01",
            "从卢安回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "钓果如何。\x01",
            "给你的鱼竿好用吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#1016F啊，嗯，\x01",
            "工作间歇不时有用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "像你这样有资质的人，\x01",
            "钓公师团是热烈欢迎哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "想入团的时候，\x01",
            "随时都可以跟团长说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "他啊，\x01",
            "一定会高兴得举双手赞成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        (
            "#1008F啊哈哈……\x01",
            "会考虑的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x164E)
    Jump("loc_22A3")

    label("loc_2249")


    ChrTalk(    #139
        0xFE,
        (
            "像你这样有资质的人，\x01",
            "钓公师团是热烈欢迎哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "想入团的时候，\x01",
            "随时都可以跟团长说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A3")

    TalkEnd(0xFE)
    Return()

    # Function_10_19F9 end

    def Function_11_22A7(): pass

    label("Function_11_22A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_22B4")
    Jump("loc_27F4")

    label("loc_22B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_232D")

    ChrTalk(    #141
        0xFE,
        (
            "我们的团员平常\x01",
            "就适应了户外生活嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "可不像其他人那样\x01",
            "惊惶失措哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "罗伊德似乎摩擦树木\x01",
            "生起了火。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27F4")

    label("loc_232D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2337")
    Jump("loc_27F4")

    label("loc_2337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_237C")

    ChrTalk(    #144
        0xFE,
        (
            "之后预定是\x01",
            "和团长碰头来着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "听说有新任务给我呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27F4")

    label("loc_237C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_23B3")

    ChrTalk(    #146
        0xFE,
        (
            "呼，正想着肚子饿了\x01",
            "原来已经到晚上了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27F4")

    label("loc_23B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2472")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_END)), "loc_240B")

    ChrTalk(    #147
        0xFE,
        (
            "最近女性的钓鱼迷\x01",
            "好像也在增加呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "作为我们来说是热烈欢迎啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_246F")

    label("loc_240B")


    ChrTalk(    #149
        0xFE,
        (
            "导力照相机普及之后\x01",
            "就不太取鱼的拓本了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "但是，大家伙上钩的时候\x01",
            "还是想用那样的形态留下呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246F")

    Jump("loc_27F4")

    label("loc_2472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_249B")

    ChrTalk(    #151
        0xFE,
        (
            "嗯～今天\x01",
            "去哪里钓鱼呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27F4")

    label("loc_249B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_256C")

    ChrTalk(    #152
        0xFE,
        (
            "讲习中带初学者出去,\x01",
            "晕船的人也很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "作为对策要保持充足睡眠。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "还有，乘船前\x01",
            "肚子不要吃得太饱哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "特别是刚刚开始钓鱼的人,\x01",
            "经常为了前一天的准备，\x01",
            "来的时候都睡眠不足。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_25DB")

    label("loc_256C")


    ChrTalk(    #156
        0xFE,
        (
            "讲习中带初学者出去,\x01",
            "晕船的人也很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "作为对策要保持充足睡眠。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "还有，乘船前\x01",
            "肚子不要吃得太饱哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DB")

    Jump("loc_27F4")

    label("loc_25DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_265E")

    ChrTalk(    #159
        0xFE,
        (
            "想起来政变的时候\x01",
            "可真惨啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "明明持续着钓鱼的绝好天气,\x01",
            "却禁止夜间外出……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "对我们来说\x01",
            "简直是残酷的折磨。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27F4")

    label("loc_265E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_27A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274A")

    ChrTalk(    #162
        0xFE,
        (
            "钓公师团的团员是根据实绩\x01",
            "来编排等级。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "钓过所谓湖之主的\x01",
            "罗伊德是『特级钓师』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "还和初学者一样的我,\x01",
            "就是『初级钓师』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "顺带一提,团长有着\x01",
            "一个自己独特的等级称号……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "叫做『太公望』。\x01",
            "真有型啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_27A1")

    label("loc_274A")


    ChrTalk(    #167
        0xFE,
        (
            "钓公师团的团员是根据实绩\x01",
            "来编排等级。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "还和初学者一样的我,\x01",
            "就是『初级钓师』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27A1")

    Jump("loc_27F4")

    label("loc_27A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_27F4")

    ChrTalk(    #169
        0xFE,
        "潜藏在各地钓鱼场的湖之主……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "我也希望有一天\x01",
            "能钓上湖之主来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F4")

    TalkEnd(0xFE)
    Return()

    # Function_11_22A7 end

    def Function_12_27F8(): pass

    label("Function_12_27F8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3109")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2987")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇哪里都没恢复通信】\x01",            # 0
            "【◇只有洛连特恢复了通信】\x01",        # 1
            "【◇只有卢安恢复了通信】\x01",          # 2
            "【◇只有蔡斯恢复了通信】\x01",          # 3
            "【◇洛连特·卢安恢复了通信】\x01",      # 4
            "【◇洛连特·蔡斯恢复了通信】\x01",      # 5
            "【◇卢安·蔡斯恢复了通信】\x01",        # 6
            "【◇什么也没有变更】\x01",              # 7
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2933"),
        (1, "loc_293F"),
        (2, "loc_294B"),
        (3, "loc_2957"),
        (4, "loc_2963"),
        (5, "loc_296F"),
        (6, "loc_297B"),
        (SWITCH_DEFAULT, "loc_2987"),
    )


    label("loc_2933")

    OP_A3(0x2003)
    OP_A3(0x2001)
    OP_A3(0x2005)
    Jump("loc_2987")

    label("loc_293F")

    OP_A2(0x2003)
    OP_A3(0x2001)
    OP_A3(0x2005)
    Jump("loc_2987")

    label("loc_294B")

    OP_A3(0x2003)
    OP_A2(0x2001)
    OP_A3(0x2005)
    Jump("loc_2987")

    label("loc_2957")

    OP_A3(0x2003)
    OP_A3(0x2001)
    OP_A2(0x2005)
    Jump("loc_2987")

    label("loc_2963")

    OP_A2(0x2003)
    OP_A2(0x2001)
    OP_A3(0x2005)
    Jump("loc_2987")

    label("loc_296F")

    OP_A2(0x2003)
    OP_A3(0x2001)
    OP_A2(0x2005)
    Jump("loc_2987")

    label("loc_297B")

    OP_A3(0x2003)
    OP_A2(0x2001)
    OP_A2(0x2005)
    Jump("loc_2987")

    label("loc_2987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3001")

    ChrTalk(    #171
        0x8,
        (
            "#763F哎呀……\x02\x03",

            "#760F各位，还有……约修亚。\x02\x03",

            "欢迎你们，\x01",
            "终于回到这里了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x102,
        (
            "#1040F艾南先生……\x01",
            "抱歉让您担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#761F哪里，没事就好。\x02\x03",

            "#760F今后还是作为游击士协会\x01",
            "的同伴，请多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1002F艾南先生，事不宜迟，\x01",
            "王都的状况怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        (
            "#764F这个啊，导力器\x01",
            "突然不能使用时\x01",
            "城中确实是一片混乱。\x02\x03",

            "#762F对面的工房也是，\x01",
            "寻求修理的市民一齐涌来。\x02\x03",

            "#760F然而，那里立刻\x01",
            "放出了艾莉茜雅女王发出的布告。\x02\x03",

            "说导力停止的原因正在调查中。\x01",
            "请大家镇定下来，\x01",
            "像平常一样生活───\x02\x03",

            "因此市里并没发生大的\x01",
            "纠纷和恐慌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        "#1018F原来如此，不愧是女王陛下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "#762F嗯嗯……然而，\x01",
            "湖上出现了贝壳样物体……\x02\x03",

            "许多市民担心是由其导致\x01",
            "导力停止而开始不安的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x102,
        "#1042F原来如此，也难怪啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x8,
        (
            "#762F现在港口参观\x01",
            "那个物体的人好像增加了。\x02\x03",

            "其他奇怪的事情，\x01",
            "就是王城的大门由于\x01",
            "导力停止无法开关了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#1015F是吗……不过，大家\x01",
            "似乎比想象中镇定得多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x8,
        (
            "#760F是的……但是，这个情况\x01",
            "如果持续下去难说不会引起混乱。\x02\x03",

            "我们也想分秒必争地\x01",
            "收集到各地的正确情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x102,
        (
            "#1035F因此要去各个支部\x01",
            "恢复通信，确保正确的情报……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1006F就是说我们的任务\x01",
            "相当重要吧。\x02\x03",

            "#1002F好，得鼓起\x01",
            "干劲来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E2F")

    ChrTalk(    #184
        0x102,
        (
            "#1042F洛连特、卢安、\x01",
            "还有蔡斯……\x02\x03",

            "哪里都好，\x01",
            "赶快把『零力场发生器』送去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F94")

    label("loc_2E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E70")

    ChrTalk(    #185
        0x102,
        (
            "#1040F剩下的是卢安，\x01",
            "还有蔡斯的协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F94")

    label("loc_2E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EB3")

    ChrTalk(    #186
        0x102,
        (
            "#1040F剩下的是洛连特，\x01",
            "还有蔡斯的协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F94")

    label("loc_2EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EF6")

    ChrTalk(    #187
        0x102,
        (
            "#1040F剩下的是洛连特，\x01",
            "还有卢安的协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F94")

    label("loc_2EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F2B")

    ChrTalk(    #188
        0x102,
        "#1040F剩下的是蔡斯的协会吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F94")

    label("loc_2F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F60")

    ChrTalk(    #189
        0x102,
        "#1040F剩下的是卢安的协会吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F94")

    label("loc_2F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F94")

    ChrTalk(    #190
        0x102,
        "#1040F剩下的是洛连特的协会吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2F94")


    ChrTalk(    #191
        0x101,
        "#1000F嗯，得赶快了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x8,
        (
            "#760F说利贝尔的治安维持\x01",
            "全看各位的努力\x01",
            "也不为过。\x02\x03",

            "就请多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20DA)
    TalkEnd(0x8)
    Return()

    label("loc_3001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3109")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_30AC")

    ChrTalk(    #193
        0x8,
        (
            "#762F这附近的居民\x01",
            "已经去协会避难了。\x02\x03",

            "在其他的街区，军队也\x01",
            "应该已经在做避难引导了。\x02\x03",

            "各位，快去追\x01",
            "前往城堡的执行者们吧。\x02\x03",

            "#765F他们的目的恐怕是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3106")

    label("loc_30AC")


    ChrTalk(    #194
        0x8,
        (
            "#760F说利贝尔的治安维持\x01",
            "全看各位的努力\x01",
            "也不为过。\x02\x03",

            "请刻不容缓地\x01",
            "恢复各支部的通信机。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3106")

    OP_A2(0x20DB)

    label("loc_3109")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3172")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "报告\x01",          # 1
            "呼叫同伴\x01",      # 2
            "离开\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_3176")

    label("loc_3172")

    Call(6, 5)

    label("loc_3176")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3245")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31A0")
    OP_28(0xC3, 0x4, 0x20)

    label("loc_31A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0xCD)"), scpexpr(EXPR_END)), "loc_31F3")

    ChrTalk(    #195
        0x8,
        (
            "#760F辛苦了。\x01",
            "看来顺利达到目的了。\x02\x03",

            "完成了什么任务的话\x01",
            "请再来报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_31F3")


    ChrTalk(    #196
        0x8,
        (
            "#760F现在\x01",
            "好像没有能报告的工作呢。\x02\x03",

            "完成了什么任务的话\x01",
            "请再来报告。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323C")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_3245")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3306")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32FF")

    ChrTalk(    #197
        0x8,
        (
            "#760F把大家都叫来这里吗？\x02\x03",

            "明白了。\x01",
            "那么我马上去联络。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #198
        (
            "\x07\x05联络各支部，\x01",
            "集合了待命人员。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_32FF")

    TalkEnd(0x8)
    Return()

    label("loc_3306")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3317")
    TalkEnd(0x8)
    Return()

    label("loc_3317")

    Call(1, 13)
    Return()

    # Function_12_27F8 end

    def Function_13_331C(): pass

    label("Function_13_331C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_33BF")

    ChrTalk(    #199
        0x8,
        (
            "#762F这附近的居民\x01",
            "已经去协会避难了。\x02\x03",

            "在其他的街区，军队也\x01",
            "应该已经在做避难引导了。\x02\x03",

            "各位，快去追\x01",
            "前往城堡的执行者们吧。\x02\x03",

            "#765F他们的目的恐怕是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44EF")

    label("loc_33BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3780")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_343F")

    ChrTalk(    #200
        0x8,
        (
            "#760F说利贝尔的治安维持\x01",
            "全看各位的努力\x01",
            "也不为过。\x02\x03",

            "洛连特，卢安，蔡斯……\x01",
            "请恢复各支部的通信。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_377D")

    label("loc_343F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34CA")

    ChrTalk(    #201
        0x8,
        (
            "#760F通信还没回复的是\x01",
            "卢安，还有蔡斯支部。\x02\x03",

            "利贝尔的治安维持\x01",
            "全看各位的努力\x01",
            "也不为过。\x02\x03",

            "劳你跑一趟了，\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_377D")

    label("loc_34CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_355B")

    ChrTalk(    #202
        0x8,
        (
            "#760F通信还没回复的是\x01",
            "是洛连特，还有蔡斯支部吧。\x02\x03",

            "利贝尔的治安维持\x01",
            "全看各位的努力\x01",
            "也不为过。\x02\x03",

            "劳你跑一趟了，\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_377D")

    label("loc_355B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35EC")

    ChrTalk(    #203
        0x8,
        (
            "#760F通信还没回复的是\x01",
            "是洛连特，还有卢安支部吧。\x02\x03",

            "利贝尔的治安维持\x01",
            "全看各位的努力\x01",
            "也不为过。\x02\x03",

            "劳你跑一趟了，\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_377D")

    label("loc_35EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3672")

    ChrTalk(    #204
        0x8,
        (
            "#760F通信还没回复的是\x01",
            "只有蔡斯支部吧。\x02\x03",

            "利贝尔的治安维持\x01",
            "全看各位的努力\x01",
            "也不为过。\x02\x03",

            "劳你跑一趟了，\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_377D")

    label("loc_3672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36F8")

    ChrTalk(    #205
        0x8,
        (
            "#760F通信还没回复的是\x01",
            "只有卢安支部吧。\x02\x03",

            "利贝尔的治安维持\x01",
            "全看各位的努力\x01",
            "也不为过。\x02\x03",

            "劳你跑一趟了，\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_377D")

    label("loc_36F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_377D")

    ChrTalk(    #206
        0x8,
        (
            "#760F通信还没回复的是\x01",
            "只有洛连特支部吧。\x02\x03",

            "利贝尔的治安维持\x01",
            "全看各位的努力\x01",
            "也不为过。\x02\x03",

            "劳你跑一趟了，\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_377D")

    Jump("loc_44EF")

    label("loc_3780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_380E")

    ChrTalk(    #207
        0x8,
        (
            "#760F接下来请前往\x01",
            "空贼团出现的柏斯地区。\x02\x03",

            "我已经联络飞船坪\x01",
            "安排了船票的事。\x02\x03",

            "准备好之后，请立即\x01",
            "前往飞船坪接待处办理搭乘手续。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44EF")

    label("loc_380E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_41DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 4)), scpexpr(EXPR_END)), "loc_388A")

    ChrTalk(    #208
        0x8,
        (
            "#760F艾丝蒂尔，\x01",
            "找到玲了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#1000F不，还没有。\x01",
            "不过，总算快要抓到了。\x02\x03",

            "（得赶快去空港才行……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41D8")

    label("loc_388A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 3)), scpexpr(EXPR_END)), "loc_3BE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 6)), scpexpr(EXPR_END)), "loc_3916")

    ChrTalk(    #210
        0x8,
        (
            "#760F没人管就会消失的点心……吗。\x02\x03",

            "说不定是说路上的\x01",
            "货摊卖的点心。\x02\x03",

            "糖果，爆米花，\x01",
            "葡萄干，还有冰淇淋……\x02\x03",

            "是这些吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BE6")

    label("loc_3916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B0C")

    ChrTalk(    #211
        0x8,
        (
            "#760F艾丝蒂尔，\x01",
            "找到玲了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        "#1000F不，还没有。\x02",
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
            "【商量关于玲的事】\x01",      # 0
            "【没什么好商量的】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AA0")

    AnonymousTalk(    #213
        "\x07\x05艾丝蒂尔向艾南说明了经过。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #214
        0x8,
        (
            "#764F没人管就会消失的点心，对吗。\x02\x03",

            "#760F说到点心，格兰赛尔的\x01",
            "路边摊上很多哦。\x02\x03",

            "说不定是指货摊卖的\x01",
            "货摊卖的点心。\x02\x03",

            "糖果，爆米花，\x01",
            "葡萄干，还有冰淇淋……\x02\x03",

            "#761F是这些吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1686)
    Jump("loc_3B06")

    label("loc_3AA0")

    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #215
        0x8,
        (
            "#761F……话说回来\x01",
            "真是会藏的孩子啊。\x02\x03",

            "#760F艾丝蒂尔在离宫\x01",
            "很难找到也值得肯定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B06")

    OP_A2(0x3)
    Jump("loc_3BE6")

    label("loc_3B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B6B")

    ChrTalk(    #216
        0x8,
        (
            "#761F……话说回来\x01",
            "真是会藏的孩子啊。\x02\x03",

            "#760F艾丝蒂尔在离宫\x01",
            "很难找到也值得肯定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BE6")

    label("loc_3B6B")


    ChrTalk(    #217
        0x8,
        (
            "#760F没人管就会消失的点心……吗。\x02\x03",

            "说不定是说路上的\x01",
            "货摊卖的点心。\x02\x03",

            "糖果，爆米花，\x01",
            "葡萄干，还有冰淇淋……\x02\x03",

            "是这些吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE6")

    Jump("loc_41D8")

    label("loc_3BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_3ED4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 5)), scpexpr(EXPR_END)), "loc_3C53")

    ChrTalk(    #218
        0x8,
        (
            "#760F又辣又苦又美味的店……是吗。\x02\x03",

            "这么说来，以前熟人\x01",
            "请我吃过辣的东西\x01",
            "这我说过吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED1")

    label("loc_3C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E37")

    ChrTalk(    #219
        0x8,
        (
            "#760F如何，\x01",
            "玲在吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        "#1007F这个……\x02",
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
            "【商量关于玲的事】\x01",      # 0
            "【没什么好商量的】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD4")

    AnonymousTalk(    #221
        "\x07\x05艾丝蒂尔向艾南说明了经过。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #222
        0x8,
        (
            "#764F又辣又苦又美味的店，对吗。\x02\x03",

            "#760F说起来，艾丝蒂尔……\x02\x03",

            "以前熟人\x01",
            "请我吃过辣的东西\x01",
            "这我说过吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1011F啊……奈尔的事吧。\x02\x03",

            "#1015F记得是哪里的\x01",
            "咖啡店或者是酒馆吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1685)
    Jump("loc_3E31")

    label("loc_3DD4")

    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #224
        0x8,
        (
            "#761F能够逃离正游击士的追捕\x01",
            "玲也相当有一套呢。\x02\x03",

            "#760F各位，请加油吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E31")

    OP_A2(0x3)
    Jump("loc_3ED1")

    label("loc_3E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E78")

    ChrTalk(    #225
        0x8,
        (
            "#761F能够逃离正游击士的追捕，\x01",
            "玲也相当有一套呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED1")

    label("loc_3E78")


    ChrTalk(    #226
        0x8,
        (
            "#760F又辣又苦又美味的店……是吗。\x02\x03",

            "这么说来，以前熟人\x01",
            "请我吃过辣的东西\x01",
            "这我说过吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED1")

    Jump("loc_41D8")

    label("loc_3ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_END)), "loc_417A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 4)), scpexpr(EXPR_END)), "loc_3F32")

    ChrTalk(    #227
        0x8,
        (
            "#760F和鱼有关系的\x01",
            "建筑物我有印象哦。\x02\x03",

            "就是这个游击士协会\x01",
            "隔壁的建筑物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4177")

    label("loc_3F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40FF")

    ChrTalk(    #228
        0x8,
        (
            "#760F哎呀，各位……\x01",
            "找到玲了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        "#1007F这个……\x02",
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
            "【商量关于玲的事】\x01",      # 0
            "【没什么好商量的】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40AC")

    AnonymousTalk(    #230
        "\x07\x05艾丝蒂尔向艾南说明了经过。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #231
        0x8,
        (
            "#764F无色的鱼……是吗。\x02\x03",

            "#760F无色，这\x01",
            "部分不太明白……\x02\x03",

            "不过和鱼有关的\x01",
            "建筑物我有印象哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        "#1004F真的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x8,
        (
            "#761F嗯嗯，就在这个游击士协会\x01",
            "的隔壁。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1684)
    Jump("loc_40F9")

    label("loc_40AC")

    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #234
        0x8,
        (
            "#762F……看来\x01",
            "好像搁浅了呢。\x02\x03",

            "玲到底，\x01",
            "去哪里了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40F9")

    OP_A2(0x3)
    Jump("loc_4177")

    label("loc_40FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_412A")

    ChrTalk(    #235
        0x8,
        (
            "#762F玲到底\x01",
            "去哪里了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4177")

    label("loc_412A")


    ChrTalk(    #236
        0x8,
        (
            "#760F和鱼有关系的\x01",
            "建筑物我有印象哦。\x02\x03",

            "就是这个游击士协会\x01",
            "隔壁的建筑物。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4177")

    Jump("loc_41D8")

    label("loc_417A")


    ChrTalk(    #237
        0x8,
        (
            "#760F而我就去进行\x01",
            "各地支部和情报部的余党\x01",
            "的情报交换工作吧。\x02\x03",

            "艾丝蒂尔你们\x01",
            "请把玲带回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41D8")

    Jump("loc_44EF")

    label("loc_41DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_41E5")
    Jump("loc_44EF")

    label("loc_41E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_431C")

    ChrTalk(    #238
        0x8,
        (
            "#760F哎呀，艾丝蒂尔。\x01",
            "探听结束了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        (
            "#1015F嗯……\x01",
            "在大使馆和城里听说了。\x02\x03",

            "#1000F之后要见见\x01",
            "利贝尔通讯的奈尔才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_42CB")

    ChrTalk(    #240
        0x8,
        (
            "#760F那么，你们那边完成后\x01",
            "麻烦赶快来报告。\x02\x03",

            "雪拉扎德应该\x01",
            "也快回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4316")

    label("loc_42CB")


    ChrTalk(    #241
        0x8,
        (
            "#760F那么，你们那边完成后\x01",
            "麻烦赶快来报告。\x02\x03",

            "阿加特差不多\x01",
            "也快回来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4316")

    OP_A2(0x3)
    Jump("loc_43C0")

    label("loc_431C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4373")

    ChrTalk(    #242
        0x8,
        (
            "#760F在利贝尔通讯的探听\x01",
            "结束之后请回这里来。\x02\x03",

            "阿加特差不多\x01",
            "也快回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C0")

    label("loc_4373")


    ChrTalk(    #243
        0x8,
        (
            "#760F在利贝尔通讯的探听\x01",
            "结束之后请回这里来。\x02\x03",

            "雪拉扎德应该\x01",
            "也快回来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C0")

    Jump("loc_44EF")

    label("loc_43C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4478")

    ChrTalk(    #244
        0x8,
        (
            "#760F按之前说好的，艾丝蒂尔小姐请\x01",
            "去帝国、共和国大使馆和格兰赛尔城和\x01",
            "利贝尔通讯社。\x02\x03",

            "关于各大使馆，就拜托金先生和\x01",
            "奥利维尔先生帮忙。\x02\x03",

            "关于格兰赛尔城\x01",
            "就拜托殿下您了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44EF")

    label("loc_4478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_4482")
    Jump("loc_44EF")

    label("loc_4482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_44EF")

    ChrTalk(    #245
        0x8,
        (
            "#760F在艾尔贝离宫工作的\x01",
            "管家雷蒙德先生，\x01",
            "负责看管迷路的孩子。\x02\x03",

            "如果到了艾尔贝离宫\x01",
            "请先问问他看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44EF")

    TalkEnd(0x8)
    Return()

    # Function_13_331C end

    def Function_14_44F3(): pass

    label("Function_14_44F3")

    TalkBegin(0xFE)

    ChrTalk(    #246
        0xFE,
        (
            "突、突然就有穿着\x01",
            "红色铠甲的家伙袭击过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "虽说早习惯了麻烦，\x01",
            "这次真是吓坏了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_44F3 end

    def Function_15_4552(): pass

    label("Function_15_4552")

    TalkBegin(0xFE)

    ChrTalk(    #248
        0xFE,
        (
            "哆哆嗦嗦……\x01",
            "颤抖不停……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        "那些人，真打算把我们……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_4552 end

    def Function_16_4596(): pass

    label("Function_16_4596")

    TalkBegin(0xFE)

    ChrTalk(    #250
        0xFE,
        "他、他们是什么人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "那样子奇怪的４个人\x01",
            "好像是他们的首领……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_4596 end

    def Function_17_45E2(): pass

    label("Function_17_45E2")

    TalkBegin(0xFE)

    ChrTalk(    #252
        0xFE,
        (
            "不止导力器不能使用\x01",
            "还碰上这样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        "太过分了……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_45E2 end

    def Function_18_4626(): pass

    label("Function_18_4626")

    TalkBegin(0xFE)

    ChrTalk(    #254
        0xFE,
        "那些家伙是帝国军吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "破坏好不容易定下的条约，\x01",
            "会做这种事的除了帝国还有谁！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_4626 end

    def Function_19_4682(): pass

    label("Function_19_4682")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 7)), scpexpr(EXPR_END)), "loc_46F5")

    ChrTalk(    #256
        0xFE,
        (
            "袭、袭击我们的人中\x01",
            "有个白衣服的女人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "士兵一转眼\x01",
            "就被她干掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        "是、是不是看错了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4739")

    label("loc_46F5")


    ChrTalk(    #259
        0xFE,
        (
            "痛痛痛……\x01",
            "逃跑的时候跌倒受伤了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "爸爸和妈妈\x01",
            "不要紧吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4739")

    TalkEnd(0xFE)
    Return()

    # Function_19_4682 end

    def Function_20_473D(): pass

    label("Function_20_473D")

    TalkBegin(0xFE)

    ChrTalk(    #261
        0xFE,
        (
            "王国军的人\x01",
            "带我来这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        "那些人不要紧吗？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_473D end

    def Function_21_4779(): pass

    label("Function_21_4779")

    TalkBegin(0xFE)

    ChrTalk(    #263
        0xFE,
        (
            "为、为什么那些人\x01",
            "要袭击我们呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        "我们完全没做坏事啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_4779 end

    def Function_22_47BF(): pass

    label("Function_22_47BF")

    TalkBegin(0xFE)

    ChrTalk(    #265
        0xFE,
        (
            "混帐！\x01",
            "我的店到底怎么回事！？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_47BF end

    def Function_23_47E9(): pass

    label("Function_23_47E9")

    TalkBegin(0xFE)

    ChrTalk(    #266
        0xFE,
        (
            "把打算留在店里的塞森\x01",
            "硬拖走去避难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "千钧一发，真是危险啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_47E9 end

    def Function_24_4837(): pass

    label("Function_24_4837")

    TalkBegin(0xFE)

    ChrTalk(    #268
        0xFE,
        (
            "王国军的士兵们\x01",
            "竟会被仅仅４人……难以置信……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_4837 end

    def Function_25_4871(): pass

    label("Function_25_4871")

    TalkBegin(0xFE)

    ChrTalk(    #269
        0xFE,
        (
            "啊啊，怎么回事……\x01",
            "王都……在燃烧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_4871 end

    def Function_26_48A3(): pass

    label("Function_26_48A3")

    TalkBegin(0xFE)

    ChrTalk(    #270
        0xFE,
        (
            "士兵们叫我\x01",
            "去避难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        "那个士兵没事吧……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_48A3 end

    def Function_27_48DB(): pass

    label("Function_27_48DB")

    TalkBegin(0xFE)

    ChrTalk(    #272
        0xFE,
        (
            "怎、怎么回事……\x01",
            "那些家伙到底是什么人！？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_48DB end

    def Function_28_4911(): pass

    label("Function_28_4911")

    TalkBegin(0xFE)

    ChrTalk(    #273
        0xFE,
        (
            "在柏斯的罗伊德\x01",
            "不要紧吗……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_4911 end

    def Function_29_4939(): pass

    label("Function_29_4939")

    TalkBegin(0xFE)

    ChrTalk(    #274
        0xFE,
        "婆婆，没事吗？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_4939 end

    def Function_30_4954(): pass

    label("Function_30_4954")

    TalkBegin(0xFE)

    ChrTalk(    #275
        0xFE,
        (
            "没事的，女神大人\x01",
            "或者女王陛下会想办法的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "努力忍耐吧……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_4954 end

    def Function_31_49A0(): pass

    label("Function_31_49A0")

    TalkBegin(0xFE)

    ChrTalk(    #277
        0xFE,
        (
            "帮、帮帮忙！\x01",
            "王都，王都……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_49A0 end

    def Function_32_49C8(): pass

    label("Function_32_49C8")

    TalkBegin(0xFE)

    ChrTalk(    #278
        0xFE,
        (
            "率领红色士兵\x01",
            "的４人向王城那边去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "女王陛下和科洛蒂娅公主\x01",
            "不知道要不要紧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_49C8 end

    def Function_33_4A29(): pass

    label("Function_33_4A29")

    TalkBegin(0xFE)

    ChrTalk(    #280
        0xFE,
        (
            "啊哇哇……\x01",
            "怎么会变成这样？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_4A29 end

    def Function_34_4A51(): pass

    label("Function_34_4A51")

    TalkBegin(0xFE)

    ChrTalk(    #281
        0xFE,
        (
            "这……\x01",
            "难道是战争？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "刚刚才缔结了互不侵犯条约……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_4A51 end

    def Function_35_4A93(): pass

    label("Function_35_4A93")

    TalkBegin(0xFE)

    ChrTalk(    #283
        0xFE,
        (
            "哪怕建筑物被烧毁，\x01",
            "钓公师团也不会灭亡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "只要我们的心中\x01",
            "还燃烧着对钓鱼的热情。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_4A93 end

    def Function_36_4AF2(): pass

    label("Function_36_4AF2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C01")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇集齐了全部『牌技师杰克』】\x01",      # 0
            "【◇没集齐全部『牌技师杰克』】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B6F"),
        (1, "loc_4BB8"),
        (SWITCH_DEFAULT, "loc_4C01"),
    )


    label("loc_4B6F")

    OP_3E(0x23A, 1)
    OP_3E(0x23B, 1)
    OP_3E(0x23C, 1)
    OP_3E(0x23D, 1)
    OP_3E(0x23E, 1)
    OP_3E(0x23F, 1)
    OP_3E(0x240, 1)
    OP_3E(0x241, 1)
    OP_3E(0x242, 1)
    OP_3E(0x243, 1)
    OP_3E(0x244, 1)
    OP_3E(0x245, 1)
    OP_3E(0x246, 1)
    OP_3E(0x247, 1)
    Jump("loc_4C01")

    label("loc_4BB8")

    OP_3F(0x23A, 1)
    OP_3F(0x23B, 1)
    OP_3F(0x23C, 1)
    OP_3F(0x23D, 1)
    OP_3F(0x23E, 1)
    OP_3F(0x23F, 1)
    OP_3F(0x240, 1)
    OP_3F(0x241, 1)
    OP_3F(0x242, 1)
    OP_3F(0x243, 1)
    OP_3F(0x244, 1)
    OP_3F(0x245, 1)
    OP_3F(0x246, 1)
    OP_3F(0x247, 1)
    Jump("loc_4C01")

    label("loc_4C01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x23A, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x23B, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23C, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23D, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23E, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23F, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x240, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x241, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x242, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x243, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x244, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x245, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x246, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x247, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C76")
    OP_A2(0x10C3)
    Call(1, 38)
    TalkEnd(0x2A)
    Return()

    label("loc_4C76")

    Call(1, 39)
    TalkEnd(0x2A)
    Return()

    label("loc_4C7E")


    ChrTalk(    #285
        0xFE,
        (
            "出来采购的时候，\x01",
            "突然说要我避难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "这种时候不要慌乱，\x01",
            "读读书镇定下来吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_4AF2 end

    def Function_37_4CD6(): pass

    label("Function_37_4CD6")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CFB")
    Call(0, 38)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4CF7")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4CFB")

    label("loc_4CF7")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4CFB")

    OP_6D(-5500, 0, 20, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -2600, 0, 560, 270)
    SetChrPos(0xC, -1280, 0, 980, 270)
    SetChrPos(0xA, -2600, 0, 1590, 270)
    SetChrPos(0x9, -2600, 0, -590, 270)
    SetChrPos(0xE, -1680, 0, 2260, 270)
    SetChrPos(0xB, -360, 0, 1500, 270)
    SetChrPos(0xD, -1240, 0, -60, 270)
    SetChrPos(0x10, -1480, 0, -1090, 270)
    SetChrPos(0x8, -5700, 0, -130, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x109, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0x8, 255)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #287
        0x8,
        (
            "#764F#6P是吗……\x02\x03",

            "#760F嗯嗯……知道了。\x02\x03",

            "那么拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(300)
    OP_8C(0x8, 45, 400)

    def lambda_4EC4():
        OP_6D(-3320, 0, 1160, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4EC4)
    OP_8E(0x8, 0xFFFFEE80, 0x0, 0x3C0, 0x5DC, 0x0)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #288
        0x101,
        "#1026F怎么了，艾南先生？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x8,
        (
            "#760F嗯嗯，凯诺娜原上尉\x01",
            "好像接受审问了。\x02\x03",

            "知道了详细情况，\x01",
            "也会告诉协会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x101,
        "#1025F是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4FC4")

    ChrTalk(    #291
        0x9,
        (
            "#027F#6P那个强硬的女人\x01",
            "居然打算招了啊。\x02\x03",

            "用了怎样的手段呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5006")

    label("loc_4FC4")


    ChrTalk(    #292
        0xA,
        (
            "#051F咦，那个强硬的\x01",
            "母狐狸居然会开口……\x02\x03",

            "使了怎样的手段啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5006")


    ChrTalk(    #293
        0xE,
        (
            "#074F#2P嗯，那边的调查\x01",
            "就交给王国军吧。\x02\x03",

            "#072F我们就做好自己的事情，\x01",
            "继续整理情报吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x8,
        (
            "#764F嗯……\x02\x03",

            "#760F那么，先交给你们\x01",
            "这次工作的报酬吧。\x02\x03",

            "其他的小委托也就都\x01",
            "一并核定了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8D, 0x4, 0x20)
    OP_28(0x89, 0x4, 0x10)
    OP_AF(0xCD, 0x89)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50DF")
    OP_2B(0x8C, 0x1)

    label("loc_50DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50EC")
    OP_2B(0x8C, 0x1)

    label("loc_50EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F9")
    OP_2B(0x8C, 0x1)

    label("loc_50F9")

    OP_28(0x8C, 0x4, 0x10)
    OP_AF(0xCD, 0x8C)
    Sleep(100)
    OP_28(0x8E, 0x4, 0x10)
    OP_AF(0xCD, 0x8E)
    Sleep(100)
    OP_28(0x8A, 0x4, 0x10)
    OP_28(0x8A, 0x4, 0x20)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #295
        0xC,
        (
            "#043F那个，艾丝蒂尔。\x02\x03",

            "玲真的是『结社』的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x101,
        "#1003F#5P嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    def lambda_5182():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5182)

    def lambda_5190():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5190)

    def lambda_519E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_519E)

    def lambda_51AC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_51AC)

    def lambda_51BA():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_51BA)

    def lambda_51C8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_51C8)
    Sleep(500)

    ChrTalk(    #297
        0x101,
        (
            "#1025F#5P『执行者』之一\x01",
            "名为『歼灭天使』……\x02\x03",

            "本人这么说就没错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xC,
        "#049F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xD,
        "#063F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x10,
        (
            "#1317F#6P但，但是那样的女孩\x01",
            "竟然是『结社』的精锐……\x02\x03",

            "而且『执行者』\x01",
            "不是很厉害的人吗？\x02\x03",

            "会不会是弄错了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        (
            "#1003F#5P不，我想大概是真的。\x02\x03",

            "约修亚也是在和她同龄的时候\x01",
            "就已经成为『执行者』了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x10,
        "#813F#6P………啊……………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_53F5")

    ChrTalk(    #303
        0x9,
        (
            "#522F#6P不过真是\x01",
            "彻底被耍了啊。\x02\x03",

            "将『福音』交给凯诺娜,\x01",
            "挑唆使用战车卷土重来的\x01",
            "好像也是那个孩子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xA,
        (
            "#555F向各方发出恐吓信的\x01",
            "似乎也是那个小鬼啊……\x02\x03",

            "到底是为什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54A5")

    label("loc_53F5")


    ChrTalk(    #305
        0xA,
        (
            "#552F不过真是\x01",
            "彻底被耍了啊。\x02\x03",

            "把『福音』交给那母狐狸,\x01",
            "挑唆使用战车卷土重来的\x01",
            "好像也是那小鬼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x9,
        (
            "#022F#6P向各方发出恐吓信的\x01",
            "似乎也是那个孩子呢……\x02\x03",

            "到底是什么打算呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54A5")


    ChrTalk(    #307
        0x101,
        (
            "#1015F#5P虽然是我的直觉……\x02\x03",

            "但会不会是这样做\x01",
            "比较有趣呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_55C6")

    ChrTalk(    #308
        0xA,
        "#052F什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x101,
        (
            "#1003F#5P玲认为这次的实验\x01",
            "是『茶会』。\x02\x03",

            "于是，为了让包括我们在内\x01",
            "众多的人都来参加\x01",
            "而做了很多准备邀请……\x02\x03",

            "我感觉是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xA,
        (
            "#055F……真的吗。\x02\x03",

            "因为恐吓信的事来到王都\x01",
            "这的确没错，不过……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_569D")

    label("loc_55C6")


    ChrTalk(    #311
        0x9,
        "#023F#6P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        (
            "#1003F#5P玲认为这次的实验\x01",
            "是『茶会』。\x02\x03",

            "于是，为了让包括我们在内\x01",
            "众多的人都来参加\x01",
            "而做了很多准备邀请……\x02\x03",

            "我感觉是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x9,
        (
            "#522F#6P……受不了了。\x02\x03",

            "我们的确是因为恐吓信的事\x01",
            "来到王都……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_569D")


    ChrTalk(    #314
        0xB,
        (
            "#035F唔，那只小猫咪\x01",
            "确实可能这么做。\x02\x03",

            "#030F看来让我们睡着的\x01",
            "安眠药的量也有控制。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_573C")

    ChrTalk(    #315
        0xA,
        (
            "#057F让我们刚好\x01",
            "能在那个时机\x01",
            "到达码头啊……\x02\x03",

            "真是胡闹……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_577C")

    label("loc_573C")


    ChrTalk(    #316
        0x9,
        (
            "#022F#6P让我们刚好\x01",
            "能在那个时机\x01",
            "可以到达吗……\x02\x03",

            "真行啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_577C")


    ChrTalk(    #317
        0x101,
        (
            "#1015F#5P唔，就是说都是\x01",
            "那孩子让大家睡着的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xC,
        (
            "#043F嗯嗯……恐怕是。\x02\x03",

            "吃了玲在百货店买的\x01",
            "曲奇之后马上就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xE,
        (
            "#074F#2P但是……\x01",
            "真是严重的失策啊。\x02\x03",

            "要是她用的是毒，\x01",
            "搞不好大家就都会死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x101,
        "#1026F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x8,
        (
            "#765F这是我的失策。\x02\x03",

            "作为大家的后援\x01",
            "应该更加当心才是。\x02\x03",

            "真是对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x101,
        (
            "#1025F#5P哪、哪里的话嘛，艾南先生。\x02\x03",

            "#1007F我想这次\x01",
            "是我们全体人员的责任。\x02\x03",

            "没想到『结社』竟是\x01",
            "那样的亡命之徒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xD,
        (
            "#561F#6P那个巨大人形兵器……\x02\x03",

            "那种东西，恐怕连\x01",
            "爷爷也很难制造出来……\x02\x03",

            "#062F即使能造出来……\x01",
            "竟能那样移动……\x02\x03",

            "而且……那个玲……\x02\x03",

            "#562F………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x101,
        "#1026F#5P提妲……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #325
        0x101,
        (
            "#1018F#5P真是的，打起精神来啦！#2S\x02\x03",

            "下次碰到她，绝对\x01",
            "要让她脱离『结社』！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #326
        0xD,
        "#064F#6P呜哎…？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5A6F")

    ChrTalk(    #327
        0xA,
        "#055F慢、慢着！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A8D")

    label("loc_5A6F")


    ChrTalk(    #328
        0x9,
        "#023F#6P艾丝蒂尔……！？\x02",
    )

    CloseMessageWindow()

    label("loc_5A8D")


    ChrTalk(    #329
        0x101,
        (
            "#1006F#5P５年前，老爸就让约修亚\x01",
            "脱离『结社』了……\x02\x03",

            "所以，身为他女儿的我\x01",
            "不可能做不到同样的事！\x02\x03",

            "哪怕揪着她的头发\x01",
            "也要把她拖出来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xD,
        (
            "#560F#6P姐、姐姐……\x02\x03",

            "#067F嗯，是啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xC,
        (
            "#048F呵呵……\x01",
            "到底是艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x10,
        "#811F#6P嗯嗯，就是这股劲！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xB,
        (
            "#031F呼，这股冲劲\x01",
            "真令人高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xA,
        (
            "#556F真是的……\x01",
            "别说得那么轻松。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x9,
        (
            "#021F#6P呵呵，有什么不好。\x01",
            "这才是艾丝蒂尔嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xE,
        (
            "#070F#2P这股冲劲\x01",
            "说不定更胜过老师呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x109, -20, -500, -7250, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #337
        0x109,
        "青年的声音",
        (
            "#2P嗯～真棒啊。\x01",
            "我好像越来越被她吸引了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5CA2():
        OP_6D(-1820, 0, -1810, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_5CA2)

    def lambda_5CBA():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CBA)

    def lambda_5CC8():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5CC8)

    def lambda_5CD6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5CD6)

    def lambda_5CE4():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5CE4)

    def lambda_5CF2():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5CF2)

    def lambda_5D00():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5D00)

    def lambda_5D0E():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5D0E)

    def lambda_5D1C():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5D1C)

    def lambda_5D2A():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5D2A)

    def lambda_5D38():

        label("loc_5D38")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_5D38")

    QueueWorkItem2(0x101, 1, lambda_5D38)

    def lambda_5D49():

        label("loc_5D49")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_5D49")

    QueueWorkItem2(0xA, 1, lambda_5D49)

    def lambda_5D5A():

        label("loc_5D5A")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_5D5A")

    QueueWorkItem2(0x9, 1, lambda_5D5A)

    def lambda_5D6B():

        label("loc_5D6B")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_5D6B")

    QueueWorkItem2(0xC, 1, lambda_5D6B)

    def lambda_5D7C():

        label("loc_5D7C")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_5D7C")

    QueueWorkItem2(0xD, 1, lambda_5D7C)

    def lambda_5D8D():

        label("loc_5D8D")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_5D8D")

    QueueWorkItem2(0xE, 1, lambda_5D8D)

    def lambda_5D9E():

        label("loc_5D9E")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_5D9E")

    QueueWorkItem2(0x8, 1, lambda_5D9E)

    def lambda_5DAF():

        label("loc_5DAF")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_5DAF")

    QueueWorkItem2(0x10, 1, lambda_5DAF)
    ClearChrFlags(0x109, 0x80)
    Sleep(1000)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5DD5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5DD5)

    def lambda_5DE7():
        OP_8E(0xFE, 0xFFFFFFEC, 0xFFFFFF06, 0xFFFFE958, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5DE7)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #338
        0x101,
        "#1004F#4P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x8,
        (
            "#761F#6P凯文神父。\x01",
            "正等着你呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5E43():
        OP_6D(-2800, 0, 240, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5E43)

    def lambda_5E5B():
        OP_8E(0xFE, 0xFFFFF8B2, 0x0, 0xFFFFF74A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E5B)
    WaitChrThread(0x109, 0x1)
    TurnDirection(0x109, 0x101, 400)
    Sleep(500)

    ChrTalk(    #340
        0x109,
        (
            "#1068F#6P呀～抱歉迟到了。\x02\x03",

            "之前被卡兰大主教\x01",
            "严厉说教了啊。\x02\x03",

            "所以才迟到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_62(0x109, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #341
        0x109,
        (
            "#1064F#6P怎么了？\x01",
            "我脸上有什么东西吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(    #342
        0x101,
        (
            "#1019F我说～事到如今\x01",
            "才问这个问题……\x02\x03",

            "凯文先生到底是什么人？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5FBF")

    ChrTalk(    #343
        0x9,
        (
            "#026F#5P嗯嗯，说得对。\x02\x03",

            "#027F到头来，我们\x01",
            "也总是被转移话题啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FFB")

    label("loc_5FBF")


    ChrTalk(    #344
        0xA,
        (
            "#051F咦，说得对啊。\x02\x03",

            "到头来，我们\x01",
            "也总是被转移话题啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FFB")


    ChrTalk(    #345
        0x10,
        (
            "#816F#5P当然不是普通的\x01",
            "神父吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x109,
        (
            "#1065F#6P是吗……\x01",
            "那我重新自我介绍一下吧。\x02\x03",

            "#1060F──我是七耀教会星杯骑士团\x01",
            "所属的凯文·格拉汉姆神父。\x02\x03",

            "以后，请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        "#1002F星杯骑士团……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xB,
        (
            "#033F#2P哟，这可诚惶诚恐了。\x02\x03",

            "#030F没想到你这么年轻\x01",
            "居然是『星杯骑士』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x101,
        "#1004F#5P奥利维尔，你知道吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xB,
        (
            "#035F#2P古代遗物被\x01",
            "教会管理的事，\x01",
            "你应该听说过吧……\x02\x03",

            "担任其调查·回收任务的\x01",
            "就是被称为星杯骑士团的组织。\x02\x03",

            "#030F成员似乎都是非公开\x01",
            "挑选的相当精干之人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x109,
        (
            "#1064F#6P咦，很清楚嘛。\x02\x03",

            "#1066F很遗憾，我在骑士团\x01",
            "还是一介新人呢。\x02\x03",

            "说精干实在是过奖了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x101,
        (
            "#1015F古代遗物的回收……\x02\x03",

            "#1004F那么，那时用的\x01",
            "戴尔蒙市长之杖……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x109,
        (
            "#1060F#6P啊啊，那个是王国军\x01",
            "正式交给我的东西。\x02\x03",

            "教会和利贝尔之间\x01",
            "缔结了古代遗物\x01",
            "回收的盟约的。\x02\x03",

            "#1068F由于我私自破坏\x01",
            "而被大主教说教……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x101,
        (
            "#1025F是、是这样啊……\x02\x03",

            "但是那个情况下，除了那样做\x01",
            "我想也没有别的办法了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_638B")

    ChrTalk(    #355
        0x9,
        (
            "#020F#5P嗯嗯，那可不是\x01",
            "该选择手段的时机啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63B7")

    label("loc_638B")


    ChrTalk(    #356
        0xA,
        (
            "#051F啊啊，也不是\x01",
            "该选择手段的时机啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63B7")


    ChrTalk(    #357
        0x109,
        (
            "#1066F#6P嘿嘿。\x01",
            "这样说我真是轻松多了。\x02\x03",

            "#1060F嗯，就是这样。\x01",
            "今后也请多关照了。\x02\x03",

            "关于『噬身之蛇』，\x01",
            "要是知道了什么就交换情报吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        "#1004F啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x109,
        (
            "#1065F#6P我来利贝尔\x01",
            "是为了调查『结社』嘛。\x02\x03",

            "#1063F正确的说……\x01",
            "是调查他们想得到的\x01",
            "『辉之环』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x101,
        "#1020F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x9,
        "#023F#5P『辉之环』……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xC,
        (
            "#047F#2P女神授予古代人的\x01",
            "『七至宝』之一……\x02\x03",

            "#042F被认为封印在\x01",
            "格兰赛尔城地下的\x01",
            "传说之古代遗物对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x109,
        (
            "#1063F#6P嗯嗯，是啊。\x02\x03",

            "#1065F最近，在大陆各地\x01",
            "似乎出现了收集有关\x01",
            "『七至宝』相关情报的人……\x02\x03",

            "即使是教会，对其动向\x01",
            "也相当在意。\x02\x03",

            "#1060F利贝尔也在此时\x01",
            "发来了『辉之环』的情报。\x02\x03",

            "因此，为了确认真伪，\x01",
            "就派遣了我这个新人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xC,
        "#542F#2P是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x101,
        (
            "#1002F那么『辉之环』\x01",
            "真的在利贝尔吗？\x02\x03",

            "因为不在封印区域里\x01",
            "我以为仅仅是传说而已……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_66D9")

    ChrTalk(    #366
        0xA,
        (
            "#555F说到底，并不知道\x01",
            "是怎样的东西对吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_670C")

    label("loc_66D9")


    ChrTalk(    #367
        0x9,
        (
            "#022F#5P说到底，并不知道\x01",
            "是怎样的东西不是吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_670C")


    ChrTalk(    #368
        0x109,
        (
            "#1065F#6P嗯，关于此事真伪的\x01",
            "调查也是我的工作。\x02\x03",

            "#1060F今天来，是想说明\x01",
            "我的情况……\x02\x03",

            "就是说，有什么事\x01",
            "再互相帮助吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x101,
        (
            "#1015F原来如此……\x02\x03",

            "#1006F嗯，我们也这么想呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xE,
        (
            "#070F是啊。\x01",
            "也帮了我们大忙啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6815")

    ChrTalk(    #371
        0x9,
        (
            "#027F#5P这也是种缘分，\x01",
            "有困难再联络了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_683B")

    label("loc_6815")


    ChrTalk(    #372
        0xA,
        (
            "#051F没办法……\x01",
            "有困难再联络啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_683B")


    ChrTalk(    #373
        0x109,
        (
            "#1062F#6P非常感谢！\x02\x03",

            "#1061F那么，今天\x01",
            "我就告辞了。\x02\x03",

            "回见～各位！\x02",
        )
    )

    CloseMessageWindow()
    OP_B7(0x8)
    OP_8C(0x109, 135, 400)

    def lambda_6890():
        OP_6D(-1820, 0, -1810, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6890)
    OP_8E(0x109, 0xFFFFFF92, 0xFFFFFF06, 0xFFFFE7AA, 0x7D0, 0x0)

    def lambda_68BC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_68BC)

    def lambda_68CE():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFE0C, 0xFFFFE3AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_68CE)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    SetChrFlags(0x109, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x8, 0x1)

    def lambda_6922():
        OP_6D(-3320, 0, 1160, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6922)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #374
        0x101,
        "#1007F#5P走了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x9,
        (
            "#027F#5P真是个和奥利维尔不同风格\x01",
            "却同样让人脱力的神父啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xB,
        (
            "#035F#2P呼，要我说来\x01",
            "修行还差的远呢。\x02\x03",

            "再稍微优雅一点就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x101,
        (
            "#1019F#5P你那些无聊话\x01",
            "哪里优雅了啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xC,
        (
            "#049F#2P不过『辉之环』啊……\x02\x03",

            "#043F和结社在各地\x01",
            "用『福音』做实验\x01",
            "有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    Sleep(400)

    ChrTalk(    #379
        0x8,
        (
            "#764F嗯……\x01",
            "不能否定这个可能性。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6A89():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6A89)

    def lambda_6A97():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6A97)
    Sleep(50)

    def lambda_6AAA():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6AAA)

    def lambda_6AB8():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6AB8)
    Sleep(50)

    def lambda_6ACB():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6ACB)

    def lambda_6AD9():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6AD9)
    Sleep(50)

    def lambda_6AEC():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AEC)

    def lambda_6AFA():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6AFA)
    Sleep(500)

    ChrTalk(    #380
        0x8,
        (
            "#762F顺带一提，这次事件中\x01",
            "他们在３个地方\x01",
            "进行了『福音』的实验。\x02\x03",

            "照这样看来，其他地方\x01",
            "可能也进行了实验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x101,
        (
            "#1002F是这样啊……\x02\x03",

            "王都的骚动也解决了，\x01",
            "是不是该转移了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6BF6")

    ChrTalk(    #382
        0xA,
        (
            "#053F这么说，就是洛连特地区\x01",
            "或者柏斯地区了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C2F")

    label("loc_6BF6")


    ChrTalk(    #383
        0x9,
        (
            "#020F#6P这么说，就是洛连特地区\x01",
            "或者柏斯地区了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C2F")

    Sleep(100)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x1, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 270, 400)

    def lambda_6CB0():
        OP_6D(-5500, 0, 20, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6CB0)
    OP_8F(0x8, 0xFFFFE9BC, 0x0, 0xFFFFFF7E, 0x7D0, 0x0)
    Sleep(400)
    WaitChrThread(0x8, 0x2)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    ChrTalk(    #384
        0x8,
        (
            "#760F#6P是，这里是游击士协会，\x01",
            "格兰赛尔支部。\x02\x03",

            "………………………………\x02\x03",

            "#763F什么……是吗。\x02\x03",

            "#764F……明白了。\x01",
            "我们也会注意。\x02\x03",

            "嗯嗯，那么再见。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(500)

    ChrTalk(    #385
        0x9,
        "#020F#6P艾南先生，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xA,
        (
            "#051F#2P那母狐狸的\x01",
            "审讯结束了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)

    def lambda_6E35():
        OP_6D(-3320, 0, 1160, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6E35)
    OP_8E(0x8, 0xFFFFEE80, 0x0, 0x3C0, 0x7D0, 0x0)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #387
        0x8,
        (
            "#762F不，是其他的事。\x02\x03",

            "看来昨夜，柏斯地方\x01",
            "出现了空贼团的余党。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #388
        0x101,
        "#1005F#3S咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xE,
        (
            "#072F情报部加上空贼团……\x01",
            "真是忙得一塌糊涂的夜晚。\x02\x03",

            "那，到底是在哪里出现的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x8,
        (
            "#762F似乎是以前他们作为大本营的\x01",
            "『迷雾峡谷』里的要塞。\x02\x03",

            "现在，本是作为军队的\x01",
            "飞行训练场来用的……\x02\x03",

            "他们抢了保管在那里的\x01",
            "空贼艇逃走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x9,
        "#023F#6P你说什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xB,
        (
            "#033F哦哦，穆拉\x01",
            "收领的那个吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x101,
        (
            "#1020F等、等一下。\x02\x03",

            "不觉得这\x01",
            "时机好得太过头了？\x02\x03",

            "搞不好这个\x01",
            "也和『结社』有关系？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x8,
        (
            "#764F不否定这个可能性。\x02\x03",

            "#762F由于这个，接下来\x01",
            "请各位去柏斯地区\x01",
            "可能比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x101,
        "#1002F确实……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7645")
    TurnDirection(0x9, 0x101, 400)
    Sleep(500)

    ChrTalk(    #396
        0x9,
        (
            "#020F#6P不是挺好吗。\x02\x03",

            "现在本来就不清楚\x01",
            "洛连特和柏斯\x01",
            "到底哪边会发生事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x101,
        "#1015F嗯……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #398
        0x101,
        (
            "#1004F#5P那，雪拉姐\x01",
            "也要一起来？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7231():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7231)

    def lambda_723F():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_723F)
    Sleep(10)

    def lambda_7252():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7252)

    def lambda_7260():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7260)
    Sleep(30)

    def lambda_7273():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7273)

    def lambda_7281():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7281)

    ChrTalk(    #399
        0x9,
        (
            "#027F#6P情报部的余党收拾后，\x01",
            "我们的工作也告一段落了。\x02\x03",

            "敌人似乎相当不好对付，\x01",
            "我也打算出一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x101,
        "#1018F#5P太好啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0xA,
        (
            "#051F呵，『银闪』的手腕，\x01",
            "可要好好见识一下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0xB,
        (
            "#037F呵呵呵，雪拉\x01",
            "也终于来到我身边了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0xC,
        (
            "#048F雪拉扎德小姐。\x01",
            "就请多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x9,
        "#021F#6P嗯嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #405
        0x101,
        (
            "#1004F#5P啊，难道……\x01",
            "亚妮拉丝也一起吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #406
        0x10,
        (
            "#819F#6P嘿嘿……\x01",
            "我就不好意思了。\x02\x03",

            "#816F克鲁茨他们也快\x01",
            "结束强化训练回来了。\x02\x03",

            "我打算加入\x01",
            "那边的队伍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x101,
        "#1025F#5P这样啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 400)

    ChrTalk(    #408
        0xE,
        (
            "#070F#2P说是队伍的话\x01",
            "果然还是对付『结社』吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xE, 400)

    ChrTalk(    #409
        0x10,
        (
            "#816F#6P是的，打算去搜索\x01",
            "『结社』的据点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x101,
        "#1004F#5P据点的搜索？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x8,
        (
            "#764F根据目前的行动来看，\x01",
            "『结社』在国内构筑了\x01",
            "什么据点的可能性似乎很高。\x02\x03",

            "#762F不破坏那里，\x01",
            "就无法从根本上解决问题。\x02\x03",

            "今后，有必要与王国军\x01",
            "全面合作进行搜索活动吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0xD,
        (
            "#062F的确，那个巨大人形兵器\x01",
            "绝对需要维护……\x02\x03",

            "在什么地方一定有\x01",
            "规范的设施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xA,
        (
            "#051F哦，对付结社的队伍\x01",
            "再多一个当然也是必要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B09")

    label("loc_7645")

    TurnDirection(0xA, 0x101, 400)
    Sleep(500)

    ChrTalk(    #414
        0xA,
        (
            "#051F不是很好吗。\x02\x03",

            "现在这时候\x01",
            "洛连特和柏斯，\x01",
            "也不清楚是否会有事件发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0x101,
        "#1015F嗯……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #416
        0x101,
        (
            "#1004F那，阿加特\x01",
            "也要一起来？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_76FC():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_76FC)
    Sleep(10)

    def lambda_770F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_770F)

    def lambda_771D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_771D)
    Sleep(30)

    def lambda_7730():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7730)

    def lambda_773E():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_773E)

    ChrTalk(    #417
        0xA,
        (
            "#051F情报部的余党收拾之后，\x01",
            "我们的工作也告一段落了。\x02\x03",

            "敌人似乎相当不好对付，\x01",
            "我也打算出一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x101,
        "#1018F真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0xD,
        (
            "#061F#6P哇，阿加特哥哥\x01",
            "也一起来啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x9,
        (
            "#027F#6P『重剑』的威力，\x01",
            "可要做个示范哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0xE,
        "#070F嗯，就承蒙关照了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xD, 400)

    ChrTalk(    #422
        0xA,
        "#051F#5P啊啊，彼此彼此。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #423
        0x101,
        (
            "#1004F#5P啊，难道……\x01",
            "亚妮拉丝也一起吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #424
        0x10,
        (
            "#819F#6P嘿嘿……\x01",
            "我就不好意思了。\x02\x03",

            "#816F克鲁茨他们也快\x01",
            "结束强化训练回来了。\x02\x03",

            "我打算加入\x01",
            "那边的队伍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        "#1025F#5P这样啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 400)

    ChrTalk(    #426
        0xE,
        (
            "#070F#2P说是队伍的话\x01",
            "果然还是对付『结社』吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xE, 400)

    ChrTalk(    #427
        0x10,
        (
            "#816F#6P是的，打算去搜索\x01",
            "『结社』的据点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x101,
        "#1004F#5P据点的搜索？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x8,
        (
            "#764F根据目前的行动来看，\x01",
            "『结社』在国内构筑了\x01",
            "什么据点的可能性似乎很高。\x02\x03",

            "#762F不破坏那里，\x01",
            "就无法从根本上解决问题。\x02\x03",

            "今后，有必要与王国军\x01",
            "全面合作进行搜索活动吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0xC,
        (
            "#040F看来这次事件中，\x01",
            "王国军对『结社』的应对\x01",
            "似乎也大幅度强化了。\x02\x03",

            "或许需要\x01",
            "更紧密的合作体制呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x9,
        (
            "#027F#6P唔，对付结社的队伍\x01",
            "再多一个当然也是必要的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B09")


    ChrTalk(    #432
        0x101,
        (
            "#1015F#5P嗯～这么说\x01",
            "克鲁茨的队伍\x01",
            "似乎也需要战力了……\x02\x03",

            "#1016F亚妮拉丝\x01",
            "被抢走也没办法呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #433
        0x10,
        (
            "#819F#6P嘿嘿，抱歉哦。\x02\x03",

            "#816F『结社』的据点找到之后，\x01",
            "应该也会需要借助\x01",
            "艾丝蒂尔你们的力量。\x02\x03",

            "到时候一起作战吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x101,
        "#1017F#5P嗯……好啊！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x8, 0xFF)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/C5601   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_37_4CD6 end

    def Function_38_7C19(): pass

    label("Function_38_7C19")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 124010, 0, -3770, 90)
    SetChrPos(0x102, 124010, 0, -2950, 90)
    SetChrPos(0xF8, 122910, 0, -3770, 90)
    SetChrPos(0xF9, 122910, 0, -2950, 90)
    OP_8C(0xFE, 270, 0)
    OP_0D()

    ChrTalk(    #435
        0x101,
        "#1004F啊，咖啡店的老板？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0xFE,
        (
            "呀，本来出来采购，\x01",
            "突然叫我去避难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0xFE,
        (
            "这种时候正应该\x01",
            "读本书镇定一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x101,
        (
            "#1015F（嗯～不过你现在\x01",
            "　就已经足够镇定了嘛……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x2A,
        "哟……这本书是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x2A,
        (
            "应该是流行于街头巷尾的\x01",
            "传说中的《牌技师杰克》吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x101,
        "#1004F啊，你是说这本小说？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x2A,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x2A,
        (
            "以共和国为舞台，\x01",
            "背负了不幸命运的\x01",
            "牌技师们的故事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x2A,
        (
            "哎呀呀，我老早\x01",
            "就想读这本书了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x101,
        (
            "#1011F是，是这样啊……\x02\x03",

            "#1015F（唔～我也受了不少\x01",
            "　老板的关照……)\x02",
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
            "【给店主小说】\x01",      # 0
            "【不给】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E99")
    Call(1, 40)
    Jump("loc_7EB5")

    label("loc_7E99")


    ChrTalk(    #446
        0x101,
        "#1016F（还是算了吧。）\x02",
    )

    CloseMessageWindow()

    label("loc_7EB5")

    EventEnd(0x0)
    Return()

    # Function_38_7C19 end

    def Function_39_7EB8(): pass

    label("Function_39_7EB8")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 124010, 0, -3770, 90)
    SetChrPos(0x102, 124010, 0, -2950, 90)
    SetChrPos(0xF8, 122910, 0, -3770, 90)
    SetChrPos(0xF9, 122910, 0, -2950, 90)
    OP_8C(0xFE, 270, 0)
    OP_0D()

    ChrTalk(    #447
        0x2A,
        "咦，你这是？\x02",
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
            "【给店主小说】\x01",      # 0
            "【不给】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F7F")
    Call(1, 40)
    Jump("loc_7F9B")

    label("loc_7F7F")


    ChrTalk(    #448
        0x101,
        "#1015F（还是算了吧。）\x02",
    )

    CloseMessageWindow()

    label("loc_7F9B")

    EventEnd(0x0)
    Return()

    # Function_39_7EB8 end

    def Function_40_7F9E(): pass

    label("Function_40_7F9E")


    ChrTalk(    #449
        0x101,
        (
            "#1001F喏，给你。\x01",
            "就送给老板吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0x2A,
        (
            "啊，我不是为了要书\x01",
            "才跟你们说这些的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0x101,
        (
            "#1000F请别介意。\x02\x03",

            "这就当美味咖喱和咖啡\x01",
            "的回礼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x2A,
        (
            "你能这么说\x01",
            "我真高兴…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0x2A,
        (
            "这样的话，\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #454
        "\x07\x02牌技师杰克\x07\x00交给了店主。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3F(0x23A, 1)
    OP_3F(0x23B, 1)
    OP_3F(0x23C, 1)
    OP_3F(0x23D, 1)
    OP_3F(0x23E, 1)
    OP_3F(0x23F, 1)
    OP_3F(0x240, 1)
    OP_3F(0x241, 1)
    OP_3F(0x242, 1)
    OP_3F(0x243, 1)
    OP_3F(0x244, 1)
    OP_3F(0x245, 1)
    OP_3F(0x246, 1)
    OP_3F(0x247, 1)
    OP_0D()

    ChrTalk(    #455
        0x2A,
        (
            "谢谢，我马上读来\x01",
            "镇定一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x2A,
        (
            "对了……\x01",
            "这点东西，\x01",
            "不呈谢意。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #457
        "\x1F\x17\x04\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x417, 1)
    OP_0D()

    ChrTalk(    #458
        0x102,
        "#1044F这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0x2A,
        (
            "这是我还在当外交官的时候，\x01",
            "在亚尔特利亚得到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x101,
        (
            "#1015F亚尔特利亚应该是\x01",
            "七耀教会的总部吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x2A,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x2A,
        (
            "这好像是用很久以前的塞姆里亚时代\x01",
            "出产的金属制成的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0x102,
        (
            "#1044F塞姆里亚时代的？\x01",
            "确实从没见过这样的金属……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0x2A,
        (
            "哈哈，我也不知道\x01",
            "是真是假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0x2A,
        (
            "顺带一提，加工此物的技术,\x01",
            "据说已经完全失传了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0x101,
        (
            "#1004F咦，这样想\x01",
            "感觉像是很不得了的人了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 7)), scpexpr(EXPR_END)), "loc_83A4")

    ChrTalk(    #467
        0x102,
        (
            "#1040F记得以前老板也拿武器\x01",
            "来跟我换过书吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0x2A,
        "哈哈，你还记得阿。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0x2A,
        (
            "这次虽然不是什么好东西，\x01",
            "还请各位收下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x101,
        "#1001F嗯，我会好好珍惜它的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_83FB")

    label("loc_83A4")


    ChrTalk(    #471
        0x2A,
        (
            "哈哈，这次虽然不是什么好东西，\x01",
            "还请各位收下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x101,
        "#1001F嗯，我会好好珍惜它的。\x02",
    )

    CloseMessageWindow()

    label("loc_83FB")

    OP_A2(0x10C4)
    Return()

    # Function_40_7F9E end

    SaveToFile()

Try(main)
