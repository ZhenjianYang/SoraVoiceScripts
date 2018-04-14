from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2412   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2412.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '特蕾莎院长',                           # 9
        '水壶',                                 # 10
        '红茶',                                 # 11
        '红茶',                                 # 12
        '红茶',                                 # 13
        '克拉姆',                               # 14
        '波利',                                 # 15
        '玛丽',                                 # 16
        '达尼艾尔',                             # 17
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


    AddCharChip(
        'ED6_DT07/CH02570 ._CH',             # 00
        'ED6_DT07/CH02573 ._CH',             # 01
        'ED6_DT27/CH03003 ._CH',             # 02
        'ED6_DT07/CH00023 ._CH',             # 03
        'ED6_DT07/CH00053 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT07/CH02590 ._CH',             # 06
        'ED6_DT07/CH02500 ._CH',             # 07
        'ED6_DT07/CH02630 ._CH',             # 08
        'ED6_DT07/CH02640 ._CH',             # 09
        'ED6_DT27/CH03083 ._CH',             # 0A
        'ED6_DT07/CH02593 ._CH',             # 0B
        'ED6_DT07/CH02503 ._CH',             # 0C
        'ED6_DT07/CH02633 ._CH',             # 0D
        'ED6_DT07/CH02643 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02570P._CP',             # 00
        'ED6_DT07/CH02573P._CP',             # 01
        'ED6_DT27/CH03003P._CP',             # 02
        'ED6_DT07/CH00023P._CP',             # 03
        'ED6_DT07/CH00053P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT07/CH02590P._CP',             # 06
        'ED6_DT07/CH02500P._CP',             # 07
        'ED6_DT07/CH02630P._CP',             # 08
        'ED6_DT07/CH02640P._CP',             # 09
        'ED6_DT27/CH03083P._CP',             # 0A
        'ED6_DT07/CH02593P._CP',             # 0B
        'ED6_DT07/CH02503P._CP',             # 0C
        'ED6_DT07/CH02633P._CP',             # 0D
        'ED6_DT07/CH02643P._CP',             # 0E
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_295",          # 01, 1
        "Function_2_2A8",          # 02, 2
        "Function_3_2BE",          # 03, 3
        "Function_4_2E2",          # 04, 4
        "Function_5_AFB",          # 05, 5
        "Function_6_E17",          # 06, 6
        "Function_7_14F5",         # 07, 7
        "Function_8_225C",         # 08, 8
    )


    def Function_0_242(): pass

    label("Function_0_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_269")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 4200, 0)
    OP_43(0x10, 0x0, 0x0, 0x3)
    Jump("loc_275")

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_275")
    SetChrFlags(0x8, 0x80)

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_283")
    OP_A3(0x10F0)
    Event(0, 7)

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_294")

    Return()

    # Function_0_242 end

    def Function_1_295(): pass

    label("Function_1_295")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7")
    OP_A3(0x0)
    OP_A3(0x1)

    label("loc_2A7")

    Return()

    # Function_1_295 end

    def Function_2_2A8(): pass

    label("Function_2_2A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2A8")

    label("loc_2BD")

    Return()

    # Function_2_2A8 end

    def Function_3_2BE(): pass

    label("Function_3_2BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1")
    OP_8D(0xFE, -1720, 8440, 1470, 870, 2000)
    Jump("Function_3_2BE")

    label("loc_2E1")

    Return()

    # Function_3_2BE end

    def Function_4_2E2(): pass

    label("Function_4_2E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_663")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-2590, 0, 15070, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x102, -4040, 0, 13240, 0)
    SetChrPos(0x101, -3050, 0, 13440, 0)
    SetChrPos(0xF8, -3980, 0, 12140, 0)
    SetChrPos(0xF9, -2940, 0, 12340, 0)
    OP_8C(0xFE, 180, 0)
    OP_4A(0xFE, 255)
    OP_0D()

    ChrTalk(    #0
        0x8,
        (
            "#750F#5P艾丝蒂尔……\x01",
            "还有约修亚。\x02\x03",

            "#751F衷心欢迎你们到来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#1035F#6P院长老师……\x01",
            "……让您担心了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #2
        0x8,
        (
            "#750F#5P约修亚，今后请务必\x01",
            "待在艾丝蒂尔身边。\x02\x03",

            "#751F我的希望仅此而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        "#1054F#6P……是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1017F#4P特蕾莎老师……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#751F#5P呵呵，看来也没有\x01",
            "担心的必要呢。\x02\x03",

            "#750F科洛丝\x01",
            "想必也放心了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1004F#4P这么说来……#1150W #20W \x01",
            "#1015F老师，说到科洛丝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#754F#5P嗯嗯，好像在王都呢。\x02\x03",

            "#750F基库送来了\x01",
            "她的信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1016F#4P啊哈哈，这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#1049F#6P不愧是基库呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#754F#5P看起来科洛丝\x01",
            "也有不少麻烦呢。\x02\x03",

            "从字面上看来，似乎\x01",
            "已经下定决心面对\x01",
            "自己的烦恼了。\x02\x03",

            "#750F虽然我并不明白\x01",
            "那是怎样的决心……\x02\x03",

            "但相信那孩子\x01",
            "一定能找到自己的道路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1004F#4P特蕾莎老师……\x02\x03",

            "#1006F嗯，我也这么想！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x20B1)
    EventEnd(0x0)
    OP_4B(0xFE, 255)
    Jump("loc_8C8")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_78C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6F7")

    ChrTalk(    #12
        0x8,
        (
            "#757F科洛丝的信里，\x01",
            "表达出正视烦恼\x01",
            "的决心。\x02\x03",

            "#754F虽然我并不明白\x01",
            "那是怎样的决心……\x02\x03",

            "#750F但相信那孩子\x01",
            "一定能找到自己的道路。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_789")

    label("loc_6F7")


    ChrTalk(    #13
        0x8,
        (
            "#750F迫降飞艇上的士兵\x01",
            "似乎暂时在做警备。\x02\x03",

            "看起来很疲劳的样子，\x01",
            "我想待会儿\x01",
            "沏点草药茶给他们送去。\x02\x03",

            "#751F不介意的话，艾丝蒂尔你们\x01",
            "也随便用吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_789")

    Jump("loc_8C8")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_819")

    ChrTalk(    #14
        0x8,
        (
            "#757F科洛丝的信里，\x01",
            "表达出正视烦恼\x01",
            "的决心。\x02\x03",

            "#754F虽然我并不明白\x01",
            "那是怎样的决心……\x02\x03",

            "#750F但相信那孩子\x01",
            "一定能找到自己的道路。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C8")

    label("loc_819")


    ChrTalk(    #15
        0x8,
        (
            "#754F由于魔兽骚乱，\x01",
            "前几天都在玛诺利亚避难。\x02\x03",

            "#757F还以为总算可以回家了\x01",
            "却又马上发生了这种事……\x02\x03",

            "#750F不过，真不可思议啊。\x02\x03",

            "#751F只要孩子们露出笑脸\x01",
            "就感觉总会有办法的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C8")

    Jump("loc_AF7")

    label("loc_8CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_8D5")
    Jump("loc_AF7")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_9A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_932")

    ChrTalk(    #16
        0xFE,
        (
            "#751F孩子们也在衷心期待\x01",
            "考试结束呢。\x02\x03",

            "考试一结束，\x01",
            "科洛丝\x01",
            "又会来玩了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99F")

    label("loc_932")

    OP_A2(0x0)

    ChrTalk(    #17
        0x8,
        (
            "#750F学院的考试\x01",
            "也快结束了。\x02\x03",

            "孩子们也在衷心期待\x01",
            "考试结束呢。\x02\x03",

            "#751F考试一结束，\x01",
            "科洛丝\x01",
            "又会来玩了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99F")

    Jump("loc_AF7")

    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9F1")

    ChrTalk(    #18
        0x8,
        (
            "#751F在卢安的期间，\x01",
            "方便的话请再来吧。\x02\x03",

            "孩子们也在等待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A56")

    label("loc_9F1")

    OP_A2(0x0)

    ChrTalk(    #19
        0x8,
        (
            "#750F今天真是不好意思。\x02\x03",

            "还麻烦你们\x01",
            "去接孩子们……\x02\x03",

            "#751F方便的话请再来哦。\x01",
            "孩子们也在等待。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A56")

    Jump("loc_AF7")

    label("loc_A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_END)), "loc_AF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AB3")

    ChrTalk(    #20
        0x8,
        (
            "#750F玛诺利亚村在梅威海道\x01",
            "往西走的地方。\x02\x03",

            "那么，孩子们就\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF7")

    label("loc_AB3")

    OP_A2(0x0)

    ChrTalk(    #21
        0x8,
        (
            "#750F玛诺利亚村的\x01",
            "主日学校也快结束了。\x02\x03",

            "孩子们就\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF7")

    TalkEnd(0xFE)
    Return()

    # Function_4_2E2 end

    def Function_5_AFB(): pass

    label("Function_5_AFB")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0A")
    TurnDirection(0xFE, 0x102, 0)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #22
        0xFE,
        (
            "哇……\x01",
            "是约修亚哥哥！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1040F达尼艾尔……好久不见了呢。\x02\x03",

            "有乖乖听话吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "我也和克拉姆一样\x01",
            "在帮老师干活哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "今天也帮菜叶\x01",
            "浇水了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#1049F是吗……\x01",
            "达尼艾尔真了不起呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "嘿嘿……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x20ED)
    Jump("loc_E13")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_D72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C66")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #29
        0xFE,
        (
            "我也和克拉姆一样\x01",
            "在帮老师干活哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "今天也帮菜叶\x01",
            "浇水了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D6F")

    label("loc_C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D30")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #31
        0xFE,
        "对了，艾丝蒂尔姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1011F嗯？什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "姐姐\x01",
            "会做苹果派吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1015F唔，嗯～……\x02\x03",

            "#1007F对、对不起哦。\x01",
            "不太会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "嗯～是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "还是只能拜托\x01",
            "科洛丝姐姐了啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_D6F")

    label("loc_D30")


    ChrTalk(    #37
        0xFE,
        (
            "如果科洛丝姐姐来了\x01",
            "就要她做苹果派。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "姐姐做的最棒了～\x02",
    )

    CloseMessageWindow()

    label("loc_D6F")

    Jump("loc_E13")

    label("loc_D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DC7")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #39
        0xFE,
        (
            "我也和克拉姆一样\x01",
            "在帮老师干活哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "今天也给菜叶\x01",
            "浇水了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E13")

    label("loc_DC7")


    ChrTalk(    #41
        0xFE,
        (
            "最近的夜晚\x01",
            "真是一片漆黑啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "虽然星星是很漂亮\x01",
            "不过还是有点可怕呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E13")

    TalkEnd(0x10)
    Return()

    # Function_5_AFB end

    def Function_6_E17(): pass

    label("Function_6_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E28")
    Call(0, 8)

    label("loc_E28")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xF7, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x8, 1)
    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_E56")
    SetChrChipByIndex(0x103, 3)
    Jump("loc_E5B")

    label("loc_E56")

    SetChrChipByIndex(0x106, 4)

    label("loc_E5B")

    SetChrPos(0x101, -5240, 200, 7350, 90)
    SetChrPos(0xF7, -5240, 200, 6050, 90)
    SetChrPos(0x8, -2550, 200, 7350, 270)
    SetChrPos(0x9, -3710, 700, 6060, 0)
    SetChrPos(0xA, -4550, 700, 6860, 0)
    SetChrPos(0xB, -4530, 700, 6060, 0)
    SetChrPos(0xC, -3810, 700, 6860, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_6D(-3770, 100, 7530, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #43
        0x101,
        (
            "#1007F#6P唉……真难为情啊。\x02\x03",

            "难得想展示一下\x01",
            "成为正游击士的身姿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#751F呵呵，这么说来\x01",
            "你成为正游击士了呢。\x02\x03",

            "恭喜恭喜，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1016F#6P哪里，啊哈哈……\x01",
            "其实还是新手。\x02\x03",

            "#1026F啊，这么说来……\x02\x03",

            "老师刚才提到\x01",
            "科洛丝有烦恼？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#750F嗯嗯，是艾丝蒂尔\x01",
            "和约修亚的事。\x02\x03",

            "#754F重要的人感到痛苦，\x01",
            "自己却无法帮上忙……\x02\x03",

            "这对那孩子来说\x01",
            "大概是最难过的事了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1004F#6P重要的人……\x02\x03",

            "#1008F嘿嘿，虽然有点不好意思\x01",
            "但还是觉得很高兴……\x02\x03",

            "要早点去见见科洛丝才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#750F记得现在学院是考试期间，\x01",
            "可能进不去……\x02\x03",

            "应该很快就会结束了，\x01",
            "马上就能见面了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1017F#6P嗯，明白了。\x02\x03",

            "话虽如此……\x01",
            "孩子们还真慢呢。\x02\x03",

            "主日学校的授课\x01",
            "不会那么长吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#750F难道是下课以后\x01",
            "还留在村里玩了？\x02\x03",

            "听说新来的巡回神父\x01",
            "很喜欢小孩子的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1015F#6P新来的巡回神父……\x01",
            "（咦……好像在哪里听过？）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF7, 1)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_129C")

    ChrTalk(    #52
        0x106,
        (
            "#051F#4P那就去玛诺利亚村\x01",
            "确认一下情况吧。\x02\x03",

            "顺便把孩子们\x01",
            "送回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F2")

    label("loc_129C")


    ChrTalk(    #53
        0x103,
        (
            "#020F#4P那么，去玛诺利亚村\x01",
            "确认一下可能比较好吧。\x02\x03",

            "顺便把孩子们\x01",
            "送回这里就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F2")

    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(    #54
        0x101,
        "#1006F#3P啊，那倒也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        "#753F哎呀……可以吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(300)

    ChrTalk(    #56
        0x101,
        (
            "#1001F#6P嘿嘿。\x01",
            "请别介意。\x02\x03",

            "算是美味茶点的回礼吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13A5")

    ChrTalk(    #57
        0x106,
        (
            "#051F#4P还要回\x01",
            "受人安慰的礼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13CC")

    label("loc_13A5")


    ChrTalk(    #58
        0x103,
        (
            "#021F#4P还要回\x01",
            "被紧紧抱住的礼呢㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CC")

    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(    #59
        0x101,
        "#1013F#3P讨、讨厌……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#751F呵呵……\x02\x03",

            "#750F明白了。\x01",
            "那么就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x101, -3650, 0, 8410, 90)
    SetChrPos(0xF7, -3650, 0, 8410, 90)
    SetChrPos(0x8, -3700, 0, 14600, 0)
    OP_6D(-3650, 0, 8410, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_4B(0x8, 255)
    OP_A2(0x1216)
    OP_28(0x82, 0x2, 0x80)
    OP_28(0x82, 0x1, 0x100)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_E17 end

    def Function_7_14F5(): pass

    label("Function_7_14F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1506")
    Call(0, 8)

    label("loc_1506")

    EventBegin(0x0)
    OP_72(0x6, 0x4)
    OP_72(0x7, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xF7, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0xD, 11)
    SetChrChipByIndex(0xE, 12)
    SetChrChipByIndex(0xF, 13)
    SetChrChipByIndex(0x10, 14)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0x10, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF7, -5240, 200, 4750, 90)
    SetChrPos(0x10, -2550, 200, 4750, 0)
    SetChrPos(0x109, -3850, 200, 3900, 12)
    SetChrPos(0x8, -3930, 200, 8250, 180)
    SetChrPos(0xF, -5240, 200, 7350, 90)
    SetChrPos(0x101, -5240, 200, 6050, 90)
    SetChrPos(0xD, -2550, 200, 7350, 270)
    SetChrPos(0xE, -2550, 200, 6050, 270)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x109, 10)
    SetChrChipByIndex(0x8, 1)
    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1645")
    SetChrChipByIndex(0x103, 3)
    Jump("loc_164A")

    label("loc_1645")

    SetChrChipByIndex(0x106, 4)

    label("loc_164A")

    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #61
        0x8,
        (
            "#750F这样啊……\x02\x03",

            "神父和艾丝蒂尔\x01",
            "认识啊。\x02\x03",

            "#751F呵呵，世界真是小啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x109,
        (
            "#1061F呀～真是这么回事呢。\x02\x03",

            "#1062F话说回来，\x01",
            "还准备了我的午饭，\x01",
            "真是对老师不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#750F哪里哪里，反正是顺便做的，\x01",
            "你教孩子们学习\x01",
            "这是应该的谢礼。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    ChrTalk(    #64
        0xD,
        (
            "#775F对了，艾丝蒂尔姐姐。\x02\x03",

            "约修亚哥哥不在，\x01",
            "今天没一起来吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #65
        0x101,
        (
            "#1025F#6P啊，嗯……算是吧。\x02\x03",

            "他有点事，\x01",
            "没一起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x109,
        "#1067F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        "这样啊……好失望。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xD,
        (
            "#773F呜～还想让约修亚哥哥\x01",
            "也看看孤儿院\x01",
            "恢复原状的样子呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xF,
        "真是可惜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xE,
        (
            "#2P他当公主的样子\x01",
            "也想再看看呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1016F#6P啊、啊哈哈……\x02\x03",

            "#1011F话说回来，\x01",
            "主日学校课时真长啊。\x02\x03",

            "最后好像在读什么，\x01",
            "是小说吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xD,
        (
            "#770F哼哼。\x01",
            "叫做『人偶骑士』。\x02\x03",

            "是以人偶师的战斗为主题，\x01",
            "紧张刺激的动作剧哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    ChrTalk(    #73
        0xF,
        "啊，不对啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xF,
        (
            "不是以身份不同的恋爱为主题的\x01",
            "浪漫爱情故事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x109,
        (
            "#1068F来利贝尔时带来的\x01",
            "青少年向小说……\x02\x03",

            "本来只是打算\x01",
            "一点点读给他们听的，\x01",
            "一不小心就读了全卷……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(    #76
        0x101,
        (
            "#1016F#6P啊哈哈。\x01",
            "你就别抱怨了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#751F呵呵。\x01",
            "真是辛苦了。\x02\x03",

            "#750F神父大人今后\x01",
            "打算回卢安吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x109,
        (
            "#1062F嗯嗯，算是吧。\x02\x03",

            "还有其它的村子要巡回，\x01",
            "应该很快就要\x01",
            "上定期船了。\x02\x03",

            "#1060F这么说来，艾丝蒂尔\x01",
            "怎么会在卢安地区？\x02\x03",

            "还是游击士的工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1006F#6P嗯，发生了不少事。\x02\x03",

            "#1004F对了，我们\x01",
            "来孤儿院是想\x01",
            "打听一件事的……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(300)

    ChrTalk(    #80
        0x8,
        (
            "#750F是波利见到的\x01",
            "『白衣叔叔』吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #81
        0xD,
        "#770F啊～那件事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xE,
        (
            "#2P嗯～？\x01",
            "波利怎么了？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)

    ChrTalk(    #83
        0x101,
        (
            "#1011F#6P嗯，有点事\x01",
            "想要打听一下……\x02\x03",

            "『白衣叔叔』的事\x01",
            "能不能详细告诉我们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xE,
        (
            "#2P白衣叔叔\x01",
            "就是白衣叔叔嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xE,
        (
            "#2P骨碌骨碌地转着圈，\x01",
            "看起来很快乐的样子～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #86
        0x101,
        "#1016F#6P嗯……不是很明白呢。\x02",
    )

    CloseMessageWindow()
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    ChrTalk(    #87
        0xF,
        (
            "嗯，让我\x01",
            "来说明吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xF,
        "那是４天前……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xF,
        (
            "这孩子晚饭之后\x01",
            "跑去外边发呆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xF,
        (
            "然后天上好像\x01",
            "浮现出一个白色的男子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xE,
        "#2P是啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        (
            "#2P很高兴的飞来跳去，\x01",
            "在天空骨碌骨碌地跳着舞～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xE,
        (
            "#2P波利一跟他说话\x01",
            "他就鞠躬行了个礼，\x01",
            "然后就飞走了～\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    ChrTalk(    #94
        0xD,
        (
            "#772F我看啊～\x01",
            "只是你睡迷糊了而已。\x02\x03",

            "如果说是幽灵的话\x01",
            "完全不可怕嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "#754F我一开始也是这么想，\x01",
            "但是达尼艾尔好像也看到了。\x02\x03",

            "#750F对吧，达尼艾尔？\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    ChrTalk(    #96
        0x10,
        (
            "嗯。\x01",
            "我只看到一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x10,
        (
            "白色的奇怪影子，往东边\x01",
            "咻的一下就飞走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1007F#6P嗯、嗯～\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1F61")

    ChrTalk(    #99
        0x106,
        (
            "#552F有两个目击者，\x01",
            "可信性似乎就很高了。\x02\x03",

            "#053F不过，一搭话\x01",
            "就行礼吗……\x02\x03",

            "#051F那个白衣叔叔，\x01",
            "看到他长什么样子了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FE7")

    label("loc_1F61")


    ChrTalk(    #100
        0x103,
        (
            "#522F目击者有两个，\x01",
            "可信度就变高了呢。\x02\x03",

            "#026F话说回来，一搭话\x01",
            "就行了个礼啊……\x02\x03",

            "#020F对了，那个白衣叔叔，\x01",
            "看到他长什么样子了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE7")


    ChrTalk(    #101
        0xE,
        "#2P脸没看到～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xE,
        (
            "#2P因为叔叔\x01",
            "戴着奇怪的面具。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #103
        0x101,
        "#1004F#6P面、面具！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_209A")

    ChrTalk(    #104
        0x106,
        (
            "#055F这实在是……\x01",
            "奇怪的幽灵啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C4")

    label("loc_209A")


    ChrTalk(    #105
        0x103,
        (
            "#023F怎么说呢……\x01",
            "相当诡异的幽灵啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C4")


    ChrTalk(    #106
        0xD,
        (
            "#775F我说啊，波利。\x01",
            "这种事你早说啊。\x02\x03",

            "我可是第一次听到呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xE,
        (
            "#2P但是谁也\x01",
            "没问过我嘛～\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 2)
    Sleep(400)

    ChrTalk(    #108
        0x8,
        (
            "#750F嗯，面具暂且不管，\x01",
            "看来好像不是梦……\x02\x03",

            "慎重起见，我还是通知了\x01",
            "游击士协会。\x02\x03",

            "从那以后，虽然多加注意，\x01",
            "但好像没有再次出现。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #109
        0x101,
        "#1015F#6P嗯、嗯……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF7, 1)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_220F")

    ChrTalk(    #110
        0x106,
        (
            "#051F大致上明白了。\x01",
            "得了不少参考。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223F")

    label("loc_220F")


    ChrTalk(    #111
        0x103,
        (
            "#021F情况明白了。\x01",
            "应该算是掌握了不少信息。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_14F5 end

    def Function_8_225C(): pass

    label("Function_8_225C")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22D6"),
        (1, "loc_22DC"),
        (SWITCH_DEFAULT, "loc_22E2"),
    )


    label("loc_22D6")

    OP_A2(0x1200)
    Jump("loc_22E2")

    label("loc_22DC")

    OP_A2(0x1201)
    Jump("loc_22E2")

    label("loc_22E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_22F0")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_22F4")

    label("loc_22F0")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_22F4")

    Return()

    # Function_8_225C end

    SaveToFile()

Try(main)
