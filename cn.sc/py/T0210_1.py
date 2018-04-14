from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0210_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0210   ._SN',
            'ED6_DT21/T0210_1 ._SN',
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
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0x101,
        (
            "#1011F啊，米蕾奴阿姨。\x02\x03",

            "我能问你一件事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "哎呀，什么事呢？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05诉说了在寻找拉欧老人\x01",
            "所说的炖煮料理食谱的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #3
        0xFE,
        "哦，是炖煮料理……呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#020F难不成您\x01",
            "知道那个食谱？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #5
        0xFE,
        (
            "真不凑巧。\x01",
            "我并不是那么精通料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "应该是吃过，\x01",
            "但是做法就完全不知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1007F呼～还是不行吗。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_25B")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #8
        0x103,
        (
            "#020F总之\x01",
            "先去报告那个食谱吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #9
        0x101,
        "#1015F嗯，只有先这样了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_490")

    label("loc_25B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_2BF")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #10
        0x103,
        (
            "#020F看来还是得\x01",
            "调查雷特拉先生家了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #11
        0x101,
        "#1015F嗯……或许是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_490")

    label("loc_2BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F4")

    ChrTalk(    #12
        0x107,
        (
            "#063F嗯～怎么也\x01",
            "找不到线索呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_384")

    label("loc_2F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_323")

    ChrTalk(    #13
        0x105,
        (
            "#043F好难找到\x01",
            "线索呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_384")

    label("loc_323")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_354")

    ChrTalk(    #14
        0x104,
        (
            "#032F唔，很难\x01",
            "找到线索呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_384")

    label("loc_354")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_384")

    ChrTalk(    #15
        0x108,
        (
            "#075F唔，调查\x01",
            "没什么进展啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_384")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #16
        0x103,
        (
            "#020F唉，着急也不是办法。\x02\x03",

            "还是得坚持下去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1006F嗯……\x01",
            "放弃就前功尽弃了。\x02\x03",

            "阿姨，也谢谢您帮忙。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #18
        0xFE,
        (
            "哪里，别客气了。\x01",
            "我也没帮上什么嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "你们一直工作真是很辛苦，\x01",
            "要好好努力哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1006F嗯，明白。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 400)

    ChrTalk(    #21
        0x103,
        "#020F那么，我们告辞了。\x02",
    )

    CloseMessageWindow()

    label("loc_490")

    OP_A2(0x6)
    OP_28(0x75, 0x1, 0x40)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
