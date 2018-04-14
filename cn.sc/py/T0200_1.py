from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0200_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0200_1 ._SN',
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

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 7870, 0, -15950, 0)
    SetChrPos(0xF7, 6710, 0, -16560, 0)
    SetChrPos(0xF8, 7910, 0, -17100, 0)
    SetChrPos(0xF9, 8940, 0, -16500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0xF9, 7910, 0, -17100, 0)
    SetChrPos(0xF8, 8940, 0, -16500, 0)

    label("loc_124")

    OP_6D(8740, 0, -14620, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#1002F#5P嗯，这些木箱的排列方式……\x02\x03",

            "和卡片上的记号\x01",
            "不是一模一样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        (
            "#020F#3P是啊，箱子的数量\x01",
            "也正好是五个。\x02\x03",

            "还是调查一下比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1006F#5P嗯，那么马上……\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x1EBE, 0x0, 0xFFFFC6F8, 0x7D0, 0x0)

    ChrTalk(    #3
        0x101,
        (
            "#1028F#5P那么～到底\x01",
            "是·在·哪·里·呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8F(0x101, 0x1ACC, 0x0, 0xFFFFC6F8, 0x7D0, 0x0)
    Sleep(1500)
    OP_8F(0x101, 0x2152, 0x0, 0xFFFFC6F8, 0x7D0, 0x0)
    Sleep(500)
    OP_8F(0x101, 0x1EBE, 0x0, 0xFFFFC6F8, 0x7D0, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #4
        0x101,
        "#1018F#5P有，有了！\x02",
    )

    CloseMessageWindow()

    def lambda_2F6():
        TurnDirection(0xF7, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2F6)

    def lambda_304():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_304)

    def lambda_312():
        TurnDirection(0xF9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_312)
    OP_8C(0x101, 180, 400)
    Fade(1000)
    SetChrChipByIndex(0x101, 6)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05　\x01",
            "　　第三把钥匙在市内。　　\x01",
            "  在『八眼铁兽』的腹部寻找。\x01",
            "　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #6
        0x101,
        (
            "#1015F#5P──是这么\x01",
            "写着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#022F#3P『八眼铁兽』啊……\x02\x03",

            "好像是在洛连特市内，\x01",
            "不过到底是什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_493")

    ChrTalk(    #8
        0x104,
        (
            "#034F呼，看来还是只有\x01",
            "四处走动走动继续调查了……\x02\x03",

            "不管怎样都得早点找到钥匙，\x01",
            "那样才能放松下来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D2")

    label("loc_493")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FD")

    ChrTalk(    #9
        0x108,
        (
            "#070F就和以前一样，只好\x01",
            "四处走动走动继续调查了。\x02\x03",

            "虽然是麻烦，\x01",
            "但这时候更要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D2")

    label("loc_4FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55D")

    ChrTalk(    #10
        0x106,
        (
            "#050F就和以前一样，只好\x01",
            "四处走动走动继续调查了。\x02\x03",

            "别磨磨蹭蹭了\x01",
            "赶快去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D2")

    label("loc_55D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D2")

    ChrTalk(    #11
        0x105,
        (
            "#040F看来还是只能和以前一样\x01",
            "四处走动走动继续调查了。\x02\x03",

            "一定就差最后一口气了，\x01",
            "就努力再坚持一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D2")

    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62B")

    ChrTalk(    #12
        0x101,
        (
            "#1016F#5P啊哈哈，我也是这么想的……\x02\x03",

            "#1006F那么就走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B9")

    label("loc_62B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_662")

    ChrTalk(    #13
        0x101,
        (
            "#1006F#5P嗯，明白。\x01",
            "那么就走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B9")

    label("loc_662")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68C")

    ChrTalk(    #14
        0x101,
        "#1006F#5P嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B9")

    label("loc_68C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B9")

    ChrTalk(    #15
        0x101,
        "#1006F#5P嗯，那么出发吧。\x02",
    )

    CloseMessageWindow()

    label("loc_6B9")

    OP_28(0x77, 0x1, 0x20)
    OP_64(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
