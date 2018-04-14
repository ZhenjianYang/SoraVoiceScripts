from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0701_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0701_1 ._SN',
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
        "Function_1_2AE",          # 01, 1
        "Function_2_7EF",          # 02, 2
        "Function_3_14CB",         # 03, 3
        "Function_4_1F2D",         # 04, 4
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 42160, 4000, 32689, 135)
    SetChrPos(0x103, 41220, 4000, 31800, 90)
    SetChrPos(0xF8, 41110, 4000, 32970, 135)
    SetChrPos(0xF9, 42320, 4000, 33710, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0xF9, 41110, 4000, 32970, 135)
    SetChrPos(0xF8, 42320, 4000, 33710, 135)

    label("loc_124")

    TurnDirection(0xFE, 0x101, 0)
    OP_6D(42900, 4000, 32590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0xFE,
        (
            "真是厉害的雾啊。\x01",
            "连工作服也湿透了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1000F请问，打扰一下行吗？\x02\x03",

            "向你询问一些事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "哦，什么？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x05向他说明了正在寻找\x01",
            "褐色猫的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #4
        0xFE,
        "唔～猫啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "不巧我没看到。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1000F啊？是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "看见那只猫的\x01",
            "肯定是斯库拉特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "你们去找他问问吧。\x01",
            "他应该在仓库附近。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_2AE(): pass

    label("Function_1_2AE")

    EventBegin(0x0)
    OP_8C(0xFE, 135, 0)
    Fade(1000)
    SetChrPos(0x101, 36380, 0, 50200, 90)
    SetChrPos(0x103, 35330, 0, 49670, 90)
    SetChrPos(0xF8, 34610, 0, 50660, 90)
    SetChrPos(0xF9, 33650, 0, 49980, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F")
    SetChrPos(0xF9, 34610, 0, 50660, 90)
    SetChrPos(0xF8, 33650, 0, 49980, 90)

    label("loc_32F")

    OP_4A(0xFE, 255)
    OP_6D(37130, 0, 50200, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #9
        0xFE,
        "呼，好厉害的露水啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "这下可得想点\x01",
            "厉害的办法对付湿气啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1011F请问～打扰一下行吗？\x02\x03",

            "我们有事想问你。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #12
        0xFE,
        "嗯？　什么？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05向他说明了正在寻找\x01",
            "褐色猫的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #14
        0xFE,
        "啊啊，那只猫啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "确实见过呢。\x01",
            "今天中午的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C0")

    ChrTalk(    #16
        0x105,
        "#040F中午……是吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_53B")

    label("loc_4C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E8")

    ChrTalk(    #17
        0x107,
        "#060F中午啊……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_53B")

    label("loc_4E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_514")

    ChrTalk(    #18
        0x104,
        "#030F唔，中午……吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_53B")

    label("loc_514")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53B")

    ChrTalk(    #19
        0x108,
        "#070F唔，中午吗……\x02",
    )

    CloseMessageWindow()

    label("loc_53B")


    ChrTalk(    #20
        0x101,
        (
            "#1002F……和伊娜阿姨的话\x01",
            "恰好相符呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#020F那，之后那猫\x01",
            "去了哪里知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "之后啊……\x01",
            "到底去了哪里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "从那之后也再没看见，\x01",
            "完全没印象呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "怎么说猫这东西呢，\x01",
            "真是种反复无常的生物嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1016F嗯，这倒是没错……\x02\x03",

            "#1015F不过，真伤脑筋啊。\x01",
            "线索断了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "那就去问问\x01",
            "库因特那家伙怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "刚刚吃完晚饭，\x01",
            "好像出城了来着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        "#023F库因特先生？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "啊啊，赛希莉亚号的操舵手。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "那个家伙也说起过猫呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1006F操舵手库因特先生吗。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72F")

    ChrTalk(    #32
        0x106,
        "#050F赶快去找吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AB")

    label("loc_72F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_757")

    ChrTalk(    #33
        0x108,
        "#070F赶快去找吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AB")

    label("loc_757")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_786")

    ChrTalk(    #34
        0x104,
        (
            "#030F那么就赶快\x01",
            "去找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AB")

    label("loc_786")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AB")

    ChrTalk(    #35
        0x105,
        "#040F赶快去找吧。\x02",
    )

    CloseMessageWindow()

    label("loc_7AB")


    ChrTalk(    #36
        0x103,
        "#020F……谢谢您提供线索。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "哪里，一点小事。\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x10)
    OP_28(0x74, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_1_2AE end

    def Function_2_7EF(): pass

    label("Function_2_7EF")

    EventBegin(0x0)
    OP_8C(0xFE, 180, 0)
    Fade(1000)
    SetChrPos(0x101, 30460, 0, 3220, 270)
    SetChrPos(0xF7, 31440, 0, 3750, 270)
    SetChrPos(0xF8, 31360, 0, 2610, 270)
    SetChrPos(0xF9, 32270, 0, 3270, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_870")
    SetChrPos(0xF9, 31360, 0, 2610, 270)
    SetChrPos(0xF8, 32270, 0, 3270, 270)

    label("loc_870")

    OP_6D(29790, 0, 2710, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(213000, 0)
    OP_6E(262, 0)
    OP_4A(0xFE, 255)
    OP_0D()

    ChrTalk(    #38
        0xFE,
        "呼～真安静啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1003F#4P啊……果然是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #40
        0xFE,
        "哎呀～怎么了～～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1007F#4P正找你呢，索斯摩夫先生。\x02\x03",

            "你躲在这里\x01",
            "到底在干什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "这不是一看就知道了吗，\x01",
            "在享受森林浴哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "呀，船上待久了，\x01",
            "就开始怀念绿色了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "所以就经常像这样\x01",
            "被树木包围享受一阵自然浴呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1019F#4P好、好奇怪的习惯啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x103,
        (
            "#026F啊啊，不管怎样\x01",
            "找到就好。\x02\x03",

            "#020F好啦，赶快\x01",
            "把事情办完吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1002F#4P嗯，说的是呢。\x02\x03",

            "#1015F……其实有些事\x01",
            "想跟索斯摩夫先生打听一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "哦～～是什么事呢？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        (
            "\x07\x05向他说明了正在寻找\x01",
            "褐色猫的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #50
        0xFE,
        "咦～在找猫吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x103,
        (
            "#020F从库因特先生那里\x01",
            "听说您好像见过猫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "嗯嗯～确实看见过哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "今天中午，卸货时\x01",
            "看到在船舱里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "喵喵叫着\x01",
            "吵得厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1015F#4P船舱？也就是说……\x02\x03",

            "#1002F猫在飞船里了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "船舱……这么说，\x01",
            "一般是在飞船里面吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "再怎么联想\x01",
            "也只能是那里了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C4B")

    ChrTalk(    #58
        0x106,
        (
            "#051F#1P原来如此，飞船里啊……\x02\x03",

            "怪不得找不到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4B")

    label("loc_C4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA4")

    ChrTalk(    #59
        0x108,
        (
            "#070F#1P不过，定期船里面啊……\x02\x03",

            "#071F哈哈，在外面找\x01",
            "难怪找不到了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4B")

    label("loc_CA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF1")

    ChrTalk(    #60
        0x104,
        (
            "#030F#1P没想到在定期船里面啊……\x02\x03",

            "呼，怪不得找不到了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4B")

    label("loc_CF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D4B")

    ChrTalk(    #61
        0x105,
        (
            "#043F#1P话说回来，\x01",
            "真没想到会在定期船里面……\x02\x03",

            "#047F怪不得找不到了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D78")

    ChrTalk(    #62
        0x107,
        "#067F#1P嘿嘿，真是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_E02")

    label("loc_D78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA5")

    ChrTalk(    #63
        0x105,
        "#040F#1P呵呵，真是的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E02")

    label("loc_DA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD8")

    ChrTalk(    #64
        0x104,
        "#030F#1P呼，真没办法……呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E02")

    label("loc_DD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E02")

    ChrTalk(    #65
        0x108,
        "#070F#1P哈哈，真是的。\x02",
    )

    CloseMessageWindow()

    label("loc_E02")


    ChrTalk(    #66
        0x103,
        (
            "#020F不过……\x01",
            "现在还不能太高兴哟。\x02\x03",

            "赶快去请求许可，\x01",
            "到飞船里调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #67
        0x101,
        "#1006F#4P嗯，就这么定了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #68
        0x101,
        (
            "#1006F#4P那么，索斯摩夫先生。\x01",
            "真是谢谢您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "哈，这倒不必……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "嗯……那个……\x01",
            "怎么说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1011F#4P？？？\x02\x03",

            "怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        "#023F您刚才好像想说什么吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "嗯嗯，说出来\x01",
            "可能比较为难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "……大家在寻找的\x01",
            "是『褐色』的猫吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1011F#4P嗯，是这样的没错……\x01",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x101,
        "#1004F#4P……唔，难不成！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "啊，明白了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "嗯嗯，是你想的那样的。\x01",
            "其实我看见的猫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "不是褐色，\x01",
            "是『纯黑』的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106D")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_10AB")

    label("loc_106D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1094")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_10AB")

    label("loc_1094")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_10AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D2")
    OP_62(0xF6, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1110")

    label("loc_10D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F9")
    OP_62(0xF6, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1110")

    label("loc_10F9")

    OP_62(0xF6, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1110")

    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113C")
    OP_62(0xF7, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_117A")

    label("loc_113C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1163")
    OP_62(0xF7, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_117A")

    label("loc_1163")

    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_117A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A1")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_11DF")

    label("loc_11A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C8")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_11DF")

    label("loc_11C8")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_11DF")

    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121C")

    ChrTalk(    #80
        0x106,
        (
            "#551F#1P喂，大叔……\x01",
            "这你早说啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BB")

    label("loc_121C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1252")

    ChrTalk(    #81
        0x108,
        (
            "#075F#1P呼，这应该\x01",
            "早说才是啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BB")

    label("loc_1252")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_128A")

    ChrTalk(    #82
        0x104,
        (
            "#031F#1P哈哈哈。\x01",
            "真是被你打败了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BB")

    label("loc_128A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12BB")

    ChrTalk(    #83
        0x105,
        (
            "#045F#1P完、完全\x01",
            "吃了一惊了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BB")


    ChrTalk(    #84
        0xFE,
        (
            "对不起啊……\x01",
            "怎么都说不出口呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "不过，飞船里确实\x01",
            "是有猫肯定没错……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "要不还是去调查一下看看？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1007F#4P嗯，确实……\x02\x03",

            "也不确定安莉尔\x01",
            "一定不在那。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13AA")

    ChrTalk(    #88
        0x107,
        (
            "#560F#1P是，是啊。\x02\x03",

            "那只黑猫，搞不好\x01",
            "是安莉尔的朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AA")


    ChrTalk(    #89
        0x103,
        (
            "#025F嗯嗯，是啊……\x01",
            "反正也没有其他线索……\x02\x03",

            "#020F调整调整心情，\x01",
            "然后去调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1433")

    ChrTalk(    #90
        0x108,
        "#070F#1P是啊……去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14C2")

    label("loc_1433")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_146B")

    ChrTalk(    #91
        0x104,
        (
            "#030F#1P唔，是啊。\x01",
            "就当散个步啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C2")

    label("loc_146B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_149C")

    ChrTalk(    #92
        0x106,
        "#551F#1P啊啊，只能这样了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14C2")

    label("loc_149C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C2")

    ChrTalk(    #93
        0x107,
        "#560F#1P啊……好！\x02",
    )

    CloseMessageWindow()

    label("loc_14C2")

    OP_28(0x74, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_2_7EF end

    def Function_3_14CB(): pass

    label("Function_3_14CB")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 43090, 4000, 33470, 180)
    SetChrPos(0x103, 42250, 4000, 34000, 180)
    SetChrPos(0xF8, 42150, 4000, 35100, 180)
    SetChrPos(0xF9, 43120, 4000, 34660, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1545")
    SetChrPos(0xF9, 42150, 4000, 35100, 180)
    SetChrPos(0xF8, 43120, 4000, 34660, 180)

    label("loc_1545")

    TurnDirection(0xFE, 0x101, 0)
    OP_4A(0xFE, 255)
    OP_6D(43090, 4000, 33130, 0)
    OP_67(0, 8370, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_15DF")

    ChrTalk(    #94
        0xFE,
        "哟，猫找到了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1011F嗯，其实关于这个\x01",
            "想麻烦您帮个忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1661")

    label("loc_15DF")


    ChrTalk(    #96
        0xFE,
        "哟，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "这么晚还在工作，\x01",
            "你们也真辛苦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1016F嗯，彼此彼此啦。\x02\x03",

            "#1000F别提这个了，关于工作\x01",
            "想麻烦您帮个忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1661")


    ChrTalk(    #99
        0xFE,
        "咦，什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x103,
        (
            "#020F#3P嗯嗯，希望能让我们\x01",
            "到定期船里面调查一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "这就是说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "要进入这艘\x01",
            "赛希莉亚号，是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1015F嗯，是这么回事。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_178B")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #104
        (
            "\x07\x05说明之前的经过和调查状况，\x01",
            "传达了可能有猫在飞船内的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #105
        0xFE,
        (
            "原来如此啊……\x01",
            "事情倒是明白了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1863")

    label("loc_178B")


    ChrTalk(    #106
        0xFE,
        (
            "但是，这不是说说\x01",
            "就ＯＫ的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "把相关的根据\x01",
            "说给我听听吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1002F嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #109
        (
            "\x07\x05说明之前的经过和调查状况，\x01",
            "传达了可能有猫在飞船内的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #110
        0xFE,
        (
            "原来如此啊……\x01",
            "这么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1863")


    ChrTalk(    #111
        0xFE,
        (
            "但是，这不是我一个人\x01",
            "就能批准的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "……不好意思，请放弃吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1019F呜……\x02\x03",

            "好，好干脆的就\x01",
            "被拒绝了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "不是我干脆，\x01",
            "不可能就是不可能啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "再纠缠也是徒劳的，\x01",
            "还是赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 400)
    Sleep(400)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #116
        0x101,
        "#1003F唉……没办法了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        "#026F#3P哎呀──\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0x101, 0x20)

    def lambda_197E():
        OP_8C(0xFE, 180, 100)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_197E)
    OP_8E(0x103, 0xA6B8, 0xFA0, 0x7C38, 0x3E8, 0x0)
    OP_8C(0x103, 90, 400)
    WaitChrThread(0x101, 0x3)
    ClearChrFlags(0x101, 0x20)
    OP_62(0x103, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #118
        0x103,
        (
            "#520F#3P你真是的㈱\x01",
            "干吗说得那么死板嘛㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(    #119
        0xFE,
        "哇哇……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)

    ChrTalk(    #120
        0xFE,
        "那、那个……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A71")
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x104)

    ChrTalk(    #121
        0x104,
        "#037F（这、这是！）\x02",
    )

    CloseMessageWindow()

    label("loc_1A71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ABD")
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x106)

    ChrTalk(    #122
        0x106,
        "#552F（终于出手了啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_1ABD")


    ChrTalk(    #123
        0x103,
        (
            "#027F#3P听好了哦？\x01",
            "请仔～细考虑一下。\x02\x03",

            "万一猫在船里，\x01",
            "你们也会有麻烦吧？\x02\x03",

            "要是座椅被抓坏了\x01",
            "可怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "这、这个……确实。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "但、但是，也不能\x01",
            "因此就随便批准……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x103, 0xA708, 0xFA0, 0x7C38, 0x3E8, 0x0)

    ChrTalk(    #126
        0x103,
        (
            "#027F#3P没关系㈱\x01",
            "不会给你们添麻烦的。\x02\x03",

            "只要稍微\x01",
            "进去一下就行啦。\x02\x03",

            "#525F所以拜托……了呢㈱\x01",
            "……………（软玉温香）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_9E(0xFE, 0x32, 0x0, 0x1F4, 0x5DC)

    ChrTalk(    #127
        0xFE,
        "☆△×○☆～～！！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #128
        0x101,
        (
            "#1013F（雪拉姐，碰到了。\x01",
            "  碰到了啦……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CDA")
    OP_62(0x104, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #129
        0x104,
        (
            "#039F（啊啊啊啊───！\x01",
            "  好羡慕──！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D12")

    ChrTalk(    #130
        0x107,
        (
            "#562F（真、真是的～～\x01",
            "  雪拉姐……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D3F")

    ChrTalk(    #131
        0x105,
        "#540F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_1D3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D70")

    ChrTalk(    #132
        0x106,
        "#551F（真是的……真厉害啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_1D70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DB0")

    ChrTalk(    #133
        0x108,
        (
            "#071F（哈哈，事到如今\x01",
            "  美人计也是绝招啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB0")

    OP_8F(0x103, 0xA514, 0xFA0, 0x7C38, 0x3E8, 0x0)

    ChrTalk(    #134
        0x103,
        (
            "#526F#3P……如何？\x01",
            "明白了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #135
        0xFE,
        "真，真没办法啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "那么，真的\x01",
            "只是一小会儿哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "以、以后这事\x01",
            "绝对下不为例哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x103,
        "#021F#3P呵呵，明白啦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_71(0xA, 0x4)
    OP_8C(0xFE, 90, 0)
    ClearChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, 43100, 4000, 30900, 90)
    SetChrPos(0x103, 42250, 4000, 34000, 180)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #139
        0xFE,
        "──好，准备完成了。\x02",
    )

    CloseMessageWindow()
    OP_8E(0xFE, 0xA848, 0xFA0, 0x7D3C, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #140
        0xFE,
        "那么，麻烦尽快啦。\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x200)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_3_14CB end

    def Function_4_1F2D(): pass

    label("Function_4_1F2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F42")
    Return()

    label("loc_1F42")

    EventBegin(0x1)
    OP_4A(0x9, 255)
    TurnDirection(0x9, 0x0, 0)
    OP_6D(41340, 4000, 35650, 1000)

    ChrTalk(    #141
        0x9,
        (
            "喂喂！\x01",
            "去哪里啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x9,
        (
            "请赶快\x01",
            "去调查啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0x9, 255)
    OP_8C(0x9, 270, 0)
    Return()

    # Function_4_1F2D end

    SaveToFile()

Try(main)
