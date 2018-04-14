from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0120_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0120   ._SN',
            'ED6_DT21/T0120_1 ._SN',
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10E")

    ChrTalk(    #0
        0x101,
        (
            "#1011F啊，对了阿姨。\x02\x03",

            "其实是有点事…\x01",
            "想向你询问一些事情。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #1
        0xFE,
        "咦？想问的事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D")

    label("loc_10E")


    ChrTalk(    #2
        0x101,
        (
            "#1011F啊，斯蒂娜阿姨。\x01",
            "问您件事行吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #3
        0xFE,
        "哎呀，怎么了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1000F嗯，其实想向您打听\x01",
            "一些事情…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05诉说了在寻找拉欧老人\x01",
            "所说的炖煮料理食谱的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #6
        0x103,
        (
            "#020F──大概就是这样的，\x01",
            "这个料理有印象吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #7
        0xFE,
        (
            "嗯～小的时候\x01",
            "的确吃过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "很可惜，详细的食谱\x01",
            "我也没听说过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1020F咦～怎么会……\x01",
            "连阿姨也不知道吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #10
        0xFE,
        (
            "一般的食谱我是知道的，\x01",
            "但不知道那个料理哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "说不定是只在\x01",
            "洛连特流传的乡土料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1007F呼，是吗～……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_305")
    Jump("loc_334")

    label("loc_305")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_313")
    Jump("loc_334")

    label("loc_313")


    ChrTalk(    #13
        0x103,
        "#025F……比想象的更麻烦呢。\x02",
    )

    CloseMessageWindow()

    label("loc_334")


    ChrTalk(    #14
        0xFE,
        "抱歉，帮不上忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "但是，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "别老是顾着工作，\x01",
            "不好好休息可不行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#1016F啊哈哈……我会注意的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #18
        0xFE,
        (
            "雪拉也是，\x01",
            "要多注意点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#021F嗯嗯，我知道的。\x02\x03",

            "那么，失陪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_28(0x75, 0x1, 0x20)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
